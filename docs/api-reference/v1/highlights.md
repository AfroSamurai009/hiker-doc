# Highlights Endpoints

Get story highlights by ID or URL.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/highlight/by/id`](#get-v1highlightbyid) | [`/v1/highlight/by/url`](#get-v1highlightbyurl) | [`/v1/user/highlights`](#get-v1userhighlights) | [`/v1/user/highlights/by/username`](#get-v1userhighlightsbyusername)

---

### GET /v1/highlight/by/id

Prefer v2/highlight/by/id. Returns a Highlight object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/highlight/by/id?id=18085475671830440"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/highlight/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "18085475671830440"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/highlight/by/id?id=18085475671830440",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "18085475671830440",
  "id": "highlight:18085475671830440",
  "latest_reel_media": 1773304526,
  "cover_media": {
    "cropped_image_version": {
      "width": 150,
      "height": 150,
      "url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.82787-15/649485671_17878703184529120_5378486390545016366_n.jpg?stp=c0.772.1440.1440a_dst-jpg_e15_s150x150_tt6&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=104&_nc_oc=Q6cZ2gGoWhSYaMuXJAQfLmfEKtBEj8k-Khyc_tq9O-fJAYDzqRVCvP2jfRA_3VNsuVfgczo&_nc_ohc=MJ8q8O6o15UQ7kNvwE6QDIE&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af0AFMEZrj5g3-oxk7ig6y801T0_S3_Qq-285YAPuqVmcw&oe=69DC5BBB&_nc_sid=982cc7",
      "scans_profile": ""
    },
    "crop_rect": [
      0.0,
      0.30167106,
      1.0
    ],
    "media_id": "3849652044117864571_75885841119",
    "full_image_version": null,
    "upload_id": null
  },
  "user": {
    "pk": "75885841119",
    "id": "75885841119",
    "username": "salwaaa_ki",
    "full_name": "𓆩سلوى 𓆪",
    "profile_pic_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.82787-19/660301771_17883534429529120_6857519161323086524_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_cat=104&_nc_oc=Q6cZ2gGoWhSYaMuXJAQfLmfEKtBEj8k-Khyc_tq9O-fJAYDzqRVCvP2jfRA_3VNsuVfgczo&_nc_ohc=NP_MmBl4lA4Q7kNvwG6k69S&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GMtnWycgJADV_og-ALziGDNYzSpfbmNDAQAB1501500j-ccb7-5&oh=00_Af3FbCZobqRKi4dvZOndqgS-Gq86fKjPk77zO-HRrIPNWg&oe=69DC55BF&_nc_sid=982cc7",
    "profile_pic_url_hd": null,
    "is_private": false,
    "is_verified": false
  },
  "title": "me 🦋",
  "created_at": "2025-11-26T06:32:13+00:00",
  "is_pinned_highlight": false,
  "media_count": 98,
  "media_ids": [
    3772053608293416704,
    3773586006193708855,
    3777839902093167269
  ],
  "items": [
    {
      "pk": "3772053608293416704",
      "id": "3772053608293416704_75885841119",
      "code": "DRZBsWEDz8A",
      "taken_at": "2025-11-23T07:44:11+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.82787-15/588461508_17863934817529120_8595336332983327927_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzc3MjA1MzYwODI5MzQxNjcwNA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=SdDsQh8WTPEQ7kNvwFyRWbt&_nc_oc=AdqDd2XZlnKjtlU48ApR2yhaCbbLYITxmnuC8bnZF2Qf7vGQLu0oYq4KKvGxPZShv_E&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.ftia13-1.fna&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&_nc_ss=7a3ba&oh=00_Af08LxO40wikEDnnd7BC8MKCqIC8x5-gugz-B6QTSnG2tA&oe=69DC576A",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://instagram.ftia13-1.fna.fbcdn.net/o1/v/t2/f2/m78/AQM4454MqF2Hx4p0JOmr3z8YBeoIoKV09Zv1Olvgqw_q2QRA6kfJgBdXiqE4RRda5R47rkZ_juiMq8rESlIW7MTaiVtMAW7MVqFWiB4.mp4?_nc_cat=105&_nc_oc=AdpqTau0YffOjr86ntKu5SWdoPXs4p9024W_i1PjtMrWJZ87kDsrTgqLg4N9Tt_W0pw&_nc_sid=5e9851&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_ohc=tRKBzKqdrfUQ7kNvwFIAmD3&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MjMyMTQyMzEwNDk3NDkxNywiYXNzZXRfYWdlX2RheXMiOjEzNiwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=2f4246a0f95d8fbd&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0Q4NEM4REM2MzE0QTQzRUZEQjk0QzA1RjUxOTVDOEJGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhHaWdfeHB2X3JlZWxzX3Blcm1hbmVudF9zcl9wcm9kLzEzNzg3MjcxNTAyNzY4MDZfMzgxOTMxOTgwNjgzNzc0MDMzNy5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmioHd-M3UnwgVAigCQzMsF0A0AAAAAAAAGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2bDirmkX-ucG7sv7a1sygcZ124AwXdEY477S8k6pbQEQ&oe=69D886EA",
      "video_duration": 20.014999389648438,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    },
    {
      "pk": "3773586006193708855",
      "id": "3773586006193708855_75885841119",
      "code": "DReeHq0j583",
      "taken_at": "2025-11-25T10:28:38+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.71878-15/588154318_728190939725494_5950880813983757081_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ig_cache_key=Mzc3MzU4NjAwNjE5MzcwODg1NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM4LnNkci5DMyJ9&_nc_ohc=RpPP-rAs06gQ7kNvwGjRfiH&_nc_oc=AdpCTkMyFg7hDMjA6T0NvsCo45usLn1z71wMY_bdShpK1rSEmFtWqTQl0yv2WzdDxM8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.ftia13-1.fna&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&_nc_ss=7a3ba&oh=00_Af2EoAQbCj7UnKcBrAQofCQtrYVd5X0j7vewdNtExezf2A&oe=69DC641B",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://instagram.ftia13-1.fna.fbcdn.net/o1/v/t2/f2/m78/AQOUjhHv0lGqQdnEa9pFVkGCLHQivW23hFrzQ-TB2B3PJmkSnN-NxgSpslUdeQJ8KwoJqD6eZR_OPbq3LL9dHr0zmBEyTbnCf9Qj034.mp4?_nc_cat=109&_nc_oc=AdqgItQ9nmj90A-TOMf6zqOGjIHlB7Np7rOC9kwAU96o-xht0Q0CjzZZJvF0JUOUENw&_nc_sid=5e9851&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_ohc=zW5wPjAQE64Q7kNvwFuXeEM&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzE2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6ODU0MTY0MTcwMzQzODg4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNiwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7c7b1bf68b739e99&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U3NDE5QTczMkI3OTAyNjhDRDkzMkFBQTdDNkM2RUExX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhHaWdfeHB2X3JlZWxzX3Blcm1hbmVudF9zcl9wcm9kLzIyMzE2MDE3MDM5ODU4MzBfMjY0MTYyNDkzODUxMzg1OTQ3NS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmoJeg__K2hAMVAigCQzMsF0A0CHKwIMScGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1GlxZI0CVaMyAAZ3SRKWfdCnb6FidPYFcKXpWU7A8TwQ&oe=69D888E2",
      "video_duration": 20.038000106811523,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    },
    {
      "pk": "3777839902093167269",
      "id": "3777839902093167269_75885841119",
      "code": "DRtlWAGj0ql",
      "taken_at": "2025-12-01T07:20:23+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://instagram.ftia13-1.fna.fbcdn.net/v/t51.71878-15/589062762_864740615926830_8379534102917113604_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ig_cache_key=Mzc3NzgzOTkwMjA5MzE2NzI2OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bnnfAV02fxIQ7kNvwHTL4Qp&_nc_oc=Adq2FgayrUcjscUNXT62aG36Q36NaqIEHPRZaV_DR7jMYzG8w9TGzorzP1rLx7Fa5MY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=instagram.ftia13-1.fna&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&_nc_ss=7a3ba&oh=00_Af1s_sdvh_MiD4UUxpfIx1e4JdgTpyjJtQtdZ5FjMQEQuw&oe=69DC7303",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://instagram.ftia13-1.fna.fbcdn.net/o1/v/t2/f2/m78/AQNau6RzELEtOR24qqPISXbOIelAiUNKJjmKX_X_yUtkBJP3icxa9oT4O4uBmWmzXk0ZC1GXflrrKzgK9-_NlP8WwsVSmb6_4yTWJY8.mp4?_nc_cat=106&_nc_oc=AdqEuYDG4vO5yfOVp6tK7mtgPNll7AerdTmpYA7yIsy8VnyVAGmxKqQZwqS0hPRYLfY&_nc_sid=5e9851&_nc_ht=instagram.ftia13-1.fna.fbcdn.net&_nc_ohc=CCbe4i66DY8Q7kNvwHNK4Sl&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6ODgxNjg1NTc3NjU4NDg1LCJhc3NldF9hZ2VfZGF5cyI6MTI4LCJ2aV91c2VjYXNlX2lkIjoxMDgyNiwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=f44d8c2c62e8f694&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzM5NDQyMkEyQTk2Njg3RTBCNDFEODY2NTkyM0IzQjlCX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhGaWdfeHB2X3JlZWxzX3Blcm1hbmVudF9zcl9wcm9kLzg2NTg2NzgyOTMxMzQ2Nl8yMzQ3NTc0MzExNjc1MDk1OTc3Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbqwce67fiQAxUCKAJDMywXQDQIcrAgxJwYEmRhc2hfYmFzZWxpbmVfMV92MREAdegHZZSpAQA&_nc_gid=bxDk6Y-CteuIw7MdBzqrQA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2jgfovwJhQhgZdJbgns3MS82MhJU_Tk2MwUAfO4P57Ag&oe=69D87217",
      "video_duration": 20.038000106811523,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    }
  ]
}
```

</details>

---

### GET /v1/highlight/by/url

Get highlight object by id. Returns a Highlight object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/18085475671830440/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.highlight_by_url_v1(url="https://www.instagram.com/stories/highlights/18085475671830440/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/highlight/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/stories/highlights/18085475671830440/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/18085475671830440/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "18085475671830440",
  "id": "highlight:18085475671830440",
  "latest_reel_media": 1773304526,
  "cover_media": {
    "cropped_image_version": {
      "width": 150,
      "height": 150,
      "url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "scans_profile": ""
    },
    "crop_rect": [
      0.0,
      0.30167106,
      1.0
    ],
    "media_id": "3849652044117864571_75885841119",
    "full_image_version": null,
    "upload_id": null
  },
  "user": {
    "pk": "75885841119",
    "id": "75885841119",
    "username": "salwaaa_ki",
    "full_name": "𓆩سلوى 𓆪",
    "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/...",
    "profile_pic_url_hd": null,
    "is_private": false,
    "is_verified": false
  },
  "title": "me 🦋",
  "created_at": "2025-11-26T06:32:13+00:00",
  "is_pinned_highlight": false,
  "media_count": 98,
  "media_ids": [
    3772053608293416704,
    3773586006193708855,
    3777839902093167269
  ],
  "items": [
    {
      "pk": "3772053608293416704",
      "id": "3772053608293416704_75885841119",
      "code": "DRZBsWEDz8A",
      "taken_at": "2025-11-23T07:44:11+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "video_duration": 20.014999389648438,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    },
    {
      "pk": "3773586006193708855",
      "id": "3773586006193708855_75885841119",
      "code": "DReeHq0j583",
      "taken_at": "2025-11-25T10:28:38+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "video_duration": 20.038000106811523,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    },
    {
      "pk": "3777839902093167269",
      "id": "3777839902093167269_75885841119",
      "code": "DRtlWAGj0ql",
      "taken_at": "2025-12-01T07:20:23+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "user": {
        "pk": "75885841119",
        "id": "75885841119",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "video_duration": 20.038000106811523,
      "sponsor_tags": [],
      "mentions": [],
      "links": [],
      "hashtags": [],
      "locations": [],
      "stickers": [],
      "medias": []
    }
  ]
}
```

</details>

---

### GET /v1/user/highlights

⚠️ Billing: 2 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/highlights?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/highlights?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17983616051768088",
    "id": "highlight:17983616051768088",
    "latest_reel_media": 1766242839,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-lax3-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Gift Guide",
    "created_at": "2025-12-04T11:06:31Z",
    "is_pinned_highlight": false,
    "media_count": 12,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "18018069326790931",
    "id": "highlight:18018069326790931",
    "latest_reel_media": 1762870363,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-lax3-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "BOTW 2026",
    "created_at": "2025-10-21T13:07:47Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "17893209825281221",
    "id": "highlight:17893209825281221",
    "latest_reel_media": 1752840788,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-lax3-2.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Limitless",
    "created_at": "2025-08-08T17:33:52Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  }
]
```

</details>

---

### GET /v1/user/highlights/by/username

⚠️ Billing: 3 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/highlights/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_by_username_v1(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/highlights/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17983616051768088",
    "id": "highlight:17983616051768088",
    "latest_reel_media": 1766242839,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Gift Guide",
    "created_at": "2025-12-04T11:06:31Z",
    "is_pinned_highlight": false,
    "media_count": 12,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "18018069326790931",
    "id": "highlight:18018069326790931",
    "latest_reel_media": 1762870363,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw6-1.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "BOTW 2026",
    "created_at": "2025-10-21T13:07:47Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "17893209825281221",
    "id": "highlight:17893209825281221",
    "latest_reel_media": 1752840788,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Limitless",
    "created_at": "2025-08-08T17:33:52Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-highlights){ target=_blank }
