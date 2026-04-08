# Hashtag Endpoints

Get hashtag info, top and recent media.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/hashtag/by/name`](#get-v1hashtagbyname) | [`/v1/hashtag/medias/clips`](#get-v1hashtagmediasclips) | [`/v1/hashtag/medias/clips/chunk`](#get-v1hashtagmediasclipschunk) | [`/v1/hashtag/medias/top`](#get-v1hashtagmediastop) | [`/v1/hashtag/medias/top/chunk`](#get-v1hashtagmediastopchunk) | [`/v1/hashtag/medias/top/recent/chunk`](#get-v1hashtagmediastoprecentchunk)

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

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/by/name",
        headers={"x-access-key": "YOUR_TOKEN"},
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

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/clips",
        headers={"x-access-key": "YOUR_TOKEN"},
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
    "pk": "3870771007451871805",
    "id": "3870771007451871805_375121505",
    "code": "DW3vbkaDLo9",
    "taken_at": "2026-04-08T12:38:17Z",
    "taken_at_ts": 1775651897,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "375121505",
      "id": "375121505",
      "username": "fallinginsociety",
      "full_name": "FallingInSociety",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 5,
    "comments_disabled": false,
    "like_count": 416,
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
          23532,
          35299
        ],
        "height": 1101,
        "scans_profile": "e35",
        "url": "https://scontent-sea5-1.cdninstagram.com/...",
        "width": 1079,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870855071546483116",
    "id": "3870855071546483116_375121505",
    "code": "DW4Ci3MjCGs",
    "taken_at": "2026-04-08T15:25:08Z",
    "taken_at_ts": 1775661908,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "375121505",
      "id": "375121505",
      "username": "fallinginsociety",
      "full_name": "FallingInSociety",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 3,
    "comments_disabled": false,
    "like_count": 325,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "24 year olds deserve it",
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
          11957,
          23915,
          35873
        ],
        "height": 1440,
        "scans_profile": "e35",
        "url": "https://scontent-sea5-1.cdninstagram.com/...",
        "width": 1440,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870743885521623606",
    "id": "3870743885521623606_71436013584",
    "code": "DW3pQ5JCBo2",
    "taken_at": "2026-04-08T11:46:26Z",
    "taken_at_ts": 1775648786,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "71436013584",
      "id": "71436013584",
      "username": "jesuslovesyou2620",
      "full_name": "Grandma",
      "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 22,
    "comments_disabled": false,
    "like_count": 337,
    "play_count": 2093,
    "has_liked": false,
    "caption_text": "#jesuslovesyou #grandma #Jesus #Christian #love",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-sea1-1.cdninstagram.com/...",
    "view_count": 0,
    "video_duration": 79.8280029296875,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          10891,
          21783,
          32675
        ],
        "height": 1136,
        "scans_profile": "e15",
        "url": "https://scontent-sea5-1.cdninstagram.com/...",
        "width": 640,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 798880,
        "height": 1280,
        "id": "1577230313379737v",
        "type": 101,
        "url": "https://scontent-sea1-1.cdninstagram.com/...",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  }
]
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
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_clips_chunk_v1(name="love")
    # Next page: cl.hashtag_medias_clips_chunk_v1(name="love", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"name": "love"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
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
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 416,
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
            23532,
            35299
          ],
          "height": 1101,
          "scans_profile": "e35",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 1079,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870878037013437314",
      "id": "3870878037013437314_61776189307",
      "code": "DW4HxDdDBuC",
      "taken_at": "2026-04-08T16:11:15Z",
      "taken_at_ts": 1775664675,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": {
        "pk": 414026382653741,
        "name": "Limassol, Cyprus",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 33.092566668898,
        "lat": 34.700580757465,
        "external_id": "414026382653741",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "61776189307",
        "id": "61776189307",
        "username": "feelloveheal.live",
        "full_name": "✍️",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 3,
      "comments_disabled": false,
      "like_count": 710,
      "play_count": 16033,
      "has_liked": false,
      "caption_text": "#love #quotes #cyprus #instagram #sea",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 34.73500061035156,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            8483,
            16966,
            25450
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 428616,
          "height": 1280,
          "id": "1331715915447731v",
          "type": 101,
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "68137148105",
          "pk": 68137148105,
          "pk_id": "68137148105",
          "id": "68137148105",
          "username": "en_psixi",
          "full_name": "",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3822113780445062331_68137148105",
          "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
        },
        {
          "strong_id__": "59386353188",
          "pk": 59386353188,
          "pk_id": "59386353188",
          "id": "59386353188",
          "username": "_eros.a",
          "full_name": "ἔ ρ ω ς",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3091603214372483610_59386353188",
          "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
        }
      ],
      "is_paid_partnership": false
    },
    {
      "pk": "3870855071546483116",
      "id": "3870855071546483116_375121505",
      "code": "DW4Ci3MjCGs",
      "taken_at": "2026-04-08T15:25:08Z",
      "taken_at_ts": 1775661908,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 3,
      "comments_disabled": false,
      "like_count": 325,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "24 year olds deserve it",
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
            11957,
            23915,
            35873
          ],
          "height": 1440,
          "scans_profile": "e35",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 1440,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WyIzMzBmNzAyNDkxM2Y0MzYyOWY4NjliNGNhYjJiODYxZCIsW10sMV0="
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

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top",
        headers={"x-access-key": "YOUR_TOKEN"},
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
    "pk": "3870768597966942446",
    "id": "3870768597966942446_73780082474",
    "code": "DW3u4gZjnDu",
    "taken_at": "2026-04-08T12:37:32Z",
    "taken_at_ts": 1775651852,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "73780082474",
      "id": "73780082474",
      "username": "1malachimitchell",
      "full_name": "Malachi “The Messenger”",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 8,
    "comments_disabled": false,
    "like_count": 463,
    "play_count": 3822,
    "has_liked": false,
    "caption_text": "Anything outside the Will & Word of God is a DANGER ZONE!!\n•\n•\n•\n#explorepage✨ #explore #prayer #worship #anointed #ʙɪʙʟᴇsᴛᴜᴅʏ #messiah #christianity #praiseandworship #fyp #reelsinstagram #amazinggrace #ᴊᴇsᴜsʟᴏᴠᴇsʏᴏᴜ #peace #joy #ɢᴏᴅɪsɢᴏᴏᴅ #spreadthegospel #faith #love #holyspirit #faithfulness #christfollower",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-dfw5-1.cdninstagram.com/...",
    "view_count": 0,
    "video_duration": 47.48400115966797,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          7509,
          15019,
          22529
        ],
        "height": 1136,
        "scans_profile": "e15",
        "url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "width": 640,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1640242,
        "height": 1280,
        "id": "2187892455288229v",
        "type": 101,
        "url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870771007451871805",
    "id": "3870771007451871805_375121505",
    "code": "DW3vbkaDLo9",
    "taken_at": "2026-04-08T12:38:17Z",
    "taken_at_ts": 1775651897,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "375121505",
      "id": "375121505",
      "username": "fallinginsociety",
      "full_name": "FallingInSociety",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 5,
    "comments_disabled": false,
    "like_count": 416,
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
          23532,
          35299
        ],
        "height": 1101,
        "scans_profile": "e35",
        "url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "width": 1079,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870787133267296530",
    "id": "3870787133267296530_9816762",
    "code": "DW3zGOvjMES",
    "taken_at": "2026-04-08T13:10:18Z",
    "taken_at_ts": 1775653818,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
    "location": null,
    "user": {
      "pk": "9816762",
      "id": "9816762",
      "username": "nocap",
      "full_name": "No Cap",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 3,
    "comments_disabled": false,
    "like_count": 297,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "the greatest human experience",
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
          9548,
          19097,
          28646
        ],
        "height": 1350,
        "scans_profile": "e35",
        "url": "https://scontent-dfw6-1.cdninstagram.com/...",
        "width": 1080,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  }
]
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
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_chunk_v1(name="love")
    # Next page: cl.hashtag_medias_top_chunk_v1(name="love", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"name": "love"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870878037013437314",
      "id": "3870878037013437314_61776189307",
      "code": "DW4HxDdDBuC",
      "taken_at": "2026-04-08T16:11:15Z",
      "taken_at_ts": 1775664675,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": {
        "pk": 414026382653741,
        "name": "Limassol, Cyprus",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 33.092566668898,
        "lat": 34.700580757465,
        "external_id": "414026382653741",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "61776189307",
        "id": "61776189307",
        "username": "feelloveheal.live",
        "full_name": "✍️",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 3,
      "comments_disabled": false,
      "like_count": 708,
      "play_count": 16001,
      "has_liked": false,
      "caption_text": "#love #quotes #cyprus #instagram #sea",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 34.73500061035156,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            8483,
            16966,
            25450
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 428616,
          "height": 1280,
          "id": "1331715915447731v",
          "type": 101,
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "68137148105",
          "pk": 68137148105,
          "pk_id": "68137148105",
          "id": "68137148105",
          "username": "en_psixi",
          "full_name": "",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3822113780445062331_68137148105",
          "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
        },
        {
          "strong_id__": "59386353188",
          "pk": 59386353188,
          "pk_id": "59386353188",
          "id": "59386353188",
          "username": "_eros.a",
          "full_name": "ἔ ρ ω ς",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3091603214372483610_59386353188",
          "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/..."
        }
      ],
      "is_paid_partnership": false
    },
    {
      "pk": "3870756630392485359",
      "id": "3870756630392485359_75057789494",
      "code": "DW3sKWuiDXv",
      "taken_at": "2026-04-08T12:11:02Z",
      "taken_at_ts": 1775650262,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "75057789494",
        "id": "75057789494",
        "username": "lucifa_therapper",
        "full_name": "LucifaTheRapper",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 80,
      "comments_disabled": false,
      "like_count": 1258,
      "play_count": 18603,
      "has_liked": false,
      "caption_text": "#islam #love #muslim #peace #family",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 37.70000076293945,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            8682,
            17365,
            26048
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 938321,
          "height": 1280,
          "id": "2021399742138766v",
          "type": 101,
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870800882389149027",
      "id": "3870800882389149027_44253208819",
      "code": "DW32OTnEuVj",
      "taken_at": "2026-04-08T13:38:59Z",
      "taken_at_ts": 1775655539,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "44253208819",
        "id": "44253208819",
        "username": "___.roshann00",
        "full_name": " Roshan",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 8,
      "comments_disabled": false,
      "like_count": 465,
      "play_count": 5599,
      "has_liked": false,
      "caption_text": "Paro🩶🎶\n.\n.\n.\n.\n.\n#trending #love #hindi #reels #instagood",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 34.566001892089844,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            9787,
            19574,
            29361
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 0,
          "height": 1280,
          "id": "1258660423130792v",
          "type": 101,
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WyI1YzdlY2Q2MmYzODg0MWVjODYwZWEwZDg0N2MzNDQ2ZiIsW10sMV0="
]
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
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_recent_chunk_v1(name="love")
    # Next page: cl.hashtag_medias_top_recent_chunk_v1(name="love", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"name": "love"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870768642929551615",
      "id": "3870768642929551615_45214193439",
      "code": "DW3u5KRiWj_",
      "taken_at": "2026-04-08T12:36:14Z",
      "taken_at_ts": 1775651774,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "45214193439",
        "id": "45214193439",
        "username": "bhoomika.ammu_official",
        "full_name": "Roopa Ammu",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 19,
      "comments_disabled": false,
      "like_count": 1418,
      "play_count": 16544,
      "has_liked": false,
      "caption_text": "❤️❤️❤️❤️jogi\n#instagram #trending #reels #love #reelitfeelit",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 29.743999481201172,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            3332,
            6665,
            9998
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1477734,
          "height": 1280,
          "id": "2146509629455334v",
          "type": 101,
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870771007451871805",
      "id": "3870771007451871805_375121505",
      "code": "DW3vbkaDLo9",
      "taken_at": "2026-04-08T12:38:17Z",
      "taken_at_ts": 1775651897,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 416,
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
            23532,
            35299
          ],
          "height": 1101,
          "scans_profile": "e35",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 1079,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870732292641548189",
      "id": "3870732292641548189_477970295",
      "code": "DW3moMbiGed",
      "taken_at": "2026-04-08T11:22:21Z",
      "taken_at_ts": 1775647341,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "location": null,
      "user": {
        "pk": "477970295",
        "id": "477970295",
        "username": "tromsoarcticreindeer",
        "full_name": "Tromsø Arctic Reindeer",
        "profile_pic_url": "https://scontent-otp1-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 56,
      "comments_disabled": false,
      "like_count": 984,
      "play_count": 16383,
      "has_liked": false,
      "caption_text": "Thank you world, thank you life ❤️ Thank  you team, friends and family ❤️. Thank you guests from all over the world 🤩.\nLast week was our last in winterhome and already now we've migrated up to the mountains 🏔️ We'll stay here with the herd for a while when the calves will be born in wildlife and we'll be the silent observers to keep them safe from predators.\nThis season was incredible with so many memories made, new friendships as well as old been nourished until we meet again ❤️.\nThe wilderness is calling 🦌. Stay tuned for mountain and reindeer baby update 🤩\n\n#love #friendship #community #reindeer #traveltheworld",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-otp1-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 27.143999099731445,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            6594,
            13189,
            19784
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 2000548,
          "height": 1280,
          "id": "26888921610705337v",
          "type": 101,
          "url": "https://scontent-otp1-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WyJlNDM1NTkwMzZjZjg0ZDIxODdhNzJjY2ZlODI3YjE4NSIsW10sMV0="
]
```

</details>

---

## Deprecated endpoints

These endpoints are still available but will be removed in a future version. Use the recommended alternatives.

### ~~GET /v1/hashtag/medias/recent~~

!!! warning
    Hashtag Medias Recent

### ~~GET /v1/hashtag/medias/recent/chunk~~

!!! warning
    Hashtag Medias Recent Chunk

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-hashtags){ target=_blank }
