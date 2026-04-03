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

    [:octicons-arrow-right-24: Explore endpoints](api-reference/v1/index.md)

-   :material-language-python:{ .lg .middle } **SDKs**

    ---

    Official clients for Python, JavaScript, Go, and PHP

    [:octicons-arrow-right-24: View SDKs](sdk/python.md)

</div>

## Why HikerAPI?

<div class="grid cards" markdown>

-   **10,000+**{ .stat-number }

    developers worldwide

-   **147**{ .stat-number }

    API endpoints

-   **10M+**{ .stat-number }

    requests per day

-   **$0.0006**{ .stat-number }

    per request

</div>

## See it in action

```bash
curl -H "x-access-key: YOUR_TOKEN" \
  "https://api.hikerapi.com/v1/user/by/username?username=ronaldo"
```

```json
{"pk": "173560420", "username": "ronaldo", "full_name": "Cristiano Ronaldo",
 "is_verified": true, "follower_count": 612000000, ...}
```

---

<div class="cta-box" markdown>

**Ready to start?** Get 100 free requests after signup — no credit card required.

[Start Free Trial](https://hikerapi.com/p/hybef5jn){ .md-button .md-button--primary target=_blank }
[View API Reference](api-reference/v1/index.md){ .md-button }

</div>
