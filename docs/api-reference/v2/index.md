# REST API v2

Enhanced API endpoints with structured pagination and extended data.

v2 endpoints return responses with `next_page_id` for easy pagination — no need to parse cursors manually. Also includes v3 and a2 endpoints.

All endpoints use `GET` method and require the `x-access-key` header. See [Authentication](../../getting-started/authentication.md).

| Resource | Description | Endpoints |
|----------|-------------|-----------|
| [User](user.md) | Profiles, followers, following, streams | 17 |
| [Media](media.md) | Posts, reels, likes, comments | 11 |
| [Stories](stories.md) | User stories | 2 |
| [Highlights](highlights.md) | Story highlights | 1 |
| [Hashtags](hashtags.md) | Hashtag info and media | 4 |
| [Search](search.md) | Search users, hashtags, places | 10 |
| [Track](track.md) | Audio tracks and music | 7 |
