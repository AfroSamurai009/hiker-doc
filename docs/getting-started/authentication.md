# Authentication

All HikerAPI requests require an API key passed via the `x-access-key` header.

## Get your API key

1. [Sign up at hikerapi.com](https://hikerapi.com/p/hybef5jn){ target=_blank }
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
