# REST API v2

Enhanced API endpoints with structured pagination and extended data.

v2 endpoints return responses with `next_page_id` for easy pagination — no need to parse cursors manually. Also includes v3 and a2 endpoints with additional features.

All endpoints use `GET` method and require the `x-access-key` header. See [Authentication](../getting-started/authentication.md).

## v2 vs v1

| Feature | v1 | v2 |
|---------|----|----|
| Pagination | `end_cursor` (opaque) | `next_page_id` (simple) |
| Response format | Raw Instagram data | Structured `{ response, next_page_id }` |
| Data richness | Basic fields | Extended fields |

!!! tip
    Use v2 when available. Fall back to v1 for endpoints not yet in v2.

## All v2/v3/a2 endpoints (52)

<swagger-ui src="../openapi-v2.json" docExpansion="list" filter="true"/>

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/hybef5jn){ target=_blank }
