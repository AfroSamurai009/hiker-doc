#!/usr/bin/env python3
"""Split openapi.json into per-resource specs for docs."""

import json
import copy
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
SOURCE = DOCS_DIR / "openapi.json"
OUT_DIR = DOCS_DIR / "openapi"

# Resource splits: filename -> list of path prefixes
V1_RESOURCES = {
    "v1-user.json": ["/v1/user/"],
    "v1-media.json": ["/v1/media/"],
    "v1-stories.json": ["/v1/story/", "/v1/user/stories"],
    "v1-highlights.json": ["/v1/highlight/", "/v1/user/highlights"],
    "v1-hashtags.json": ["/v1/hashtag/"],
    "v1-locations.json": ["/v1/location/"],
    "v1-search.json": [
        "/v1/search/",
        "/v1/fbsearch/",
        "/v1/share/",
    ],
}

V2_RESOURCES = {
    "v2-user.json": [
        "/v2/user/",
        "/a2/user",
        "/v2/userstream/",
    ],
    "v2-media.json": ["/v2/media/"],
    "v2-stories.json": ["/v2/story/"],
    "v2-highlights.json": ["/v2/highlight/"],
    "v2-hashtags.json": ["/v2/hashtag/"],
    "v2-search.json": ["/v2/search/", "/v2/fbsearch/"],
    "v2-locations.json": ["/v2/location/"],
    "v2-track.json": ["/v2/track/", "/v3/"],
}

GQL_RESOURCES = {
    "gql.json": ["/gql/", "/g2/"],
}

SYS_RESOURCES = {
    "sys.json": ["/sys/"],
}

# Paths to exclude from v1-user (they belong in stories/highlights)
V1_USER_EXCLUDE = {
    "v1-user.json": ["/v1/user/stories", "/v1/user/highlights"],
}

# Response description patterns (order matters — first match wins)
RESPONSE_DESCRIPTIONS = [
    ("/user/by/username", "Returns a User object."),
    ("/user/by/id", "Returns a User object."),
    ("/user/by/url", "Returns a User object."),
    ("/user/about", "Returns user about info."),
    ("/user/followers", "Returns a list of User objects."),
    ("/user/following", "Returns a list of User objects."),
    ("/user/medias", "Returns a list of Media objects."),
    ("/user/clips", "Returns a list of Media objects (Reels)."),
    ("/user/stories", "Returns a list of Story objects."),
    ("/user/highlights", "Returns a list of Highlight objects."),
    ("/user/search", "Returns matching User objects."),
    ("/user/tagged", "Returns a list of Media objects."),
    ("/user/guide", "Returns guide data."),
    ("/user/explore", "Returns recommended accounts."),
    ("/userstream/", "Returns user stream data."),
    ("/media/by/", "Returns a Media object."),
    ("/media/comments", "Returns a list of Comment objects."),
    ("/media/likers", "Returns a list of User objects."),
    ("/media/related", "Returns a list of related Media objects."),
    ("/story/by/", "Returns a Story object."),
    ("/story/download", "Returns story download data."),
    ("/story/viewers", "Returns a list of User objects."),
    ("/highlight/by/", "Returns a Highlight object."),
    ("/hashtag/by/", "Returns a Hashtag object."),
    ("/hashtag/medias", "Returns a list of Media objects."),
    ("/location/medias", "Returns a list of Media objects."),
    ("/location/by/", "Returns a Location object."),
    ("/location/guide", "Returns location guide data."),
    ("/search/", "Returns a list of matching results."),
    ("/fbsearch/", "Returns a list of matching results."),
    ("/share/", "Returns shared content data."),
    ("/track/", "Returns audio track data."),
    ("/comments/chunk", "Returns Comment objects with cursor."),
    ("/followers/chunk", "Returns User objects with cursor."),
    ("/following/chunk", "Returns User objects with cursor."),
]


def _is_api_key_header(param):
    """Check if param is the APIKeyHeader security param."""
    is_key = param.get("name") == "APIKeyHeader"
    return is_key and param.get("in") == "header"


def _get_response_desc(path):
    """Get response description based on path pattern."""
    for pattern, desc in RESPONSE_DESCRIPTIONS:
        if pattern in path:
            return desc
    return None


def clean_spec(spec):
    """Remove noise and enhance endpoint descriptions."""
    # Minimize info block
    spec["info"] = {"title": "", "version": ""}

    # Remove servers
    spec.pop("servers", None)

    # Clean each endpoint
    for path, methods in spec.get("paths", {}).items():
        for method, operation in methods.items():
            if not isinstance(operation, dict):
                continue

            # Remove APIKeyHeader from parameters
            if "parameters" in operation:
                params = operation["parameters"]
                params = [p for p in params if not _is_api_key_header(p)]
                if params:
                    operation["parameters"] = params
                else:
                    del operation["parameters"]

            # Remove security references
            operation.pop("security", None)

            # Clean responses: keep 200 with real schema, drop empty
            responses = operation.get("responses", {})
            cleaned_responses = {}
            for code, resp in responses.items():
                schema = (
                    resp.get("content", {})
                    .get("application/json", {})
                    .get("schema", {})
                )
                if schema:
                    cleaned_responses[code] = resp
            if cleaned_responses:
                operation["responses"] = cleaned_responses
            else:
                operation.pop("responses", None)

            # Add response description
            resp_desc = _get_response_desc(path)
            if resp_desc:
                existing = operation.get("description", "")
                if existing:
                    sep = "" if existing.endswith(".") else "."
                    operation["description"] = f"{existing}{sep} {resp_desc}"
                else:
                    operation["description"] = resp_desc

    # Remove tags and externalDocs
    spec.pop("tags", None)
    spec.pop("externalDocs", None)
    for methods in spec.get("paths", {}).values():
        for op in methods.values():
            if isinstance(op, dict):
                op.pop("externalDocs", None)
                op.pop("tags", None)

    # Keep only referenced components (schemas used by $ref)
    _prune_components(spec)

    return spec


def _collect_refs(obj):
    """Recursively collect all $ref values from a JSON structure."""
    refs = set()
    if isinstance(obj, dict):
        if "$ref" in obj:
            refs.add(obj["$ref"])
        for v in obj.values():
            refs |= _collect_refs(v)
    elif isinstance(obj, list):
        for item in obj:
            refs |= _collect_refs(item)
    return refs


def _prune_components(spec):
    """Keep only components/schemas that are referenced by paths."""
    all_schemas = spec.get("components", {}).get("schemas", {})
    if not all_schemas:
        spec.pop("components", None)
        return

    # Collect all $refs from paths, then resolve transitive refs
    refs = _collect_refs(spec.get("paths", {}))
    needed = set()
    for ref in refs:
        if ref.startswith("#/components/schemas/"):
            needed.add(ref.split("/")[-1])

    # Resolve transitive: schemas that reference other schemas
    changed = True
    while changed:
        changed = False
        for name in list(needed):
            if name in all_schemas:
                sub_refs = _collect_refs(all_schemas[name])
                for ref in sub_refs:
                    if ref.startswith("#/components/schemas/"):
                        sub_name = ref.split("/")[-1]
                        if sub_name not in needed:
                            needed.add(sub_name)
                            changed = True

    if needed:
        pruned = {k: v for k, v in all_schemas.items() if k in needed}
        spec["components"] = {"schemas": pruned}
    else:
        spec.pop("components", None)


def split_to_files(spec, resources, out_dir, exclude=None):
    """Split spec by resource prefixes and write cleaned files."""
    exclude = exclude or {}
    for filename, prefixes in resources.items():
        excl = exclude.get(filename, [])
        out = copy.deepcopy(spec)
        out["paths"] = {
            path: ops
            for path, ops in spec["paths"].items()
            if any(path.startswith(p) for p in prefixes)
            and not any(path.startswith(e) for e in excl)
        }
        if not out["paths"]:
            continue
        out = clean_spec(out)
        dest = out_dir / filename
        with open(dest, "w") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
        print(f"  {filename}: {len(out['paths'])} endpoints")


def main():
    OUT_DIR.mkdir(exist_ok=True)

    with open(SOURCE) as f:
        spec = json.load(f)

    print("v1 resources:")
    split_to_files(spec, V1_RESOURCES, OUT_DIR, exclude=V1_USER_EXCLUDE)

    print("v2 resources:")
    split_to_files(spec, V2_RESOURCES, OUT_DIR)

    print("gql:")
    split_to_files(spec, GQL_RESOURCES, OUT_DIR)

    print("sys:")
    split_to_files(spec, SYS_RESOURCES, OUT_DIR)


if __name__ == "__main__":
    main()
