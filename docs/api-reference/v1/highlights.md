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
      "https://api.hikerapi.com/v1/highlight/by/id?id=17893209825281221"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/highlight/by/id",
        headers=headers,
        params={"id": "17893209825281221"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/highlight/by/id?id=17893209825281221",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "17893209825281221",
  "id": "highlight:17893209825281221",
  "latest_reel_media": 1752840788,
  "cover_media": {
    "cropped_image_version": {
      "width": 150,
      "height": 150,
      "url": "https://scontent-mia3-2.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gE0s41WuNy0-zQX-RtSe26Xv6IeS58ejYGHR49-uRfJtFooM9aqxNSyQmMB93qRbLM&_nc_ohc=-NOYVJuE190Q7kNvwFvtwte&_nc_gid=b6vFTRdxpMI2hf6PwftUzg&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af3XpQj9ieemfiJoi0_GkJZWF9SHTiqGYQEYYVdbmD_nRg&oe=69DC1EDC&_nc_sid=982cc7",
      "scans_profile": ""
    },
    "crop_rect": null,
    "media_id": null,
    "full_image_version": null,
    "upload_id": null
  },
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-mia3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE0s41WuNy0-zQX-RtSe26Xv6IeS58ejYGHR49-uRfJtFooM9aqxNSyQmMB93qRbLM&_nc_ohc=XbeNvhLXv28Q7kNvwGUXSRK&_nc_gid=b6vFTRdxpMI2hf6PwftUzg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0joYl1hEzNkWoy2t2qqva8hHZXAmldeAkfOSn3Sy6zsw&oe=69DC51E9&_nc_sid=982cc7",
    "profile_pic_url_hd": null,
    "is_private": false,
    "is_verified": true
  },
  "title": "Limitless",
  "created_at": "2025-08-08T17:33:52+00:00",
  "is_pinned_highlight": false,
  "media_count": 11,
  "media_ids": [
    3679002956306686062,
    3679012649209069648
  ],
  "items": [
    {
      "pk": "3679002956306686062",
      "id": "3679002956306686062_787132",
      "code": "DMOcbJSRaBu",
      "taken_at": "2025-07-17T22:29:06+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/520978025_1226610042597033_6340514479679745090_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=MzY3OTAwMjk1NjMwNjY4NjA2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=MimHeG00MjQQ7kNvwFhTViL&_nc_oc=AdogKW0jyw3-MhCnG4b26KJaA2otKMKuPQC09sV0tbABzsosrL3HT0hQhamm3AP6hFI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=b6vFTRdxpMI2hf6PwftUzg&_nc_ss=7a3ba&oh=00_Af3WfHWvwFwOJc5D00OypTApvqVlbCn0qhN3BeDUjxllaA&oe=69DC2CAC",
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNDhHXDqZMqEz2slWNYcNv06IoY5n7k49HZ3iv4nxW5Kw9FpM6EgIUAKO-HPNATzt8wE6X_JGrfEWLi_Ygiv4q9qqXOseNVFOmJJRs.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_ohc=wMrxuyskfRQQ7kNvwH5NwFc&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTQzNTg5MjI1NDEyNzc5MiwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e5e224354dcd99b5&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC8wOTRGQTM1OURGMkQzRDIwMEM1QTFDRThBRjY3NzJBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRGxTSFI4bGdXZXJOemdDQUFCUmtsZnFJemtjYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm4Nrx-_b7jAUVAigCQzMsF0Avu2RaHKwIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=b6vFTRdxpMI2hf6PwftUzg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3knjFLxK26TN0BjfRSfccLoos5wQHb4-wT6H7IgjnyeA&oe=69DC3F36",
      "video_duration": 15.866000175476074,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "191074609",
            "id": "191074609",
            "username": "hulu",
            "full_name": "Hulu",
            "profile_pic_url": "https://scontent-mia3-1.cdninstagram.com/v/t51.82787-19/574400438_18538966897034610_4563057389814688225_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDc5LmMyIn0&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE0s41WuNy0-zQX-RtSe26Xv6IeS58ejYGHR49-uRfJtFooM9aqxNSyQmMB93qRbLM&_nc_ohc=MW84984-PUoQ7kNvwHGsnQ-&_nc_gid=b6vFTRdxpMI2hf6PwftUzg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLanPCJyhWaYF91BAOEpoBmFPFM-bmNDAQAB1501500j-ccb7-5&oh=00_Af1VNiOXjuJqyIUCk-c44X2py_lKFPgwKLNr0N6a-CSFiw&oe=69DC3924&_nc_sid=982cc7",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.0,
          "y": 0.0,
          "width": 0.0,
          "height": 0.0
        },
        {
          "user": {
            "pk": "1822594644",
            "id": "1822594644",
            "username": "chrishemsworth",
            "full_name": "Chris Hemsworth",
            "profile_pic_url": "https://scontent-mia3-1.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE0s41WuNy0-zQX-RtSe26Xv6IeS58ejYGHR49-uRfJtFooM9aqxNSyQmMB93qRbLM&_nc_ohc=bzOXlq22QsMQ7kNvwG-4DDN&_nc_gid=b6vFTRdxpMI2hf6PwftUzg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af3vMcJEh0HDGK3pDdun3Nnl_ugIjlhyQLajQkvn-NJdpg&oe=69DC42B4&_nc_sid=982cc7",
  // ... truncated
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
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/17893209825281221/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.highlight_by_url_v1(url="https://www.instagram.com/stories/highlights/17893209825281221/")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/highlight/by/url",
        headers=headers,
        params={"url": "https://www.instagram.com/stories/highlights/17893209825281221/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/17893209825281221/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "17893209825281221",
  "id": "highlight:17893209825281221",
  "latest_reel_media": 1752840788,
  "cover_media": {
    "cropped_image_version": {
      "width": 150,
      "height": 150,
      "url": "https://scontent-arn2-1.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHbtp8Ec6MMb1CSariyMlpIzzCmecUeDgrL2mJlRUJV3HhhaXJx4PMH6mWhp9BvKVM&_nc_ohc=-NOYVJuE190Q7kNvwHzBucI&_nc_gid=a86ujsH4JVRFRl17wcVg6g&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af0ODpSTZC0DZEj-0PlOtJBMtkqJRIwlXdqnXhaFmOh31g&oe=69DC1EDC&_nc_sid=982cc7",
      "scans_profile": ""
    },
    "crop_rect": null,
    "media_id": null,
    "full_image_version": null,
    "upload_id": null
  },
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-arn2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHbtp8Ec6MMb1CSariyMlpIzzCmecUeDgrL2mJlRUJV3HhhaXJx4PMH6mWhp9BvKVM&_nc_ohc=XbeNvhLXv28Q7kNvwGZP_yZ&_nc_gid=a86ujsH4JVRFRl17wcVg6g&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2HERIyf1iXQAnEFnO3A-3Q2LjreKx4t8N-ynp71V3Drg&oe=69DC51E9&_nc_sid=982cc7",
    "profile_pic_url_hd": null,
    "is_private": false,
    "is_verified": true
  },
  "title": "Limitless",
  "created_at": "2025-08-08T17:33:52+00:00",
  "is_pinned_highlight": false,
  "media_count": 11,
  "media_ids": [
    3679002956306686062,
    3679012649209069648
  ],
  "items": [
    {
      "pk": "3679002956306686062",
      "id": "3679002956306686062_787132",
      "code": "DMOcbJSRaBu",
      "taken_at": "2025-07-17T22:29:06+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-arn2-1.cdninstagram.com/v/t51.71878-15/520978025_1226610042597033_6340514479679745090_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=MzY3OTAwMjk1NjMwNjY4NjA2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=MimHeG00MjQQ7kNvwHqegYb&_nc_oc=Adr1cSpA_Q6nvdgY39wvbuqzQeU0ofbs8akdSpM6Ar8PFog6MMHSrCu2F_JjQJqvppw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_gid=a86ujsH4JVRFRl17wcVg6g&_nc_ss=7a3ba&oh=00_Af1WbVUT-uLV5VlWo6ocNwaJNkbD89kY1edU_gVxDXmxMA&oe=69DC2CAC",
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": null,
        "full_name": "",
        "profile_pic_url": null,
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": null
      },
      "video_url": "https://scontent-arn2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNDhHXDqZMqEz2slWNYcNv06IoY5n7k49HZ3iv4nxW5Kw9FpM6EgIUAKO-HPNATzt8wE6X_JGrfEWLi_Ygiv4q9qqXOseNVFOmJJRs.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_ohc=wMrxuyskfRQQ7kNvwEvI9aG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTQzNTg5MjI1NDEyNzc5MiwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e5e224354dcd99b5&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC8wOTRGQTM1OURGMkQzRDIwMEM1QTFDRThBRjY3NzJBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRGxTSFI4bGdXZXJOemdDQUFCUmtsZnFJemtjYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm4Nrx-_b7jAUVAigCQzMsF0Avu2RaHKwIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=a86ujsH4JVRFRl17wcVg6g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af29S3FTOiB75LFD5QIZVBxmDX4KXYyDY8cEEeUjBmOIOw&oe=69DC3F36",
      "video_duration": 15.866000175476074,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "191074609",
            "id": "191074609",
            "username": "hulu",
            "full_name": "Hulu",
            "profile_pic_url": "https://scontent-arn2-1.cdninstagram.com/v/t51.82787-19/574400438_18538966897034610_4563057389814688225_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDc5LmMyIn0&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHbtp8Ec6MMb1CSariyMlpIzzCmecUeDgrL2mJlRUJV3HhhaXJx4PMH6mWhp9BvKVM&_nc_ohc=MW84984-PUoQ7kNvwGZdA8q&_nc_gid=a86ujsH4JVRFRl17wcVg6g&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLanPCJyhWaYF91BAOEpoBmFPFM-bmNDAQAB1501500j-ccb7-5&oh=00_Af3Q_TijjA5bJgte3owk9dsd3gSHo7VvQBbECMS0YGUSkg&oe=69DC3924&_nc_sid=982cc7",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.0,
          "y": 0.0,
          "width": 0.0,
          "height": 0.0
        },
        {
          "user": {
            "pk": "1822594644",
            "id": "1822594644",
            "username": "chrishemsworth",
            "full_name": "Chris Hemsworth",
            "profile_pic_url": "https://scontent-arn2-1.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHbtp8Ec6MMb1CSariyMlpIzzCmecUeDgrL2mJlRUJV3HhhaXJx4PMH6mWhp9BvKVM&_nc_ohc=bzOXlq22QsMQ7kNvwGeiMpt&_nc_gid=a86ujsH4JVRFRl17wcVg6g&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af1_XeYO2j1AIWuIyDP1a7ep9s6ojZNcNHGH5vqQzUNDhQ&oe=69DC42B4&_nc_sid=982cc7",
  // ... truncated
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights",
        headers=headers,
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
        "url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gH8xzhMx7WLDumifXG9QVH6rUAXRYtKPM9GlA7Y1NQhuwO0kp6x_AS-IDkgDw4yYm4&_nc_ohc=y1uvOTY1dWMQ7kNvwEcCJ1N&_nc_gid=kM5UaDPaLxgbQFHt4nMjXA&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af0-lLYEUNFq9pg2JqAj9wTFWuurjUgcFt5BVQTPIpboJQ&oe=69DC397C&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH8xzhMx7WLDumifXG9QVH6rUAXRYtKPM9GlA7Y1NQhuwO0kp6x_AS-IDkgDw4yYm4&_nc_ohc=XbeNvhLXv28Q7kNvwGV2pZZ&_nc_gid=kM5UaDPaLxgbQFHt4nMjXA&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0Rwwmr7dR6InebKfFz_KUoId-JL2ZnisHTCPOugIc_tQ&oe=69DC19A9&_nc_sid=847350",
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
        "url": "https://scontent-vie1-1.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gH8xzhMx7WLDumifXG9QVH6rUAXRYtKPM9GlA7Y1NQhuwO0kp6x_AS-IDkgDw4yYm4&_nc_ohc=KnNItKNMJcAQ7kNvwGEjQ0G&_nc_gid=kM5UaDPaLxgbQFHt4nMjXA&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af3WjcocUx7zQYzbmexy7s5pEFyl-ljpoQ-Mmmutexi85w&oe=69DC19F3&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH8xzhMx7WLDumifXG9QVH6rUAXRYtKPM9GlA7Y1NQhuwO0kp6x_AS-IDkgDw4yYm4&_nc_ohc=XbeNvhLXv28Q7kNvwGV2pZZ&_nc_gid=kM5UaDPaLxgbQFHt4nMjXA&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0Rwwmr7dR6InebKfFz_KUoId-JL2ZnisHTCPOugIc_tQ&oe=69DC19A9&_nc_sid=847350",
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights/by/username",
        headers=headers,
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
        "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gGYTBmsZVMRpsXOJhrhiZLO09zSclKoS0CtODTpYemEgOWJvdTVsByi6w92YYecY_Q&_nc_ohc=y1uvOTY1dWMQ7kNvwGZpR_l&_nc_gid=JPwD_XCPTkdSYEmXoBNgig&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af38vt8d3wfWzp5DQxvpPm08L_vzBC4gFhSBXSe7H1GL3Q&oe=69DC397C&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-mia3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGYTBmsZVMRpsXOJhrhiZLO09zSclKoS0CtODTpYemEgOWJvdTVsByi6w92YYecY_Q&_nc_ohc=XbeNvhLXv28Q7kNvwGU-0Tc&_nc_gid=JPwD_XCPTkdSYEmXoBNgig&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0Z5qKG8YHWAN_D-aO2yRYhoJ6rhvsiWvRYmGha1aY4Tw&oe=69DC19A9&_nc_sid=847350",
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
        "url": "https://scontent-mia5-1.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-mia5-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gGYTBmsZVMRpsXOJhrhiZLO09zSclKoS0CtODTpYemEgOWJvdTVsByi6w92YYecY_Q&_nc_ohc=KnNItKNMJcAQ7kNvwEryBOC&_nc_gid=JPwD_XCPTkdSYEmXoBNgig&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af1WBItclxte1Q4SGeb3lydUQMsAr7MPfm1vDIRe82gnLw&oe=69DC19F3&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-mia3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGYTBmsZVMRpsXOJhrhiZLO09zSclKoS0CtODTpYemEgOWJvdTVsByi6w92YYecY_Q&_nc_ohc=XbeNvhLXv28Q7kNvwGU-0Tc&_nc_gid=JPwD_XCPTkdSYEmXoBNgig&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0Z5qKG8YHWAN_D-aO2yRYhoJ6rhvsiWvRYmGha1aY4Tw&oe=69DC19A9&_nc_sid=847350",
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
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-highlights){ target=_blank }
