# GraphQL API

Anonymous data retrieval via Instagram's GraphQL API.

GraphQL endpoints use cursor-based pagination and return data in Instagram's native graph format.

## Endpoints

<swagger-ui src="../openapi.json"
  filter="true"
  docExpansion="list"
/>

!!! tip "Filtering"
    Type `gql/` in the filter box to see only GraphQL endpoints.

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

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/hybef5jn){ target=_blank }
