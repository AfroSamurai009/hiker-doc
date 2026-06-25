"""MkDocs build hook: keep the advertised endpoint count in sync with the spec.

Replaces every ``{{ endpoint_count }}`` placeholder with the number of paths in
``docs/openapi.json``, computed once at build time. No manual edits, no drift —
the count updates automatically on every build (including ReadTheDocs).
"""

import json
from pathlib import Path

PLACEHOLDER = "{{ endpoint_count }}"
_count = None


def _endpoint_count(config) -> int:
    global _count
    if _count is None:
        spec = Path(config["docs_dir"]) / "openapi.json"
        _count = len(json.loads(spec.read_text()).get("paths", {}))
    return _count


def on_page_markdown(markdown, page, config, files):
    if PLACEHOLDER not in markdown:
        return markdown
    return markdown.replace(PLACEHOLDER, str(_endpoint_count(config)))
