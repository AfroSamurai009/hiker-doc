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
    [Contact us](../support/contacts.md) to discuss custom rate limits for your use case. Starting at $0.0006/request — [see pricing →](https://hikerapi.com/p/hybef5jn){ target=_blank }
