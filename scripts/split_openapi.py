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
    "v1-search.json": ["/v1/search/", "/v1/fbsearch/", "/v1/share/"],
}

V2_RESOURCES = {
    "v2-user.json": ["/v2/user/", "/a2/user", "/v2/userstream/"],
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


def _is_api_key_header(param):
    """Check if param is the APIKeyHeader security param."""
    is_key = param.get("name") == "APIKeyHeader"
    return is_key and param.get("in") == "header"


def clean_spec(spec):
    """Remove noise from spec: APIKeyHeader, response schemas, metadata."""
    # Remove info noise
    for key in ("termsOfService", "license", "x-logo"):
        spec.get("info", {}).pop(key, None)

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

            # Remove security references (auth is described separately)
            operation.pop("security", None)

            # Remove response schemas (keep status codes but clear schema)
            for status, resp in operation.get("responses", {}).items():
                content = resp.get("content", {})
                for media_type, media in content.items():
                    media.pop("schema", None)

    # Remove components if present (no longer referenced)
    spec.pop("components", None)

    return spec


def split_to_files(spec, resources, out_dir):
    """Split spec by resource prefixes and write cleaned files."""
    for filename, prefixes in resources.items():
        out = copy.deepcopy(spec)
        out["paths"] = {
            path: ops
            for path, ops in spec["paths"].items()
            if any(path.startswith(p) for p in prefixes)
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
    split_to_files(spec, V1_RESOURCES, OUT_DIR)

    print("v2 resources:")
    split_to_files(spec, V2_RESOURCES, OUT_DIR)

    print("gql:")
    split_to_files(spec, GQL_RESOURCES, OUT_DIR)


if __name__ == "__main__":
    main()
