# GraphQL API

Anonymous data retrieval via Instagram's GraphQL API.

GraphQL endpoints use cursor-based pagination (`end_cursor`) and return data in Instagram's native graph format. Includes both `gql/` and `g2/` endpoint families.

All endpoints use `GET` method and require the `x-access-key` header. See [Authentication](../../getting-started/authentication.md).

| Group | Description | Endpoints |
|-------|-------------|-----------|
| User | Profiles, followers, following, clips, reposts | 12 |
| Comments | Post comments, threaded replies, likers | 5 |
| Media | Media likers, usertags | 2 |
| Search | Global top search | 1 |
| g2 | Extended follower/following data | 2 |

## Pagination

Most GraphQL endpoints return `(data, end_cursor)`. Pass `end_cursor` to the next request to get the next page. When `end_cursor` is `null`, you've reached the end.

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

## All GraphQL endpoints (22)


!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

[OAD(../../openapi/gql.json)]

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-gql){ target=_blank }
