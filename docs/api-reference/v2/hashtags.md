# Hashtag Endpoints

Get hashtag info and media.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/hashtag/by/name`](#get-v2hashtagbyname) | [`/v2/hashtag/medias/clips`](#get-v2hashtagmediasclips) | [`/v2/hashtag/medias/recent`](#get-v2hashtagmediasrecent) | [`/v2/hashtag/medias/top`](#get-v2hashtagmediastop)

---

### GET /v2/hashtag/by/name

Get hashtag object by name. Returns a Hashtag object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/hashtag/by/name?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_by_name_v2(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/hashtag/by/name",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/hashtag/by/name?name=love",
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
  "allow_muting_story": true,
  "subtitle": null,
  "follow_button_text": null,
  "show_follow_drop_down": false,
  "formatted_media_count": "2.1B",
  "is_trending": false,
  "hide_use_hashtag_button": false,
  "status": "ok",
  "allow_following": false,
  "profile_pic_url": null
}
```

</details>

---

### GET /v2/hashtag/medias/clips

Get hashtag chunk of clips (reels). Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/hashtag/medias/clips?name=love"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/hashtag/medias/clips",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/hashtag/medias/clips?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "sections": [
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870771007451871805_375121505",
                "id": "3870771007451871805_375121505",
                "fbid": 18119849704714197,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc3MTAwNzQ1MTg3MTgwNQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870771007451871805",
                "has_delayed_metadata": false,
                "mezql_token": "",
                "should_request_ads": false,
                "has_privately_liked": false,
                "collaborator_edit_eligibility": false,
                "share_count_disabled": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "subtype_name_for_REST__": "XDTFeedMedia",
                "has_views_fetching_on_search_grid": false,
                "image_versions2": {
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        11766,
                        23532
                      ],
                      "height": 1101,
                      "scans_profile": "e35",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af0S6klVtPYpfeL-HpuCWYmFPsnt8lA6c0UA7VYUX6Rw1g&oe=69DC1EC3",
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
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af3jjndY9GMc-VbGxt0-Ew9LO11LdxUSkZTDozgQXAGNuw&oe=69DC1EC3",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1079,
                "original_height": 1101,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYzQ2YTgyZDEzNGYxNDFjMmJkZTMxZGIyYzI2N2Y1NTEzODcwNzcxMDA3NDUxODcxODA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkzNzk0MXwzODcwNzcxMDA3NDUxODcxODA1fDMwMDA5MzA1OTIwfGMxNWNiMTA4MDZhMDJhNWIzYmM4ZWQ5NzhmMzZlNGFmODM1N2E5ZDhiNjIyNDFjNGI3OGQyMmZhMjJlYzkyNWEifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": null,
                  "music_canonical_id": "0",
                  "pinned_media_ids": null,
                  "music_info": null,
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775651897,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
  // ... truncated
```

</details>

---

### GET /v2/hashtag/medias/recent

Get hashtag chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/hashtag/medias/recent?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_recent_v2(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/hashtag/medias/recent",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/hashtag/medias/recent?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "sections": [
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870768443850599706_80471414250",
                "id": "3870768443850599706_80471414250",
                "disable_caption_and_comment": false,
                "fbid": 17864210406616995,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc2ODQ0Mzg1MDU5OTcwNg==.3",
                "integrity_review_decision": "pending",
                "pk": "3870768443850599706",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        4035,
                        8071
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/660975041_1222815363396675_7920028636465502001_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Rl1IdTbyXHAQ7kNvwFS6Zbd&_nc_oc=Ado7riRJUdAl02yTnzu4EUyao9Q3j-z9ej_ROYNF0OwIY4Y9Y4ndwCBRR4KH1QKbwms&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1m9DCXF8B2-aBFSoFYxbAjtHEMHavbhJCvmh_6zgkLKw&oe=69DC3373",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        4035,
                        8071
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/660975041_1222815363396675_7920028636465502001_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Rl1IdTbyXHAQ7kNvwFS6Zbd&_nc_oc=Ado7riRJUdAl02yTnzu4EUyao9Q3j-z9ej_ROYNF0OwIY4Y9Y4ndwCBRR4KH1QKbwms&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1m9DCXF8B2-aBFSoFYxbAjtHEMHavbhJCvmh_6zgkLKw&oe=69DC3373",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        4035,
                        8071
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/657333707_1643455193521085_868122056204770385_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc2ODQ0Mzg1MDU5OTcwNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=PEnJtbrhYCQQ7kNvwGSbAho&_nc_oc=AdpwtAxUHAvrjqCMYIYSnHLCPJbc9vVlSDFLC3WXRYUq3wVGYAFJey6hsxPmJrG_r44&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af2DHf1hEx-TlR5ngmeriWJgG1PwE8qbsFrnbPVch-F0pw&oe=69DC4AD3",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 422,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
  // ... truncated
```

</details>

---

### GET /v2/hashtag/medias/top

Get hashtag chunk of top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Name |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/hashtag/medias/top?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_v2(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/hashtag/medias/top",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/hashtag/medias/top?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "sections": [
      {
        "layout_type": "media_grid",
        "feed_type": "media",
        "explore_item_info": {
          "num_columns": 3,
          "total_num_columns": 3,
          "aspect_ratio": 3.0,
          "autoplay": false
        },
        "layout_content": {
          "medias": [
            {
              "media": {
                "strong_id__": "3870672463294524412_75290853567",
                "id": "3870672463294524412_75290853567",
                "disable_caption_and_comment": false,
                "fbid": 17882332371521536,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDY3MjQ2MzI5NDUyNDQxMg==.3",
                "integrity_review_decision": "pending",
                "pk": "3870672463294524412",
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
                "is_third_party_downloads_eligible": true,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "estimated_scans_sizes": [
                        852,
                        1704
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661157082_800931466046474_5827830693986962211_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_VFHpfU6zL8Q7kNvwGVvNhB&_nc_oc=Ado9hJCtRRCmLGmPxzlqjDagv4m3PBeKF5kpjdvAEb1ILQHQItyn7sBpwiWSlBGps3M&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af1_e3uGkDA0Br5Adts5aceQQEgv-Cqp9bczFnInU7tWLQ&oe=69DC2917",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        852,
                        1704
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661157082_800931466046474_5827830693986962211_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_VFHpfU6zL8Q7kNvwGVvNhB&_nc_oc=Ado9hJCtRRCmLGmPxzlqjDagv4m3PBeKF5kpjdvAEb1ILQHQItyn7sBpwiWSlBGps3M&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af1_e3uGkDA0Br5Adts5aceQQEgv-Cqp9bczFnInU7tWLQ&oe=69DC2917",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        3744,
                        7488
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/661604863_829242592916270_2274851443561613542_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDY3MjQ2MzI5NDUyNDQxMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=GlqvufCNZqMQ7kNvwFwwY9o&_nc_oc=Adq6f7yITxA7IKaDUoNeT_YIg5-O-BYclOuoAbEn30bQiuaSIPwNkYkGS2vyoolSm58&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af3PDTFPA-rbkXwDq_uaahDbgWmhHIMUkvxoltKFeKODcQ&oe=69DC447A",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 451,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
  // ... truncated
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-hashtags){ target=_blank }
