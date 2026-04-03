# Quick Start

Make your first HikerAPI request in 5 minutes.

## 1. Get your API key

[Sign up at hikerapi.com](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=quickstart-signup){ target=_blank } and grab your token from the [dashboard](https://hikerapi.com/tokens){ target=_blank }.

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
    - Browse the [API Reference](../api-reference/v1/index.md) for all 147 endpoints
    - Check [Rate Limits](../guides/rate-limits.md) to optimize your integration
    - See [SDKs](../sdk/python.md) for language-specific clients
