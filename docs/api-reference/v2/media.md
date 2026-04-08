# Media Endpoints

Get posts, comments, and media details.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/media/by/code`](#get-v2mediabycode) | [`/v2/media/by/id`](#get-v2mediabyid) | [`/v2/media/by/url`](#get-v2mediabyurl) | [`/v2/media/comment/offensive`](#get-v2mediacommentoffensive) | [`/v2/media/comments`](#get-v2mediacomments) | [`/v2/media/comments/replies`](#get-v2mediacommentsreplies) | [`/v2/media/info/by/code`](#get-v2mediainfobycode) | [`/v2/media/info/by/id`](#get-v2mediainfobyid) | [`/v2/media/info/by/url`](#get-v2mediainfobyurl) | [`/v2/media/likers`](#get-v2medialikers) | [`/v2/media/template`](#get-v2mediatemplate)

---

### GET /v2/media/by/code

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/by/code?code=DRqAYKuAIUx"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/by/code",
        headers=headers,
        params={"code": "DRqAYKuAIUx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/by/code?code=DRqAYKuAIUx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "num_results": 1,
  "more_available": false,
  "items": [
    {
      "strong_id__": "3776832898280228145_787132",
      "id": "3776832898280228145_787132",
      "disable_caption_and_comment": false,
      "fbid": 18065011277571522,
      "deleted_reason": 0,
      "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
      "integrity_review_decision": "pending",
      "pk": 3776832898280228145,
      "is_affiliate_commission_eligible": false,
      "has_delayed_metadata": false,
      "mezql_token": "",
      "should_request_ads": false,
      "has_privately_liked": false,
      "is_quiet_post": false,
      "collaborator_edit_eligibility": false,
      "share_count_disabled": false,
      "is_reshare_of_text_post_app_media_in_ig": false,
      "is_visual_reply_commenter_notice_enabled": true,
      "translated_langs_for_autodub": [],
      "subtype_name_for_REST__": "XDTClipsMedia",
      "is_third_party_downloads_eligible": false,
      "image_versions2": {
        "additional_candidates": {
          "first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHY0qE3&_nc_oc=AdpmHU2Fex92cDbFW-MvLSm4ow6OBxHK6osq4-PXhfAWo_WbmmbdNKyl5ggZV8FCscQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&_nc_ss=7a3ba&oh=00_Af1TKEbHu8eHpae3vNfc3Vn5k8k_-OY7GyyqdX1N_cl-eQ&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "igtv_first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHY0qE3&_nc_oc=AdpmHU2Fex92cDbFW-MvLSm4ow6OBxHK6osq4-PXhfAWo_WbmmbdNKyl5ggZV8FCscQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&_nc_ss=7a3ba&oh=00_Af1TKEbHu8eHpae3vNfc3Vn5k8k_-OY7GyyqdX1N_cl-eQ&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "smart_frame": null
        },
        "candidates": [
          {
            "estimated_scans_sizes": [
              27870,
              55740
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwEJnm24&_nc_oc=AdrAfeL0RSi9kzWPL7Dzxr_HBSLGXZoePc6hukNO2sfKL6hIzN3WL7WAPxbkeSiYL7o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&_nc_ss=7a3ba&oh=00_Af2Tja24jaLCHge2O6Rp10T6OPurZr2WoIKKNcQ4_Kj56Q&oe=69DC3E7E",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "scrubber_spritesheet_info_candidates": {
          "default": {
            "file_size_kb": 428,
            "max_thumbnails_per_sprite": 105,
            "rendered_width": 96,
            "sprite_height": 1232,
            "sprite_urls": [
              "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEss1iWvtD6oG30x9rqUuzwTKD0PaRY50-vvupOCfuuy6_TyKHxJZXKI-USEqL6XV4&_nc_ohc=7fRK9vLZo4UQ7kNvwFNTKX9&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&edm=ALQROFkBAAAA&ccb=7-5&oh=00_Af0LHJxsJdqY5RciVWy1d4kOwme0cYbwKe1hQYWo7x1e_g&oe=69DC4C8A&_nc_sid=fc8dfb"
            ],
            "sprite_width": 1500,
            "thumbnail_duration": 0.2125047619047619,
            "thumbnail_height": 176,
            "thumbnail_width": 100,
            "thumbnails_per_row": 15,
            "total_thumbnail_num_per_sprite": 105,
  // ... truncated
```

</details>

---

### GET /v2/media/by/id

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/by/id?id=3776832898280228145"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/by/id",
        headers=headers,
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/by/id?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "num_results": 1,
  "more_available": false,
  "items": [
    {
      "strong_id__": "3776832898280228145_787132",
      "id": "3776832898280228145_787132",
      "disable_caption_and_comment": false,
      "fbid": 18065011277571522,
      "deleted_reason": 0,
      "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
      "integrity_review_decision": "pending",
      "pk": 3776832898280228145,
      "is_affiliate_commission_eligible": false,
      "has_delayed_metadata": false,
      "mezql_token": "",
      "should_request_ads": false,
      "has_privately_liked": false,
      "is_quiet_post": false,
      "collaborator_edit_eligibility": false,
      "share_count_disabled": false,
      "is_reshare_of_text_post_app_media_in_ig": false,
      "is_visual_reply_commenter_notice_enabled": true,
      "translated_langs_for_autodub": [],
      "subtype_name_for_REST__": "XDTClipsMedia",
      "is_third_party_downloads_eligible": false,
      "image_versions2": {
        "additional_candidates": {
          "first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGCKyDT&_nc_oc=AdoiydDDBQeibFzDkHcaY8GYj6hFy0jJVcx0XCpd2QYWWnqiR0Pj1mRkk4usIjLkjao&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&_nc_ss=7a3ba&oh=00_Af3Q3i2PG3Yx-AU5rr7-EPEecNvtxfYxI4zXTjs2z_VqCg&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "igtv_first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGCKyDT&_nc_oc=AdoiydDDBQeibFzDkHcaY8GYj6hFy0jJVcx0XCpd2QYWWnqiR0Pj1mRkk4usIjLkjao&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&_nc_ss=7a3ba&oh=00_Af3Q3i2PG3Yx-AU5rr7-EPEecNvtxfYxI4zXTjs2z_VqCg&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "smart_frame": null
        },
        "candidates": [
          {
            "estimated_scans_sizes": [
              27870,
              55740
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwH9Zez4&_nc_oc=AdoEM1egpfA4PIyEhvRFaM8a8D2y-RJ0i_ltnGIu6mCwgDIPRoCcP7V5CNLUmFX5bKQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&_nc_ss=7a3ba&oh=00_Af34ic4--ZKkM_6yhEUO2sp7Y-fc24c9O7cmN87QXRJpfQ&oe=69DC3E7E",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "scrubber_spritesheet_info_candidates": {
          "default": {
            "file_size_kb": 428,
            "max_thumbnails_per_sprite": 105,
            "rendered_width": 96,
            "sprite_height": 1232,
            "sprite_urls": [
              "https://scontent-lax3-2.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFm15zcVP-xSPB8Mugx4KR49byI8iGahbzl7dN1_Hrmfqxg1F3KeOwwfZx1Dd2SQYU&_nc_ohc=7fRK9vLZo4UQ7kNvwFW3za1&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&edm=ALQROFkBAAAA&ccb=7-5&oh=00_Af2eS39d4JZq6C_h4eOVzm1y6dCgv-hPBlB1u8gQUZg8Bw&oe=69DC4C8A&_nc_sid=fc8dfb"
            ],
            "sprite_width": 1500,
            "thumbnail_duration": 0.2125047619047619,
            "thumbnail_height": 176,
            "thumbnail_width": 100,
            "thumbnails_per_row": 15,
            "total_thumbnail_num_per_sprite": 105,
  // ... truncated
```

</details>

---

### GET /v2/media/by/url

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/by/url",
        headers=headers,
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "num_results": 1,
  "more_available": false,
  "items": [
    {
      "strong_id__": "3776832898280228145_787132",
      "id": "3776832898280228145_787132",
      "disable_caption_and_comment": false,
      "fbid": 18065011277571522,
      "deleted_reason": 0,
      "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
      "integrity_review_decision": "pending",
      "pk": 3776832898280228145,
      "is_affiliate_commission_eligible": false,
      "has_delayed_metadata": false,
      "mezql_token": "",
      "should_request_ads": false,
      "has_privately_liked": false,
      "is_quiet_post": false,
      "collaborator_edit_eligibility": false,
      "share_count_disabled": false,
      "is_reshare_of_text_post_app_media_in_ig": false,
      "is_visual_reply_commenter_notice_enabled": true,
      "translated_langs_for_autodub": [],
      "subtype_name_for_REST__": "XDTClipsMedia",
      "is_third_party_downloads_eligible": false,
      "image_versions2": {
        "additional_candidates": {
          "first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGtK5Kf&_nc_oc=Adq_97v6_JEB04bUmhWA9x4vdrvUhPD2YiT4vjxQl02x5XR0pG7Zl3-nzDMKP0b7z9A&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&_nc_ss=7a3ba&oh=00_Af024Y3XLKtKxwbGoDTCLKruFzD9DyC3qt2QDQspQxuAYw&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "igtv_first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGtK5Kf&_nc_oc=Adq_97v6_JEB04bUmhWA9x4vdrvUhPD2YiT4vjxQl02x5XR0pG7Zl3-nzDMKP0b7z9A&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&_nc_ss=7a3ba&oh=00_Af024Y3XLKtKxwbGoDTCLKruFzD9DyC3qt2QDQspQxuAYw&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "smart_frame": null
        },
        "candidates": [
          {
            "estimated_scans_sizes": [
              27870,
              55740
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwE9PLiG&_nc_oc=AdrOX_-jaQ4Rgi4c4yIOmPMb5Wo9SeNB2YZVGs9JY_Zll-Rzfufvvz35j0UfftfWf58&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&_nc_ss=7a3ba&oh=00_Af3GVmZt213sJS5j3of7Ah_b2qcWviX-nYJ92U-6lUfmiw&oe=69DC3E7E",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "scrubber_spritesheet_info_candidates": {
          "default": {
            "file_size_kb": 428,
            "max_thumbnails_per_sprite": 105,
            "rendered_width": 96,
            "sprite_height": 1232,
            "sprite_urls": [
              "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGSog-HAZ_2AlSTH8bSkHUlle044gAHMO5eH8qqfGkfUOKv8eYOx3BFqn1BR0YfTh8&_nc_ohc=7fRK9vLZo4UQ7kNvwE-DJ2g&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&edm=ALQROFkBAAAA&ccb=7-5&oh=00_Af1fG9hnC0nCVCIpm-vU8zFDmj-qyJV8_54ja_Br2eD8Yg&oe=69DC4C8A&_nc_sid=fc8dfb"
            ],
            "sprite_width": 1500,
            "thumbnail_duration": 0.2125047619047619,
            "thumbnail_height": 176,
            "thumbnail_width": 100,
            "thumbnails_per_row": 15,
            "total_thumbnail_num_per_sprite": 105,
  // ... truncated
```

</details>

---

### GET /v2/media/comment/offensive

Whether to receive an offensive comment

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `comment` | string | Yes | Comment |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/comment/offensive?media_id=3776832898280228145&comment=test comment"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comment_offensive_v2(media_id="3776832898280228145", comment="test comment")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/comment/offensive",
        headers=headers,
        params={"media_id": "3776832898280228145", "comment": "test comment"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comment/offensive?media_id=3776832898280228145&comment=test comment",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "is_offensive": false,
    "text_language": null,
    "status": "ok"
  },
  "next_page_id": null
}
```

</details>

---

### GET /v2/media/comments

Get comments on a media. Returns a list of Comment objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `can_support_threading` | boolean | No | Can Support Threading |
| `page_id` | string | No | Page Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/comments?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_v2(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/comments",
        headers=headers,
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comments?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "can_view_more_preview_comments": false,
    "caption": {
      "bit_flags": 0,
      "content_type": "comment",
      "created_at": 1764453632,
      "created_at_for_fb_app": 1764453632,
      "created_at_utc": 1764453632,
      "did_report_as_spam": false,
      "is_covered": false,
      "is_created_by_media_owner": true,
      "is_ranked_comment": true,
      "media_id": 3776832898280228145,
      "pk": "18065011298571522",
      "private_reply_status": 0,
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "18065011298571522",
      "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
      "type": 1,
      "user": {
        "fbid_v2": 17841400573960012,
        "full_name": "National Geographic",
        "id": "787132",
        "is_private": false,
        "is_unpublished": false,
        "is_verified": true,
        "pk": 787132,
        "pk_id": "787132",
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=1&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwFMP5te&_nc_oc=AdpMx482XQO0TUJc8VUDGyIrHyOA4nnvGPDVxUyvVFFnjfPZ1N68DhhmjzFIASTfLC0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=lEjzIWFJ73NaMueeKGtW8w&_nc_ss=7a3ba&oh=00_Af3zS8Li3LIEBIsonpFMer9CIHsXXCPVdO3CYup_0AjUHA&oe=69DC51E9",
        "strong_id__": "787132",
        "username": "natgeo"
      },
      "user_id": 787132
    },
    "caption_is_edited": false,
    "comment_count": 485,
    "comment_cover_pos": "bottom",
    "comment_filter_param": "no_filter",
    "comment_likes_enabled": true,
    "comments": [
      {
        "bit_flags": 0,
        "comment_like_count": 66,
        "content_type": "comment",
        "created_at": 1764455782,
        "created_at_for_fb_app": 1764455782,
        "created_at_utc": 1764455782,
        "did_report_as_spam": false,
        "has_liked_comment": false,
        "has_disliked_comment": false,
        "inline_composer_display_condition": "never",
        "is_covered": false,
        "is_photo_comments_enabled_for_comment_author": false,
        "is_text_editable": false,
        "is_edited": false,
        "meta_ai_comment_type": "NONE",
        "is_ranked_comment": true,
        "keywords_data": [],
        "liked_by_media_coauthors": [],
        "other_preview_users": [],
        "media_id": 3776832898280228145,
        "pk": "17915190762228930",
        "preview_child_comments": [],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "17915190762228930",
        "text": "Nature is brilliantly beautiful!🤩",
        "type": 0,
        "user": {
          "fbid_v2": 17841401684251765,
          "full_name": "Karen",
          "id": "1393016141",
          "is_mentionable": true,
          "is_private": true,
          "is_verified": false,
          "pk": "1393016141",
  // ... truncated
```

</details>

---

### GET /v2/media/comments/replies

Get media comment replies with pagination by min_id. Returns a list of Comment objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `comment_id` | string | Yes | Comment Id |
| `min_id` | string | No | Min Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/comments/replies?media_id=3776832898280228145&comment_id=17901801633335930"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_replies_v2(media_id="3776832898280228145", comment_id="17901801633335930")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/comments/replies",
        headers=headers,
        params={"media_id": "3776832898280228145", "comment_id": "17901801633335930"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comments/replies?media_id=3776832898280228145&comment_id=17901801633335930",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "status": "ok"
}
```

</details>

---

### GET /v2/media/info/by/code

Get media object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/info/by/code?code=DRqAYKuAIUx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_info_by_code_v2(code="DRqAYKuAIUx")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/code",
        headers=headers,
        params={"code": "DRqAYKuAIUx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/info/by/code?code=DRqAYKuAIUx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "media_or_ad": {
    "strong_id__": "3776832898280228145_787132",
    "id": "3776832898280228145_787132",
    "disable_caption_and_comment": false,
    "fbid": 18065011277571522,
    "deleted_reason": 0,
    "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
    "integrity_review_decision": "pending",
    "pk": 3776832898280228145,
    "is_affiliate_commission_eligible": false,
    "has_delayed_metadata": false,
    "mezql_token": "",
    "should_request_ads": false,
    "has_privately_liked": false,
    "collaborator_edit_eligibility": false,
    "share_count_disabled": false,
    "is_reshare_of_text_post_app_media_in_ig": false,
    "is_visual_reply_commenter_notice_enabled": true,
    "translated_langs_for_autodub": [],
    "subtype_name_for_REST__": "XDTClipsMedia",
    "is_third_party_downloads_eligible": false,
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-atl3-3.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHIsXYh&_nc_oc=AdqE4g2JR5mID2obxS4JPXcrPi00dSDJb46fCwoXro5yYAUZoHayEb576bMKR1a6t7k&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_gid=87M24HNrc0sS13EXm3wLVA&_nc_ss=7a3ba&oh=00_Af1V-QE4HYijXibXZoAN3Bnau6uVsXAV__U3AXk2pEfAQQ&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-atl3-3.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHIsXYh&_nc_oc=AdqE4g2JR5mID2obxS4JPXcrPi00dSDJb46fCwoXro5yYAUZoHayEb576bMKR1a6t7k&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_gid=87M24HNrc0sS13EXm3wLVA&_nc_ss=7a3ba&oh=00_Af1V-QE4HYijXibXZoAN3Bnau6uVsXAV__U3AXk2pEfAQQ&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-atl3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwHHyAyb&_nc_oc=AdpQn755f4IP9fEXFJGCnthbTRfDZMEbgfoDdCQZ9_gTzO2MzSlVVPzcr25NwuO0NbA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_gid=87M24HNrc0sS13EXm3wLVA&_nc_ss=7a3ba&oh=00_Af0HAV7L-L5ONJrVMs_tzn9WXFacGdihtAcMRWdGcQmXRw&oe=69DC3E7E",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_urls": [
            "https://scontent-atl3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHrpnYIq0-QxyWAjEkckZ2VxNOO5B6RXEo_m-QIdSywk9IYF8lI5jDPSvn_YGJ6ots&_nc_ohc=7fRK9vLZo4UQ7kNvwHJXtXE&_nc_gid=87M24HNrc0sS13EXm3wLVA&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af1qUQGJ6Ph9ktdHmH8aMjUmPYMv2X841hoYaG9mi9-Ypw&oe=69DC4C8A&_nc_sid=55bbed"
          ],
          "sprite_width": 1500,
          "thumbnail_duration": 0.2125047619047619,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
  // ... truncated
```

</details>

---

### GET /v2/media/info/by/id

Get media object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/info/by/id?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_info_by_id_v2(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/id",
        headers=headers,
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/info/by/id?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "media_or_ad": {
    "strong_id__": "3776832898280228145_787132",
    "id": "3776832898280228145_787132",
    "disable_caption_and_comment": false,
    "fbid": 18065011277571522,
    "deleted_reason": 0,
    "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
    "integrity_review_decision": "pending",
    "pk": 3776832898280228145,
    "is_affiliate_commission_eligible": false,
    "has_delayed_metadata": false,
    "mezql_token": "",
    "should_request_ads": false,
    "has_privately_liked": false,
    "collaborator_edit_eligibility": false,
    "share_count_disabled": false,
    "is_reshare_of_text_post_app_media_in_ig": false,
    "is_visual_reply_commenter_notice_enabled": true,
    "translated_langs_for_autodub": [],
    "subtype_name_for_REST__": "XDTClipsMedia",
    "is_third_party_downloads_eligible": false,
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHTA9yC&_nc_oc=AdqHmW9YnmZQ7IDCKvZXC4Flj8_RVhOqFMlT_ofarIIyMMYxbD3IMufaIH1o4pxcd_w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&_nc_ss=7a3ba&oh=00_Af3a33y1SCADK3X8Y1vac3krZa67OxZXts_bP9nDIm06bg&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHTA9yC&_nc_oc=AdqHmW9YnmZQ7IDCKvZXC4Flj8_RVhOqFMlT_ofarIIyMMYxbD3IMufaIH1o4pxcd_w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&_nc_ss=7a3ba&oh=00_Af3a33y1SCADK3X8Y1vac3krZa67OxZXts_bP9nDIm06bg&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwEG2NBP&_nc_oc=Adrl6rLtRT8oA-sYrk7sWqASGZ1VHT1cPEkb5X0zwcMyPzPa8S77ah3qLmH6Gi289JE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&_nc_ss=7a3ba&oh=00_Af1ur4A5nh4jF4HLSOklXtzfSArEr5sp69CzorRVK-iEqg&oe=69DC3E7E",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_urls": [
            "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gH1ChdJBoSeGs0Ve_z8ef0EtbaWWXKwmbms-bMCkAVINVU6-EFYlnYLd3hPLv13Mbw&_nc_ohc=7fRK9vLZo4UQ7kNvwFYSYSE&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af3NgRuiSjRqaQWNbFcteslUnU1M1T6f5mVV-DX9FKKUFA&oe=69DC4C8A&_nc_sid=55bbed"
          ],
          "sprite_width": 1500,
          "thumbnail_duration": 0.2125047619047619,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
  // ... truncated
```

</details>

---

### GET /v2/media/info/by/url

Get media object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/info/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_info_by_url_v2(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/url",
        headers=headers,
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/info/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "media_or_ad": {
    "strong_id__": "3776832898280228145_787132",
    "id": "3776832898280228145_787132",
    "disable_caption_and_comment": false,
    "fbid": 18065011277571522,
    "deleted_reason": 0,
    "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
    "integrity_review_decision": "pending",
    "pk": 3776832898280228145,
    "is_affiliate_commission_eligible": false,
    "has_delayed_metadata": false,
    "mezql_token": "",
    "should_request_ads": false,
    "has_privately_liked": false,
    "collaborator_edit_eligibility": false,
    "share_count_disabled": false,
    "is_reshare_of_text_post_app_media_in_ig": false,
    "is_visual_reply_commenter_notice_enabled": true,
    "translated_langs_for_autodub": [],
    "subtype_name_for_REST__": "XDTClipsMedia",
    "is_third_party_downloads_eligible": false,
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-mad2-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHsRQ5h&_nc_oc=AdpQDeeZlfpJjk7TUbD0O6N3FbrSEDt78tSr38JZQePb_kDHw45b70H3ntKdREhtvHU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mad2-1.cdninstagram.com&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&_nc_ss=7a3ba&oh=00_Af2TpLJ_gRx4nJMCbPbuQtfxwPETmkcsyT4utBmQBltx5w&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-mad2-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHsRQ5h&_nc_oc=AdpQDeeZlfpJjk7TUbD0O6N3FbrSEDt78tSr38JZQePb_kDHw45b70H3ntKdREhtvHU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mad2-1.cdninstagram.com&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&_nc_ss=7a3ba&oh=00_Af2TpLJ_gRx4nJMCbPbuQtfxwPETmkcsyT4utBmQBltx5w&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-mad2-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwEDQke1&_nc_oc=AdpcSJNE-rTJ8rV4mix8lQuDrccGo--vstL5v3-nk_48Ft2d7RA9MSfyhsqdR12CxH8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mad2-1.cdninstagram.com&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&_nc_ss=7a3ba&oh=00_Af2wPxS4oMax-hisM1sNOpWCuMsJs5MjkxEkXVeVi9KzRA&oe=69DC3E7E",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_urls": [
            "https://scontent-mad1-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGB-qNzYmJRor7N8xX57vBVFllucQDYeHcHoaWZ4WJEDDi36eMJrcRqE3RlSiD1uFs&_nc_ohc=7fRK9vLZo4UQ7kNvwHTRANA&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af1Pw8FUXEL-jm0IGcmyIYVXILhETGieAqxiFR28RpfplA&oe=69DC4C8A&_nc_sid=55bbed"
          ],
          "sprite_width": 1500,
          "thumbnail_duration": 0.2125047619047619,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
  // ... truncated
```

</details>

---

### GET /v2/media/likers

Get user's likers. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/likers?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_likers_v2(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/likers",
        headers=headers,
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/likers?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "users": [
    {
      "strong_id__": "1469722832",
      "pk": 1469722832,
      "pk_id": "1469722832",
      "id": "1469722832",
      "full_name": "🅙orge Delgado 🦖",
      "is_private": true,
      "is_verified": false,
      "profile_pic_id": "3011497359763514020_1469722832",
      "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/324069253_5836767539705305_7097116477300814733_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gFh_MY3zYnKGik4uL8ZdW4zOj3CR6gHoPxjIVcfXdk4PM86jdxS5hrtUcoczODQ4U8&_nc_ohc=hKoACuZrKRgQ7kNvwF94gjA&_nc_gid=5aOLzkRaNLmoMOoCxKYYMA&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GIXnUBPZNddXgrwUAI0zFn-VBX5ibkULAAAB1501500j-ccb7-5&oh=00_Af0otuwZwalrh7ZYVEHVR2uRtQ2bDoJ4m2Dfeajak-ftnQ&oe=69DC2518&_nc_sid=bc52df",
      "username": "jorge10.ds",
      "is_new": false,
      "latest_reel_media": 0
    },
    {
      "strong_id__": "48158574428",
      "pk": 48158574428,
      "pk_id": "48158574428",
      "id": "48158574428",
      "full_name": "",
      "is_private": true,
      "is_verified": false,
      "profile_pic_id": "3861336032742852912_48158574428",
      "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-19/656236846_18037016978606429_8176123182175805432_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gFh_MY3zYnKGik4uL8ZdW4zOj3CR6gHoPxjIVcfXdk4PM86jdxS5hrtUcoczODQ4U8&_nc_ohc=8hgiqdDnz8cQ7kNvwFtu-Sd&_nc_gid=5aOLzkRaNLmoMOoCxKYYMA&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GC5hHSddSdFFkhRAAPjfbBm3bHdxbmNDAQAB1501500j-ccb7-5&oh=00_Af0-GZlNisFtWNC00qZrbLImoKvOFvUg_3KZBor42T8bYg&oe=69DC48D9&_nc_sid=bc52df",
      "username": "only_looking_at_fashionpeople",
      "is_new": false,
      "latest_reel_media": 0
    }
  ],
  "user_count": 135430,
  "status": "ok"
}
```

</details>

---

### GET /v2/media/template

Get media template

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/media/template?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_template_v2(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/media/template",
        headers=headers,
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/template?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "items": [
    {
      "media": {
        "strong_id__": "3776832898280228145_787132",
        "id": "3776832898280228145_787132",
        "pk": 3776832898280228145,
        "fbid": 18065011277571522,
        "media_type": 2,
        "like_and_view_counts_disabled": false,
        "code": "DRqAYKuAIUx",
        "taken_at": 1764453631,
        "product_type": "clips",
        "caption_is_edited": false,
        "can_viewer_reshare": true,
        "can_viewer_save": true,
        "comment_count": 485,
        "are_remixes_crosspostable": true,
        "video_versions": [
          {
            "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwE0M_w7&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0wOyLNB6UZiC0JmjoVGCA9flioAXGsGK-b0r1BaY-NoA&oe=69D8376F",
            "height": 1280,
            "width": 720,
            "type": 101,
            "id": "1525428988604088v",
            "bandwidth": 2315752
          },
          {
            "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwE0M_w7&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0wOyLNB6UZiC0JmjoVGCA9flioAXGsGK-b0r1BaY-NoA&oe=69D8376F",
            "height": 1280,
            "width": 720,
            "type": 102,
            "id": "1525428988604088v",
            "bandwidth": 2315752
          }
        ],
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                27870,
                55740
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFgTVfS&_nc_oc=AdpLHoQLXfU0rKWVlWACiYKacy41KnAciNOOdzVeK2iP-h6e1-V0dmyJzUetHDnP_lo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af34OC2Cb-tVsO0XqwIq-aHSHhEV-k9tyA3wt-_GXm3yjw&oe=69DC3E7E",
              "width": 750
            }
          ],
          "additional_candidates": {
            "first_frame": {
              "estimated_scans_sizes": [
                6839,
                13678
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGWwcXX&_nc_oc=Ado-A2vQBmUFKGBDfI56Wb_IHzPBlkfp_h78h5E8NNBs7l8q3CblKbaEPE0rt2Ls-i4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af3TEQWHLkzG67UwYgyNnzt3i8W14TlFcbpkjy8z-VVeBw&oe=69DC368F",
              "width": 640
            },
            "igtv_first_frame": {
              "estimated_scans_sizes": [
                6839,
                13678
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGWwcXX&_nc_oc=Ado-A2vQBmUFKGBDfI56Wb_IHzPBlkfp_h78h5E8NNBs7l8q3CblKbaEPE0rt2Ls-i4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af3TEQWHLkzG67UwYgyNnzt3i8W14TlFcbpkjy8z-VVeBw&oe=69DC368F",
              "width": 640
            }
          },
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "sprite_urls": [
                "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_cat=102&ccb=7-5&_nc_sid=efdbef&_nc_ohc=pyZiGYy3BegQ7kNvwFDvObk&_nc_oc=AdrcAWRgx1OiNB0Tdl6cqAIq_ooOD-LIiiXU5i7EEavcXeX6sURPl1PBB8KX15RC928&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af0oYfnKNdXLD6lwqrRb79vbjwQw0gz_vPMVrZzNZlkzDA&oe=69DC4C8A"
              ],
              "file_size_kb": 428,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
  // ... truncated
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-media){ target=_blank }
