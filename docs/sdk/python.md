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
import asyncio
from hikerapi import AsyncClient


async def main():
    cl = AsyncClient(token="YOUR_TOKEN")
    user = await cl.user_by_username_v1("ronaldo")
    followers, end_cursor = await cl.user_followers_chunk_gql(user_id=user["pk"])
    print(f"Got {len(followers)} followers")


asyncio.run(main())
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

Pattern: `endpoint_path_version()` — see [API Reference](../api-reference/v1/index.md) for all endpoints.

## Source code

- PyPI: [hikerapi](https://pypi.org/project/hikerapi/)
- Version: 1.7.7
