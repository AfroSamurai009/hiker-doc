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
    "pk": "3870828041672894129",
    "id": "3870828041672894129_787132",
    "code": "DW38ZhqiKax",
    "taken_at": "2026-04-08T14:31:15Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/662308336_1449496010284799_6982950920110364679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgyODA0MTY3Mjg5NDEyOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_t3hmPz1AKsQ7kNvwEg0DmG&_nc_oc=Adr2sYlbdIdVRrHms1Kd--nYfTtYox1ZsbmZGrUeVbuVFcH1C8pI7Afhcx_-PcWB0u0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&_nc_ss=7a3ba&oh=00_Af134KECSMv1Q7ilDRKs8UOuzKec0kjnfl6-Fy1RCqX8oQ&oe=69DC3DF4",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=XbeNvhLXv28Q7kNvwGH2kAN&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3YUH2V7A8k8nvP_zaK6Pw1kbfxeqEaQO5CX2CxI6qvPQ&oe=69DC51E9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-vie1-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwFT37On&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3wgvlHpyReUZAKHWn0Tpra6RWJoozmFb4EKfmtkgaSAA&oe=69D83FDE",
    "video_duration": 14.965999603271484,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=vY0PvLetHQgQ7kNvwHQDdvO&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1nWN-byDXAL03Z9UpvYsGbAE7f-VYnVVj6p30Ps8XYSg&oe=69DC58F0&_nc_sid=6d62aa",
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
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=vY0PvLetHQgQ7kNvwHQDdvO&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1nWN-byDXAL03Z9UpvYsGbAE7f-VYnVVj6p30Ps8XYSg&oe=69DC58F0&_nc_sid=6d62aa",
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
    "thumbnail_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/657255699_1385632013371495_7666726418949229423_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODMyNDM1MjE3MDIzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m7SPdY3D7l0Q7kNvwECFCh4&_nc_oc=AdptRgjZ8Wxh8lM95ibq66rD6BUGq_Y0Z6oqJ84u4Q_nH6g1SsPTDmprhNzOG3eFSpY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&_nc_ss=7a3ba&oh=00_Af318eKRlTpNqG2CfVOkbhqyLG0Et_S7nzZb7xR5aT7JiQ&oe=69DC54C2",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=XbeNvhLXv28Q7kNvwGH2kAN&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3YUH2V7A8k8nvP_zaK6Pw1kbfxeqEaQO5CX2CxI6qvPQ&oe=69DC51E9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-vie1-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwFigLjg&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af01PibuNnucW0gP0kojdZq6l5_aLP6kKWrArHyw9amhWA&oe=69D85281",
    "video_duration": 14.965999603271484,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=vY0PvLetHQgQ7kNvwHQDdvO&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1nWN-byDXAL03Z9UpvYsGbAE7f-VYnVVj6p30Ps8XYSg&oe=69DC58F0&_nc_sid=6d62aa",
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
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=vY0PvLetHQgQ7kNvwHQDdvO&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1nWN-byDXAL03Z9UpvYsGbAE7f-VYnVVj6p30Ps8XYSg&oe=69DC58F0&_nc_sid=6d62aa",
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
    "thumbnail_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/659614888_1512637680515245_5529787493603763341_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODY4NzUyODYyMTQ0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=gitXYB93E4QQ7kNvwHFDBNs&_nc_oc=Adp6hsHKeYmtWmhdzdG3I_np1zerdBD8ppt2nbcuJGw-o179bNqF9M6wimYfHrVHwq8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&_nc_ss=7a3ba&oh=00_Af3fS7YeafDASCvUEsWEVeyyAVko_m7eItnpXCs8Hc_0XA&oe=69DC69B1",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=XbeNvhLXv28Q7kNvwGH2kAN&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3YUH2V7A8k8nvP_zaK6Pw1kbfxeqEaQO5CX2CxI6qvPQ&oe=69DC51E9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-vie1-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwH_ZFNC&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2HHSfst1p2H72wE-Thqlxf2ctNI0ErT_6C909c7YaUMw&oe=69D85C07",
    "video_duration": 13.732999801635742,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=vY0PvLetHQgQ7kNvwHQDdvO&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1nWN-byDXAL03Z9UpvYsGbAE7f-VYnVVj6p30Ps8XYSg&oe=69DC58F0&_nc_sid=6d62aa",
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
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5HvCVTFf62sI1uhc0L2B3IFDpNMAD9r7NAfdEDHZbH37NatkJ2X9ioH66ziaV0OU&_nc_ohc=vY0PvLetHQgQ7kNvwHQDdvO&_nc_gid=lszgurtPOv2jPAbQQ6QfQg&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1nWN-byDXAL03Z9UpvYsGbAE7f-VYnVVj6p30Ps8XYSg&oe=69DC58F0&_nc_sid=6d62aa",
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
    "pk": "3870828041672894129",
    "id": "3870828041672894129_787132",
    "code": "DW38ZhqiKax",
    "taken_at": "2026-04-08T14:31:15Z",
    "media_type": 2,
    "product_type": "story",
    "thumbnail_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/662308336_1449496010284799_6982950920110364679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODA0MTY3Mjg5NDEyOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_t3hmPz1AKsQ7kNvwG3FVoY&_nc_oc=Ado3ltUFaggL3GdjOQn2XCY44yRfxVx_OLX8_i9fXSMKI8H8X6elIVMVDeBQo9FFaGM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&_nc_ss=7a3ba&oh=00_Af3Yr0e6t5KQyifux78oEOj181aabPsMWbPsx6JOnMseEQ&oe=69DC3DF4",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=XbeNvhLXv28Q7kNvwGV2pZZ&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af04MaARBsHdrXVGZdjaFpwgLMb23T4qigW86xTtc453Dw&oe=69DC51E9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-vie1-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwHwXgMp&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3UCLypaY_mSitt4glOHj2USjvfSvTGXpTIkI_T-LSD6w&oe=69D83FDE",
    "video_duration": 15.0,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=vY0PvLetHQgQ7kNvwFYYgc7&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af3PQkoNPwVv8LFdh0FdUdqS0CCt0B_JInWGoMjPVhmp0A&oe=69DC58F0&_nc_sid=6d62aa",
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
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=vY0PvLetHQgQ7kNvwFYYgc7&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af3PQkoNPwVv8LFdh0FdUdqS0CCt0B_JInWGoMjPVhmp0A&oe=69DC58F0&_nc_sid=6d62aa",
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
    "thumbnail_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/657255699_1385632013371495_7666726418949229423_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODMyNDM1MjE3MDIzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m7SPdY3D7l0Q7kNvwHhm0kI&_nc_oc=AdoFcQUAXy_aw4ewRREnO4JNiRWjG_x3q7quIW5nCBkTOk3Xh5Rlity_VTQwqkOg3OM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&_nc_ss=7a3ba&oh=00_Af1TcdoiD7njk5rS9SC0vE3x3vH3BzgRAokD3g3YafMAnA&oe=69DC54C2",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=XbeNvhLXv28Q7kNvwGV2pZZ&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af04MaARBsHdrXVGZdjaFpwgLMb23T4qigW86xTtc453Dw&oe=69DC51E9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-vie1-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwHJog79&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0Ehqk1EjinHcHpfEoDFkAiW41lduYAnRkU00AeprnMLg&oe=69D85281",
    "video_duration": 15.0,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=vY0PvLetHQgQ7kNvwFYYgc7&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af3PQkoNPwVv8LFdh0FdUdqS0CCt0B_JInWGoMjPVhmp0A&oe=69DC58F0&_nc_sid=6d62aa",
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
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=vY0PvLetHQgQ7kNvwFYYgc7&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af3PQkoNPwVv8LFdh0FdUdqS0CCt0B_JInWGoMjPVhmp0A&oe=69DC58F0&_nc_sid=6d62aa",
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
    "thumbnail_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/659614888_1512637680515245_5529787493603763341_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODY4NzUyODYyMTQ0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=gitXYB93E4QQ7kNvwG2cO4y&_nc_oc=AdqVCov_XxB1wXPwUTYT54jyQgknHelQZRw2OyOjy92Bh3W5SVVPdSngcLHWs-lDOxo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&_nc_ss=7a3ba&oh=00_Af2gAwyGDTJsSZIWK7RKLC78UADfHnklUTlBicotOI3wPg&oe=69DC69B1",
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=XbeNvhLXv28Q7kNvwGV2pZZ&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af04MaARBsHdrXVGZdjaFpwgLMb23T4qigW86xTtc453Dw&oe=69DC51E9&_nc_sid=6d62aa",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "video_url": "https://scontent-vie1-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwF2U228&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3HxF5ThswLyC5oiueCpfWgeyQbhTCGi33VOBE73d2n6A&oe=69D85C07",
    "video_duration": 13.765999794006348,
    "sponsor_tags": [
      {
        "pk": "304662892",
        "id": "304662892",
        "username": "prada",
        "full_name": "Prada",
        "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=vY0PvLetHQgQ7kNvwFYYgc7&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af3PQkoNPwVv8LFdh0FdUdqS0CCt0B_JInWGoMjPVhmp0A&oe=69DC58F0&_nc_sid=6d62aa",
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
          "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHvL6r114KBXVBJE_RV_tBoHfsuflLHYm9Lj31kmE_9z35HUAG1U74zrCh6eWKTyPE&_nc_ohc=vY0PvLetHQgQ7kNvwFYYgc7&_nc_gid=Xop-_QxMyQpqyoyFAiP9Zw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af3PQkoNPwVv8LFdh0FdUdqS0CCt0B_JInWGoMjPVhmp0A&oe=69DC58F0&_nc_sid=6d62aa",
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
