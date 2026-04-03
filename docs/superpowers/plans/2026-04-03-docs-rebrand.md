# HikerAPI Documentation Rebrand — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate HikerAPI docs from Sphinx+RST to MkDocs Material+Markdown with CTA elements to increase conversion to free trial signup.

**Architecture:** MkDocs with Material theme renders Markdown pages + OpenAPI spec via swagger-ui-tag plugin. Hosted on Read the Docs. CTA elements via Material announcement bar and custom HTML blocks. API Reference rendered directly from openapi.json (no intermediate Python stubs).

**Tech Stack:** MkDocs, mkdocs-material, mkdocs-swagger-ui-tag, Read the Docs

**Design spec:** `docs/superpowers/specs/2026-04-03-docs-rebrand-design.md`

**GitLab epic:** net/hikerapi#185

---

### Task 1: MkDocs Material setup + base config

**Files:**
- Modify: `mkdocs.yml` (currently just `site_name: My Docs`)
- Modify: `docs/requirements.txt` (currently has sphinx deps)
- Modify: `.readthedocs.yaml` (currently points to sphinx)
- Create: `docs/index.md` (placeholder to verify build)

- [ ] **Step 1: Install MkDocs Material locally**

```bash
uv pip install mkdocs-material mkdocs-swagger-ui-tag
```

- [ ] **Step 2: Write mkdocs.yml**

Replace the contents of `mkdocs.yml` with:

```yaml
site_name: HikerAPI Documentation
site_url: https://hikerapi.readthedocs.io/
site_description: Instagram Data API — profiles, posts, stories, reels, comments, followers, hashtags, locations

theme:
  name: material
  custom_dir: docs/overrides
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
    - content.tabs.link
    - content.code.copy
    - announce.dismiss
  icon:
    logo: material/api

plugins:
  - search
  - swagger-ui-tag:
      docExpansion: list
      syntaxHighlightTheme: monokai
      tryItOutEnabled: false

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - tables
  - attr_list
  - md_in_html

nav:
  - Home: index.md

extra:
  social:
    - icon: fontawesome/brands/telegram
      link: https://t.me/hikerapi
  generator: false
```

- [ ] **Step 3: Write placeholder index.md**

Create `docs/index.md` with minimal content:

```markdown
# HikerAPI Documentation

Welcome to HikerAPI — Instagram Data API for Developers.
```

- [ ] **Step 4: Create overrides directory**

```bash
mkdir -p docs/overrides
```

Create empty `docs/overrides/.gitkeep`:

```
```

- [ ] **Step 5: Update docs/requirements.txt**

Replace contents of `docs/requirements.txt`:

```
mkdocs-material>=9.5
mkdocs-swagger-ui-tag>=0.6
```

- [ ] **Step 6: Update .readthedocs.yaml**

Replace contents of `.readthedocs.yaml`:

```yaml
version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.12"

python:
  install:
    - requirements: docs/requirements.txt

mkdocs:
  configuration: mkdocs.yml
```

- [ ] **Step 7: Verify local build**

```bash
cd /Users/vasil/work/hiker-doc && mkdocs serve
```

Open http://localhost:8000 — should see Material theme with "HikerAPI Documentation" heading and dark/light toggle. Stop server with Ctrl+C.

- [ ] **Step 8: Commit**

```bash
git add mkdocs.yml docs/requirements.txt .readthedocs.yaml docs/index.md docs/overrides/
git commit -m "feat: setup MkDocs Material base config

Replace Sphinx with MkDocs Material theme. Configure RTD for mkdocs build.
Refs net/hikerapi#185"
```

---

### Task 2: Home page — mini-landing with CTA

**Files:**
- Modify: `docs/index.md`

- [ ] **Step 1: Write home page**

Replace `docs/index.md` with:

```markdown
---
hide:
  - navigation
  - toc
---

# Instagram Data API for Developers

Access public Instagram profiles, posts, stories, reels, comments, followers, hashtags, and locations through one developer-friendly REST API.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Quick Start**

    ---

    Make your first API request in 5 minutes

    [:octicons-arrow-right-24: Get started](getting-started/quick-start.md)

-   :material-api:{ .lg .middle } **API Reference**

    ---

    147 endpoints — REST v1, v2, and GraphQL

    [:octicons-arrow-right-24: Explore endpoints](api-reference/rest-v1.md)

-   :material-language-python:{ .lg .middle } **SDKs**

    ---

    Official clients for Python, JavaScript, Go, and PHP

    [:octicons-arrow-right-24: View SDKs](sdk/python.md)

-   :material-currency-usd:{ .lg .middle } **Pricing**

    ---

    Starting at $0.001/request. 100 free requests on signup.

    [:octicons-arrow-right-24: Start free trial](https://hikerapi.com/p/7it8oc2i){ target=_blank }

</div>

## Why HikerAPI?

| | |
|---|---|
| **10,000+ developers** | Trusted worldwide for Instagram data extraction |
| **147 endpoints** | REST v1/v2, GraphQL, and Facebook Search APIs |
| **4-5M requests/day** | Battle-tested infrastructure, 300+ req/sec capacity |
| **No rate limits** | No blocks, no OAuth required, anonymous access |
| **$0.001/request** | Pay only for what you use. Free trial available |

---

<div class="cta-box" markdown>

**Ready to start?** Get 100 free requests after signup — no credit card required.

[Start Free Trial](https://hikerapi.com/p/7it8oc2i){ .md-button .md-button--primary target=_blank }
[View API Reference](api-reference/rest-v1.md){ .md-button }

</div>
```

- [ ] **Step 2: Add custom CSS for CTA box**

Create `docs/overrides/extra.css`:

```css
.cta-box {
  background: var(--md-primary-fg-color--light);
  padding: 1.5rem 2rem;
  border-radius: 0.5rem;
  text-align: center;
  margin: 2rem 0;
}

[data-md-color-scheme="slate"] .cta-box {
  background: var(--md-default-fg-color--lightest);
}
```

- [ ] **Step 3: Reference CSS in mkdocs.yml**

Add to `mkdocs.yml` at root level (after `extra:` section):

```yaml
extra_css:
  - overrides/extra.css
```

- [ ] **Step 4: Verify locally**

```bash
mkdocs serve
```

Check http://localhost:8000 — should see grid cards, trust signals table, CTA box with buttons. Verify dark/light toggle works with CTA box.

- [ ] **Step 5: Commit**

```bash
git add docs/index.md docs/overrides/extra.css mkdocs.yml
git commit -m "feat: add home page with CTA and trust signals

Mini-landing with grid cards, value props, and signup CTA.
Refs net/hikerapi#185"
```

---

### Task 3: Announcement bar

**Files:**
- Create: `docs/overrides/main.html`

- [ ] **Step 1: Create announcement bar template**

Create `docs/overrides/main.html`:

```html
{% extends "base.html" %}

{% block announce %}
<style>
  .announce-cta {
    color: inherit;
    font-weight: 600;
    border-bottom: 1px solid currentColor;
  }
  .announce-cta:hover {
    opacity: 0.8;
  }
</style>
Get 100 free requests —
<a href="https://hikerapi.com/p/7it8oc2i" target="_blank" class="announce-cta">
  Start your free trial &rarr;
</a>
{% endblock %}
```

- [ ] **Step 2: Verify locally**

```bash
mkdocs serve
```

Check http://localhost:8000 — blue announcement bar at top of every page with dismissible "X". Navigate to different pages to verify it persists.

- [ ] **Step 3: Commit**

```bash
git add docs/overrides/main.html
git commit -m "feat: add announcement bar with free trial CTA

Dismissible banner on all pages linking to signup.
Refs net/hikerapi#185"
```

---

### Task 4: Getting Started pages

**Files:**
- Create: `docs/getting-started/quick-start.md`
- Create: `docs/getting-started/authentication.md`
- Modify: `mkdocs.yml` (update nav)

- [ ] **Step 1: Create getting-started directory**

```bash
mkdir -p docs/getting-started
```

- [ ] **Step 2: Write Quick Start page**

Create `docs/getting-started/quick-start.md`:

```markdown
# Quick Start

Make your first HikerAPI request in 5 minutes.

## 1. Get your API key

[Sign up at hikerapi.com](https://hikerapi.com/p/7it8oc2i){ target=_blank } and grab your token from the [dashboard](https://hikerapi.com/tokens){ target=_blank }.

## 2. Make a request

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/username?username=ronaldo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    user = cl.user_by_username_v1("ronaldo")
    print(user)
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN", "accept": "application/json"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/by/username",
        headers=headers,
        params={"username": "ronaldo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/by/username?username=ronaldo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const user = await response.json();
    console.log(user);
    ```

## 3. Example response

```json
{
  "pk": "173560420",
  "username": "ronaldo",
  "full_name": "Cristiano Ronaldo",
  "is_private": false,
  "is_verified": true,
  "media_count": 3789,
  "follower_count": 612000000,
  "following_count": 582,
  "biography": "..."
}
```

## 4. Paginate through followers

Most list endpoints return paginated results. Use `end_cursor` to get the next page:

=== "Python SDK"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")

    followers = {}
    end_cursor = None

    while True:
        chunk, end_cursor = cl.user_followers_chunk_gql(
            user_id="173560420", end_cursor=end_cursor
        )
        followers.update({u["pk"]: u for u in chunk})
        if not end_cursor:
            break

    print(f"Got {len(followers)} followers")
    ```

=== "curl"

    ```bash
    # First page
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/followers/chunk?user_id=173560420"

    # Next page — use end_cursor from previous response
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/followers/chunk?user_id=173560420&end_cursor=QVFB..."
    ```

## 5. Export to CSV

```python
import csv
from hikerapi import Client

cl = Client(token="YOUR_TOKEN")
user_ids = ["173560420", "12345678"]

with open("users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "pk", "username", "full_name", "is_private",
        "is_verified", "follower_count", "following_count",
    ])
    writer.writeheader()
    for uid in user_ids:
        user = cl.user_by_id_v1(uid)
        writer.writerow({k: user.get(k) for k in writer.fieldnames})
```

---

!!! tip "What's next?"
    - Browse the [API Reference](../api-reference/rest-v1.md) for all 147 endpoints
    - Check [Rate Limits](../guides/rate-limits.md) to optimize your integration
    - See [SDKs](../sdk/python.md) for language-specific clients
```

- [ ] **Step 3: Write Authentication page**

Create `docs/getting-started/authentication.md`:

```markdown
# Authentication

All HikerAPI requests require an API key passed via the `x-access-key` header.

## Get your API key

1. [Sign up at hikerapi.com](https://hikerapi.com/p/7it8oc2i){ target=_blank }
2. Confirm via Telegram
3. Get your token from the [dashboard](https://hikerapi.com/tokens){ target=_blank }

## Usage

=== "Header (recommended)"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/username?username=ronaldo"
    ```

=== "Python SDK"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    ```

=== "JavaScript"

    ```javascript
    const headers = { "x-access-key": "YOUR_TOKEN" };
    ```

## Free trial

After signup you get **100 free requests** to test the API. No credit card required.

## Check your balance

```bash
curl -H "x-access-key: YOUR_TOKEN" \
  "https://api.hikerapi.com/sys/balance"
```

Response:

```json
{
  "balance": 99.94,
  "rate": 11
}
```

- `balance` — remaining request units
- `rate` — your current rate limit (requests/second)
```

- [ ] **Step 4: Update nav in mkdocs.yml**

Replace the `nav:` section in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Quick Start: getting-started/quick-start.md
    - Authentication: getting-started/authentication.md
```

- [ ] **Step 5: Verify locally**

```bash
mkdocs serve
```

Check:
- Navigation tabs show "Home" and "Getting Started"
- Quick Start page has working language tabs (curl/Python/JavaScript)
- Links between pages work
- Code blocks have copy buttons

- [ ] **Step 6: Commit**

```bash
git add docs/getting-started/ mkdocs.yml
git commit -m "feat: add Getting Started pages with multi-language examples

Quick Start with 5-step guide and Authentication page.
Refs net/hikerapi#185"
```

---

### Task 5: API Reference — OpenAPI render

**Files:**
- Create: `docs/api-reference/rest-v1.md`
- Create: `docs/api-reference/rest-v2.md`
- Create: `docs/api-reference/graphql.md`
- Create: `docs/api-reference/response-codes.md`
- Create: `docs/openapi.json` (copy from API)
- Modify: `mkdocs.yml` (update nav)

- [ ] **Step 1: Download OpenAPI spec**

```bash
curl -s https://api.hikerapi.com/openapi.json | python3 -m json.tool > docs/openapi.json
```

Verify it downloaded correctly:

```bash
python3 -c "import json; d=json.load(open('docs/openapi.json')); print(f'{len(d[\"paths\"])} paths')"
```

Expected: something like `104 paths` (may vary).

- [ ] **Step 2: Write REST v1 page**

Create `docs/api-reference/rest-v1.md`:

```markdown
# REST API v1

Mobile API endpoints for anonymous Instagram data retrieval.

Endpoints cover: user profiles, media, stories, highlights, followers/following, hashtags, locations, and search.

All endpoints use `GET` method and require the `x-access-key` header. See [Authentication](../getting-started/authentication.md).

<swagger-ui src="../openapi.json"
  filter="true"
  operationsSorter="alpha"
  tagsSorter="alpha"
  docExpansion="list"
/>

!!! note "Filtering"
    Use the filter box above to search for specific endpoints. Type `v1/user` to see all v1 user endpoints.

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/7it8oc2i){ target=_blank }
```

- [ ] **Step 3: Write REST v2 page**

Create `docs/api-reference/rest-v2.md`:

```markdown
# REST API v2

Enhanced API v2 endpoints with pagination support and extended data.

v2 endpoints return structured responses with `next_page_id` for pagination, making it easier to iterate through large datasets.

<swagger-ui src="../openapi.json"
  filter="true"
  operationsSorter="alpha"
  docExpansion="list"
/>

!!! tip "v1 vs v2"
    v2 endpoints generally offer better pagination and richer response data. Use v2 when available.

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/7it8oc2i){ target=_blank }
```

- [ ] **Step 4: Write GraphQL page**

Create `docs/api-reference/graphql.md`:

```markdown
# GraphQL API

Anonymous data retrieval via Instagram's GraphQL API.

GraphQL endpoints use cursor-based pagination and return data in Instagram's native graph format.

## Endpoints

<swagger-ui src="../openapi.json"
  filter="true"
  docExpansion="list"
/>

!!! tip "Filtering"
    Type `gql/` in the filter box to see only GraphQL endpoints.

## Example: Get comments

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comments/chunk?media_id=2698190634266625811"
    ```

=== "Python"

    ```python
    cl = Client(token="YOUR_TOKEN")
    comments, end_cursor = cl.comments_chunk_gql(media_id="2698190634266625811")
    ```

Example response:

```json
{
  "id": "17871375683538333",
  "text": "Amazing!",
  "created_at": 1635869420,
  "owner": {
    "id": "33259029032",
    "username": "user123",
    "is_verified": false
  },
  "edge_liked_by": { "count": 258 },
  "edge_threaded_comments": { "count": 16 }
}
```

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/7it8oc2i){ target=_blank }
```

- [ ] **Step 5: Write Response Codes page**

Create `docs/api-reference/response-codes.md`:

```markdown
# Response Codes

| Code | Status | Description |
|------|--------|-------------|
| 200 | OK | The request has succeeded. |
| 307 | Temporary Redirect | The requested resource is temporarily available at a different URL. |
| 400 | Bad Request | Arguments are not correctly transmitted. |
| 401 | Unauthorized | You forgot to add the token to the query. |
| 402 | Payment Required | Payment is required to access HikerAPI. |
| 403 | Forbidden | The account, comment, or media is private. |
| 404 | Not Found | The account, comment, or media was not found. |
| 405 | Method Not Allowed | This HTTP method is not allowed for HikerAPI. |
| 408 | Request Timeout | The server waited too long and closed the connection. |
| 422 | Unprocessable Entity | The server understands the request but cannot process it due to semantic errors. |
| 429 | Too Many Requests | Your request was rejected due to exceeding the request limit. See [Rate Limits](../guides/rate-limits.md). |
| 430 | Request Header Fields Too Large | Request header fields too large. |
| 500 | Internal Server Error | Internal server error (request fee is **not** charged). |
| 503 | Service Unavailable | Server temporarily unable to process requests (request fee is **not** charged). |
| 504 | Gateway Timeout | Network delays or server access problems (request fee is **not** charged). |

!!! info "Billing note"
    Errors 500, 503, and 504 are **not charged** — you only pay for successful requests.
```

- [ ] **Step 6: Create api-reference directory and update nav**

```bash
mkdir -p docs/api-reference
```

Update `nav:` in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Quick Start: getting-started/quick-start.md
    - Authentication: getting-started/authentication.md
  - API Reference:
    - REST API v1: api-reference/rest-v1.md
    - REST API v2: api-reference/rest-v2.md
    - GraphQL API: api-reference/graphql.md
    - Response Codes: api-reference/response-codes.md
```

- [ ] **Step 7: Verify locally**

```bash
mkdocs serve
```

Check:
- API Reference tab appears in navigation
- Swagger UI renders with endpoint list on REST v1 page
- Filter box works (type `user` to filter)
- Response Codes table renders correctly
- GraphQL page shows example with tabs

- [ ] **Step 8: Commit**

```bash
git add docs/api-reference/ docs/openapi.json mkdocs.yml
git commit -m "feat: add API Reference pages with OpenAPI render

REST v1, v2, GraphQL, and Response Codes. Swagger UI renders
openapi.json directly — no intermediate stubs needed.
Refs net/hikerapi#185"
```

---

### Task 6: Guides — Rate Limits and Request Costs

**Files:**
- Create: `docs/guides/rate-limits.md`
- Create: `docs/guides/request-costs.md`
- Modify: `mkdocs.yml` (update nav)

- [ ] **Step 1: Create guides directory**

```bash
mkdir -p docs/guides
```

- [ ] **Step 2: Write Rate Limits page**

Create `docs/guides/rate-limits.md`:

```markdown
# Rate Limits & Retry Logic

## Default limits

| Plan | Requests/day | Requests/second |
|------|-------------|-----------------|
| Default | 1,000,000 | ~11 |

If you exceed the per-second limit, the server returns **429 Too Many Requests**.

## Handling rate limits

1. **Monitor frequency** — stay under your req/sec limit
2. **On 429** — pause 1-2 seconds, then retry
3. **Use semaphores** — limit concurrent requests in async code

## Check your current rate limit

```bash
curl -H "x-access-key: YOUR_TOKEN" "https://api.hikerapi.com/sys/balance"
```

The `rate` field in the response is your current requests/second limit.

## Example: Async with rate limiting

```python
import httpx
import asyncio

headers = {
    "x-access-key": "YOUR_TOKEN",
    "accept": "application/json",
}

# Get your rate limit
rate_limit = httpx.get(
    "https://api.hikerapi.com/sys/balance", headers=headers
).json()["rate"]

semaphore = asyncio.Semaphore(rate_limit)


async def get_followers(user_id: str) -> list:
    async with httpx.AsyncClient(timeout=20) as client:
        params = {"user_id": user_id, "page_id": "", "force": "on"}
        followers = []

        while True:
            async with semaphore:
                response = await client.get(
                    "https://api.hikerapi.com/v2/user/followers",
                    params=params,
                    headers=headers,
                )
                if response.status_code == 429:
                    await asyncio.sleep(2)
                    continue
                elif response.status_code == 402:
                    raise Exception("Insufficient balance")

                res = response.json()
                users = res["response"]["users"]
                page_id = res["next_page_id"]
                followers.extend(users)

                if not page_id:
                    break
                params["page_id"] = page_id

        return followers


async def main():
    user_ids = ["1553030189", "12345", "4238157586"]
    tasks = [asyncio.create_task(get_followers(uid)) for uid in user_ids]
    results = await asyncio.gather(*tasks)
    print(f"Got followers for {len(results)} users")


asyncio.run(main())
```

!!! tip "Need higher limits?"
    [Contact us](../support/contacts.md) to discuss custom rate limits for your use case. Starting at $0.001/request — [see pricing →](https://hikerapi.com/p/7it8oc2i){ target=_blank }
```

- [ ] **Step 3: Write Request Costs page**

Create `docs/guides/request-costs.md`:

```markdown
# Request Costs

Each API call may use one or more internal request units. The actual cost is returned in the response header:

```
x-hiker-info: reqs=<number>
```

Most endpoints cost **1 request**. Some endpoints perform additional checks (privacy, ID lookup) and cost more.

## Multi-request endpoints

| Endpoint | Reqs | What it does |
|----------|------|-------------|
| `/v1/user/highlights` | 2 | Gets highlights + privacy check |
| `/v2/user/highlights` | 2 | Gets highlights + privacy check |
| `/v1/user/highlights/by/username` | 3 | Username→ID lookup + highlights + privacy check |
| `/v2/user/highlights/by/username` | 3 | Username→ID lookup + highlights + privacy check |
| `/v1/user/stories` | 2 | Gets stories + privacy check |
| `/v2/user/stories` | 2 | Gets stories + privacy check |
| `/v1/user/stories/by/username` | 3 | Username→ID lookup + stories + privacy check |
| `/v2/user/stories/by/username` | 3 | Username→ID lookup + stories + privacy check |
| `/v1/user/search/followers` | 2 | Gets followers + privacy check |
| `/v1/user/search/following` | 2 | Gets following + privacy check |
| `/a2/user` | 2 | Profile data + media |
| `/v2/user/explore/businesses/by/id` | 2 | Business recommendations + account details |
| `/gql/user/followers/chunk` | 2 | Gets followers + privacy check |
| `/gql/user/following/chunk` | 2 | Gets following + privacy check |

## Force mode — skip privacy checks

Add `force=on` to skip privacy checks and reduce request cost by 1:

=== "With force (1 req)"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/stories?user_id=123&force=on"
    ```

=== "Without force (2 reqs)"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/stories?user_id=123"
    ```

!!! note
    Privacy checks identify **private accounts** specifically. Shadow-banned, deleted, or suspended accounts are handled differently.
```

- [ ] **Step 4: Update nav in mkdocs.yml**

Add to `nav:` in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Quick Start: getting-started/quick-start.md
    - Authentication: getting-started/authentication.md
  - API Reference:
    - REST API v1: api-reference/rest-v1.md
    - REST API v2: api-reference/rest-v2.md
    - GraphQL API: api-reference/graphql.md
    - Response Codes: api-reference/response-codes.md
  - Guides:
    - Rate Limits: guides/rate-limits.md
    - Request Costs: guides/request-costs.md
```

- [ ] **Step 5: Verify locally**

```bash
mkdocs serve
```

Check Guides tab, rate limits code example, request costs table, force mode tabs.

- [ ] **Step 6: Commit**

```bash
git add docs/guides/ mkdocs.yml
git commit -m "feat: add Guides — Rate Limits and Request Costs

Converted from RST with improved examples and force mode tabs.
Refs net/hikerapi#185"
```

---

### Task 7: SDK guide pages

**Files:**
- Create: `docs/sdk/python.md`
- Create: `docs/sdk/javascript.md`
- Create: `docs/sdk/go.md`
- Create: `docs/sdk/php.md`
- Modify: `mkdocs.yml` (update nav)

- [ ] **Step 1: Create sdk directory**

```bash
mkdir -p docs/sdk
```

- [ ] **Step 2: Write Python SDK page**

Create `docs/sdk/python.md`:

```markdown
# Python SDK

Official Python client for HikerAPI. Sync and async support.

## Installation

```bash
pip install hikerapi
```

## Quick start

```python
from hikerapi import Client

cl = Client(token="YOUR_TOKEN")

# Get user profile
user = cl.user_by_username_v1("ronaldo")
print(user["follower_count"])  # 612000000

# Get user's recent media
medias, end_cursor = cl.user_medias_chunk_v1(user_id=user["pk"])
for media in medias:
    print(media["code"], media["like_count"])
```

## Async client

```python
from hikerapi import AsyncClient

cl = AsyncClient(token="YOUR_TOKEN")

user = await cl.user_by_username_v1("ronaldo")
followers, end_cursor = await cl.user_followers_chunk_gql(user_id=user["pk"])
```

## Pagination

```python
cl = Client(token="YOUR_TOKEN")
all_followers = {}
end_cursor = None

while True:
    chunk, end_cursor = cl.user_followers_chunk_gql(
        user_id="173560420", end_cursor=end_cursor
    )
    all_followers.update({u["pk"]: u for u in chunk})
    if not end_cursor:
        break
```

## Method naming

SDK methods map 1:1 to API endpoints:

| Endpoint | Method |
|----------|--------|
| `GET /v1/user/by/username` | `cl.user_by_username_v1()` |
| `GET /v2/user/followers` | `cl.user_followers_v2()` |
| `GET /gql/comments/chunk` | `cl.comments_chunk_gql()` |

Pattern: `endpoint_path_version()` — see [API Reference](../api-reference/rest-v1.md) for all endpoints.

## Source code

- PyPI: [hikerapi](https://pypi.org/project/hikerapi/)
- Version: 1.7.7
```

- [ ] **Step 3: Write JavaScript SDK page**

Create `docs/sdk/javascript.md`:

```markdown
# JavaScript SDK

Official Node.js client for HikerAPI.

## Installation

```bash
npm install hikerapi
```

## Quick start

```javascript
import { Client } from "hikerapi";

const client = new Client({ token: "YOUR_TOKEN" });

// Get user profile
const user = await client.v1.userByUsername("ronaldo");
console.log(user.follower_count);

// Get followers
const { users, nextPageId } = await client.v2.userFollowers("173560420");
```

## Pagination

```javascript
let pageId = "";
const allFollowers = [];

while (true) {
  const { response, next_page_id } = await client.v2.userFollowers(
    "173560420",
    { page_id: pageId }
  );
  allFollowers.push(...response.users);
  if (!next_page_id) break;
  pageId = next_page_id;
}
```

## Without SDK

```javascript
const headers = { "x-access-key": "YOUR_TOKEN" };

const response = await fetch(
  "https://api.hikerapi.com/v1/user/by/username?username=ronaldo",
  { headers }
);
const user = await response.json();
```

See [API Reference](../api-reference/rest-v1.md) for all endpoints.
```

- [ ] **Step 4: Write Go SDK page**

Create `docs/sdk/go.md`:

```markdown
# Go SDK

Official Go client for HikerAPI.

## Installation

```bash
go get github.com/hikerapi/hikerapi-go
```

## Quick start

```go
package main

import (
    "fmt"
    "github.com/hikerapi/hikerapi-go"
)

func main() {
    client := hikerapi.NewClient("YOUR_TOKEN")

    user, err := client.V1.UserByUsername("ronaldo")
    if err != nil {
        panic(err)
    }
    fmt.Println(user.FollowerCount)
}
```

## Without SDK

```go
req, _ := http.NewRequest("GET",
    "https://api.hikerapi.com/v1/user/by/username?username=ronaldo", nil)
req.Header.Set("x-access-key", "YOUR_TOKEN")

resp, _ := http.DefaultClient.Do(req)
```

See [API Reference](../api-reference/rest-v1.md) for all endpoints.
```

- [ ] **Step 5: Write PHP SDK page**

Create `docs/sdk/php.md`:

```markdown
# PHP SDK

Official PHP client for HikerAPI.

## Installation

```bash
composer require hikerapi/hikerapi-php
```

## Quick start

```php
use HikerAPI\Client;

$client = new Client('YOUR_TOKEN');

$user = $client->v1->userByUsername('ronaldo');
echo $user['follower_count'];

$followers = $client->v2->userFollowers('173560420');
```

## Without SDK

```php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,
    'https://api.hikerapi.com/v1/user/by/username?username=ronaldo');
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'x-access-key: YOUR_TOKEN',
    'accept: application/json',
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = json_decode(curl_exec($ch), true);
curl_close($ch);
```

See [API Reference](../api-reference/rest-v1.md) for all endpoints.
```

- [ ] **Step 6: Update nav in mkdocs.yml**

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Quick Start: getting-started/quick-start.md
    - Authentication: getting-started/authentication.md
  - API Reference:
    - REST API v1: api-reference/rest-v1.md
    - REST API v2: api-reference/rest-v2.md
    - GraphQL API: api-reference/graphql.md
    - Response Codes: api-reference/response-codes.md
  - SDKs:
    - Python: sdk/python.md
    - JavaScript: sdk/javascript.md
    - Go: sdk/go.md
    - PHP: sdk/php.md
  - Guides:
    - Rate Limits: guides/rate-limits.md
    - Request Costs: guides/request-costs.md
```

- [ ] **Step 7: Verify locally**

```bash
mkdocs serve
```

Check all 4 SDK pages render, code blocks have copy buttons, links to API Reference work.

- [ ] **Step 8: Commit**

```bash
git add docs/sdk/ mkdocs.yml
git commit -m "feat: add SDK guide pages for Python, JS, Go, PHP

Quick start + pagination examples for each language.
Refs net/hikerapi#185"
```

---

### Task 8: Support page

**Files:**
- Create: `docs/support/contacts.md`
- Modify: `mkdocs.yml` (update nav)

- [ ] **Step 1: Create support directory and page**

```bash
mkdir -p docs/support
```

Create `docs/support/contacts.md`:

```markdown
# Support

## Contact us

| Channel | Link |
|---------|------|
| Email | [support@hikerapi.com](mailto:support@hikerapi.com) |
| Telegram | [@hikerapi](https://t.me/hikerapi) |

## Feature requests

Vote for new endpoints and features in our [Telegram channel](https://t.me/hikerapi).

## Documentation

Found an issue in the docs? [Let us know](mailto:support@hikerapi.com).
```

- [ ] **Step 2: Add final nav to mkdocs.yml**

Complete `nav:` section:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Quick Start: getting-started/quick-start.md
    - Authentication: getting-started/authentication.md
  - API Reference:
    - REST API v1: api-reference/rest-v1.md
    - REST API v2: api-reference/rest-v2.md
    - GraphQL API: api-reference/graphql.md
    - Response Codes: api-reference/response-codes.md
  - SDKs:
    - Python: sdk/python.md
    - JavaScript: sdk/javascript.md
    - Go: sdk/go.md
    - PHP: sdk/php.md
  - Guides:
    - Rate Limits: guides/rate-limits.md
    - Request Costs: guides/request-costs.md
  - Support:
    - Contacts: support/contacts.md
```

- [ ] **Step 3: Verify locally**

```bash
mkdocs serve
```

Full site navigation should now work: Home, Getting Started, API Reference, SDKs, Guides, Support.

- [ ] **Step 4: Commit**

```bash
git add docs/support/ mkdocs.yml
git commit -m "feat: add Support/Contacts page

Refs net/hikerapi#185"
```

---

### Task 9: Cleanup — remove old Sphinx files

**Files:**
- Remove: `docs/source/` (all RST + conf.py)
- Remove: `docs/hikerapi/` (Python stubs)
- Remove: `docs/build/` (Sphinx artifacts)
- Remove: `docs/Makefile`, `docs/make.bat`
- Remove: `docs/index.md` (old MkDocs placeholder — replaced by new one)
- Remove: `Makefile.bak`

- [ ] **Step 1: Verify new site works completely before deleting**

```bash
mkdocs build --strict
```

Should build with no errors. If warnings about missing pages — fix them first.

- [ ] **Step 2: Remove old Sphinx files**

```bash
rm -rf docs/source/ docs/hikerapi/ docs/build/
rm -f docs/Makefile docs/make.bat
rm -f Makefile Makefile.bak
```

- [ ] **Step 3: Verify build still works**

```bash
mkdocs build --strict
```

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore: remove old Sphinx files and Python stubs

Sphinx config, RST sources, autodoc stubs, and build artifacts
no longer needed after MkDocs migration.
Refs net/hikerapi#185"
```

---

### Task 10: Final verification

- [ ] **Step 1: Full local review**

```bash
mkdocs serve
```

Walk through every page and check:

1. **Home** — grid cards render, CTA buttons link to hikerapi.com, trust signals table
2. **Announcement bar** — visible on all pages, dismiss works, links to signup
3. **Getting Started > Quick Start** — language tabs switch, code copy works
4. **Getting Started > Authentication** — header example, balance check
5. **API Reference > REST v1** — Swagger UI loads, filter works, endpoints listed
6. **API Reference > REST v2** — same checks
7. **API Reference > GraphQL** — example with tabs, Swagger UI
8. **API Reference > Response Codes** — table renders, billing note admonition
9. **SDKs** — all 4 pages, code blocks, links to API Reference
10. **Guides > Rate Limits** — async code example, pricing CTA
11. **Guides > Request Costs** — force mode tabs, cost table
12. **Support** — email and telegram links
13. **Dark mode toggle** — all pages look good in both modes
14. **Search** — type "followers" — should find relevant pages

- [ ] **Step 2: Build for production**

```bash
mkdocs build --strict
```

Should complete with zero errors and zero warnings.

- [ ] **Step 3: Commit any fixes**

If any issues were found and fixed during review, commit them:

```bash
git add -A
git commit -m "fix: polish docs after full review

Refs net/hikerapi#185"
```
