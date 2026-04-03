# Contributing to HikerAPI Documentation

## Local Development

```bash
# Install dependencies
uv pip install mkdocs-material neoteroi-mkdocs

# Start dev server
.venv/bin/mkdocs serve -a localhost:8002

# Build (check for errors)
.venv/bin/mkdocs build --strict
```

## Updating API endpoints (OpenAPI spec changed)

When new endpoints are added or existing ones change:

```bash
# 1. Download fresh spec
curl -s https://api.hikerapi.com/openapi.json | python3 -m json.tool > docs/openapi.json

# 2. Regenerate per-resource spec files
python3 scripts/split_openapi.py

# 3. Check if new resources appeared — may need new .md pages in docs/api-reference/
# 4. Verify
.venv/bin/mkdocs build --strict

# 5. Commit + push
git add docs/openapi.json docs/openapi/ docs/api-reference/
git commit -m "docs: update API spec"
git push
```

RTD rebuilds automatically on push to master.

## Updating content (text, examples, CTA)

Edit the `.md` file directly, commit, push. RTD rebuilds automatically.

## File structure

```
mkdocs.yml                    # MkDocs config (theme, nav, plugins)
.readthedocs.yaml             # RTD build config
docs/
  index.md                    # Home page
  openapi.json                # Full OpenAPI spec (source of truth)
  openapi/                    # Split specs per resource (auto-generated)
    v1-user.json
    v1-media.json
    ...
  api-reference/
    v1/                       # REST v1 pages per resource
    v2/                       # REST v2 pages per resource
    gql/                      # GraphQL pages
    response-codes.md
  getting-started/
  sdk/
  guides/
  support/
  overrides/                  # Material theme overrides (announcement bar, CSS)
scripts/
  split_openapi.py            # Splits openapi.json into per-resource files
```

## Promo links

All links to hikerapi.com use promo code `7it8oc2i` with UTM tracking:

```
https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=<placement>
```

See `pm-sync.md` Task 23 for the full UTM content mapping.

## Dependencies (for RTD)

Listed in `docs/requirements.txt`:
- `mkdocs-material` — theme
- `neoteroi-mkdocs` — OpenAPI renderer (replaces Swagger UI)
