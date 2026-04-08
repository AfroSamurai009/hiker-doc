# Hashtag Endpoints

Get hashtag info, top and recent media.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/hashtag/by/name`](#get-v1hashtagbyname) | [`/v1/hashtag/medias/clips`](#get-v1hashtagmediasclips) | [`/v1/hashtag/medias/clips/chunk`](#get-v1hashtagmediasclipschunk) | [`/v1/hashtag/medias/recent`](#get-v1hashtagmediasrecent) | [`/v1/hashtag/medias/recent/chunk`](#get-v1hashtagmediasrecentchunk) | [`/v1/hashtag/medias/top`](#get-v1hashtagmediastop) | [`/v1/hashtag/medias/top/chunk`](#get-v1hashtagmediastopchunk) | [`/v1/hashtag/medias/top/recent/chunk`](#get-v1hashtagmediastoprecentchunk)

---

### GET /v1/hashtag/by/name

Get hashtag object by name. Returns a Hashtag object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/by/name?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_by_name_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/by/name",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/by/name?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "id": "17843826142012701",
  "name": "love",
  "media_count": 2147483647,
  "allow_following": false,
  "profile_pic_url": null
}
```

</details>

---

### GET /v1/hashtag/medias/clips

Get hashtag clips (reels). Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/clips?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_clips_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/clips",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/clips?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870711225189699935",
    "id": "3870711225189699935_501243330",
    "code": "DW3h1n1jJFf",
    "taken_at": "2026-04-08T10:40:30Z",
    "taken_at_ts": 1775644830,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwGtoMIc&_nc_oc=Adp1_liK9CsQNmtO77zecLiRk64oF9Ku_ZDIDKIJlchX5oqc_tguCtJvSvSl0tWyU6c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af0UHG02eXEsEoafbEZo1PUiuDIgPEdOs4shaldkx9jZLw&oe=69DC2620",
    "location": {
      "pk": 1031791313,
      "name": "Davies Coaches LTD",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "The Old Colliery",
      "city": "",
      "zip": null,
      "lng": -4.0678841390208,
      "lat": 51.774418090574,
      "external_id": "272344219549251",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "501243330",
      "id": "501243330",
      "username": "gkfentonn",
      "full_name": "Georgina Fenton",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFnnpySmXw1k1aK86pbe4MoxlhmxXM1Os4rwQBDOhZPEEVBlRdgot8qTkMlWJ_OIG4&_nc_ohc=n-uwrwSVU3kQ7kNvwE0Iokh&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af13lX2tTuFzgncW4FK_dZtI_gDx8h4EzSHIwK0FBE67rA&oe=69DC425F&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 279,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Summer Pending🕶️☀️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n#love\n#instagood\n#photooftheday\n#viral \n#beautiful",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          54433,
          108867
        ],
        "height": 1820,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwGtoMIc&_nc_oc=Adp1_liK9CsQNmtO77zecLiRk64oF9Ku_ZDIDKIJlchX5oqc_tguCtJvSvSl0tWyU6c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af0UHG02eXEsEoafbEZo1PUiuDIgPEdOs4shaldkx9jZLw&oe=69DC2620",
        "width": 1365,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          28402,
          56804
        ],
        "height": 1000,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwGtoMIc&_nc_oc=Adp1_liK9CsQNmtO77zecLiRk64oF9Ku_ZDIDKIJlchX5oqc_tguCtJvSvSl0tWyU6c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af1PB_5Tkzy4gLhQnwt79jACQEkk12Vm4xW0TNhwg7GbLg&oe=69DC2620",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "clips_metadata": {},
    "video_dash_manifest": "",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  // ... truncated
```

</details>

---

### GET /v1/hashtag/medias/clips/chunk

Get hashtag chunk of clips (reels). Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_clips_chunk_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870711225189699935",
      "id": "3870711225189699935_501243330",
      "code": "DW3h1n1jJFf",
      "taken_at": "2026-04-08T10:40:30Z",
      "taken_at_ts": 1775644830,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af3aVaGPcPVah9SWtBfSPfZLCLptSUYpx_kJ-JMtIVapcA&oe=69DC2620",
      "location": {
        "pk": 1031791313,
        "name": "Davies Coaches LTD",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "The Old Colliery",
        "city": "",
        "zip": null,
        "lng": -4.0678841390208,
        "lat": 51.774418090574,
        "external_id": "272344219549251",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "501243330",
        "id": "501243330",
        "username": "gkfentonn",
        "full_name": "Georgina Fenton",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEMZhIY_bp9WhwlOZusB2mSHSOTcr0ePVCgbsEI8n_UbAqkaLduP06FK89T4CQDQro&_nc_ohc=n-uwrwSVU3kQ7kNvwGSmQX6&_nc_gid=BYVilSGza8tgyflbIMxAYA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af3f9_gzF-lK61K5PGbqpmAHybX2UvB9_ClZRNUpeMvE1w&oe=69DC425F&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 279,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Summer Pending🕶️☀️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n#love\n#instagood\n#photooftheday\n#viral \n#beautiful",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            54433,
            108867
          ],
          "height": 1820,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af3aVaGPcPVah9SWtBfSPfZLCLptSUYpx_kJ-JMtIVapcA&oe=69DC2620",
          "width": 1365,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            28402,
            56804
          ],
          "height": 1000,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af0fDaOpl852zkqCXzllFCbnD_hWzPKTchhbfdnaEIZJsA&oe=69DC2620",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "clips_metadata": {},
      "video_dash_manifest": "",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
  // ... truncated
```

</details>

---

### GET /v1/hashtag/medias/recent

Get hashtag medias top. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/recent?name=love"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/recent",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/recent?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[]
```

</details>

---

### GET /v1/hashtag/medias/recent/chunk

Get hashtag chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk?name=love"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  [],
  ""
]
```

</details>

---

### GET /v1/hashtag/medias/top

Get hashtag medias top. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/top?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870711225189699935",
    "id": "3870711225189699935_501243330",
    "code": "DW3h1n1jJFf",
    "taken_at": "2026-04-08T10:40:30Z",
    "taken_at_ts": 1775644830,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEtNuo_&_nc_oc=AdrpL-Xh5mGpeKy3MVPBJ3hfhQgWRjmRxy8pBoE2kIIOIL4ZgZgLNkGEMhBebi2wIRA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af2sVvc6mrsDuPW3PXQbNvyVTcjTytgOJ1WxIXq5MF1tzw&oe=69DC2620",
    "location": {
      "pk": 1031791313,
      "name": "Davies Coaches LTD",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "The Old Colliery",
      "city": "",
      "zip": null,
      "lng": -4.0678841390208,
      "lat": 51.774418090574,
      "external_id": "272344219549251",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "501243330",
      "id": "501243330",
      "username": "gkfentonn",
      "full_name": "Georgina Fenton",
      "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFIqItSnC7PcCl-LBL7YA5WcVzuLyiEXGi1Hak8YXh66eiCRX3MjohNtBe9JDA0Huk&_nc_ohc=n-uwrwSVU3kQ7kNvwEvZN6g&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af1YIalcelNhhL2oUUl31uTPBBrdzT9hObuGwMAwZJ-aEg&oe=69DC425F&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 279,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Summer Pending🕶️☀️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n#love\n#instagood\n#photooftheday\n#viral \n#beautiful",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          54433,
          108867
        ],
        "height": 1820,
        "scans_profile": "e35",
        "url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEtNuo_&_nc_oc=AdrpL-Xh5mGpeKy3MVPBJ3hfhQgWRjmRxy8pBoE2kIIOIL4ZgZgLNkGEMhBebi2wIRA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af2sVvc6mrsDuPW3PXQbNvyVTcjTytgOJ1WxIXq5MF1tzw&oe=69DC2620",
        "width": 1365,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          28402,
          56804
        ],
        "height": 1000,
        "scans_profile": "e35",
        "url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEtNuo_&_nc_oc=AdrpL-Xh5mGpeKy3MVPBJ3hfhQgWRjmRxy8pBoE2kIIOIL4ZgZgLNkGEMhBebi2wIRA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af3LQehtMF54SrEF7b1Db3BkUDzeYkep5pTgtbdeW8nRkQ&oe=69DC2620",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "clips_metadata": {},
    "video_dash_manifest": "",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  // ... truncated
```

</details>

---

### GET /v1/hashtag/medias/top/chunk

Get hashtag chunk of top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/top/chunk?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_chunk_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870771007451871805",
      "id": "3870771007451871805_375121505",
      "code": "DW3vbkaDLo9",
      "taken_at": "2026-04-08T12:38:17Z",
      "taken_at_ts": 1775651897,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af2QoX-FDYeb18bZIu54qlCp5LtNWbYiKBuhA-OJX5uWTA&oe=69DC1EC3",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gG9tmIVEDWPJ7LLSy6oCQAIL59WpG29UKCAgojAuhRUXe0QH2WYMGE3cqmO3C5cuzE&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=sr9EZbdQVEkBThdVobfVVg&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af309ypqZRK3f4ZxjQ1eJWZP9glWdsu3ratLz2HSM8PRhQ&oe=69DC3771&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 299,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Disney Princess irl",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            11766,
            23532
          ],
          "height": 1101,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af2QoX-FDYeb18bZIu54qlCp5LtNWbYiKBuhA-OJX5uWTA&oe=69DC1EC3",
          "width": 1079,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            7924,
            15848
          ],
          "height": 765,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af1QxuQ1T63hLz4U5uPK9iU75PM-7G66P1fZFt0bQDW4iA&oe=69DC1EC3",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "clips_metadata": {},
      "video_dash_manifest": "",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870796662037942390",
      "id": "3870796662037942390_56596768220",
      "code": "DW31Q5GihB2",
      "taken_at": "2026-04-08T13:29:39Z",
      "taken_at_ts": 1775654979,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/658030355_18005902142880221_4311317524523702353_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc5NjY2MjAzNzk0MjM5MDE4MDA1OTAyMTM2ODgwMjIx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RvLG2O_PqqkQ7kNvwG08eE1&_nc_oc=AdqVAN9AhvNtkbC8yeO31-xt8MlR2IfggNdHNZElPa2BaPqC-ePUyBaixAAJiDGTSkc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af0otvPeaZYt2i_yzbTAwrmf5CUDzmgQHWWNzHfnhSnzGg&oe=69DC49F6",
      "location": null,
      "user": {
        "pk": "56596768220",
        "id": "56596768220",
  // ... truncated
```

</details>

---

### GET /v1/hashtag/medias/top/recent/chunk

Get hashtag chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_recent_chunk_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870797517055833010",
      "id": "3870797517055833010_47906970587",
      "code": "DW31dVZk7Oy",
      "taken_at": "2026-04-08T13:30:43Z",
      "taken_at_ts": 1775655043,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": null,
      "user": {
        "pk": "47906970587",
        "id": "47906970587",
        "username": "nani_kranthi_07",
        "full_name": "𝐍𝐚𝐧𝐢_𝐊𝐫𝐚𝐧𝐭𝐡𝐢💗",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/633049469_18079785680594588_8147815449926346534_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFsnXq-IF3enaJnlXzEWVetMlpXOxRTwSNe4AciIv9wutVSg1WOub7voOEQ3o8QmZ8&_nc_ohc=B4ltc3Tug3cQ7kNvwGju5lg&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GH2RuyWcZhsjeDtAACanTJT72hJxbmNDAQAB1501500j-ccb7-5&oh=00_Af2lYfwX93SFcV1vOxiJRgqQDmSGT3iyfsXwtjZxRDdKXQ&oe=69DC1E90&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 30,
      "comments_disabled": false,
      "like_count": 3,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "✨🖤\n\n#new #post #love #fyp #viral",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870797366237059175",
          "id": "3870797366237059175_47906970587",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af0e23xooBLwuubg8YD-fA-MlwVvdB-sOW0Fev0zdAou6A&oe=69DC2D35",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                21233,
                42467
              ],
              "height": 1440,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af0e23xooBLwuubg8YD-fA-MlwVvdB-sOW0Fev0zdAou6A&oe=69DC2D35",
              "width": 1080,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                14288,
                28577
              ],
              "height": 1000,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af1IrtHkxIZTIyp04_2oFx4HUZ_T6Bm_S-YKVwS6_1p7_A&oe=69DC2D35",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870797517055833010_47906970587",
          "commerciality_status": "not_commercial",
          "taken_at": 1775655042
        },
        {
          "pk": "3870797366941648411",
          "id": "3870797366941648411_47906970587",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661703299_18086365946594588_7065368417728275359_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc5NzM2Njk0MTY0ODQxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=h-RHe-FqlLgQ7kNvwGSpwwJ&_nc_oc=AdqtYRv8Ed4SzzP26mvWZ7PZVYr7smotU5lv35xgzOi44A14305RedWT5RvulcF8Anw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af2cy3Si90Pdau17LUOF82-RT6glfTYn8R_gWJSx4WAhaw&oe=69DC3BF1",
          "media_type": 1,
          "product_type": "carousel_item",
  // ... truncated
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-hashtags){ target=_blank }
