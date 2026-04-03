# REST API v1

Mobile API endpoints for anonymous Instagram data retrieval. v1 endpoints return raw Instagram data structures with minimal transformation.

All endpoints use `GET` method and require the `x-access-key` header. See [Authentication](../getting-started/authentication.md).

## Endpoint groups

| Group | Description | Example |
|-------|-------------|---------|
| **User** | Profiles, followers, following, search | `/v1/user/by/username` |
| **Media** | Posts, reels, likes, comments | `/v1/media/by/code` |
| **Stories** | User stories and story items | `/v1/user/stories` |
| **Highlights** | Story highlights and covers | `/v1/user/highlights` |
| **Hashtags** | Hashtag info and recent media | `/v1/hashtag/by/name` |
| **Locations** | Location info and media | `/v1/location/by/id` |
| **Search** | Global search across users, hashtags, locations | `/v1/search` |

## All v1 endpoints (72)

[OAD(../openapi-v1.json)]

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/hybef5jn){ target=_blank }
