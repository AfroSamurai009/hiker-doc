# HikerAPI Documentation Rebrand — Design Spec

## Goal

Rebrand HikerAPI documentation to increase conversion to signup/free trial.
Migration from Sphinx + RST to MkDocs Material + Markdown, staying on Read the Docs.

## Target Audience

Primary: developers evaluating Instagram API solutions (arrive via search/RTD).
Secondary: agencies/businesses — devs act as internal advocates ("let's use this").

## Conversion Funnel

```
Reads docs → Tries examples → Signs up for free trial → Paid plan
```

Future addition: API Playground (see net/hikerapi#184) inserts between "reads docs" and "signs up".

## Tech Stack

| Component | Solution |
|---|---|
| Generator | MkDocs + Material for MkDocs theme |
| Format | Markdown (replacing RST) |
| API Reference | OpenAPI render + language tabs (Python, JS, Go, PHP, curl) |
| Hosting | Read the Docs (unchanged) |
| Search | Material built-in search |
| Dark mode | Material theme toggle |
| Colors | Indigo/blue matching hikerapi.com branding |

## Site Structure

```
HikerAPI Documentation
├── Home (mini-landing with CTA)
├── Getting Started
│   ├── Quick Start (5 min to first request)
│   └── Authentication
├── API Reference
│   ├── REST API v1
│   ├── REST API v2
│   ├── GraphQL API
│   └── Response Codes
├── SDK
│   ├── Python
│   ├── JavaScript
│   ├── Go
│   └── PHP
├── Guides
│   ├── Rate Limits & Retry Logic
│   └── Request Costs
└── Support
    └── Contacts
```

## API Reference Approach

Stripe-style: each endpoint documented with language tabs showing SDK usage.

```
GET /v1/user/by/username

  Python:    client.user_by_username_v1("ronaldo")
  Node.js:   client.v1.userByUsername("ronaldo")
  curl:      curl -H "x-access-key: ..." .../v1/user/by/username?username=ronaldo
```

Source: openapi.json rendered directly. No intermediate Python stubs.

### Update Pipeline

**Current (broken):**
```
openapi.json → gen.py → _build/ → (manual copy) → hikerapi-py/ → (manual copy) → hiker-doc/docs/hikerapi/ → Sphinx autodoc
```

**New:**
```
openapi.json → hiker-doc/docs/ → MkDocs renders directly
```

SDK tab examples maintained manually (1 line per language per endpoint).

## CTA Elements

1. **Announcement bar** — fixed top banner on every page: "Get 100 free requests → Sign up" with button
2. **Hero on Home** — headline + value prop + "Start Free Trial" button + "View API Reference" button
3. **Code examples with responses** — Getting Started shows request AND real JSON response
4. **CTA after API Reference** — bottom of endpoint pages: "Ready to integrate? Get your API key →"
5. **Pricing hint** — in Rate Limits section: "Starting at $0.001/request. See pricing →"
6. **Trust signals** — on Home: "10,000+ developers", "147 endpoints", "99.9% uptime"

## SDK Documentation

No full autodoc of 116+ methods. Each SDK gets a guide page:
- Installation
- Initialization (auth)
- 5-7 key usage examples
- Link to API Reference ("methods map 1:1 to endpoints")

## Branding

- Primary color: indigo/blue (matching hikerapi.com)
- Light/dark theme toggle
- Clean, minimal, developer-friendly
- No strict brand guidelines — align with hikerapi.com visually

## Migration Scope

### Content to migrate (RST → MD)

| Current RST | New MD | Notes |
|---|---|---|
| index.rst | index.md | Rewrite as mini-landing with CTA |
| gettingstarted.rst | getting-started/quick-start.md | Expand with better examples |
| gettingstarted.rst (auth part) | getting-started/authentication.md | Split out |
| python.rst | sdk/python.md | Rewrite as guide, drop autodoc |
| v1.rst | api-reference/v1.md | Replace with OpenAPI render |
| gql.rst | api-reference/graphql.md | Replace with OpenAPI render |
| response_codes.rst | api-reference/response-codes.md | Convert to MD table |
| timeoutinfo.rst | guides/rate-limits.md | Convert + add CTA |
| requests_info.rst | guides/request-costs.md | Convert + add CTA |
| contacts.rst | support/contacts.md | Convert |

### New pages

- Home (index.md) — mini-landing
- getting-started/authentication.md — split from getting started
- sdk/javascript.md — new
- sdk/go.md — new
- sdk/php.md — new

### Files to remove after migration

- docs/source/ (all RST files + conf.py)
- docs/hikerapi/ (Python stubs for autodoc — no longer needed)
- docs/build/ (Sphinx build artifacts)

### Config changes

- mkdocs.yml — full Material config
- .readthedocs.yaml — switch from sphinx to mkdocs
- docs/requirements.txt — replace sphinx deps with mkdocs deps

## Local Development

```bash
pip install mkdocs-material
mkdocs serve
# Opens http://localhost:8000 with hot reload
```

Deploy to RTD only when satisfied with local result.

## Out of Scope

- API Playground (separate ticket: net/hikerapi#184)
- OpenAPI spec updates (done in gen repo)
- SDK code changes (done in respective SDK repos)
