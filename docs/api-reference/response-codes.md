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
