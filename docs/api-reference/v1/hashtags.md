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
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwHRRFI7&_nc_oc=AdpQjlk9EhAnNfCX0NUq_vRNz-veUt5_mGlHqJJC0erPjOChWcP1Hc-miV5k1piXSTE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af3DyOCUO2KnoN0NofaJceK1z9oGSBBTFiYznQqwY8GKfQ&oe=69DC5703",
    "location": null,
    "user": {
      "pk": "375121505",
      "id": "375121505",
      "username": "fallinginsociety",
      "full_name": "FallingInSociety",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGkaY55LKWayuYPyZFC_mXfodSoR-p6TWy4nq1sc9SBXJrhyjVwBhvVhl_pHf2ZV1Q&_nc_ohc=8UGwMTx74pgQ7kNvwFrV7YW&_nc_gid=VN7KX9fwn22l0qab2OSDag&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af1DLObAd4aQnuaXMj0PiL25cdAKdLZ-Xh5w3iQrP6rVag&oe=69DC3771&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 5,
    "comments_disabled": false,
    "like_count": 387,
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
        "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwHRRFI7&_nc_oc=AdpQjlk9EhAnNfCX0NUq_vRNz-veUt5_mGlHqJJC0erPjOChWcP1Hc-miV5k1piXSTE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af3DyOCUO2KnoN0NofaJceK1z9oGSBBTFiYznQqwY8GKfQ&oe=69DC5703",
        "width": 1079,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          7924,
          15848,
          23772
        ],
        "height": 765,
        "scans_profile": "e35",
        "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwHRRFI7&_nc_oc=AdpQjlk9EhAnNfCX0NUq_vRNz-veUt5_mGlHqJJC0erPjOChWcP1Hc-miV5k1piXSTE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af0jcJYls7DAIP2OaSieobGnWgG1ZuWQTCrDQwDlPfayxQ&oe=69DC5703",
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
    "pk": "3870773039978007674",
    "id": "3870773039978007674_321972094",
    "code": "DW3v5JWDEx6",
    "taken_at": "2026-04-08T12:42:05Z",
    "taken_at_ts": 1775652125,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": null,
    "user": {
      "pk": "321972094",
      "id": "321972094",
      "username": "leandermckl",
      "full_name": "LJM",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/607390274_18553850086052095_8054136568059912714_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGkaY55LKWayuYPyZFC_mXfodSoR-p6TWy4nq1sc9SBXJrhyjVwBhvVhl_pHf2ZV1Q&_nc_ohc=AbkLdVi_YF0Q7kNvwE-Wba7&_nc_gid=VN7KX9fwn22l0qab2OSDag&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GEIKNCT-UJjboOpBAArisTeJCsZvbmNDAQAB1501500j-ccb7-5&oh=00_Af3xInTAlcB6ENFjkmRdqZAxDe5ETWHuUSq1XMh1JhXhEQ&oe=69DC554B&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 17,
    "comments_disabled": false,
    "like_count": 3,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Larp",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870772944096224330",
        "id": "3870772944096224330_321972094",
        "video_url": null,
        "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/661360873_18583030168052095_3048125277147945686_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=109&ig_cache_key=Mzg3MDc3Mjk0NDA5NjIyNDMzMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=Z02V73IW3OkQ7kNvwH-wyK7&_nc_oc=AdqHTispgbHOu5FLXqj-2E6MIbU3AgOwqxP_M4tQhI4E5X8EkrbRHdgOVaA2Biuvnuc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af2a8uWIbApE4VwVLcov1zuc5e4cskNkoG9Bxp9x0lkF1g&oe=69DC5A38",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              24593,
              49186,
              73779
            ],
            "height": 1656,
            "scans_profile": "e35",
            "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/661360873_18583030168052095_3048125277147945686_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=109&ig_cache_key=Mzg3MDc3Mjk0NDA5NjIyNDMzMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=Z02V73IW3OkQ7kNvwH-wyK7&_nc_oc=AdqHTispgbHOu5FLXqj-2E6MIbU3AgOwqxP_M4tQhI4E5X8EkrbRHdgOVaA2Biuvnuc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af2a8uWIbApE4VwVLcov1zuc5e4cskNkoG9Bxp9x0lkF1g&oe=69DC5A38",
            "width": 1242,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              14218,
              28436,
              42654
            ],
            "height": 1000,
            "scans_profile": "e35",
            "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/661360873_18583030168052095_3048125277147945686_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=109&ig_cache_key=Mzg3MDc3Mjk0NDA5NjIyNDMzMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=Z02V73IW3OkQ7kNvwH-wyK7&_nc_oc=AdqHTispgbHOu5FLXqj-2E6MIbU3AgOwqxP_M4tQhI4E5X8EkrbRHdgOVaA2Biuvnuc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af2jfzDtFSRLMLui33ymcChDBxXllEtWJ9gRnkw0Y2v4qA&oe=69DC5A38",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870773039978007674_321972094",
        "commerciality_status": "not_commercial",
        "taken_at": 1775652124
      },
      {
        "pk": "3870772947585916097",
        "id": "3870772947585916097_321972094",
        "video_url": null,
        "thumbnail_url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-15/661843269_18583030177052095_6439199022029790455_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc3Mjk0NzU4NTkxNjA5Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=UOgOS_GrKboQ7kNvwEImnP-&_nc_oc=Ado9yBz6brdmIU8kVQDltlIxlANwhMzLd0ft8cA3l8jsaavXgTDZJDv0-HuLF-7pfOw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af1lqo362TvtpL4HH-Ht6kxw8TdzwmmE6ObJYmT5_kQMDA&oe=69DC4929",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              27753,
              55506,
              83259
            ],
            "height": 1656,
            "scans_profile": "e35",
            "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-15/661843269_18583030177052095_6439199022029790455_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc3Mjk0NzU4NTkxNjA5Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=UOgOS_GrKboQ7kNvwEImnP-&_nc_oc=Ado9yBz6brdmIU8kVQDltlIxlANwhMzLd0ft8cA3l8jsaavXgTDZJDv0-HuLF-7pfOw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af1lqo362TvtpL4HH-Ht6kxw8TdzwmmE6ObJYmT5_kQMDA&oe=69DC4929",
            "width": 1242,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              16045,
              32090,
              48135
            ],
            "height": 1000,
            "scans_profile": "e35",
            "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-15/661843269_18583030177052095_6439199022029790455_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc3Mjk0NzU4NTkxNjA5Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=UOgOS_GrKboQ7kNvwEImnP-&_nc_oc=Ado9yBz6brdmIU8kVQDltlIxlANwhMzLd0ft8cA3l8jsaavXgTDZJDv0-HuLF-7pfOw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af2RDmckhouJZQ1H93sifppIbZUkMX2IeqgrU56j1Tcpwg&oe=69DC4929",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870773039978007674_321972094",
        "commerciality_status": "not_commercial",
        "taken_at": 1775652124
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          24593,
          49186,
          73779
        ],
        "height": 1656,
        "scans_profile": "e35",
        "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/661360873_18583030168052095_3048125277147945686_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=109&ig_cache_key=Mzg3MDc3Mjk0NDA5NjIyNDMzMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=Z02V73IW3OkQ7kNvwH-wyK7&_nc_oc=AdqHTispgbHOu5FLXqj-2E6MIbU3AgOwqxP_M4tQhI4E5X8EkrbRHdgOVaA2Biuvnuc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af2a8uWIbApE4VwVLcov1zuc5e4cskNkoG9Bxp9x0lkF1g&oe=69DC5A38",
        "width": 1242,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          14218,
          28436,
          42654
        ],
        "height": 1000,
        "scans_profile": "e35",
        "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/661360873_18583030168052095_3048125277147945686_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=109&ig_cache_key=Mzg3MDc3Mjk0NDA5NjIyNDMzMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyNDJ4MTY1Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=Z02V73IW3OkQ7kNvwH-wyK7&_nc_oc=AdqHTispgbHOu5FLXqj-2E6MIbU3AgOwqxP_M4tQhI4E5X8EkrbRHdgOVaA2Biuvnuc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af2jfzDtFSRLMLui33ymcChDBxXllEtWJ9gRnkw0Y2v4qA&oe=69DC5A38",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "clips_metadata": {},
    "video_dash_manifest": "",
    "like_and_view_counts_disabled": true,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870755518164018910",
    "id": "3870755518164018910_58402453310",
    "code": "DW3r6K4jKbe",
    "taken_at": "2026-04-08T12:09:53Z",
    "taken_at_ts": 1775650193,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/663131833_4308995229361628_1732703064334565814_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc1NTUxODE2NDAxODkxMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=L1-2WNLhcJYQ7kNvwGxUruo&_nc_oc=Adqtu3bqXsxNNrPZd1dI5wy72gILzxHG6aVZFFWJaAlRPCCBV3Mxu6l51sbcZrA4630&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af1mSk2a2ic6gdXbS5jKvJ1w64aJdJazM-ht5q6OUOGrvg&oe=69DC4FB6",
    "location": null,
    "user": {
      "pk": "58402453310",
      "id": "58402453310",
      "username": "tejas_cholke_7171",
      "full_name": "CHOLKE PHOTOGRAPHY",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/657707038_17991595787949311_3066213950240011378_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gGkaY55LKWayuYPyZFC_mXfodSoR-p6TWy4nq1sc9SBXJrhyjVwBhvVhl_pHf2ZV1Q&_nc_ohc=AErV7hKuF_MQ7kNvwG_IhCp&_nc_gid=VN7KX9fwn22l0qab2OSDag&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GB7QMyf-FOLTQus-AHI0Z51XYY0qbmNDAQAB1501500j-ccb7-5&oh=00_Af2g0iUucO7qoj2PoS9qonN-dhfaH99i_76Qs7sp88t8fA&oe=69DC3395&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 22,
    "comments_disabled": false,
    "like_count": 3,
    "play_count": 11890,
    "has_liked": false,
    "caption_text": "#वर्दी 🚨💯💫\n\n#instagram #love #instagood #maharashtra",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNNHMI9qnBZiKoO9pVIowNz7QklI4_mgCVar1AeNgQO4FbgH1cr3bdMKZYubO42BqSj21mXf-UqB9IILUH-XKOtNWSO8tlH1aq8HL4.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_ohc=Ga61H9trFs4Q7kNvwEdzx8-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5OTI3MDI2ODI5NDkzMTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=bc268a0bc38fe92c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80QzQxNjBGQjFERjA5NUMzMkRDQjc1RTNDNEUwMjRBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENEIwNjNEQkYwRTJDMURERjMyRUY0NDI5NTkxN0EzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACb-mru_kZH2PxUCKAJDMywXQDjMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1XlpEfhrt_nGqOgDw6Jar6oVfl6M_-dKDYbrUKPTIA1g&oe=69D8626A",
    "view_count": 0,
    "video_duration": 24.799999237060547,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          5600,
          11200,
          16800
        ],
        "height": 1136,
        "scans_profile": "e15",
        "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/663131833_4308995229361628_1732703064334565814_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc1NTUxODE2NDAxODkxMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=L1-2WNLhcJYQ7kNvwGxUruo&_nc_oc=Adqtu3bqXsxNNrPZd1dI5wy72gILzxHG6aVZFFWJaAlRPCCBV3Mxu6l51sbcZrA4630&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&oh=00_Af1mSk2a2ic6gdXbS5jKvJ1w64aJdJazM-ht5q6OUOGrvg&oe=69DC4FB6",
        "width": 640,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 2478468,
        "height": 1280,
        "id": "1655341825618319v",
        "type": 101,
        "url": "https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNNHMI9qnBZiKoO9pVIowNz7QklI4_mgCVar1AeNgQO4FbgH1cr3bdMKZYubO42BqSj21mXf-UqB9IILUH-XKOtNWSO8tlH1aq8HL4.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_ohc=Ga61H9trFs4Q7kNvwEdzx8-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5OTI3MDI2ODI5NDkzMTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=bc268a0bc38fe92c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80QzQxNjBGQjFERjA5NUMzMkRDQjc1RTNDNEUwMjRBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENEIwNjNEQkYwRTJDMURERjMyRUY0NDI5NTkxN0EzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACb-mru_kZH2PxUCKAJDMywXQDjMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1XlpEfhrt_nGqOgDw6Jar6oVfl6M_-dKDYbrUKPTIA1g&oe=69D8626A",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2478468,
        "height": 1280,
        "id": "1655341825618319v",
        "type": 102,
        "url": "https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNNHMI9qnBZiKoO9pVIowNz7QklI4_mgCVar1AeNgQO4FbgH1cr3bdMKZYubO42BqSj21mXf-UqB9IILUH-XKOtNWSO8tlH1aq8HL4.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_ohc=Ga61H9trFs4Q7kNvwEdzx8-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5OTI3MDI2ODI5NDkzMTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=bc268a0bc38fe92c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80QzQxNjBGQjFERjA5NUMzMkRDQjc1RTNDNEUwMjRBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENEIwNjNEQkYwRTJDMURERjMyRUY0NDI5NTkxN0EzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACb-mru_kZH2PxUCKAJDMywXQDjMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1XlpEfhrt_nGqOgDw6Jar6oVfl6M_-dKDYbrUKPTIA1g&oe=69D8626A",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2478468,
        "height": 1280,
        "id": "1655341825618319v",
        "type": 103,
        "url": "https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNNHMI9qnBZiKoO9pVIowNz7QklI4_mgCVar1AeNgQO4FbgH1cr3bdMKZYubO42BqSj21mXf-UqB9IILUH-XKOtNWSO8tlH1aq8HL4.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_ohc=Ga61H9trFs4Q7kNvwEdzx8-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5OTI3MDI2ODI5NDkzMTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=bc268a0bc38fe92c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80QzQxNjBGQjFERjA5NUMzMkRDQjc1RTNDNEUwMjRBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENEIwNjNEQkYwRTJDMURERjMyRUY0NDI5NTkxN0EzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACb-mru_kZH2PxUCKAJDMywXQDjMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1XlpEfhrt_nGqOgDw6Jar6oVfl6M_-dKDYbrUKPTIA1g&oe=69D8626A",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "clips_metadata": {
      "clips_creation_entry_point": "clips",
      "featured_label": null,
      "is_public_chat_welcome_video": false,
      "professional_clips_upsell_type": 0,
      "show_tips": null,
      "achievements_info": {
        "num_earned_achievements": null,
        "show_achievements": false
      },
      "additional_audio_info": {
        "additional_audio_username": null,
        "audio_reattribution_info": {
          "should_allow_restore": false
        }
      },
      "asset_recommendation_info": null,
      "audio_ranking_info": {
        "best_audio_cluster_id": "2881821365322715"
      },
      "audio_type": "original_sounds",
      "basel_template_info_for_ig_app": {
        "is_basel_template": null,
        "should_show_reuse_setting_for_owner": false,
        "use_template_deeplink": null
      },
      "branded_content_tag_info": {
        "can_add_tag": false
      },
      "breaking_content_info": null,
      "breaking_creator_info": null,
      "challenge_info": null,
      "content_appreciation_info": null,
      "contextual_highlight_info": null,
      "cutout_sticker_info": [],
      "disable_use_in_clips_client_cache": false,
      "external_media_info": null,
      "is_fan_club_promo_video": false,
      "is_shared_to_fb": false,
      "mashup_info": {
        "can_toggle_mashups_allowed": false,
        "formatted_mashups_count": null,
        "has_been_mashed_up": false,
        "has_nonmimicable_additional_audio": false,
        "is_creator_requesting_mashup": false,
        "is_light_weight_check": true,
        "is_light_weight_reuse_allowed_check": false,
        "is_pivot_page_available": false,
        "is_reuse_allowed": true,
        "mashup_type": null,
        "mashups_allowed": true,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18386969215094474",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 25846303675044337,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT24.797461S\" FBManifestTimestamp=\"1775664063\" FBManifestIdentifier=\"Fv7us50NKRamgtuBl43EByIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT24.797461S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2120084845453459a\" bandwidth=\"67034\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"67034\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m78/AQOlPdjzDAfpeyctrj9xSslDaSpNwB0tkxVOGjh0wcwcIe9R0fkx3JIa8oncY0IiShHeIkVYocFd3BBFZD5rBGCrnMB_wyvLiOZxE68.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=nhF79ylIP2kQ7kNvwGM9Nga&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTkyNzAyNjgyOTQ5MzExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI0LCJiaXRyYXRlIjo2NzM2MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1Re9u4NgvYZOYCphRGmnj1AHh1n9-FDPK93I7OwjMiMg&amp;oe=69D86CFA</BaseURL><SegmentBase indexRange=\"824-1011\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 24800,
        "formatted_clips_media_count": null,
        "hide_remixing": false,
        "is_audio_automatically_attributed": false,
        "is_eligible_for_audio_effects": true,
        "is_eligible_for_vinyl_sticker": true,
        "is_explicit": false,
        "is_original_audio_download_eligible": false,
        "is_reuse_disabled": false,
        "is_xpost_from_fb": false,
        "music_canonical_id": null,
        "oa_owner_is_music_artist": false,
        "original_audio_subtype": "default",
        "original_audio_title": "Original audio",
        "original_media_id": 3870755518164018910,
        "progressive_download_url": "https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m69/AQNkZjELsuoJaW3vx9HM1RoqKK1k-WPEuSyqJwzzLiae8Nb1tJwKFSEREqglpGH3L1_ZyUXNanE4IQPuKRA6hkjN.mp4?strext=1&_nc_cat=104&_nc_sid=8bf8fe&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_ohc=3Ozr_ha5Bc0Q7kNvwEcDVPy&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5OTI3MDI2ODI5NDkzMTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=VN7KX9fwn22l0qab2OSDag&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0WslMyWTAvToHdPdOWG2_m1K6I8IyNCy6BDObghoGqGQ&oe=69DC539E",
        "should_mute_audio": false,
        "time_created": 1775650194,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "58402453310",
          "pk": 58402453310,
          "pk_id": "58402453310",
          "id": "58402453310",
          "username": "tejas_cholke_7171",
          "full_name": "CHOLKE PHOTOGRAPHY",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3864329393631402618_58402453310",
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/657707038_17991595787949311_3066213950240011378_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gGkaY55LKWayuYPyZFC_mXfodSoR-p6TWy4nq1sc9SBXJrhyjVwBhvVhl_pHf2ZV1Q&_nc_ohc=AErV7hKuF_MQ7kNvwG_IhCp&_nc_gid=VN7KX9fwn22l0qab2OSDag&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GB7QMyf-FOLTQus-AHI0Z51XYY0qbmNDAQAB1501500j-ccb7-5&oh=00_Af2g0iUucO7qoj2PoS9qonN-dhfaH99i_76Qs7sp88t8fA&oe=69DC3395&_nc_sid=472314"
        },
        "audio_filter_infos": null,
        "audio_parts": [],
        "audio_parts_by_filter": [],
        "consumption_info": {
          "display_media_id": null,
          "is_bookmarked": false,
          "is_trending_in_clips": false,
          "should_mute_audio_reason": "",
          "should_mute_audio_reason_type": null,
          "inline_audio_label": null,
          "display_labels": null,
          "user_notes": null
        },
        "xpost_fb_creator_info": null,
        "fb_downstream_use_xpost_metadata": {
          "downstream_use_xpost_deny_reason": "NONE"
        }
      },
      "originality_info": null,
      "reels_on_the_rise_info": null,
      "reusable_text_attribute_string": null,
      "reusable_text_info": null,
      "shopping_info": null,
      "show_achievements": false,
      "template_info": null,
      "may_have_template_info": null,
      "viewer_interaction_settings": null
    },
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT24.799999S\" FBManifestTimestamp=\"1775664063\" FBManifestIdentifier=\"Fv7us50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtoqErMP+rLoD4Nv5j4aIuQSs4Mm4l/m+BJ7V+//KzNsEoqvG5vnciAWIztyhz5DhBbqvq9vouoAHstav+6/ljwf0q7zopZnOB8rU/IWW6sMI/J2A4P/7gg8iGCJkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGVfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT24.799999S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:83.6\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1971335323806685v\" bandwidth=\"551016\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1708150\" FBPlaybackResolutionMos=\"0:100,360:77.9,480:74.9,720:70.4,1080:66.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.6,480:94.4,720:92.5,1080:89.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMqrnbSyPHYtC-h5S7C3PtIkBDUmhmAsrqexK47_lNmIxzCad1zRuyYmRE_6NaZ5oXgrdqiab29mLkov_rDDIzSAKHqtNrhYMomg4s.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=I3mADj_1NP8Q7kNvwFmBb5D&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6NTUxMDE2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af21nN031qgNpfZZb1i76MyrbcLIagbSe97yQ6wioUWdkw&amp;oe=69DC4388</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1727\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-69538\" FBFirstSegmentRange=\"918-104064\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"104065-322794\" FBPrefetchSegmentRange=\"918-104064\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1426563965438673v\" bandwidth=\"953270\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2955140\" FBPlaybackResolutionMos=\"0:100,360:83.1,480:79.3,720:74.8,1080:70.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.2,480:96.6,720:95.6,1080:93\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m367/AQM93rL5wbeQBC1qkOD-WA00VUv6sRe2wJ1jIJmwKS0j2vgYS-fuMfaoxXmZc8A5iLo1ggzKDbjFJGJvQrsoup55Tq20i5esdd9Xnc4.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=0YtjgI7hRbMQ7kNvwGQWaw8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6OTUzMjcwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1xFZfInjJdfJeXh-6X-qZ96nCjsoV4N8pfOwdqGCGH2Q&amp;oe=69DC6059</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1697\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-103999\" FBFirstSegmentRange=\"918-160851\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"160852-510376\" FBPrefetchSegmentRange=\"918-160851\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1620965655810948v\" bandwidth=\"1281906\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3973911\" FBPlaybackResolutionMos=\"0:100,360:85,480:81.5,720:76.5,1080:72\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:97.3,720:96.5,1080:94.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN8WwZWX9Mbh3M8psGUH5DxDW_w8TBlK_z9uH5_BzQ98sy0h2pvssVQ3op_M9opQeD4XBsFAP-tX1Krgcxq-fF2J_6-onz1kh9FDH0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=cC4z5lPzM3MQ7kNvwEkpp-l&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6MTI4MTkwNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af31dQ-VKltbs6RlF13AaiV4mbE_MKLcotWDDkvqG7mcRg&amp;oe=69DC562B</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1727\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-128456\" FBFirstSegmentRange=\"918-204788\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"204789-657639\" FBPrefetchSegmentRange=\"918-204788\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1327326759449935v\" bandwidth=\"1617272\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"5013545\" FBPlaybackResolutionMos=\"0:100,360:86.5,480:83.1,720:77.8,1080:73.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.08,480:97.9,720:97.2,1080:95.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOIp-c1aJheMeCDF8QHUhjfyZDWU63E2-ay01iDzrnV1bn2OPUGIjRtFbTcyg6s8tq1uxCTdsphk_oBsM4fGvcbHafMjnp41IU5npE.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=CGRvQWHzdH4Q7kNvwHIISm8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6MTYxNzI3MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0i4AFNQgv6mApGokX80e5k6ogPlXodftWXpWBUBh8_3A&amp;oe=69DC4B37</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1704\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-153502\" FBFirstSegmentRange=\"918-254575\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"254576-813761\" FBPrefetchSegmentRange=\"918-254575\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1264321259190294v\" bandwidth=\"2177412\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"6749978\" FBPlaybackResolutionMos=\"0:100,360:88,480:84.8,720:79.9,1080:74.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.4,480:98.43,720:98.06,1080:96.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0406pGxUm5nO9GZzxZ3SXWK5VduWS6i7xwTfE246Mv7SzZbzBX7f5qfELl_bTaVGdKuP1vjdzlNDooVR9l7TYBQyBIsI5auBLPQw.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=ZvB_zqU8c44Q7kNvwE5okiA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6MjE3NzQxMiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af07jlW9geO3okHXkveQcYVcObz4YBuz0Q1SkAl8vLhlEA&amp;oe=69DC4144</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1699\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-194629\" FBFirstSegmentRange=\"918-341837\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"341838-1066640\" FBPrefetchSegmentRange=\"918-341837\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1251382493394672v\" bandwidth=\"2732803\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"8471691\" FBPlaybackResolutionMos=\"0:100,360:89.1,480:86,720:81.3,1080:75.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.51,480:98.64,720:98.57,1080:97\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m367/AQP07PZ3SgnpTBelSk4TM378yCrbJ0qIa0cKnnaA6d9CS0DDF2r4nApisBoLArHfz-3OMZC0d85GJMHXBFLYh5cL30-CY2xolEu5vvQ.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=LdtTxfnIeVEQ7kNvwFmkQ6l&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6MjczMjgwMywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2yx7Y8C37pz2O3Msr3wP6BmOpqv5bhhO8ZzsDU8T_VtA&amp;oe=69DC6481</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1708\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-234687\" FBFirstSegmentRange=\"918-439068\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"439069-1346480\" FBPrefetchSegmentRange=\"918-439068\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"972741175247109v\" bandwidth=\"3641447\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"11288488\" FBPlaybackResolutionMos=\"0:100,360:90.4,480:87.5,720:83.2,1080:77.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.75,480:98.95,720:98.99,1080:97.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxX3ZaTc_ZOKXAgMOYphgxo_ePlXaq1Lg83Oeuyh6q5MxhAYXfNqu7scKbM3gTjeJ8ryRs4g0I4nRC9Lui4Xpq_LuPtgca8BmlzHs.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=WwRPprrL6WsQ7kNvwEzqFWG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6MzY0MTQ0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1rvqv2jZOi_jKyaK7WemukWtvwz9mpOQ9QCVEOEDj5pQ&amp;oe=69DC65D4</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-333142\" FBFirstSegmentRange=\"918-676951\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"676952-2029971\" FBPrefetchSegmentRange=\"918-676951\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4228652967397246v\" bandwidth=\"4957913\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"15369532\" FBPlaybackResolutionMos=\"0:100,360:92,480:89.5,720:85.9,1080:83.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.86,480:99.136,720:99.447,1080:99.545\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNYrjfdcOuez9jnuvrb4hQmaHJGFPZl2nfwjtQfA32c8UV4ACBswgm6_L4v_c4GVvQzyluWKsvTJNtv-3GO48e0N_Mr0oZLIS3EBpY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=NZVDgQOM9WAQ7kNvwHsZofe&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk5MjcwMjY4Mjk0OTMxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNCwiYml0cmF0ZSI6NDk1NzkxMywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3y7zuPYfQxPVDwSlEHiZYsVZewijORFnG9FulsDTktHA&amp;oe=69DC5DD4</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-1731\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-575487\" FBFirstSegmentRange=\"918-1135723\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1135724-3346135\" FBPrefetchSegmentRange=\"918-1135723\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2005051790194073a\" bandwidth=\"41875\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"41875\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"130740\" FBPaqMos=\"87.16\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m367/AQMUR_JyQAhAGs2ljroEUCjOFxWfCYrNp62Qko26IfC3V1iakcywpnmCMHwImUGcwJSXU_5iW9OWHyHoZWvNCJ4cUzxYXT5WnRIwDi8.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=1XhyT1QQAOsQ7kNvwExF0cI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTkyNzAyNjgyOTQ5MzExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI0LCJiaXRyYXRlIjo0MjE3OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af18EjKzs5BOHGPgkiqMrsVHIeCWGQSW4w43YbrV_hxwtQ&amp;oe=69DC3731</BaseURL><SegmentBase indexRange=\"839-942\" timescale=\"44100\" FBMinimumPrefetchRange=\"943-1932\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"943-13957\" FBFirstSegmentRange=\"943-26740\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"26741-52195\" FBPrefetchSegmentRange=\"943-26740\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-838\"/></SegmentBase></Representation><Representation id=\"2400958396994853a\" bandwidth=\"75085\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"75085\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"233682\" FBPaqMos=\"90.90\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m367/AQMn37o6PJng_ZuMv88n_r25RjXZLJSH_AV9ePgtHGMKMn2U5Z-UA44FyAc9C2mJqR2nLCn-NSiPhSutOvbDs-dxsTfTNK-6CCVcpbE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=mkkvid87R4cQ7kNvwFU74So&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTkyNzAyNjgyOTQ5MzExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI0LCJiaXRyYXRlIjo3NTM4OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1OMSXrPU-FMlDidpz7zPRvVtKyWO_haIlyRGVobnXlCg&amp;oe=69DC45CE</BaseURL><SegmentBase indexRange=\"840-943\" timescale=\"44100\" FBMinimumPrefetchRange=\"944-2373\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"944-24420\" FBFirstSegmentRange=\"944-47211\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"47212-92790\" FBPrefetchSegmentRange=\"944-47211\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-839\"/></SegmentBase></Representation><Representation id=\"2142283223239418a\" bandwidth=\"111610\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"111610\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"346893\" FBPaqMos=\"93.78\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOMEXTk2K5BdxmL3m1xcxwGiSYzFPyWkkyKcYABS733azLPjHGckr_uCbEVPSnF7JIGaESOIFpTQfuxy2urMKejOx60wNlMS_1M6q0.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=IroJ37xSafgQ7kNvwFxI_gt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTkyNzAyNjgyOTQ5MzExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI0LCJiaXRyYXRlIjoxMTE5MTIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VN7KX9fwn22l0qab2OSDag&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Nn0Xtke1GwOSJp5l6VLX9p_D0xS6-Oj8Xy9KDYA5rJA&amp;oe=69DC49BE</BaseURL><SegmentBase indexRange=\"835-938\" timescale=\"44100\" FBMinimumPrefetchRange=\"939-2077\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"939-35757\" FBFirstSegmentRange=\"939-69504\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"69505-138010\" FBPrefetchSegmentRange=\"939-69504\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-834\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": true,
    "coauthor_producers": [
      {
        "strong_id__": "41337844073",
        "pk": 41337844073,
        "pk_id": "41337844073",
        "id": "41337844073",
        "username": "_mk_7171",
        "full_name": "MAYUR KARDILE",
        "is_private": true,
        "is_verified": false,
        "profile_pic_id": "3849504971998590657_41337844073",
        "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-19/649236980_18076136090380074_3174331847673223496_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGkaY55LKWayuYPyZFC_mXfodSoR-p6TWy4nq1sc9SBXJrhyjVwBhvVhl_pHf2ZV1Q&_nc_ohc=1pEoihKtWqwQ7kNvwHR4gRy&_nc_gid=VN7KX9fwn22l0qab2OSDag&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GPSRsiYqJ5RmJjhAAEiZxUP-fQ0sbmNDAQAB1501500j-ccb7-5&oh=00_Af16uqpTM2YsQuJaQ6bfzGwZs5jKlsprCZBoBjWZ35P1KA&oe=69DC53E2&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": true,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      },
      {
        "strong_id__": "50804892534",
        "pk": 50804892534,
        "pk_id": "50804892534",
        "id": "50804892534",
        "username": "manisha_cholke_7171",
        "full_name": "MANISHA CHOLKE",
        "is_private": true,
        "is_verified": false,
        "profile_pic_id": "3770459970668604915_50804892534",
        "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/583337877_18044744771692535_2691987486452387469_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDY1LmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gGkaY55LKWayuYPyZFC_mXfodSoR-p6TWy4nq1sc9SBXJrhyjVwBhvVhl_pHf2ZV1Q&_nc_ohc=ujRSEFwtgK8Q7kNvwFxk9Ix&_nc_gid=VN7KX9fwn22l0qab2OSDag&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJUHxSL35y2KmRtAAI2Oyi1b3FslbmNDAQAB1501500j-ccb7-5&oh=00_Af3-MZGBoba4OPEHsEfRLE1Sl6TAcGWsAja_VXVtbe3Qxg&oe=69DC5406&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": true,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      },
      {
        "strong_id__": "80421832756",
        "pk": 80421832756,
        "pk_id": "80421832756",
        "id": "80421832756",
        "username": "cholke__photoghraphy_7171",
        "full_name": "CHOLKE PHOTOGRAPHY",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "3838952163842484702_80421832756",
        "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/641732917_17851405116680757_7888836412287899639_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2gGkaY55LKWayuYPyZFC_mXfodSoR-p6TWy4nq1sc9SBXJrhyjVwBhvVhl_pHf2ZV1Q&_nc_ohc=kCaJp8xD2QAQ7kNvwHTruJz&_nc_gid=VN7KX9fwn22l0qab2OSDag&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDURQCY1qrgkwms-APdXlo3rxnptbmNDAQAB1501500j-ccb7-5&oh=00_Af2amuCEhn8_bPOdR1dqRORy64nShD0IcNBCG5pG7Y88gA&oe=69DC4FBC&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      }
    ],
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
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2Xja0wqByXxfof7pm193htadX6Mp_MtsYZXFuPSk4aMQ&oe=69DC5703",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHJ1t3hemKBDOWUjMRXWMdOG_vDDINLh4DYx_wgowdkR19PZjqmIAFyFypYj2d9Us8&_nc_ohc=8UGwMTx74pgQ7kNvwHA5dwc&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af35gy1s6yv3f0tEdnZYJ51wbE3iRYgUxbdna3tts5gJwA&oe=69DC3771&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 387,
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
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2Xja0wqByXxfof7pm193htadX6Mp_MtsYZXFuPSk4aMQ&oe=69DC5703",
          "width": 1079,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            7924,
            15848,
            23772
          ],
          "height": 765,
          "scans_profile": "e35",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af0LEmpXanPj97E5aiCcnPBF1FO8kxYTYmY-9nMER6s1sA&oe=69DC5703",
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
      "pk": "3870743885521623606",
      "id": "3870743885521623606_71436013584",
      "code": "DW3pQ5JCBo2",
      "taken_at": "2026-04-08T11:46:26Z",
      "taken_at_ts": 1775648786,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/661212477_944039288523737_2741936145184857132_n.jpg?stp=dst-jpegr_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDc0Mzg4NTUyMTYyMzYwNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2Lmhkci5DMyJ9&_nc_ohc=0-MgWorE5cAQ7kNvwFtQH6y&_nc_oc=AdpIOUm-ge-AneVYYS0pd6XCVhkul4GdtuVLlyaHJJWvtngfX-23JIdt0CL-tJGHqEs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af25EvEI2-nwee2mE8QO6gGa4ipt4U2KO1wd7_o9sd53YQ&oe=69DC69F6",
      "location": null,
      "user": {
        "pk": "71436013584",
        "id": "71436013584",
        "username": "jesuslovesyou2620",
        "full_name": "Grandma",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/471928243_574253788804684_552793214650570792_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MjIuYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gHJ1t3hemKBDOWUjMRXWMdOG_vDDINLh4DYx_wgowdkR19PZjqmIAFyFypYj2d9Us8&_nc_ohc=KBJE8MKtiToQ7kNvwHBdnhC&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GLMNIRxMthfhRwoCAChYfvl-6qsHbkULAAAB1501500j-ccb7-5&oh=00_Af09pI3HVob2C3eyb9vk1Rmfg7VOhoi2OHRlqGmonLi5ww&oe=69DC5B88&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 21,
      "comments_disabled": false,
      "like_count": 306,
      "play_count": 1879,
      "has_liked": false,
      "caption_text": "#jesuslovesyou #grandma #Jesus #Christian #love",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPsUIBn_X4pRueNy3vDsIDTjRMaVcwakhdCD-TR4tQ_QTcLTFqlNOwQam8NEiSJIDmTQlfky8LyeCjgPg0scQA5jvzpnZ1EKqQP13E.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ivi3sA7WuAEQ7kNvwE4j5W-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5MDg0NDA3NjIzODE1ODUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=9252eefb4811a509&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9ENDRGNTE3NDJCMUJDQTY0NUVEODBCMUY1OUJCNjQ5Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzEyNDAwM0Y1RTMzNjMzODEzMjVENThEREY2NUFENDg4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACai1PuhuejPPxUCKAJDMywXQFPzMzMzMzMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0jDnbbSxQkFG_vz-y44x9xHAXDEpG5TfSmmwieOlhy9Q&oe=69D84C7F",
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
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/661212477_944039288523737_2741936145184857132_n.jpg?stp=dst-jpegr_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDc0Mzg4NTUyMTYyMzYwNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2Lmhkci5DMyJ9&_nc_ohc=0-MgWorE5cAQ7kNvwFtQH6y&_nc_oc=AdpIOUm-ge-AneVYYS0pd6XCVhkul4GdtuVLlyaHJJWvtngfX-23JIdt0CL-tJGHqEs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af25EvEI2-nwee2mE8QO6gGa4ipt4U2KO1wd7_o9sd53YQ&oe=69DC69F6",
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
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPsUIBn_X4pRueNy3vDsIDTjRMaVcwakhdCD-TR4tQ_QTcLTFqlNOwQam8NEiSJIDmTQlfky8LyeCjgPg0scQA5jvzpnZ1EKqQP13E.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ivi3sA7WuAEQ7kNvwE4j5W-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5MDg0NDA3NjIzODE1ODUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=9252eefb4811a509&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9ENDRGNTE3NDJCMUJDQTY0NUVEODBCMUY1OUJCNjQ5Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzEyNDAwM0Y1RTMzNjMzODEzMjVENThEREY2NUFENDg4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACai1PuhuejPPxUCKAJDMywXQFPzMzMzMzMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0jDnbbSxQkFG_vz-y44x9xHAXDEpG5TfSmmwieOlhy9Q&oe=69D84C7F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 798880,
          "height": 1280,
          "id": "1577230313379737v",
          "type": 102,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPsUIBn_X4pRueNy3vDsIDTjRMaVcwakhdCD-TR4tQ_QTcLTFqlNOwQam8NEiSJIDmTQlfky8LyeCjgPg0scQA5jvzpnZ1EKqQP13E.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ivi3sA7WuAEQ7kNvwE4j5W-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5MDg0NDA3NjIzODE1ODUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=9252eefb4811a509&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9ENDRGNTE3NDJCMUJDQTY0NUVEODBCMUY1OUJCNjQ5Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzEyNDAwM0Y1RTMzNjMzODEzMjVENThEREY2NUFENDg4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACai1PuhuejPPxUCKAJDMywXQFPzMzMzMzMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0jDnbbSxQkFG_vz-y44x9xHAXDEpG5TfSmmwieOlhy9Q&oe=69D84C7F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 798880,
          "height": 1280,
          "id": "1577230313379737v",
          "type": 103,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPsUIBn_X4pRueNy3vDsIDTjRMaVcwakhdCD-TR4tQ_QTcLTFqlNOwQam8NEiSJIDmTQlfky8LyeCjgPg0scQA5jvzpnZ1EKqQP13E.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ivi3sA7WuAEQ7kNvwE4j5W-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5MDg0NDA3NjIzODE1ODUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=9252eefb4811a509&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9ENDRGNTE3NDJCMUJDQTY0NUVEODBCMUY1OUJCNjQ5Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzEyNDAwM0Y1RTMzNjMzODEzMjVENThEREY2NUFENDg4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACai1PuhuejPPxUCKAJDMywXQFPzMzMzMzMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0jDnbbSxQkFG_vz-y44x9xHAXDEpG5TfSmmwieOlhy9Q&oe=69D84C7F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "clips_metadata": {
        "clips_creation_entry_point": "feed",
        "featured_label": null,
        "is_public_chat_welcome_video": false,
        "professional_clips_upsell_type": 0,
        "show_tips": null,
        "achievements_info": {
          "num_earned_achievements": null,
          "show_achievements": false
        },
        "additional_audio_info": {
          "additional_audio_username": null,
          "audio_reattribution_info": {
            "should_allow_restore": false
          }
        },
        "asset_recommendation_info": null,
        "audio_ranking_info": {
          "best_audio_cluster_id": "2471278869983385"
        },
        "audio_type": "original_sounds",
        "basel_template_info_for_ig_app": {
          "is_basel_template": null,
          "should_show_reuse_setting_for_owner": false,
          "use_template_deeplink": null
        },
        "branded_content_tag_info": {
          "can_add_tag": false
        },
        "breaking_content_info": null,
        "breaking_creator_info": null,
        "challenge_info": null,
        "content_appreciation_info": null,
        "contextual_highlight_info": null,
        "cutout_sticker_info": [],
        "disable_use_in_clips_client_cache": false,
        "external_media_info": null,
        "is_fan_club_promo_video": false,
        "is_shared_to_fb": false,
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": false,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": false,
          "is_pivot_page_available": false,
          "is_reuse_allowed": true,
          "mashup_type": null,
          "mashups_allowed": true,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18461374489103143",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26383290328031831,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": false,
          "can_remix_be_shared_to_fb_expansion": false,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT79.830208S\" FBManifestTimestamp=\"1775664068\" FBManifestIdentifier=\"Fojvs50NKRbY8frWttazAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT79.830208S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"958059923856492a\" bandwidth=\"73241\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"73241\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m78/AQOj1D3OeJMYx3LTIfD48OTOa0M2-txaDOwDtpAuqolaiWk9FoX9_O5rjJQJAWEjTZNGxpjrP2VRQWwCveU_Ku8kkKExdYsjAULMMFM.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=EesUq1u8U3oQ7kNvwFdD9NA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTA4NDQwNzYyMzgxNTg1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc5LCJiaXRyYXRlIjo3MzM3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2hV3sYDhhUIVIlyx6Ztd05bL9a4AO1oS2nHRT-dcTDrA&amp;oe=69D8724A</BaseURL><SegmentBase indexRange=\"824-1335\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 79000,
          "formatted_clips_media_count": null,
          "hide_remixing": false,
          "is_audio_automatically_attributed": false,
          "is_eligible_for_audio_effects": true,
          "is_eligible_for_vinyl_sticker": true,
          "is_explicit": false,
          "is_original_audio_download_eligible": true,
          "is_reuse_disabled": false,
          "is_xpost_from_fb": false,
          "music_canonical_id": null,
          "oa_owner_is_music_artist": false,
          "original_audio_subtype": "default",
          "original_audio_title": "Original audio",
          "original_media_id": 3870743885521623606,
          "progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQOJVgCNdonSEh7t0rb3fucYs3bM-eCzb3GOKd-UyO2QyB3lVxQx-oRpyhiI_zbVm6-njRqv7fauBAPlRhsXGaLp.mp4?strext=1&_nc_cat=108&_nc_sid=8bf8fe&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=weDXY-45SsEQ7kNvwGScck0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5MDg0NDA3NjIzODE1ODUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0rCp_csa9o9Ug7w-hIAjzbSBt-GGYTRw7gkWvtBKOSyg&oe=69DC36A2",
          "should_mute_audio": false,
          "time_created": 1775648688,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "71436013584",
            "pk": 71436013584,
            "pk_id": "71436013584",
            "id": "71436013584",
            "username": "jesuslovesyou2620",
            "full_name": "Grandma",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3534340130690622427_71436013584",
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/471928243_574253788804684_552793214650570792_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MjIuYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gHJ1t3hemKBDOWUjMRXWMdOG_vDDINLh4DYx_wgowdkR19PZjqmIAFyFypYj2d9Us8&_nc_ohc=KBJE8MKtiToQ7kNvwHBdnhC&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GLMNIRxMthfhRwoCAChYfvl-6qsHbkULAAAB1501500j-ccb7-5&oh=00_Af09pI3HVob2C3eyb9vk1Rmfg7VOhoi2OHRlqGmonLi5ww&oe=69DC5B88&_nc_sid=472314"
          },
          "audio_filter_infos": null,
          "audio_parts": [],
          "audio_parts_by_filter": [],
          "consumption_info": {
            "display_media_id": null,
            "is_bookmarked": false,
            "is_trending_in_clips": false,
            "should_mute_audio_reason": "",
            "should_mute_audio_reason_type": null,
            "inline_audio_label": null,
            "display_labels": null,
            "user_notes": null
          },
          "xpost_fb_creator_info": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "originality_info": null,
        "reels_on_the_rise_info": null,
        "reusable_text_attribute_string": null,
        "reusable_text_info": null,
        "shopping_info": null,
        "show_achievements": false,
        "template_info": null,
        "may_have_template_info": null,
        "viewer_interaction_settings": null
      },
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT79.828751S\" FBManifestTimestamp=\"1775664068\" FBManifestIdentifier=\"Fojvs50NGBFpZ19kYXNoX2Jhc2ljX3ZwORmGtpyHsIeGvQPy5oXX5vfCBPDgsKj/kMME5LLIwJDX1ATu1cCD9IiNBY6w2/u+1JUFmozakPi5oAWWg+HCu9XWBSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT79.828751S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:76.3\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"1273093627623865v\" bandwidth=\"136440\" codecs=\"vp09.00.21.08.01.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_360p\" FBContentLength=\"1360990\" FBPlaybackResolutionMos=\"0:100,360:74.4,480:68.2,720:58.8,1080:49.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.9,480:83,720:74.1,1080:64.1\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNVGtsB5OhDldZ--K7oUIZe6ucMLJThTC5QJw_79A0U3EvZJQYnAGpErNu0EZNojMlTi1SUw0ai2CTIpuBQHWvtS9f9QCdQ3CNRc5rKeWms8A.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=grukQYbq9KcQ7kNvwFzyNF-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMzYwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkwODQ0MDc2MjM4MTU4NSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3OSwiYml0cmF0ZSI6MTM2NDQwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af37-_e6DoLQqSLy9CEuIZCe-NIWborxuGJHg4H28lqfMw&amp;oe=69DC4E0B</BaseURL><SegmentBase indexRange=\"818-1041\" timescale=\"15360\" FBMinimumPrefetchRange=\"1042-21392\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1042-48652\" FBFirstSegmentRange=\"1042-68262\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"68263-133350\" FBPrefetchSegmentRange=\"1042-68262\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1436115197760887v\" bandwidth=\"353709\" codecs=\"vp09.00.30.08.01.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_540p\" FBContentLength=\"3528251\" FBPlaybackResolutionMos=\"0:100,360:83,480:80.2,720:73.9,1080:67.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:93.2,720:88.4,1080:82\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP7O-Lh_HEp_tJ4FYXSZUPtEKST7dgD6_eTLp8L_-7F0-IVbXkPZ91adtdnNUw_OiedXhLzyxTsA5iJXkIgELi7araYp02WjsiuN4CqoOBSWA.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=TN7nldnPe2EQ7kNvwH5y4iH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNTQwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkwODQ0MDc2MjM4MTU4NSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3OSwiYml0cmF0ZSI6MzUzNzA5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Br9c6LMrLUeZARvphvy-viiyUOM8BwupNRz1j179YUQ&amp;oe=69DC6978</BaseURL><SegmentBase indexRange=\"818-1041\" timescale=\"15360\" FBMinimumPrefetchRange=\"1042-45072\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1042-123443\" FBFirstSegmentRange=\"1042-177906\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"177907-347476\" FBPrefetchSegmentRange=\"1042-177906\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1597959161258187v\" bandwidth=\"651055\" codecs=\"vp09.00.31.08.01.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_720p\" FBContentLength=\"6494280\" FBPlaybackResolutionMos=\"0:100,360:90.6,480:88.1,720:84.1,1080:75.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.6,480:95.9,720:94.6,1080:89.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQO57rBm2l-shFKdq2frC96KNA8oHZQJW_4IJQV6KvrQriI1GAmFrs-ArijVTbi20x-QS-mzAsOlBjA0XxCUlX9xprWvHOx72m6cg9ioKIJXaQ.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=a6T_Q2QgwoIQ7kNvwFjY7G6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNzIwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkwODQ0MDc2MjM4MTU4NSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3OSwiYml0cmF0ZSI6NjUxMDU1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0z6Tb33EAjNe4cDZqtthV8b2ciU3fTgGIq2963645O2A&amp;oe=69DC5101</BaseURL><SegmentBase indexRange=\"818-1041\" timescale=\"15360\" FBMinimumPrefetchRange=\"1042-58693\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1042-220283\" FBFirstSegmentRange=\"1042-330997\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"330998-649311\" FBPrefetchSegmentRange=\"1042-330997\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1312114724113586v\" bandwidth=\"974112\" codecs=\"vp09.00.40.08.01.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_1080p\" FBContentLength=\"9716775\" FBPlaybackResolutionMos=\"0:100,360:92.7,480:91.5,720:88.3,1080:83.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.3,480:96.9,720:96,1080:94.6\" FBAbrPolicyTags=\"avoid_on_cellular\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPpDnKLVsaywqz6q_3qxUjYB-5TADdkhsYJFhjtgHXgMkCu2S2GZ7EteztS2fUxeP1zANQVV4fUTOT6Eg9RxeojW34RJTlnt7_bs6Y8HI7fZw.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=8Mi3i_TmU68Q7kNvwHCHQT3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMTA4MHAiLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjU2NzA2NzM0MzM1MjQyNywiY2xpZW50X25hbWUiOiJpZyIsInhwdl9hc3NldF9pZCI6MTc5MDg0NDA3NjIzODE1ODUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzksImJpdHJhdGUiOjk3NDExMiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3XxtxIGW7QDOL6nsx9rgGmAQ4scHhgw-a9nCyZVz290g&amp;oe=69DC47D8</BaseURL><SegmentBase indexRange=\"818-1041\" timescale=\"15360\" FBMinimumPrefetchRange=\"1042-72241\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1042-324871\" FBFirstSegmentRange=\"1042-500087\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"500088-982942\" FBPrefetchSegmentRange=\"1042-500087\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1478739003917069a\" bandwidth=\"31510\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"31510\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"315490\" FBPaqMos=\"83.08\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBGIhJnU58vfPgz2kZPT7xRqWtOwQn78YLJxRNGaLZLiYRBmLLTKr3XVkEVClkcvSnrUkkpK1trzp_JQ2bpFCjtEGjBP5zv9hQkTk.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=VRA2afEuD0MQ7kNvwHZe-eQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTA4NDQwNzYyMzgxNTg1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc5LCJiaXRyYXRlIjozMTYxNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af28vRnqOcMLiCjRAkhatlNg9HSqfcnG4ivTXxbgpxvtSQ&amp;oe=69DC3AAD</BaseURL><SegmentBase indexRange=\"837-1072\" timescale=\"44100\" FBMinimumPrefetchRange=\"1073-2100\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1073-11513\" FBFirstSegmentRange=\"1073-21128\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"21129-39771\" FBPrefetchSegmentRange=\"1073-21128\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1273526430865464a\" bandwidth=\"61768\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"61768\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"617428\" FBPaqMos=\"90.28\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMslXpvA3PA9s9SuHbJmGpblPG_l2E8z-xIYhE3BwMnBOTcbXA_KAa0idjHxam7w-DOmC8gZ0Pj5RcZLO87uI0WbcZmIdS9PJaSPeo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=aBNuctQTbd0Q7kNvwHhfLxm&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTA4NDQwNzYyMzgxNTg1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc5LCJiaXRyYXRlIjo2MTg3NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3lV-cblSEv11OBzHeaRIkJPL71Wzt3UBkXjRlyN7WTiw&amp;oe=69DC5EE6</BaseURL><SegmentBase indexRange=\"838-1073\" timescale=\"44100\" FBMinimumPrefetchRange=\"1074-2671\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1074-21212\" FBFirstSegmentRange=\"1074-39674\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"39675-76455\" FBPrefetchSegmentRange=\"1074-39674\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1455005932153863a\" bandwidth=\"81147\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"81147\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"810797\" FBPaqMos=\"93.45\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQO7_VoWzro17P0ye3YAncN77sM7k-9yvRo5bOW-Y7Xuu7o6dtYVGAw63EahkxFiU_BnmEu2OSxxFFo8H7fdUwNg_toL9mSwVOUW78U.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=UCpBYxD1j0YQ7kNvwEjMBQX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTA4NDQwNzYyMzgxNTg1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc5LCJiaXRyYXRlIjo4MTI1MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0h9YyzsN-l66_mD1SsmrH7rWnhl-6EEYTfNXy0_t2IMg&amp;oe=69DC5812</BaseURL><SegmentBase indexRange=\"833-1068\" timescale=\"44100\" FBMinimumPrefetchRange=\"1069-2473\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1069-27043\" FBFirstSegmentRange=\"1069-51854\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"51855-99431\" FBPrefetchSegmentRange=\"1069-51854\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"978669417850651a\" bandwidth=\"102347\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"102347\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1022342\" FBPaqMos=\"92.82\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMESQJj16tpVAVqVHlbFCf_XnCdLYV1CqtzeK3D8qobLwJ7RqBH3uSMzldZKXhFvESpyJZn-IZQUluxiSHrzRwadj48nFAI27N23w4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=MjjghuQ8YHIQ7kNvwEmJAXg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTA4NDQwNzYyMzgxNTg1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc5LCJiaXRyYXRlIjoxMDI0NTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=iL2VWqusHSKjb48JZjT3iQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Wp8ap_xWFcT5VXBXzE1yRynBYpKAYTPbsmY8MOErmpw&amp;oe=69DC68AD</BaseURL><SegmentBase indexRange=\"833-1068\" timescale=\"44100\" FBMinimumPrefetchRange=\"1069-2561\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1069-33421\" FBFirstSegmentRange=\"1069-64612\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"64613-124669\" FBPrefetchSegmentRange=\"1069-64612\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870656897376334293",
      "id": "3870656897376334293_13239728305",
      "code": "DW3VfDHiDHV",
      "taken_at": "2026-04-08T08:51:20Z",
      "taken_at_ts": 1775638280,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": {
        "pk": 1015608660,
        "name": "Barcelona España",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 2.1447806867305,
        "lat": 41.491580045974,
        "external_id": "162052480661219",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "13239728305",
        "id": "13239728305",
        "username": "cattery_solette",
        "full_name": "Anzhela Kavalevich",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/414442984_2985087991653686_79199780473185183_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gHJ1t3hemKBDOWUjMRXWMdOG_vDDINLh4DYx_wgowdkR19PZjqmIAFyFypYj2d9Us8&_nc_ohc=ZB3nnfAHtb4Q7kNvwEjeRFj&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GOjlsxg2pV3165oKAJ_jZN3HXxkBbkULAAAB1501500j-ccb7-5&oh=00_Af17ulW5yE5BZXdbTS0_SeVe0t5L0k2sU8CnGYPduS6ZTw&oe=69DC384C&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 29,
      "comments_disabled": false,
      "like_count": 462,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Hola queridos amigos ❤️ nuestra princesita Felicia os desea que tengais un maravilloso día 🥰 \n.\n📌 No d!spon\n.\n#feliciasolette",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870656347435966818",
          "id": "3870656347435966818_13239728305",
          "video_url": null,
          "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/655755652_18159615649440306_1518109390108740959_n.jpg?stp=dst-jpegr_e35_tt6&_nc_cat=103&ig_cache_key=Mzg3MDY1NjM0NzQzNTk2NjgxOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=UWIuAwEAkxwQ7kNvwFdWxg5&_nc_oc=AdoI8cpidAYP9xjxMxyiMrkxiiafqlK_RT2GRz1T5-OnrEnLA-oKr_5JIHPeV1bWn_4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2XnBHkaTtEUk_WVS8hlyp_PZg9x9UU_FpjcZjHGGGZSQ&oe=69DC41E7",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                40863,
                81727,
                122591
              ],
              "height": 1733,
              "scans_profile": "e35",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/655755652_18159615649440306_1518109390108740959_n.jpg?stp=dst-jpegr_e35_tt6&_nc_cat=103&ig_cache_key=Mzg3MDY1NjM0NzQzNTk2NjgxOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=UWIuAwEAkxwQ7kNvwFdWxg5&_nc_oc=AdoI8cpidAYP9xjxMxyiMrkxiiafqlK_RT2GRz1T5-OnrEnLA-oKr_5JIHPeV1bWn_4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2XnBHkaTtEUk_WVS8hlyp_PZg9x9UU_FpjcZjHGGGZSQ&oe=69DC41E7",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                20122,
                40245,
                60368
              ],
              "height": 903,
              "scans_profile": "e35",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/655755652_18159615649440306_1518109390108740959_n.jpg?stp=dst-jpegr_e35_p750x750_sh0.08_tt6&_nc_cat=103&ig_cache_key=Mzg3MDY1NjM0NzQzNTk2NjgxOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=UWIuAwEAkxwQ7kNvwFdWxg5&_nc_oc=AdoI8cpidAYP9xjxMxyiMrkxiiafqlK_RT2GRz1T5-OnrEnLA-oKr_5JIHPeV1bWn_4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af3_5WB2x_hekWBazLMdsp_yh_u_R-dsgpdwGmvzS8xkPw&oe=69DC41E7",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870656897376334293_13239728305",
          "commerciality_status": "not_commercial",
          "taken_at": 1775638277
        },
        {
          "pk": "3870656352695625894",
          "id": "3870656352695625894_13239728305",
          "video_url": null,
          "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662503333_18159615658440306_5966436535173011756_n.jpg?stp=dst-jpegr_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDY1NjM1MjY5NTYyNTg5NA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=WNafPRsaliEQ7kNvwHdN42Z&_nc_oc=Adqf-a5CjEMmzc0jePHkRVdicY35RuieJdrM6if-9l8jMtU_C0DfyZRpMuPUFG6OvNY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2w7Do57sSgLBb9G1PCEalXoZEG8zSFik2FFoYX6w2hvA&oe=69DC521B",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                41382,
                82765,
                124148
              ],
              "height": 1733,
              "scans_profile": "e35",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662503333_18159615658440306_5966436535173011756_n.jpg?stp=dst-jpegr_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDY1NjM1MjY5NTYyNTg5NA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=WNafPRsaliEQ7kNvwHdN42Z&_nc_oc=Adqf-a5CjEMmzc0jePHkRVdicY35RuieJdrM6if-9l8jMtU_C0DfyZRpMuPUFG6OvNY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2w7Do57sSgLBb9G1PCEalXoZEG8zSFik2FFoYX6w2hvA&oe=69DC521B",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                20378,
                40756,
                61135
              ],
              "height": 903,
              "scans_profile": "e35",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662503333_18159615658440306_5966436535173011756_n.jpg?stp=dst-jpegr_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDY1NjM1MjY5NTYyNTg5NA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=WNafPRsaliEQ7kNvwHdN42Z&_nc_oc=Adqf-a5CjEMmzc0jePHkRVdicY35RuieJdrM6if-9l8jMtU_C0DfyZRpMuPUFG6OvNY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af0bclQzjlxq2aZLEuAtDXo9FUilCWdmJDDVxCKoOUoCZA&oe=69DC521B",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870656897376334293_13239728305",
          "commerciality_status": "not_commercial",
          "taken_at": 1775638277
        },
        {
          "pk": "3870656351789646447",
          "id": "3870656351789646447_13239728305",
          "video_url": null,
          "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661760449_18159615685440306_7641365032704972699_n.jpg?stp=dst-jpegr_e35_tt6&_nc_cat=107&ig_cache_key=Mzg3MDY1NjM1MTc4OTY0NjQ0Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMi5oZHIuQzMifQ%3D%3D&_nc_ohc=h1Q_R6qjo2cQ7kNvwHURyoX&_nc_oc=Adqt6xZvY2HwVNbSADIc1dK72-GXeX-VRf7_1UdqAVnvHk9V6EL-7ixxUc60rZ4KU7w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af1HW1oWVv9y3sZb28M9q-MklDm1JsVyrr3jtn3lGB4vBQ&oe=69DC3BDC",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                38611,
                77223,
                115835
              ],
              "height": 1732,
              "scans_profile": "e35",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661760449_18159615685440306_7641365032704972699_n.jpg?stp=dst-jpegr_e35_tt6&_nc_cat=107&ig_cache_key=Mzg3MDY1NjM1MTc4OTY0NjQ0Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMi5oZHIuQzMifQ%3D%3D&_nc_ohc=h1Q_R6qjo2cQ7kNvwHURyoX&_nc_oc=Adqt6xZvY2HwVNbSADIc1dK72-GXeX-VRf7_1UdqAVnvHk9V6EL-7ixxUc60rZ4KU7w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af1HW1oWVv9y3sZb28M9q-MklDm1JsVyrr3jtn3lGB4vBQ&oe=69DC3BDC",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                19008,
                38016,
                57025
              ],
              "height": 902,
              "scans_profile": "e35",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661760449_18159615685440306_7641365032704972699_n.jpg?stp=dst-jpegr_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg3MDY1NjM1MTc4OTY0NjQ0Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMi5oZHIuQzMifQ%3D%3D&_nc_ohc=h1Q_R6qjo2cQ7kNvwHURyoX&_nc_oc=Adqt6xZvY2HwVNbSADIc1dK72-GXeX-VRf7_1UdqAVnvHk9V6EL-7ixxUc60rZ4KU7w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2suH2H5sRTAqIA6Jd6eJkwZWzine0LMl-UvzzZ23X2eA&oe=69DC3BDC",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870656897376334293_13239728305",
          "commerciality_status": "not_commercial",
          "taken_at": 1775638277
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            40863,
            81727,
            122591
          ],
          "height": 1733,
          "scans_profile": "e35",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/655755652_18159615649440306_1518109390108740959_n.jpg?stp=dst-jpegr_e35_tt6&_nc_cat=103&ig_cache_key=Mzg3MDY1NjM0NzQzNTk2NjgxOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=UWIuAwEAkxwQ7kNvwFdWxg5&_nc_oc=AdoI8cpidAYP9xjxMxyiMrkxiiafqlK_RT2GRz1T5-OnrEnLA-oKr_5JIHPeV1bWn_4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af2XnBHkaTtEUk_WVS8hlyp_PZg9x9UU_FpjcZjHGGGZSQ&oe=69DC41E7",
          "width": 1440,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            20122,
            40245,
            60368
          ],
          "height": 903,
          "scans_profile": "e35",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/655755652_18159615649440306_1518109390108740959_n.jpg?stp=dst-jpegr_e35_p750x750_sh0.08_tt6&_nc_cat=103&ig_cache_key=Mzg3MDY1NjM0NzQzNTk2NjgxOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTczMy5oZHIuQzMifQ%3D%3D&_nc_ohc=UWIuAwEAkxwQ7kNvwFdWxg5&_nc_oc=AdoI8cpidAYP9xjxMxyiMrkxiiafqlK_RT2GRz1T5-OnrEnLA-oKr_5JIHPeV1bWn_4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=iL2VWqusHSKjb48JZjT3iQ&_nc_ss=7a3ba&oh=00_Af3_5WB2x_hekWBazLMdsp_yh_u_R-dsgpdwGmvzS8xkPw&oe=69DC41E7",
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
    }
  ],
  "WyIwYTFmODY0NjFmYmQ0ZmViYjdjZDYzZTg4OTE3N2E5ZSIsW10sMV0="
]
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

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/recent",
        headers={"x-access-key": "YOUR_TOKEN"},
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
    # Next page: add &max_id=... from previous response
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"name": "love"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
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
    "pk": "3870771007451871805",
    "id": "3870771007451871805_375121505",
    "code": "DW3vbkaDLo9",
    "taken_at": "2026-04-08T12:38:17Z",
    "taken_at_ts": 1775651897,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFKg8eG&_nc_oc=AdoAZiSsiuOipBWd4A0OcOOIUETL_ILBQQ29CN3gaFNlukWgtPPgZtvXWDjW_4zd2CU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af0z2rFE_Pk8ZnrBUxeQyNEkOPweuhQh1FjdBeW_VwClww&oe=69DC5703",
    "location": null,
    "user": {
      "pk": "375121505",
      "id": "375121505",
      "username": "fallinginsociety",
      "full_name": "FallingInSociety",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=8UGwMTx74pgQ7kNvwHOW241&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af0GnzR8IxI4-M7pnRQoy70cK1DzU2iANxjUHQ_jmN0F_Q&oe=69DC3771&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 5,
    "comments_disabled": false,
    "like_count": 387,
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
        "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFKg8eG&_nc_oc=AdoAZiSsiuOipBWd4A0OcOOIUETL_ILBQQ29CN3gaFNlukWgtPPgZtvXWDjW_4zd2CU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af0z2rFE_Pk8ZnrBUxeQyNEkOPweuhQh1FjdBeW_VwClww&oe=69DC5703",
        "width": 1079,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          7924,
          15848,
          23772
        ],
        "height": 765,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFKg8eG&_nc_oc=AdoAZiSsiuOipBWd4A0OcOOIUETL_ILBQQ29CN3gaFNlukWgtPPgZtvXWDjW_4zd2CU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af2dGHse8rpa8jZdu5-IzgTn72s2UvV9GXSHUZbZi4wE2A&oe=69DC5703",
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
    "pk": "3870734620916604460",
    "id": "3870734620916604460_39341580224",
    "code": "DW3nKEzil4s",
    "taken_at": "2026-04-08T11:28:19Z",
    "taken_at_ts": 1775647699,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/661788723_1908751309845927_8173444236989701420_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=Mzg3MDczNDYyMDkxNjYwNDQ2MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=uQaCjbLDI1MQ7kNvwHlQ9AW&_nc_oc=AdoB6rhaE0sxDmgiiuouPfxQ_UvtQYXvbLAuxa2gofiZLf_rAMNLpCZ0HvPOQMAllKM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af1dU6wR2ZxEveYYWufgtbfoL-S0sgoMaljrM2J0jOEqGg&oe=69DC6A31",
    "location": null,
    "user": {
      "pk": "39341580224",
      "id": "39341580224",
      "username": "rishii_2909",
      "full_name": "status_4You",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658831137_18074110451308225_9143662132794746305_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=w4Y9QtWnnPsQ7kNvwFta3Pe&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCH3RCfB1hTFTjZAAMHla7tD0OR_bmNDAQAB1501500j-ccb7-5&oh=00_Af0BS4fkCNG0HnthfsmxB3xR7d_2tWfOPIZVKBzGZ_tyPg&oe=69DC544A&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 530,
    "play_count": 1080,
    "has_liked": false,
    "caption_text": "💔...\n.\n.\n.#ɴᴇᴡᴘᴏs#trending#lovelife #like4like #love reels ᴛ reels",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPBAcj5cX9fydi4IjJrIuYuw_sNMrbdO9nWrH3Tir5WGDqJM1ortIkYNdUbtP140OSiviJJfbZmEmQkbOKoAyzTU24gkw92yYAquFI.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=yIzoUgFwnBQQ7kNvwFdQNps&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzQxOTA2NDQzMDgyMjUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=cb77632c04be7b47&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BNzQ4OUIyREJFQkEyRUYxMDRFNDk1MjUzOUFEMTQ4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0UwNDk5QTM4RTk5NUU1QTFBODNDM0QzOTE0QkFDQkE4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaCpKePrpibQBUCKAJDMywXQD3u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1nFCqd7-pXIOfY8OCHHxNa72XBenWtBrsIYSD5xtPbfw&oe=69D85706",
    "view_count": 0,
    "video_duration": 29.933000564575195,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          5528,
          11056,
          16584
        ],
        "height": 1136,
        "scans_profile": "e15",
        "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/661788723_1908751309845927_8173444236989701420_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=Mzg3MDczNDYyMDkxNjYwNDQ2MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=uQaCjbLDI1MQ7kNvwHlQ9AW&_nc_oc=AdoB6rhaE0sxDmgiiuouPfxQ_UvtQYXvbLAuxa2gofiZLf_rAMNLpCZ0HvPOQMAllKM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af1dU6wR2ZxEveYYWufgtbfoL-S0sgoMaljrM2J0jOEqGg&oe=69DC6A31",
        "width": 640,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1220251,
        "height": 1280,
        "id": "3487374221426438v",
        "type": 101,
        "url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPBAcj5cX9fydi4IjJrIuYuw_sNMrbdO9nWrH3Tir5WGDqJM1ortIkYNdUbtP140OSiviJJfbZmEmQkbOKoAyzTU24gkw92yYAquFI.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=yIzoUgFwnBQQ7kNvwFdQNps&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzQxOTA2NDQzMDgyMjUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=cb77632c04be7b47&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BNzQ4OUIyREJFQkEyRUYxMDRFNDk1MjUzOUFEMTQ4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0UwNDk5QTM4RTk5NUU1QTFBODNDM0QzOTE0QkFDQkE4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaCpKePrpibQBUCKAJDMywXQD3u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1nFCqd7-pXIOfY8OCHHxNa72XBenWtBrsIYSD5xtPbfw&oe=69D85706",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1220251,
        "height": 1280,
        "id": "3487374221426438v",
        "type": 102,
        "url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPBAcj5cX9fydi4IjJrIuYuw_sNMrbdO9nWrH3Tir5WGDqJM1ortIkYNdUbtP140OSiviJJfbZmEmQkbOKoAyzTU24gkw92yYAquFI.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=yIzoUgFwnBQQ7kNvwFdQNps&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzQxOTA2NDQzMDgyMjUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=cb77632c04be7b47&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BNzQ4OUIyREJFQkEyRUYxMDRFNDk1MjUzOUFEMTQ4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0UwNDk5QTM4RTk5NUU1QTFBODNDM0QzOTE0QkFDQkE4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaCpKePrpibQBUCKAJDMywXQD3u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1nFCqd7-pXIOfY8OCHHxNa72XBenWtBrsIYSD5xtPbfw&oe=69D85706",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1220251,
        "height": 1280,
        "id": "3487374221426438v",
        "type": 103,
        "url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPBAcj5cX9fydi4IjJrIuYuw_sNMrbdO9nWrH3Tir5WGDqJM1ortIkYNdUbtP140OSiviJJfbZmEmQkbOKoAyzTU24gkw92yYAquFI.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=yIzoUgFwnBQQ7kNvwFdQNps&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzQxOTA2NDQzMDgyMjUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=cb77632c04be7b47&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BNzQ4OUIyREJFQkEyRUYxMDRFNDk1MjUzOUFEMTQ4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0UwNDk5QTM4RTk5NUU1QTFBODNDM0QzOTE0QkFDQkE4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaCpKePrpibQBUCKAJDMywXQD3u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1nFCqd7-pXIOfY8OCHHxNa72XBenWtBrsIYSD5xtPbfw&oe=69D85706",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "clips_metadata": {
      "clips_creation_entry_point": "clips",
      "featured_label": null,
      "is_public_chat_welcome_video": false,
      "professional_clips_upsell_type": 0,
      "show_tips": null,
      "achievements_info": {
        "num_earned_achievements": null,
        "show_achievements": false
      },
      "additional_audio_info": {
        "additional_audio_username": null,
        "audio_reattribution_info": {
          "should_allow_restore": false
        }
      },
      "asset_recommendation_info": null,
      "audio_ranking_info": {
        "best_audio_cluster_id": "746030898131356"
      },
      "audio_type": "licensed_music",
      "basel_template_info_for_ig_app": {
        "is_basel_template": null,
        "should_show_reuse_setting_for_owner": false,
        "use_template_deeplink": null
      },
      "branded_content_tag_info": {
        "can_add_tag": false
      },
      "breaking_content_info": null,
      "breaking_creator_info": null,
      "challenge_info": null,
      "content_appreciation_info": null,
      "contextual_highlight_info": null,
      "cutout_sticker_info": [],
      "disable_use_in_clips_client_cache": false,
      "external_media_info": null,
      "is_fan_club_promo_video": false,
      "is_shared_to_fb": false,
      "mashup_info": {
        "can_toggle_mashups_allowed": false,
        "formatted_mashups_count": null,
        "has_been_mashed_up": false,
        "has_nonmimicable_additional_audio": false,
        "is_creator_requesting_mashup": false,
        "is_light_weight_check": true,
        "is_light_weight_reuse_allowed_check": false,
        "is_pivot_page_available": false,
        "is_reuse_allowed": true,
        "mashup_type": null,
        "mashups_allowed": true,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18149039953024476",
      "music_info": {
        "music_canonical_id": 18149039953024476,
        "music_asset_info": {
          "allows_saving": false,
          "artist_id": "1477660303783528",
          "audio_asset_id": "2123658304364973",
          "audio_cluster_id": "294272578099791",
          "cover_artwork_thumbnail_uri": "https://scontent-lga3-2.cdninstagram.com/v/t39.30808-6/427583528_1546646502779909_5068748275901251878_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=8FbJEHFjdpYQ7kNvwElsyk9&_nc_oc=AdrGZ2gJSpNSyFOLkSvlr2H74bbLuBDF7aQUWBBEiYcIgRjCISSNYiRLMKhuZb9G52I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a39b&oh=00_Af17xSncl0acCLeLUCBJ7HrFW_LSpgrpmv61ryxyNpEQNQ&oe=69DC40DE",
          "cover_artwork_uri": "https://scontent-lga3-2.cdninstagram.com/v/t39.30808-6/427583528_1546646502779909_5068748275901251878_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=8FbJEHFjdpYQ7kNvwElsyk9&_nc_oc=AdrGZ2gJSpNSyFOLkSvlr2H74bbLuBDF7aQUWBBEiYcIgRjCISSNYiRLMKhuZb9G52I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a39b&oh=00_Af17xSncl0acCLeLUCBJ7HrFW_LSpgrpmv61ryxyNpEQNQ&oe=69DC40DE",
          "dark_message": null,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT312.23999S\"><Period id=\"0\" duration=\"PT312.23999S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1904861696756727a\" bandwidth=\"66457\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66457\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m69/AQMf1cl846vjq-NcfmAC3gx99Rb5xqcx_JNTkqSkuLDgtcKFdj557p2yx0STGwRkeC6SM_cu0T0A66Kx4cZgYPVD.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=QsDDvaL9CxsQ7kNvwHInE37&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo0NDU3NTY5NTEzNDM4MTYsImFzc2V0X2FnZV9kYXlzIjoyNjY1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzEyLCJiaXRyYXRlIjo2NjUyNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2Dt65gLbc-IzKaPuRjKR_HzC6wka8V8XB2loH-ga9W7w&amp;oe=69DC54AB</BaseURL><SegmentBase indexRange=\"824-2739\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "display_artist": "Arijit Singh",
          "duration_in_ms": 312240,
          "fast_start_progressive_download_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m69/AQMf1cl846vjq-NcfmAC3gx99Rb5xqcx_JNTkqSkuLDgtcKFdj557p2yx0STGwRkeC6SM_cu0T0A66Kx4cZgYPVD.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=QsDDvaL9CxsQ7kNvwHInE37&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo0NDU3NTY5NTEzNDM4MTYsImFzc2V0X2FnZV9kYXlzIjoyNjY1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzEyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=b6312b690028e853&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HREtGTWlBa2tsdEE2NGdDQU5ZeUdCVzlGU2xqYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkMvti7zaygEVAigCQzMsF0Bzg9cKPXCkGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af33M3ccksXi2lppbSBhZrctjSqrNA5GBokMZsULAjfgHQ&oe=69DC54AB",
          "has_lyrics": false,
          "highlight_start_times_in_ms": [
            59000,
            139000,
            250500
          ],
          "id": "2123658304364973",
          "ig_username": "arijitsingh",
          "is_eligible_for_audio_effects": false,
          "is_eligible_for_vinyl_sticker": true,
          "is_explicit": false,
          "licensed_music_subtype": "DEFAULT",
          "progressive_download_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m69/AQMf1cl846vjq-NcfmAC3gx99Rb5xqcx_JNTkqSkuLDgtcKFdj557p2yx0STGwRkeC6SM_cu0T0A66Kx4cZgYPVD.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=QsDDvaL9CxsQ7kNvwHInE37&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo0NDU3NTY5NTEzNDM4MTYsImFzc2V0X2FnZV9kYXlzIjoyNjY1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzEyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=b6312b690028e853&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HREtGTWlBa2tsdEE2NGdDQU5ZeUdCVzlGU2xqYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkMvti7zaygEVAigCQzMsF0Bzg9cKPXCkGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af33M3ccksXi2lppbSBhZrctjSqrNA5GBokMZsULAjfgHQ&oe=69DC54AB",
          "reactive_audio_download_url": null,
          "sanitized_title": null,
          "song_monetization_info": null,
          "subtitle": "",
          "title": "Aaj Se Teri",
          "web_30s_preview_download_url": null,
          "lyrics": null,
          "spotify_track_metadata": null,
          "related_audios": null
        },
        "music_consumption_info": {
          "allow_media_creation_with_music": true,
          "music_creation_restriction_reason": null,
          "audio_asset_start_time_in_ms": 135007,
          "derived_content_start_time_in_composition_in_ms": 0,
          "contains_lyrics": null,
          "derived_content_id": null,
          "display_labels": null,
          "formatted_clips_media_count": null,
          "is_bookmarked": false,
          "is_trending_in_clips": false,
          "overlap_duration_in_ms": 29907,
          "placeholder_profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=HMeNVRbt-xsQ7kNvwFJODYr&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4AAAAA&ccb=7-5&oh=00_Af2vW55GjoYX4gYPevmKpTMtYsArVtMsMVndK5MiGycROg&oe=69DC5D7D&_nc_sid=472314",
          "should_allow_music_editing": false,
          "should_mute_audio": false,
          "should_mute_audio_reason": "",
          "should_mute_audio_reason_type": null,
          "should_render_soundwave": false,
          "trend_rank": null,
          "previous_trend_rank": null,
          "ig_artist": {
            "strong_id__": "8179014770",
            "pk": 8179014770,
            "pk_id": "8179014770",
            "id": "8179014770",
            "username": "arijitsingh",
            "full_name": "Arijit Singh",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "2711226980484677711_8179014770",
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/258874952_1115934952480051_2100666748796338283_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=exNbLKeRv7UQ7kNvwEqijXi&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GEgebg8zXW-a7-YDAGsAezlHEScdbkULAAAB1501500j-ccb7-5&oh=00_Af0qoowZI1TKrOu-odf7FOMXYjIINDNADwX2GBLSt-t-aw&oe=69DC648A&_nc_sid=472314"
          },
          "audio_filter_infos": [],
          "audio_muting_info": {
            "mute_audio": false,
            "mute_reason_str": "",
            "allow_audio_editing": false,
            "show_muted_audio_toast": false
          },
          "user_notes": null,
          "related_audios": null
        }
      },
      "nux_info": null,
      "original_sound_info": null,
      "originality_info": null,
      "reels_on_the_rise_info": null,
      "reusable_text_attribute_string": null,
      "reusable_text_info": null,
      "shopping_info": null,
      "show_achievements": false,
      "template_info": null,
      "may_have_template_info": null,
      "viewer_interaction_settings": null
    },
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT29.933332S\" FBManifestTimestamp=\"1775664044\" FBManifestIdentifier=\"Ftjus50NGBBpZ19kYXNoX2Jhc2VsaW5lGTbkw+2wz+qyA4z81dry77EMitXZzdKYyl8iGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABYAFAASFAIA\"><Period id=\"0\" duration=\"PT29.933332S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:74.5\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"6\"/><Representation id=\"3487374221426438v\" bandwidth=\"1155198\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"4322366\" FBPlaybackResolutionMos=\"0:100,360:86,480:84,720:79.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.2,480:94.6,720:93\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPBAcj5cX9fydi4IjJrIuYuw_sNMrbdO9nWrH3Tir5WGDqJM1ortIkYNdUbtP140OSiviJJfbZmEmQkbOKoAyzTU24gkw92yYAquFI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=yIzoUgFwnBQQ7kNvwFdQNps&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NDE5MDY0NDMwODIyNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyOSwiYml0cmF0ZSI6MTE1NTE5OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=AH1tgjCtS7lC4AOMsF07ng&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0ZslP_9wOgAzbQb6hT1rBfsdj-hAuQiDnUJjldlrJt6A&amp;oe=69D85706</BaseURL><SegmentBase indexRange=\"893-996\" timescale=\"15360\" FBMinimumPrefetchRange=\"997-70724\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"997-386326\" FBFirstSegmentRange=\"997-771347\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"771348-1500787\" FBPrefetchSegmentRange=\"997-771347\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-892\"/></SegmentBase></Representation><Representation id=\"26903273912612165v\" bandwidth=\"131209\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"490943\" FBPlaybackResolutionMos=\"0:100,360:72.9,480:67.7,720:58.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.5,480:82.5,720:73.5\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQP769DIjlq9Wz8c5qZ3iPDcGyTKHgwDkg6YMavZOYl-3HLNEybABWUOouH9JbGeCNek6hXPRGMftlnkRons8agI36dGX_OCizMJBEo.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=IrDxg8jmB00Q7kNvwEkQKK6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NDE5MDY0NDMwODIyNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyOSwiYml0cmF0ZSI6MTMxMjA5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=AH1tgjCtS7lC4AOMsF07ng&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1JpIgCzruB8L4z-a_0lN8_jA6cOa_fWCO4ZaWR8D37Ig&amp;oe=69D85BE5</BaseURL><SegmentBase indexRange=\"888-991\" timescale=\"15360\" FBMinimumPrefetchRange=\"992-18905\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-56531\" FBFirstSegmentRange=\"992-100083\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"100084-181870\" FBPrefetchSegmentRange=\"992-100083\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-887\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"956207813472498a\" bandwidth=\"64777\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"64777\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"243384\" FBPaqMos=\"92.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_F3mz5vYoCgJm5-oa4vh8rWuuzATl6VU8_kpUHl2THsWbjwO0sN7eysMHCxXY8rz3nIOgMLHdtfd1VZsGgDu36qBcBDt2H2LS-wI.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=zX6cQGjKqA0Q7kNvwF0baMC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NDE5MDY0NDMwODIyNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyOSwiYml0cmF0ZSI6NjUwNTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=AH1tgjCtS7lC4AOMsF07ng&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3zJQcTH8BvVGSZyOWfmTVjNBBvxvr2-UkDvSo7xznbuQ&amp;oe=69D84DAA</BaseURL><SegmentBase indexRange=\"824-1035\" timescale=\"44100\" FBMinimumPrefetchRange=\"1036-1379\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1036-18356\" FBFirstSegmentRange=\"1036-15471\" FBFirstSegmentDuration=\"2021\" FBSecondSegmentRange=\"15472-29793\" FBPrefetchSegmentRange=\"1036-29793\" FBPrefetchSegmentDuration=\"4017\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870729737757151899",
    "id": "3870729737757151899_49646700667",
    "code": "DW3mDBAjlKb",
    "taken_at": "2026-04-08T11:20:02Z",
    "taken_at_ts": 1775647202,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=wngMxYac1rMQ7kNvwGHkeRX&_nc_oc=Adrv8zOISfRePqjwYvRKekkzXO6DwwXUOZnr7ImhuhUILsudeAOzJfvFLQCiz4DAP10&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af0OIssAzlw23ZJR0K4l9fy9-RBKK6u2M842UBH7nADXAQ&oe=69DC4396",
    "location": {
      "pk": 226738352,
      "name": "Apopka, Florida",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "",
      "city": "",
      "zip": null,
      "lng": -81.5258,
      "lat": 28.6899,
      "external_id": "107549262599145",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "49646700667",
      "id": "49646700667",
      "username": "chosen_2_reign",
      "full_name": "𝐂𝐢𝐧𝐝𝐲 & 𝐖𝐞𝐧𝐝𝐲",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/245410687_270162081680252_8621949966077360040_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40ODAuYzIifQ&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=6IiLqxbZRAgQ7kNvwEY5siP&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GH_roA58C_kCtvUAAKh3OyfQUad3bkULAAAB1501500j-ccb7-5&oh=00_Af0lrX_qbL5Rqnr2EwxReBAvcoA0hPWb-qH8v8mRUTa-vA&oe=69DC51EE&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 125,
    "comments_disabled": false,
    "like_count": 3,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "𝗚𝗼𝗼𝗱 𝗺𝗼𝗿𝗻𝗶𝗻𝗴 𝗳𝗮𝗺𝗶𝗹𝘆 💝\n𝗜𝗳 𝘆𝗼𝘂 𝘄𝗼𝗸𝗲 𝘂𝗽 𝘁𝗵𝗶𝘀 𝗺𝗼𝗿𝗻𝗶𝗻𝗴… \n𝗚𝗼𝗱 𝗶𝘀 𝗻𝗼𝘁 𝗱𝗼𝗻𝗲 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂 𝘆𝗲𝘁. \n\nToday, we rise with gratitude in our \nhearts & praise on our lips. God has \nbeen so good to us. He woke us up, \ncovered us, and is leading us into a \nnew day filled w/ purpose & promise.\n\n“Because of the Lord’s great love \nwe are not consumed, for His \nmercies never fail. They are new \nevery morning; great is Your \nfaithfulness.” — 𝗟𝗮𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻𝘀 𝟯:𝟮𝟮–𝟮𝟯\n\n𝗣𝗿𝗮𝘆𝗲𝗿:\nLord, thank You for the gift of today.\nEven if my heart feels heavy, help \nme choose gratitude. Remind me that \nYou are with me, guiding me, and \nworking all things for good. Give me \npeace for what I can’t control and \nstrength for what’s ahead. Let my \nlife reflect Your love today. In Jesus’ \nname, Amen. 🤍✨\n\n𝗗𝗲𝗰𝗹𝗮𝗿𝗮𝘁𝗶𝗼𝗻:\nToday, I will walk in gratitude.\nI will trust God with every step.\nI am covered, I am guided, and I am \nnot alone. This day holds purpose, \nand I will walk in it. 🙌🏼✨\n\n𝗚𝗼𝗱 𝗯𝗹𝗲𝘀𝘀 𝘆𝗼𝘂 𝗽𝗿𝗲𝗰𝗶𝗼𝘂𝘀 𝗰𝗵𝗶𝗹𝗱! 👑\n\n𝐈𝐟 𝐲𝐨𝐮 𝐤𝐧𝐨𝐰 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐭𝐡𝐚𝐭 𝐧𝐞𝐞𝐝𝐬 \n𝐭𝐡𝐢𝐬 𝐞𝐧𝐜𝐨𝐮𝐫𝐚𝐠𝐞𝐦𝐞𝐧𝐭, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐡𝐚𝐫𝐞 \n& 𝐭𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 🙏🏼\n\n#chosen2reign #childlikefaith #godfirst\n#trustinthelord #happywednesday",
    "accessibility_caption": null,
    "usertags": [
      {
        "user": {
          "pk": "201558512",
          "id": "201558512",
          "username": "wendy_saved_by_grace",
          "full_name": "Wendy Huber",
          "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/184015669_492120375249882_7370163052157690695_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=LmbLdMmoC1oQ7kNvwFjmHsP&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDXb9wraSye0lL8BAEdjkUQ-FEhmbkULAAAB1501500j-ccb7-5&oh=00_Af1ZxoxVXXkdweHiKuNhH6miWAs1ZsRj1_Q_opKHjdG-Pg&oe=69DC4B92&_nc_sid=472314",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "x": 0.8106060606000001,
        "y": 0.9836601298000001
      },
      {
        "user": {
          "pk": "307509295",
          "id": "307509295",
          "username": "elevationworship",
          "full_name": "Elevation Worship",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/619566013_18550293298053296_8897657889483886820_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=8anF_jWdEBkQ7kNvwFO2aq1&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GL3T7SSwgIK6ZOdBAOSQo2u11Hp7bmNDAQAB1501500j-ccb7-5&oh=00_Af2xAttqO6Vwm_tcEHv1KuQZnvBzk57MfSWPlEKmhX0IKw&oe=69DC5DA1&_nc_sid=472314",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "x": 0.8549242424,
        "y": 0.9836601298000001
      },
      {
        "user": {
          "pk": "6258535637",
          "id": "6258535637",
          "username": "cindy_saved_by_grace",
          "full_name": "Cindy Moore",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/468367136_545676408366967_6972864757526950554_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=szV8GBoN7jQQ7kNvwHYyPsM&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCC36ht3p3swSvABAJryO5uNl8RgbkULAAAB1501500j-ccb7-5&oh=00_Af3lIy0jKd6jAPVsaM7ge9YcMzhKS4v5-8oyVNn9t3oIEQ&oe=69DC3EB9&_nc_sid=472314",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "x": 0.7916666667000001,
        "y": 0.9836601298000001
      }
    ],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          31926,
          63853,
          95780
        ],
        "height": 1800,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=wngMxYac1rMQ7kNvwGHkeRX&_nc_oc=Adrv8zOISfRePqjwYvRKekkzXO6DwwXUOZnr7ImhuhUILsudeAOzJfvFLQCiz4DAP10&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af0OIssAzlw23ZJR0K4l9fy9-RBKK6u2M842UBH7nADXAQ&oe=69DC4396",
        "width": 1440,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          15722,
          31445,
          47168
        ],
        "height": 938,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=wngMxYac1rMQ7kNvwGHkeRX&_nc_oc=Adrv8zOISfRePqjwYvRKekkzXO6DwwXUOZnr7ImhuhUILsudeAOzJfvFLQCiz4DAP10&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&_nc_ss=7a3ba&oh=00_Af1lKkXjxkoeEXc3PbyQY2jMXn0MNCEH8Kl8P8BnuDdOEQ&oe=69DC4396",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "clips_metadata": {},
    "video_dash_manifest": "",
    "like_and_view_counts_disabled": true,
    "coauthor_producers": [
      {
        "strong_id__": "6258535637",
        "pk": 6258535637,
        "pk_id": "6258535637",
        "id": "6258535637",
        "username": "cindy_saved_by_grace",
        "full_name": "Cindy Moore",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "3508521783842475593_6258535637",
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/468367136_545676408366967_6972864757526950554_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=szV8GBoN7jQQ7kNvwHYyPsM&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCC36ht3p3swSvABAJryO5uNl8RgbkULAAAB1501500j-ccb7-5&oh=00_Af3lIy0jKd6jAPVsaM7ge9YcMzhKS4v5-8oyVNn9t3oIEQ&oe=69DC3EB9&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      },
      {
        "strong_id__": "201558512",
        "pk": 201558512,
        "pk_id": "201558512",
        "id": "201558512",
        "username": "wendy_saved_by_grace",
        "full_name": "Wendy Huber",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "2570751627756893814_201558512",
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/184015669_492120375249882_7370163052157690695_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGksZRD2jp8qUUkRCBMw1eWenYtXRunWCu1wKAMq17LtT331k2Ho5Fw6HlvHLwz4ls&_nc_ohc=LmbLdMmoC1oQ7kNvwFjmHsP&_nc_gid=AH1tgjCtS7lC4AOMsF07ng&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDXb9wraSye0lL8BAEdjkUQ-FEhmbkULAAAB1501500j-ccb7-5&oh=00_Af1ZxoxVXXkdweHiKuNhH6miWAs1ZsRj1_Q_opKHjdG-Pg&oe=69DC4B92&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      }
    ],
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
      "pk": "3870809376467023305",
      "id": "3870809376467023305_1765726798",
      "code": "DW34J6VkXXJ",
      "taken_at": "2026-04-08T13:57:22Z",
      "taken_at_ts": 1775656642,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/662300139_1961770747765232_7748473666959299630_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ig_cache_key=Mzg3MDgwOTM3NjQ2NzAyMzMwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=RcRZg-JjpckQ7kNvwEUX71J&_nc_oc=AdogCSYWr-SFZBT-ZM-8oMfILw_rGYfCQ9bwWdpftoYe3gDBXSYTIL8mL--8iS6qb4c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&oh=00_Af1tXaNOGjIXMyHSEk-guEe1Qifrb3t3FJcwhY3Ijb0B_w&oe=69DC3FEB",
      "location": null,
      "user": {
        "pk": "1765726798",
        "id": "1765726798",
        "username": "officialquinnpratt5",
        "full_name": "Quinn Pratt",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/399296473_866481388364313_2638115332035364263_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgUAp2UqfIKCtXDbNcjjhHMcugMs-2nb8qJHDSY_6cOKxqpoTa3EtXR-aOdyWq_is&_nc_ohc=1_vYz6a9sf4Q7kNvwGr8Cdi&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GNnHzBcZoltrDxQDAKfFesrqd5wkbkULAAAB1501500j-ccb7-5&oh=00_Af2z5tDLY3Y6IoPMR7D8GdjRlWtQQCyL0p3hbB3AYE7ldA&oe=69DC62D8&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 135,
      "comments_disabled": false,
      "like_count": 1442,
      "play_count": 17178,
      "has_liked": false,
      "caption_text": "Don’t mess with a man’s dog. #Dog #love #viral #comedy #funny.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPDXfCagct6o-0ap5xBuMUSykQNSg7PJucuSFQuFVzrJjzvfYwDnSyKIVMOQIppSlQewwAeLBR5uSWjBmfZC6VYe6bh9kwQUji0CV8.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=wmPB7kO796sQ7kNvwFFtOwx&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNTc2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTY2MzM3NTgxMTM1MDgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=22f91a36b3399feb&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80RDRCNTg3RUI0MzNEOUQ4MUE5MTZGQzc1MEZCQkY5Q192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzg3NEM0QkYwRUYzQ0RFNEU2NUE0OTc4QUM0QTkyMzgzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbI-5yI093lPxUCKAJDMywXQE2u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0YubcZXNAwXD9PoaZsx5cyMXpcrxxFu0YLoiJuoNf0wQ&oe=69D842A1",
      "view_count": 0,
      "video_duration": 59.36600112915039,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            5946,
            11892,
            17839
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/662300139_1961770747765232_7748473666959299630_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ig_cache_key=Mzg3MDgwOTM3NjQ2NzAyMzMwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=RcRZg-JjpckQ7kNvwEUX71J&_nc_oc=AdogCSYWr-SFZBT-ZM-8oMfILw_rGYfCQ9bwWdpftoYe3gDBXSYTIL8mL--8iS6qb4c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&oh=00_Af1tXaNOGjIXMyHSEk-guEe1Qifrb3t3FJcwhY3Ijb0B_w&oe=69DC3FEB",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1087944,
          "height": 1024,
          "id": "1267490342230390v",
          "type": 101,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPDXfCagct6o-0ap5xBuMUSykQNSg7PJucuSFQuFVzrJjzvfYwDnSyKIVMOQIppSlQewwAeLBR5uSWjBmfZC6VYe6bh9kwQUji0CV8.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=wmPB7kO796sQ7kNvwFFtOwx&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNTc2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTY2MzM3NTgxMTM1MDgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=22f91a36b3399feb&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80RDRCNTg3RUI0MzNEOUQ4MUE5MTZGQzc1MEZCQkY5Q192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzg3NEM0QkYwRUYzQ0RFNEU2NUE0OTc4QUM0QTkyMzgzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbI-5yI093lPxUCKAJDMywXQE2u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0YubcZXNAwXD9PoaZsx5cyMXpcrxxFu0YLoiJuoNf0wQ&oe=69D842A1",
          "url_expiration_timestamp_us": null,
          "width": 576,
          "fallback": null
        },
        {
          "bandwidth": 1087944,
          "height": 1024,
          "id": "1267490342230390v",
          "type": 102,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPDXfCagct6o-0ap5xBuMUSykQNSg7PJucuSFQuFVzrJjzvfYwDnSyKIVMOQIppSlQewwAeLBR5uSWjBmfZC6VYe6bh9kwQUji0CV8.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=wmPB7kO796sQ7kNvwFFtOwx&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNTc2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTY2MzM3NTgxMTM1MDgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=22f91a36b3399feb&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80RDRCNTg3RUI0MzNEOUQ4MUE5MTZGQzc1MEZCQkY5Q192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzg3NEM0QkYwRUYzQ0RFNEU2NUE0OTc4QUM0QTkyMzgzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbI-5yI093lPxUCKAJDMywXQE2u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0YubcZXNAwXD9PoaZsx5cyMXpcrxxFu0YLoiJuoNf0wQ&oe=69D842A1",
          "url_expiration_timestamp_us": null,
          "width": 576,
          "fallback": null
        },
        {
          "bandwidth": 1087944,
          "height": 1024,
          "id": "1267490342230390v",
          "type": 103,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPDXfCagct6o-0ap5xBuMUSykQNSg7PJucuSFQuFVzrJjzvfYwDnSyKIVMOQIppSlQewwAeLBR5uSWjBmfZC6VYe6bh9kwQUji0CV8.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=wmPB7kO796sQ7kNvwFFtOwx&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNTc2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTY2MzM3NTgxMTM1MDgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=22f91a36b3399feb&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80RDRCNTg3RUI0MzNEOUQ4MUE5MTZGQzc1MEZCQkY5Q192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzg3NEM0QkYwRUYzQ0RFNEU2NUE0OTc4QUM0QTkyMzgzX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbI-5yI093lPxUCKAJDMywXQE2u2RaHKwIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0YubcZXNAwXD9PoaZsx5cyMXpcrxxFu0YLoiJuoNf0wQ&oe=69D842A1",
          "url_expiration_timestamp_us": null,
          "width": 576,
          "fallback": null
        }
      ],
      "clips_metadata": {
        "clips_creation_entry_point": "clips",
        "featured_label": null,
        "is_public_chat_welcome_video": false,
        "professional_clips_upsell_type": 0,
        "show_tips": null,
        "achievements_info": {
          "num_earned_achievements": null,
          "show_achievements": false
        },
        "additional_audio_info": {
          "additional_audio_username": null,
          "audio_reattribution_info": {
            "should_allow_restore": false
          }
        },
        "asset_recommendation_info": null,
        "audio_ranking_info": {
          "best_audio_cluster_id": "26470184565978984"
        },
        "audio_type": "original_sounds",
        "basel_template_info_for_ig_app": {
          "is_basel_template": null,
          "should_show_reuse_setting_for_owner": false,
          "use_template_deeplink": null
        },
        "branded_content_tag_info": {
          "can_add_tag": false
        },
        "breaking_content_info": null,
        "breaking_creator_info": null,
        "challenge_info": null,
        "content_appreciation_info": null,
        "contextual_highlight_info": null,
        "cutout_sticker_info": [],
        "disable_use_in_clips_client_cache": false,
        "external_media_info": null,
        "is_fan_club_promo_video": false,
        "is_shared_to_fb": false,
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": false,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": false,
          "is_pivot_page_available": false,
          "is_reuse_allowed": true,
          "mashup_type": null,
          "mashups_allowed": true,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18576688639058858",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26515391588099669,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": true,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT59.234104S\" FBManifestTimestamp=\"1775664047\" FBManifestIdentifier=\"Ft7us50NKRaG34PjzoSKBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT59.234104S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1429444408408003a\" bandwidth=\"41503\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"41503\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m78/AQNw34QQ6d6KeUUbfwP98AtUlYv5QJAmR96mV6Pupzdtiz3tcA539NBwm_rpis6KIA65sL7-PPK8qHimoxs2xLK2XdIvSKjlZmF-2so.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=l2IHMmRqi6sQ7kNvwHfdOzZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU2NjMzNzU4MTEzNTA4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU5LCJiaXRyYXRlIjo0MTY2NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af19jPgqbYacGru3-GUVLy2mplw61fikBMTcbxelfHxnuQ&amp;oe=69D85F8B</BaseURL><SegmentBase indexRange=\"824-1215\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 59000,
          "formatted_clips_media_count": null,
          "hide_remixing": false,
          "is_audio_automatically_attributed": false,
          "is_eligible_for_audio_effects": true,
          "is_eligible_for_vinyl_sticker": true,
          "is_explicit": false,
          "is_original_audio_download_eligible": true,
          "is_reuse_disabled": false,
          "is_xpost_from_fb": false,
          "music_canonical_id": null,
          "oa_owner_is_music_artist": false,
          "original_audio_subtype": "default",
          "original_audio_title": "Original audio",
          "original_media_id": 3870809376467023305,
          "progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQOTDBxaMtNFvex-fujBHsel1sa0YNeXfycr4DLjvMaGVsEf8zQONdjlSjDK8cPUFt9UeeS1UivbNAkJDHkPwW9g.mp4?strext=1&_nc_cat=106&_nc_sid=8bf8fe&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=S1KlcyEMhSwQ7kNvwGAYIKy&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTY2MzM3NTgxMTM1MDgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3TIeHGouzKoIyIsck9NIfeFYSR0xmvezCZD5Ka30KdwQ&oe=69DC6814",
          "should_mute_audio": false,
          "time_created": 1775656603,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "1765726798",
            "pk": 1765726798,
            "pk_id": "1765726798",
            "id": "1765726798",
            "username": "officialquinnpratt5",
            "full_name": "Quinn Pratt",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3231007389960004846_1765726798",
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/399296473_866481388364313_2638115332035364263_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgUAp2UqfIKCtXDbNcjjhHMcugMs-2nb8qJHDSY_6cOKxqpoTa3EtXR-aOdyWq_is&_nc_ohc=1_vYz6a9sf4Q7kNvwGr8Cdi&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GNnHzBcZoltrDxQDAKfFesrqd5wkbkULAAAB1501500j-ccb7-5&oh=00_Af2z5tDLY3Y6IoPMR7D8GdjRlWtQQCyL0p3hbB3AYE7ldA&oe=69DC62D8&_nc_sid=472314"
          },
          "audio_filter_infos": null,
          "audio_parts": [],
          "audio_parts_by_filter": [],
          "consumption_info": {
            "display_media_id": null,
            "is_bookmarked": false,
            "is_trending_in_clips": false,
            "should_mute_audio_reason": "",
            "should_mute_audio_reason_type": null,
            "inline_audio_label": null,
            "display_labels": null,
            "user_notes": null
          },
          "xpost_fb_creator_info": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "originality_info": null,
        "reels_on_the_rise_info": null,
        "reusable_text_attribute_string": null,
        "reusable_text_info": null,
        "shopping_info": null,
        "show_achievements": false,
        "template_info": null,
        "may_have_template_info": null,
        "viewer_interaction_settings": null
      },
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT59.366665S\" FBManifestTimestamp=\"1775664047\" FBManifestIdentifier=\"Ft7us50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZluqjzePonKcD1qfKgsL7swTeu9iS1dG5BNLt5La59MYE7Nzs/ISEmgWMlN2Uj5jpBbLcyNX5rcEHmtPnzKznjwjqmr6g/q6mCCIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT59.366665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:72.2\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1638686677247238v\" bandwidth=\"120698\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"895683\" FBPlaybackResolutionMos=\"0:100,360:62.6,480:57.9,576:56.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.3,480:90.9,576:89.2,720:89.2,1080:89.2\" FBAbrPolicyTags=\"\" width=\"576\" height=\"1024\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"180p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP9lRTQqQJoMtYCaMipB259kzmLOnQENa9pqvIyd69toBgh9c9sgOKUpSMcPqJgyEQcLYT7jyIA9hXBnjX941avc8pa3fPX05-hKKU.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=n3KXz3DuUMQQ7kNvwF1z4SM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NjYzMzc1ODExMzUwOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1OSwiYml0cmF0ZSI6MTIwNjk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af04B1ClJko55yzHAHco81loga42C_F1FrLgf_mfT1sDgw&amp;oe=69DC38BC</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"15360\" FBMinimumPrefetchRange=\"1002-17589\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-48890\" FBFirstSegmentRange=\"1002-78636\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"78637-148994\" FBPrefetchSegmentRange=\"1002-78636\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"930681936521461v\" bandwidth=\"251180\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"1863966\" FBPlaybackResolutionMos=\"0:100,360:74.1,480:70.1,576:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.4,480:96.5,576:95.6,720:95.6,1080:95.6\" FBAbrPolicyTags=\"\" width=\"576\" height=\"1024\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMHdKL4GbEWGDGPoFsIIqa7R3A_6NXJElqED1WdTZT9-_yKgNSmCvjxhk7KiCrulkOPBq2madh4sIO3LfAyKEo3hx1YZyU1jFrWSEw.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=-FpIbAVMaXIQ7kNvwHcqce7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NjYzMzc1ODExMzUwOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1OSwiYml0cmF0ZSI6MjUxMTgwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Kk5Ge3-K8UXZtVhYpFCT07W1M-2CdkOMeZ82ZC90Miw&amp;oe=69DC68E6</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"15360\" FBMinimumPrefetchRange=\"1002-27990\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-95672\" FBFirstSegmentRange=\"1002-164759\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"164760-314792\" FBPrefetchSegmentRange=\"1002-164759\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2114050772768537v\" bandwidth=\"384437\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"2852849\" FBPlaybackResolutionMos=\"0:100,360:78.3,480:74.6,576:73.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.94,480:98.5,576:97.8,720:97.8,1080:97.8\" FBAbrPolicyTags=\"\" width=\"576\" height=\"1024\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNE81e1t10L1KYtY7GCEIiA72phCF85zNeCQuPYReVDfMc86wxeFo8eVVrD90u7l10FbpayO2o2iPg3nZvlTBNf8Zecu-tIihWpZ3s.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=sHLps7VzeukQ7kNvwGsJLKU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NjYzMzc1ODExMzUwOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1OSwiYml0cmF0ZSI6Mzg0NDM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1M4Gpacudr7FMv3MiUWDMJ4SOz5tDusTSsyAw6C4vvSQ&amp;oe=69DC51C8</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"15360\" FBMinimumPrefetchRange=\"1002-34112\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-139737\" FBFirstSegmentRange=\"1002-252110\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"252111-479211\" FBPrefetchSegmentRange=\"1002-252110\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1281832107416425v\" bandwidth=\"510112\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"3785463\" FBPlaybackResolutionMos=\"0:100,360:81.4,480:77,576:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.527,480:99.224,576:98.94,720:98.94,1080:98.94\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"576\" height=\"1024\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOsn3EBJDxDXSN7jzux9KSiHvDX8YeycSU9HK0U_Bs-t8-le0dFDG5H1TtD1IHNtI5E4bQhyERluh5RqeqKZ4992BSdD8BvllyH2O4.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=pkskIpZK2kgQ7kNvwGAPsAN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NjYzMzc1ODExMzUwOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1OSwiYml0cmF0ZSI6NTEwMTEyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af27vBkOjznnoUg_4Rvx0IZxJ_BJAzckXvSO4UYaDjuEpA&amp;oe=69DC3991</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"15360\" FBMinimumPrefetchRange=\"1002-37888\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-181645\" FBFirstSegmentRange=\"1002-339303\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"339304-640846\" FBPrefetchSegmentRange=\"1002-339303\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2286560675165389v\" bandwidth=\"718195\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"5329607\" FBPlaybackResolutionMos=\"0:100,360:84.1,480:79.9,576:78.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.833,480:99.823,576:99.864,720:99.864,1080:99.864\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"576\" height=\"1024\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOp1QyHAcUF7FV_pfFhYRZTYtqrMDj_my7bEKLBcFdZ1Ss6bh5FlFJAyCQkI4G_B23dohv7x9DQ9pQcpxufJRwuCe2T7Eyz_TTSFt0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=zJD7fhhDW78Q7kNvwGVWIkp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NjYzMzc1ODExMzUwOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1OSwiYml0cmF0ZSI6NzE4MTk1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1y5pdVNw6zM-Bqs86Qt3hgyJBffeUJHQ7qpY1zBDq1oQ&amp;oe=69DC335B</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"15360\" FBMinimumPrefetchRange=\"1002-42673\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-249886\" FBFirstSegmentRange=\"1002-481596\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"481597-906822\" FBPrefetchSegmentRange=\"1002-481596\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1464618875459382v\" bandwidth=\"1039809\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"7716251\" FBPlaybackResolutionMos=\"0:100,360:85.9,480:82.1,576:80.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.935,480:99.948,576:99.986,720:99.986,1080:99.986\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"576\" height=\"1024\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMm6J6GTIpuhUoedGgxjXQ6sNWYl4igsxtGtVigSZUUeDDhHpZ7EVMAZo8CfGd2vxJeN-xyfc9G3UEwTEwv9LGMOC5ERf5p0wIBRU4.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=uHpq_EEyMTcQ7kNvwEgt_X9&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NjYzMzc1ODExMzUwOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1OSwiYml0cmF0ZSI6MTAzOTgwOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3nuAEno_PibtKF0XOcsUb93g96I654pt_sXVsvbvf3Ew&amp;oe=69DC4EA7</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"15360\" FBMinimumPrefetchRange=\"1002-46350\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-357383\" FBFirstSegmentRange=\"1002-705322\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"705323-1328238\" FBPrefetchSegmentRange=\"1002-705322\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2336169916876469a\" bandwidth=\"34258\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"34258\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"254664\" FBPaqMos=\"90.57\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"1\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNvDicpkehhF0Pj5cCVIFMUYWUZu_6GSCfqtvMI_lpC35EotZmRV_zFCEeZ0aN3x7oMvJ01p7kh9aribvQP9A59dAMq2mYE_2WkzeY.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=FagZqGX8R0MQ7kNvwGWgq9k&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU2NjMzNzU4MTEzNTA4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU5LCJiaXRyYXRlIjozNDM5NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2yrMYn7pRzvocnHDDKXdAlGjp2WmkhYJ9Mv1Uu0XGqNQ&amp;oe=69DC3B42</BaseURL><SegmentBase indexRange=\"827-1014\" timescale=\"44100\" FBMinimumPrefetchRange=\"1015-1984\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1015-11890\" FBFirstSegmentRange=\"1015-22851\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"22852-45791\" FBPrefetchSegmentRange=\"1015-22851\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-826\"/></SegmentBase></Representation><Representation id=\"1240172077861355a\" bandwidth=\"39284\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"39284\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"291877\" FBPaqMos=\"85.31\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"1\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNltXCZQu4J0HdaYbY9JOsmcFjAIniIlxKw2zZoreZs9ovQuPgKaQaA3WQMfSjHv2pZbEp-rKAOJKbelQeryMz4c1XOPvdJGBtVODs.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=l0ZKauqpABIQ7kNvwH8W0MV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU2NjMzNzU4MTEzNTA4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU5LCJiaXRyYXRlIjozOTQyMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2qPmQUvEzRTsTKSsE7A1X0h3srvHToI3bN8q3HvjQ0pw&amp;oe=69DC5DE5</BaseURL><SegmentBase indexRange=\"828-1015\" timescale=\"44100\" FBMinimumPrefetchRange=\"1016-2073\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1016-13443\" FBFirstSegmentRange=\"1016-25299\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"25300-50573\" FBPrefetchSegmentRange=\"1016-25299\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-827\"/></SegmentBase></Representation><Representation id=\"1252647229918959a\" bandwidth=\"51709\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"51709\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"383867\" FBPaqMos=\"90.06\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"1\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMz7oNzzamVG3AjVmVBGw5azXhFFbT72K3iNoPw5YTl97DjJZ8YbG83stDscHh7bZ8vVfhzKjtyXj9Xv8sO1qxG41dIvtKF531chUY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=3mZOhZabVScQ7kNvwEo6e8u&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU2NjMzNzU4MTEzNTA4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU5LCJiaXRyYXRlIjo1MTg0NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1DaqHFk1yg374tIWHcXiwzY_7S-6mAkjtWIOZ6HzQp1g&amp;oe=69DC59CD</BaseURL><SegmentBase indexRange=\"825-1012\" timescale=\"44100\" FBMinimumPrefetchRange=\"1013-2318\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1013-17354\" FBFirstSegmentRange=\"1013-32914\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"32915-65596\" FBPrefetchSegmentRange=\"1013-32914\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-824\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870814013311774562",
      "id": "3870814013311774562_46914369422",
      "code": "DW35NYvDW9i",
      "taken_at": "2026-04-08T14:04:45Z",
      "taken_at_ts": 1775657085,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/658872336_941625884942449_5002385790465364788_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDAxMzMxMTc3NDU2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vSa1EG8MJ0MQ7kNvwF69gw1&_nc_oc=AdohJXERAL00u80Z6CcdUt-Lzrxkfu7KFkgSrfADLPZ-qnNqXw3NJEs9WhOvvDLz4DM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&oh=00_Af20QpOtdj9GraQiaymItNoKiWWdIAVPWQ6daSFpZclcAw&oe=69DC43BA",
      "location": null,
      "user": {
        "pk": "46914369422",
        "id": "46914369422",
        "username": "my_lattakia",
        "full_name": "My Lattakia | لاذقيتي",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/648688632_18073626773561423_7317965678043620162_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHgUAp2UqfIKCtXDbNcjjhHMcugMs-2nb8qJHDSY_6cOKxqpoTa3EtXR-aOdyWq_is&_nc_ohc=vP8Kbfc0WOQQ7kNvwF-amOb&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GPgzqiZPIKQn3jVAAEJjSg4Do45lbmNDAQAB1501500j-ccb7-5&oh=00_Af0ccBkMBsRaY8lyYToHkJxwBQEFoiKBboBfsf9Cwki19g&oe=69DC368A&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 32,
      "comments_disabled": false,
      "like_count": 329,
      "play_count": 3869,
      "has_liked": false,
      "caption_text": "لادقيتي 🩵\n.\n.\n.\n.\n.\n.\n#explore #fyp #reels #syria #explorepage #love #instagram #viral #sea",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQN3GEwcv11o4Wc1XWTwlbAhmIN2KWzPJ08Lmmqon-wtyD3Ts9FzYFXDXO2p9BD6GWrIw8vy6Bt5-PjDaxiduCjY4n7WVZoCRSlkxak.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=u-KlQZAaUWYQ7kNvwGGxkUV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzc1NDE4NjM1NjE0MjMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=34db5e17c3a949d3&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83RDQ1RDdENjlCMEY3RDk1NUI5NkU2NTQ2QkREQkI4NF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JCNDRGNjMyOUFERjYxNzJCNzVBNDk4MDc5NDE1MTlGX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACae44TTttucQBUCKAJDMywXQDQQ5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af23lfrgHPIvTw_l6EUeHBfKn_ROJTAvdADY2ZWM_NYxdg&oe=69D84CFB",
      "view_count": 0,
      "video_duration": 20.084999084472656,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            6450,
            12900,
            19351
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/658872336_941625884942449_5002385790465364788_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDAxMzMxMTc3NDU2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vSa1EG8MJ0MQ7kNvwF69gw1&_nc_oc=AdohJXERAL00u80Z6CcdUt-Lzrxkfu7KFkgSrfADLPZ-qnNqXw3NJEs9WhOvvDLz4DM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&oh=00_Af20QpOtdj9GraQiaymItNoKiWWdIAVPWQ6daSFpZclcAw&oe=69DC43BA",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1759556,
          "height": 1280,
          "id": "4263986047199134v",
          "type": 101,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQN3GEwcv11o4Wc1XWTwlbAhmIN2KWzPJ08Lmmqon-wtyD3Ts9FzYFXDXO2p9BD6GWrIw8vy6Bt5-PjDaxiduCjY4n7WVZoCRSlkxak.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=u-KlQZAaUWYQ7kNvwGGxkUV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzc1NDE4NjM1NjE0MjMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=34db5e17c3a949d3&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83RDQ1RDdENjlCMEY3RDk1NUI5NkU2NTQ2QkREQkI4NF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JCNDRGNjMyOUFERjYxNzJCNzVBNDk4MDc5NDE1MTlGX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACae44TTttucQBUCKAJDMywXQDQQ5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af23lfrgHPIvTw_l6EUeHBfKn_ROJTAvdADY2ZWM_NYxdg&oe=69D84CFB",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1759556,
          "height": 1280,
          "id": "4263986047199134v",
          "type": 102,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQN3GEwcv11o4Wc1XWTwlbAhmIN2KWzPJ08Lmmqon-wtyD3Ts9FzYFXDXO2p9BD6GWrIw8vy6Bt5-PjDaxiduCjY4n7WVZoCRSlkxak.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=u-KlQZAaUWYQ7kNvwGGxkUV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzc1NDE4NjM1NjE0MjMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=34db5e17c3a949d3&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83RDQ1RDdENjlCMEY3RDk1NUI5NkU2NTQ2QkREQkI4NF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JCNDRGNjMyOUFERjYxNzJCNzVBNDk4MDc5NDE1MTlGX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACae44TTttucQBUCKAJDMywXQDQQ5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af23lfrgHPIvTw_l6EUeHBfKn_ROJTAvdADY2ZWM_NYxdg&oe=69D84CFB",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1759556,
          "height": 1280,
          "id": "4263986047199134v",
          "type": 103,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQN3GEwcv11o4Wc1XWTwlbAhmIN2KWzPJ08Lmmqon-wtyD3Ts9FzYFXDXO2p9BD6GWrIw8vy6Bt5-PjDaxiduCjY4n7WVZoCRSlkxak.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=u-KlQZAaUWYQ7kNvwGGxkUV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNzc1NDE4NjM1NjE0MjMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=34db5e17c3a949d3&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83RDQ1RDdENjlCMEY3RDk1NUI5NkU2NTQ2QkREQkI4NF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JCNDRGNjMyOUFERjYxNzJCNzVBNDk4MDc5NDE1MTlGX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACae44TTttucQBUCKAJDMywXQDQQ5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af23lfrgHPIvTw_l6EUeHBfKn_ROJTAvdADY2ZWM_NYxdg&oe=69D84CFB",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "clips_metadata": {
        "clips_creation_entry_point": "clips",
        "featured_label": null,
        "is_public_chat_welcome_video": false,
        "professional_clips_upsell_type": 0,
        "show_tips": null,
        "achievements_info": {
          "num_earned_achievements": null,
          "show_achievements": false
        },
        "additional_audio_info": {
          "additional_audio_username": null,
          "audio_reattribution_info": {
            "should_allow_restore": false
          }
        },
        "asset_recommendation_info": null,
        "audio_ranking_info": {
          "best_audio_cluster_id": "460326914390447"
        },
        "audio_type": "licensed_music",
        "basel_template_info_for_ig_app": {
          "is_basel_template": null,
          "should_show_reuse_setting_for_owner": false,
          "use_template_deeplink": null
        },
        "branded_content_tag_info": {
          "can_add_tag": false
        },
        "breaking_content_info": null,
        "breaking_creator_info": null,
        "challenge_info": null,
        "content_appreciation_info": null,
        "contextual_highlight_info": null,
        "cutout_sticker_info": [],
        "disable_use_in_clips_client_cache": false,
        "external_media_info": null,
        "is_fan_club_promo_video": false,
        "is_shared_to_fb": false,
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": false,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": false,
          "is_pivot_page_available": false,
          "is_reuse_allowed": true,
          "mashup_type": null,
          "mashups_allowed": true,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18149320033045248",
        "music_info": {
          "music_canonical_id": 18149320033045248,
          "music_asset_info": {
            "allows_saving": false,
            "artist_id": "2422089177862131",
            "audio_asset_id": "752118211664077",
            "audio_cluster_id": "460326914390447",
            "cover_artwork_thumbnail_uri": "https://scontent-ams2-1.cdninstagram.com/v/t39.30808-6/427453408_1548957872617088_8621507504237386126_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=_n-CovGS1y4Q7kNvwFgh5HM&_nc_oc=Adqpwo9UhkIDNKERQnWHcLUxAmQ5Zdn_JvzH_WmtqwKAiXiBLW29cmUbyvw2UanSJyI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a39b&oh=00_Af0H_JNj6Ht9v60bh49DvGSmzHUQMyWHM61kDuFSxRXGgA&oe=69DC5F65",
            "cover_artwork_uri": "https://scontent-ams2-1.cdninstagram.com/v/t39.30808-6/427453408_1548957872617088_8621507504237386126_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=_n-CovGS1y4Q7kNvwFgh5HM&_nc_oc=Adqpwo9UhkIDNKERQnWHcLUxAmQ5Zdn_JvzH_WmtqwKAiXiBLW29cmUbyvw2UanSJyI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a39b&oh=00_Af0H_JNj6Ht9v60bh49DvGSmzHUQMyWHM61kDuFSxRXGgA&oe=69DC5F65",
            "dark_message": null,
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT265.053345S\"><Period id=\"0\" duration=\"PT265.053345S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"667899855738406a\" bandwidth=\"61331\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"61331\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQMPPu0rNMo-eJKpyd6so80qgDmNcK2i5lLbfyl64zmPj459xmRICak7E3YaButpwuhbzAvl1lnPFhioTdI1HUFV.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=5ijncaqBbPwQ7kNvwEL5cSb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjozNDEzNDUxNjE4NTM2MDEsImFzc2V0X2FnZV9kYXlzIjoyOTgzLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MjY1LCJiaXRyYXRlIjo2MTQwNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2lqEUGW5UG2K8T7PRjMAhbbuEzixHOoXW_HNaVDIxYtw&amp;oe=69DC52F5</BaseURL><SegmentBase indexRange=\"824-2451\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "display_artist": "Fairuz",
            "duration_in_ms": 265053,
            "fast_start_progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQMPPu0rNMo-eJKpyd6so80qgDmNcK2i5lLbfyl64zmPj459xmRICak7E3YaButpwuhbzAvl1lnPFhioTdI1HUFV.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=5ijncaqBbPwQ7kNvwEL5cSb&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjozNDEzNDUxNjE4NTM2MDEsImFzc2V0X2FnZV9kYXlzIjoyOTgzLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MjY1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=2b32277ec3f6697&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT19VUlNCZGk0UG1LcDBFQUx4MHlPWGdDcEpUYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmwurx0fOcmwEVAigCQzMsF0BwkNkWhysCGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af3dtxW0BbG-w8SRAYWmN6qurcDmn_qxLlgT20Glirnmjg&oe=69DC52F5",
            "has_lyrics": true,
            "highlight_start_times_in_ms": [
              11000,
              26000,
              96000
            ],
            "id": "752118211664077",
            "ig_username": "fayrouz.love1",
            "is_eligible_for_audio_effects": true,
            "is_eligible_for_vinyl_sticker": true,
            "is_explicit": false,
            "licensed_music_subtype": "DEFAULT",
            "progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQMPPu0rNMo-eJKpyd6so80qgDmNcK2i5lLbfyl64zmPj459xmRICak7E3YaButpwuhbzAvl1lnPFhioTdI1HUFV.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=5ijncaqBbPwQ7kNvwEL5cSb&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjozNDEzNDUxNjE4NTM2MDEsImFzc2V0X2FnZV9kYXlzIjoyOTgzLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MjY1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=2b32277ec3f6697&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT19VUlNCZGk0UG1LcDBFQUx4MHlPWGdDcEpUYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmwurx0fOcmwEVAigCQzMsF0BwkNkWhysCGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af3dtxW0BbG-w8SRAYWmN6qurcDmn_qxLlgT20Glirnmjg&oe=69DC52F5",
            "reactive_audio_download_url": null,
            "sanitized_title": null,
            "song_monetization_info": null,
            "subtitle": "",
            "title": "Indi Thika Feek",
            "web_30s_preview_download_url": null,
            "lyrics": null,
            "spotify_track_metadata": null,
            "related_audios": null
          },
          "music_consumption_info": {
            "allow_media_creation_with_music": true,
            "music_creation_restriction_reason": null,
            "audio_asset_start_time_in_ms": 10500,
            "derived_content_start_time_in_composition_in_ms": null,
            "contains_lyrics": null,
            "derived_content_id": null,
            "display_labels": null,
            "formatted_clips_media_count": null,
            "is_bookmarked": false,
            "is_trending_in_clips": false,
            "overlap_duration_in_ms": 20000,
            "placeholder_profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHgUAp2UqfIKCtXDbNcjjhHMcugMs-2nb8qJHDSY_6cOKxqpoTa3EtXR-aOdyWq_is&_nc_ohc=HMeNVRbt-xsQ7kNvwHxTTUN&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&edm=AMKDjl4AAAAA&ccb=7-5&oh=00_Af1aCx_ApVIoNYiY7Hg2d--QIwB33RqBABVkpLNRt31qDA&oe=69DC5D7D&_nc_sid=472314",
            "should_allow_music_editing": false,
            "should_mute_audio": false,
            "should_mute_audio_reason": "",
            "should_mute_audio_reason_type": null,
            "should_render_soundwave": false,
            "trend_rank": null,
            "previous_trend_rank": null,
            "ig_artist": {
              "strong_id__": "6190523710",
              "pk": 6190523710,
              "pk_id": "6190523710",
              "id": "6190523710",
              "username": "fayrouz.love1",
              "full_name": "فَيروّز",
              "is_private": false,
              "is_verified": false,
              "profile_pic_id": "2792616470385083357_6190523710",
              "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/275594467_292376356292240_7383161877255152331_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHgUAp2UqfIKCtXDbNcjjhHMcugMs-2nb8qJHDSY_6cOKxqpoTa3EtXR-aOdyWq_is&_nc_ohc=KHhoNxH20_QQ7kNvwGm68Db&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GOM8bRCQhtss6gkBAMvi-xScQnZmbkULAAAB1501500j-ccb7-5&oh=00_Af2vmFqpBDRIXipAxS86fW2dUziY8Ue4ly6Ljuow-dYY5w&oe=69DC55C4&_nc_sid=472314"
            },
            "audio_filter_infos": [],
            "audio_muting_info": {
              "mute_audio": false,
              "mute_reason_str": "",
              "allow_audio_editing": false,
              "show_muted_audio_toast": false
            },
            "user_notes": null,
            "related_audios": null
          }
        },
        "nux_info": null,
        "original_sound_info": null,
        "originality_info": null,
        "reels_on_the_rise_info": null,
        "reusable_text_attribute_string": null,
        "reusable_text_info": null,
        "shopping_info": null,
        "show_achievements": false,
        "template_info": null,
        "may_have_template_info": null,
        "viewer_interaction_settings": null
      },
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT20.08526S\" FBManifestTimestamp=\"1775664047\" FBManifestIdentifier=\"Ft7us50NGA9yMmF2MS1yMWdlbjJ2cDkZxrDW/tTFoacDitKv7qW0rwP4gY3/v47NA+C5j9OB2sAE/uWwwPqMmAXatJmr0efFBYyY8/7J/sUFoq3S0P+m6AXO+sbUm9eFBpqwlaysw/cHoK+o3OT0nl34osjE6JyKYSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT20.08526S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:84.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1460374042188159v\" bandwidth=\"308605\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"774086\" FBPlaybackResolutionMos=\"0:100,360:61.9,480:54.3,720:45.1,1080:41.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.7,480:85.3,720:78.5,1080:70.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN1W5uYnPvSn2cr3ZUAXbPSGaI1GOtQe0PZosVDwGRMQQpbXnmxBG9SF7MUBNf10wMEUpfP3U4Ccsa9CvYakSwUVrok5ay8-j-b5zo.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=Mcb3COctfWEQ7kNvwGPHyaG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6MzA4NjA1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2OyHjgZUX0OlwMFoU3dKOVI4NQ38vOrcoJbEimC_uo8Q&amp;oe=69DC4EEC</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-44869\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-128577\" FBFirstSegmentRange=\"918-190700\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"190701-365283\" FBPrefetchSegmentRange=\"918-190700\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1701343337701031v\" bandwidth=\"464246\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"1164484\" FBPlaybackResolutionMos=\"0:100,360:68.4,480:61.1,720:52.4,1080:47.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.4,480:88.8,720:83.1,1080:76.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMoOeuYpoJtrAxNmFFnw1nL4BKSMJzZVPsa79SWsp2kbE4qCMiIbzelA0Ot8ByGoqzAn4IJH6Mqxx0wUWXo55lpYbIjz8KYrX0vPQE.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=kbjWzM1lzVUQ7kNvwHNrmux&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6NDY0MjQ2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af11CdLRsxmeEP_i3xOwMyCm44zK9oK8YRnYp2XQs5PfiA&amp;oe=69DC63D5</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-56449\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-189192\" FBFirstSegmentRange=\"918-287193\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"287194-556374\" FBPrefetchSegmentRange=\"918-287193\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1636743267371857v\" bandwidth=\"613646\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"1539229\" FBPlaybackResolutionMos=\"0:100,360:72.3,480:65.6,720:56.6,1080:51.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.8,480:90.6,720:85.8,1080:79.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOkO9NJGDNhzMmyRyAjcg9nJ2uDm3dBM_CM_D33eZScYJo-9Pou2BMU8I_3GWrMDoGbgKTFYmK3FWnvbQ9SUqzGdaQYoIu2fHiPJ04.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=u1qffmknqvoQ7kNvwF11oC1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6NjEzNjQ2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0zAdyUgF7SYpy-pLSnnj465Fklct-Cdugm23GPvbngLQ&amp;oe=69DC4FAD</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-63546\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-245301\" FBFirstSegmentRange=\"918-376677\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"376678-737922\" FBPrefetchSegmentRange=\"918-376677\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"26245149915155408v\" bandwidth=\"879339\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"2205676\" FBPlaybackResolutionMos=\"0:100,360:76.4,480:70.5,720:61.9,1080:56.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.1,480:92.6,720:88.5,1080:82.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPY80Td3ykN5TRMG3UvxdoIKqCJQeLEGAeS4ApXEran8h-M9Ohx0LZgNBz5bDjjPPZpMM-yHhrKvV4Xok0yDqreN1hNa6NQwtAc2yA.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=JsbHwcolCsQQ7kNvwE87K9N&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6ODc5MzM5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0XRGZjRln77OMldysvrNeozPc4OsdnRbjSLmMS0PpRVQ&amp;oe=69DC505C</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-71507\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-330510\" FBFirstSegmentRange=\"918-523147\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"523148-1056292\" FBPrefetchSegmentRange=\"918-523147\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1013998827970684v\" bandwidth=\"1276081\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"3200837\" FBPlaybackResolutionMos=\"0:100,360:81,480:75.1,720:67.2,1080:61.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.3,480:94.1,720:91,1080:85.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPOrHstn2uPjtgl9wnStwxxOQUaUds7UxLclYMiAqzNtT8SBFw2US8WldAL4kqCuBkRanxO_xQaWDsNKMD-X1-Ma4mCgBAksl18_3Q.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=TtFiLeuUdKUQ7kNvwGV7Ikq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6MTI3NjA4MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1mGwXiKqYkaT0xBhxboQyubsLJHjeujtdd-VS__QVo4Q&amp;oe=69DC464A</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-77043\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-446487\" FBFirstSegmentRange=\"918-735052\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"735053-1543408\" FBPrefetchSegmentRange=\"918-735052\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"930763122922904v\" bandwidth=\"1850614\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"4641959\" FBPlaybackResolutionMos=\"0:100,360:85.1,480:79.4,720:71.9,1080:66\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:95.3,720:93,1080:88.7\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNToxMLTS7S1qCjlzt1qk00GtwiYdF81hqImnaWoS19Z_wskN-Ld7NdwOa1HHgfz4zlu3JcEQFFZK1Fw4TB5Q_SGksiRYVHLCenl8E.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=GHnOPL4AL3kQ7kNvwGGbX89&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6MTg1MDYxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3MLM-oRRTCCKS4lNY3haHKiKFVHuFSQsfTNDJZ1hg1BA&amp;oe=69DC3591</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-80462\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-600594\" FBFirstSegmentRange=\"918-1042048\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1042049-2260884\" FBPrefetchSegmentRange=\"918-1042048\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1560887931645229v\" bandwidth=\"2651560\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"6650997\" FBPlaybackResolutionMos=\"0:100,360:88.3,480:83.8,720:76,1080:70.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:96.3,720:94.6,1080:91\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOBmLy4eSRXo1SLhpT914flXs4-DZRxxy5DB6kJL81RBPqCcIzbvoGDyASIIkpKg4kvAsaLjbFYObyBdUzgrfPSGyMIiichaomtLdA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=s9DzWOz8sFcQ7kNvwEDxfy4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6MjY1MTU2MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2niaOI2oMJS2wZo5S4LDgSpbOGbvckwYzxb5Km6-GfiQ&amp;oe=69DC6295</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-85295\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-827529\" FBFirstSegmentRange=\"918-1480709\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1480710-3259333\" FBPrefetchSegmentRange=\"918-1480709\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1268183804800624v\" bandwidth=\"4209628\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"10559152\" FBPlaybackResolutionMos=\"0:100,360:92.2,480:89.2,720:83.6,1080:78.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.5,480:97.3,720:96.4,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPPAlYnYd_PdycJQzNdUXUyasCgXjcrf6uP2WkaKGaM80KclrmSnIAycYJqtpG5XOJo6ASlrO1_FDpHVtvaSbs9RRlTdYW8rdCN6t4.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=ZWz1hfYf6y4Q7kNvwHNjpAE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA3NzU0MTg2MzU2MTQyMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMCwiYml0cmF0ZSI6NDIwOTYyOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3wPSBbO6t7lVYqrwsUwOM7N8yMpAbGvd1iHXs2_ryL5w&amp;oe=69DC33A6</BaseURL><SegmentBase indexRange=\"826-917\" timescale=\"15360\" FBMinimumPrefetchRange=\"918-121452\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-1338421\" FBFirstSegmentRange=\"918-2392892\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"2392893-5275992\" FBPrefetchSegmentRange=\"918-2392892\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1561282082661894a\" bandwidth=\"42475\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"42475\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"107569\" FBPaqMos=\"92.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOXAwM_ymWQoJo1jow1jAPAJD9niTeORe0I5QJwKvbiEA7tdtZlg5Wspk26pCjWrYPAsBOxd7nl8zJehhK87PWFGpgxLJiIf61GJVw.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=vvA6PQ9ljqoQ7kNvwFZN34P&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDc3NTQxODYzNTYxNDIzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIwLCJiaXRyYXRlIjo0Mjg0NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1h5S1SIkUZpj5au5kjAD1W-lDQO2R9i3cZ6e5lBOR-UQ&amp;oe=69DC5834</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"44100\" FBMinimumPrefetchRange=\"929-1627\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-13549\" FBFirstSegmentRange=\"929-25800\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"25801-52468\" FBPrefetchSegmentRange=\"929-25800\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"948677458130053a\" bandwidth=\"80098\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"80098\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"202027\" FBPaqMos=\"91.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOpV_WR2Ea6nG77K1X0YbHLAfKeWSERNw0BtiVM2ALwrFXT1QH8WL3Se_XQoJ216903D9iwph4cSfan9UebTvfyRW3_jCavyxLlt3M.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=exJ8GSr_BzAQ7kNvwGDY2Bi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDc3NTQxODYzNTYxNDIzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIwLCJiaXRyYXRlIjo4MDQ2NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1gxWBpw3_ux72TFU0wBBnAmW8nR6cHDUWtE1-dKaX2Aw&amp;oe=69DC64A7</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"44100\" FBMinimumPrefetchRange=\"930-1659\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-24282\" FBFirstSegmentRange=\"930-47254\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"47255-97485\" FBPrefetchSegmentRange=\"930-47254\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"2233165607513101a\" bandwidth=\"119110\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119110\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"299967\" FBPaqMos=\"93.91\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNbgXlWeSlkiKbHUzuk1hDOZGH4CbK3535PiWSq63G9G8IyHZ6nwRAD7JbwB7NhVfY8BuIHQZj_cWfbjy1PpVZB7BXdClOPiuNpwTE.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=M-mm5JjFhqkQ7kNvwEpl4gj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDc3NTQxODYzNTYxNDIzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIwLCJiaXRyYXRlIjoxMTk0NzcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2zxsqTVFie72CTc5QNkkjJqAPmsGP27sAfmYFcnCzTlA&amp;oe=69DC3307</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"44100\" FBMinimumPrefetchRange=\"925-1978\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-36004\" FBFirstSegmentRange=\"925-71599\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"71600-145208\" FBPrefetchSegmentRange=\"925-71599\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"27325558040365244a\" bandwidth=\"133420\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"133420\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"335895\" FBPaqMos=\"94.31\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN4LDwRmNhrSKWQEaXhXpj66dRptdLalNxTCQxQ6oo0BbKXJoCrQw3pXZKWkLThOklkVxp6p5x9UtqhdJQR-kLEdwL-IYXIKTL_i90.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=xiZDtVqLI3QQ7kNvwHQQt5e&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDc3NTQxODYzNTYxNDIzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIwLCJiaXRyYXRlIjoxMzM3ODcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af38ea3E7qKZsAbhL48rVmqcWZvt4SRuTBvXDpiouJlbSg&amp;oe=69DC3678</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"44100\" FBMinimumPrefetchRange=\"925-1978\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-41087\" FBFirstSegmentRange=\"925-80816\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"80817-163568\" FBPrefetchSegmentRange=\"925-80816\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&oh=00_Af2spO3Oa2uVBiC5DBSRS_bgOO6hzQmRjVQQUDuA8g4Ngw&oe=69DC5703",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHgUAp2UqfIKCtXDbNcjjhHMcugMs-2nb8qJHDSY_6cOKxqpoTa3EtXR-aOdyWq_is&_nc_ohc=8UGwMTx74pgQ7kNvwHA5dwc&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af1vVeQ7L_K4kIsiUWeXurl-7e6uGYjTIU1C5IBR82zstw&oe=69DC3771&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 387,
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
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&oh=00_Af2spO3Oa2uVBiC5DBSRS_bgOO6hzQmRjVQQUDuA8g4Ngw&oe=69DC5703",
          "width": 1079,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            7924,
            15848,
            23772
          ],
          "height": 765,
          "scans_profile": "e35",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=j-hDWIAgqJ3FPtqT7KoH2g&_nc_ss=7a3ba&oh=00_Af0z0l8PQgtbwQhAq3kTC1dQssdDqQJRXLktrhnyoLwAcw&oe=69DC5703",
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
    }
  ],
  "WyIwNjgzYTBiMzczZDM0MGI0YTYzMTE4ZTNmZTU2Mzk1OSIsW10sMV0="
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
      "pk": "3870825518413174759",
      "id": "3870825518413174759_927880077",
      "code": "DW370zsiNfn",
      "taken_at": "2026-04-08T14:32:02Z",
      "taken_at_ts": 1775658722,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/659126051_4384705655181138_5048496285282486028_n.jpg?stp=dst-jpegr_e15_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgyNTUxODQxMzE3NDc1OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2Lmhkci5DMyJ9&_nc_ohc=FpE3T5lfgkcQ7kNvwElNF7S&_nc_oc=AdqrptTWO3mJ19s8FIIA-2NzvgSbjhQX0dZNlmRAudJCbf0ybdneSCGeeYtIUpidKFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&oh=00_Af1tNqUB2Nkn6shIWvC1C98hK_WFKYUvFI1xEV6tF4ZU5Q&oe=69DC544F",
      "location": null,
      "user": {
        "pk": "927880077",
        "id": "927880077",
        "username": "krantiprrakashjha",
        "full_name": "Kranti Prakash Jha",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/455906223_1190850028701911_5470488519508325701_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gFCiFN1FZ8hp_sMdWmp4Wfy7m0NWS41YJKLyHQbjhkVO_MBfRPF0igm5-FZ-MueEKc&_nc_ohc=2La-XRAfmYwQ7kNvwHA8pod&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GK_TLBvXCPFgEjsEAEV1JRlTFOtLbkULAAAB1501500j-ccb7-5&oh=00_Af1RteVaFVXyFV5Jasxsluah6tLHDetfluF1hESBxWHQjQ&oe=69DC5F6E&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 63,
      "comments_disabled": false,
      "like_count": 3,
      "play_count": 4036,
      "has_liked": false,
      "caption_text": "Ek Baat Kahun -\nआपकी भी साँसें चल रही हैं, मेरी भी साँसें चल रही हैं..💫\n.\n.\n.\n#ekbaatkahun #breathe #love #belove #krantiprakashjha",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOR2oRcRicE5PIiQJU7OaMeybaXmXZSrrDwlL0pAMWp2AsAWBDzEUSgDknNymbbB7NktWkhx0v_Amh2dS-Gon__m5De9PhYLQk-QQU.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=rYtoBz1-jlEQ7kNvwEEw_J_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg1NzA5MTk0MzUwMDgwNzgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d440b1f912ddf12&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8yNDQzREIwNTA2Q0E0MjUxODhGNjEyQkZGRUIzMEJCMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNDRGNzE4Mzg2QTFGNTUyQzc3QTMwMzhFMDIwOUEwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACac4ZuB5In9QRUCKAJDMywXQEvMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2IQbroq8Es5Rc0neTcy9S6uj4IXK4VMoj_fM0T5eCQ3Q&oe=69D86818",
      "view_count": 0,
      "video_duration": 55.611000061035156,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            10608,
            21217,
            31825
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/659126051_4384705655181138_5048496285282486028_n.jpg?stp=dst-jpegr_e15_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgyNTUxODQxMzE3NDc1OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2Lmhkci5DMyJ9&_nc_ohc=FpE3T5lfgkcQ7kNvwElNF7S&_nc_oc=AdqrptTWO3mJ19s8FIIA-2NzvgSbjhQX0dZNlmRAudJCbf0ybdneSCGeeYtIUpidKFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&oh=00_Af1tNqUB2Nkn6shIWvC1C98hK_WFKYUvFI1xEV6tF4ZU5Q&oe=69DC544F",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 908316,
          "height": 1280,
          "id": "3053730671491257v",
          "type": 101,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOR2oRcRicE5PIiQJU7OaMeybaXmXZSrrDwlL0pAMWp2AsAWBDzEUSgDknNymbbB7NktWkhx0v_Amh2dS-Gon__m5De9PhYLQk-QQU.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=rYtoBz1-jlEQ7kNvwEEw_J_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg1NzA5MTk0MzUwMDgwNzgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d440b1f912ddf12&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8yNDQzREIwNTA2Q0E0MjUxODhGNjEyQkZGRUIzMEJCMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNDRGNzE4Mzg2QTFGNTUyQzc3QTMwMzhFMDIwOUEwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACac4ZuB5In9QRUCKAJDMywXQEvMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2IQbroq8Es5Rc0neTcy9S6uj4IXK4VMoj_fM0T5eCQ3Q&oe=69D86818",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 908316,
          "height": 1280,
          "id": "3053730671491257v",
          "type": 102,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOR2oRcRicE5PIiQJU7OaMeybaXmXZSrrDwlL0pAMWp2AsAWBDzEUSgDknNymbbB7NktWkhx0v_Amh2dS-Gon__m5De9PhYLQk-QQU.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=rYtoBz1-jlEQ7kNvwEEw_J_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg1NzA5MTk0MzUwMDgwNzgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d440b1f912ddf12&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8yNDQzREIwNTA2Q0E0MjUxODhGNjEyQkZGRUIzMEJCMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNDRGNzE4Mzg2QTFGNTUyQzc3QTMwMzhFMDIwOUEwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACac4ZuB5In9QRUCKAJDMywXQEvMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2IQbroq8Es5Rc0neTcy9S6uj4IXK4VMoj_fM0T5eCQ3Q&oe=69D86818",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 908316,
          "height": 1280,
          "id": "3053730671491257v",
          "type": 103,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOR2oRcRicE5PIiQJU7OaMeybaXmXZSrrDwlL0pAMWp2AsAWBDzEUSgDknNymbbB7NktWkhx0v_Amh2dS-Gon__m5De9PhYLQk-QQU.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=rYtoBz1-jlEQ7kNvwEEw_J_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg1NzA5MTk0MzUwMDgwNzgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d440b1f912ddf12&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8yNDQzREIwNTA2Q0E0MjUxODhGNjEyQkZGRUIzMEJCMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNDRGNzE4Mzg2QTFGNTUyQzc3QTMwMzhFMDIwOUEwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACac4ZuB5In9QRUCKAJDMywXQEvMzMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2IQbroq8Es5Rc0neTcy9S6uj4IXK4VMoj_fM0T5eCQ3Q&oe=69D86818",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "clips_metadata": {
        "clips_creation_entry_point": "clips",
        "featured_label": null,
        "is_public_chat_welcome_video": false,
        "professional_clips_upsell_type": 0,
        "show_tips": null,
        "achievements_info": {
          "num_earned_achievements": null,
          "show_achievements": false
        },
        "additional_audio_info": {
          "additional_audio_username": null,
          "audio_reattribution_info": {
            "should_allow_restore": false
          }
        },
        "asset_recommendation_info": null,
        "audio_ranking_info": {
          "best_audio_cluster_id": "1132046312124812"
        },
        "audio_type": "licensed_music",
        "basel_template_info_for_ig_app": {
          "is_basel_template": null,
          "should_show_reuse_setting_for_owner": false,
          "use_template_deeplink": null
        },
        "branded_content_tag_info": {
          "can_add_tag": false
        },
        "breaking_content_info": null,
        "breaking_creator_info": null,
        "challenge_info": null,
        "content_appreciation_info": null,
        "contextual_highlight_info": null,
        "cutout_sticker_info": [],
        "disable_use_in_clips_client_cache": false,
        "external_media_info": null,
        "is_fan_club_promo_video": false,
        "is_shared_to_fb": false,
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": true,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": false,
          "is_pivot_page_available": false,
          "is_reuse_allowed": true,
          "mashup_type": null,
          "mashups_allowed": true,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18150469600003880",
        "music_info": {
          "music_canonical_id": 18150469600003880,
          "music_asset_info": {
            "allows_saving": false,
            "artist_id": "679611353003252",
            "audio_asset_id": "439532776504647",
            "audio_cluster_id": "188139088554918",
            "cover_artwork_thumbnail_uri": "https://scontent-ams2-1.cdninstagram.com/v/t39.30808-6/427861788_3564818117090294_5867225579520667172_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=_NzdrG4GAgoQ7kNvwFq-Dqe&_nc_oc=AdrhsNyBFrTvp-ORsI_0ZrGJS5gjty6l7pbCMVF8K3DIpwlhNojE-BpT2QEUn_qbFmM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a39b&oh=00_Af3y-kWQEqoBs04Rc5FKaRp5KCH1bXJIIiGFQJx3gRBqJg&oe=69DC5420",
            "cover_artwork_uri": "https://scontent-ams2-1.cdninstagram.com/v/t39.30808-6/427861788_3564818117090294_5867225579520667172_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=_NzdrG4GAgoQ7kNvwFq-Dqe&_nc_oc=AdrhsNyBFrTvp-ORsI_0ZrGJS5gjty6l7pbCMVF8K3DIpwlhNojE-BpT2QEUn_qbFmM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a39b&oh=00_Af3y-kWQEqoBs04Rc5FKaRp5KCH1bXJIIiGFQJx3gRBqJg&oe=69DC5420",
            "dark_message": null,
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT335.160004S\"><Period id=\"0\" duration=\"PT335.160004S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1312087417205555a\" bandwidth=\"59411\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"59411\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQNTesc6foEfHY9avT3dtjmtzJeRquG3WWxIklGCbVtURLVQ0weJlpvxW9veA1uxtEdGGI4OLg9Y8RtMZryUanrf.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=BQ6vBXHnOgsQ7kNvwGR_XHa&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5MzQxMDA3NzE1MjQxMzQsImFzc2V0X2FnZV9kYXlzIjoyOTE0LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzM1LCJiaXRyYXRlIjo1OTQ3OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1oHIIHoYhaNVa4cdDBVoPf2iXfM1ad3lcV_-oVyJh4zQ&amp;oe=69DC44FD</BaseURL><SegmentBase indexRange=\"824-2871\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "display_artist": "Shankar Ehsaan Loy, Alka Yagnik, Richa Sharma, Sonu Nigam",
            "duration_in_ms": 335160,
            "fast_start_progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQNTesc6foEfHY9avT3dtjmtzJeRquG3WWxIklGCbVtURLVQ0weJlpvxW9veA1uxtEdGGI4OLg9Y8RtMZryUanrf.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=BQ6vBXHnOgsQ7kNvwGR_XHa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5MzQxMDA3NzE1MjQxMzQsImFzc2V0X2FnZV9kYXlzIjoyOTE0LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzM1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=a88a3ff5714b13a8&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTjdfWWlDOWdpTWViMklQQU9kS1FkTnVxV3B4Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmzLjeiunjqAMVAigCQzMsF0B08o9cKPXDGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af2XrtjB7zeBDUzm3kCQdA58lFyef0ok1Ve6047OuQlQqQ&oe=69DC44FD",
            "has_lyrics": true,
            "highlight_start_times_in_ms": [
              232500,
              97000,
              268500
            ],
            "id": "439532776504647",
            "ig_username": "shankarehsaanloy",
            "is_eligible_for_audio_effects": true,
            "is_eligible_for_vinyl_sticker": true,
            "is_explicit": false,
            "licensed_music_subtype": "DEFAULT",
            "progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQNTesc6foEfHY9avT3dtjmtzJeRquG3WWxIklGCbVtURLVQ0weJlpvxW9veA1uxtEdGGI4OLg9Y8RtMZryUanrf.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=BQ6vBXHnOgsQ7kNvwGR_XHa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5MzQxMDA3NzE1MjQxMzQsImFzc2V0X2FnZV9kYXlzIjoyOTE0LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzM1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=a88a3ff5714b13a8&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTjdfWWlDOWdpTWViMklQQU9kS1FkTnVxV3B4Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmzLjeiunjqAMVAigCQzMsF0B08o9cKPXDGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af2XrtjB7zeBDUzm3kCQdA58lFyef0ok1Ve6047OuQlQqQ&oe=69DC44FD",
            "reactive_audio_download_url": null,
            "sanitized_title": null,
            "song_monetization_info": null,
            "subtitle": "",
            "title": "Kal Ho Naa Ho (From \"Kal Ho Naa Ho\") (Sad)",
            "web_30s_preview_download_url": null,
            "lyrics": null,
            "spotify_track_metadata": null,
            "related_audios": null
          },
          "music_consumption_info": {
            "allow_media_creation_with_music": true,
            "music_creation_restriction_reason": null,
            "audio_asset_start_time_in_ms": 232500,
            "derived_content_start_time_in_composition_in_ms": 0,
            "contains_lyrics": null,
            "derived_content_id": null,
            "display_labels": null,
            "formatted_clips_media_count": null,
            "is_bookmarked": false,
            "is_trending_in_clips": false,
            "overlap_duration_in_ms": 55601,
            "placeholder_profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFCiFN1FZ8hp_sMdWmp4Wfy7m0NWS41YJKLyHQbjhkVO_MBfRPF0igm5-FZ-MueEKc&_nc_ohc=HMeNVRbt-xsQ7kNvwHxTTUN&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&edm=AMKDjl4AAAAA&ccb=7-5&oh=00_Af1lbXDlhc1V7BblYpY9XKtrp3EnYqdXwNGLqFL3iSJ_Wg&oe=69DC5D7D&_nc_sid=472314",
            "should_allow_music_editing": false,
            "should_mute_audio": false,
            "should_mute_audio_reason": "",
            "should_mute_audio_reason_type": null,
            "should_render_soundwave": false,
            "trend_rank": null,
            "previous_trend_rank": null,
            "ig_artist": {
              "strong_id__": "2261454832",
              "pk": 2261454832,
              "pk_id": "2261454832",
              "id": "2261454832",
              "username": "shankarehsaanloy",
              "full_name": "Shankar Ehsaan Loy",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3147383806062828779_2261454832",
              "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/360159042_658152073021127_7509246223196425503_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MjguYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFCiFN1FZ8hp_sMdWmp4Wfy7m0NWS41YJKLyHQbjhkVO_MBfRPF0igm5-FZ-MueEKc&_nc_ohc=dF9AlbyfuNoQ7kNvwELEkfu&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GEKXdxXHRoX4lVYCAB8NkYCnMzZobkULAAAB1501500j-ccb7-5&oh=00_Af1RGCGFfo8raEOcL4LQPDmK-9SSrBmLyh63jzc9Yef9_A&oe=69DC697C&_nc_sid=472314"
            },
            "audio_filter_infos": [],
            "audio_muting_info": {
              "mute_audio": false,
              "mute_reason_str": "",
              "allow_audio_editing": false,
              "show_muted_audio_toast": false
            },
            "user_notes": null,
            "related_audios": null
          }
        },
        "nux_info": null,
        "original_sound_info": null,
        "originality_info": null,
        "reels_on_the_rise_info": null,
        "reusable_text_attribute_string": null,
        "reusable_text_info": null,
        "shopping_info": null,
        "show_achievements": false,
        "template_info": null,
        "may_have_template_info": null,
        "viewer_interaction_settings": null
      },
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.61179S\" FBManifestTimestamp=\"1775664059\" FBManifestIdentifier=\"Fvbus50NGA9yMmF2MS1yMWdlbjJ2cDkZxoSOxOz+u5wDyv2o7LuXpgOose3Qgc6/A9KhpsDr5d8EjP79l77ZjwXQo9m0u/ekBba4j86B3NgFmPmt8NLW5QXSt+i4g+npBbDkv5bFof8GsPDnkdrC4AeUodqGwZ7ZCSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT55.61179S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:83.4\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1602469694139931v\" bandwidth=\"118737\" codecs=\"av01.0.04M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"825225\" FBPlaybackResolutionMos=\"0:100,360:75.9,480:70.8,720:62.8,1080:57.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.5,480:88.3,720:82.6,1080:75.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQM5C54aM8S9yyfpAMp9nnSoj7hxJ5XyrRP2oDX3i_GMBBuVJwE-6YDOm0fqyHCri7QxoXUY-7awhxeT7ZDqoojFf7LohtyumYe3LRg.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=VuazJZ9Bh4MQ7kNvwGdn4oh&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTE4NzM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1RMT5ZPi0Z4Ibel7gYY_LLS5Mb90M77AUxJxs0sdMepw&amp;oe=69DC4C4D</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-15504\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-39704\" FBFirstSegmentRange=\"1018-57043\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"57044-113703\" FBPrefetchSegmentRange=\"1018-57043\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"1630964824784460v\" bandwidth=\"187893\" codecs=\"av01.0.05M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"1305861\" FBPlaybackResolutionMos=\"0:100,360:78.8,480:73.8,720:65.8,1080:59.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.6,480:91.4,720:87.1,1080:81.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMv-uxcgoHc_M7v1EPyrraLWdsufzESloxYwWg4cqIh7jvVf39wbVrGBvZKD-aIPzJ84rMdVsDgLT8-hI1GaK6wq9iLcmcUaxIgcBE.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=g5Uk5oVxlv8Q7kNvwFSGPD5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTg3ODkzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2axSAGc4nD3VOH22f6oNEjghzBVAh9ad8th9OHCam5EA&amp;oe=69DC4874</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-20157\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-62362\" FBFirstSegmentRange=\"1018-92441\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"92442-184449\" FBPrefetchSegmentRange=\"1018-92441\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"2729511987398730v\" bandwidth=\"246230\" codecs=\"av01.0.05M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"1711301\" FBPlaybackResolutionMos=\"0:100,360:80.5,480:75,720:67,1080:60.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.4,480:92.4,720:88.4,1080:83\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOwl2a3jvCGprlZIA1sP6MMPo51S-ms5MVBYzAVTYxGe48cyFEMQ6DzQiLXcFmvDQO5GPF1GN-0LP5TXF04eFfsS9lSRU3CYVIGe2E.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=yOubvJuL0iwQ7kNvwGswNU8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MjQ2MjMwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1SJoBvvrinrPEWWQG-G9R3PZFkiuybP393EREgHYVzyQ&amp;oe=69DC60E8</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-24417\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-81154\" FBFirstSegmentRange=\"1018-121524\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"121525-241390\" FBPrefetchSegmentRange=\"1018-121524\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"1336556711626857v\" bandwidth=\"327237\" codecs=\"av01.0.05M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"2274299\" FBPlaybackResolutionMos=\"0:100,360:82,480:76.1,720:68.1,1080:61.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95,480:93.2,720:89.7,1080:84.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP9qHnbaPpy06mmochrOJfqey7toAsGTWyPcQDBEz0mWPovlSNqUmCvE9Y3KMVDKrNphpfr5qFLymLRCfN57lA30MasZEBAkp7ZLK0.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=2aAU8MtOkzQQ7kNvwH3h7jf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MzI3MjM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1RZJADgAHy5IF9sUAxZ6tTzuFrPlR_K41geMsrMquI8w&amp;oe=69DC3861</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-27508\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-102891\" FBFirstSegmentRange=\"1018-158261\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"158262-318841\" FBPrefetchSegmentRange=\"1018-158261\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"984303644027988v\" bandwidth=\"457511\" codecs=\"av01.0.05M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"3179706\" FBPlaybackResolutionMos=\"0:100,360:83.5,480:77.3,720:69.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.8,480:94.2,720:91.1,1080:86.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP_fZVEl55AeM6XQ8bWFhy9OPA2nfw3arqlYwMWGge3OmLFPbsJpFGZI4Qzs6_l2nA4suEo7l-QzP0NBz-DyEE82SiaRmNXTkjYfwI.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=s4Cl_pZASuEQ7kNvwHlj9LQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NDU3NTExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2MhKw87UPFr3nk3VupRwC08Ju8SZ6BxsSjKGHArxW8cg&amp;oe=69DC4E8B</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-32756\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-140233\" FBFirstSegmentRange=\"1018-219536\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"219537-446560\" FBPrefetchSegmentRange=\"1018-219536\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"1968702034016536v\" bandwidth=\"675219\" codecs=\"av01.0.05M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"4692773\" FBPlaybackResolutionMos=\"0:100,360:85.3,480:79.4,720:71.3,1080:64.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:95,720:92.3,1080:88.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQM6l2OKGAIfLmlUhzilDPFqR5rgeGfXwsbvL0SI_wE1HTt3mt5EOjmH_I0cdhjrWwC2SMZDW_r7KoQyEVACkm6o0JYC4ZarsP5EaNo.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=NmvJMGF5OlUQ7kNvwHnWPGQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Njc1MjE5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ijlMdlmAXAZiAP3mwQRXney4bCrDcXppsAQ6TLvaMAw&amp;oe=69DC5A48</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-40782\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-210157\" FBFirstSegmentRange=\"1018-332287\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"332288-666069\" FBPrefetchSegmentRange=\"1018-332287\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"928390983262053v\" bandwidth=\"1056474\" codecs=\"av01.0.05M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"7342501\" FBPlaybackResolutionMos=\"0:100,360:87.2,480:81.9,720:73.6,1080:66.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.7,480:95.8,720:93.5,1080:90.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOc_jlb-4Xovg79ZfcWvh5mL8spn_1szCstdvS9BVQ-zp2iasfTb16l_Eeel4qV5qGmYIVf15bQrDWEX8n5nxbcT536ZgkMDV29BN4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=P9EB-IFmVO0Q7kNvwFErVG2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTA1NjQ3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af26mf7B0uwxJ49j4V85TH5rgyi6J3C1eQH1rcAxHJgLGg&amp;oe=69DC3D65</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-47776\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-352794\" FBFirstSegmentRange=\"1018-559938\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"559939-1081944\" FBPrefetchSegmentRange=\"1018-559938\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"1488592099289320v\" bandwidth=\"2419519\" codecs=\"av01.0.08M.08.0.110.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"16815659\" FBPlaybackResolutionMos=\"0:100,360:91.2,480:87.7,720:81.2,1080:76.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:97.2,720:96.1,1080:93.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQO8Jrw_E7Kdv_STrkP_0aLutD_OnDLaZy1PZ0uXLOJ2Iaj99ABT7hfr2LocQPOJTREh8P3-BQO1h3O01W-wHGHVrro5fRyl2gMUjzM.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=qcX88yQvCM8Q7kNvwFf4a0h&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODU3MDkxOTQzNTAwODA3OCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MjQxOTUxOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1ytjhK1xiHBRTnjjXpmAY36IUZYxsBMLZLIQpxWC__Aw&amp;oe=69DC6714</BaseURL><SegmentBase indexRange=\"842-1017\" timescale=\"15360\" FBMinimumPrefetchRange=\"1018-92931\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1018-912117\" FBFirstSegmentRange=\"1018-1411217\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1411218-2662954\" FBPrefetchSegmentRange=\"1018-1411217\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"907028218807170a\" bandwidth=\"43699\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"43699\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"304783\" FBPaqMos=\"85.21\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNn3Uc-I1bAkGRiPLAsuOJTUXi7mYCH1awa8CKq98sr7y37746W04NAqKuPjdK64Q6fM6Wrj1wVp9SPh3k1u5-LgYJlIDVE69SLq6E.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=AlI6AEFbjG4Q7kNvwFp_zyJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTcwOTE5NDM1MDA4MDc4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo0Mzg0NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af31RDynar4Lz5v2vSqrBlGbNbKoJmTHcbDT0EdWaA52nw&amp;oe=69DC63CF</BaseURL><SegmentBase indexRange=\"837-1012\" timescale=\"44100\" FBMinimumPrefetchRange=\"1013-2222\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1013-14707\" FBFirstSegmentRange=\"1013-26748\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"26749-52615\" FBPrefetchSegmentRange=\"1013-26748\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1640076673879529a\" bandwidth=\"75465\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"75465\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"525602\" FBPaqMos=\"86.33\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNg7e_yjoRXvRFQAeG-D_l0fWBqpCvQKSYEEVRfPkMR0MFgN-OjxzMphB2VOS653kwCFMf8tDwROG4mrJUfVoEx0xn__K1KSxK5dhg.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=ClsZd83GOhoQ7kNvwEMWdVR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTcwOTE5NDM1MDA4MDc4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo3NTYxMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0pv893T3x0hleSJcPlEZCkFHk3lYUawOnbIkG9P3UqPg&amp;oe=69DC3EA6</BaseURL><SegmentBase indexRange=\"838-1013\" timescale=\"44100\" FBMinimumPrefetchRange=\"1014-2802\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-24789\" FBFirstSegmentRange=\"1014-45840\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"45841-91498\" FBPrefetchSegmentRange=\"1014-45840\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1441897587392390a\" bandwidth=\"125019\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"125019\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"870071\" FBPaqMos=\"93.66\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMpbV_ghzNyycyti6VXubpSZRxVYdVuZ8_mYOLIxOMVPIf--uAXbhefrBVS2OXmupcQnb74jdqpgQsh6WyojdBkHFUzhHYsONQaW80.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=xRI-7M7j2mYQ7kNvwF8yS0y&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTcwOTE5NDM1MDA4MDc4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMjUxNjMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3FvA27mT6h8QDjWbJHS3th-W2iUo3WmCAh9ah2DAINVQ&amp;oe=69DC58F9</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"44100\" FBMinimumPrefetchRange=\"1009-2652\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-40150\" FBFirstSegmentRange=\"1009-76752\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"76753-151527\" FBPrefetchSegmentRange=\"1009-76752\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2182577039146008a\" bandwidth=\"148638\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"148638\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1034261\" FBPaqMos=\"94.26\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMLOQUTAn_i7Voz4E9LO9j37cPBVdIWiclc3O4ViojxZcz0fwUoTLpDyE5UJUhmOcu8dsx2yy-Zksx0DuCFTpQl5w2j_xBUMQZtuxY.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=w0kA03mrfZ0Q7kNvwEO0xWc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTcwOTE5NDM1MDA4MDc4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxNDg3ODIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1TI1CvtE54SeA2wndqomXcWgqvvFZewBVl4xW5KgypaQ&amp;oe=69DC55E5</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"44100\" FBMinimumPrefetchRange=\"1009-2786\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-47036\" FBFirstSegmentRange=\"1009-90462\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"90463-179192\" FBPrefetchSegmentRange=\"1009-90462\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": true,
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
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&oh=00_Af2Ompn0G_cOK1kA_Y27DXww2XQtywMZNXDsuLrzfzxwzw&oe=69DC5703",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFCiFN1FZ8hp_sMdWmp4Wfy7m0NWS41YJKLyHQbjhkVO_MBfRPF0igm5-FZ-MueEKc&_nc_ohc=8UGwMTx74pgQ7kNvwHA5dwc&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af0le0_o4Bu_GPt61vUJ3H6TD45S6FM1-FbsQUQuBhxeJg&oe=69DC3771&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 387,
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
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&oh=00_Af2Ompn0G_cOK1kA_Y27DXww2XQtywMZNXDsuLrzfzxwzw&oe=69DC5703",
          "width": 1079,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            7924,
            15848,
            23772
          ],
          "height": 765,
          "scans_profile": "e35",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwGYkKrg&_nc_oc=AdrkH_FzoEKbh4ouEkyDG44hlIkbfIHM7MKCC6HEkbWSKXFydM9YoSi9M7Ah4xOBE-g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&oh=00_Af2fJ801ZGLUXF9aY9jAh15NX0x9OuGLZ_23-WIbIhy-Jg&oe=69DC5703",
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
      "pk": "3870776608970227594",
      "id": "3870776608970227594_18341434899",
      "code": "DW3wtFOj7-K",
      "taken_at": "2026-04-08T12:50:46Z",
      "taken_at_ts": 1775652646,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/658109836_2375813856176533_5833914654334600173_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ig_cache_key=Mzg3MDc3NjYwODk3MDIyNzU5NA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=S_cYc4kRUlcQ7kNvwHDCL7U&_nc_oc=Ado5ncV7YSWxoqKqu3j_fYocCvvJObqb7k9JKfBN-DXMRKB89XLrNAevIsiR_IIYVOo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&oh=00_Af2TpOjTg9NjlCRHrFbHekZtQU_MqVlpzo2reN0suotRHw&oe=69DC60D7",
      "location": {
        "pk": 273440226,
        "name": "Sharanabasaveshwar Temple, Gulbarga",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 76.827037921106,
        "lat": 17.336312129141,
        "external_id": "217341185047137",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "18341434899",
        "id": "18341434899",
        "username": "smiley.wali",
        "full_name": "Smiley Wali",
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/543663143_18101059678610900_4044512800673539198_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFCiFN1FZ8hp_sMdWmp4Wfy7m0NWS41YJKLyHQbjhkVO_MBfRPF0igm5-FZ-MueEKc&_nc_ohc=_Ze9uytoGdQQ7kNvwG-RrCv&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCekZyDUpTNg0U5AAH6kqqX2-iA4bmNDAQAB1501500j-ccb7-5&oh=00_Af0-_e2F_1qdqhoBzVmq6ccLWlZB4Kczto6EESXJBWhhxw&oe=69DC5994&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 12,
      "comments_disabled": false,
      "like_count": 1247,
      "play_count": 19339,
      "has_liked": false,
      "caption_text": "wait for end❤️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#kannada #kalaburagi #karnataka #love #kannadasongs",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQNY_d6EzPWJ-yAhwuEbOmDXQoq0_LJx36xeKyE2q-jfDJ45uMNLdEF5Kcsx5Lj40VhGFfRwqiTbyTMmRLf-oxj9VFxp-pZgZxEpJK0.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZC-B8_N0K0kQ7kNvwHyVqQX&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4ODMzNjM4MDc0ODM2MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=ebe17e4ca3244505&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wODREMENFMjg3MjJEQzdDOUM2MzFBMzU3ODBEMTI5Ql92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzUwNDAzNDUzNUVCQkU3OEQxNzI0MUE1MDI4NUMxMkJFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbm25Ky47TEPxUCKAJDMywXQFKu6XjU_fQYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1rc2XSMvUQFn_DvOEgLeNWvscX8LiqFH1VBq5PFLQ_mg&oe=69D8759D",
      "view_count": 0,
      "video_duration": 74.73300170898438,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            9583,
            19166,
            28750
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/658109836_2375813856176533_5833914654334600173_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ig_cache_key=Mzg3MDc3NjYwODk3MDIyNzU5NA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=S_cYc4kRUlcQ7kNvwHDCL7U&_nc_oc=Ado5ncV7YSWxoqKqu3j_fYocCvvJObqb7k9JKfBN-DXMRKB89XLrNAevIsiR_IIYVOo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&oh=00_Af2TpOjTg9NjlCRHrFbHekZtQU_MqVlpzo2reN0suotRHw&oe=69DC60D7",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 3119298,
          "height": 1280,
          "id": "927191233418830v",
          "type": 101,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQNY_d6EzPWJ-yAhwuEbOmDXQoq0_LJx36xeKyE2q-jfDJ45uMNLdEF5Kcsx5Lj40VhGFfRwqiTbyTMmRLf-oxj9VFxp-pZgZxEpJK0.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZC-B8_N0K0kQ7kNvwHyVqQX&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4ODMzNjM4MDc0ODM2MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=ebe17e4ca3244505&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wODREMENFMjg3MjJEQzdDOUM2MzFBMzU3ODBEMTI5Ql92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzUwNDAzNDUzNUVCQkU3OEQxNzI0MUE1MDI4NUMxMkJFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbm25Ky47TEPxUCKAJDMywXQFKu6XjU_fQYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1rc2XSMvUQFn_DvOEgLeNWvscX8LiqFH1VBq5PFLQ_mg&oe=69D8759D",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 3119298,
          "height": 1280,
          "id": "927191233418830v",
          "type": 102,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQNY_d6EzPWJ-yAhwuEbOmDXQoq0_LJx36xeKyE2q-jfDJ45uMNLdEF5Kcsx5Lj40VhGFfRwqiTbyTMmRLf-oxj9VFxp-pZgZxEpJK0.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZC-B8_N0K0kQ7kNvwHyVqQX&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4ODMzNjM4MDc0ODM2MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=ebe17e4ca3244505&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wODREMENFMjg3MjJEQzdDOUM2MzFBMzU3ODBEMTI5Ql92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzUwNDAzNDUzNUVCQkU3OEQxNzI0MUE1MDI4NUMxMkJFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbm25Ky47TEPxUCKAJDMywXQFKu6XjU_fQYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1rc2XSMvUQFn_DvOEgLeNWvscX8LiqFH1VBq5PFLQ_mg&oe=69D8759D",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 3119298,
          "height": 1280,
          "id": "927191233418830v",
          "type": 103,
          "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQNY_d6EzPWJ-yAhwuEbOmDXQoq0_LJx36xeKyE2q-jfDJ45uMNLdEF5Kcsx5Lj40VhGFfRwqiTbyTMmRLf-oxj9VFxp-pZgZxEpJK0.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZC-B8_N0K0kQ7kNvwHyVqQX&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4ODMzNjM4MDc0ODM2MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=ebe17e4ca3244505&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wODREMENFMjg3MjJEQzdDOUM2MzFBMzU3ODBEMTI5Ql92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzUwNDAzNDUzNUVCQkU3OEQxNzI0MUE1MDI4NUMxMkJFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbm25Ky47TEPxUCKAJDMywXQFKu6XjU_fQYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1rc2XSMvUQFn_DvOEgLeNWvscX8LiqFH1VBq5PFLQ_mg&oe=69D8759D",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "clips_metadata": {
        "clips_creation_entry_point": "clips",
        "featured_label": null,
        "is_public_chat_welcome_video": false,
        "professional_clips_upsell_type": 0,
        "show_tips": null,
        "achievements_info": {
          "num_earned_achievements": null,
          "show_achievements": false
        },
        "additional_audio_info": {
          "additional_audio_username": null,
          "audio_reattribution_info": {
            "should_allow_restore": false
          }
        },
        "asset_recommendation_info": null,
        "audio_ranking_info": {
          "best_audio_cluster_id": "1217849043515274"
        },
        "audio_type": "original_sounds",
        "basel_template_info_for_ig_app": {
          "is_basel_template": null,
          "should_show_reuse_setting_for_owner": false,
          "use_template_deeplink": null
        },
        "branded_content_tag_info": {
          "can_add_tag": false
        },
        "breaking_content_info": null,
        "breaking_creator_info": null,
        "challenge_info": null,
        "content_appreciation_info": null,
        "contextual_highlight_info": null,
        "cutout_sticker_info": [],
        "disable_use_in_clips_client_cache": false,
        "external_media_info": null,
        "is_fan_club_promo_video": false,
        "is_shared_to_fb": false,
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": false,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": false,
          "is_pivot_page_available": false,
          "is_reuse_allowed": true,
          "mashup_type": null,
          "mashups_allowed": true,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18586793140010893",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26700572086226468,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": false,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT74.721817S\" FBManifestTimestamp=\"1775664059\" FBManifestIdentifier=\"Fvbus50NKRb2oumg2IaaBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT74.721817S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1746139389700283a\" bandwidth=\"61212\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"61212\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m78/AQOQlLX8CLUQawoJ_jEKE_dR2sass79npzxeX67_NV_CGnx2fKdYp8JXvkPLtDK9dqzRunRQHLhvS8SdCTtMY76XtRWWBukclDngjzE.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=Sb2kvRw5I20Q7kNvwG2dZ1U&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3ODgzMzYzODA3NDgzNjM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc0LCJiaXRyYXRlIjo2MTM1MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3n4hs8T4ioB38-7luM05-Di1XY0CCdngOuD3rj8Cyfdw&amp;oe=69D85548</BaseURL><SegmentBase indexRange=\"824-1311\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 74000,
          "formatted_clips_media_count": null,
          "hide_remixing": false,
          "is_audio_automatically_attributed": false,
          "is_eligible_for_audio_effects": true,
          "is_eligible_for_vinyl_sticker": true,
          "is_explicit": false,
          "is_original_audio_download_eligible": true,
          "is_reuse_disabled": false,
          "is_xpost_from_fb": false,
          "music_canonical_id": null,
          "oa_owner_is_music_artist": false,
          "original_audio_subtype": "default",
          "original_audio_title": "Original audio",
          "original_media_id": 3870776608970227594,
          "progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m69/AQMNcygDtUfnO0lt44C24RQXF6CQ4J0bt_uSHIuMXLxhLG3do9eccOTjvlMFmuBHEmejqZf01lMbJgHGPJVOp7TB.mp4?strext=1&_nc_cat=100&_nc_sid=8bf8fe&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=AaEpmW477yYQ7kNvwH6j4U9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc4ODMzNjM4MDc0ODM2MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0XBHlHOFWtcFY24Bt8OWZk9nMAgSH-IdDjv6rl28Yd-w&oe=69DC36BA",
          "should_mute_audio": false,
          "time_created": 1775652596,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "18341434899",
            "pk": 18341434899,
            "pk_id": "18341434899",
            "id": "18341434899",
            "username": "smiley.wali",
            "full_name": "Smiley Wali",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3718022023135545974_18341434899",
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/543663143_18101059678610900_4044512800673539198_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFCiFN1FZ8hp_sMdWmp4Wfy7m0NWS41YJKLyHQbjhkVO_MBfRPF0igm5-FZ-MueEKc&_nc_ohc=_Ze9uytoGdQQ7kNvwG-RrCv&_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCekZyDUpTNg0U5AAH6kqqX2-iA4bmNDAQAB1501500j-ccb7-5&oh=00_Af0-_e2F_1qdqhoBzVmq6ccLWlZB4Kczto6EESXJBWhhxw&oe=69DC5994&_nc_sid=472314"
          },
          "audio_filter_infos": null,
          "audio_parts": [],
          "audio_parts_by_filter": [],
          "consumption_info": {
            "display_media_id": null,
            "is_bookmarked": false,
            "is_trending_in_clips": false,
            "should_mute_audio_reason": "",
            "should_mute_audio_reason_type": null,
            "inline_audio_label": null,
            "display_labels": null,
            "user_notes": null
          },
          "xpost_fb_creator_info": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "originality_info": null,
        "reels_on_the_rise_info": null,
        "reusable_text_attribute_string": null,
        "reusable_text_info": null,
        "shopping_info": null,
        "show_achievements": false,
        "template_info": null,
        "may_have_template_info": null,
        "viewer_interaction_settings": null
      },
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT74.73333S\" FBManifestTimestamp=\"1775664059\" FBManifestIdentifier=\"Fvbus50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxobi8MGDmpcD7rCLhMvhsQPOxYGRjNe0A7qi5cOZocAD1NHd5YjW2QPq3qLC34PABL7sgK/Pr7UFko2BybP2sQfM8/bOhr66CM6ZuK3G4dsJ6LTnzb6Bzg/U8oOd4pWBXSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT74.73333S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:87.7\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"960270416490855v\" bandwidth=\"860950\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"8042715\" FBPlaybackResolutionMos=\"0:100,360:53,480:44.1,720:35.3,1080:31.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:93,720:86.8,1080:77.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPp2hf0rSwL2LXksF27ssMsiOILIheYuryvIG4MnUtlYigK1d1YnadziJhvtFq32Aqj_yFxdr2F-7opZl1bk73kw7ioLsVEiSCPxKM.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=sjExrz8CXzsQ7kNvwErf8rf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6ODYwOTUwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2xz4vyCxVsfIhqansAUDbYtYzMExi4MTCFRzX8RyVASg&amp;oe=69DC6692</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-21212\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-309255\" FBFirstSegmentRange=\"1038-534465\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"534466-1156214\" FBPrefetchSegmentRange=\"1038-534465\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"953853587582007v\" bandwidth=\"1193304\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"11147450\" FBPlaybackResolutionMos=\"0:100,360:61.6,480:53.5,720:43.4,1080:36.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.5,720:91.9,1080:83.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNGYdkCa51YGXcjjQUhMnjo7oQApSvjxDWw3qFMF9dOFt2-N1F1_7JXMeT3DS-S0CYNySNqb_2fv6QgHGt2xsE3az-BybN5JINcYik.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=Ytuuh7_KSkIQ7kNvwHwVYMQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6MTE5MzMwNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0U_PuP2OBfM7OYAdODeCOsu8TlXStlUqFTBOepuOigmg&amp;oe=69DC49C4</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-27249\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-437888\" FBFirstSegmentRange=\"1038-755976\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"755977-1624163\" FBPrefetchSegmentRange=\"1038-755976\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"26179745818377386v\" bandwidth=\"1509578\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"14101982\" FBPlaybackResolutionMos=\"0:100,360:67,480:59,720:49.2,1080:41.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.85,480:98.04,720:95.1,1080:88\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMfpyoo2PRVNrwFI0C9GIuF1c0kndQloC44-zTu_tX6PuCgk3seaod4FAfXlD07JXXtGqKrOI5ob9_wpgePYHDsh1wXZbBB0FHA37w.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=l_9lr4qvj4wQ7kNvwHnsA03&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6MTUwOTU3OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af01GSC_t3_D_2SmRWg9qw8IWsktkE-fuxfvxu_7JyqxJA&amp;oe=69DC41CC</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-32398\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-564059\" FBFirstSegmentRange=\"1038-981630\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"981631-2083277\" FBPrefetchSegmentRange=\"1038-981630\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"985732780697757v\" bandwidth=\"1864010\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"17412965\" FBPlaybackResolutionMos=\"0:100,360:71.1,480:63.7,720:54,1080:45\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.154,480:98.83,720:97.3,1080:91.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN5g4QCsUUPTmQwsBPM2xmDH14IJ6jDBlCuRjAj0T3zGWJ29AjXirZwd7INCeVuYId_klEvxbDKOawQnD-DB0-ukeI9M9gZeWlHpts.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=lwGP1pP15b8Q7kNvwFB0Wv-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6MTg2NDAxMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3fDeS-1b9SlIMnJLAzrgMQ6MSxnHgiiiKV0VNQs6k0Sw&amp;oe=69DC62DE</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-38175\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-712699\" FBFirstSegmentRange=\"1038-1243767\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1243768-2624757\" FBPrefetchSegmentRange=\"1038-1243767\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2080111122719561v\" bandwidth=\"2367988\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"22120956\" FBPlaybackResolutionMos=\"0:100,360:74.7,480:67.9,720:58.1,1080:49.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.388,480:99.172,720:98.4,1080:94.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMI1yRFnNm07wpSqtMEWXPYHn6DFn7H09osSqSUEKsyZpbTC8tCzjfnHLHTXNxmAwiFjzMCA2ITzS-AQIM6rLPT3bHCSCvImOUq65A.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=ZmnGISiIpf8Q7kNvwHyGfZC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6MjM2Nzk4OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0YXQeHK206zmjm7AmNxqM0_Ge8eU3UH_kA-iqo3xauIA&amp;oe=69DC4BE1</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-45296\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-907970\" FBFirstSegmentRange=\"1038-1606941\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1606942-3377780\" FBPrefetchSegmentRange=\"1038-1606941\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"895449613342851v\" bandwidth=\"2832310\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"26458500\" FBPlaybackResolutionMos=\"0:100,360:76.9,480:70.6,720:61.3,1080:51.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.509,480:99.395,720:98.88,1080:96.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPs1subFzVt1YpLOEhZAVR3CVPz5ANtkDFdBLAitMPPT2CvXEzJLYgBroI6lDF9EENHw2eVyu3zuImFWlh1ryCZehEHKLVXVd44Yvk.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=fawr-8RXAxsQ7kNvwHgldg_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6MjgzMjMxMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3poG-BplwEr2v4qSp9Mor4NIgWThB_f12zA5rQ_WvrRA&amp;oe=69DC3645</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-52306\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-1088994\" FBFirstSegmentRange=\"1038-1933712\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1933713-4058484\" FBPrefetchSegmentRange=\"1038-1933712\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2735061796849255v\" bandwidth=\"3664218\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"34229904\" FBPlaybackResolutionMos=\"0:100,360:80.4,480:74.1,720:65.4,1080:55.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.6,480:99.554,720:99.299,1080:98\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPUYtQ68Rt0LIjfWHAI1HdHBya3lfL9jkwmDytsaojG-zr3TRc660oLKkYm1WnJdPLlq58_g8BnRpwDFoPZKsA24muR0urloqEA5JQ.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=TkyFnJqPB3oQ7kNvwEqaGS-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6MzY2NDIxOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af08Olj-7VLDGpBFrFkoS8vmTA_WrKD1SRGk7hE--8ajLg&amp;oe=69DC4967</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-62397\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-1403225\" FBFirstSegmentRange=\"1038-2522951\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"2522952-5289754\" FBPrefetchSegmentRange=\"1038-2522951\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1041616649041002v\" bandwidth=\"5649790\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"52778457\" FBPlaybackResolutionMos=\"0:100,360:85.8,480:80,720:72.9,1080:67.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.702,480:99.679,720:99.62,1080:99.542\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOWAJiKWGeX5EajaIAFK_LmWhpMlGZLTPVbBODv934k54pSypm4cIsyiUmkcszJ8eRRK0T8IiMzEZwuP9P2pbnQA2mciFo9FeRTZ48.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=4Oa_ew4meVMQ7kNvwGqXjOY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg4MzM2MzgwNzQ4MzYzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NCwiYml0cmF0ZSI6NTY0OTc5MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ERz-BVQ3aI3ZNXgd9nzZqrCs0OJC6gWhk5YuGorzbVA&amp;oe=69DC347B</BaseURL><SegmentBase indexRange=\"826-1037\" timescale=\"15360\" FBMinimumPrefetchRange=\"1038-91656\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-2293564\" FBFirstSegmentRange=\"1038-3945375\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"3945376-8138662\" FBPrefetchSegmentRange=\"1038-3945375\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2380409202466022a\" bandwidth=\"44394\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"44394\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"415694\" FBPaqMos=\"86.78\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPTf3thDYpd08JN3g1S2nr0-V3w04Nm867xzh1DmK5uJaRPs1xDlMs79Rrgyf3MEhSmZxaDZWv5Y4ikXMe-Zh95VmotulJ2dMglf_g.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=-W_U2gbMfrkQ7kNvwGCCywz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODgzMzYzODA3NDgzNjM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc0LCJiaXRyYXRlIjo0NDUwNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1_PkKRYYnIzq2hJB1XSKGZuxJQdSgv61eJ5suKXu1kqg&amp;oe=69DC3669</BaseURL><SegmentBase indexRange=\"837-1060\" timescale=\"44100\" FBMinimumPrefetchRange=\"1061-2277\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1061-14188\" FBFirstSegmentRange=\"1061-26758\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"26759-54028\" FBPrefetchSegmentRange=\"1061-26758\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"4393674047548724a\" bandwidth=\"80618\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"80618\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"754033\" FBPaqMos=\"88.72\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMs7BKPRYhE5zb196W9IDu0j-UHplBvvQlzVTybwlZu6rPv69B7icbIyxYmmC6Hon86avzZwbtqS1rDhNxm2FULLiASKue8A6kbc-Q.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=rhbywHlnFTsQ7kNvwHXdNHY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODgzMzYzODA3NDgzNjM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc0LCJiaXRyYXRlIjo4MDczMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Hy_7sOB1nMIJrkmn8gyfiyVJ9r2umDDa1oLJ_OJAUjw&amp;oe=69DC3BE3</BaseURL><SegmentBase indexRange=\"838-1061\" timescale=\"44100\" FBMinimumPrefetchRange=\"1062-2900\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1062-28954\" FBFirstSegmentRange=\"1062-51034\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"51035-101389\" FBPrefetchSegmentRange=\"1062-51034\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1524741222439711a\" bandwidth=\"115753\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"115753\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"1082190\" FBPaqMos=\"93.70\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNTkv_CluhmkfkQ-Ccl2fVuUxZ0z6ZUjPi8SXt3TzKwtX_nrelrphcSCSzxEaLkVDUVUsyJReQ1mHaLZAtDjbwpPYipnLHnv_wVaRM.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=k9ONvEqK4uoQ7kNvwGQGKzj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODgzMzYzODA3NDgzNjM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc0LCJiaXRyYXRlIjoxMTU4NjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0G9yPwjIiqib5pQTlPGNYxQwA9NtDTma-po5Ufo9ZBaw&amp;oe=69DC665F</BaseURL><SegmentBase indexRange=\"833-1056\" timescale=\"44100\" FBMinimumPrefetchRange=\"1057-2636\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1057-39030\" FBFirstSegmentRange=\"1057-70881\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"70882-143697\" FBPrefetchSegmentRange=\"1057-70881\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1266701754980277a\" bandwidth=\"144851\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"144851\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1353969\" FBPaqMos=\"92.70\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOuOav-eRu8ihVSWW7Sot5idO2mHg52kmkf967y5e15KLDeHFv5FhIJvRBvsV7RxclP0VHY_YLBywS0SQMQMmewHMw_ZBF3S6-75Nc.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=Eo8Wq6QHIB8Q7kNvwG7p4n_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODgzMzYzODA3NDgzNjM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc0LCJiaXRyYXRlIjoxNDQ5NjMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0Hkstho2J6Zsx-KkAX6kgA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1kin_7VFCIhHqxU6dqaLxeiSvgygqJMxMFjnHvm5rf1w&amp;oe=69DC6371</BaseURL><SegmentBase indexRange=\"833-1056\" timescale=\"44100\" FBMinimumPrefetchRange=\"1057-2765\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1057-45719\" FBFirstSegmentRange=\"1057-86955\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"86956-175195\" FBPrefetchSegmentRange=\"1057-86955\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WyI5NTI1MGEwNDNiYTM0M2U2YjAxMTlkMThkOWMzZWM5OSIsW10sMV0="
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-hashtags){ target=_blank }
