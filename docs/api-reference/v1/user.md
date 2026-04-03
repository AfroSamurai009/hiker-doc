# User Endpoints

Get user profiles, followers, following lists, and search within followers.

**Endpoints:** [`/v1/user/about`](#get-v1userabout) | [`/v1/user/by/id`](#get-v1userbyid) | [`/v1/user/by/url`](#get-v1userbyurl) | [`/v1/user/by/username`](#get-v1userbyusername) | [`/v1/user/clips`](#get-v1userclips) | [`/v1/user/clips/chunk`](#get-v1userclipschunk) | [`/v1/user/followers`](#get-v1userfollowers) | [`/v1/user/followers/chunk`](#get-v1userfollowerschunk) | [`/v1/user/following`](#get-v1userfollowing) | [`/v1/user/following/chunk`](#get-v1userfollowingchunk) | [`/v1/user/guides`](#get-v1userguides) | [`/v1/user/medias`](#get-v1usermedias) | [`/v1/user/medias/chunk`](#get-v1usermediaschunk) | [`/v1/user/medias/pinned`](#get-v1usermediaspinned) | [`/v1/user/search/followers`](#get-v1usersearchfollowers) | [`/v1/user/search/following`](#get-v1usersearchfollowing) | [`/v1/user/tag/medias`](#get-v1usertagmedias) | [`/v1/user/tag/medias/chunk`](#get-v1usertagmediaschunk) | [`/v1/user/videos`](#get-v1uservideos) | [`/v1/user/videos/chunk`](#get-v1uservideoschunk) | [`/v1/user/web_profile_info`](#get-v1userweb_profile_info)


!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

[OAD(../../openapi/v1-user.json)]

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-user){ target=_blank }
