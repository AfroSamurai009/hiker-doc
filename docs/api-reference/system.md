# System Endpoints

Account balance and rate limit info.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../getting-started/authentication.md). Error responses: [Response Codes](response-codes.md).

**Endpoints:** [`/sys/balance`](#get-sysbalance)

---

### GET /sys/balance

Balance

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/sys/balance"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/sys/balance",
        headers={"x-access-key": "YOUR_TOKEN"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/sys/balance",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "requests": 2176377,
  "rate": 15,
  "currency": "USD",
  "amount": 914.2117
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-system){ target=_blank }
