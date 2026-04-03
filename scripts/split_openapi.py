#!/usr/bin/env python3
"""Split openapi.json into per-version specs for docs."""

import json
import copy
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
SOURCE = DOCS_DIR / "openapi.json"

SPLITS = {
    "openapi-v1.json": ["/v1/"],
    "openapi-v2.json": ["/v2/", "/v3/", "/a2/"],
    "openapi-gql.json": ["/gql/", "/g2/"],
}


def split():
    with open(SOURCE) as f:
        spec = json.load(f)

    for filename, prefixes in SPLITS.items():
        out = copy.deepcopy(spec)
        out["paths"] = {
            path: ops
            for path, ops in spec["paths"].items()
            if any(path.startswith(p) for p in prefixes)
        }
        dest = DOCS_DIR / filename
        with open(dest, "w") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
        print(f"{filename}: {len(out['paths'])} endpoints")


if __name__ == "__main__":
    split()
