# Authentication

All HikerAPI requests require an API key passed via the `x-access-key` header.

## Get your API key

1. [Sign up at hikerapi.com](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=auth-signup){ target=_blank }
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
  "requests": 100000,
  "rate": 15,
  "currency": "USD",
  "amount": 100.00
}
```

- `requests` — remaining request units
- `rate` — your current rate limit (requests/second)
- `currency` — account currency
- `amount` — remaining balance
