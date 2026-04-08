# Stories Endpoints

Get user stories and story items.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/story/by/id`](#get-v1storybyid) | [`/v1/story/by/url`](#get-v1storybyurl) | [`/v1/story/download`](#get-v1storydownload) | [`/v1/story/download/by/story/url`](#get-v1storydownloadbystoryurl) | [`/v1/story/download/by/url`](#get-v1storydownloadbyurl) | [`/v1/user/stories`](#get-v1userstories) | [`/v1/user/stories/by/username`](#get-v1userstoriesbyusername)

---

### GET /v1/story/by/id

Get story object by id. Returns a Story object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/story/by/id?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.story_by_id_v1(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/story/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/story/by/id?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/story/by/url

Get story object by id. Returns a Story object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/story/by/url?url=https://www.instagram.com/stories/natgeo/3776832898280228145/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.story_by_url_v1(url="https://www.instagram.com/stories/natgeo/3776832898280228145/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/story/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/stories/natgeo/3776832898280228145/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/story/by/url?url=https://www.instagram.com/stories/natgeo/3776832898280228145/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/story/download

Download story media by story id. Returns story download data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/story/download?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.story_download_v1(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/story/download",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/story/download?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/story/download/by/story/url

Download story file by story URL

Example: https://ins...ram.com/stories/example/30038568123745341231284. Returns story download data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/story/download/by/story/url?url=https://www.instagram.com/stories/natgeo/3776832898280228145/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.story_download_by_story_url_v1(url="https://www.instagram.com/stories/natgeo/3776832898280228145/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/story/download/by/story/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/stories/natgeo/3776832898280228145/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/story/download/by/story/url?url=https://www.instagram.com/stories/natgeo/3776832898280228145/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/story/download/by/url

Download story file by URL to file
(you can take it from "/v1/story/by/id" or "/v1/story/by/url")

Example: https://scontent-lga3-1.cdnins...ram.com/v/t66.30100-16/
    310890533_1622838408176007_5601749632271872566_n.mp4?efg=... Returns story download data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/story/download/by/url?url=https://www.instagram.com/stories/natgeo/3776832898280228145/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.story_download_by_url_v1(url="https://www.instagram.com/stories/natgeo/3776832898280228145/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/story/download/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/stories/natgeo/3776832898280228145/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/story/download/by/url?url=https://www.instagram.com/stories/natgeo/3776832898280228145/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/user/stories

⚠️ Billing: 2 requests per call. Returns a list of Story objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/stories?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_stories_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/stories",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/stories?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870828041672894129",
    "id": "3870828041672894129_787132",
    "code": "DW38ZhqiKax",
    "taken_at": "2026-04-08T14:31:15Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-ord5-2.cdninstagram.com/...",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-ord5-3.cdninstagram.com/...",
    "video_duration": 14.965999603271484,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      }
    ],
    "mentions": [
      {
        "user": {
          "pk": "304662892",
          "id": "304662892",
          "username": "prada",
          "full_name": "Prada",
          "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "x": 0.0,
        "y": 0.0,
        "width": 0.0,
        "height": 0.0
      }
    ],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [],
    "medias": []
  },
  {
    "pk": "3870828324352170239",
    "id": "3870828324352170239_787132",
    "code": "DW38do7iBj_",
    "taken_at": "2026-04-08T14:31:44Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-ord5-2.cdninstagram.com/...",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-ord5-3.cdninstagram.com/...",
    "video_duration": 14.965999603271484,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      }
    ],
    "mentions": [
      {
        "user": {
          "pk": "304662892",
          "id": "304662892",
          "username": "prada",
          "full_name": "Prada",
          "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "x": 0.0,
        "y": 0.0,
        "width": 0.0,
        "height": 0.0
      }
    ],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [],
    "medias": []
  },
  {
    "pk": "3870828687528621445",
    "id": "3870828687528621445_787132",
    "code": "DW38i7KiPWF",
    "taken_at": "2026-04-08T14:32:16Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-ord5-2.cdninstagram.com/...",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-ord5-3.cdninstagram.com/...",
    "video_duration": 13.732999801635742,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      }
    ],
    "mentions": [
      {
        "user": {
          "pk": "304662892",
          "id": "304662892",
          "username": "prada",
          "full_name": "Prada",
          "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/...",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "x": 0.0,
        "y": 0.0,
        "width": 0.0,
        "height": 0.0
      }
    ],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [],
    "medias": []
  }
]
```

</details>

---

### GET /v1/user/stories/by/username

Get user stories. Returns a list of Story objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/stories/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_stories_by_username_v1(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/stories/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/stories/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870828041672894129",
    "id": "3870828041672894129_787132",
    "code": "DW38ZhqiKax",
    "taken_at": "2026-04-08T14:31:15Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-sea5-1.cdninstagram.com/...",
    "video_duration": 15.0,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      }
    ],
    "mentions": [
      {
        "user": {
          "pk": "304662892",
          "id": "304662892",
          "username": "prada",
          "full_name": "Prada",
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "x": 0.0,
        "y": 0.0,
        "width": 0.0,
        "height": 0.0
      }
    ],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [],
    "medias": []
  },
  {
    "pk": "3870828324352170239",
    "id": "3870828324352170239_787132",
    "code": "DW38do7iBj_",
    "taken_at": "2026-04-08T14:31:44Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-sea1-1.cdninstagram.com/...",
    "video_duration": 15.0,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      }
    ],
    "mentions": [
      {
        "user": {
          "pk": "304662892",
          "id": "304662892",
          "username": "prada",
          "full_name": "Prada",
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "x": 0.0,
        "y": 0.0,
        "width": 0.0,
        "height": 0.0
      }
    ],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [],
    "medias": []
  },
  {
    "pk": "3870828687528621445",
    "id": "3870828687528621445_787132",
    "code": "DW38i7KiPWF",
    "taken_at": "2026-04-08T14:32:16Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-sea1-1.cdninstagram.com/...",
    "video_duration": 13.765999794006348,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      }
    ],
    "mentions": [
      {
        "user": {
          "pk": "304662892",
          "id": "304662892",
          "username": "prada",
          "full_name": "Prada",
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "x": 0.0,
        "y": 0.0,
        "width": 0.0,
        "height": 0.0
      }
    ],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [],
    "medias": []
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-stories){ target=_blank }
