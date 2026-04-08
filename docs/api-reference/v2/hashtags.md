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
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 7,
                "like_count": 300,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18119849740714197",
                  "bit_flags": 0,
                  "created_at": 1775651899,
                  "created_at_utc": 1775651899,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18119849740714197",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870771007451871805,
                  "status": "Active",
                  "type": 1,
                  "user_id": 375121505,
                  "text": "Disney Princess irl",
                  "user": {
                    "strong_id__": "375121505",
                    "pk": 375121505,
                    "pk_id": "375121505",
                    "id": "375121505",
                    "is_unpublished": false,
                    "fbid_v2": 17841400525155861,
                    "username": "fallinginsociety",
                    "full_name": "FallingInSociety",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "1408922974837077103_375121505",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af2pkN_x7vJkaN3AdlpIEsaidTRFku5r3mSJ5r_Sw5KN5g&oe=69DC3771&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 5,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "375121505",
                  "id": "375121505",
                  "username": "fallinginsociety",
                  "full_name": "FallingInSociety",
                  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af2pkN_x7vJkaN3AdlpIEsaidTRFku5r3mSJ5r_Sw5KN5g&oe=69DC3771&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3vbkaDLo9",
                "device_timestamp": 1775651897,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
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
                ],
                "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af0S6klVtPYpfeL-HpuCWYmFPsnt8lA6c0UA7VYUX6Rw1g&oe=69DC1EC3",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775651897,
                "sponsor_tags": [],
                "play_count": 0
              }
            },
            {
              "media": {
                "strong_id__": "3870729737757151899_49646700667",
                "id": "3870729737757151899_49646700667",
                "fbid": 18096271229088381,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDcyOTczNzc1NzE1MTg5OQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870729737757151899",
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
                        31926,
                        63853
                      ],
                      "height": 1800,
                      "scans_profile": "e35",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af1ujBnkmonEo40525XbOcOaEf1XewN5KOakKIHZvU8wgw&oe=69DC4396",
                      "width": 1440,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        15722,
                        31445
                      ],
                      "height": 938,
                      "scans_profile": "e35",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af3tZwy6LzimziucIFFUIHtBGEI3G12GkN_zjg5ZZrWO2Q&oe=69DC4396",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1440,
                "original_height": 1800,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYzQ2YTgyZDEzNGYxNDFjMmJkZTMxZGIyYzI2N2Y1NTEzODcwNzI5NzM3NzU3MTUxODk5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkzNzk5OXwzODcwNzI5NzM3NzU3MTUxODk5fDMwMDA5MzA1OTIwfDBiNmQ3NGVkMDZiYzJhZWMyNmZiZmM2YmE5OTYxNjZmODY1MmUyZjVkOTU1MTYyZWU0YzUyNjJjZWQ1ZWExNDQifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": "licensed_music",
                  "music_canonical_id": "18356424895008836",
                  "pinned_media_ids": [],
                  "music_info": {
                    "music_canonical_id": 18356424895008836,
                    "music_asset_info": {
                      "allows_saving": false,
                      "artist_id": "2283138201970465",
                      "audio_asset_id": "541406764688578",
                      "audio_cluster_id": "1160377154637454",
                      "cover_artwork_thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/427913851_425943576536267_3463236288605832735_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=nA18uJ4rm4cQ7kNvwETn6Eh&_nc_oc=Adq5zsaNrDbvcGHKyqnt0APrn2l6ByyxvmZUolQ-JUcH0Qb8PrSHlT_N9yP8gBeyhGQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a39b&oh=00_Af3yviNYB_GDAWFMFJrRTYguHX9P32sbgDEkUy3L9ECZlQ&oe=69DC249B",
                      "cover_artwork_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/427913851_425943576536267_3463236288605832735_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=nA18uJ4rm4cQ7kNvwETn6Eh&_nc_oc=Adq5zsaNrDbvcGHKyqnt0APrn2l6ByyxvmZUolQ-JUcH0Qb8PrSHlT_N9yP8gBeyhGQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a39b&oh=00_Af3yviNYB_GDAWFMFJrRTYguHX9P32sbgDEkUy3L9ECZlQ&oe=69DC249B",
                      "dark_message": null,
                      "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT304.535675S\"><Period id=\"0\" duration=\"PT304.535675S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2262677247504857a\" bandwidth=\"75616\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"75616\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQMpZvFrpN7erLyNXXM-8zMuaOgqiXi24KMUD9FaPc6TtGOzf_h6ZMOwldz_fRqNsQu2Q17Khsy75m-saHb4HKBw.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=iJaUihDDTiwQ7kNvwHka3xB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo4MDA2NjUwNTE0ODkxNDEsImFzc2V0X2FnZV9kYXlzIjoxMTA1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzA0LCJiaXRyYXRlIjo3NTY4NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1RUO2-A6116KQXHS8R24qM3Fbgu9h-CfpKuRmveVQtLQ&amp;oe=69DC3806</BaseURL><SegmentBase indexRange=\"824-2691\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                      "display_artist": "Elevation Worship",
                      "duration_in_ms": 304535,
                      "fast_start_progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQMpZvFrpN7erLyNXXM-8zMuaOgqiXi24KMUD9FaPc6TtGOzf_h6ZMOwldz_fRqNsQu2Q17Khsy75m-saHb4HKBw.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=iJaUihDDTiwQ7kNvwHka3xB&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo4MDA2NjUwNTE0ODkxNDEsImFzc2V0X2FnZV9kYXlzIjoxMTA1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzA0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e87326c5858928f2&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT3E1UlNCMzlNb2h5a2NOQUNhSjIyeF90a01sYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm6o3Tv-uM7AIVAigCQzMsF0BzCI9cKPXDGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af0xXtlctXhhF0WQRWblns62-Ita-bqAgtbfO1bxE8T3yQ&oe=69DC3806",
                      "has_lyrics": true,
                      "highlight_start_times_in_ms": [
                        48000,
                        105000
                      ],
                      "id": "541406764688578",
                      "ig_username": "elevationworship",
                      "is_eligible_for_audio_effects": true,
                      "is_eligible_for_vinyl_sticker": true,
                      "is_explicit": false,
                      "licensed_music_subtype": "DEFAULT",
                      "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQMpZvFrpN7erLyNXXM-8zMuaOgqiXi24KMUD9FaPc6TtGOzf_h6ZMOwldz_fRqNsQu2Q17Khsy75m-saHb4HKBw.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=iJaUihDDTiwQ7kNvwHka3xB&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo4MDA2NjUwNTE0ODkxNDEsImFzc2V0X2FnZV9kYXlzIjoxMTA1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzA0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e87326c5858928f2&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT3E1UlNCMzlNb2h5a2NOQUNhSjIyeF90a01sYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm6o3Tv-uM7AIVAigCQzMsF0BzCI9cKPXDGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af0xXtlctXhhF0WQRWblns62-Ita-bqAgtbfO1bxE8T3yQ&oe=69DC3806",
                      "reactive_audio_download_url": null,
                      "sanitized_title": null,
                      "song_monetization_info": null,
                      "subtitle": "",
                      "title": "Praise (feat. Brandon Lake, Chris Brown, Chandler Moore)",
                      "web_30s_preview_download_url": null,
                      "lyrics": null,
                      "spotify_track_metadata": null,
                      "related_audios": null
                    },
                    "music_consumption_info": {
                      "allow_media_creation_with_music": true,
                      "music_creation_restriction_reason": null,
                      "audio_asset_start_time_in_ms": 55424,
                      "derived_content_start_time_in_composition_in_ms": 0,
                      "contains_lyrics": null,
                      "derived_content_id": null,
                      "display_labels": null,
                      "formatted_clips_media_count": null,
                      "is_bookmarked": false,
                      "is_trending_in_clips": true,
                      "overlap_duration_in_ms": 90000,
                      "placeholder_profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=HMeNVRbt-xsQ7kNvwEVy9wE&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4AAAAA&ccb=7-5&oh=00_Af0ADakOptAaAs_rYwsrFClfvib2kpqFr1HWfx1F13ortA&oe=69DC253D&_nc_sid=472314",
                      "should_allow_music_editing": false,
                      "should_mute_audio": false,
                      "should_mute_audio_reason": "",
                      "should_mute_audio_reason_type": null,
                      "should_render_soundwave": false,
                      "trend_rank": null,
                      "previous_trend_rank": null,
                      "ig_artist": {
                        "strong_id__": "307509295",
                        "pk": 307509295,
                        "pk_id": "307509295",
                        "id": "307509295",
                        "username": "elevationworship",
                        "full_name": "Elevation Worship",
                        "is_private": false,
                        "is_verified": true,
                        "profile_pic_id": "3814372290864467300_307509295",
                        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/619566013_18550293298053296_8897657889483886820_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=8anF_jWdEBkQ7kNvwEV-aT_&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GL3T7SSwgIK6ZOdBAOSQo2u11Hp7bmNDAQAB1501500j-ccb7-5&oh=00_Af1J0Ge6IK8O8oo1sRyAzHISZRqYADxL4UOg0Cg95T4iEg&oe=69DC2561&_nc_sid=472314"
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
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775647202,
                "usertags": [
                  {
                    "user": {
                      "pk": "201558512",
                      "id": "201558512",
                      "username": "wendy_saved_by_grace",
                      "full_name": "Wendy Huber",
                      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/184015669_492120375249882_7370163052157690695_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=LmbLdMmoC1oQ7kNvwHZP_qe&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDXb9wraSye0lL8BAEdjkUQ-FEhmbkULAAAB1501500j-ccb7-5&oh=00_Af2z5TSgEmAXhqMxO5dmzNPbJBlSYc2gSRA7jwmyfR2jSg&oe=69DC4B92&_nc_sid=472314",
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
                      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/619566013_18550293298053296_8897657889483886820_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=8anF_jWdEBkQ7kNvwEV-aT_&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GL3T7SSwgIK6ZOdBAOSQo2u11Hp7bmNDAQAB1501500j-ccb7-5&oh=00_Af1J0Ge6IK8O8oo1sRyAzHISZRqYADxL4UOg0Cg95T4iEg&oe=69DC2561&_nc_sid=472314",
                      "profile_pic_url_hd": null,
                      "is_private": false,
                      "is_verified": true
                    },
                    "x": 0.8549242424,
                    "y": 0.9836601298000001
                  }
                ],
                "photo_of_you": false,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": true,
                  "mashup_type": null,
                  "mashups_allowed": true,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
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
                    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/468367136_545676408366967_6972864757526950554_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=szV8GBoN7jQQ7kNvwH0RJDl&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCC36ht3p3swSvABAJryO5uNl8RgbkULAAAB1501500j-ccb7-5&oh=00_Af2rhfPS_F_nBQDcGIgUFYzEK0e0dwL19t4EWiGozs6vDg&oe=69DC3EB9&_nc_sid=472314",
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
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/184015669_492120375249882_7370163052157690695_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=LmbLdMmoC1oQ7kNvwHZP_qe&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDXb9wraSye0lL8BAEdjkUQ-FEhmbkULAAAB1501500j-ccb7-5&oh=00_Af2z5TSgEmAXhqMxO5dmzNPbJBlSYc2gSRA7jwmyfR2jSg&oe=69DC4B92&_nc_sid=472314",
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
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "collab_follow_button_info": {
                  "show_follow_button": true,
                  "is_owner_in_author_exp": true
                },
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 90,
                "like_count": 3,
                "top_likers": [
                  "pamelajo13"
                ],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18096271373088381",
                  "bit_flags": 0,
                  "created_at": 1775647202,
                  "created_at_utc": 1775647202,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18096271373088381",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870729737757151899,
                  "status": "Active",
                  "type": 1,
                  "user_id": 49646700667,
                  "text": "𝗚𝗼𝗼𝗱 𝗺𝗼𝗿𝗻𝗶𝗻𝗴 𝗳𝗮𝗺𝗶𝗹𝘆 💝\n𝗜𝗳 𝘆𝗼𝘂 𝘄𝗼𝗸𝗲 𝘂𝗽 𝘁𝗵𝗶𝘀 𝗺𝗼𝗿𝗻𝗶𝗻𝗴… \n𝗚𝗼𝗱 𝗶𝘀 𝗻𝗼𝘁 𝗱𝗼𝗻𝗲 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂 𝘆𝗲𝘁. \n\nToday, we rise with gratitude in our \nhearts & praise on our lips. God has \nbeen so good to us. He woke us up, \ncovered us, and is leading us into a \nnew day filled w/ purpose & promise.\n\n“Because of the Lord’s great love \nwe are not consumed, for His \nmercies never fail. They are new \nevery morning; great is Your \nfaithfulness.” — 𝗟𝗮𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻𝘀 𝟯:𝟮𝟮–𝟮𝟯\n\n𝗣𝗿𝗮𝘆𝗲𝗿:\nLord, thank You for the gift of today.\nEven if my heart feels heavy, help \nme choose gratitude. Remind me that \nYou are with me, guiding me, and \nworking all things for good. Give me \npeace for what I can’t control and \nstrength for what’s ahead. Let my \nlife reflect Your love today. In Jesus’ \nname, Amen. 🤍✨\n\n𝗗𝗲𝗰𝗹𝗮𝗿𝗮𝘁𝗶𝗼𝗻:\nToday, I will walk in gratitude.\nI will trust God with every step.\nI am covered, I am guided, and I am \nnot alone. This day holds purpose, \nand I will walk in it. 🙌🏼✨\n\n𝗚𝗼𝗱 𝗯𝗹𝗲𝘀𝘀 𝘆𝗼𝘂 𝗽𝗿𝗲𝗰𝗶𝗼𝘂𝘀 𝗰𝗵𝗶𝗹𝗱! 👑\n\n𝐈𝐟 𝐲𝐨𝐮 𝐤𝐧𝐨𝐰 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐭𝐡𝐚𝐭 𝐧𝐞𝐞𝐝𝐬 \n𝐭𝐡𝐢𝐬 𝐞𝐧𝐜𝐨𝐮𝐫𝐚𝐠𝐞𝐦𝐞𝐧𝐭, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐡𝐚𝐫𝐞 \n& 𝐭𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 🙏🏼\n\n#chosen2reign #childlikefaith #godfirst\n#trustinthelord #happywednesday",
                  "user": {
                    "strong_id__": "49646700667",
                    "pk": 49646700667,
                    "pk_id": "49646700667",
                    "id": "49646700667",
                    "is_unpublished": false,
                    "fbid_v2": 17841449580035837,
                    "username": "chosen_2_reign",
                    "full_name": "𝐂𝐢𝐧𝐝𝐲 & 𝐖𝐞𝐧𝐝𝐲",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "2685218318953352068_49646700667",
                    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/245410687_270162081680252_8621949966077360040_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40ODAuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=6IiLqxbZRAgQ7kNvwGU4mIt&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GH_roA58C_kCtvUAAKh3OyfQUad3bkULAAAB1501500j-ccb7-5&oh=00_Af0Ics1w5xUHqiDJX9fN2P-e0mmx7wH9R5s50H0GMkF1RQ&oe=69DC51EE&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 93,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
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
                "locations": [],
                "lng": -81.5258,
                "lat": 28.6899,
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "IPTC_METADATA_EDITED"
                },
                "user": {
                  "pk": "49646700667",
                  "id": "49646700667",
                  "username": "chosen_2_reign",
                  "full_name": "𝐂𝐢𝐧𝐝𝐲 & 𝐖𝐞𝐧𝐝𝐲",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/245410687_270162081680252_8621949966077360040_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40ODAuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=6IiLqxbZRAgQ7kNvwGU4mIt&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GH_roA58C_kCtvUAAKh3OyfQUad3bkULAAAB1501500j-ccb7-5&oh=00_Af0Ics1w5xUHqiDJX9fN2P-e0mmx7wH9R5s50H0GMkF1RQ&oe=69DC51EE&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3mDBAjlKb",
                "device_timestamp": 177564696383231,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "like_and_view_counts_disabled": true,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      31926,
                      63853
                    ],
                    "height": 1800,
                    "scans_profile": "e35",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af1ujBnkmonEo40525XbOcOaEf1XewN5KOakKIHZvU8wgw&oe=69DC4396",
                    "width": 1440,
                    "is_spatial_image": false
                  },
                  {
                    "estimated_scans_sizes": [
                      15722,
                      31445
                    ],
                    "height": 938,
                    "scans_profile": "e35",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af3tZwy6LzimziucIFFUIHtBGEI3G12GkN_zjg5ZZrWO2Q&oe=69DC4396",
                    "width": 750,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af1ujBnkmonEo40525XbOcOaEf1XewN5KOakKIHZvU8wgw&oe=69DC4396",
                "taken_at_ts": 1775647202,
                "sponsor_tags": [],
                "play_count": 0
              }
            }
          ]
        }
      },
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
                "strong_id__": "3870783242873457024_36818859777",
                "id": "3870783242873457024_36818859777",
                "disable_caption_and_comment": false,
                "fbid": 18094269269145299,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc4MzI0Mjg3MzQ1NzAyNA==.3",
                "integrity_review_decision": "pending",
                "pk": "3870783242873457024",
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
                        5023,
                        10046
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/669664565_801223275985690_187139950299545489_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=106&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=kt46XuxvS0wQ7kNvwFW4xnh&_nc_oc=AdqzmcNjoTKQ_nChI2QEGpl-BwYpMef2qxDyBHPQwfv03QEp6ssF1MYR3OeuM_Bayvc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af2ajzjglM_rDOfGeMAlVSt56I1PqH-RsgRmF3ACeK5ufQ&oe=69DC1EC0",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        5023,
                        10046
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/669664565_801223275985690_187139950299545489_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=106&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=kt46XuxvS0wQ7kNvwFW4xnh&_nc_oc=AdqzmcNjoTKQ_nChI2QEGpl-BwYpMef2qxDyBHPQwfv03QEp6ssF1MYR3OeuM_Bayvc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af2ajzjglM_rDOfGeMAlVSt56I1PqH-RsgRmF3ACeK5ufQ&oe=69DC1EC0",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        5288,
                        10577
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/669855753_1635148147696919_3730890493730747042_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc4MzI0Mjg3MzQ1NzAyNA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=og-8Spyn5rwQ7kNvwFkUHim&_nc_oc=AdoX1RAedtTbLWYLmHdKT9HuoqAHnWJsVAjPSq8dMbuQ_0XozmK15av5Ybe6CtPiVus&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af2FqwCLElBP_6xY6XtDVY5kUQj5DN87WKL7CLXmVOBM7A&oe=69DC4562",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 625,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/662347871_1774829556835225_2027274968876806101_n.jpg?_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=o7McvXRA1asQ7kNvwE5C3Ax&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af15_JXU6DO1CSkcL0GPoZYSzhs10vG9u49z0OZDn_JKJA&oe=69DC3AC3&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.1527809523809524,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 16.042
                    }
                  }
                },
                "media_type": 2,
                "original_width": 720,
                "original_height": 1280,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYzQ2YTgyZDEzNGYxNDFjMmJkZTMxZGIyYzI2N2Y1NTEzODcwNzgzMjQyODczNDU3MDI0Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkzNzk5OXwzODcwNzgzMjQyODczNDU3MDI0fDMwMDA5MzA1OTIwfDNlNTE1M2YyNTJhNDQ3Yzk3NDljNmIyZjg2ZDZlYjI0MzJjNDJhN2RhYjMxY2NmM2E5ZmZhZjNiZGU4OGI5ZWQifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "hi",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775653394,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "is_artist_pick": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "clips",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "cutout_sticker_info": [],
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "media_ui_attributions_data": [],
                "media_ui_attributions_data_v2": [],
                "creator_product_link_infos": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 0,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 7,
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
                    "best_audio_cluster_id": "1971844406985030"
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
                  "music_canonical_id": "18522874690037722",
                  "music_info": null,
                  "nux_info": null,
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": 1472406570571016,
                    "attributed_custom_audio_asset_id": null,
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": true,
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT16.044989S\" FBManifestTimestamp=\"1775657938\" FBManifestIdentifier=\"FqSPs50NKRawvM3Oo+/kAiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT16.044989S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"784764024499992a\" bandwidth=\"71823\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71823\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNYtBHcXVTP2sPa0R2SCWi1-1oG4HBjdlVgAYQarpq8uUWgr3RcF8G9AwO5aWCBJ39Ur_ybauIlUlHx1gKzmNo.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=n8EtKLbyfRAQ7kNvwGcSXca&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjc2NDUwNjgxMzEzMjI0MCwiYXNzZXRfYWdlX2RheXMiOjIyMiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjo3MjI5NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3_vWN3Moy-1qqDAja3aEnO-f1I8PB-Vbyi-eu4F-wECw&amp;oe=69D8308E</BaseURL><SegmentBase indexRange=\"824-951\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 16065,
                    "formatted_clips_media_count": null,
                    "hide_remixing": false,
                    "is_audio_automatically_attributed": true,
                    "is_eligible_for_audio_effects": true,
                    "is_eligible_for_vinyl_sticker": true,
                    "is_explicit": false,
                    "is_original_audio_download_eligible": true,
                    "is_reuse_disabled": false,
                    "is_xpost_from_fb": false,
                    "music_canonical_id": null,
                    "oa_owner_is_music_artist": false,
                    "original_audio_subtype": "contains",
                    "original_audio_title": "Original audio",
                    "original_media_id": 3709911927801166703,
                    "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQOcSuZ3iyEAoyNATJKZ3340-g1qFe9gbXFQHeLlnLDK1yUpfXok86Zj4FUWJ9uLm03HjaVDU77ayjE_koaU1jtt.mp4?strext=1&_nc_cat=102&_nc_sid=8bf8fe&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=vXnPd0TTCcsQ7kNvwEMYWbP&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6NzY0NTA2ODEzMTMyMjQwLCJhc3NldF9hZ2VfZGF5cyI6MjIyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af1rFXKeQtT51WmyQcCsgwvor8htIqEp17hProIYKkg1pw&oe=69DC2F20",
                    "should_mute_audio": false,
                    "time_created": 1756476273,
                    "trend_rank": null,
                    "previous_trend_rank": null,
                    "overlap_duration_in_ms": 16036,
                    "audio_asset_start_time_in_ms": 0,
                    "derived_content_start_time_in_composition_in_ms": 0,
                    "ig_artist": {
                      "strong_id__": "8552447000",
                      "pk": 8552447000,
                      "pk_id": "8552447000",
                      "id": "8552447000",
                      "username": "lisha_hema",
                      "full_name": "Lisha Jayaraj",
                      "is_private": false,
                      "is_verified": false,
                      "profile_pic_id": "3845280851110810778_8552447000",
                      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/642564518_18310746604287001_542870674382066659_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=5y1euaErzp0Q7kNvwE1S-ZD&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GKbBTCYZtOvqhg1BAOMThYkAqogHbmNDAQAB1501500j-ccb7-5&oh=00_Af3ss1QX8Ur477d8SciH57c9cviR6qsLLDISqXgr_3PShw&oe=69DC2587&_nc_sid=472314"
                    },
                    "audio_filter_infos": null,
                    "audio_parts": [
                      {
                        "music_canonical_id": "18197571160002327",
                        "audio_type": "licensed_music",
                        "display_artist": "Javed Ali, Priya Himesh, Kunal Ganjawala",
                        "ig_artist": {
                          "strong_id__": "3242126306",
                          "pk": 3242126306,
                          "pk_id": "3242126306",
                          "id": "3242126306",
                          "username": "javedali4u",
                          "full_name": "Javed Ali",
                          "is_private": false,
                          "is_verified": true,
                          "profile_pic_id": "3511784938506497208_3242126306",
                          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/468751179_592608986500097_1587115570474278568_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MzQuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=BHk4WxZfApgQ7kNvwFywTgT&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GEuT8BsBjCGI_RoCAKhenNMzkQYWbkULAAAB1501500j-ccb7-5&oh=00_Af3Wmn34axL3XFOVP4WY3CuWXRX1pB8S2cvX0nhlzZqlPA&oe=69DC2904&_nc_sid=472314"
                        },
                        "display_title": "Kannukkulle",
                        "thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/424599872_1096459691383717_1539373183882334647_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=yMczNsEIpuAQ7kNvwFkj9aI&_nc_oc=AdrErWSqieqQyY-i6UTctd_cNFXda_-zw0Ygwty8aelGaAelnOb8pLGqWAO30L7pLT4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a39b&oh=00_Af1jCpYcKqaGrDQU8xSIaIHt283TyAMpoH2MC2rTqmNEiA&oe=69DC294F",
                        "is_bookmarked": false,
                        "is_explicit": false,
                        "parent_start_time_in_ms": 0,
                        "audio_start_time_in_ms": 0,
                        "duration_in_ms": 30,
                        "is_eligible_for_audio_effects": false,
                        "derived_content_start_time_in_composition_in_ms": 0
                      }
                    ],
                    "audio_parts_by_filter": [
                      {
                        "music_canonical_id": "18197571160002327",
                        "audio_type": "licensed_music",
                        "display_artist": "Javed Ali, Priya Himesh, Kunal Ganjawala",
                        "ig_artist": {
                          "strong_id__": "3242126306",
                          "pk": 3242126306,
                          "pk_id": "3242126306",
                          "id": "3242126306",
                          "username": "javedali4u",
                          "full_name": "Javed Ali",
                          "is_private": false,
                          "is_verified": true,
                          "profile_pic_id": "3511784938506497208_3242126306",
                          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/468751179_592608986500097_1587115570474278568_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MzQuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=BHk4WxZfApgQ7kNvwFywTgT&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GEuT8BsBjCGI_RoCAKhenNMzkQYWbkULAAAB1501500j-ccb7-5&oh=00_Af3Wmn34axL3XFOVP4WY3CuWXRX1pB8S2cvX0nhlzZqlPA&oe=69DC2904&_nc_sid=472314"
                        },
                        "display_title": "Kannukkulle",
                        "thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/424599872_1096459691383717_1539373183882334647_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=yMczNsEIpuAQ7kNvwFkj9aI&_nc_oc=AdrErWSqieqQyY-i6UTctd_cNFXda_-zw0Ygwty8aelGaAelnOb8pLGqWAO30L7pLT4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a39b&oh=00_Af1jCpYcKqaGrDQU8xSIaIHt283TyAMpoH2MC2rTqmNEiA&oe=69DC294F",
                        "is_bookmarked": false,
                        "is_explicit": false,
                        "parent_start_time_in_ms": 0,
                        "audio_start_time_in_ms": 0,
                        "duration_in_ms": 30,
                        "is_eligible_for_audio_effects": false,
                        "derived_content_start_time_in_composition_in_ms": 0
                      }
                    ],
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
                "like_count": 815,
                "fb_like_count": 6,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18094269311145299",
                  "bit_flags": 0,
                  "created_at": 1775653379,
                  "created_at_utc": 1775653379,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18094269311145299",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870783242873457024,
                  "status": "Active",
                  "type": 1,
                  "user_id": 36818859777,
                  "text": "Un kanukulaa\n.\n.\n.\n#sadhana #reels #insta #instagood #love",
                  "user": {
                    "strong_id__": "36818859777",
                    "pk": 36818859777,
                    "pk_id": "36818859777",
                    "id": "36818859777",
                    "is_unpublished": false,
                    "fbid_v2": 17841436833322357,
                    "username": "_sadhana_off_",
                    "full_name": "Sadhana Namidass",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3862839882363818533_36818859777",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658043634_18088106555227778_711827866841328521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NjAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=sC6SAfK4AlgQ7kNvwHaX7pL&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GPLyOCeCPuJ9CUNAAIkrTWis6_AJbmNDAQAB1501500j-ccb7-5&oh=00_Af3CwpcBm_PAKGZ6yboOKkOLWjs0sEcUbA1nVV5l8GBUrQ&oe=69DC408B&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 48,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "fb_comment_count": 0,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 15078,
                "ig_play_count": 14913,
                "fb_play_count": 165,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "is_feedback_aggregated": true,
                  "unified_feedback_enabled": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_subtitles_locale": "hi_FB",
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 16.04400062561035,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1853484,
                    "height": 1280,
                    "id": "2023951411523821v",
                    "type": 101,
                    "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOJS4O3tO7-FrB7h8sbls55jJpbgXM-e_gESqtWDjRiJzgYQP9OTTlg3HKwyFIanULCkzR2U6n4TiUn8XRh99gWo_boaLDEpo13sA8.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=9bU5wAoPIrkQ7kNvwETdQGj&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0MTM3ODQxMTU1MTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=e2b10f1013f002b8&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80QzQ2M0UwRUU0RTAwNjFDOEZDNjkxMjA4RjQzNzM5M192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzgwNEI1QzFBRDA1QjI3MEE2RTg1NDI3OTkyM0FBMkIxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbu5K3G0ZblPxUCKAJDMywXQDAIcrAgxJwYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2Ar0ozD3sPUnElwW4o_zASLJS9OvSmVaWtnWu5cMxDWQ&oe=69D8532A",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  },
                  {
                    "bandwidth": 1853484,
                    "height": 1280,
                    "id": "2023951411523821v",
                    "type": 102,
                    "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOJS4O3tO7-FrB7h8sbls55jJpbgXM-e_gESqtWDjRiJzgYQP9OTTlg3HKwyFIanULCkzR2U6n4TiUn8XRh99gWo_boaLDEpo13sA8.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=9bU5wAoPIrkQ7kNvwETdQGj&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0MTM3ODQxMTU1MTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=e2b10f1013f002b8&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80QzQ2M0UwRUU0RTAwNjFDOEZDNjkxMjA4RjQzNzM5M192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzgwNEI1QzFBRDA1QjI3MEE2RTg1NDI3OTkyM0FBMkIxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbu5K3G0ZblPxUCKAJDMywXQDAIcrAgxJwYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2Ar0ozD3sPUnElwW4o_zASLJS9OvSmVaWtnWu5cMxDWQ&oe=69D8532A",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT16.044989S\" FBManifestTimestamp=\"1775657938\" FBManifestIdentifier=\"FqSPs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxt6rx7+Mg8YC9pfezs3d5gLat/S9zsH+AoyX+Lni360D4pmk/+qSuATyzMnBi4/DBPqy6cnI7rEFiKjTlOrp6gXOwuzr59DyBZqps7LJhLgGyPiQvvbrtQfW5cKE6PH1eyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT16.044989S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.5\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1273493708157753v\" bandwidth=\"153517\" codecs=\"av01.0.00M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"307674\" FBPlaybackResolutionMos=\"0:100,360:57.6,480:55,720:53\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:85.9,480:80.2,720:70.3\" FBAbrPolicyTags=\"\" width=\"288\" height=\"512\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"180p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPrFC38mgbp-UMtFaTpc8pQatofsjNHuNnh5zXNSy9xyZRgnGDxl1cB6CE3Hq8Sht77SUF7bOAZbmkAR6NMQnyr1L6aqV10D7OQSWY.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=XTdK_Y-XeQgQ7kNvwFp2d8f&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MTUzNTE3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3vjv1aYbVsKem3VgSXgSio6OqtePrSc-0P6DSNHhL4UQ&amp;oe=69DC443E</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-8046\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-71978\" FBFirstSegmentRange=\"906-103621\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"103622-184864\" FBPrefetchSegmentRange=\"906-103621\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1517026549771453v\" bandwidth=\"204778\" codecs=\"av01.0.00M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"410411\" FBPlaybackResolutionMos=\"0:100,360:62.2,480:59.2,720:56.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.2,480:84.2,720:75.3\" FBAbrPolicyTags=\"\" width=\"288\" height=\"512\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOCzUqZJ4nudH1LXq9bOY7B3547d2S2ztkO-ihMaoisdDxoWbmNdX_vPfxCEV1PGYb_qorTxEpvdLfMCbUiQwNevHB5oIou5yWoExI.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=tEKq0X4SGOEQ7kNvwFQW5VZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MjA0Nzc4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3DTwTk6brFZmGehW_lF0pIOmoHWvhVl3T6pVeQYyne8A&amp;oe=69DC5000</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-9110\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-93196\" FBFirstSegmentRange=\"906-137919\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"137920-245924\" FBPrefetchSegmentRange=\"906-137919\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"34880663144913259v\" bandwidth=\"271439\" codecs=\"av01.0.01M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"544009\" FBPlaybackResolutionMos=\"0:100,360:68.1,480:64.9,720:62.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:88.8,720:81.3\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQO18AtiWmRF3ej6nVtzGGglkvLstq_J2ZfEz63JnUm6ue0ZEV6XoOuzV3oN96Xsr6pIow24e3FekIdU6WmxldcoGhfwXdM6Ok_Wq0E.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=QvCP3ukTFQoQ7kNvwH4rRqC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MjcxNDM5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3pQfZ2gNw1GbXVAn5QNxOK1Y5LOaDkI4tQtR1wUz5RDg&amp;oe=69DC2B11</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-10358\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-122140\" FBFirstSegmentRange=\"906-183030\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"183031-325374\" FBPrefetchSegmentRange=\"906-183030\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"716934798174959v\" bandwidth=\"416889\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"835517\" FBPlaybackResolutionMos=\"0:100,360:73.2,480:70.5,720:68.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.3,480:92.7,720:87.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQP37DAk-eoksW-Ettygmq0szBuwVyNU2mQ0faY-d2eSoXrifTOVpdCq9iPMKp494mazob87fp3bl8SQCsSJE2iTCO0EpjWaN1H9lL4.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=gYWSjqZ57zcQ7kNvwHT7wMo&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6NDE2ODg5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af02X39Ykmy7myE7fI4UrveEXqyU9-a2eH9F6S5qA0e1Rw&amp;oe=69DC4B08</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-16268\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-183653\" FBFirstSegmentRange=\"906-278166\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"278167-499067\" FBPrefetchSegmentRange=\"906-278166\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1249368807343729v\" bandwidth=\"544929\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"1092129\" FBPlaybackResolutionMos=\"0:100,360:76.2,480:73.6,720:71.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:95.1,720:90.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOz5WpZRY_Y0h5Qn21RmbrL_wkEg75NSUetuOvCP6CrKZWwShUOWp2-M9txDNT9SwZykhvVYCqWAhkitJR6YykZRXKYD-c_rFA8Sa0.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=X_Esu2QPTpQQ7kNvwGi_qgG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6NTQ0OTI5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3AEh7J_JCYxxjn-yUt6hfmR3tPOactlIDmMUVBEiuQbg&amp;oe=69DC2040</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-18546\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-234862\" FBFirstSegmentRange=\"906-363354\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"363355-651419\" FBPrefetchSegmentRange=\"906-363354\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"945026278294982v\" bandwidth=\"708673\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"1420300\" FBPlaybackResolutionMos=\"0:100,360:78.6,480:76,720:73.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.8,720:93.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOk-4VSDD4V336sTencZuuRcsjz3jtbo74cl82Ix3abeY3XxQgacc6OIQGuzicAOAbE6lxqfNWYL44gQon5tACMDVo8-2LjpbYtoNU.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=2A667pxnk2gQ7kNvwHWw3jK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6NzA4NjczLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0zsn4MCx7O7SEXc2bOidxAtiuplIBgasnzU0Yky8hH4Q&amp;oe=69DC2E74</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-20348\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-298227\" FBFirstSegmentRange=\"906-471257\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"471258-848141\" FBPrefetchSegmentRange=\"906-471257\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1659451861733543v\" bandwidth=\"1037824\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"2079973\" FBPlaybackResolutionMos=\"0:100,360:82.1,480:79,720:76.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.84,480:98.29,720:96.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOv29JN60WHZyC20c3EvFKmi95H_fne7BPrmtSW9BJX_QX_fHrdQqx_0aSr7FZJ4stv2SGtgEY1UeR3O3QmLm4I1nsNLdd9qWFmUpE.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=kCu-VsLVYOYQ7kNvwER3TSD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MTAzNzgyNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1yIYau5DYwG3Gkp4yPQnhM6HTDwv2PgBej0U7Zo6qGwQ&amp;oe=69DC4BA5</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-24270\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-423630\" FBFirstSegmentRange=\"906-690553\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"690554-1251858\" FBPrefetchSegmentRange=\"906-690553\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"788858470647291v\" bandwidth=\"1693585\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"3394228\" FBPlaybackResolutionMos=\"0:100,360:85.5,480:82.8,720:79.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.412,480:99.179,720:98.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMaBJRduhMvzNJIl5gplv958JbCY9M20niLRteSZuBoPSIAY6wIceqMonIbnvZ9O0jfZ8d1_6Hbiz3CUwvium1OG9w_f6RjTKLRK3w.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=pSl7OdBbq9oQ7kNvwFfxkOe&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQxMzc4NDExNTUxMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MTY5MzU4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0hPA_JxgXb6VdIsg88jBcbk20617oHoBrR9BWPUM0q8Q&amp;oe=69DC20E2</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-30700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-662070\" FBFirstSegmentRange=\"906-1116189\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1116190-2065267\" FBPrefetchSegmentRange=\"906-1116189\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1812073732794957a\" bandwidth=\"45492\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45492\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"92155\" FBPaqMos=\"87.94\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQM8hcJ9LweKcIn92BnLB4M4hIgyMbMLGToS8veVb2p679DT48V3xyNa2M6HMsknngWMolXmPZYj8TZgqjYbt5I7PBR7SEvMJ0Qvgbw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=em3w79iPyU0Q7kNvwG0Y_Jw&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDEzNzg0MTE1NTExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjo0NTk0OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1R9WF-u_9YEVoFkxQtKjo3GLAxs__yzp9PMz_RdLvUJA&amp;oe=69DC27CE</BaseURL><SegmentBase indexRange=\"837-916\" timescale=\"44100\" FBMinimumPrefetchRange=\"917-2163\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"917-15737\" FBFirstSegmentRange=\"917-29093\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"29094-57164\" FBPrefetchSegmentRange=\"917-29093\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1642289483639300a\" bandwidth=\"78861\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"78861\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"159082\" FBPaqMos=\"89.66\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPjUvZOSgiKn8VcYMjQoNeoizYjthOd9rJiY241DEtlizB8yBVqseTOvk2cb2nvk0WeDddreBdna__rFVFUePBBrNB64M_sMQjd3OY.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=IBo49D9jlEcQ7kNvwGA0sEj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDEzNzg0MTE1NTExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjo3OTMxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1LsqI-CS-snAK18qRb1n-ZqaIijQEu1FwKE6OQQjAuAg&amp;oe=69DC230A</BaseURL><SegmentBase indexRange=\"838-917\" timescale=\"44100\" FBMinimumPrefetchRange=\"918-2847\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-26752\" FBFirstSegmentRange=\"918-50341\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"50342-99335\" FBPrefetchSegmentRange=\"918-50341\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"2088727218363940a\" bandwidth=\"132565\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"132565\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"266788\" FBPaqMos=\"94.11\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMDvBbBMwDjxi27Zsdh-tek4QfwI2D-Q7Sc8UjatmQt8K_zUuabOxo7j1ylMZcuPXF4sgt9JgyNctMHst_kMTvylRbuKb0b0pM56R4.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=SayvRpACgmQQ7kNvwFfi5zM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDEzNzg0MTE1NTExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjoxMzMwMTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3OwBk0UIvTK-gY0On8rkJLbMlzZIDWCKa291B4GUWYrA&amp;oe=69DC202F</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2649\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-42264\" FBFirstSegmentRange=\"913-81630\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"81631-165356\" FBPrefetchSegmentRange=\"913-81630\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"841154109017581a\" bandwidth=\"166796\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"166796\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"335441\" FBPaqMos=\"94.35\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPbkhnvk7hzIgpIb5dJeU0yaS364t2TnHyFaiQogJ5Sb4KkXt8whU9jVpyYTx_UkUDTSO_1p5EIDsGHzmSGKs7pyxYJBA4piCgyo90.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=UONuYdxiaYsQ7kNvwF7NTVH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDEzNzg0MTE1NTExLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjoxNjcyNTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af14RndkTVAbpo2hAHtNOPUcpxW1UGM12sdUiOQ0stXmMw&amp;oe=69DC1B51</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2787\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-54529\" FBFirstSegmentRange=\"913-104926\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"104927-207687\" FBPrefetchSegmentRange=\"913-104926\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "number_of_qualities": 8,
                "video_codec": "av01.0.00M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "36818859777",
                  "id": "36818859777",
                  "username": "_sadhana_off_",
                  "full_name": "Sadhana Namidass",
                  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658043634_18088106555227778_711827866841328521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NjAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=sC6SAfK4AlgQ7kNvwHaX7pL&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GPLyOCeCPuJ9CUNAAIkrTWis6_AJbmNDAQAB1501500j-ccb7-5&oh=00_Af3CwpcBm_PAKGZ6yboOKkOLWjs0sEcUbA1nVV5l8GBUrQ&oe=69DC408B&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3yNniAcmA",
                "device_timestamp": 1775653339286703,
                "enable_media_notes_production": true,
                "filter_type": 810,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOJS4O3tO7-FrB7h8sbls55jJpbgXM-e_gESqtWDjRiJzgYQP9OTTlg3HKwyFIanULCkzR2U6n4TiUn8XRh99gWo_boaLDEpo13sA8.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=9bU5wAoPIrkQ7kNvwETdQGj&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0MTM3ODQxMTU1MTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=e2b10f1013f002b8&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80QzQ2M0UwRUU0RTAwNjFDOEZDNjkxMjA4RjQzNzM5M192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzgwNEI1QzFBRDA1QjI3MEE2RTg1NDI3OTkyM0FBMkIxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbu5K3G0ZblPxUCKAJDMywXQDAIcrAgxJwYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2Ar0ozD3sPUnElwW4o_zASLJS9OvSmVaWtnWu5cMxDWQ&oe=69D8532A",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      5288,
                      10577
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/669855753_1635148147696919_3730890493730747042_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc4MzI0Mjg3MzQ1NzAyNA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=og-8Spyn5rwQ7kNvwFkUHim&_nc_oc=AdoX1RAedtTbLWYLmHdKT9HuoqAHnWJsVAjPSq8dMbuQ_0XozmK15av5Ybe6CtPiVus&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af2FqwCLElBP_6xY6XtDVY5kUQj5DN87WKL7CLXmVOBM7A&oe=69DC4562",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/669855753_1635148147696919_3730890493730747042_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc4MzI0Mjg3MzQ1NzAyNA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=og-8Spyn5rwQ7kNvwFkUHim&_nc_oc=AdoX1RAedtTbLWYLmHdKT9HuoqAHnWJsVAjPSq8dMbuQ_0XozmK15av5Ybe6CtPiVus&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af2FqwCLElBP_6xY6XtDVY5kUQj5DN87WKL7CLXmVOBM7A&oe=69DC4562",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775653394,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870810105716795067_49492628331",
                "id": "3870810105716795067_49492628331",
                "disable_caption_and_comment": false,
                "fbid": 18100095628795639,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDgxMDEwNTcxNjc5NTA2Nw==.3",
                "integrity_review_decision": "pending",
                "pk": "3870810105716795067",
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
                        3317,
                        6634
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/658953883_956442893750979_6894961801744733374_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM4LnNkci5DMyJ9&_nc_ohc=izuLIJDjUnsQ7kNvwEPSh7C&_nc_oc=Ado0aevXfJiupQOiAyEi0CxViNzhiaxAChdW97HHHuENkgqS-O1qXW2PwvNJuzDY3jo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af3QHm9hx0IB6tFZ5DsunPCsBoxdR3K58H47ED6i01pz0w&oe=69DC4EDC",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        3317,
                        6634
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/658953883_956442893750979_6894961801744733374_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM4LnNkci5DMyJ9&_nc_ohc=izuLIJDjUnsQ7kNvwEPSh7C&_nc_oc=Ado0aevXfJiupQOiAyEi0CxViNzhiaxAChdW97HHHuENkgqS-O1qXW2PwvNJuzDY3jo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af3QHm9hx0IB6tFZ5DsunPCsBoxdR3K58H47ED6i01pz0w&oe=69DC4EDC",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        3317,
                        6634
                      ],
                      "height": 1138,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/661900114_1633721564842645_3393832525482036398_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxMDEwNTcxNjc5NTA2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM4LnNkci5DMyJ9&_nc_ohc=v0-06liNPJYQ7kNvwFSz22Y&_nc_oc=AdojAOh7UcyaCEehPfaMhJXjAWZWVdoGq7SyokZiRSxlHtf7sxSTmV-oEIQ6C6yPlZE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af1NWnPuuRo8hlpoiHMOCv6K9C5eXhLxY_nb5Ib_TDpNwg&oe=69DC3D18",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 341,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/656749815_1268209472044572_5724811173387226569_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=3VsEc8NfUTAQ7kNvwFMbjAh&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af0_J9ACtbhS-sdb2Qwuzq6MEF8bESvVDruQlX9H6a-N6Q&oe=69DC4553&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.1011047619047619,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 10.616
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1088,
                "original_height": 1936,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYzQ2YTgyZDEzNGYxNDFjMmJkZTMxZGIyYzI2N2Y1NTEzODcwODEwMTA1NzE2Nzk1MDY3Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkzNzk5OXwzODcwODEwMTA1NzE2Nzk1MDY3fDMwMDA5MzA1OTIwfGNkZWM5ZmI1MTIwNzE5YWZiZTYzMWZkZjU4NTliMzE5ODYzOTdlNWNlY2U0NTgzZTI5N2MzOTYzZDUxMmJjNTYifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "en",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775656516,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "is_artist_pick": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "clips",
                "subscribe_cta_visible": false,
                "creative_config": {
                  "capture_type": "clips_v2",
                  "face_effect_id": null,
                  "failure_reason": null,
                  "attribution_user": null,
                  "creation_tool_info": [
                    {
                      "camera_tool": 97,
                      "duration_selector_seconds": 0,
                      "speed_selector": 0.0,
                      "color_filters": "",
                      "appearance_effect": 0,
                      "timer_selector_seconds": 0,
                      "magic_cut_start_time": 0.0,
                      "magic_cut_end_time": 0.0,
                      "effect_filter_name": ""
                    }
                  ],
                  "effect_configs": null,
                  "effect_preview": null,
                  "gen_ai_tool_info": null
                },
                "is_cutout_sticker_allowed": true,
                "cutout_sticker_info": [],
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "media_ui_attributions_data": [],
                "media_ui_attributions_data_v2": [],
                "creator_product_link_infos": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 0,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 25,
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
                    "best_audio_cluster_id": "1050324367047294"
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
                  "music_canonical_id": "18465445630064348",
                  "music_info": {
                    "music_canonical_id": 18465445630064348,
                    "music_asset_info": {
                      "allows_saving": false,
                      "artist_id": "3516181498639319",
                      "audio_asset_id": "3885964585042787",
                      "audio_cluster_id": "1298312681390055",
                      "cover_artwork_thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/657653324_71060886071030_6786091090726164685_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=zvV2MJGx-noQ7kNvwEcHt91&_nc_oc=AdpfnhoeF9WL1HJd1Q-JyHTdpPwRfPpRVu_K5PpuPZExtPAhm4oZcDZVGLt7tc1yqvw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a39b&oh=00_Af3Y8slexDeVwb-O76mmYQ2o9ZdFuQUv-4ZmXiagN_R3_g&oe=69DC37D8",
                      "cover_artwork_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/657653324_71060886071030_6786091090726164685_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=zvV2MJGx-noQ7kNvwEcHt91&_nc_oc=AdpfnhoeF9WL1HJd1Q-JyHTdpPwRfPpRVu_K5PpuPZExtPAhm4oZcDZVGLt7tc1yqvw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a39b&oh=00_Af3Y8slexDeVwb-O76mmYQ2o9ZdFuQUv-4ZmXiagN_R3_g&oe=69DC37D8",
                      "dark_message": null,
                      "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT76S\"><Period id=\"0\" duration=\"PT76S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1665388408148256a\" bandwidth=\"59669\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"59669\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPTOMId46wyszeKiJD0qSRTT1XL5TfTXg2frROkOv_JEwCZTVr59xRYjyDu_jzRPDqdxhcybdfVg_JcRePlhl0l.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=QNWOCYWQ9z8Q7kNvwFXeFDO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5NjMxODMxODI5MDI0NzIsImFzc2V0X2FnZV9kYXlzIjo5LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6NzYsImJpdHJhdGUiOjU5ODA2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1bAsHoqbbEHxa0RmavHpgr4locPy4EfXlHpPTHu1LQQQ&amp;oe=69DC4E2A</BaseURL><SegmentBase indexRange=\"824-1311\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                      "display_artist": "Teesa",
                      "duration_in_ms": 76000,
                      "fast_start_progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPTOMId46wyszeKiJD0qSRTT1XL5TfTXg2frROkOv_JEwCZTVr59xRYjyDu_jzRPDqdxhcybdfVg_JcRePlhl0l.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=QNWOCYWQ9z8Q7kNvwFXeFDO&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NjMxODMxODI5MDI0NzIsImFzc2V0X2FnZV9kYXlzIjo5LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=a654ba3d7693083a&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR0lPV1NkLW5OMEZ4RlFEQUJEV3FVbEpzMXBJYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkNPD99GAtgMVAigCQzMsF0BTAAAAAAAAGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af2IO5c-sJoCe1_vsK9l4IX9c0YXoxgj5b7YhqtukrgZMg&oe=69DC4E2A",
                      "has_lyrics": false,
                      "highlight_start_times_in_ms": [
                        1500,
                        37000
                      ],
                      "id": "3885964585042787",
                      "ig_username": "teesadagostino",
                      "is_eligible_for_audio_effects": true,
                      "is_eligible_for_vinyl_sticker": true,
                      "is_explicit": false,
                      "licensed_music_subtype": "DEFAULT",
                      "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPTOMId46wyszeKiJD0qSRTT1XL5TfTXg2frROkOv_JEwCZTVr59xRYjyDu_jzRPDqdxhcybdfVg_JcRePlhl0l.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=QNWOCYWQ9z8Q7kNvwFXeFDO&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NjMxODMxODI5MDI0NzIsImFzc2V0X2FnZV9kYXlzIjo5LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=a654ba3d7693083a&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR0lPV1NkLW5OMEZ4RlFEQUJEV3FVbEpzMXBJYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkNPD99GAtgMVAigCQzMsF0BTAAAAAAAAGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af2IO5c-sJoCe1_vsK9l4IX9c0YXoxgj5b7YhqtukrgZMg&oe=69DC4E2A",
                      "reactive_audio_download_url": null,
                      "sanitized_title": null,
                      "song_monetization_info": null,
                      "subtitle": "",
                      "title": "Where Roses Bloom (Voice Memo Clip)",
                      "web_30s_preview_download_url": null,
                      "lyrics": null,
                      "spotify_track_metadata": null,
                      "related_audios": null
                    },
                    "music_consumption_info": {
                      "allow_media_creation_with_music": true,
                      "music_creation_restriction_reason": null,
                      "audio_asset_start_time_in_ms": 153,
                      "derived_content_start_time_in_composition_in_ms": 0,
                      "contains_lyrics": null,
                      "derived_content_id": null,
                      "display_labels": null,
                      "formatted_clips_media_count": null,
                      "is_bookmarked": false,
                      "is_trending_in_clips": false,
                      "overlap_duration_in_ms": 10581,
                      "placeholder_profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=HMeNVRbt-xsQ7kNvwEVy9wE&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4AAAAA&ccb=7-5&oh=00_Af0ADakOptAaAs_rYwsrFClfvib2kpqFr1HWfx1F13ortA&oe=69DC253D&_nc_sid=472314",
                      "should_allow_music_editing": false,
                      "should_mute_audio": false,
                      "should_mute_audio_reason": "",
                      "should_mute_audio_reason_type": null,
                      "should_render_soundwave": false,
                      "trend_rank": null,
                      "previous_trend_rank": null,
                      "ig_artist": {
                        "strong_id__": "8580251814",
                        "pk": 8580251814,
                        "pk_id": "8580251814",
                        "id": "8580251814",
                        "username": "teesadagostino",
                        "full_name": "Teesa (tee•suh)",
                        "is_private": false,
                        "is_verified": false,
                        "profile_pic_id": "3170850935144464423_8580251814",
                        "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.2885-19/367758274_619047687074111_4100869933534163626_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40NDIuYzIifQ&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=G80peCsjWCEQ7kNvwFqbi0d&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMKL6xU-sXxFBTMCAKoyYip6N_k4bkULAAAB1501500j-ccb7-5&oh=00_Af2SvD-uqXB0NsvqiOmiLNgn6Mm0ZNPmRcKtSHFBTpl1xg&oe=69DC50B7&_nc_sid=472314"
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
                "like_count": 1036,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18100099279795639",
                  "bit_flags": 0,
                  "created_at": 1775656520,
                  "created_at_utc": 1775656520,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18100099279795639",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870810105716795067,
                  "status": "Active",
                  "type": 1,
                  "user_id": 49492628331,
                  "text": "Together ❤️\n#cute #love #chippitwins #animation #comfort",
                  "user": {
                    "strong_id__": "49492628331",
                    "pk": 49492628331,
                    "pk_id": "49492628331",
                    "id": "49492628331",
                    "is_unpublished": false,
                    "fbid_v2": 17841449569936578,
                    "username": "chippi.twins",
                    "full_name": "Chippi Twins",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3203119907907282501_49492628331",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/384173687_1488772278587269_5013767750424726005_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=WxwCtRt2mz4Q7kNvwF0fgu3&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GHcG5haFD9HOB0oFAPUJYHY0e5RFbkULAAAB1501500j-ccb7-5&oh=00_Af29Jf7QzPOwkd5O-RpmgfhmPB0-0WrGjX7z8kGWzx_jhg&oe=69DC331B&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 16,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 10613,
                "ig_play_count": 10613,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 10.611000061035156,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 522142,
                    "height": 1280,
                    "id": "1518674963309925v",
                    "type": 101,
                    "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQNvzXeTXXde_bV0GM3pLVRvdRtZgF1imb8FBBLruxGwdHRgHI3YbdBuk4UT2u_-c814pe7kUFwzAw7INIGQPj9EdCiC1fss9MyZKk0.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=wAqu_5nT6mwQ7kNvwFTO7ze&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzE2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNjk0MjAwNjg2NTIzMzIsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=aba36e1a2161c47f&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NDQ3MERERTYwRjhFNEY0MDA0RDY3MzAwNDQzQkFCRl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzNFNDZCNjhCRjFBMTY4RkYzODBCODU5NUMyNDcyOEFBX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbYlOrH1oKZQBUCKAJDMywXQCUU_fO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2ZFXwggIcReHLdIgAMd7pg4gH9uRYMObzJMQ9STLPiLw&oe=69D84271",
                    "url_expiration_timestamp_us": null,
                    "width": 716,
                    "fallback": null
                  },
                  {
                    "bandwidth": 522142,
                    "height": 1280,
                    "id": "1518674963309925v",
                    "type": 102,
                    "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQNvzXeTXXde_bV0GM3pLVRvdRtZgF1imb8FBBLruxGwdHRgHI3YbdBuk4UT2u_-c814pe7kUFwzAw7INIGQPj9EdCiC1fss9MyZKk0.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=wAqu_5nT6mwQ7kNvwFTO7ze&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzE2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNjk0MjAwNjg2NTIzMzIsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=aba36e1a2161c47f&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NDQ3MERERTYwRjhFNEY0MDA0RDY3MzAwNDQzQkFCRl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzNFNDZCNjhCRjFBMTY4RkYzODBCODU5NUMyNDcyOEFBX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbYlOrH1oKZQBUCKAJDMywXQCUU_fO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2ZFXwggIcReHLdIgAMd7pg4gH9uRYMObzJMQ9STLPiLw&oe=69D84271",
                    "url_expiration_timestamp_us": null,
                    "width": 716,
                    "fallback": null
                  }
                ],
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT10.611519S\" FBManifestTimestamp=\"1775657938\" FBManifestIdentifier=\"FqSPs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZhq7ouP+Tye8C+rutu9mgtgOCipj3m6HGA+TVkP2/iMMEsrLp9cGU4wSMs5vywOfJBYSEqcyl8vgGzOTe0sTSpwwiGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT10.611519S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.6\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1273380490843506v\" bandwidth=\"126266\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"21760:21659\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"166383\" FBPlaybackResolutionMos=\"0:100,360:84.3,480:79.5,720:75,1080:70.5,1088:71.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.2,480:96.8,720:96.3,1080:95.3\" FBAbrPolicyTags=\"\" width=\"716\" height=\"1280\" frameRate=\"12288/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN98VRB-dKofhqG9hg7Uu6xlSkh4yRLuZJuv3CKsHko4AdrXEQt0K9KKXYp7P_FuRsL13KJqXIusAyqZ1K_Id92MB7sN4S3P_xqEE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=H81FbeS4xQIQ7kNvwHY420y&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA2OTQyMDA2ODY1MjMzMiwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMCwiYml0cmF0ZSI6MTI2MjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af059ZnaXKUBwm-YgoL9cTSBZjhV9_w6_qRUC3afTyaBJA&amp;oe=69DC2E3C</BaseURL><SegmentBase indexRange=\"842-909\" timescale=\"12288\" FBMinimumPrefetchRange=\"910-37448\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"910-48640\" FBFirstSegmentRange=\"910-69971\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"69972-151561\" FBPrefetchSegmentRange=\"910-69971\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"1569681817431238v\" bandwidth=\"326163\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"21760:21659\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"429788\" FBPlaybackResolutionMos=\"0:100,360:90.1,480:86.5,720:81.1,1080:75.1,1088:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.07,480:98.04,720:98.17,1080:97.7\" FBAbrPolicyTags=\"\" width=\"716\" height=\"1280\" frameRate=\"12288/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPgI272XSskMiZmkbh9Y-Q0HJO9LJdLSZ7c6zp2LLA83oDEFqkJC2c8GjB3L15q5xIVZ9JHgOcD0IeFvq2kNnoBqRzc6Dv3LAMaqUM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=_P-UcQKLH9EQ7kNvwHT_F7y&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA2OTQyMDA2ODY1MjMzMiwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMCwiYml0cmF0ZSI6MzI2MTYzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0pyiHJanAEawZkDYrUX1-td6mk8AZV9CBu5kns5NvxLA&amp;oe=69DC1E7F</BaseURL><SegmentBase indexRange=\"842-909\" timescale=\"12288\" FBMinimumPrefetchRange=\"910-90757\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"910-117126\" FBFirstSegmentRange=\"910-164062\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"164063-389618\" FBPrefetchSegmentRange=\"910-164062\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"963733949361917v\" bandwidth=\"660968\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"21760:21659\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"870964\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:89.8,720:84.9,1080:77.7,1088:78.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.58,480:98.86,720:99.267,1080:99.11\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"716\" height=\"1280\" frameRate=\"12288/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP4o-DYvlTnM_CmYm0s8PF1C10v_E5dTC2cImkxzlVfuKsBkJPfjq6UJ4G3vrtBt5w9Wkm1BWu5rVucIxzhKzbv0sJbfwdtfOtSAOU.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=fXNPSu6pACQQ7kNvwEDqECt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA2OTQyMDA2ODY1MjMzMiwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMCwiYml0cmF0ZSI6NjYwOTY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1atKviH5dbRLrXaZcqgLFsvo9f__eDqeWKEav98sB5Jw&amp;oe=69DC4FC8</BaseURL><SegmentBase indexRange=\"842-909\" timescale=\"12288\" FBMinimumPrefetchRange=\"910-149234\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"910-243506\" FBFirstSegmentRange=\"910-328803\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"328804-786112\" FBPrefetchSegmentRange=\"910-328803\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-841\"/></SegmentBase></Representation><Representation id=\"808298349009431v\" bandwidth=\"1632153\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"2150702\" FBPlaybackResolutionMos=\"0:100,360:94.5,480:92.7,720:89.1,1080:84.8,1088:85.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.099,480:99.51,720:99.974,1080:100\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1088\" height=\"1936\" frameRate=\"12288/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMtqNI3mPhq1yR5ZZ2ZrkLTI4KQ55NlGymVi3AJ1Sv7WYlamqZyLX-kqfHI4HeRPwaOUhnMs5oGYSaIECgDR9t83y7S7PJQgHMmL-w.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=imrougEBNPYQ7kNvwFdSw5h&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA2OTQyMDA2ODY1MjMzMiwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMCwiYml0cmF0ZSI6MTYzMjE1MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2nZwxMcNGJ8bWd1CMAkhfP1x5WCfD0Wu7UaBEFv7FqaQ&amp;oe=69DC4D01</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"12288\" FBMinimumPrefetchRange=\"894-288955\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-655239\" FBFirstSegmentRange=\"894-926772\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"926773-1973986\" FBPrefetchSegmentRange=\"894-926772\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1954696202100994a\" bandwidth=\"37353\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"37353\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"50451\" FBPaqMos=\"87.86\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO0zkV_DSoKzi28m_vzhCmBhlobEpC4ZV89wLh4lP3hvYuSZOHg_LfC1ny2tdEH4XCNp1luTmcmUrYIq7Ke6P1f3K4RF1_T5t3ZmtI.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=GFgRhWJYV6EQ7kNvwGy1Nbs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDY5NDIwMDY4NjUyMzMyLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEwLCJiaXRyYXRlIjozODAzNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af00ew9rHrNCOmnLoVWbddn16WH5xJsJzO-4hkiWZ-466g&amp;oe=69DC237F</BaseURL><SegmentBase indexRange=\"837-904\" timescale=\"44100\" FBMinimumPrefetchRange=\"905-1669\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"905-12238\" FBFirstSegmentRange=\"905-23211\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"23212-46125\" FBPrefetchSegmentRange=\"905-23211\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"3464879590332710a\" bandwidth=\"65944\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"65944\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"88376\" FBPaqMos=\"91.81\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOfi5K4D1p30p5OzVIHlLgdVGKG5kI1HcQswyQyywdFuLfOKKlczqoGFI30tGMxiex02wm-AzRx1YZGwfQ5l8xIwqX-AeoUluBtIj8.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=dSJ6JLDOT1sQ7kNvwF9CUqZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDY5NDIwMDY4NjUyMzMyLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEwLCJiaXRyYXRlIjo2NjYyNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1yjKYbYEAUBoIGFf1dSAQv9eqz6ozK64Sx-3rvgU76cw&amp;oe=69DC3E56</BaseURL><SegmentBase indexRange=\"838-905\" timescale=\"44100\" FBMinimumPrefetchRange=\"906-1951\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-22179\" FBFirstSegmentRange=\"906-41252\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"41253-81500\" FBPrefetchSegmentRange=\"906-41252\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1343955654225049a\" bandwidth=\"108219\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108219\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"144447\" FBPaqMos=\"93.71\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN5F5BjBhVmiAyM7i-1ixcTVwGCaycO4lwWZErHxWpEpdNZcndpaxUpugQUdJZ0avYq-WQnq6b1v0uEFu0J7DvQc3i8uDBStHz3Mk.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=DJwHaMzBGQwQ7kNvwFYZ_Ca&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDY5NDIwMDY4NjUyMzMyLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEwLCJiaXRyYXRlIjoxMDg4OTgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3X8WEzARJnq8AtptahzX1WJAz6FuHaNeT2Vud9Vjcryg&amp;oe=69DC3507</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-1954\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-33058\" FBFirstSegmentRange=\"901-69949\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"69950-134003\" FBPrefetchSegmentRange=\"901-69949\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"998927242560129a\" bandwidth=\"124014\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"124014\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"165398\" FBPaqMos=\"94.10\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNi9iz5YbvqTVMBIrSZHAj9DRbznv2NP9qUKvTdX2vEfp3utGJ_FZfkBaE_TGl91bD0XoGuHlhUYs8p2N69pZqhx2CQiWmma3QS58w.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=W89y_6pLlPIQ7kNvwFlBggc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDY5NDIwMDY4NjUyMzMyLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEwLCJiaXRyYXRlIjoxMjQ2OTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=uhYHemx66t8XMAQKCbyI7A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Eqa8wFrCGce4U39030BC9itqIxyq4w7W4e19C49RC3A&amp;oe=69DC30D9</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-1954\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-38872\" FBFirstSegmentRange=\"901-81131\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"81132-153001\" FBPrefetchSegmentRange=\"901-81131\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "number_of_qualities": 4,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "49492628331",
                  "id": "49492628331",
                  "username": "chippi.twins",
                  "full_name": "Chippi Twins",
                  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/384173687_1488772278587269_5013767750424726005_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGmNzVM1EV2n1o5WP6twGxfeDH7DsqNPbOHDRJYOx3mmmppCd1DmnsVECa2JIMlSmk&_nc_ohc=WxwCtRt2mz4Q7kNvwF0fgu3&_nc_gid=uhYHemx66t8XMAQKCbyI7A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GHcG5haFD9HOB0oFAPUJYHY0e5RFbkULAAAB1501500j-ccb7-5&oh=00_Af29Jf7QzPOwkd5O-RpmgfhmPB0-0WrGjX7z8kGWzx_jhg&oe=69DC331B&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW34UhgPea7",
                "device_timestamp": 1775656516,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQNvzXeTXXde_bV0GM3pLVRvdRtZgF1imb8FBBLruxGwdHRgHI3YbdBuk4UT2u_-c814pe7kUFwzAw7INIGQPj9EdCiC1fss9MyZKk0.mp4?_nc_cat=104&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=wAqu_5nT6mwQ7kNvwFTO7ze&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzE2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNjk0MjAwNjg2NTIzMzIsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=aba36e1a2161c47f&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NDQ3MERERTYwRjhFNEY0MDA0RDY3MzAwNDQzQkFCRl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzNFNDZCNjhCRjFBMTY4RkYzODBCODU5NUMyNDcyOEFBX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbYlOrH1oKZQBUCKAJDMywXQCUU_fO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2ZFXwggIcReHLdIgAMd7pg4gH9uRYMObzJMQ9STLPiLw&oe=69D84271",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      3317,
                      6634
                    ],
                    "height": 1138,
                    "scans_profile": "e15",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/661900114_1633721564842645_3393832525482036398_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxMDEwNTcxNjc5NTA2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM4LnNkci5DMyJ9&_nc_ohc=v0-06liNPJYQ7kNvwFSz22Y&_nc_oc=AdojAOh7UcyaCEehPfaMhJXjAWZWVdoGq7SyokZiRSxlHtf7sxSTmV-oEIQ6C6yPlZE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af1NWnPuuRo8hlpoiHMOCv6K9C5eXhLxY_nb5Ib_TDpNwg&oe=69DC3D18",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/661900114_1633721564842645_3393832525482036398_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxMDEwNTcxNjc5NTA2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM4LnNkci5DMyJ9&_nc_ohc=v0-06liNPJYQ7kNvwFSz22Y&_nc_oc=AdojAOh7UcyaCEehPfaMhJXjAWZWVdoGq7SyokZiRSxlHtf7sxSTmV-oEIQ6C6yPlZE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=uhYHemx66t8XMAQKCbyI7A&_nc_ss=7a3ba&oh=00_Af1NWnPuuRo8hlpoiHMOCv6K9C5eXhLxY_nb5Ib_TDpNwg&oe=69DC3D18",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775656516,
                "sponsor_tags": []
              }
            }
          ]
        }
      }
    ],
    "more_available": true,
    "next_max_id": "851bb26850a941c5ac8d3dd9ef9fe87a",
    "next_page": 1,
    "next_media_ids": [],
    "auto_load_more_enabled": true,
    "status": "ok"
  },
  "next_page_id": "WyI4NTFiYjI2ODUwYTk0MWM1YWM4ZDNkZDllZjlmZTg3YSIsW10sMV0="
}
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
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/660767621_822966907072261_1165447814785867142_n.jpg?_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=WId066BQfAwQ7kNvwEPHJ27&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af1Zyi12vCdDL38PQYQIl9u740C0onMKqhTvfOLSNwO_Zg&oe=69DC2A16&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.4135238095238095,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 43.42
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTYwYjdlNjkyY2VmNDA2ZGE1YTczY2UwZGY2YTY0YmMzODcwNzY4NDQzODUwNTk5NzA2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyOTI5MHwzODcwNzY4NDQzODUwNTk5NzA2fDMwMDA5MzA1OTIwfDJiYTE2OTU5OWJlMDYxMjk3MTk2YTVhMDZkMjAxNmFmZjQyMTQ2Y2RhNzZiOGUyMjRjYWQzMTNiYzZjYTcyODQifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": true,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775651643,
                "photo_of_you": false,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "is_artist_pick": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "clips",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "cutout_sticker_info": [],
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "media_ui_attributions_data": [],
                "media_ui_attributions_data_v2": [],
                "creator_product_link_infos": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 120,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 52,
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
                    "best_audio_cluster_id": "975187385466327"
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
                  "music_canonical_id": "18580431622046223",
                  "music_info": null,
                  "nux_info": null,
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": 34763066076641185,
                    "attributed_custom_audio_asset_id": null,
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": false,
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT43.421314S\" FBManifestTimestamp=\"1775657931\" FBManifestIdentifier=\"FpaPs50NKRbgw5G4wdTUDyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT43.421314S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"4408294496153840a\" bandwidth=\"58514\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"58514\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQNugpvojNGoGmtdqTge3v_cZB3f_7x1Icg2Q0Ln8rNqL936bOokfBB52gtoSadnp7VSRxczRCY3xoC0yw6ailbnaFVzIrjXvd5WuHU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=5XLe3QiXWwoQ7kNvwHVSnNV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3ODU2ODE5NzgzNjg2MjUxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQzLCJiaXRyYXRlIjo1ODcxOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2LgrpWjLbVT0Li6vNjY1DwE1Un9GlgcsziXSTEOekGcg&amp;oe=69D85A5B</BaseURL><SegmentBase indexRange=\"824-1119\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 43000,
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
                    "original_media_id": 3870768443850599706,
                    "progressive_download_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m69/AQOlOFCamVeNPWGc2q223w944bCT0emFqWl7ihP0ltdphjy6x-PME1DR2Tuo85KzTPQm41GH3EQb8wdsC8NS0ZV3.mp4?strext=1&_nc_cat=109&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=LeqrzJGpWKwQ7kNvwHrRbBi&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc4NTY4MTk3ODM2ODYyNTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0qnWxvuYCHceU8Foh2x0eW-4bmM69eggyrax_5UOCfFQ&oe=69DC3B71",
                    "should_mute_audio": false,
                    "time_created": 1775651596,
                    "trend_rank": null,
                    "previous_trend_rank": null,
                    "overlap_duration_in_ms": 0,
                    "audio_asset_start_time_in_ms": 0,
                    "derived_content_start_time_in_composition_in_ms": 0,
                    "ig_artist": {
                      "strong_id__": "80471414250",
                      "pk": 80471414250,
                      "pk_id": "80471414250",
                      "id": "80471414250",
                      "username": "ai_assistant_pari",
                      "full_name": "Jalpesh Rathod | AI Assistant Pari",
                      "is_private": false,
                      "is_verified": false,
                      "profile_pic_id": "3825045202755457044_80471414250",
                      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/627702375_17844036975686251_7526041391374837960_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=Fj4JM5XBqP0Q7kNvwGYrV5k&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GGf6aSVrckudDmU-AMioyFHF3nFobmNDAQAB1501500j-ccb7-5&oh=00_Af3xhRg1kFWpHRee3wtMKmrEiwRgDgAVxpR93QcTcQagBA&oe=69DC500E&_nc_sid=472314"
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
                "like_count": 697,
                "fb_like_count": 0,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "17864210508616995",
                  "bit_flags": 0,
                  "created_at": 1775651595,
                  "created_at_utc": 1775651595,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "17864210508616995",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870768443850599706,
                  "status": "Active",
                  "type": 1,
                  "user_id": 80471414250,
                  "has_translation": true,
                  "text": "બસ એક અમારી જાત ના મળી ❤️‍🩹🥀\n.\n.\n#cast \n#love \n#heartbroken \n#pari \n#instagood",
                  "user": {
                    "strong_id__": "80471414250",
                    "pk": 80471414250,
                    "pk_id": "80471414250",
                    "id": "80471414250",
                    "is_unpublished": false,
                    "fbid_v2": 17841480587508926,
                    "username": "ai_assistant_pari",
                    "full_name": "Jalpesh Rathod | AI Assistant Pari",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3825045202755457044_80471414250",
                    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/627702375_17844036975686251_7526041391374837960_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=Fj4JM5XBqP0Q7kNvwGYrV5k&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GGf6aSVrckudDmU-AMioyFHF3nFobmNDAQAB1501500j-ccb7-5&oh=00_Af3xhRg1kFWpHRee3wtMKmrEiwRgDgAVxpR93QcTcQagBA&oe=69DC500E&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 30,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "fb_comment_count": 0,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 5635,
                "ig_play_count": 5533,
                "fb_play_count": 102,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "is_feedback_aggregated": true,
                  "unified_feedback_enabled": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 43.41899871826172,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 737683,
                    "height": 1280,
                    "id": "1570975618077049v",
                    "type": 101,
                    "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQNAv6nilKfPdcv0CqY6Z5MkVQkqGt4SqWo3FxK41OL45SSV_MFvhtFeGTTqORGiIS-YHgCKuQ6tUCjBtVvsuXtIjjB2UHll-PpIAdg.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=NONHKuUjZCAQ7kNvwFI7s_Y&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NTY4MTk3ODM2ODYyNTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=808573d2ae21d2d9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9FMjQ0MzY0NDNGMDlFRDRCRjMxMEE1OTA5QzBDMTlBQV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzRFNEIyNEM1NTU3MjJDOTZCOEM3QUFCQUY0QjBEMTkxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbW4bKA26u4PxUCKAJDMywXQEWzMzMzMzMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2kbJAOsXsoTWBXskNsrfcQJv_PMaQZdFq5gVD_81etcQ&oe=69D8551D",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  },
                  {
                    "bandwidth": 737683,
                    "height": 1280,
                    "id": "1570975618077049v",
                    "type": 102,
                    "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQNAv6nilKfPdcv0CqY6Z5MkVQkqGt4SqWo3FxK41OL45SSV_MFvhtFeGTTqORGiIS-YHgCKuQ6tUCjBtVvsuXtIjjB2UHll-PpIAdg.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=NONHKuUjZCAQ7kNvwFI7s_Y&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NTY4MTk3ODM2ODYyNTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=808573d2ae21d2d9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9FMjQ0MzY0NDNGMDlFRDRCRjMxMEE1OTA5QzBDMTlBQV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzRFNEIyNEM1NTU3MjJDOTZCOEM3QUFCQUY0QjBEMTkxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbW4bKA26u4PxUCKAJDMywXQEWzMzMzMzMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2kbJAOsXsoTWBXskNsrfcQJv_PMaQZdFq5gVD_81etcQ&oe=69D8551D",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT43.419865S\" FBManifestTimestamp=\"1775657931\" FBManifestIdentifier=\"FpaPs50NGA9yMmF2MS1yMWdlbjJ2cDkZxp7Eh9zqpeUCyrmvntSOsgP0z4/B6+TDBOaOrJb+/vkErs39maybogWSlrPIg8ujBdT6jsH1magFzPrl0oeYyAXM4bzv8b+ABsjAjZrLoqwG1JWsjJfKwwe0i8+j4qeSCCIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT43.419865S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:80\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1274966881465338v\" bandwidth=\"100161\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"543377\" FBPlaybackResolutionMos=\"0:100,360:75.5,480:71,720:66.3,1080:64.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:90.4,480:87.2,720:81,1080:73.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNRCJppz2F7_uH5WoO5gJOCTsMrCu0KXPL1cNK5xGnYnpOxHDJpN1htFxc7dZvSs2PFZOcWwFtDkM6oEFf5OwHjALCJcEYRDJTRfmI.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=YcaXspdsW40Q7kNvwHEaXV_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6MTAwMTYxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af351J_VrAn2_Ymt1HSn65yc22hKViaM3m5etLD0LrRxGw&amp;oe=69DC44A4</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-13243\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-50247\" FBFirstSegmentRange=\"966-69386\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"69387-155225\" FBPrefetchSegmentRange=\"966-69386\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1485629666256265v\" bandwidth=\"182561\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"990398\" FBPlaybackResolutionMos=\"0:100,360:82.2,480:77.2,720:72.7,1080:70.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.7,480:91.6,720:87,1080:80.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMsq6o3qgANWBYBOiuGV-hQhrEjmw4kN6WV2NpsmNOP4ozVjh0h6mREeFCDV6YQ-ZwNnV7-_yxIYBq-4_S5gA8jvD1ljzP7_H5f0nA.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=FKpVpS-Ezu0Q7kNvwG8M_r6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6MTgyNTYxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0bpaWjR9zvV_sc2syzKdHmsqGFWHfz-mNG-tDTHBSjPA&amp;oe=69DC2782</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-20544\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-90434\" FBFirstSegmentRange=\"966-129525\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"129526-290774\" FBPrefetchSegmentRange=\"966-129525\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1689947475515494v\" bandwidth=\"257197\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"1395294\" FBPlaybackResolutionMos=\"0:100,360:85.4,480:80.8,720:75.8,1080:73.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.9,480:93.2,720:89.4,1080:83.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMOFZCiCZRQt5GzD3slgQNCEPFl0m_2rEtS3un1EfSKV30UPM42OUyxpMtyCczKL8yZqr2tZCeHbZag85ZytZE643D0HKW1JG1gA0w.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=ik6fq25xrHkQ7kNvwFiHnUc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6MjU3MTk3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3mi2AJiOHGUxh5Ly4AUQwdhumOcTSNDN7KPti5KV0noQ&amp;oe=69DC3181</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-25866\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-124970\" FBFirstSegmentRange=\"966-183395\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"183396-412622\" FBPrefetchSegmentRange=\"966-183395\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"954627917213285v\" bandwidth=\"343191\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"1861813\" FBPlaybackResolutionMos=\"0:100,360:87.6,480:83.5,720:78,1080:75.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.6,480:94.1,720:91,1080:85.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOzZlbfx0Lzt1P0-jxbqhg5cDDJTpMvgavjRG34soHYEMLTL78CewwWrSxIiDY5GIbx-vP6PfSh26gvky4-WQfIXq5a06sYnFvxRqY.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=BTNer1Er7TwQ7kNvwF1mtaZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6MzQzMTkxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0uhl3fD-3z73WFiLC5qUlLy0ZyvK-ZWcqHB0Q0Uw_EOA&amp;oe=69DC4964</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-30530\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-165245\" FBFirstSegmentRange=\"966-247192\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"247193-556843\" FBPrefetchSegmentRange=\"966-247192\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2118933805368682v\" bandwidth=\"436498\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"2368003\" FBPlaybackResolutionMos=\"0:100,360:89.1,480:85.4,720:80.2,1080:76.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:94.9,720:92.1,1080:87.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMwI3yKChGLXsTy0nvR6vq8jfqyRA9hO8qz4AsdvU9bdrhrFkj-kPbOpjEKEHob_wKEGUB8UcUm02ZVRNhKn90myIwOANY7dLo3aaE.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=zd0FHhjUTrAQ7kNvwGAj6K-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6NDM2NDk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af19hUXa6YhBQgN18RHVNZOfQSHV9H0rCpj7dQ1lTKutbA&amp;oe=69DC3861</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-34398\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-207917\" FBFirstSegmentRange=\"966-317387\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"317388-710262\" FBPrefetchSegmentRange=\"966-317387\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1566117901156006v\" bandwidth=\"642074\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"3483253\" FBPlaybackResolutionMos=\"0:100,360:91.4,480:88,720:83.5,1080:79.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.6,480:95.8,720:93.5,1080:89.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMfk7S6fwMShwmDFCz4Aq6lwYQRR7eLlBbvLZMylK9Z77_YpNUOdX7Jn9SlsDpdWDxvPfabTs_1KGSYmT-oY-SP9FeCUn3FoI41XZM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=UvvNPmKEzuoQ7kNvwE9Kx1r&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6NjQyMDc0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1trDKYh4z9a7hprpEK7JqgcjxniWdpw1V-mm6KTbaevg&amp;oe=69DC46E8</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-41225\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-299547\" FBFirstSegmentRange=\"966-471353\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"471354-1048833\" FBPrefetchSegmentRange=\"966-471353\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2292065437868762v\" bandwidth=\"897996\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"4871631\" FBPlaybackResolutionMos=\"0:100,360:92.8,480:89.9,720:85.7,1080:81.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:96.4,720:94.6,1080:91\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMDufMwyT3sHRgSp8aIuURThvpWeiIJPIl4PpXEEa1sCZH6rze3XRX_iApp20ATU-sCIQnxxQVjRheFQuzeri2iiVdIMVrfsZI-vrw.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=458hxHx1gcEQ7kNvwHiWw5F&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6ODk3OTk2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af03lzDiOnJceH6OJZgVOKtK-hQ5UGq_xR9qecEKCGdTYA&amp;oe=69DC4697</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-46355\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-411758\" FBFirstSegmentRange=\"966-671556\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"671557-1479289\" FBPrefetchSegmentRange=\"966-671556\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1482611463533399v\" bandwidth=\"1426915\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"7741017\" FBPlaybackResolutionMos=\"0:100,360:94.8,480:92.6,720:89.2,1080:86.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.4,480:97,720:95.9,1080:94.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNo4nZl-ApRGsXCx-03BT7QMmFOM-M0lCka7j5ACBYSNHvbk7mUPL6V7ZovSyiEQt7sRplzEwKPI8WCUFkeLmVLlEHNPEEb77Kf49Y.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=2oGhUvcFSSQQ7kNvwGejHRc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg1NjgxOTc4MzY4NjI1MSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MywiYml0cmF0ZSI6MTQyNjkxNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1FtMVMg1MEjSAjeldHP3XceMAg2jUyFIOEwvOIlOPA9w&amp;oe=69DC4836</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-62907\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-649750\" FBFirstSegmentRange=\"966-1087054\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1087055-2359909\" FBPrefetchSegmentRange=\"966-1087054\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1394163319145395a\" bandwidth=\"39395\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"39395\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"214791\" FBPaqMos=\"87.75\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOzcAkM3_GpeUBus5fKO02pCLjnCK4cag2F7SzvghVpnWA6sy_rNUTdWGPWFrkOrIhAZ_grtjOvjODVlPH612AVC4KVumJ8I1P4Kw0.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=5bflYm0WIekQ7kNvwGo7iGS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODU2ODE5NzgzNjg2MjUxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQzLCJiaXRyYXRlIjozOTU3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3NWVdijsrDVT0sisOtdeO67krwQ81kTBLgobWVWUfB8Q&amp;oe=69DC3BC4</BaseURL><SegmentBase indexRange=\"839-978\" timescale=\"44100\" FBMinimumPrefetchRange=\"979-2115\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"979-12021\" FBFirstSegmentRange=\"979-22941\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"22942-45264\" FBPrefetchSegmentRange=\"979-22941\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-838\"/></SegmentBase></Representation><Representation id=\"1495781082259114a\" bandwidth=\"71545\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71545\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"389284\" FBPaqMos=\"87.75\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP4wS4o4TZu7go9jITWv5dV6uWJCM3G_OhjE-94QQqLbR0fD0g4qPEzCefKEruUCl0obMH3VUHCSlkMhoZ-0CDaAyVyPlYMYG3tLNo.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=Ps9IYn3XOlwQ7kNvwF3t4nR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODU2ODE5NzgzNjg2MjUxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQzLCJiaXRyYXRlIjo3MTcyNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1kw912-25b12kEUIKp1IZLoJ9K7IASUoX7_WFyW6JlVA&amp;oe=69DC4BAE</BaseURL><SegmentBase indexRange=\"840-979\" timescale=\"44100\" FBMinimumPrefetchRange=\"980-2601\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-21071\" FBFirstSegmentRange=\"980-41445\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"41446-81901\" FBPrefetchSegmentRange=\"980-41445\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-839\"/></SegmentBase></Representation><Representation id=\"1786201092763684a\" bandwidth=\"96601\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"96601\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"525271\" FBPaqMos=\"92.76\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOFrD0OEEQLwM2q81Sz8WWB3Et6AY1eLl9Sb6pPwymxpHqDw_MZKxaBcEcIyYdldYra9ekH6YRW9JxgfHX6gt12cT0JS04bXOr_Mms.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=kgFLweErGjUQ7kNvwFlyCoU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODU2ODE5NzgzNjg2MjUxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQzLCJiaXRyYXRlIjo5Njc3OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af30rmv4pJb-eQiMQnz9Gd9Sb9-RgzHT9zgfTZET5FAHBw&amp;oe=69DC2F6B</BaseURL><SegmentBase indexRange=\"835-974\" timescale=\"44100\" FBMinimumPrefetchRange=\"975-2434\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-26641\" FBFirstSegmentRange=\"975-52956\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"52957-105620\" FBPrefetchSegmentRange=\"975-52956\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-834\"/></SegmentBase></Representation><Representation id=\"785701281001743a\" bandwidth=\"115121\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"115121\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"625792\" FBPaqMos=\"92.89\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPKQSfWvCKgc5YDjSsDAgGsJ9SfEIXnWQdaxtvGlfkF3D4biVQUVTalSPxNDWQ8fovMU4m7Q41kfEQa4ljShAJNHFA-Wy971JD0QLc.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=8yLuTc3_sjAQ7kNvwGTjh_4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODU2ODE5NzgzNjg2MjUxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQzLCJiaXRyYXRlIjoxMTUzMDAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af03P9EeiRDTLKvYetoZIWvMZJvmiMNAB5RK7hS8Jv5G7A&amp;oe=69DC1C26</BaseURL><SegmentBase indexRange=\"835-974\" timescale=\"44100\" FBMinimumPrefetchRange=\"975-2516\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-31268\" FBFirstSegmentRange=\"975-61317\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"61318-121695\" FBPrefetchSegmentRange=\"975-61317\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-834\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "80471414250",
                  "id": "80471414250",
                  "username": "ai_assistant_pari",
                  "full_name": "Jalpesh Rathod | AI Assistant Pari",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/627702375_17844036975686251_7526041391374837960_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=Fj4JM5XBqP0Q7kNvwGYrV5k&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GGf6aSVrckudDmU-AMioyFHF3nFobmNDAQAB1501500j-ccb7-5&oh=00_Af3xhRg1kFWpHRee3wtMKmrEiwRgDgAVxpR93QcTcQagBA&oe=69DC500E&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3u2Q3ga0a",
                "device_timestamp": 1775651555687062,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQNAv6nilKfPdcv0CqY6Z5MkVQkqGt4SqWo3FxK41OL45SSV_MFvhtFeGTTqORGiIS-YHgCKuQ6tUCjBtVvsuXtIjjB2UHll-PpIAdg.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=NONHKuUjZCAQ7kNvwFI7s_Y&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NTY4MTk3ODM2ODYyNTEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=808573d2ae21d2d9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9FMjQ0MzY0NDNGMDlFRDRCRjMxMEE1OTA5QzBDMTlBQV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzRFNEIyNEM1NTU3MjJDOTZCOEM3QUFCQUY0QjBEMTkxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbW4bKA26u4PxUCKAJDMywXQEWzMzMzMzMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2kbJAOsXsoTWBXskNsrfcQJv_PMaQZdFq5gVD_81etcQ&oe=69D8551D",
                "image_versions": [
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
                "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/657333707_1643455193521085_868122056204770385_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc2ODQ0Mzg1MDU5OTcwNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=PEnJtbrhYCQQ7kNvwGSbAho&_nc_oc=AdpwtAxUHAvrjqCMYIYSnHLCPJbc9vVlSDFLC3WXRYUq3wVGYAFJey6hsxPmJrG_r44&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af2DHf1hEx-TlR5ngmeriWJgG1PwE8qbsFrnbPVch-F0pw&oe=69DC4AD3",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775651643,
                "sponsor_tags": []
              }
            },
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
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1x_5X5L5tv4mnhDoWxXL6Y1_bYLkuxDLrUtKrr3sr8qQ&oe=69DC1EC3",
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
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af0ZgzGKhrvhK-UV5Sw_3r9pj9ZammbVNy1vUCwDCRfA-Q&oe=69DC1EC3",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1079,
                "original_height": 1101,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTYwYjdlNjkyY2VmNDA2ZGE1YTczY2UwZGY2YTY0YmMzODcwNzcxMDA3NDUxODcxODA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyOTM3M3wzODcwNzcxMDA3NDUxODcxODA1fDMwMDA5MzA1OTIwfDllZmQ1YzU2YWE1YjJjMGYwMmU4NzE3YzIyMGJmNmM4MjQyNGJjNDc2ZmVmY2Y5NTY1NzhmZWMzYzRmZGRhNTkifSwic2lnbmF0dXJlIjoiIn0=",
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
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": false,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 7,
                "like_count": 300,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18119849740714197",
                  "bit_flags": 0,
                  "created_at": 1775651899,
                  "created_at_utc": 1775651899,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18119849740714197",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870771007451871805,
                  "status": "Active",
                  "type": 1,
                  "user_id": 375121505,
                  "text": "Disney Princess irl",
                  "user": {
                    "strong_id__": "375121505",
                    "pk": 375121505,
                    "pk_id": "375121505",
                    "id": "375121505",
                    "is_unpublished": false,
                    "fbid_v2": 17841400525155861,
                    "username": "fallinginsociety",
                    "full_name": "FallingInSociety",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "1408922974837077103_375121505",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af1cMbybA6xItQQlvUAI56oe3zwfJKobX1o1BZKvjxLxIw&oe=69DC3771&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 5,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "375121505",
                  "id": "375121505",
                  "username": "fallinginsociety",
                  "full_name": "FallingInSociety",
                  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af1cMbybA6xItQQlvUAI56oe3zwfJKobX1o1BZKvjxLxIw&oe=69DC3771&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3vbkaDLo9",
                "device_timestamp": 1775651897,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      11766,
                      23532
                    ],
                    "height": 1101,
                    "scans_profile": "e35",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1x_5X5L5tv4mnhDoWxXL6Y1_bYLkuxDLrUtKrr3sr8qQ&oe=69DC1EC3",
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
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af0ZgzGKhrvhK-UV5Sw_3r9pj9ZammbVNy1vUCwDCRfA-Q&oe=69DC1EC3",
                    "width": 750,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1x_5X5L5tv4mnhDoWxXL6Y1_bYLkuxDLrUtKrr3sr8qQ&oe=69DC1EC3",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775651897,
                "sponsor_tags": [],
                "play_count": 0
              }
            }
          ]
        }
      },
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
                "strong_id__": "3870711225189699935_501243330",
                "id": "3870711225189699935_501243330",
                "fbid": 18095164141877817,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDcxMTIyNTE4OTY5OTkzNQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870711225189699935",
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
                        54433,
                        108867
                      ],
                      "height": 1820,
                      "scans_profile": "e35",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af0f2_JjkpOZFeVWEG_NaBVnmipbjsHwusoW5zQL299AHQ&oe=69DC2620",
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
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1Wnjg_g_thgiegfjZu-DQ63DUL6zSC-A-rnr6_L2ntpA&oe=69DC2620",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1365,
                "original_height": 1820,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTYwYjdlNjkyY2VmNDA2ZGE1YTczY2UwZGY2YTY0YmMzODcwNzExMjI1MTg5Njk5OTM1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyOTM3NHwzODcwNzExMjI1MTg5Njk5OTM1fDMwMDA5MzA1OTIwfDY0ZTE5NjQ3MTBiMjU3ZDI5NWU3NGQwYmUwYzI5MTE4YzVlZGUwNTdhNjczYTMyZTNiNjU3ODYyMmE5MDIzZjcifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": "licensed_music",
                  "music_canonical_id": "18123820021106092",
                  "pinned_media_ids": [],
                  "music_info": {
                    "music_canonical_id": 18123820021106092,
                    "music_asset_info": {
                      "allows_saving": false,
                      "artist_id": "347136506816046",
                      "audio_asset_id": "161539057732774",
                      "audio_cluster_id": "460214811397853",
                      "cover_artwork_thumbnail_uri": "https://scontent-dfw5-1.cdninstagram.com/v/t39.30808-6/426355524_7258746917539301_2553739156521727583_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=109&ccb=7-5&_nc_sid=2f2557&_nc_ohc=8XxpCsZY7UcQ7kNvwEqaiAD&_nc_oc=AdpSt57kclJw7OOIDwP-DjOP6X1w_Ek2nnEdj8Xq_2UlukygvD_Zijv2w53EJiC2AFw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a39b&oh=00_Af2IalY3761nrQAXF87zkuzblOyY_28mYMhCSafMAAtq6A&oe=69DC4AE7",
                      "cover_artwork_uri": "https://scontent-dfw5-1.cdninstagram.com/v/t39.30808-6/426355524_7258746917539301_2553739156521727583_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=109&ccb=7-5&_nc_sid=2f2557&_nc_ohc=8XxpCsZY7UcQ7kNvwEqaiAD&_nc_oc=AdpSt57kclJw7OOIDwP-DjOP6X1w_Ek2nnEdj8Xq_2UlukygvD_Zijv2w53EJiC2AFw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a39b&oh=00_Af2IalY3761nrQAXF87zkuzblOyY_28mYMhCSafMAAtq6A&oe=69DC4AE7",
                      "dark_message": null,
                      "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT168.346664S\"><Period id=\"0\" duration=\"PT168.346664S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2499091897150685a\" bandwidth=\"65332\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"65332\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m69/AQO3xvfSn1nwA8iY_Ymuol7D0ap96nmM6bvgHsaqWPxXq9nG1th5ILFAzS3su_MzR3wSdD4BYzT8SeVYaHYR7zNF.mp4?strext=1&amp;_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=D9Z04ud3aMcQ7kNvwG_jwKS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjoyNDc4NjM4NDY1NjU1OTUxLCJhc3NldF9hZ2VfZGF5cyI6Mjk4MiwidmlfdXNlY2FzZV9pZCI6MTA1NjgsImR1cmF0aW9uX3MiOjE2OCwiYml0cmF0ZSI6NjU0MjEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2aO6oEmcMYyR3JdMG9Ig8Mn5_gc6ooho2FMjuGi2fayg&amp;oe=69DC1E51</BaseURL><SegmentBase indexRange=\"824-1875\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                      "display_artist": "The Kooks",
                      "duration_in_ms": 168346,
                      "fast_start_progressive_download_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m69/AQO3xvfSn1nwA8iY_Ymuol7D0ap96nmM6bvgHsaqWPxXq9nG1th5ILFAzS3su_MzR3wSdD4BYzT8SeVYaHYR7zNF.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=D9Z04ud3aMcQ7kNvwG_jwKS&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjoyNDc4NjM4NDY1NjU1OTUxLCJhc3NldF9hZ2VfZGF5cyI6Mjk4MiwidmlfdXNlY2FzZV9pZCI6MTA1NjgsImR1cmF0aW9uX3MiOjE2OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=5a5a10b2a90e01c7&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQ09xUUNDTDVEYi1mendGQUlqbXBwaGpXTDlsYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmnpKt1N-T5wgVAigCQzMsF0BlCxJul41QGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af3tWTKFmmZSLPxZpmSFHzEfO7h1UKK86HfNcRvT4iBNzw&oe=69DC1E51",
                      "has_lyrics": true,
                      "highlight_start_times_in_ms": [
                        142500,
                        1500
                      ],
                      "id": "161539057732774",
                      "ig_username": "thekooks",
                      "is_eligible_for_audio_effects": true,
                      "is_eligible_for_vinyl_sticker": true,
                      "is_explicit": false,
                      "licensed_music_subtype": "DEFAULT",
                      "progressive_download_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m69/AQO3xvfSn1nwA8iY_Ymuol7D0ap96nmM6bvgHsaqWPxXq9nG1th5ILFAzS3su_MzR3wSdD4BYzT8SeVYaHYR7zNF.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=D9Z04ud3aMcQ7kNvwG_jwKS&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjoyNDc4NjM4NDY1NjU1OTUxLCJhc3NldF9hZ2VfZGF5cyI6Mjk4MiwidmlfdXNlY2FzZV9pZCI6MTA1NjgsImR1cmF0aW9uX3MiOjE2OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=5a5a10b2a90e01c7&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQ09xUUNDTDVEYi1mendGQUlqbXBwaGpXTDlsYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmnpKt1N-T5wgVAigCQzMsF0BlCxJul41QGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af3tWTKFmmZSLPxZpmSFHzEfO7h1UKK86HfNcRvT4iBNzw&oe=69DC1E51",
                      "reactive_audio_download_url": null,
                      "sanitized_title": null,
                      "song_monetization_info": null,
                      "subtitle": "",
                      "title": "She Moves In Her Own Way",
                      "web_30s_preview_download_url": null,
                      "lyrics": null,
                      "spotify_track_metadata": null,
                      "related_audios": null
                    },
                    "music_consumption_info": {
                      "allow_media_creation_with_music": true,
                      "music_creation_restriction_reason": null,
                      "audio_asset_start_time_in_ms": 142000,
                      "derived_content_start_time_in_composition_in_ms": 0,
                      "contains_lyrics": null,
                      "derived_content_id": null,
                      "display_labels": null,
                      "formatted_clips_media_count": null,
                      "is_bookmarked": false,
                      "is_trending_in_clips": false,
                      "overlap_duration_in_ms": 30000,
                      "placeholder_profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=HMeNVRbt-xsQ7kNvwEVy9wE&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4AAAAA&ccb=7-5&oh=00_Af30iazonP8ImZkMoh7pJhzDjc8FV_6eL1E-asRuPSZoOw&oe=69DC253D&_nc_sid=472314",
                      "should_allow_music_editing": false,
                      "should_mute_audio": false,
                      "should_mute_audio_reason": "",
                      "should_mute_audio_reason_type": null,
                      "should_render_soundwave": false,
                      "trend_rank": null,
                      "previous_trend_rank": null,
                      "ig_artist": {
                        "strong_id__": "297448251",
                        "pk": 297448251,
                        "pk_id": "297448251",
                        "id": "297448251",
                        "username": "thekooks",
                        "full_name": "The Kooks",
                        "is_private": false,
                        "is_verified": true,
                        "profile_pic_id": "3743245092657080969_297448251",
                        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/564334065_18541842748040252_571249401774566537_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NDUuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=njF2WBNQULkQ7kNvwEY8-yo&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GPENoyE8ZHoutd9BAIls7eZNfO0HbmNDAQAB1501500j-ccb7-5&oh=00_Af0dKPDcXz_LLoqBHmz3Qsc7lX-iQyvfpXuybu2qkF6U8w&oe=69DC472D&_nc_sid=472314"
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
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775644830,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": true,
                  "mashup_type": null,
                  "mashups_allowed": true,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": true,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "like_count": 279,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18095164702877817",
                  "bit_flags": 0,
                  "created_at": 1775645262,
                  "created_at_utc": 1775645262,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18095164702877817",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870711225189699935,
                  "status": "Active",
                  "type": 1,
                  "user_id": 501243330,
                  "text": "Summer Pending🕶️☀️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n#love\n#instagood\n#photooftheday\n#viral \n#beautiful",
                  "user": {
                    "strong_id__": "501243330",
                    "pk": 501243330,
                    "pk_id": "501243330",
                    "id": "501243330",
                    "is_unpublished": false,
                    "fbid_v2": 17841401779907831,
                    "username": "gkfentonn",
                    "full_name": "Georgina Fenton",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3852783596470027389_501243330",
                    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=n-uwrwSVU3kQ7kNvwGSmQX6&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af31Qf_BOkGTZadrhLnbBNLkH6nzNsEhWmd5VdHA_uyw9Q&oe=69DC425F&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 0,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
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
                "locations": [],
                "lng": -4.0678841390208,
                "lat": 51.774418090574,
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "501243330",
                  "id": "501243330",
                  "username": "gkfentonn",
                  "full_name": "Georgina Fenton",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=n-uwrwSVU3kQ7kNvwGSmQX6&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af31Qf_BOkGTZadrhLnbBNLkH6nzNsEhWmd5VdHA_uyw9Q&oe=69DC425F&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": true,
                "code": "DW3h1n1jJFf",
                "device_timestamp": 1775644754395864,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      54433,
                      108867
                    ],
                    "height": 1820,
                    "scans_profile": "e35",
                    "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af0f2_JjkpOZFeVWEG_NaBVnmipbjsHwusoW5zQL299AHQ&oe=69DC2620",
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
                    "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1Wnjg_g_thgiegfjZu-DQ63DUL6zSC-A-rnr6_L2ntpA&oe=69DC2620",
                    "width": 750,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af0f2_JjkpOZFeVWEG_NaBVnmipbjsHwusoW5zQL299AHQ&oe=69DC2620",
                "usertags": [],
                "taken_at_ts": 1775644830,
                "sponsor_tags": [],
                "play_count": 0
              }
            },
            {
              "media": {
                "strong_id__": "3870573465710207341_49460984326",
                "id": "3870573465710207341_49460984326",
                "disable_caption_and_comment": false,
                "fbid": 18091242415905171,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDU3MzQ2NTcxMDIwNzM0MQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870573465710207341",
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
                        10574,
                        21149
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/660623218_1291124096279419_8681077985502173420_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=106&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=CaEKiyPm6IQQ7kNvwHB2jmB&_nc_oc=AdrqeDOz2UpYzNsNac_ESySOqvDOXn1FwCC66fA-t3knSErE0X6aaA0GQKe3fz9zryo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1h2WpZ-9lx4iLS_wnNhEuQlmn-vUZi1nw6v1QP8n8oKQ&oe=69DC46AC",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        10574,
                        21149
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/660623218_1291124096279419_8681077985502173420_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=106&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=CaEKiyPm6IQQ7kNvwHB2jmB&_nc_oc=AdrqeDOz2UpYzNsNac_ESySOqvDOXn1FwCC66fA-t3knSErE0X6aaA0GQKe3fz9zryo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1h2WpZ-9lx4iLS_wnNhEuQlmn-vUZi1nw6v1QP8n8oKQ&oe=69DC46AC",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        10193,
                        20386
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/658917391_781527211447470_1815774175265863438_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDU3MzQ2NTcxMDIwNzM0MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=wJqQVVhVf_4Q7kNvwHsKorq&_nc_oc=AdqufAfq-6pdC4inprCtc7U8Zxk7GdNSpW1iP3gsuhjqMgkWqhMTMav1ugbcERaq5AQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1ROcK0RTLz71v54XTT2JwylCbYw7K66WHu3YEXx16brA&oe=69DC3C89",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 467,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/658862980_2130807581053175_7317976620932100927_n.jpg?_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=Yb8UYe-u13oQ7kNvwE1bjzg&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af2tn6d1GCdWs9PMdgErxl6wJtX0DtvFDOikY4XUf_FhrQ&oe=69DC35EA&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.11840952380952381,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 12.433
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTYwYjdlNjkyY2VmNDA2ZGE1YTczY2UwZGY2YTY0YmMzODcwNTczNDY1NzEwMjA3MzQxIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyOTM3NHwzODcwNTczNDY1NzEwMjA3MzQxfDMwMDA5MzA1OTIwfGE0NTQxNDQ2NzYzOGQ5OTZjZWUxNzI2NDdlMWM2YjIxMTI5OGVkNmFiMGViOTM1OTBhMDE3ZjI5NGExZmViMDEifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "hi",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775628530,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "is_artist_pick": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "clips",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "cutout_sticker_info": [],
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "media_ui_attributions_data": [],
                "media_ui_attributions_data_v2": [],
                "creator_product_link_infos": [],
                "is_eligible_for_poe": true,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 7,
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
                    "best_audio_cluster_id": "2888367634851558"
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
                  "music_canonical_id": "18572787481001825",
                  "music_info": null,
                  "nux_info": null,
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": 27151005691153868,
                    "attributed_custom_audio_asset_id": null,
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": true,
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT12.422676S\" FBManifestTimestamp=\"1775657931\" FBManifestIdentifier=\"FpaPs50NKRak3Znm762zByIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT12.422676S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2083263122454354a\" bandwidth=\"60170\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"60170\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m78/AQMLzEl8Nr20qyaoq5PbDa4bgvydGkNnkmfF78e7sD7NWfhjF3GlclbK4JwaA9OJSF0Dj9ZqIYdd4f6X7CIhecujB0IYXTp7rOmmd00.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=28cJMHKlvi8Q7kNvwEyJbhq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjEyOTA0MDIwNzYzMDY2MTcsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTIsImJpdHJhdGUiOjYwNzc1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3AXtyeWzYdD3qtz6sAWFvsGBogcuD45Z7mrb2GvU__Ew&amp;oe=69D84F91</BaseURL><SegmentBase indexRange=\"824-939\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 12433,
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
                    "original_media_id": 3870573465710207341,
                    "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQPinJNjDlbah4DmxZJOJDiyqc2YkJFDGphDxtZxnKcv--TToycKlN6pWAVOIlhsyo6_N_COl6yPY4vk5bHEzpZK.mp4?strext=1&_nc_cat=108&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=YNxh5NJAEzoQ7kNvwEohItz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTI5MDQwMjA3NjMwNjYxNywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3sIa2IjvRlS34f4eQc3pqdXAETc38zFXV_5R_Ns2Ne7w&oe=69DC2E0A",
                    "should_mute_audio": false,
                    "time_created": 1775628510,
                    "trend_rank": null,
                    "previous_trend_rank": null,
                    "overlap_duration_in_ms": 0,
                    "audio_asset_start_time_in_ms": 0,
                    "derived_content_start_time_in_composition_in_ms": 0,
                    "ig_artist": {
                      "strong_id__": "49460984326",
                      "pk": 49460984326,
                      "pk_id": "49460984326",
                      "id": "49460984326",
                      "username": "vikram_gaikwad14",
                      "full_name": "𝐕𝐢𝐤𝐲 🖤",
                      "is_private": false,
                      "is_verified": false,
                      "profile_pic_id": "3771624085844215325_49460984326",
                      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/587270894_18054552251648327_3105288554279427855_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=anRGmqVrBfIQ7kNvwHDBOZU&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GO4KASNHyYkFhSRAAA9f6dJ8MxgrbmNDAQAB1501500j-ccb7-5&oh=00_Af1U5M0rd5f729z3gtxHb1oDlsNI7AB1N9SYQrFX9B69zA&oe=69DC42DD&_nc_sid=472314"
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
                "like_count": 3,
                "top_likers": [
                  "_neerxj__x"
                ],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18091242637905171",
                  "bit_flags": 0,
                  "created_at": 1775628508,
                  "created_at_utc": 1775628508,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18091242637905171",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870573465710207341,
                  "status": "Active",
                  "type": 1,
                  "user_id": 49460984326,
                  "text": "🕊️💗\n.\n.\n#Love #longhair #longhaircat #trending #instagram",
                  "user": {
                    "strong_id__": "49460984326",
                    "pk": 49460984326,
                    "pk_id": "49460984326",
                    "id": "49460984326",
                    "is_unpublished": false,
                    "fbid_v2": 17841449449782623,
                    "username": "vikram_gaikwad14",
                    "full_name": "𝐕𝐢𝐤𝐲 🖤",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3771624085844215325_49460984326",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/587270894_18054552251648327_3105288554279427855_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=anRGmqVrBfIQ7kNvwHDBOZU&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GO4KASNHyYkFhSRAAA9f6dJ8MxgrbmNDAQAB1501500j-ccb7-5&oh=00_Af1U5M0rd5f729z3gtxHb1oDlsNI7AB1N9SYQrFX9B69zA&oe=69DC42DD&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 14,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 6024,
                "ig_play_count": 6024,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_subtitles_locale": "hi_FB",
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 12.432999610900879,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 4307879,
                    "height": 1280,
                    "id": "1510259520459091v",
                    "type": 101,
                    "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOmjlqdUKA9iPcrS-rdgsv_GBf-TICeD-wRCZELl0ka8c7s-Nj9oZElOqLVlJpML19sNb5OiFeInT2O-y7KpbCAvW9rGeTLSdY44CA.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=l9BgHDhadXMQ7kNvwETcSvB&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTI5MDQwMjA3NjMwNjYxNywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=db9ab01ce48d8fa9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MjQzNkEwMzQ3MkIxM0VEQzk0QUJCRTE4Q0ZCRkZBNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzU3NDAzQkFFRTkyQjVCNTc0MDVDOEJBNEFFQzc0RDkxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbysoHWpOfKBBUCKAJDMywXQCjdsi0OVgQYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af38sZ_SnelnNr5e0bLOOJsYzvcTnYvKFS4aJEFMfRXk_Q&oe=69D83456",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  },
                  {
                    "bandwidth": 4307879,
                    "height": 1280,
                    "id": "1510259520459091v",
                    "type": 102,
                    "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOmjlqdUKA9iPcrS-rdgsv_GBf-TICeD-wRCZELl0ka8c7s-Nj9oZElOqLVlJpML19sNb5OiFeInT2O-y7KpbCAvW9rGeTLSdY44CA.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=l9BgHDhadXMQ7kNvwETcSvB&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTI5MDQwMjA3NjMwNjYxNywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=db9ab01ce48d8fa9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MjQzNkEwMzQ3MkIxM0VEQzk0QUJCRTE4Q0ZCRkZBNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzU3NDAzQkFFRTkyQjVCNTc0MDVDOEJBNEFFQzc0RDkxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbysoHWpOfKBBUCKAJDMywXQCjdsi0OVgQYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af38sZ_SnelnNr5e0bLOOJsYzvcTnYvKFS4aJEFMfRXk_Q&oe=69D83456",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT12.433333S\" FBManifestTimestamp=\"1775657931\" FBManifestIdentifier=\"FpaPs50NGA9yMmF2MS1yMWdlbjJ2cDkZxobbsZbhiP0CgNf2opPOowPoq6fw3tSjA66vusCw6KMDgKWbu82UsgPiqsuk8fS7A9L85t7C0/oD8qLlrvaTgAW25tyN+4u7BbKArYbv/dIF7tLegL6k8QWcl4btp/abDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT12.433333S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:87.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"922733360633280v\" bandwidth=\"435296\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"676523\" FBPlaybackResolutionMos=\"0:100,360:27.7,480:22.4,720:18.7,1080:17.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:82.8,480:76.2,720:63.9,1080:48.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMmRRhrrtF34OkcyYAtjph0lDxQtmvb3HtHTqXfXVgTvm-H53cm3xVG7NOt51cAH9dWJ-wxAGPwRwWOKW6N-iExWWh8ndX9gd4Xm1I.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=GTCkUaD_ok8Q7kNvwEpkFWM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjo0MzUyOTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3N4egs4edveuhYAddUHZnhlFH-8YhGD5od9BYsBJCFpQ&amp;oe=69DC3976</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-26724\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-186234\" FBFirstSegmentRange=\"894-284674\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"284675-575097\" FBPrefetchSegmentRange=\"894-284674\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1656491308995767v\" bandwidth=\"1032525\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"1604717\" FBPlaybackResolutionMos=\"0:100,360:42.9,480:35.7,720:29.8,1080:25.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.1,480:86.9,720:77.5,1080:62.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPpJC_qXn42G42N1dwOg20pucyKu9CujAHvBFJTP96QJd7fH3K-EEn200n-7-W08eWqST5B4Y3MSOXV-pFd6Yx3ZvEBr21b0-l8avA.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=StQGwLlWn-oQ7kNvwEcg2oP&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjoxMDMyNTI1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1vwW4PVprgNglBiFIFjhErlf0HTxZJ8x696sAsC12KTw&amp;oe=69DC238F</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-50735\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-434735\" FBFirstSegmentRange=\"894-697637\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"697638-1383422\" FBPrefetchSegmentRange=\"894-697637\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"954730087147840v\" bandwidth=\"1485219\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"2308278\" FBPlaybackResolutionMos=\"0:100,360:51,480:43.3,720:35.2,1080:30.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.9,480:90.6,720:82.8,1080:68.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQN_Rq3kS5wPUKxk1nw2tQoYHlJ-kqbJyDsUvF3OfoKV9-TMmxETNv2-Ud5hvj7G5zW6dH4o7f7Brj-1CRBVKV6rnYmi117fPpdN0zM.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=-JJ7ZkpCJY8Q7kNvwHdjfbr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjoxNDg1MjE5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af151UzCtcozR39vj-IBWTxDFZlt_H9FuPLrHLxhI-NurQ&amp;oe=69DC4CD3</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-62710\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-623256\" FBFirstSegmentRange=\"894-1021711\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1021712-2000481\" FBPrefetchSegmentRange=\"894-1021711\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"923183960509399v\" bandwidth=\"2105060\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"3271615\" FBPlaybackResolutionMos=\"0:100,360:58.7,480:51.4,720:42,1080:35\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.8,480:93.4,720:87.2,1080:74\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQN_GQVCCxfUKBrfocEYrFL3iFNJx52w9iX9LZqnAdZkutyCoA7nZypF2vhAhDVJ_qFlzZA3YaO-Yd6BH-xyUhIJwob2I6a01KAD9AQ.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=CHhQ2Dqh4SIQ7kNvwEzx1Eq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjoyMTA1MDYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1CqFXSyGZhgdqBAwru1H80Er-yuPeaTe8TBVGAGk92sw&amp;oe=69DC2127</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-76722\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-875243\" FBFirstSegmentRange=\"894-1469711\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1469712-2848888\" FBPrefetchSegmentRange=\"894-1469711\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1407717187823801v\" bandwidth=\"2781317\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"4322631\" FBPlaybackResolutionMos=\"0:100,360:64.6,480:57.2,720:47.4,1080:39.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95,720:90,1080:77.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOHSzFS3OpPq5DnaOLlmf4pKhqlehST6E5rU9uLG7w78-gisX4QdCps4OpEfDouFDxdOeBmVQExx_BbJMYtbUk5TfIrdbgMRMr_n20.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=tMiFvTbnzDwQ7kNvwH-IPED&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjoyNzgxMzE3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0HBHqvaes9U3FS18lhHYR5Xr2ApCSnTi7kPTo9bCc-yA&amp;oe=69DC2366</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-85334\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-1143829\" FBFirstSegmentRange=\"894-1958392\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1958393-3781933\" FBPrefetchSegmentRange=\"894-1958392\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"922846587316980v\" bandwidth=\"4032992\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"6267942\" FBPlaybackResolutionMos=\"0:100,360:71.6,480:64.8,720:55,1080:44.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.08,480:96.9,720:93.2,1080:81.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN6DlkTmTxGzfuURQXU0acuLjXez9J9JLyNgHA6obZUbA2yBKqPk3aTfSHOkD56FcKC9LlxpTmmmi3ZLNpVYF-hgmyg3MytxsyR3_I.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=9saWWXpizkMQ7kNvwHcevxK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjo0MDMyOTkyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2X863QwHWSFykwNAyZZYfGVL5k_sjz0wjr6siOO3xDKg&amp;oe=69DC3160</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-101422\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-1619718\" FBFirstSegmentRange=\"894-2834593\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"2834594-5497808\" FBPrefetchSegmentRange=\"894-2834593\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1537322757364123v\" bandwidth=\"5520188\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"8579293\" FBPlaybackResolutionMos=\"0:100,360:76.3,480:70.4,720:60.9,1080:49.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.62,480:98.01,720:95.6,1080:84.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOnX5X7TVqeCAXE31XcrPnqK4x_9FpyVbhmmcd4gAlASZrqOmGsmD2IpzBYFGaBesibydjfAqCHHclbTtgxTdWHtUhlQyXUV6K0dLM.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=yOoWTlgXpP8Q7kNvwHgtX-5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjo1NTIwMTg4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0RxYRc9WBKioCLGgM04vuOuQogOjM_J48qk4xiGzUqGw&amp;oe=69DC1C92</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-119440\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-2159681\" FBFirstSegmentRange=\"894-3828974\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"3828975-7495842\" FBPrefetchSegmentRange=\"894-3828974\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"837978341914307v\" bandwidth=\"7874064\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"12237609\" FBPlaybackResolutionMos=\"0:100,360:81.7,480:76,720:69,1080:62.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.93,480:98.52,720:97.3,1080:94.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHVN0vpdqiBwGyk26Lnb9oR9XyyhS8RjU2UvygeOLn9O6YF5uTCw6adchwlQldYQuPX05S-xcJ0t9CV0kim4OC_2zstPlGtB7WHNs.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=xCasMkqMZ1sQ7kNvwEjQzUY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjkwNDAyMDc2MzA2NjE3LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjEyLCJiaXRyYXRlIjo3ODc0MDY0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0HXmEfUc2I0HEEBFD0IGle3OInjTLD-FppX_FBoA6o8A&amp;oe=69DC307C</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-201457\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-3094191\" FBFirstSegmentRange=\"894-5410475\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"5410476-10684312\" FBPrefetchSegmentRange=\"894-5410475\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"976175372004017a\" bandwidth=\"46357\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46357\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"72881\" FBPaqMos=\"90.39\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPRtjBG4CkFxvMXFX0xgvE6Q4436Kh9M8NjfDxDTSGpq-BouiySZQVYPY352sBWfsyU1QKNhxBDz3_W7eVwhCuGjTFWIFw55ET5x-k.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Ng2xx00jcjkQ7kNvwGrXYKf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjEyOTA0MDIwNzYzMDY2MTcsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTIsImJpdHJhdGUiOjQ2OTM5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3HmE5jA34eHRm79kZFWcpYGrHDlAo8dBsplKFXKuuSUg&amp;oe=69DC49CE</BaseURL><SegmentBase indexRange=\"837-904\" timescale=\"44100\" FBMinimumPrefetchRange=\"905-2207\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"905-16151\" FBFirstSegmentRange=\"905-29345\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"29346-57241\" FBPrefetchSegmentRange=\"905-29345\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"4283530851960270a\" bandwidth=\"85604\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"85604\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"133819\" FBPaqMos=\"93.21\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPCP34T64nbb47mVYmtx-KBTQ8icPnaGL89uKdCfuT8g9GQqZSLimSVsmICnEoYObmfhf2RmgbOD6IGmGZx6UoCK_N7XdedetsSK4g.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=kNYGGfpdpEoQ7kNvwHF4Li5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjEyOTA0MDIwNzYzMDY2MTcsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTIsImJpdHJhdGUiOjg2MTg3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3S7AGz6vUmv9k8vRDICHkF-Z3NaBZ7e9fO25bq7opSAA&amp;oe=69DC21E6</BaseURL><SegmentBase indexRange=\"838-905\" timescale=\"44100\" FBMinimumPrefetchRange=\"906-2863\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-29916\" FBFirstSegmentRange=\"906-54396\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"54397-106586\" FBPrefetchSegmentRange=\"906-54396\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1114140654231337a\" bandwidth=\"120570\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"120570\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"188103\" FBPaqMos=\"94.33\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMe67Y5nXAmA0NbfqFT7N0tx_sIPSN-GRt-OKgioIgGWtWPP0t9woSKq02x-CNIT2UoElKecld893pHHlZ57GQvQIzPS80a72mj0pQ.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=ldXrt8pPtUYQ7kNvwG1s5Gf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjEyOTA0MDIwNzYzMDY2MTcsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTIsImJpdHJhdGUiOjEyMTE0OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1kt8bvAoXNggR80pBjsoo6LTGPCul4XFSCVVDl-PtMSg&amp;oe=69DC488A</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2505\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-39927\" FBFirstSegmentRange=\"901-74667\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"74668-147221\" FBPrefetchSegmentRange=\"901-74667\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1589857178984473a\" bandwidth=\"144078\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"144078\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"224603\" FBPaqMos=\"94.38\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPMdycTfxURQS8h1lV3URGqhyXFFV_MTYlYp4lTQVayD-8nSAdrUYnYE51W1pescRw8s0S8ggRCsb3a9z_1LogJjKTRF0g7r9SppXE.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=_hcshuxfOn8Q7kNvwGequ_I&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjEyOTA0MDIwNzYzMDY2MTcsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTIsImJpdHJhdGUiOjE0NDY1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3SOH-Hhvs1OiHO-Jgi8TatNLr_QnPJLlI3tNv9qxMYfQ&amp;oe=69DC2784</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-46301\" FBFirstSegmentRange=\"901-87508\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"87509-173656\" FBPrefetchSegmentRange=\"901-87508\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "number_of_qualities": 8,
                "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "SELF_DISCLOSURE_FLOW"
                },
                "user": {
                  "pk": "49460984326",
                  "id": "49460984326",
                  "username": "vikram_gaikwad14",
                  "full_name": "𝐕𝐢𝐤𝐲 🖤",
                  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/587270894_18054552251648327_3105288554279427855_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEodWnFZ8KMGBa531DWyLk5ZhlTgUb9bHXtaqmcGIE4nEWSfRNB_MRWTeTbw0tCaPw&_nc_ohc=anRGmqVrBfIQ7kNvwHDBOZU&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GO4KASNHyYkFhSRAAA9f6dJ8MxgrbmNDAQAB1501500j-ccb7-5&oh=00_Af1U5M0rd5f729z3gtxHb1oDlsNI7AB1N9SYQrFX9B69zA&oe=69DC42DD&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3Cg9UtaFt",
                "device_timestamp": 1775628330380811,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": true,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOmjlqdUKA9iPcrS-rdgsv_GBf-TICeD-wRCZELl0ka8c7s-Nj9oZElOqLVlJpML19sNb5OiFeInT2O-y7KpbCAvW9rGeTLSdY44CA.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=l9BgHDhadXMQ7kNvwETcSvB&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTI5MDQwMjA3NjMwNjYxNywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=db9ab01ce48d8fa9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MjQzNkEwMzQ3MkIxM0VEQzk0QUJCRTE4Q0ZCRkZBNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzU3NDAzQkFFRTkyQjVCNTc0MDVDOEJBNEFFQzc0RDkxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbysoHWpOfKBBUCKAJDMywXQCjdsi0OVgQYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af38sZ_SnelnNr5e0bLOOJsYzvcTnYvKFS4aJEFMfRXk_Q&oe=69D83456",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      10193,
                      20386
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/658917391_781527211447470_1815774175265863438_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDU3MzQ2NTcxMDIwNzM0MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=wJqQVVhVf_4Q7kNvwHsKorq&_nc_oc=AdqufAfq-6pdC4inprCtc7U8Zxk7GdNSpW1iP3gsuhjqMgkWqhMTMav1ugbcERaq5AQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1ROcK0RTLz71v54XTT2JwylCbYw7K66WHu3YEXx16brA&oe=69DC3C89",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/658917391_781527211447470_1815774175265863438_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDU3MzQ2NTcxMDIwNzM0MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=wJqQVVhVf_4Q7kNvwHsKorq&_nc_oc=AdqufAfq-6pdC4inprCtc7U8Zxk7GdNSpW1iP3gsuhjqMgkWqhMTMav1ugbcERaq5AQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=-j6UCPKLRqV4aO_aM5Id8g&_nc_ss=7a3ba&oh=00_Af1ROcK0RTLz71v54XTT2JwylCbYw7K66WHu3YEXx16brA&oe=69DC3C89",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775628530,
                "sponsor_tags": []
              }
            }
          ]
        }
      }
    ],
    "more_available": true,
    "next_max_id": "b41747a35b134b46b815c01122eeefeb",
    "next_page": 1,
    "next_media_ids": [],
    "auto_load_more_enabled": true,
    "status": "ok"
  },
  "next_page_id": "WyJiNDE3NDdhMzViMTM0YjQ2YjgxNWMwMTEyMmVlZWZlYiIsW10sMV0="
}
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
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/663125737_800926396408847_3121502684282065892_n.jpg?_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=4jAuGCQkshkQ7kNvwFzr4zY&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af1QSi7y34Ej7f5cjHKzLNZDmeVu6sN2YO6mXuzLFaup0w&oe=69DC41CC&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.14602857142857142,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 15.333
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMTFkYjIwNmVkM2FmNDdkNmIxYjZlZjRjZjI0YjUyYTAzODcwNjcyNDYzMjk0NTI0NDEyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyMjMwMnwzODcwNjcyNDYzMjk0NTI0NDEyfDMwMDA5MzA1OTIwfGMwZjliMmRhNzQwMjRmOThjNTU0OTI5MGExYTAxODg4MTI5M2VmZmIzNzQ4OGZhOGI0MjU1OGJlMDhiYjY5YzgifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775640164,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "is_artist_pick": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "clips",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "cutout_sticker_info": [],
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "media_ui_attributions_data": [],
                "media_ui_attributions_data_v2": [],
                "creator_product_link_infos": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 214,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 7,
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
                    "best_audio_cluster_id": "1168434565305375"
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
                  "music_canonical_id": "18546795697066284",
                  "music_info": null,
                  "nux_info": null,
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": 26620737760947638,
                    "attributed_custom_audio_asset_id": null,
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": true,
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT15.325171S\" FBManifestTimestamp=\"1775657923\" FBManifestIdentifier=\"FoaPs50NKRamy9X0hpiLBCIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT15.325171S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1150502407156435a\" bandwidth=\"63244\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"63244\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQMtom3JdfzKzro30tP0CFwhpH7WbDwXx3T5mo583rCcGlsFpalEJ9AVinKbbjfDFa8w3JuEfnaNok4Aa52WjsU7gosGiKhQA-JE2L8.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=dwJoxJREtvcQ7kNvwFfaL-T&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3ODc4OTk2ODIxNTUxNDk5LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1LCJiaXRyYXRlIjo2Mzc0MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3TFkimtChEYbisag1H0e1DaKpnR1TIUsum6txJJN9_NQ&amp;oe=69D8301F</BaseURL><SegmentBase indexRange=\"824-951\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 15333,
                    "formatted_clips_media_count": null,
                    "hide_remixing": false,
                    "is_audio_automatically_attributed": true,
                    "is_eligible_for_audio_effects": false,
                    "is_eligible_for_vinyl_sticker": true,
                    "is_explicit": false,
                    "is_original_audio_download_eligible": true,
                    "is_reuse_disabled": false,
                    "is_xpost_from_fb": false,
                    "music_canonical_id": null,
                    "oa_owner_is_music_artist": false,
                    "original_audio_subtype": "contains",
                    "original_audio_title": "Original audio",
                    "original_media_id": 3870672463294524412,
                    "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPOnnlU5DmhMdqIqaGnUmR4TeRq9b0ZyhIDUEwMzYslk9GOOUJo7LdEEWX3mT4S5TF_KTLMz2Wle1RKAyzukIMy.mp4?strext=1&_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=kHdPA9qLYLAQ7kNvwGLBuKb&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc4Nzg5OTY4MjE1NTE0OTksImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3Rra444hz5XA5ac1j3nj4LCgNUTRKlV8wZ-NHmeoV4bg&oe=69DC1B33",
                    "should_mute_audio": false,
                    "time_created": 1775640159,
                    "trend_rank": null,
                    "previous_trend_rank": null,
                    "overlap_duration_in_ms": 0,
                    "audio_asset_start_time_in_ms": 0,
                    "derived_content_start_time_in_composition_in_ms": 0,
                    "ig_artist": {
                      "strong_id__": "75290853567",
                      "pk": 75290853567,
                      "pk_id": "75290853567",
                      "id": "75290853567",
                      "username": "pihu_ty12",
                      "full_name": "Prerna Tyagi❤️",
                      "is_private": false,
                      "is_verified": false,
                      "profile_pic_id": "3818718886770803278_75290853567",
                      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/623287413_17872696551509568_2009535807914113383_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NzkuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=2GCsY9EM9KkQ7kNvwHYfZJd&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GHWcJiVAjiFxH38-AGf5JZorTuMbbmNDAQAB1501500j-ccb7-5&oh=00_Af03n5kzJC0TtPs_rYilHmacKK6xkiu0j59y309jAeiyRA&oe=69DC1EC9&_nc_sid=472314"
                    },
                    "audio_filter_infos": null,
                    "audio_parts": [
                      {
                        "music_canonical_id": "18152726809023873",
                        "audio_type": "licensed_music",
                        "display_artist": "Armaan Malik, Shraddha Kapoor",
                        "ig_artist": {
                          "strong_id__": "545976013",
                          "pk": 545976013,
                          "pk_id": "545976013",
                          "id": "545976013",
                          "username": "armaanmalik",
                          "full_name": "ARMAAN",
                          "is_private": false,
                          "is_verified": true,
                          "profile_pic_id": "3858947176705856425_545976013",
                          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/657636244_18574601443056014_2553599727468811531_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=wPFHUKk_z_0Q7kNvwHT-rsH&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJS7MieOmdtogP1BAAsVUC5sNXAjbmNDAQAB1501500j-ccb7-5&oh=00_Af3h8ksMmSl6KE9mk_l56c6iOqRSwX6c9RVojg_Qm5YsdQ&oe=69DC3424&_nc_sid=472314"
                        },
                        "display_title": "Sab Tera",
                        "thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/427886762_2089210324765190_4858521135288744355_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=5oXKkv2b2PEQ7kNvwFZm9jA&_nc_oc=Adr-ts6s0wcl3L96UdRCIzi6QOR8GX6axBj4-hbMcep5FylP1rV0GfHB7R4GJtm5YhQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a39b&oh=00_Af2YuqjfFE2Bj_bfuJLqt4WK9JVQN1X00IW868XZPV-cQw&oe=69DC43C2",
                        "is_bookmarked": false,
                        "is_explicit": false,
                        "parent_start_time_in_ms": 0,
                        "audio_start_time_in_ms": 0,
                        "duration_in_ms": 30,
                        "is_eligible_for_audio_effects": false,
                        "derived_content_start_time_in_composition_in_ms": 0
                      }
                    ],
                    "audio_parts_by_filter": [
                      {
                        "music_canonical_id": "18152726809023873",
                        "audio_type": "licensed_music",
                        "display_artist": "Armaan Malik, Shraddha Kapoor",
                        "ig_artist": {
                          "strong_id__": "545976013",
                          "pk": 545976013,
                          "pk_id": "545976013",
                          "id": "545976013",
                          "username": "armaanmalik",
                          "full_name": "ARMAAN",
                          "is_private": false,
                          "is_verified": true,
                          "profile_pic_id": "3858947176705856425_545976013",
                          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/657636244_18574601443056014_2553599727468811531_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=wPFHUKk_z_0Q7kNvwHT-rsH&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJS7MieOmdtogP1BAAsVUC5sNXAjbmNDAQAB1501500j-ccb7-5&oh=00_Af3h8ksMmSl6KE9mk_l56c6iOqRSwX6c9RVojg_Qm5YsdQ&oe=69DC3424&_nc_sid=472314"
                        },
                        "display_title": "Sab Tera",
                        "thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/427886762_2089210324765190_4858521135288744355_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=5oXKkv2b2PEQ7kNvwFZm9jA&_nc_oc=Adr-ts6s0wcl3L96UdRCIzi6QOR8GX6axBj4-hbMcep5FylP1rV0GfHB7R4GJtm5YhQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a39b&oh=00_Af2YuqjfFE2Bj_bfuJLqt4WK9JVQN1X00IW868XZPV-cQw&oe=69DC43C2",
                        "is_bookmarked": false,
                        "is_explicit": false,
                        "parent_start_time_in_ms": 0,
                        "audio_start_time_in_ms": 0,
                        "duration_in_ms": 30,
                        "is_eligible_for_audio_effects": false,
                        "derived_content_start_time_in_composition_in_ms": 0
                      }
                    ],
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
                "like_count": 933,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "17882332389521536",
                  "bit_flags": 0,
                  "created_at": 1775640156,
                  "created_at_utc": 1775640156,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "17882332389521536",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870672463294524412,
                  "status": "Active",
                  "type": 1,
                  "user_id": 75290853567,
                  "text": "🌹\n\n#instagram #viral #instadaily #love #reelviral",
                  "user": {
                    "strong_id__": "75290853567",
                    "pk": 75290853567,
                    "pk_id": "75290853567",
                    "id": "75290853567",
                    "is_unpublished": false,
                    "fbid_v2": 17841475287031356,
                    "username": "pihu_ty12",
                    "full_name": "Prerna Tyagi❤️",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3818718886770803278_75290853567",
                    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/623287413_17872696551509568_2009535807914113383_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NzkuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=2GCsY9EM9KkQ7kNvwHYfZJd&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GHWcJiVAjiFxH38-AGf5JZorTuMbbmNDAQAB1501500j-ccb7-5&oh=00_Af03n5kzJC0TtPs_rYilHmacKK6xkiu0j59y309jAeiyRA&oe=69DC1EC9&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 25,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 15565,
                "ig_play_count": 15565,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 15.333000183105469,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1498914,
                    "height": 1280,
                    "id": "1433266891452369v",
                    "type": 101,
                    "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNFCpOJMHx75lvP_Vhp9B1SjSXBNRuTm1Bu3P6KDAzgb4oHqANzxQ43mUmozfaelYDMTbP25PVvk9v4zH5sS0zU11uw5hhq_5ebRgw.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=63Od2xdh-GkQ7kNvwG28ewJ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4Nzg5OTY4MjE1NTE0OTksImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=39629c43c5fe0b83&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BRTRENDBCMkVBMjdCNjg1QzhGNzI3NUY1MTQyQTlBNF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0Q5NDIwNTA4OTcyNzBFNENBNThDNURDNTA5RUE0Q0JEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWpunnyrbCPxUCKAJDMywXQC6qfvnbItEYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3S7DXjRc8DUk8_wj-i-sqBnKgEodd_Iyw5hRlRm2f7IA&oe=69D84228",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  },
                  {
                    "bandwidth": 1498914,
                    "height": 1280,
                    "id": "1433266891452369v",
                    "type": 102,
                    "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNFCpOJMHx75lvP_Vhp9B1SjSXBNRuTm1Bu3P6KDAzgb4oHqANzxQ43mUmozfaelYDMTbP25PVvk9v4zH5sS0zU11uw5hhq_5ebRgw.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=63Od2xdh-GkQ7kNvwG28ewJ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4Nzg5OTY4MjE1NTE0OTksImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=39629c43c5fe0b83&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BRTRENDBCMkVBMjdCNjg1QzhGNzI3NUY1MTQyQTlBNF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0Q5NDIwNTA4OTcyNzBFNENBNThDNURDNTA5RUE0Q0JEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWpunnyrbCPxUCKAJDMywXQC6qfvnbItEYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3S7DXjRc8DUk8_wj-i-sqBnKgEodd_Iyw5hRlRm2f7IA&oe=69D84228",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT15.333333S\" FBManifestTimestamp=\"1775657923\" FBManifestIdentifier=\"FoaPs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxoS4nvHVv80C9PSq2v2A+wLsqdjRg5CQA4Dan8v0pNcEjImL/9fb+gSk8OT42uiKBbz+4fqapJsF3sTi9uG4yQX+squ4/cflBvboisek6fcHyvKWmaqssgj8ntGS3qveDSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT15.333333S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"879884668439158v\" bandwidth=\"332846\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"637956\" FBPlaybackResolutionMos=\"0:100,360:73.4,480:70.8,720:68.8,1080:69.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94,480:90.6,720:84.7,1080:78\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMSvKkO-GLMX5jKTjwq9dfgrfROYutR8WIX9ib08KlcNCyA-ETl5gpgB-9JdHKGGRa2Jl1Jb2UMiRtYkyGYog6R42a-YvctJ_wbX80.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=USwMYGTBrmEQ7kNvwHJFu5Y&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6MzMyODQ2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1utvXvggpr1vcDDBgOaLdA_inyQSMD3_RvO_Q2lHSERQ&amp;oe=69DC50AA</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1678\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-76995\" FBFirstSegmentRange=\"906-169049\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"169050-359008\" FBPrefetchSegmentRange=\"906-169049\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"833446685793594v\" bandwidth=\"444711\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"852363\" FBPlaybackResolutionMos=\"0:100,360:76.9,480:74.4,720:72.2,1080:72.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.6,480:93.4,720:88.7,1080:82.5\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPw4sGGsiUffFLZpMS7K3YT6wfbI722X20RXLaCB4nRSVVQOgKNeee0UwxzLGXERSqGQBOoVPVVU4rwDo0dyGY3bNSTtfsUwCApNp0.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=DDRgiBSKbcoQ7kNvwEaqvKm&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6NDQ0NzExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1iNnRzFTPPBmhU6XpHzYl4DrJnccTn1PbI6BDyc_ulwQ&amp;oe=69DC251E</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1678\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-97468\" FBFirstSegmentRange=\"906-221244\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"221245-472033\" FBPrefetchSegmentRange=\"906-221244\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1395755922317894v\" bandwidth=\"581388\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"1114328\" FBPlaybackResolutionMos=\"0:100,360:80.3,480:77.4,720:75.7,1080:75.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.5,480:95,720:91.5,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQO-c8g6-HvpnyKVoS_PjF986jjsMJbdfTu_7qzjt_opG6-v6WtO2TXze3DNgfQt5XaJpQWWnekBi0KNE9sCQ-X-M00zMn3vuBAApuo.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=J4uBSujezE4Q7kNvwHrKkw0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6NTgxMzg4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af18gbqSPRiKqpye4sf1H99Xxtkb3ZwFTUxfWyL2v-wvgg&amp;oe=69DC492D</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1686\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-118555\" FBFirstSegmentRange=\"906-282333\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"282334-608195\" FBPrefetchSegmentRange=\"906-282333\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"733368603102722v\" bandwidth=\"744744\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"1427427\" FBPlaybackResolutionMos=\"0:100,360:83.2,480:80.5,720:78,1080:77.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.4,480:96.4,720:94,1080:90.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNzfDRb9YeoNZdzaoXFpnrBN6ANgtwqrTzqGKELZnY1emqs-ozELJSRYQ9rNcdJ8sMY6qwBcxvD-O1j0i8VBiuQmqbwNgwKcpotaxU.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=HvdQlIZf6ssQ7kNvwFymuNR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6NzQ0NzQ0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2lDN4viZ5F9FOT6K1VrkrRE_ssn6pFIknTldVZ2V3Ihg&amp;oe=69DC51E3</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1698\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-144619\" FBFirstSegmentRange=\"906-354695\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"354696-767022\" FBPrefetchSegmentRange=\"906-354695\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2233817397025339v\" bandwidth=\"1014292\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"1944060\" FBPlaybackResolutionMos=\"0:100,360:86.1,480:83.7,720:81.3,1080:79.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.17,480:97.7,720:96.1,1080:93.6\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNfbPkkYkqkQcMCO7CCsIlz3cENFlKg7YkVAzaiJV1qBn4c5IczRMLhOit0d_kZGST02Wi9RIpUM6bd5oHbE9El3MCjaz0pbZvlRfM.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=dAjcdHRrxsgQ7kNvwElAMaI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6MTAxNDI5MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3WowcJRJcosq7CZ2u0x7tXx8uvgEHljX05TTO7vIse7Q&amp;oe=69DC50EF</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-190152\" FBFirstSegmentRange=\"906-478923\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"478924-1037177\" FBPrefetchSegmentRange=\"906-478923\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1912187816078527v\" bandwidth=\"1368360\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"2622690\" FBPlaybackResolutionMos=\"0:100,360:88.4,480:86.4,720:84.1,1080:82.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.77,480:98.52,720:97.5,1080:95.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMaKPUwbFvEhza8v4DyZtG1u72zkNoyhmqOBjLJNgCua-Ns9_xWmbscASwOWLSopF3KfrleJWfvgbf0AQFzcqw8r_YI9mVGZ3wmhC0.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=dwTDpOGTeEcQ7kNvwENB0SI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6MTM2ODM2MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2laLLZl_c55fD9QTd2hIwm8AtFwcslIMLrz3GB-GkbhA&amp;oe=69DC1B54</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1699\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-245006\" FBFirstSegmentRange=\"906-637813\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"637814-1384349\" FBPrefetchSegmentRange=\"906-637813\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"3866634253641662v\" bandwidth=\"1859865\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"3564743\" FBPlaybackResolutionMos=\"0:100,360:90.5,480:88.5,720:86.4,1080:84.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.205,480:99.11,720:98.51,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPc_9VHQjrD3qtYw7vLleR9evETLJpSTUjrFnA9kYCZQKiRMRsuNzQDeYlKghPXQs8nsjKr5peajrM4-N_2i1SXn3WSw80VffZUCxA.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=VBBdZculoj8Q7kNvwGWlN2u&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6MTg1OTg2NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0PrpazytsvAa4uLQTjPF6Znmd_pebHcX_IrId-NZ8Pbg&amp;oe=69DC3596</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1702\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-319582\" FBFirstSegmentRange=\"906-860950\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"860951-1859184\" FBPrefetchSegmentRange=\"906-860950\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1568878797541679v\" bandwidth=\"2890181\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"5539514\" FBPlaybackResolutionMos=\"0:100,360:92.9,480:91.3,720:89.2,1080:87.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.551,480:99.612,720:99.568,1080:99.384\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPtAzYrIJ4UZ24S_AXHPLMZDYGBwDVft6SesN9-4PSxyYjCo0jg_YpQfDjHAtF1xS8PeejT98-qc4JbnpldYwMplWnHilg5jXXvqiU.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=YG-gY5yeXDcQ7kNvwGDnDdd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3ODk5NjgyMTU1MTQ5OSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNSwiYml0cmF0ZSI6Mjg5MDE4MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2bnUAndQY965G5OtNo31jAAPm_V6pAtSLCCeeU-vA3eg&amp;oe=69DC486B</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-1757\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-509400\" FBFirstSegmentRange=\"906-1355536\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1355537-2913179\" FBPrefetchSegmentRange=\"906-1355536\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2362512554253477a\" bandwidth=\"46889\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46889\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"90739\" FBPaqMos=\"90.91\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQO8uOaf2gEXo3ZKgzA0hzz2kDnHu57QZkHLCdS7054WXT7qU-UBuH1CD2C8hXjOBntx4hKZ2nhJvfBXrc6bSD8BYL59Hgd8ZWzT-7w.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=_abW4Z5tMoYQ7kNvwEFaycC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc4OTk2ODIxNTUxNDk5LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1LCJiaXRyYXRlIjo0NzM2NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1iuSQNIeNmFOPzCOq2U9u4Xd1okKW7HRvtrsqtnsNG8Q&amp;oe=69DC35A5</BaseURL><SegmentBase indexRange=\"837-916\" timescale=\"44100\" FBMinimumPrefetchRange=\"917-2227\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"917-16209\" FBFirstSegmentRange=\"917-29740\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"29741-58641\" FBPrefetchSegmentRange=\"917-29740\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1317849053525632a\" bandwidth=\"79188\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"79188\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"152613\" FBPaqMos=\"92.02\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMyydi4TJje8MMjYmM3IxqxqBSkFhQbUL5trajBiVjEiHrYzh5fjclO98Dz7IR-iKtj0EWE38QUWhSzyjcv8eu8gXT0SjZW6xAmyWs.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Hdkikt50gmsQ7kNvwGSJB0O&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc4OTk2ODIxNTUxNDk5LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1LCJiaXRyYXRlIjo3OTY2NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Iq2P8hM-8DFg9JfKY3ODY_CHyx6si5HG1qZok1BDhOw&amp;oe=69DC1D43</BaseURL><SegmentBase indexRange=\"838-917\" timescale=\"44100\" FBMinimumPrefetchRange=\"918-2869\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-26620\" FBFirstSegmentRange=\"918-49550\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"49551-98384\" FBPrefetchSegmentRange=\"918-49550\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1467370605133726a\" bandwidth=\"127137\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"127137\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"244462\" FBPaqMos=\"93.89\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNFJ74GelGGDYPpL4ww5DrxF0D0O-cBHoeCOBtRqYgSHeo7OtxqbTdsxEZqhwo2pGkTI9NzqGiLrBak_Xyn7BqYjVLar6JvuDhOaAE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=P48BEfL3g-YQ7kNvwFlQIio&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc4OTk2ODIxNTUxNDk5LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1LCJiaXRyYXRlIjoxMjc2MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1dwk8nWMwzYqhsbp2IB8OSMxQmqZRwo15dyKXddbR0gg&amp;oe=69DC37B8</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2648\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-41017\" FBFirstSegmentRange=\"913-79155\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"79156-157500\" FBPrefetchSegmentRange=\"913-79155\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1431164028754962a\" bandwidth=\"146199\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"146199\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"280978\" FBPaqMos=\"94.12\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNdVW1DYg_ukBtjWEfbBPrSz75qeqoJmdPjrYTOVD8TK0J_WxjygKrP47hEUtjGgbgyEv40TwbO2v22kTrDqZSzyrS9pfOM3HXreII.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=BhBBgjLJZVYQ7kNvwFn5KfB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc4OTk2ODIxNTUxNDk5LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1LCJiaXRyYXRlIjoxNDY2NzUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3xJZB69BxSwjl2z39aCAfmsidqGjDzc6ouznCOClqODQ&amp;oe=69DC393C</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2770\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-47543\" FBFirstSegmentRange=\"913-90898\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"90899-181064\" FBPrefetchSegmentRange=\"913-90898\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "number_of_qualities": 8,
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "75290853567",
                  "id": "75290853567",
                  "username": "pihu_ty12",
                  "full_name": "Prerna Tyagi❤️",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/623287413_17872696551509568_2009535807914113383_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NzkuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=2GCsY9EM9KkQ7kNvwHYfZJd&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GHWcJiVAjiFxH38-AGf5JZorTuMbbmNDAQAB1501500j-ccb7-5&oh=00_Af03n5kzJC0TtPs_rYilHmacKK6xkiu0j59y309jAeiyRA&oe=69DC1EC9&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3ZBkAjmv8",
                "device_timestamp": 1775640132239923,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNFCpOJMHx75lvP_Vhp9B1SjSXBNRuTm1Bu3P6KDAzgb4oHqANzxQ43mUmozfaelYDMTbP25PVvk9v4zH5sS0zU11uw5hhq_5ebRgw.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=63Od2xdh-GkQ7kNvwG28ewJ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4Nzg5OTY4MjE1NTE0OTksImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=39629c43c5fe0b83&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BRTRENDBCMkVBMjdCNjg1QzhGNzI3NUY1MTQyQTlBNF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0Q5NDIwNTA4OTcyNzBFNENBNThDNURDNTA5RUE0Q0JEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWpunnyrbCPxUCKAJDMywXQC6qfvnbItEYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3S7DXjRc8DUk8_wj-i-sqBnKgEodd_Iyw5hRlRm2f7IA&oe=69D84228",
                "image_versions": [
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
                "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/661604863_829242592916270_2274851443561613542_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDY3MjQ2MzI5NDUyNDQxMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=GlqvufCNZqMQ7kNvwFwwY9o&_nc_oc=Adq6f7yITxA7IKaDUoNeT_YIg5-O-BYclOuoAbEn30bQiuaSIPwNkYkGS2vyoolSm58&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af3PDTFPA-rbkXwDq_uaahDbgWmhHIMUkvxoltKFeKODcQ&oe=69DC447A",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775640164,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870786707311011812_52722857117",
                "id": "3870786707311011812_52722857117",
                "disable_caption_and_comment": false,
                "fbid": 18013236758684330,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDc4NjcwNzMxMTAxMTgxMg==.3",
                "integrity_review_decision": "pending",
                "pk": "3870786707311011812",
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
                        5458,
                        10916
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/657608130_1295474109413937_6693916273871811927_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=100&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=1-K46EaitiEQ7kNvwE_zqbL&_nc_oc=AdpLnHDqJ5Bh7rHjN0au9P6jYoXHIcSOoxUOCw-k4BNeYVPScJ63gVb1zdS8GF2FRTk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af2njS2bnIwgKEL0TI2NZaAWwzDDck3LZiWwxPiANGFVxg&oe=69DC2E0B",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        5458,
                        10916
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/657608130_1295474109413937_6693916273871811927_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=100&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=1-K46EaitiEQ7kNvwE_zqbL&_nc_oc=AdpLnHDqJ5Bh7rHjN0au9P6jYoXHIcSOoxUOCw-k4BNeYVPScJ63gVb1zdS8GF2FRTk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af2njS2bnIwgKEL0TI2NZaAWwzDDck3LZiWwxPiANGFVxg&oe=69DC2E0B",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        5167,
                        10334
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/660422205_1273796614179190_6470373456327365366_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=Mzg3MDc4NjcwNzMxMTAxMTgxMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vKTKg30TAKgQ7kNvwHq904K&_nc_oc=AdrWIA4UgCGDLT1PxXh2p5WTA6xsfb6n1Fn3owxZUqrNFCjy14bcPibPdFshgZPAj0o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af2AwfNdcC9SYjvrTt6vXfkG-UhNr0h4GO40wceOZSRQ2Q&oe=69DC2015",
                      "width": 640,
                      "is_spatial_image": false
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 691,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_urls": [
                        "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661091077_2471741609961080_2746855933475406224_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=XfDuS-z90OMQ7kNvwF0PUdp&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&oh=00_Af0QFWMv393fNci-Yg9l7yCKZCvxx5Ma0HgEUxXA6cqiBw&oe=69DC43C9&_nc_sid=472314"
                      ],
                      "sprite_width": 1500,
                      "thumbnail_duration": 0.24333333333333335,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 25.55
                    }
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMTFkYjIwNmVkM2FmNDdkNmIxYjZlZjRjZjI0YjUyYTAzODcwNzg2NzA3MzExMDExODEyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyMjM4NXwzODcwNzg2NzA3MzExMDExODEyfDMwMDA5MzA1OTIwfDQ1NGUxOWEyNTM1MWMzNjgyNmI1YTY1ZTIwNTBmNTkyYTQ2ZDFlYjMwYWQxOGYwMDc0MDA3YmU4ZDhjMzE4NTEifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": false,
                "clips_tab_pinned_user_ids": [],
                "original_lang_for_translations": "bn",
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775653917,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "is_artist_pick": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "clips",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "cutout_sticker_info": [],
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "media_ui_attributions_data": [],
                "media_ui_attributions_data_v2": [],
                "creator_product_link_infos": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [],
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 0,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 9,
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
                    "best_audio_cluster_id": "918370384441274"
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
                  "music_canonical_id": "18460083127099607",
                  "music_info": null,
                  "nux_info": null,
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": 26484567291230271,
                    "attributed_custom_audio_asset_id": null,
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": true,
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT25.563719S\" FBManifestTimestamp=\"1775657923\" FBManifestIdentifier=\"FoaPs50NKRaikuGGx97RBCIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT25.563719S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1305645234791569a\" bandwidth=\"61629\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"61629\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQOsYEh0SiW-2uOnRgjNZOm8xhTRRDufLFMJqz2pZPfhi6w-e6CGcZZjuBA-yGpIMfH4L6dw-IVO95TFCekcWk4ya2KdaoLBgt8fqPg.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=1uIWgDW3YNsQ7kNvwGNCGBc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE4MDQ0NTg3MzM3NzUzMTE4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI1LCJiaXRyYXRlIjo2MTk0NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3nPJ4cNRHOPchZJ8ZY-Wfvpj9CM3oXvZGHyYOg1BvB8g&amp;oe=69D82938</BaseURL><SegmentBase indexRange=\"824-1011\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 25000,
                    "formatted_clips_media_count": null,
                    "hide_remixing": false,
                    "is_audio_automatically_attributed": true,
                    "is_eligible_for_audio_effects": false,
                    "is_eligible_for_vinyl_sticker": true,
                    "is_explicit": false,
                    "is_original_audio_download_eligible": true,
                    "is_reuse_disabled": false,
                    "is_xpost_from_fb": false,
                    "music_canonical_id": null,
                    "oa_owner_is_music_artist": false,
                    "original_audio_subtype": "contains",
                    "original_audio_title": "Original audio",
                    "original_media_id": 3870786707311011812,
                    "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQPbnZtNSRGd4yLMTy3NzLvpmgcB1tOJ423y0jwsOV7lpTBMKEMGW1-W7vCa_E9d1w8ErcasLwRN5CuxqB5l_lws.mp4?strext=1&_nc_cat=104&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=V9zYcxseZh8Q7kNvwF8_YNS&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTgwNDQ1ODczMzc3NTMxMTgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0BTZk4cswsisGwSC5i-C_1Pva9uPmM8qA1_tZB2XIfvw&oe=69DC43DE",
                    "should_mute_audio": false,
                    "time_created": 1775653909,
                    "trend_rank": null,
                    "previous_trend_rank": null,
                    "overlap_duration_in_ms": 0,
                    "audio_asset_start_time_in_ms": 0,
                    "derived_content_start_time_in_composition_in_ms": 0,
                    "ig_artist": {
                      "strong_id__": "52722857117",
                      "pk": 52722857117,
                      "pk_id": "52722857117",
                      "id": "52722857117",
                      "username": "_srkkk_07",
                      "full_name": "🚩",
                      "is_private": false,
                      "is_verified": false,
                      "profile_pic_id": "3863515889765973496_52722857117",
                      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/656813466_18043282949753118_3670872010364444994_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDQwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=u7wKddQogTQQ7kNvwGYYJne&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJotJiceSc0uRRpAAEJhsvGkjvEybmNDAQAB1501500j-ccb7-5&oh=00_Af0LiGFaML4nSzJOIR_FlJEvnGao2f7QT7DYRPV-kIWCrg&oe=69DC2853&_nc_sid=472314"
                    },
                    "audio_filter_infos": null,
                    "audio_parts": [
                      {
                        "music_canonical_id": "18304076689091395",
                        "audio_type": "licensed_music",
                        "display_artist": "Arindom, Shalmali Kholgade",
                        "ig_artist": {
                          "strong_id__": "4253721088",
                          "pk": 4253721088,
                          "pk_id": "4253721088",
                          "id": "4253721088",
                          "username": "arindom.chatterjee",
                          "full_name": "Arindom",
                          "is_private": false,
                          "is_verified": true,
                          "profile_pic_id": "2429191417533485242_4253721088",
                          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/122662758_212734520197756_8582777109243913279_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=ejXgOZbvYmEQ7kNvwEMQD9n&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GGavTwd8AoIde8EAAD9k1q5OJhx3bkULAAAB1501500j-ccb7-5&oh=00_Af0jQV0HjZ2lQZjoEuVUDiZX1b8PBBOX3huzB7ZHR6GRvQ&oe=69DC4609&_nc_sid=472314"
                        },
                        "display_title": "Bhalobeshe Kono Bhool",
                        "thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/597135326_71060345790014_7336470468630567440_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=BVlDjY8ECMsQ7kNvwEKUb2H&_nc_oc=AdrbgVcNsrhUFcKx9SwBDbcPlXcYlAQHjuaZ06gZeySAWCgBbZ-QQEQQ5i67jKgM1t8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a39b&oh=00_Af2lgAqoG-dQzl88miPObbt0pTNpim-1KAxQ_VF6rMMa3Q&oe=69DC461E",
                        "is_bookmarked": false,
                        "is_explicit": false,
                        "parent_start_time_in_ms": 0,
                        "audio_start_time_in_ms": 0,
                        "duration_in_ms": 30,
                        "is_eligible_for_audio_effects": false,
                        "derived_content_start_time_in_composition_in_ms": 0
                      }
                    ],
                    "audio_parts_by_filter": [
                      {
                        "music_canonical_id": "18304076689091395",
                        "audio_type": "licensed_music",
                        "display_artist": "Arindom, Shalmali Kholgade",
                        "ig_artist": {
                          "strong_id__": "4253721088",
                          "pk": 4253721088,
                          "pk_id": "4253721088",
                          "id": "4253721088",
                          "username": "arindom.chatterjee",
                          "full_name": "Arindom",
                          "is_private": false,
                          "is_verified": true,
                          "profile_pic_id": "2429191417533485242_4253721088",
                          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/122662758_212734520197756_8582777109243913279_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=ejXgOZbvYmEQ7kNvwEMQD9n&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GGavTwd8AoIde8EAAD9k1q5OJhx3bkULAAAB1501500j-ccb7-5&oh=00_Af0jQV0HjZ2lQZjoEuVUDiZX1b8PBBOX3huzB7ZHR6GRvQ&oe=69DC4609&_nc_sid=472314"
                        },
                        "display_title": "Bhalobeshe Kono Bhool",
                        "thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/597135326_71060345790014_7336470468630567440_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=BVlDjY8ECMsQ7kNvwEKUb2H&_nc_oc=AdrbgVcNsrhUFcKx9SwBDbcPlXcYlAQHjuaZ06gZeySAWCgBbZ-QQEQQ5i67jKgM1t8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a39b&oh=00_Af2lgAqoG-dQzl88miPObbt0pTNpim-1KAxQ_VF6rMMa3Q&oe=69DC461E",
                        "is_bookmarked": false,
                        "is_explicit": false,
                        "parent_start_time_in_ms": 0,
                        "audio_start_time_in_ms": 0,
                        "duration_in_ms": 30,
                        "is_eligible_for_audio_effects": false,
                        "derived_content_start_time_in_composition_in_ms": 0
                      }
                    ],
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
                "like_count": 564,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18013236944684330",
                  "bit_flags": 0,
                  "created_at": 1775653905,
                  "created_at_utc": 1775653905,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18013236944684330",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870786707311011812,
                  "status": "Active",
                  "type": 1,
                  "user_id": 52722857117,
                  "text": "I cannot live without you🫠🫶🏻💖\n#trending \n#viral \n#transition \n#love",
                  "user": {
                    "strong_id__": "52722857117",
                    "pk": 52722857117,
                    "pk_id": "52722857117",
                    "id": "52722857117",
                    "is_unpublished": false,
                    "fbid_v2": 17841452593530357,
                    "username": "_srkkk_07",
                    "full_name": "🚩",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3863515889765973496_52722857117",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/656813466_18043282949753118_3670872010364444994_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDQwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=u7wKddQogTQQ7kNvwGYYJne&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJotJiceSc0uRRpAAEJhsvGkjvEybmNDAQAB1501500j-ccb7-5&oh=00_Af0LiGFaML4nSzJOIR_FlJEvnGao2f7QT7DYRPV-kIWCrg&oe=69DC2853&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 42,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "locations": [],
                "play_count": 5372,
                "ig_play_count": 5372,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_subtitles_locale": "bn_IN",
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 25.56599998474121,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 2035941,
                    "height": 1280,
                    "id": "1466728111607234v",
                    "type": 101,
                    "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQNREAjRqztL5vMuLIkH605jt2i50mbVdFcgyD8u9stpXO0s2CTw_G0Io4cpF0Dwm8SIi5iQ-BVOTQcTjhpPzd45LZXEEUTZYnQFIOU.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=DGS_Cvprv7QQ7kNvwEe_qYC&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNDQ1ODczMzc3NTMxMTgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5b1d6fcc00c921db&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC81QjRFNzVFM0FBNDJDN0NGQzQ0Q0FEQ0U4RERERkU5Nl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0YxNDc1RDIwMkZFRTBGOTBEMzZERkI1MDMyMDAwRjk2X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACa8iJWmnN2NQBUCKAJDMywXQDmQ5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3PxirAk1epdTYUV2XTyD1n90Yz7eo_MaFxMj6gaSSlqA&oe=69D84DFA",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  },
                  {
                    "bandwidth": 2035941,
                    "height": 1280,
                    "id": "1466728111607234v",
                    "type": 102,
                    "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQNREAjRqztL5vMuLIkH605jt2i50mbVdFcgyD8u9stpXO0s2CTw_G0Io4cpF0Dwm8SIi5iQ-BVOTQcTjhpPzd45LZXEEUTZYnQFIOU.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=DGS_Cvprv7QQ7kNvwEe_qYC&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNDQ1ODczMzc3NTMxMTgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5b1d6fcc00c921db&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC81QjRFNzVFM0FBNDJDN0NGQzQ0Q0FEQ0U4RERERkU5Nl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0YxNDc1RDIwMkZFRTBGOTBEMzZERkI1MDMyMDAwRjk2X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACa8iJWmnN2NQBUCKAJDMywXQDmQ5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3PxirAk1epdTYUV2XTyD1n90Yz7eo_MaFxMj6gaSSlqA&oe=69D84DFA",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT25.566668S\" FBManifestTimestamp=\"1775657923\" FBManifestIdentifier=\"FoaPs50NGBFpZ19kYXNoX2Jhc2ljX3ZwORmG0JmhpdXgrgPIscXQ/fmiBYDh6YOZ5ckFmorR9YHW4QXus8vt4rGCBr6hmqe+0IcHjPiwhsvNsAeEld2ohpanDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT25.566668S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:81.3\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1569642107451456v\" bandwidth=\"407733\" codecs=\"vp09.00.21.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_360p\" FBContentLength=\"1303049\" FBPlaybackResolutionMos=\"0:100,360:74.3,480:70.5,720:63,1080:54.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.8,480:85.2,720:78.3,1080:69.3\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNqE9qPAgC9fMz6iMtHzDrxUWrtLF8Ka0S3OvpUDE_NWU4XLGBu_CoHLo-QxMca7zevRsesUVlS53NzQNAKUrvaArdhVizteYuTvA54b0o3kQ.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=znU9fkFXfDQQ7kNvwG4JAOi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMzYwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA0NDU4NzMzNzc1MzExOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNSwiYml0cmF0ZSI6NDA3NzMzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0ppfCTL1bhsOT6cDFjPLmaXOr9zPI3xirI4f0sfuL0xw&amp;oe=69DC503E</BaseURL><SegmentBase indexRange=\"818-921\" timescale=\"15360\" FBMinimumPrefetchRange=\"922-23424\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"922-140613\" FBFirstSegmentRange=\"922-230560\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"230561-456026\" FBPrefetchSegmentRange=\"922-230560\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1484237300083812v\" bandwidth=\"1033811\" codecs=\"vp09.00.30.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_540p\" FBContentLength=\"3303889\" FBPlaybackResolutionMos=\"0:100,360:86.8,480:82.5,720:76.6,1080:72\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.5,480:94.1,720:91,1080:86.6\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMyNQ_6uod2BCVBF3TNfGAF03LFPoeR3xyUAxVelRA9B8BrUCNsPFtFigSXPXakAzqWn7nnzQurbBopmmii31R4N6PZVroSnOVhQdJ7CtpfHQ.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=z2OgBqqXbDAQ7kNvwG5CYBq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNTQwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA0NDU4NzMzNzc1MzExOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNSwiYml0cmF0ZSI6MTAzMzgxMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1MA7R7IqcHzoQFhgnzRQE0QF2IpFVztuxur1Xh1TndhA&amp;oe=69DC4061</BaseURL><SegmentBase indexRange=\"818-921\" timescale=\"15360\" FBMinimumPrefetchRange=\"922-53940\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"922-354434\" FBFirstSegmentRange=\"922-592512\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"592513-1161908\" FBPrefetchSegmentRange=\"922-592512\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"947240714905192v\" bandwidth=\"1826711\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_720p\" FBContentLength=\"5837864\" FBPlaybackResolutionMos=\"0:100,360:93.9,480:91.5,720:85.3,1080:78.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.8,480:96.9,720:95,1080:92.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6zov6guj_vERCi8jjntf2KgZ2Ix5tfnR5N6YhHxZxwN17G1m-N4RHVeTDTNlH4ig5aXVPlcSWcSFkJypOrWgkztV-hz6NAlMEwT9I0mDiLQ.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=ZFwx5Z1WTZgQ7kNvwFBSyUF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNzIwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODA0NDU4NzMzNzc1MzExOCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyNSwiYml0cmF0ZSI6MTgyNjcxMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af19ekvR6bhS5vfA6WxqnNwgFaFrFFuDjd-z4NOqJX7e3w&amp;oe=69DC1C4F</BaseURL><SegmentBase indexRange=\"818-921\" timescale=\"15360\" FBMinimumPrefetchRange=\"922-68004\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"922-598675\" FBFirstSegmentRange=\"922-1035954\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1035955-2048802\" FBPrefetchSegmentRange=\"922-1035954\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1987100751906911v\" bandwidth=\"2530145\" codecs=\"vp09.00.40.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_1080p\" FBContentLength=\"8085922\" FBPlaybackResolutionMos=\"0:100,360:95.7,480:94.8,720:91.9,1080:85.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.66,480:98.24,720:97,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQM15XQbjwEVsHRBZS-DwlFZprvRD-5hNgVHmYArSOtMgO-_hrE5NCZm3_KlCTodqu25IQHcVqvKVvMA-tnR3xgWPPpFKYHTIEc9TohXoHtBgw.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=g_dnKyaE_GgQ7kNvwFmAu4U&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMTA4MHAiLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjU2NzA2NzM0MzM1MjQyNywiY2xpZW50X25hbWUiOiJpZyIsInhwdl9hc3NldF9pZCI6MTgwNDQ1ODczMzc3NTMxMTgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjUsImJpdHJhdGUiOjI1MzAxNDUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3kvq1FMNABVuN_xT8y-SysWzcJro6zh483859Jzd-l3A&amp;oe=69DC2425</BaseURL><SegmentBase indexRange=\"818-921\" timescale=\"15360\" FBMinimumPrefetchRange=\"922-82812\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"922-826539\" FBFirstSegmentRange=\"922-1446915\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1446916-2871048\" FBPrefetchSegmentRange=\"922-1446915\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1694102988614903a\" bandwidth=\"45651\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45651\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"146817\" FBPaqMos=\"90.98\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMO7Md-fKt_GWgeS73hgv3ytr7zdg_xs2KOj-SBsnwnmato6yyjJphFHFa395rVE6_dq04KWWN0lp43GkFERT6b620SCFsPLEVDPF4.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=TYQH_AlOhh8Q7kNvwEpAQlO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDQ0NTg3MzM3NzUzMTE4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI1LCJiaXRyYXRlIjo0NTk0NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3tFGnEwtHYRp01Hra0Q6lZg6rY_RbxL7EE3koG6pQqEQ&amp;oe=69DC4280</BaseURL><SegmentBase indexRange=\"837-940\" timescale=\"44100\" FBMinimumPrefetchRange=\"941-2153\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"941-14680\" FBFirstSegmentRange=\"941-26779\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"26780-54105\" FBPrefetchSegmentRange=\"941-26779\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"4308265362761026a\" bandwidth=\"82373\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"82373\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"264160\" FBPaqMos=\"91.55\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOoJ__PFMiaalg-Oj1jNJvqGBTa0phb0eDNGDlBZ5PzcXxbtG1lGaE118OWH3tx7RIPg4Uy2Si4eVPmG68VPQOOSQasHZa8T-NnKw0.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=YDSIReLYo6cQ7kNvwFR2Q5G&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDQ0NTg3MzM3NzUzMTE4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI1LCJiaXRyYXRlIjo4MjY2NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1PrIi1SwV-lVC4uyMwFsJr8o7TRCI6KCFl5ecRZG0QbA&amp;oe=69DC462C</BaseURL><SegmentBase indexRange=\"838-941\" timescale=\"44100\" FBMinimumPrefetchRange=\"942-2887\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"942-26014\" FBFirstSegmentRange=\"942-48352\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"48353-96106\" FBPrefetchSegmentRange=\"942-48352\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1622157865656973a\" bandwidth=\"118666\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"118666\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"380127\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMmwXXrjJi4YUAA5-3UyCRo9Kr0QePRwoCOMoK9lgZLtFVJRdupnG_c8L4uwnjcd1AzXWXntEQJA-flaulCQpax7Wt1GzCph-fDEcQ.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=FagGER70zYgQ7kNvwG4Rv0l&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDQ0NTg3MzM3NzUzMTE4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI1LCJiaXRyYXRlIjoxMTg5NTgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af04NZdJK8uBaYPISS2THaOPMWTmOGf3CrOV1D0CvGXVRQ&amp;oe=69DC288F</BaseURL><SegmentBase indexRange=\"833-936\" timescale=\"44100\" FBMinimumPrefetchRange=\"937-2619\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"937-37071\" FBFirstSegmentRange=\"937-70132\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"70133-140612\" FBPrefetchSegmentRange=\"937-70132\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2077210876190214a\" bandwidth=\"143778\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"143778\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"460372\" FBPaqMos=\"94.54\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNqL1ahw2I8dDASUi7HO2Ch_jmu4Lug3dDZNwN3kbG6HRY1yRyuX8wJdBQWvw3_-Zp3kMCTm59UPCz1Gu7ykHzRnxQroeaCGHcE228.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=OrOyRxjgoeEQ7kNvwHCQh2W&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDQ0NTg3MzM3NzUzMTE4LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjI1LCJiaXRyYXRlIjoxNDQwNzAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1aHnaE4Sc1ir4vSpAfT9rCmZnNIaBEkYQvq3faC-AJBw&amp;oe=69DC4C27</BaseURL><SegmentBase indexRange=\"833-936\" timescale=\"44100\" FBMinimumPrefetchRange=\"937-2766\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"937-44206\" FBFirstSegmentRange=\"937-85520\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"85521-172784\" FBPrefetchSegmentRange=\"937-85520\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "number_of_qualities": 4,
                "video_codec": "vp09.00.21.08.00.01.01.01.00",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "52722857117",
                  "id": "52722857117",
                  "username": "_srkkk_07",
                  "full_name": "🚩",
                  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/656813466_18043282949753118_3670872010364444994_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDQwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=u7wKddQogTQQ7kNvwGYYJne&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJotJiceSc0uRRpAAEJhsvGkjvEybmNDAQAB1501500j-ccb7-5&oh=00_Af0LiGFaML4nSzJOIR_FlJEvnGao2f7QT7DYRPV-kIWCrg&oe=69DC2853&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3zACCk6fk",
                "device_timestamp": 1775653744208646,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQNREAjRqztL5vMuLIkH605jt2i50mbVdFcgyD8u9stpXO0s2CTw_G0Io4cpF0Dwm8SIi5iQ-BVOTQcTjhpPzd45LZXEEUTZYnQFIOU.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=DGS_Cvprv7QQ7kNvwEe_qYC&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwNDQ1ODczMzc3NTMxMTgsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5b1d6fcc00c921db&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC81QjRFNzVFM0FBNDJDN0NGQzQ0Q0FEQ0U4RERERkU5Nl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0YxNDc1RDIwMkZFRTBGOTBEMzZERkI1MDMyMDAwRjk2X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACa8iJWmnN2NQBUCKAJDMywXQDmQ5WBBiTcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3PxirAk1epdTYUV2XTyD1n90Yz7eo_MaFxMj6gaSSlqA&oe=69D84DFA",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      5167,
                      10334
                    ],
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/660422205_1273796614179190_6470373456327365366_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=Mzg3MDc4NjcwNzMxMTAxMTgxMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vKTKg30TAKgQ7kNvwHq904K&_nc_oc=AdrWIA4UgCGDLT1PxXh2p5WTA6xsfb6n1Fn3owxZUqrNFCjy14bcPibPdFshgZPAj0o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af2AwfNdcC9SYjvrTt6vXfkG-UhNr0h4GO40wceOZSRQ2Q&oe=69DC2015",
                    "width": 640,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/660422205_1273796614179190_6470373456327365366_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=Mzg3MDc4NjcwNzMxMTAxMTgxMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vKTKg30TAKgQ7kNvwHq904K&_nc_oc=AdrWIA4UgCGDLT1PxXh2p5WTA6xsfb6n1Fn3owxZUqrNFCjy14bcPibPdFshgZPAj0o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af2AwfNdcC9SYjvrTt6vXfkG-UhNr0h4GO40wceOZSRQ2Q&oe=69DC2015",
                "location": null,
                "usertags": [],
                "taken_at_ts": 1775653917,
                "sponsor_tags": []
              }
            }
          ]
        }
      },
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
                "strong_id__": "3870683396108475242_1397919593",
                "id": "3870683396108475242_1397919593",
                "disable_caption_and_comment": false,
                "fbid": 18090886510913353,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDY4MzM5NjEwODQ3NTI0Mg==.3",
                "integrity_review_decision": "pending",
                "pk": "3870683396108475242",
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
                        859,
                        1718
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/660871105_926931340186081_1352352723654319752_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=hTiK8eGO71oQ7kNvwGuxKdK&_nc_oc=AdpGhVLs7Y3StMKbPf-61VJ8EVV0OOwRg9X80TSDIVYLCAr4_52biUc102tqOKDEOew&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af1VHMeWxb0nNII9Cl_rqcAAXw-z8WkM8pIJajT-NDJeFw&oe=69DC3BF2",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "igtv_first_frame": {
                      "estimated_scans_sizes": [
                        859,
                        1718
                      ],
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/660871105_926931340186081_1352352723654319752_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=hTiK8eGO71oQ7kNvwGuxKdK&_nc_oc=AdpGhVLs7Y3StMKbPf-61VJ8EVV0OOwRg9X80TSDIVYLCAr4_52biUc102tqOKDEOew&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af1VHMeWxb0nNII9Cl_rqcAAXw-z8WkM8pIJajT-NDJeFw&oe=69DC3BF2",
                      "width": 640,
                      "is_spatial_image": false
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "estimated_scans_sizes": [
                        30737,
                        61475
                      ],
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660537255_18571999486031594_6016905875916389973_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=109&ig_cache_key=Mzg3MDY4MzM5NjEwODQ3NTI0MjE4NTcxOTk5NDgzMDMxNTk0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIzMDR4NDA5Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=sGmMZkPtox8Q7kNvwG7dx6E&_nc_oc=Ado2OBw5RXlnSWFrXDyBqyrgLhP_0wn-UURT_7kkaj4ekVI-D14Dh-VJY7UbfVo_tfA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af0OmUPOKDLlVxzqI1mjBRil1hC6u5E8yU8xUIjcMsGdmA&oe=69DC35C0",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_cropping_info": {
                  "four_by_three_crop": {
                    "crop_left": 0.08121151186592601,
                    "crop_right": 0.8372520151891991,
                    "crop_top": 0.045688778618097003,
                    "crop_bottom": 0.612447199094967
                  }
                },
                "media_type": 2,
                "original_width": 1080,
                "original_height": 1920,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMTFkYjIwNmVkM2FmNDdkNmIxYjZlZjRjZjI0YjUyYTAzODcwNjgzMzk2MTA4NDc1MjQyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyMjM4NXwzODcwNjgzMzk2MTA4NDc1MjQyfDMwMDA5MzA1OTIwfGU4MzFhNDQyYWY2OGRmNGQ3MzFiOTkwNzUxZGMzOWZmYWYwMmFiYTJlNTRhZDYyNzk2NzU2MjdjMGM4OTNjNjYifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": null,
                "has_tagged_users": true,
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775641890,
                "photo_of_you": false,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "is_artist_pick": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "clips",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "cutout_sticker_info": [],
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "media_ui_attributions_data": [],
                "media_ui_attributions_data_v2": [],
                "creator_product_link_infos": [],
                "is_eligible_for_poe": true,
                "is_eligible_for_organic_eager_refresh": false,
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
                "coauthor_producers": [
                  {
                    "strong_id__": "67375031502",
                    "pk": 67375031502,
                    "pk_id": "67375031502",
                    "id": "67375031502",
                    "username": "bloggerlifestylebackup90",
                    "full_name": "Fatima",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3716054787822493187_67375031502",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/541938978_17904784644247503_433535692113981683_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=qT4qnc5hss8Q7kNvwF-6XJk&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCJVTSDPD4CITpw-APMw6D1qOgQGbmNDAQAB1501500j-ccb7-5&oh=00_Af2KznXrp1LNJxWditN_iuy0qcFHccE8HL7Nw4Gbe4lzGw&oe=69DC3D2C&_nc_sid=472314",
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
                    "strong_id__": "21234794002",
                    "pk": 21234794002,
                    "pk_id": "21234794002",
                    "id": "21234794002",
                    "username": "bloggerlyfestyle90",
                    "full_name": "Fatima Najem",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "3866003823173641185_21234794002",
                    "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658434233_18113753554706003_7356276716794235660_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=F7Kg0Yz8uLoQ7kNvwEGeGnL&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GLnoPidTXi3mXFpAAAxL-92yvhZmbmNDAQAB1501500j-ccb7-5&oh=00_Af3B5vx1kgUh8nv_s-CkbeG7ogg8cgWmWX9otBcKgQjBhw&oe=69DC1FE7&_nc_sid=472314",
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
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "collab_follow_button_info": {
                  "show_follow_button": true,
                  "is_owner_in_author_exp": true
                },
                "igbio_product": null,
                "is_paid_partnership": false,
                "reshare_count": 195,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 8,
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
                    "best_audio_cluster_id": "1160528862657498"
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
                  "music_canonical_id": "18421181614106507",
                  "music_info": null,
                  "nux_info": null,
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": 3169781663184757,
                    "attributed_custom_audio_asset_id": null,
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": true,
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT11.447437S\" FBManifestTimestamp=\"1775657923\" FBManifestIdentifier=\"FoaPs50NKRaY8svW8eCHBCIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT11.447437S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1142957594475660a\" bandwidth=\"64840\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"64840\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQOFmlBnYm0Chq8cMmOGuHwmzJw4HnU_Q0FflmbhHLWMLzCUgDzvQJ1cQfbcndnBhcPi0ibuhb5ieWtRGd69vZ7b.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=Y6eByx180H4Q7kNvwFeG2Ge&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjExNjY1NTIzODIwMDA1OTgsImFzc2V0X2FnZV9kYXlzIjoxODYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMSwiYml0cmF0ZSI6NjU0ODgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2N-TERLL99u7EookRpq9s1M-6tujUqJVABAYkBP3DEjw&amp;oe=69D853E2</BaseURL><SegmentBase indexRange=\"824-927\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 11445,
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
                    "original_media_id": 3735851220632911972,
                    "progressive_download_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNgeI5k83uFVeoJcI_FuWeCpztKtOp4RxXceCEwiKmR4fiTxW-IxPEI0rRBYmvDHGM_Ro3_IyAKrXwP8JGw578.mp4?_nc_cat=105&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=49LUB1tDpz4Q7kNvwFp_1zq&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTE2NjU1MjM4MjAwMDU5OCwiYXNzZXRfYWdlX2RheXMiOjE4NiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af1zfgDPKTTWNau6i2Zxx5vi6Sa6Ad2SaDSwMXgAki5jjQ&oe=69D85023",
                    "should_mute_audio": false,
                    "time_created": 1759568600,
                    "trend_rank": null,
                    "previous_trend_rank": null,
                    "overlap_duration_in_ms": 11445,
                    "audio_asset_start_time_in_ms": 2693,
                    "derived_content_start_time_in_composition_in_ms": 0,
                    "ig_artist": {
                      "strong_id__": "2885730639",
                      "pk": 2885730639,
                      "pk_id": "2885730639",
                      "id": "2885730639",
                      "username": "drnigargazizada",
                      "full_name": "Nigar Gazizada",
                      "is_private": false,
                      "is_verified": true,
                      "profile_pic_id": "3506446524164198791_2885730639",
                      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/467947064_586156540458164_6143293410722666247_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=2MmBs4d9POAQ7kNvwEZdZy7&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDhO5Bu0dGA0GxUCAAdXH-nOXEFVbkULAAAB1501500j-ccb7-5&oh=00_Af1vpAmU5mnlGzoN12hEP4LuYltaAYyiyqxVr6_A2N1QTA&oe=69DC362A&_nc_sid=472314"
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
                "like_count": 427,
                "top_likers": [],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18090894832913353",
                  "bit_flags": 0,
                  "created_at": 1775650497,
                  "created_at_utc": 1775650497,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18090894832913353",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870683396108475242,
                  "status": "Active",
                  "type": 1,
                  "user_id": 1397919593,
                  "text": "Main Character Today 🎂🐏♈️\n\n#birthday #instalike #itsmybirthday❤️ #instamood fashion",
                  "user": {
                    "strong_id__": "1397919593",
                    "pk": 1397919593,
                    "pk_id": "1397919593",
                    "id": "1397919593",
                    "is_unpublished": false,
                    "fbid_v2": 17841400947811842,
                    "username": "bloggerlifestyle90",
                    "full_name": "Fatima Najem 🧿",
                    "is_private": false,
                    "is_verified": true,
                    "profile_pic_id": "3843454044812259950_1397919593",
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/642273345_18563244883031594_1541363361549072420_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=iQHw1eXUygMQ7kNvwGaj2za&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GEFQSCYqtiFBLPNBACQ475LPBWQVbmNDAQAB1501500j-ccb7-5&oh=00_Af0HwNPt4ii2OYPVkOt_N-_3ryJ0IRnrWWVfxkFppYt4mg&oe=69DC36F3&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 116,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
                "location": {
                  "pk": 150060615646573,
                  "name": "Virginia, USA",
                  "phone": "",
                  "website": "",
                  "category": "",
                  "hours": {},
                  "address": "",
                  "city": "",
                  "zip": null,
                  "lng": -77.179121701349,
                  "lat": 38.868419085543,
                  "external_id": "150060615646573",
                  "external_id_source": "facebook_places"
                },
                "locations": [],
                "lng": -77.179121701349,
                "lat": 38.868419085543,
                "play_count": 8726,
                "ig_play_count": 8726,
                "shop_routing_user_id": null,
                "featured_products": [],
                "are_remixes_crosspostable": true,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "is_eligible_for_autodub": false,
                "is_eligible_for_autodub_upsell": false,
                "video_sticker_locales": [],
                "has_audio": true,
                "video_duration": 4.875999927520752,
                "is_dash_eligible": 1,
                "video_versions": [
                  {
                    "bandwidth": 1491851,
                    "height": 1280,
                    "id": "721202997684002v",
                    "type": 101,
                    "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPYNG1OIRafYi3zdfr8li8mWMFcvtMa6vNhlYt6g7CCFmfsB8doMEkGeGm8e-6yt_obvOoERmTG3rmll_mFABLWnx4PWY_rkkWfS9g.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=NRp7evsTJlwQ7kNvwECyGKP&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU3MTExODkxMTUwNjAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=8d73f620de3ba41c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84RTQ4OEU4MUIxRTM4REQzNjdBMEZGNDA2MjhFRTVBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U3NEJBM0ZGNUM4MTUwMDRGNTZFM0Q3RDVDNUJGODlDX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbogu-x-aflPxUCKAJDMywXQBN2yLQ5WBAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1sLlqw3PFDdVC7l4elnWFKWThCoBt4i69yzZa7xJzljw&oe=69D844F5",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  },
                  {
                    "bandwidth": 1491851,
                    "height": 1280,
                    "id": "721202997684002v",
                    "type": 102,
                    "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPYNG1OIRafYi3zdfr8li8mWMFcvtMa6vNhlYt6g7CCFmfsB8doMEkGeGm8e-6yt_obvOoERmTG3rmll_mFABLWnx4PWY_rkkWfS9g.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=NRp7evsTJlwQ7kNvwECyGKP&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU3MTExODkxMTUwNjAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=8d73f620de3ba41c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84RTQ4OEU4MUIxRTM4REQzNjdBMEZGNDA2MjhFRTVBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U3NEJBM0ZGNUM4MTUwMDRGNTZFM0Q3RDVDNUJGODlDX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbogu-x-aflPxUCKAJDMywXQBN2yLQ5WBAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1sLlqw3PFDdVC7l4elnWFKWThCoBt4i69yzZa7xJzljw&oe=69D844F5",
                    "url_expiration_timestamp_us": null,
                    "width": 720,
                    "fallback": null
                  }
                ],
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT4.876191S\" FBManifestTimestamp=\"1775657923\" FBManifestIdentifier=\"FoaPs50NGA9yMmF2MS1yMWdlbjJ2cDkZxqSAmOis/f8Cvp39q+mtpQPSntCblZGsA5TIgPyS3bQDus2JypS18AOi0+KcoIeTB9y29tj88LsH/qOFjsfmnAiC2cGWi4naCMjzs4jHnLIK6ruxgeC3+wvupuy7wY/vDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT4.876191S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:74.9\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1091628829848413v\" bandwidth=\"252264\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"153461\" FBPlaybackResolutionMos=\"0:100,360:65.5,480:61.7,720:58.8,1080:59.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.5,480:87.4,720:79.4,1080:70.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNkKMr0ah3sYJKs0kcCcKsIizvhkV_bVrimUqxHGnnsmrFAhNFawIXJVa3h6lAknUUtcKybek6h_0aG9tI8QbX-IyqlNzlbR6PGmpo.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=FiXo48PSnroQ7kNvwFosNJF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjoyNTIyNjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0dI8qJOs45nON-VIxe9xe4DiaL7_1x9Qvi4GDKxHxZRQ&amp;oe=69DC2830</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1663\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-90124\" FBFirstSegmentRange=\"870-153460\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-153460\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"844379405352978v\" bandwidth=\"340287\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"207008\" FBPlaybackResolutionMos=\"0:100,360:71.8,480:68.2,720:64.8,1080:64.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:91.6,720:84.9,1080:77\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNU2PtQJmaARTNc-IZU1jxYK54N7UOK_oPZFI3htY6V1Cg58qWIYLWfOa1Ht9EOa9kmrpC-o2eid7wsOEw09uK96KghSFx6vzDOvDA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=pT4xOsk4C74Q7kNvwGmqIVH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjozNDAyODcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0_4wdcF3ABwhVmjbPkXFBVg9o20jg0Q8Qg3VCtsB2ImA&amp;oe=69DC4401</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1670\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-118658\" FBFirstSegmentRange=\"870-207007\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-207007\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"941476858693545v\" bandwidth=\"425697\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"258966\" FBPlaybackResolutionMos=\"0:100,360:74.6,480:71.4,720:68.3,1080:67.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.5,480:93.2,720:87.7,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO9u8A8V1KAhRAglprFA28zHy76EE5c35x7RKeAQU2lurwwIq_5A5y-RZuWH2HdPabsH2j4fq9qPJKXmNAEypWvWaqQGzlY31p8T1E.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=bcQuXZM2nX0Q7kNvwG1sILN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjo0MjU2OTcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2OYiwKabeW1BFySXuebZGE0eBJkTD3RqbeqZEKeKGdOQ&amp;oe=69DC2704</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1757\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-147266\" FBFirstSegmentRange=\"870-258965\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-258965\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2102008090643886v\" bandwidth=\"553765\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"336874\" FBPlaybackResolutionMos=\"0:100,360:78.1,480:75.2,720:72.1,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:95.2,720:91.1,1080:85.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOB69HnnasXTK7QofV3a7Q5ISENW5hDlA1sqdgDne5HdQP7ovj7TL9pOQGVgOMGWeSrK3FoKU5NqeMQ14mXU_U3dkjK3YiwTYoewzg.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=He_Q-95CuxwQ7kNvwFwYEpc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjo1NTM3NjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Mof1jI0pSvFNSwU6D3d4CdkD28bArJUQfY4NSzziNYg&amp;oe=69DC431F</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1763\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-187164\" FBFirstSegmentRange=\"870-336873\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-336873\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2012230863049937v\" bandwidth=\"679354\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"413274\" FBPlaybackResolutionMos=\"0:100,360:81.7,480:77.9,720:75,1080:73.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.5,720:92.9,1080:88.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNSGnOM8el_wXk3CBQui-_Ty-PWrMfIb5rVmz2YOPb8Pgou4lQVgu0Xi7ej2b8_jlFKT8zV0qcv1y7cKXvfFDyZo2oH1mhd7Xrf1Tc.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=kEK7_vTIY_MQ7kNvwHDZlPt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjo2NzkzNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3QNnyq2gYInvYgySxsVD1peth6DdLefVGcaMxEVIPc2g&amp;oe=69DC2E37</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1763\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-226594\" FBFirstSegmentRange=\"870-413273\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-413273\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4466482716969399v\" bandwidth=\"888491\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"540499\" FBPlaybackResolutionMos=\"0:100,360:84.8,480:81.5,720:77.6,1080:76\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.65,480:97.9,720:95.2,1080:91.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOG4mH52Ce0VoIVqmccQR1yZ9cav6pk2UmG_GZs0wBQko5S6_9Oa4gXQXeOu1LcUCtkVq-feIqn7UC2v263QF2YdpleDtySRZw7A28.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=-vzkB3CZdy0Q7kNvwGNGGP4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjo4ODg0OTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0X2LTWC_onq5ttCV4_YIVAluA1NIyVfMKONAB5PuKESg&amp;oe=69DC3279</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1778\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-293491\" FBFirstSegmentRange=\"870-540498\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-540498\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"3367662383410933v\" bandwidth=\"1123582\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"683513\" FBPlaybackResolutionMos=\"0:100,360:87,480:84.1,720:80.4,1080:78\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.015,480:98.53,720:96.6,1080:93.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOdMhLhmWPEGyigJLVz1Op6TfFody9YyXRAdA7SDGh4Rs9hjucM8kaloybKwXcgOBETKDCZ_qARo9XX3c0KdlHfDSJAsfkLIY7jMIU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=lX3ZgTbO1coQ7kNvwELU8OT&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjoxMTIzNTgyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1s4Z9O_5Ew8GRo_goKKM3RgVNd8wMIdKUViKr1orNeLQ&amp;oe=69DC3F59</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1757\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-370812\" FBFirstSegmentRange=\"870-683512\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-683512\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2925191504493796v\" bandwidth=\"1599622\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"973104\" FBPlaybackResolutionMos=\"0:100,360:89.7,480:87.3,720:84.3,1080:82.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.324,480:99.111,720:98.17,1080:95.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOdOQN-CwS2naUrHQOwcIQxx8p_APRL7PztPiGX5wqLOMePPT61Cf10d-oaXHq9RiBf0JGj24zwou9XZumZG6FImle_i1JwbRJYa8M.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=jLT8wiw_bCsQ7kNvwF5UqXA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTcxMTE4OTExNTA2MCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0LCJiaXRyYXRlIjoxNTk5NjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af30hSVYW3XDAqemWk9pQpkkvKIo1LxkGYrPk9OWr7ePfA&amp;oe=69DC4A02</BaseURL><SegmentBase indexRange=\"826-869\" timescale=\"15360\" FBMinimumPrefetchRange=\"870-1920\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"870-523766\" FBFirstSegmentRange=\"870-973103\" FBFirstSegmentDuration=\"4866\" FBPrefetchSegmentRange=\"870-973103\" FBPrefetchSegmentDuration=\"4866\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"960374413201930a\" bandwidth=\"48174\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"48174\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"30244\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMhe-ZBXT2AnB6n4opoChK90NpTf5xgrX8RBbYeA7noaoH_jzX_j0L8VA92ifjyhQlSYrD6C60HDIcq8KsVVdo8dcX6q7ylPF-rziE.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=QANdS9TaiBoQ7kNvwFWJfwj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NzExMTg5MTE1MDYwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQsImJpdHJhdGUiOjQ5NjE5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1HLyYO4n9Z0tPWfgjhSK2ATfJivMYEkSRgFrhb69fF4g&amp;oe=69DC2E95</BaseURL><SegmentBase indexRange=\"837-880\" timescale=\"44100\" FBMinimumPrefetchRange=\"881-2205\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"881-16715\" FBFirstSegmentRange=\"881-30243\" FBFirstSegmentDuration=\"4876\" FBPrefetchSegmentRange=\"881-30243\" FBPrefetchSegmentDuration=\"4876\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2315134355679487a\" bandwidth=\"86886\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"86886\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"53841\" FBPaqMos=\"90.75\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOvWX5Oe8PLUTBqZeTqH6l8l6WSf2kQjOIMUanNBHTM72uiSlAOsa-DTl97SeDGZFm9mmSU64FThWPVrI98BkxsURxlyU7KU5XzNbA.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=LjTMU9DCutMQ7kNvwH8GiP-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NzExMTg5MTE1MDYwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQsImJpdHJhdGUiOjg4MzMyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3_ScwuSfGslcZInzI4oeoObquko-Jdm2rEs_PYBBW_eA&amp;oe=69DC2E6E</BaseURL><SegmentBase indexRange=\"838-881\" timescale=\"44100\" FBMinimumPrefetchRange=\"882-3008\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-29322\" FBFirstSegmentRange=\"882-53840\" FBFirstSegmentDuration=\"4876\" FBPrefetchSegmentRange=\"882-53840\" FBPrefetchSegmentDuration=\"4876\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"2449868025509441a\" bandwidth=\"135424\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"135424\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"83421\" FBPaqMos=\"94.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPE4ooMrcEe5QssQBZh55-fAk8MJWW-KoAo-6wc4uR0jSyQJBsNJ7gLcwf-8qTPhyWBm_gGo45KTXNI7Woc0CFhzlaMvcdJEwYSv6I.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=dErN1wFl0XYQ7kNvwG2DRSJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NzExMTg5MTE1MDYwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQsImJpdHJhdGUiOjEzNjg2MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0bvxYwidXntpjFxiMFiWkiU83QxV-W5ueG2r-YWTzYNw&amp;oe=69DC3B80</BaseURL><SegmentBase indexRange=\"833-876\" timescale=\"44100\" FBMinimumPrefetchRange=\"877-2594\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"877-45181\" FBFirstSegmentRange=\"877-83420\" FBFirstSegmentDuration=\"4876\" FBPrefetchSegmentRange=\"877-83420\" FBPrefetchSegmentDuration=\"4876\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"926576023676767a\" bandwidth=\"158254\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"158254\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"97336\" FBPaqMos=\"94.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPI-QqrW5iKyYIi1wi0oRIjik1_dK6ZAXDx2Vqwu8znLLcJINDIk1FWMzCvRilZ2CMmuhyNkVdoSvnFcV04x_pS__jhp1GIcYvWfhw.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=kiUv4TcTTwcQ7kNvwG1CVpR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NzExMTg5MTE1MDYwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQsImJpdHJhdGUiOjE1OTY5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=29AFVmiyV9b9FM9AEszTtA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3LhWhRpz2kD2utfB8kg3sgvjeokenrOCVsNLy9jxB_2Q&amp;oe=69DC1F3E</BaseURL><SegmentBase indexRange=\"833-876\" timescale=\"44100\" FBMinimumPrefetchRange=\"877-2709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"877-52936\" FBFirstSegmentRange=\"877-97335\" FBFirstSegmentDuration=\"4876\" FBPrefetchSegmentRange=\"877-97335\" FBPrefetchSegmentDuration=\"4876\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "number_of_qualities": 8,
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "user": {
                  "pk": "1397919593",
                  "id": "1397919593",
                  "username": "bloggerlifestyle90",
                  "full_name": "Fatima Najem 🧿",
                  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/642273345_18563244883031594_1541363361549072420_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=iQHw1eXUygMQ7kNvwGaj2za&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GEFQSCYqtiFBLPNBACQ475LPBWQVbmNDAQAB1501500j-ccb7-5&oh=00_Af0HwNPt4ii2OYPVkOt_N-_3ryJ0IRnrWWVfxkFppYt4mg&oe=69DC36F3&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": true,
                "code": "DW3bgp_DFtq",
                "device_timestamp": 1775641433353491,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "is_post_live_clips_media": false,
                "like_and_view_counts_disabled": false,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPYNG1OIRafYi3zdfr8li8mWMFcvtMa6vNhlYt6g7CCFmfsB8doMEkGeGm8e-6yt_obvOoERmTG3rmll_mFABLWnx4PWY_rkkWfS9g.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=NRp7evsTJlwQ7kNvwECyGKP&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU3MTExODkxMTUwNjAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=8d73f620de3ba41c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84RTQ4OEU4MUIxRTM4REQzNjdBMEZGNDA2MjhFRTVBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U3NEJBM0ZGNUM4MTUwMDRGNTZFM0Q3RDVDNUJGODlDX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbogu-x-aflPxUCKAJDMywXQBN2yLQ5WBAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1sLlqw3PFDdVC7l4elnWFKWThCoBt4i69yzZa7xJzljw&oe=69D844F5",
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      30737,
                      61475
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660537255_18571999486031594_6016905875916389973_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=109&ig_cache_key=Mzg3MDY4MzM5NjEwODQ3NTI0MjE4NTcxOTk5NDgzMDMxNTk0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIzMDR4NDA5Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=sGmMZkPtox8Q7kNvwG7dx6E&_nc_oc=Ado2OBw5RXlnSWFrXDyBqyrgLhP_0wn-UURT_7kkaj4ekVI-D14Dh-VJY7UbfVo_tfA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af0OmUPOKDLlVxzqI1mjBRil1hC6u5E8yU8xUIjcMsGdmA&oe=69DC35C0",
                    "width": 750,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660537255_18571999486031594_6016905875916389973_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=109&ig_cache_key=Mzg3MDY4MzM5NjEwODQ3NTI0MjE4NTcxOTk5NDgzMDMxNTk0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIzMDR4NDA5Ni5zZHIuQzMifQ%3D%3D&_nc_ohc=sGmMZkPtox8Q7kNvwG7dx6E&_nc_oc=Ado2OBw5RXlnSWFrXDyBqyrgLhP_0wn-UURT_7kkaj4ekVI-D14Dh-VJY7UbfVo_tfA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af0OmUPOKDLlVxzqI1mjBRil1hC6u5E8yU8xUIjcMsGdmA&oe=69DC35C0",
                "usertags": [],
                "taken_at_ts": 1775641890,
                "sponsor_tags": []
              }
            },
            {
              "media": {
                "strong_id__": "3870729737757151899_49646700667",
                "id": "3870729737757151899_49646700667",
                "fbid": 18096271229088381,
                "deleted_reason": 0,
                "client_cache_key": "Mzg3MDcyOTczNzc1NzE1MTg5OQ==.3",
                "integrity_review_decision": "pending",
                "pk": "3870729737757151899",
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
                        31926,
                        63853
                      ],
                      "height": 1800,
                      "scans_profile": "e35",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af0888hHAs2X-tcqp0-p044Z_8sFnL2oR76oEkDmqUyFRg&oe=69DC4396",
                      "width": 1440,
                      "is_spatial_image": false
                    },
                    {
                      "estimated_scans_sizes": [
                        15722,
                        31445
                      ],
                      "height": 938,
                      "scans_profile": "e35",
                      "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af3fb4skkdmFWl_iRJfUs74vO2MmvEINjzJn6LyMoNteSA&oe=69DC4396",
                      "width": 750,
                      "is_spatial_image": false
                    }
                  ]
                },
                "media_type": 1,
                "original_width": 1440,
                "original_height": 1800,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMTFkYjIwNmVkM2FmNDdkNmIxYjZlZjRjZjI0YjUyYTAzODcwNzI5NzM3NzU3MTUxODk5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzkyMjM4NnwzODcwNzI5NzM3NzU3MTUxODk5fDMwMDA5MzA1OTIwfDVjNTNlZmRhNjMxMDg1YWY4ZTA1Y2Q5ZTk1ZjIwNzAzZWI3OGZhYzc3OTAxZGExZjg5M2FmMmM4ZjEzNDdkNzkifSwic2lnbmF0dXJlIjoiIn0=",
                "music_metadata": {
                  "audio_type": "licensed_music",
                  "music_canonical_id": "18356424895008836",
                  "pinned_media_ids": [],
                  "music_info": {
                    "music_canonical_id": 18356424895008836,
                    "music_asset_info": {
                      "allows_saving": false,
                      "artist_id": "2283138201970465",
                      "audio_asset_id": "541406764688578",
                      "audio_cluster_id": "1160377154637454",
                      "cover_artwork_thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/427913851_425943576536267_3463236288605832735_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=nA18uJ4rm4cQ7kNvwETn6Eh&_nc_oc=Adq5zsaNrDbvcGHKyqnt0APrn2l6ByyxvmZUolQ-JUcH0Qb8PrSHlT_N9yP8gBeyhGQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a39b&oh=00_Af0rMnaLQpMgGacfs1OqgQzz9DPNCrZ0mgPQcTljGXlBnw&oe=69DC249B",
                      "cover_artwork_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/427913851_425943576536267_3463236288605832735_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=nA18uJ4rm4cQ7kNvwETn6Eh&_nc_oc=Adq5zsaNrDbvcGHKyqnt0APrn2l6ByyxvmZUolQ-JUcH0Qb8PrSHlT_N9yP8gBeyhGQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a39b&oh=00_Af0rMnaLQpMgGacfs1OqgQzz9DPNCrZ0mgPQcTljGXlBnw&oe=69DC249B",
                      "dark_message": null,
                      "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT304.535675S\"><Period id=\"0\" duration=\"PT304.535675S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2262677247504857a\" bandwidth=\"75616\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"75616\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQMpZvFrpN7erLyNXXM-8zMuaOgqiXi24KMUD9FaPc6TtGOzf_h6ZMOwldz_fRqNsQu2Q17Khsy75m-saHb4HKBw.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=iJaUihDDTiwQ7kNvwHka3xB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo4MDA2NjUwNTE0ODkxNDEsImFzc2V0X2FnZV9kYXlzIjoxMTA1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzA0LCJiaXRyYXRlIjo3NTY4NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1RUO2-A6116KQXHS8R24qM3Fbgu9h-CfpKuRmveVQtLQ&amp;oe=69DC3806</BaseURL><SegmentBase indexRange=\"824-2691\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                      "display_artist": "Elevation Worship",
                      "duration_in_ms": 304535,
                      "fast_start_progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQMpZvFrpN7erLyNXXM-8zMuaOgqiXi24KMUD9FaPc6TtGOzf_h6ZMOwldz_fRqNsQu2Q17Khsy75m-saHb4HKBw.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=iJaUihDDTiwQ7kNvwHka3xB&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo4MDA2NjUwNTE0ODkxNDEsImFzc2V0X2FnZV9kYXlzIjoxMTA1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzA0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e87326c5858928f2&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT3E1UlNCMzlNb2h5a2NOQUNhSjIyeF90a01sYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm6o3Tv-uM7AIVAigCQzMsF0BzCI9cKPXDGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af0xXtlctXhhF0WQRWblns62-Ita-bqAgtbfO1bxE8T3yQ&oe=69DC3806",
                      "has_lyrics": true,
                      "highlight_start_times_in_ms": [
                        48000,
                        105000
                      ],
                      "id": "541406764688578",
                      "ig_username": "elevationworship",
                      "is_eligible_for_audio_effects": true,
                      "is_eligible_for_vinyl_sticker": true,
                      "is_explicit": false,
                      "licensed_music_subtype": "DEFAULT",
                      "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQMpZvFrpN7erLyNXXM-8zMuaOgqiXi24KMUD9FaPc6TtGOzf_h6ZMOwldz_fRqNsQu2Q17Khsy75m-saHb4HKBw.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=iJaUihDDTiwQ7kNvwHka3xB&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo4MDA2NjUwNTE0ODkxNDEsImFzc2V0X2FnZV9kYXlzIjoxMTA1LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzA0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e87326c5858928f2&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT3E1UlNCMzlNb2h5a2NOQUNhSjIyeF90a01sYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm6o3Tv-uM7AIVAigCQzMsF0BzCI9cKPXDGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af0xXtlctXhhF0WQRWblns62-Ita-bqAgtbfO1bxE8T3yQ&oe=69DC3806",
                      "reactive_audio_download_url": null,
                      "sanitized_title": null,
                      "song_monetization_info": null,
                      "subtitle": "",
                      "title": "Praise (feat. Brandon Lake, Chris Brown, Chandler Moore)",
                      "web_30s_preview_download_url": null,
                      "lyrics": null,
                      "spotify_track_metadata": null,
                      "related_audios": null
                    },
                    "music_consumption_info": {
                      "allow_media_creation_with_music": true,
                      "music_creation_restriction_reason": null,
                      "audio_asset_start_time_in_ms": 55424,
                      "derived_content_start_time_in_composition_in_ms": 0,
                      "contains_lyrics": null,
                      "derived_content_id": null,
                      "display_labels": null,
                      "formatted_clips_media_count": null,
                      "is_bookmarked": false,
                      "is_trending_in_clips": true,
                      "overlap_duration_in_ms": 90000,
                      "placeholder_profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=HMeNVRbt-xsQ7kNvwEVy9wE&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4AAAAA&ccb=7-5&oh=00_Af0BtSWqLYq5K4DWlk4hUj4-E6etRmhnv1GqkPhRQAjxAQ&oe=69DC253D&_nc_sid=472314",
                      "should_allow_music_editing": false,
                      "should_mute_audio": false,
                      "should_mute_audio_reason": "",
                      "should_mute_audio_reason_type": null,
                      "should_render_soundwave": false,
                      "trend_rank": null,
                      "previous_trend_rank": null,
                      "ig_artist": {
                        "strong_id__": "307509295",
                        "pk": 307509295,
                        "pk_id": "307509295",
                        "id": "307509295",
                        "username": "elevationworship",
                        "full_name": "Elevation Worship",
                        "is_private": false,
                        "is_verified": true,
                        "profile_pic_id": "3814372290864467300_307509295",
                        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/619566013_18550293298053296_8897657889483886820_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=8anF_jWdEBkQ7kNvwEV-aT_&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GL3T7SSwgIK6ZOdBAOSQo2u11Hp7bmNDAQAB1501500j-ccb7-5&oh=00_Af1zpcvuDxfoxfwHjY7uj4TKCVcRgr2o1XOuRL7fksCH-g&oe=69DC2561&_nc_sid=472314"
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
                  "original_sound_info": null
                },
                "clips_tab_pinned_user_ids": [],
                "is_open_to_public_submission": false,
                "is_social_ufi_disabled": false,
                "timeline_pinned_user_ids": [],
                "taken_at": 1775647202,
                "usertags": [
                  {
                    "user": {
                      "pk": "201558512",
                      "id": "201558512",
                      "username": "wendy_saved_by_grace",
                      "full_name": "Wendy Huber",
                      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/184015669_492120375249882_7370163052157690695_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=LmbLdMmoC1oQ7kNvwHZP_qe&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDXb9wraSye0lL8BAEdjkUQ-FEhmbkULAAAB1501500j-ccb7-5&oh=00_Af0KT6BW9mHYDxC2Cz_TOPKMrknChhJCkUh72h2VXAHSHQ&oe=69DC4B92&_nc_sid=472314",
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
                      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/619566013_18550293298053296_8897657889483886820_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=8anF_jWdEBkQ7kNvwEV-aT_&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GL3T7SSwgIK6ZOdBAOSQo2u11Hp7bmNDAQAB1501500j-ccb7-5&oh=00_Af1zpcvuDxfoxfwHjY7uj4TKCVcRgr2o1XOuRL7fksCH-g&oe=69DC2561&_nc_sid=472314",
                      "profile_pic_url_hd": null,
                      "is_private": false,
                      "is_verified": true
                    },
                    "x": 0.8549242424,
                    "y": 0.9836601298000001
                  }
                ],
                "photo_of_you": false,
                "can_see_insights_as_brand": false,
                "fundraiser_tag": {
                  "has_standalone_fundraiser": false
                },
                "fb_user_tags": {
                  "in": []
                },
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "formatted_mashups_count": null,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_light_weight_reuse_allowed_check": true,
                  "is_pivot_page_available": false,
                  "is_reuse_allowed": true,
                  "mashup_type": null,
                  "mashups_allowed": true,
                  "mashups_allowed_for_carousel": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "privacy_filtered_mashups_media_count": null,
                  "original_media": null
                },
                "media_overlay_info": null,
                "is_in_profile_grid": false,
                "profile_grid_control_enabled": false,
                "media_notes": {
                  "items": []
                },
                "product_type": "feed",
                "subscribe_cta_visible": false,
                "creative_config": null,
                "is_cutout_sticker_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "meta_ai_suggested_prompts": [],
                "gen_ai_chat_with_ai_cta_info": null,
                "can_reply": false,
                "floating_context_items": [],
                "is_eligible_content_for_post_roll_ad": false,
                "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
                "eligible_insights_entrypoints": "NONE",
                "media_attributions_data": [],
                "is_eligible_for_poe": false,
                "is_eligible_for_organic_eager_refresh": false,
                "commerce_integrity_review_decision": "",
                "boost_unavailable_identifier": null,
                "boost_unavailable_reason": null,
                "boost_unavailable_reason_v2": null,
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
                    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/468367136_545676408366967_6972864757526950554_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=szV8GBoN7jQQ7kNvwH0RJDl&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GCC36ht3p3swSvABAJryO5uNl8RgbkULAAAB1501500j-ccb7-5&oh=00_Af160Fj03Sm8Q4HPun5gKTmlV_Q1HMi4fLI-oVp8o4uoXA&oe=69DC3EB9&_nc_sid=472314",
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
                    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/184015669_492120375249882_7370163052157690695_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=LmbLdMmoC1oQ7kNvwHZP_qe&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GDXb9wraSye0lL8BAEdjkUQ-FEhmbkULAAAB1501500j-ccb7-5&oh=00_Af0KT6BW9mHYDxC2Cz_TOPKMrknChhJCkUh72h2VXAHSHQ&oe=69DC4B92&_nc_sid=472314",
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
                "coauthor_producer_can_see_organic_insights": false,
                "invited_coauthor_producers": [],
                "collab_follow_button_info": {
                  "show_follow_button": true,
                  "is_owner_in_author_exp": true
                },
                "product_suggestions": [],
                "igbio_product": null,
                "is_paid_partnership": false,
                "ig_media_sharing_disabled": false,
                "media_repost_count": 89,
                "like_count": 3,
                "top_likers": [
                  "stacy.wentz"
                ],
                "hidden_likes_string_variant": -1,
                "caption": {
                  "strong_id__": "18096271373088381",
                  "bit_flags": 0,
                  "created_at": 1775647202,
                  "created_at_utc": 1775647202,
                  "did_report_as_spam": false,
                  "is_ranked_comment": false,
                  "pk": "18096271373088381",
                  "share_enabled": false,
                  "content_type": "comment",
                  "media_id": 3870729737757151899,
                  "status": "Active",
                  "type": 1,
                  "user_id": 49646700667,
                  "text": "𝗚𝗼𝗼𝗱 𝗺𝗼𝗿𝗻𝗶𝗻𝗴 𝗳𝗮𝗺𝗶𝗹𝘆 💝\n𝗜𝗳 𝘆𝗼𝘂 𝘄𝗼𝗸𝗲 𝘂𝗽 𝘁𝗵𝗶𝘀 𝗺𝗼𝗿𝗻𝗶𝗻𝗴… \n𝗚𝗼𝗱 𝗶𝘀 𝗻𝗼𝘁 𝗱𝗼𝗻𝗲 𝘄𝗶𝘁𝗵 𝘆𝗼𝘂 𝘆𝗲𝘁. \n\nToday, we rise with gratitude in our \nhearts & praise on our lips. God has \nbeen so good to us. He woke us up, \ncovered us, and is leading us into a \nnew day filled w/ purpose & promise.\n\n“Because of the Lord’s great love \nwe are not consumed, for His \nmercies never fail. They are new \nevery morning; great is Your \nfaithfulness.” — 𝗟𝗮𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻𝘀 𝟯:𝟮𝟮–𝟮𝟯\n\n𝗣𝗿𝗮𝘆𝗲𝗿:\nLord, thank You for the gift of today.\nEven if my heart feels heavy, help \nme choose gratitude. Remind me that \nYou are with me, guiding me, and \nworking all things for good. Give me \npeace for what I can’t control and \nstrength for what’s ahead. Let my \nlife reflect Your love today. In Jesus’ \nname, Amen. 🤍✨\n\n𝗗𝗲𝗰𝗹𝗮𝗿𝗮𝘁𝗶𝗼𝗻:\nToday, I will walk in gratitude.\nI will trust God with every step.\nI am covered, I am guided, and I am \nnot alone. This day holds purpose, \nand I will walk in it. 🙌🏼✨\n\n𝗚𝗼𝗱 𝗯𝗹𝗲𝘀𝘀 𝘆𝗼𝘂 𝗽𝗿𝗲𝗰𝗶𝗼𝘂𝘀 𝗰𝗵𝗶𝗹𝗱! 👑\n\n𝐈𝐟 𝐲𝐨𝐮 𝐤𝐧𝐨𝐰 𝐬𝐨𝐦𝐞𝐨𝐧𝐞 𝐭𝐡𝐚𝐭 𝐧𝐞𝐞𝐝𝐬 \n𝐭𝐡𝐢𝐬 𝐞𝐧𝐜𝐨𝐮𝐫𝐚𝐠𝐞𝐦𝐞𝐧𝐭, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐡𝐚𝐫𝐞 \n& 𝐭𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 🙏🏼\n\n#chosen2reign #childlikefaith #godfirst\n#trustinthelord #happywednesday",
                  "user": {
                    "strong_id__": "49646700667",
                    "pk": 49646700667,
                    "pk_id": "49646700667",
                    "id": "49646700667",
                    "is_unpublished": false,
                    "fbid_v2": 17841449580035837,
                    "username": "chosen_2_reign",
                    "full_name": "𝐂𝐢𝐧𝐝𝐲 & 𝐖𝐞𝐧𝐝𝐲",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_id": "2685218318953352068_49646700667",
                    "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/245410687_270162081680252_8621949966077360040_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40ODAuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=6IiLqxbZRAgQ7kNvwGU4mIt&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GH_roA58C_kCtvUAAKh3OyfQUad3bkULAAAB1501500j-ccb7-5&oh=00_Af3IKVC1wlxQGLYWbb1r50WMWgtDfEnai7cacpAjqqaY0w&oe=69DC51EE&_nc_sid=472314"
                  },
                  "is_covered": false,
                  "private_reply_status": 0
                },
                "comment_count": 93,
                "can_view_more_preview_comments": false,
                "preview_comments": [],
                "comment_inform_treatment": {
                  "action_type": null,
                  "should_have_inform_treatment": false,
                  "text": "",
                  "url": null
                },
                "is_photo_comments_composer_enabled_for_author": false,
                "hide_view_all_comment_entrypoint": true,
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
                "locations": [],
                "lng": -81.5258,
                "lat": 28.6899,
                "shop_routing_user_id": null,
                "featured_products": [],
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "sharing_friction_info": {
                  "should_have_sharing_friction": false,
                  "bloks_app_url": null,
                  "sharing_friction_payload": null
                },
                "gen_ai_detection_method": {
                  "detection_method": "IPTC_METADATA_EDITED"
                },
                "user": {
                  "pk": "49646700667",
                  "id": "49646700667",
                  "username": "chosen_2_reign",
                  "full_name": "𝐂𝐢𝐧𝐝𝐲 & 𝐖𝐞𝐧𝐝𝐲",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/245410687_270162081680252_8621949966077360040_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40ODAuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGrDhZu5mhSMIWWw6XEPh2_Igy0Bvkn_Ha8ksWF2p3jwOZmP9gJW1TztgX3DkFhzXQ&_nc_ohc=6IiLqxbZRAgQ7kNvwGU4mIt&_nc_gid=29AFVmiyV9b9FM9AEszTtA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GH_roA58C_kCtvUAAKh3OyfQUad3bkULAAAB1501500j-ccb7-5&oh=00_Af3IKVC1wlxQGLYWbb1r50WMWgtDfEnai7cacpAjqqaY0w&oe=69DC51EE&_nc_sid=472314",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "community_notes_info": {
                  "has_viewer_submitted_note": false,
                  "note_submission_disabled": false,
                  "enable_submission_friction": false,
                  "is_eligible_for_request_a_note": true
                },
                "has_high_risk_gen_ai_inform_treatment": false,
                "caption_is_edited": false,
                "code": "DW3mDBAjlKb",
                "device_timestamp": 177564696383231,
                "enable_media_notes_production": true,
                "filter_type": 0,
                "has_views_fetching": true,
                "like_and_view_counts_disabled": true,
                "original_media_has_visual_reply_media": false,
                "report_info": {
                  "has_viewer_submitted_report": false
                },
                "is_organic_product_tagging_eligible": true,
                "can_viewer_reshare": true,
                "has_shared_to_fb": 0,
                "media_reposter_bottomsheet_enabled": false,
                "has_liked": false,
                "can_viewer_save": true,
                "is_comments_gif_composer_enabled": true,
                "image_versions": [
                  {
                    "estimated_scans_sizes": [
                      31926,
                      63853
                    ],
                    "height": 1800,
                    "scans_profile": "e35",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af0888hHAs2X-tcqp0-p044Z_8sFnL2oR76oEkDmqUyFRg&oe=69DC4396",
                    "width": 1440,
                    "is_spatial_image": false
                  },
                  {
                    "estimated_scans_sizes": [
                      15722,
                      31445
                    ],
                    "height": 938,
                    "scans_profile": "e35",
                    "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af3fb4skkdmFWl_iRJfUs74vO2MmvEINjzJn6LyMoNteSA&oe=69DC4396",
                    "width": 750,
                    "is_spatial_image": false
                  }
                ],
                "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658311372_18076796138652668_1383226069978729771_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDcyOTczNzc1NzE1MTg5OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=1lL-18i0chsQ7kNvwFZw0Fe&_nc_oc=AdoW2FkzIQfa7eBgWtyMrczu5GCM9FJwZrWnybgGK5ZkHQyzIr2wdynTRNC-KdkKics&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=29AFVmiyV9b9FM9AEszTtA&_nc_ss=7a3ba&oh=00_Af0888hHAs2X-tcqp0-p044Z_8sFnL2oR76oEkDmqUyFRg&oe=69DC4396",
                "taken_at_ts": 1775647202,
                "sponsor_tags": [],
                "play_count": 0
              }
            }
          ]
        }
      }
    ],
    "more_available": true,
    "next_max_id": "10955b1cbbeb468eb19b38d1578e7b02",
    "next_page": 1,
    "next_media_ids": [],
    "auto_load_more_enabled": true,
    "status": "ok"
  },
  "next_page_id": "WyIxMDk1NWIxY2JiZWI0NjhlYjE5YjM4ZDE1NzhlN2IwMiIsW10sMV0="
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-hashtags){ target=_blank }
