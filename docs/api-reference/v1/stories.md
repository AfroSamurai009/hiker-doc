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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/story/by/id",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/story/by/url",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/story/download",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/story/download/by/story/url",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/story/download/by/url",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/stories",
        headers=headers,
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
    "pk": "3870193736105885141",
    "id": "3870193736105885141_787132",
    "code": "DW1sLKkiH3V",
    "taken_at": "2026-04-07T17:31:03Z",
    "media_type": 1,
    "product_type": "story",
    "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/658429561_18647594869019133_9051380253814827091_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDE5MzczNjEwNTg4NTE0MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjc1MHgxMzM0LnNkci5DMyJ9&_nc_ohc=cEy_Zw6mVEIQ7kNvwEHQ_od&_nc_oc=AdrDSLwLP630PSKlLN_LBAACOxttz5_kdCAbDPTlN9-5jFsXDOPT82G1spt4VCODsO8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=GCLJVnwOrTIPB79D8ya6hQ&_nc_ss=7a3ba&oh=00_Af0IiW-rbTxhJgGB1kveadvVdNP8Rt44M6rySx-tXbeiwg&oe=69DC50D4",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFLrrjHIwFHmkBc9AbJhpmRfFGg16gb5FePm8qplyGH1_-D7enEDzS4XJsOxqpnJSw&_nc_ohc=XbeNvhLXv28Q7kNvwGUzvDW&_nc_gid=GCLJVnwOrTIPB79D8ya6hQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2cw9mNSbYs_gcee_VVf4Fsr3CHMs54OO8P4QehoVOMcw&oe=69DC19A9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": null,
    "video_duration": 0.0,
    "sponsor_tags": [],
    "mentions": [],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [
      {
        "id": "18062921705692032",
        "type": "gif",
        "x": 0.5,
        "y": 0.8028485757121431,
        "z": 0,
        "width": 0.40441287555694505,
        "height": 0.06831102485599501,
        "rotation": 0.0,
        "story_link": {
          "url": "https://l.instagram.com/?u=https%3A%2F%2Fwww.nationalgeographic.com%2Fscience%2Farticle%2Fartemis-ii-new-earthrise-earthset-eclipse%3Fcmpid%3Dorg%253Dngp%253A%253Amc%253Dsocial%253A%253Asrc%253Dinstagram%253A%253Acmp%253Deditorial%253A%253Aadd%253Digs20260407science-artemisiinewearthriseearthseteclipsefreemiumhedcard%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn0avnJ2gX-sRIa5BFqMaYiLfsGf0C8jBegd42EPXegoA5Ial_fQ92SzPYCTs_aem_o1khV9BcT-4BDNpL-gnLFQ&e=AT6RaaEau8WsXjASAcjxyV0G8TiQmiJu7evSRimKYyz7hoPAQsgwhnIRZccgcjR1aWO6hwhAQqvXbIPABGB__aAh6skOGjQra87Wk12blw",
          "link_title": "Visit Link",
          "link_type": "web",
          "display_url": "nationalgeographic.com/science/article/artemis-ii-new-earthrise-earthset-eclipse?cmpid=org=ngp::mc=social::src=instagram::cmp=editorial::add=igs20260407science-artemisiinewearthriseearthseteclipsefreemiumhedcard"
        },
        "extra": {}
      }
    ],
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/stories/by/username",
        headers=headers,
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
    "pk": "3870193736105885141",
    "id": "3870193736105885141_787132",
    "code": "DW1sLKkiH3V",
    "taken_at": "2026-04-07T17:31:03Z",
    "media_type": 1,
    "product_type": "story",
    "thumbnail_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-15/658429561_18647594869019133_9051380253814827091_n.jpg?stp=dst-jpg_e35_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDE5MzczNjEwNTg4NTE0MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjc1MHgxMzM0LnNkci5DMyJ9&_nc_ohc=cEy_Zw6mVEIQ7kNvwFXwSkf&_nc_oc=AdrVeH76EtVKsfutQFhxEbR9aBVTQ4WA-ZGHVl9EvbQUDZOyMMpFK19PtIcKpAYWZ5Y&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=sJqJ8LDk0RoVXfPRJI3Mog&_nc_ss=7a3ba&oh=00_Af0H7FDhI9gEcY9OvuCRhQXUHzdRvL70AVB-U816To2mIQ&oe=69DC50D4",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFkg7_KjP96hHtjNoio1j6KqRH3evQzEoRPy8d5icJ47IxIDiwQJdR3kh81SeH68zI&_nc_ohc=XbeNvhLXv28Q7kNvwEPkxe_&_nc_gid=sJqJ8LDk0RoVXfPRJI3Mog&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2DUW-P4ZFjxbPh5T0O_L5DqwqnoaAI12ZbvG_Y-OfJMw&oe=69DC19A9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": null,
    "video_duration": 0.0,
    "sponsor_tags": [],
    "mentions": [],
    "links": [],
    "hashtags": [],
    "locations": [],
    "stickers": [
      {
        "id": "18062921705692032",
        "type": "gif",
        "x": 0.5,
        "y": 0.8028485757121431,
        "z": 0,
        "width": 0.40441287555694505,
        "height": 0.06831102485599501,
        "rotation": 0.0,
        "story_link": {
          "url": "https://l.instagram.com/?u=https%3A%2F%2Fwww.nationalgeographic.com%2Fscience%2Farticle%2Fartemis-ii-new-earthrise-earthset-eclipse%3Fcmpid%3Dorg%253Dngp%253A%253Amc%253Dsocial%253A%253Asrc%253Dinstagram%253A%253Acmp%253Deditorial%253A%253Aadd%253Digs20260407science-artemisiinewearthriseearthseteclipsefreemiumhedcard%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnBWTb-wDrjyEfaHqyRB5D9bCMNqmzmCzPaYCtIWJPz6755GK3DUdilYqWe9I_aem_amhsiiyHtWy5dKCbFRnfAw&e=AT4nwNH2f-3bx3l3Os0Kt04_yz15Hu3Pq41bNka3F21QvpkNuN7hVRjlwttFrGrm_vBSCPEMevaLmHijnn60aDcl2oaTPM1SqTliN5jWxg",
          "link_title": "Visit Link",
          "link_type": "web",
          "display_url": "nationalgeographic.com/science/article/artemis-ii-new-earthrise-earthset-eclipse?cmpid=org=ngp::mc=social::src=instagram::cmp=editorial::add=igs20260407science-artemisiinewearthriseearthseteclipsefreemiumhedcard"
        },
        "extra": {}
      }
    ],
    "medias": []
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-stories){ target=_blank }
