# Track Endpoints

Get audio tracks, likers, and associated media.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/track/by/canonical/id`](#get-v2trackbycanonicalid) | [`/v2/track/by/id`](#get-v2trackbyid) | [`/v2/track/stream/by/id`](#get-v2trackstreambyid) | [`/v3/fbsearch/accounts`](#get-v3fbsearchaccounts) | [`/v3/fbsearch/places`](#get-v3fbsearchplaces) | [`/v3/fbsearch/reels`](#get-v3fbsearchreels) | [`/v3/fbsearch/topsearch`](#get-v3fbsearchtopsearch)

---

### GET /v2/track/by/canonical/id

Get music track object by canonical_id. Returns audio track data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `canonical_id` | string | Yes | Canonical Id |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/track/by/canonical/id?canonical_id=578218498892498"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.track_by_canonical_id_v2(canonical_id="578218498892498")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/track/by/canonical/id",
        headers=headers,
        params={"canonical_id": "578218498892498"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/track/by/canonical/id?canonical_id=578218498892498",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "root_node_for_rest_merged_response": null,
    "music_canonical_id": "",
    "auto_created_reels_preview_metadata": [],
    "status": "ok",
    "status_code": "200"
  },
  "next_page_id": ""
}
```

</details>

---

### GET /v2/track/by/id

Get music track object by id. Returns audio track data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `track_id` | string | Yes | Track Id |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/track/by/id?track_id=578218498892498"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.track_by_id_v2(track_id="578218498892498")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/track/by/id",
        headers=headers,
        params={"track_id": "578218498892498"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/track/by/id?track_id=578218498892498",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "items": [],
    "audio_page_reporting_id": "",
    "formatted_media_count": "",
    "music_canonical_id": "",
    "auto_created_reels_preview_metadata": [],
    "audio_page_segments": [],
    "metadata": {
      "additional_audio_info": null,
      "music_info": null,
      "original_sound_info": null
    },
    "audio_ranking_info": {},
    "is_music_page_restricted": false,
    "media_count": {
      "clips_count": 0,
      "photos_count": 0
    },
    "paging_info": {
      "more_available": false
    },
    "status": "ok",
    "status_code": "200"
  },
  "next_page_id": ""
}
```

</details>

---

### GET /v2/track/stream/by/id

Get music track object by id. Returns audio track data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `track_id` | string | Yes | Track Id |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/track/stream/by/id?track_id=578218498892498"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.track_stream_by_id_v2(track_id="578218498892498")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/track/stream/by/id",
        headers=headers,
        params={"track_id": "578218498892498"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/track/stream/by/id?track_id=578218498892498",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "items": [],
    "is_media_preview": false,
    "music_page_response": {
      "paging_info": {
        "more_available": false
      },
      "audio_page_segments": [],
      "auto_created_reels_preview_metadata": [],
      "audio_page_reporting_id": "",
      "music_canonical_id": "",
      "formatted_media_count": "",
      "metadata": {},
      "audio_ranking_info": {},
      "is_music_page_restricted": false,
      "available_tabs": [],
      "media_count": {
        "clips_count": 0,
        "photos_count": 0
      }
    },
    "paging_info": {
      "more_available": false
    },
    "status": "ok"
  },
  "next_page_id": null
}
```

</details>

---

### GET /v3/fbsearch/accounts

Search accounts. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `page_token` | string | No | Page Token |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v3/fbsearch/accounts?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_accounts_v3(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v3/fbsearch/accounts",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v3/fbsearch/accounts?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "num_results": 20,
  "users": [
    {
      "strong_id__": "787132",
      "coeff_weight": null,
      "fbid_v2": 17841400573960012,
      "is_active": null,
      "pk": 787132,
      "pk_id": "787132",
      "all_media_count": null,
      "allowed_commenter_type": null,
      "following_tag_count": null,
      "is_verified_search_boosted": false,
      "liked_clips_count": null,
      "reel_auto_archive": null,
      "search_serp_type": 3,
      "text_post_app_take_a_break_setting": null,
      "third_party_downloads_enabled": 2,
      "live_invite_only_branding_enabled": null,
      "id": "787132",
      "full_name": "National Geographic",
      "has_onboarded_to_text_post_app": null,
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEaASWvyKpBkFpKl1bzEltVB2mEFrIjC9Us0Xx6U9OkC4uT43iPu9EjrOpxNilnphU&_nc_ohc=XbeNvhLXv28Q7kNvwGuzNfJ&_nc_gid=DkgPDZBUgn_MCdSIgznD5g&edm=ALgmGsQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0FPMb8RQpSscCyhpN7yr53Q1AdsZXycU-cyKVwiTMH9Q&oe=69DC51E9&_nc_sid=2f557e",
      "username": "natgeo",
      "account_badges": [],
      "ai_agent_owner_username": null,
      "friendship_status": {
        "following": false,
        "is_bestie": false,
        "is_feed_favorite": false,
        "is_private": false,
        "is_restricted": false,
        "text_post_app_pre_following": null,
        "incoming_request": false,
        "outgoing_request": false
      },
      "has_anonymous_profile_picture": false,
      "interop_messaging_user_fbid": null,
      "is_ai_user": null,
      "is_ring_creator": false,
      "latest_reel_media": 1775583063,
      "reachability_status": null,
      "reel_media_seen_timestamp": null,
      "should_show_category": true,
      "show_ig_app_switcher_badge": true,
      "show_ring_award": false,
      "show_text_post_app_badge": true,
      "unseen_count": 0,
      "aigm_account_label_info": null,
      "live_broadcast_id": null,
      "live_broadcast_visibility": null,
      "social_context": "274M followers",
      "search_social_context": "274M followers",
      "search_social_context_snippet_type": "typeahead_follow_count",
      "search_social_context_facepiles": null
    },
    {
      "strong_id__": "1029649300",
      "coeff_weight": null,
      "fbid_v2": 17841400519016088,
      "is_active": null,
      "pk": 1029649300,
      "pk_id": "1029649300",
      "all_media_count": null,
      "allowed_commenter_type": null,
      "following_tag_count": null,
      "is_verified_search_boosted": false,
      "liked_clips_count": null,
      "reel_auto_archive": null,
      "search_serp_type": 3,
      "text_post_app_take_a_break_setting": null,
      "third_party_downloads_enabled": 1,
      "live_invite_only_branding_enabled": null,
      "id": "1029649300",
      "full_name": "National Geographic Animals",
      "has_onboarded_to_text_post_app": null,
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865698702530758137_1029649300",
      "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEaASWvyKpBkFpKl1bzEltVB2mEFrIjC9Us0Xx6U9OkC4uT43iPu9EjrOpxNilnphU&_nc_ohc=ic5ODsLE2O8Q7kNvwG79G8t&_nc_gid=DkgPDZBUgn_MCdSIgznD5g&edm=ALgmGsQBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af29J5IjdorHv3X6rP3mC56w4qGtSQIbbESg6UXDC4E0Og&oe=69DC204C&_nc_sid=2f557e",
      "username": "natgeoanimals",
      "account_badges": [],
      "ai_agent_owner_username": null,
      "friendship_status": {
        "following": false,
        "is_bestie": false,
        "is_feed_favorite": false,
        "is_private": false,
        "is_restricted": false,
        "text_post_app_pre_following": null,
        "incoming_request": false,
        "outgoing_request": false
      },
      "has_anonymous_profile_picture": false,
      "interop_messaging_user_fbid": null,
      "is_ai_user": null,
      "is_ring_creator": false,
      "latest_reel_media": 0,
      "reachability_status": null,
      "reel_media_seen_timestamp": null,
      "should_show_category": true,
      "show_ig_app_switcher_badge": false,
      "show_ring_award": false,
      "show_text_post_app_badge": true,
      "unseen_count": 0,
      "aigm_account_label_info": null,
      "live_broadcast_id": null,
      "live_broadcast_visibility": null,
      "social_context": "15.1M followers",
      "search_social_context": "15.1M followers",
      "search_social_context_snippet_type": "typeahead_follow_count",
      "search_social_context_facepiles": null
    }
  ],
  "has_more": true,
  "rank_token": "1775657989819|47fe5b16de5a9aee09c8990d74529e016b843dc64e095e262db47f4cce0b56f0",
  "clear_client_cache": false,
  "page_token": "9da98c7e209a4bb48710ca823cd15955",
  "status": "ok"
}
```

</details>

---

### GET /v3/fbsearch/places

Search places. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v3/fbsearch/places?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_places_v3(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v3/fbsearch/places",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v3/fbsearch/places?query=natgeo",
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
      "location": {
        "pk": 338815492647410,
        "facebook_places_id": 338815492647410,
        "external_source": "facebook_places",
        "name": "Mangar NatGeo News",
        "address": "",
        "city": "",
        "has_viewer_saved": false,
        "short_name": "Mangar NatGeo News",
        "lng": 35.735943781561,
        "lat": 0.49440278162708
      },
      "title": "Mangar NatGeo News",
      "subtitle": ""
    },
    {
      "location": {
        "pk": 103142692753506,
        "facebook_places_id": 103142692753506,
        "external_source": "facebook_places",
        "name": "NatGeo Fish",
        "address": "8593 Fawn St. Brooklyn",
        "city": "",
        "has_viewer_saved": false,
        "short_name": "NatGeo Fish",
        "lng": -73.89254,
        "lat": 40.66595
      },
      "title": "NatGeo Fish",
      "subtitle": "8593 Fawn St. Brooklyn"
    }
  ],
  "has_more": false,
  "rank_token": "1775657992875|25341dc4a6b4f2c9308a257cf08807f255142caa9bcf3c6f3e045ece1faa9da4",
  "status": "ok"
}
```

</details>

---

### GET /v3/fbsearch/reels

Search reels by keyword. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `reels_max_id` | string | No | Reels Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v3/fbsearch/reels?query=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v3/fbsearch/reels",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v3/fbsearch/reels?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "reels_serp_modules": [
    {
      "module_type": "clips",
      "clips": [
        {
          "media": {
            "strong_id__": "3773072751201155590_47276232",
            "context__": null,
            "id": "3773072751201155590_47276232",
            "is_post_live": null,
            "disable_caption_and_comment": false,
            "fbid": 18068167955104780,
            "is_music_only_story": null,
            "soft_deleted_at": null,
            "deleted_reason": 0,
            "client_cache_key": "Mzc3MzA3Mjc1MTIwMTE1NTU5MA==.3",
            "has_bc_violation": null,
            "integrity_review_decision": "pending",
            "is_awaiting_distribution": false,
            "is_reel_media": null,
            "is_sidecar_child": null,
            "sticker_translations_enabled": null,
            "subscription_media_visibility": null,
            "timezone_offset": null,
            "pk": 3773072751201155590,
            "is_affiliate_commission_eligible": false,
            "visibility": null,
            "expiring_at": null,
            "organic_cta_type": null,
            "has_delayed_metadata": false,
            "client_cache_expiration_ts": null,
            "is_eof": null,
            "mezql_token": "",
            "should_request_ads": false,
            "has_privately_liked": false,
            "dynamic_ad_carousel_card_starting_index": null,
            "log_time": null,
            "is_quiet_post": false,
            "collaborator_edit_eligibility": false,
            "share_count_disabled": false,
            "is_reshare_of_text_post_app_media_in_ig": false,
            "ranking_weight": null,
            "ranked_at": null,
            "algorithm": null,
            "connection_id": null,
            "carousel_last_edited_at": null,
            "is_visual_reply_commenter_notice_enabled": true,
            "media_level_comment_controls": null,
            "translated_langs_for_autodub": [],
            "is_terminal_video_segment": null,
            "segmented_video_group_id": null,
            "subtype_name_for_REST__": "XDTClipsMedia",
            "is_third_party_downloads_eligible": true,
            "clips_mashup_follow_button_info": null,
            "has_views_fetching_on_search_grid": null,
            "linked_media_playlist_data": null,
            "image_versions2": {
              "additional_candidates": {
                "first_frame": {
                  "estimated_scans_sizes": [
                    5121,
                    10242
                  ],
                  "height": 1136,
                  "scans_profile": "e15",
                  "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/587895083_1582451659437904_2371604589830659666_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=5zTeWC8-UaoQ7kNvwEobXcG&_nc_oc=AdqM7NLU_r04kDiQvFrqU_792PT7XXy3dIvzqDH19t4BU6VsU1rxw6-scDhju6dwlas&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&oh=00_Af2c378sF0MLXGv1BSyzki9BRZWXXJ7FTEQWsI5Mzm5umw&oe=69DC410B",
                  "width": 640,
                  "is_spatial_image": false
                },
                "igtv_first_frame": {
                  "estimated_scans_sizes": [
                    5121,
                    10242
                  ],
                  "height": 1136,
                  "scans_profile": "e15",
                  "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/587895083_1582451659437904_2371604589830659666_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=5zTeWC8-UaoQ7kNvwEobXcG&_nc_oc=AdqM7NLU_r04kDiQvFrqU_792PT7XXy3dIvzqDH19t4BU6VsU1rxw6-scDhju6dwlas&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&oh=00_Af2c378sF0MLXGv1BSyzki9BRZWXXJ7FTEQWsI5Mzm5umw&oe=69DC410B",
                  "width": 640,
                  "is_spatial_image": false
                },
                "smart_frame": null
              },
              "candidates": [
                {
                  "estimated_scans_sizes": [
                    26510,
                    53021
                  ],
                  "height": 1332,
                  "scans_profile": "e15",
                  "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.82787-15/588242089_18544441921044233_3161580958584083436_n.jpg?stp=dst-jpg_e15_p750x750_tt6&_nc_cat=110&ig_cache_key=Mzc3MzA3Mjc1MTIwMTE1NTU5MDE4NTQ0NDQxOTE4MDQ0MjMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNTR4MTg3Mi5zZHIuQzMifQ%3D%3D&_nc_ohc=FGXE_FV4fn8Q7kNvwEpjJzx&_nc_oc=AdpOdYFkKQ-UbVNCFuwokhcHobl2hPNeo2cYilnYJtUU0EY_-BfFphWUjBQJoS1hX5Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&oh=00_Af2FT-up4PnMMilfpx_qva1-n26D2kATqS8qCasZGZwRtg&oe=69DC3631",
                  "width": 750,
                  "is_spatial_image": false
                }
              ],
              "scrubber_spritesheet_info_candidates": {
                "default": {
                  "file_size_kb": 482,
                  "max_thumbnails_per_sprite": 105,
                  "rendered_width": 96,
                  "sprite_height": 1232,
                  "sprite_urls": [
                    "https://scontent-mia5-1.cdninstagram.com/v/t51.71878-15/586914880_1796498024386526_1689958848606284189_n.jpg?_nc_ht=scontent-mia5-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=IX5fbWWvZmMQ7kNvwHTRkDt&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8BAAAA&ccb=7-5&oh=00_Af1WQW40R--rnpSJdI55xdaHr-5NyIk7H20sfcC2g9CjDA&oe=69DC4E87&_nc_sid=026283"
                  ],
                  "sprite_width": 1500,
                  "thumbnail_duration": 0.41269523809523806,
                  "thumbnail_height": 176,
                  "thumbnail_width": 100,
                  "thumbnails_per_row": 15,
                  "total_thumbnail_num_per_sprite": 105,
                  "video_length": 43.333
                }
              }
            },
            "wearable_attribution_info": null,
            "clips_timely_event_info": null,
            "media_cropping_info": {
              "four_by_three_crop": {
                "crop_left": 0.0,
                "crop_right": 1.0,
                "crop_top": 0.0,
                "crop_bottom": 0.75
              }
            },
            "media_type": 2,
            "original_width": 1080,
            "original_height": 1920,
            "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYzEwMjc3ZmE0YjM3NGVjY2E3ODZkZjAzYjRjY2VkYTkzNzczMDcyNzUxMjAxMTU1NTkwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1ODAxMDI3OXwzNzczMDcyNzUxMjAxMTU1NTkwfDM1Mzk0NDM1MDEzfGVjZmQ2OWQxMGRhOWI5YjgyODRmZmYwOTNkMTJkMjYzZTZiYzJmYzliMDY0NTU3ZTA2NDBhMTFiNDE0MTVmNWQifSwic2lnbmF0dXJlIjoiIn0=",
            "attribution": null,
            "caption_add_on": null,
            "music_metadata": null,
            "clips_trial": null,
            "has_tagged_users": false,
            "is_eligible_for_media_note_recs_nux": null,
            "is_shared_from_basel": true,
            "show_story_deleted_error_label": null,
            "is_dismiss_pending_media_banner": null,
            "clips_tab_pinned_user_ids": [],
            "is_spinnable": null,
            "clips_attribution_info": null,
            "original_lang_for_translations": null,
            "all_previous_submitters": null,
            "app_install_cta_info": null,
            "archived_media_timestamp": null,
            "can_hype": null,
            "highlights_info": null,
            "igtv_series_info": null,
            "is_fb_only": null,
            "is_internal_only": null,
            "is_open_to_public_submission": false,
            "is_social_ufi_disabled": false,
            "is_viewer_location_nearby": null,
            "previous_submitter": null,
            "timeline_pinned_user_ids": [],
            "title": null,
            "taken_at": 1764005641,
            "usertags": null,
            "photo_of_you": null,
            "can_see_insights_as_brand": false,
            "fundraiser_tag": {
              "has_standalone_fundraiser": false
            },
            "media_notice": null,
            "media_prompt_data": null,
            "text_sticker_content": null,
            "has_translation": null,
            "accessibility_caption": null,
            "content_scheduling_metadata": null,
            "media_appreciation_settings": null,
            "organic_post_id": null,
            "media_gating_info": null,
            "lumen_logging_info": null,
            "display_uri": null,
            "fb_user_tags": {
              "in": []
            },
            "mashup_info": null,
            "visual_replies_info": null,
            "gating": null,
            "preview": null,
            "media_overlay_info": null,
            "is_in_profile_grid": false,
            "profile_grid_control_enabled": false,
            "attribution_content_url": null,
            "channel_tag_data": null,
            "is_artist_pick": false,
            "copyright_attribution_info": null,
            "media_notes": {
              "items": []
            },
            "linked_media_data": null,
            "product_type": "clips",
            "inventory_source": null,
            "story_polls": null,
            "social_context": [],
            "should_have_hscroll_items": null,
            "explore": null,
            "story_poll_voter_infos": null,
            "audio": null,
            "subscribe_cta_visible": false,
            "creative_config": null,
            "is_cutout_sticker_allowed": true,
            "cutout_sticker_info": [],
            "cutout_stickers": null,
            "is_seen": null,
            "main_feed_carousel_starting_media_id": null,
            "main_feed_carousel_has_unseen_cover_media": null,
            "text_with_entities": null,
            "mv_link": null,
            "shimmed_mv_link": null,
            "mv_link_info": null,
            "mv_original_content_review_status": null,
            "story_prompts": null,
            "story_notify_me_stickers": null,
            "immersive_media_metadata": null,
            "text_post_share_to_ig_story_stickers": null,
            "is_tagged_media_shared_to_viewer_profile_grid": false,
            "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
            "impression_token": null,
            "meta_place": null,
            "reminder_info": null,
            "meta_ai_suggested_prompts": [],
            "gen_ai_chat_with_ai_cta_info": null,
            "gen_ai_share_info": null,
            "can_reply": false,
            "floating_context_items": [],
            "is_eligible_content_for_post_roll_ad": false,
            "instream_ad_media_eligibility_info": null,
            "contextual_ads_info": null,
            "item_client_gap_rules": null,
            "explore_context": null,
            "multi_ads_info": null,
            "nearly_complete_copyright_match": null,
            "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
            "related_ads_pivots_organic_search_query": null,
            "geo_gated_countries": null,
            "has_overflow_bubbles": null,
            "tallest_media_aspect_ratio": null,
            "giphy_media_info": null,
            "eligible_insights_entrypoints": "NONE",
            "basel_encoding_timeout": 146,
            "media_attributions_data": [],
            "media_ui_attributions_data": [],
            "media_ui_attributions_data_v2": [],
            "clips_on_impression_control": null,
            "snippets_overlays": null,
            "snippets_attribution_info": null,
            "creator_product_links": null,
            "creator_product_link_infos": [],
            "is_eligible_for_poe": false,
            "is_eligible_for_organic_eager_refresh": false,
            "cta_rendering_config": null,
            "commerce_integrity_review_decision": null,
            "is_reuse_allowed": true,
            "goals_toast_info": null,
            "logging_info_token": "GCA2ODI5ZDc1ODI4MmQ0NDMxYTM2YmEyYzE5OTZiOWUwZHgDbmhhAA==",
            "clips_delivery_parameters": null,
            "basel_inspiration_info": null,
            "basel_sticky_note": null,
            "boosted_status": null,
            "boost_unavailable_identifier": null,
            "boost_unavailable_reason": null,
            "boost_unavailable_reason_v2": null,
            "is_currently_promoting_by_sponsor": null,
            "boosted_by_sponsor": null,
            "boosted_post_id": null,
            "branded_content_ads_boost_post_tokens": null,
            "branded_content_project_metadata": null,
            "coauthor_producers": [],
            "coauthor_producer_can_see_organic_insights": false,
            "invited_coauthor_producers": [],
            "collab_follow_button_info": null,
            "product_suggestions": null,
            "igbio_product": null,
            "ig_iab_post_click_data": null,
            "is_eligible_for_shoppable_everything": null,
            "shoppable_everything_detected_objects": null,
            "sponsor_tags": null,
            "is_paid_partnership": false,
            "reshare_count": 70380,
            "has_reshares": null,
            "ig_media_sharing_disabled": false,
            "media_repost_count": 44132,
            "score": null,
            "ranking_scores_list": null,
            "recommendation_data": null,
            "feed_delivery_parameters": null,
            "feed_ranking_source_debug_label": null,
            "view_state_item_type": 128,
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
                "best_audio_cluster_id": "827855427560332"
              },
              "audio_type": "licensed_music",
              "basel_video_composition_model": null,
              "basel_reusable_elements": null,
              "basel_template_info_for_ig_app": {
                "is_basel_template": null,
                "should_show_reuse_setting_for_owner": false,
                "use_template_deeplink": null
              },
              "basel_template_attribution": null,
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
                "has_been_mashed_up": true,
                "has_nonmimicable_additional_audio": true,
                "is_creator_requesting_mashup": false,
                "is_light_weight_check": true,
                "is_light_weight_reuse_allowed_check": false,
                "is_pivot_page_available": true,
                "is_reuse_allowed": true,
                "mashup_type": null,
                "mashups_allowed": true,
                "mashups_allowed_for_carousel": false,
                "non_privacy_filtered_mashups_media_count": 119,
                "privacy_filtered_mashups_media_count": null,
                "original_media": null
              },
              "merchandising_pill_info": null,
              "music_canonical_id": "18149417842052711",
              "music_info": {
                "music_canonical_id": 18149417842052711,
                "music_asset_info": {
                  "allows_saving": false,
                  "artist_id": "1952911064912159",
                  "audio_asset_id": "1456846724444758",
                  "audio_cluster_id": "827855427560332",
                  "cover_artwork_thumbnail_uri": "https://scontent-mia3-2.cdninstagram.com/v/t39.30808-6/427975773_1326440388074917_6707285205492640613_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=y2CrW2FwE_wQ7kNvwEe3k3F&_nc_oc=Adq74h-T3Enq4ydUj2h_hQO0crPt-npV4wnAvsSrpvQCwZX4S6ZdNUXT2ahVRNo6_Ss&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a39b&oh=00_Af02uWmLI-GYdatTkYuER8BrlJRXS0uKP63gIIRiKlvB4A&oe=69DC1BFE",
                  "cover_artwork_uri": "https://scontent-mia3-2.cdninstagram.com/v/t39.30808-6/427975773_1326440388074917_6707285205492640613_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=y2CrW2FwE_wQ7kNvwEe3k3F&_nc_oc=Adq74h-T3Enq4ydUj2h_hQO0crPt-npV4wnAvsSrpvQCwZX4S6ZdNUXT2ahVRNo6_Ss&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a39b&oh=00_Af02uWmLI-GYdatTkYuER8BrlJRXS0uKP63gIIRiKlvB4A&oe=69DC1BFE",
                  "dark_message": null,
                  "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT354.906769S\"><Period id=\"0\" duration=\"PT354.906769S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"804748288749737a\" bandwidth=\"72100\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"72100\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m69/AQMRBPIaWGK2FcEcwSDsnzYQ7yBwuED8L3QQAbky5lzI17fFRjjHz89l3Y86SDMd9YZ0M-BZhXldaQrm_mSvv-OR.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=MD7ZxGEbuhcQ7kNvwGl7yQa&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjoxMTM1NDcyNjA3Nzk5OTAyLCJhc3NldF9hZ2VfZGF5cyI6Mjk4MiwidmlfdXNlY2FzZV9pZCI6MTA1NjgsImR1cmF0aW9uX3MiOjM1NCwiYml0cmF0ZSI6NzIxNjcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2GJxShbDpHVkkD2mNQQKJNCGqhBmOjljGcaeDE4q9aSA&amp;oe=69DC50AE</BaseURL><SegmentBase indexRange=\"824-2991\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                  "display_artist": "Vangelis",
                  "duration_in_ms": 354906,
                  "fast_start_progressive_download_url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m69/AQMRBPIaWGK2FcEcwSDsnzYQ7yBwuED8L3QQAbky5lzI17fFRjjHz89l3Y86SDMd9YZ0M-BZhXldaQrm_mSvv-OR.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=MD7ZxGEbuhcQ7kNvwGl7yQa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjoxMTM1NDcyNjA3Nzk5OTAyLCJhc3NldF9hZ2VfZGF5cyI6Mjk4MiwidmlfdXNlY2FzZV9pZCI6MTA1NjgsImR1cmF0aW9uX3MiOjM1NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=33fdb9e764b6c38e&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQXRIT1NBQ3pWRlF5NnNIQUh1dGhQRHNDUlJVYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmvKmFl5qthAQVAigCQzMsF0B2Ln752yLRGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af0vHFriqcRxW1bbysyakDunYy-gmPmZU9pt8tshi3xrFw&oe=69DC50AE",
                  "has_lyrics": false,
                  "highlight_start_times_in_ms": [
                    15000,
                    47000
                  ],
                  "id": "1456846724444758",
                  "ig_username": null,
                  "is_eligible_for_audio_effects": true,
                  "is_eligible_for_vinyl_sticker": true,
                  "is_explicit": false,
                  "licensed_music_subtype": "DEFAULT",
                  "progressive_download_url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m69/AQMRBPIaWGK2FcEcwSDsnzYQ7yBwuED8L3QQAbky5lzI17fFRjjHz89l3Y86SDMd9YZ0M-BZhXldaQrm_mSvv-OR.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=MD7ZxGEbuhcQ7kNvwGl7yQa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjoxMTM1NDcyNjA3Nzk5OTAyLCJhc3NldF9hZ2VfZGF5cyI6Mjk4MiwidmlfdXNlY2FzZV9pZCI6MTA1NjgsImR1cmF0aW9uX3MiOjM1NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=33fdb9e764b6c38e&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQXRIT1NBQ3pWRlF5NnNIQUh1dGhQRHNDUlJVYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmvKmFl5qthAQVAigCQzMsF0B2Ln752yLRGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af0vHFriqcRxW1bbysyakDunYy-gmPmZU9pt8tshi3xrFw&oe=69DC50AE",
                  "reactive_audio_download_url": null,
                  "sanitized_title": null,
                  "song_monetization_info": null,
                  "subtitle": "",
                  "title": "La petite fille de la mer (Remastered)",
                  "web_30s_preview_download_url": null,
                  "lyrics": null,
                  "spotify_track_metadata": null,
                  "related_audios": null
                },
                "music_consumption_info": {
                  "allow_media_creation_with_music": true,
                  "music_creation_restriction_reason": null,
                  "audio_asset_start_time_in_ms": 0,
                  "derived_content_start_time_in_composition_in_ms": 0,
                  "contains_lyrics": null,
                  "derived_content_id": null,
                  "display_labels": null,
                  "formatted_clips_media_count": null,
                  "is_bookmarked": false,
                  "is_trending_in_clips": false,
                  "overlap_duration_in_ms": 43333,
                  "placeholder_profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=HMeNVRbt-xsQ7kNvwH4XXoJ&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8AAAAA&ccb=7-5&oh=00_Af1JGL665RSOdBuWi1hb38-ZggS-PeufN3TBxVpYZ1nLyg&oe=69DC253D&_nc_sid=026283",
                  "should_allow_music_editing": false,
                  "should_mute_audio": false,
                  "should_mute_audio_reason": "",
                  "should_mute_audio_reason_type": null,
                  "should_render_soundwave": false,
                  "trend_rank": null,
                  "previous_trend_rank": null,
                  "ig_artist": null,
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
            "story_sliders": null,
            "story_quizs": null,
            "story_slider_voter_infos": null,
            "story_quiz_participant_infos": null,
            "story_questions": null,
            "question_response_reply_stickers_info": null,
            "story_bloks_tappables": null,
            "avatar_stickers": null,
            "clips_karaoke_caption": null,
            "clips_chats": null,
            "clips_captions": null,
            "clips_captions_translations_urls": null,
            "clips_text": null,
            "visual_comment_reply_sticker_info": null,
            "carousel_media_count": null,
            "carousel_media_pending_post_count": null,
            "can_modify_carousel": null,
            "carousel_media_ids": null,
            "carousel_media": null,
            "total_carousel_media_count": null,
            "more_carousel_media_available": null,
            "open_carousel_show_follow_button": null,
            "open_carousel_submission_state": null,
            "like_count": 447730,
            "fb_like_count": null,
            "top_likers": [],
            "facepile_top_likers": null,
            "hidden_likes_string_variant": -1,
            "has_viewer_saved": null,
            "saved_collection_ids": null,
            "save_count": null,
            "caption": {
              "strong_id__": "18068168333104780",
              "background_color": null,
              "bit_flags": 0,
              "created_at": 1764005641,
              "created_at_utc": 1764005641,
              "did_report_as_spam": false,
              "is_ranked_comment": false,
              "pk": "18068168333104780",
              "share_enabled": false,
              "text_size": null,
              "background_color_alpha": null,
              "content_type": "comment",
              "media_id": 3773072751201155590,
              "status": "Active",
              "text_color": null,
              "type": 1,
              "user_id": 47276232,
              "has_translation": null,
              "mention_user_list": null,
              "text": "Large drop of unpublished videos of Mariposas Monarcas / Mexico / 💧💦#mariposas #natura #monarca #mexico",
              "user": {
                "strong_id__": "47276232",
                "pk": 47276232,
                "pk_id": "47276232",
                "id": "47276232",
                "coeff_weight": null,
                "is_active": null,
                "is_unpublished": false,
                "fbid_v2": 17841401326960738,
                "username": "hobopeeba",
                "full_name": "Kristina Makeeva↟Kotleta↟Timon",
                "is_private": false,
                "is_verified": true,
                "profile_pic_id": null,
                "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.2885-19/11910054_1626257790981501_575133001_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=dfhJaS_x2qUQ7kNvwFjC5sN&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8BAAAA&ccb=7-5&ig_cache_key=GKa7tQB91fGlEscFAEnVRyIAAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af3q37U7g1ytol3Zolq--ybwR5CPdnBB-MG_ciy6buNVeQ&oe=69DC3C02&_nc_sid=026283",
                "has_onboarded_to_text_post_app": null
              },
              "fb_mentioned_users": null,
              "is_covered": false,
              "mentioned_users": null,
              "private_reply_status": 0,
              "text_translation": null
            },
            "comment_count": 2029,
            "commenting_disabled_for_viewer": null,
            "comments_disabled": null,
            "inline_composer_display_condition": null,
            "inline_composer_imp_trigger_time": null,
            "has_hidden_comments": null,
            "comment_inform_treatment": {
              "action_type": null,
              "should_have_inform_treatment": false,
              "text": "",
              "url": null
            },
            "show_keyboard_in_comments": null,
            "is_photo_comments_composer_enabled_for_author": false,
            "fb_comment_count": null,
            "hide_view_all_comment_entrypoint": true,
            "location": {
              "pk": 360673574,
              "facebook_places_id": 110383002315658,
              "external_source": "facebook_places",
              "name": "Michoacán, Mexico",
              "address": "",
              "city": "",
              "has_viewer_saved": false,
              "short_name": "Michoacán",
              "lng": -93.8833,
              "lat": 17.9167
            },
            "locations": [],
            "lng": -93.8833,
            "lat": 17.9167,
            "play_count": 4821184,
            "ig_play_count": 4821184,
            "fb_play_count": null,
            "view_count": null,
            "bucketed_view_count": null,
            "carrera_topic": null,
            "carrera_topic_metadata": null,
            "overflow_carrera_topics": null,
            "are_remixes_crosspostable": true,
            "crosspost": null,
            "crosspost_metadata": {
              "fb_crosspost_deeplink_profile_id": null,
              "fb_crosspost_fbid": null,
              "is_feedback_aggregated": null,
              "is_feed_feedback_aggregated": null,
              "th_unified_feedback_row_tap_target_url": null,
              "unified_feedback_enabled": null,
              "fb_downstream_use_xpost_metadata": {
                "downstream_use_xpost_deny_reason": "NONE"
              }
            },
            "xpost_deny_reason": null,
            "xpost_deny_reason_enum": null,
            "threads_xpost_deny_reason": null,
            "autodub_status": null,
            "byoa_langs": null,
            "is_eligible_for_autodub": false,
            "is_eligible_for_autodub_upsell": false,
            "voice_translations_consumption_data": null,
            "video_subtitles_locale": null,
            "video_subtitles_confidence": null,
            "video_subtitles_enabled": null,
            "video_subtitles_uri": null,
            "video_subtitles_translations_enabled": null,
            "translated_video_subtitles": null,
            "video_sticker_locales": [],
            "transcription_data": null,
            "has_audio": true,
            "video_duration": 43.349998474121094,
            "is_dash_eligible": 1,
            "video_versions": [
              {
                "bandwidth": 3104086,
                "height": 1280,
                "id": "1495177061595317v",
                "type": 101,
                "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOj0t4bWY6qEiIQYY2fjPM0ZP-hypYUCa9PnQqN-j1OLfEnpiKG87UN0FksO_HVgNsv6ngtFZnGIkMoDl9OWgCp8WUH5VnqHBvrlPQ.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=Jwfi_WKiEdwQ7kNvwH5BXbG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTIzMTYwNDA4NTQ3MzYwOCwiYXNzZXRfYWdlX2RheXMiOjEzNCwidmlfdXNlY2FzZV9pZCI6MTA4MjcsImR1cmF0aW9uX3MiOjQzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=5688269e4af95591&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GNzRCRDkyNDRFM0E1NTVBMEU3NDgzOTZEREI0N0VBQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQVhQNFNJYWJFSTFSTzBDQUR4cnpMUWVaSGg1YnN0VEFRQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkIWmwOWIsAQVAigCQzMsF0BFqp--dsi0GBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2WWqQEA&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3c9BFsERN3Xb_sPDBgrknXqvX3KEk_higbM98jpyp5fA&oe=69D82F26",
                "url_expiration_timestamp_us": null,
                "width": 720,
                "fallback": null
              },
              {
                "bandwidth": 3104086,
                "height": 1280,
                "id": "1495177061595317v",
                "type": 102,
                "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOj0t4bWY6qEiIQYY2fjPM0ZP-hypYUCa9PnQqN-j1OLfEnpiKG87UN0FksO_HVgNsv6ngtFZnGIkMoDl9OWgCp8WUH5VnqHBvrlPQ.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=Jwfi_WKiEdwQ7kNvwH5BXbG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTIzMTYwNDA4NTQ3MzYwOCwiYXNzZXRfYWdlX2RheXMiOjEzNCwidmlfdXNlY2FzZV9pZCI6MTA4MjcsImR1cmF0aW9uX3MiOjQzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=5688269e4af95591&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GNzRCRDkyNDRFM0E1NTVBMEU3NDgzOTZEREI0N0VBQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQVhQNFNJYWJFSTFSTzBDQUR4cnpMUWVaSGg1YnN0VEFRQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkIWmwOWIsAQVAigCQzMsF0BFqp--dsi0GBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2WWqQEA&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3c9BFsERN3Xb_sPDBgrknXqvX3KEk_higbM98jpyp5fA&oe=69D82F26",
                "url_expiration_timestamp_us": null,
                "width": 720,
                "fallback": null
              }
            ],
            "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT43.350204S\" FBManifestTimestamp=\"1775658011\" FBManifestIdentifier=\"FraQs50NGA9yMmF2MS1yMWdlbjJ2cDkZhoLZiJCV8oQDlqf167KQmQSA9fiU7qbjBIC1sr2Nn/cEiMSx0raGsQW6xriOgdK6Be7Rv4To8PIGpruSlYjnog8iGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYDmxhdGFtX21vZGVyYXRlABaMAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT43.350204S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:83.1\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1515237436436740v\" bandwidth=\"349100\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"1890961\" FBPlaybackResolutionMos=\"0:100,360:37.7,480:35.5,720:33.8,1080:34.3,1440:35.2,2160:37.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:67.7,480:58.8,720:46.2,1080:32.9,1440:24.3,2160:13.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNsa1WkwGHwaYQTLAtbv4b7MByH_feHeZ9G5aWV_SkjhADjwqc_35yxO8GlgrIDe5Iix3U9KNj8CFfScqowQG8hAbL8_6NA5t9f2SE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=IE16Rn1r0wMQ7kNvwGpjSxc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjM0OTEwMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af30M9lGOkAj9TnIZjZ-791mU75k-cRQnxHLMaKKNuxSlw&amp;oe=69DC329E</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-16019\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-64496\" FBFirstSegmentRange=\"966-102836\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"102837-291096\" FBPrefetchSegmentRange=\"966-102836\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1344270830083392v\" bandwidth=\"976753\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"5290748\" FBPlaybackResolutionMos=\"0:100,360:64.1,480:59.3,720:53.4,1080:51.3,1440:51.2,2160:51.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.6,480:85.9,720:78.3,1080:68.3,1440:59.9,2160:47.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMRDWpnhBovNEPuhqsJ2xRiT0FD4IN4dP2g3wT8RBSYninYDmFfD7wHRz4as7KOBwlvBlmKu3GheOi6Vt0-t8WM6-I9IXgiJMgqreI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=dke0F2YqSwsQ7kNvwHirvUs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjk3Njc1MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1apKs2cpb1Wo8ZGpBkhM2PwTkP9nrxK6Kmflq-t5njVw&amp;oe=69DC1B2B</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-32240\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-258610\" FBFirstSegmentRange=\"966-432886\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"432887-1000442\" FBPrefetchSegmentRange=\"966-432886\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1536327131009437v\" bandwidth=\"1393255\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"7546800\" FBPlaybackResolutionMos=\"0:100,360:72.1,480:67.3,720:60.2,1080:57,1440:56.4,2160:56.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.5,480:91.1,720:85.5,1080:77.3,1440:69.8,2160:58.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQM7gWOMxlG8Zo3cs6bLqkLPmfRyx7ywN6PEzVRyWcDvbCi6wNjCo4lL0aLvbNANxdcfBCmt9z00f-OAKW4BmzhXL0huV0ngTimtofQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=WRCizycxgSgQ7kNvwGll-3c&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjEzOTMyNTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2IIlTKxwFl9fbBeClj5wERJOgB6Zj5bLkXnwO_kTkOXA&amp;oe=69DC3552</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-40053\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-410190\" FBFirstSegmentRange=\"966-688189\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"688190-1525563\" FBPrefetchSegmentRange=\"966-688189\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"855182363661889v\" bandwidth=\"1903534\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"10310811\" FBPlaybackResolutionMos=\"0:100,360:77.5,480:73.1,720:65.8,1080:61.7,1440:60.7,2160:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.4,480:93.6,720:89.5,1080:82.4,1440:75.7,2160:65\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOVkH6CDtowcCB9haURfdct7bLVG-n2JL8QSZ14vC8l-CGfhdunO2Qr4oDVY_9iuXCAQgEZzrAH2W6ov_ziAWlKn1WIKu_CIG8X-0I.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=f2vaIaCLHTIQ7kNvwEmVhDF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjE5MDM1MzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Ub2cenSLMZfQdQydkwcuji_zXdBxsGA5yGP7L0A5-3Q&amp;oe=69DC3FCF</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-46389\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-571504\" FBFirstSegmentRange=\"966-969927\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"969928-2158207\" FBPrefetchSegmentRange=\"966-969927\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1181157190183371v\" bandwidth=\"2456971\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"13308597\" FBPlaybackResolutionMos=\"0:100,360:80.9,480:76.2,720:69.5,1080:65.1,1440:63.9,2160:62.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.5,480:95.3,720:92,1080:85.8,1440:79.9,2160:69.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPr-GxM0r1x8Er9sovANffZH5SuP30_4f93S6v6bbK05eoQo2BXND0wnddznZBRTlCllQunAy7irEsZvEor1N2AJ4MsfiXpsMdT00c.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=7wfAY__1GeMQ7kNvwHx9w2P&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjI0NTY5NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2AveJZeXe5D604BlfDdDq2hFproEcOkBM4Wj-B1NMSwA&amp;oe=69DC4E56</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-51033\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-728865\" FBFirstSegmentRange=\"966-1249505\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1249506-2844600\" FBPrefetchSegmentRange=\"966-1249505\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1941476620104823v\" bandwidth=\"3236225\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"17529554\" FBPlaybackResolutionMos=\"0:100,360:85.1,480:80.7,720:73.8,1080:69,1440:67.7,2160:66.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.2,480:96.4,720:93.9,1080:88.5,1440:83.3,2160:74.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMZocCbzqoSGKwGEXI-j6dx9dCC7b8WLI5dsKRKeDg1dENAUVPt1Ffs9IcckXciyXQW6FyeVlGLlBcclGCtFX5gwni-t1fd-y33-jw.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=1-KoOwi_6bEQ7kNvwEXE-hr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjMyMzYyMjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1OPUzfeen2PYFFJ-D2VoW44qrI7nMJC-9-8Okd677d6Q&amp;oe=69DC2CDB</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-56201\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-904989\" FBFirstSegmentRange=\"966-1578295\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1578296-3822187\" FBPrefetchSegmentRange=\"966-1578295\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4298662063787731v\" bandwidth=\"4682144\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"25361616\" FBPlaybackResolutionMos=\"0:100,360:91.4,480:88.7,720:83.9,1080:79.2,1440:77.4,2160:76.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.35,480:98.09,720:97.3,1080:94.9,1440:92.1,2160:86.7\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO0v_puE3WwSPBYMJ5dWM2cER6q0XUu4ks7xkuBnEjtgSA-cCPJS0R4UXjKd7o9uc7iI1qOOQZdSlmf6IwHa-tDtnBgAIkfXIKJuu4.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=HoiB_cqebeYQ7kNvwEF1dXo&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjQ2ODIxNDQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af27eYQfqpJzHipQugdvddNryLDiX74KTF7VJM6-O3_BNw&amp;oe=69DC27B8</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-83585\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-1319664\" FBFirstSegmentRange=\"966-2334099\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"2334100-5576869\" FBPrefetchSegmentRange=\"966-2334099\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1388118059404608a\" bandwidth=\"74757\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74757\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"406206\" FBPaqMos=\"86.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t16/f2/m69/AQNNB7DglnfOPDJxu7IlZxgUHa1pqKy7W-QDx4zSqU-_2ZZUSTSJjyUtxesGpE9vSZciqgDopVme84YBb51ooz84.mp4?strext=1&amp;_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=yA3Q737n7AEQ7kNvwHaVAaL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjc0OTYyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2l4-XzanVB5PnmmCQDC9fhxa6UlMwloT6w0gNJeq4Tiw&amp;oe=69DC2D5C</BaseURL><SegmentBase indexRange=\"824-1119\" timescale=\"44100\" FBMinimumPrefetchRange=\"1120-1463\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1120-31781\" FBFirstSegmentRange=\"1120-27306\" FBFirstSegmentDuration=\"2021\" FBSecondSegmentRange=\"27307-48972\" FBPrefetchSegmentRange=\"1120-48972\" FBPrefetchSegmentDuration=\"4017\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "number_of_qualities": 7,
            "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
            "sharing_friction_info": {
              "should_have_sharing_friction": false,
              "bloks_app_url": null,
              "sharing_friction_payload": null
            },
            "gen_ai_detection_method": {
              "detection_method": "NONE"
            },
            "explore_demotion_control": null,
            "clips_demotion_control": {
              "title": "Not interested",
              "enable_word_wrapping": true,
              "confirmation_icon": "none",
              "title_style": "normal",
              "confirmation_title": "Post hidden",
              "confirmation_body": "We'll suggest fewer posts like this.",
              "confirmation_title_style": "large_left",
              "undo_style": "top_right",
              "confirmation_style": "bottomsheet",
              "followup_options": [
                {
                  "text": "Don't suggest posts from hobopeeba",
                  "style": null,
                  "id": "dislike_author",
                  "data": "author_id:47276232",
                  "show_icon": true,
                  "demotion_control": {
                    "confirmation_style": "bottomsheet",
                    "confirmation_icon": "eye-off-pano",
                    "confirmation_body": "We won't suggest posts from hobopeeba.",
                    "undo_style": "inline"
                  },
                  "subtitle": null
                },
                {
                  "text": "Don't suggest posts with certain words",
                  "id": "hide_all_specific_words",
                  "show_icon": true,
                  "data": null,
                  "style": null,
                  "demotion_control": null,
                  "subtitle": null
                }
              ]
            },
            "text_post_app_info": null,
            "user": {
              "strong_id__": "47276232",
              "all_media_count": null,
              "allowed_commenter_type": null,
              "coeff_weight": null,
              "fbid_v2": 17841401326960738,
              "feed_post_reshare_disabled": false,
              "id": "47276232",
              "is_active": null,
              "is_unpublished": false,
              "liked_clips_count": null,
              "live_invite_only_branding_enabled": null,
              "pk": 47276232,
              "pk_id": "47276232",
              "reel_auto_archive": null,
              "show_insights_terms": null,
              "text_post_app_take_a_break_setting": null,
              "third_party_downloads_enabled": 1,
              "eligible_for_text_app_activation_badge": false,
              "account_type": 3,
              "account_badges": [],
              "can_boost_post": null,
              "can_see_organic_insights": null,
              "fan_club_info": {
                "autosave_to_exclusive_highlight": null,
                "connected_member_count": null,
                "fan_club_id": null,
                "fan_club_name": null,
                "has_created_ssc": null,
                "has_enough_subscribers_for_ssc": null,
                "is_fan_club_gifting_eligible": null,
                "is_fan_club_referral_eligible": null,
                "is_free_trial_eligible": null,
                "largest_public_bc_id": null,
                "subscriber_count": null,
                "should_show_playlists_in_profile_tab": null,
                "fan_consideration_page_revamp_eligiblity": null
              },
              "full_name": "Kristina Makeeva↟Kotleta↟Timon",
              "friendship_status": {
                "following": false,
                "is_bestie": false,
                "is_feed_favorite": false,
                "is_private": false,
                "is_restricted": false,
                "text_post_app_pre_following": null,
                "followed_by": false,
                "is_muting_reel": false
              },
              "has_anonymous_profile_picture": false,
              "has_onboarded_to_text_post_app": null,
              "interop_messaging_user_fbid": null,
              "is_favorite": false,
              "is_private": false,
              "is_ring_creator": false,
              "show_ring_award": false,
              "aigm_account_label_info": null,
              "is_verified": true,
              "is_ai_user": null,
              "ai_agent_owner_username": null,
              "live_broadcast_id": null,
              "live_broadcast_visibility": null,
              "profile_pic_id": null,
              "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.2885-19/11910054_1626257790981501_575133001_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=dfhJaS_x2qUQ7kNvwFjC5sN&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8BAAAA&ccb=7-5&ig_cache_key=GKa7tQB91fGlEscFAEnVRyIAAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af3q37U7g1ytol3Zolq--ybwR5CPdnBB-MG_ciy6buNVeQ&oe=69DC3C02&_nc_sid=026283",
              "reachability_status": null,
              "show_account_transparency_details": true,
              "transparency_product_enabled": false,
              "transparency_product": null,
              "transparency_label": null,
              "username": "hobopeeba",
              "opal_info": null,
              "latest_reel_media": 1775656956,
              "user_activation_info": {
                "activation_type": null,
                "rings_custom_likes_setting_enabled": null
              },
              "text_post_app_privacy": null
            },
            "community_notes_info": {
              "has_viewer_submitted_note": false,
              "note_submission_disabled": false,
              "enable_submission_friction": false,
              "is_eligible_for_request_a_note": true
            },
            "has_high_risk_gen_ai_inform_treatment": false,
            "caption_is_edited": false,
            "code": "DRcpa03DPoG",
            "device_timestamp": 1764005343564115,
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
            "is_comments_gif_composer_enabled": true
          }
        },
        {
          "media": {
            "strong_id__": "3858117062538838388_787132",
            "context__": null,
            "id": "3858117062538838388_787132",
            "is_post_live": null,
            "disable_caption_and_comment": false,
            "fbid": 18143103847436632,
            "is_music_only_story": null,
            "soft_deleted_at": null,
            "deleted_reason": 0,
            "client_cache_key": "Mzg1ODExNzA2MjUzODgzODM4OA==.3",
            "has_bc_violation": null,
            "integrity_review_decision": "pending",
            "is_awaiting_distribution": null,
            "is_reel_media": null,
            "is_sidecar_child": null,
            "sticker_translations_enabled": null,
            "subscription_media_visibility": null,
            "timezone_offset": null,
            "pk": 3858117062538838388,
            "is_affiliate_commission_eligible": false,
            "visibility": null,
            "expiring_at": null,
            "organic_cta_type": null,
            "has_delayed_metadata": false,
            "client_cache_expiration_ts": null,
            "is_eof": null,
            "mezql_token": "",
            "should_request_ads": false,
            "has_privately_liked": false,
            "dynamic_ad_carousel_card_starting_index": null,
            "log_time": null,
            "is_quiet_post": false,
            "collaborator_edit_eligibility": false,
            "share_count_disabled": false,
            "is_reshare_of_text_post_app_media_in_ig": false,
            "ranking_weight": null,
            "ranked_at": null,
            "algorithm": null,
            "connection_id": null,
            "carousel_last_edited_at": null,
            "is_visual_reply_commenter_notice_enabled": true,
            "media_level_comment_controls": null,
            "translated_langs_for_autodub": [],
            "is_terminal_video_segment": null,
            "segmented_video_group_id": null,
            "subtype_name_for_REST__": "XDTClipsMedia",
            "is_third_party_downloads_eligible": false,
            "clips_mashup_follow_button_info": null,
            "has_views_fetching_on_search_grid": null,
            "linked_media_playlist_data": null,
            "image_versions2": {
              "additional_candidates": {
                "first_frame": {
                  "estimated_scans_sizes": [
                    5565,
                    11130
                  ],
                  "height": 1136,
                  "scans_profile": "e15",
                  "url": "https://scontent-mia3-1.cdninstagram.com/v/t51.71878-15/655553667_1694908385008299_7686189627358299085_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=qFnrJzP0x5IQ7kNvwFTOeca&_nc_oc=AdqIJnHGKeNT1q6jcMuwBBLqF_PvghhSh6wPK8HmHL0IcAWILgCrq1SbBlePplIA-f4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&oh=00_Af2D2_4qPANy32-qDk46g7oy_AVOx2qZBIaFafe9Iib4oQ&oe=69DC3AA8",
                  "width": 640,
                  "is_spatial_image": false
                },
                "igtv_first_frame": {
                  "estimated_scans_sizes": [
                    5565,
                    11130
                  ],
                  "height": 1136,
                  "scans_profile": "e15",
                  "url": "https://scontent-mia3-1.cdninstagram.com/v/t51.71878-15/655553667_1694908385008299_7686189627358299085_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=qFnrJzP0x5IQ7kNvwFTOeca&_nc_oc=AdqIJnHGKeNT1q6jcMuwBBLqF_PvghhSh6wPK8HmHL0IcAWILgCrq1SbBlePplIA-f4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&oh=00_Af2D2_4qPANy32-qDk46g7oy_AVOx2qZBIaFafe9Iib4oQ&oe=69DC3AA8",
                  "width": 640,
                  "is_spatial_image": false
                },
                "smart_frame": null
              },
              "candidates": [
                {
                  "estimated_scans_sizes": [
                    22552,
                    45105
                  ],
                  "height": 1333,
                  "scans_profile": "e35",
                  "url": "https://scontent-mia5-2.cdninstagram.com/v/t51.82787-15/655918808_18642480373019133_2706709073646407389_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzg1ODExNzA2MjUzODgzODM4ODE4NjQyNDgwMzY3MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=mR20z9GjA6kQ7kNvwFzvy9B&_nc_oc=Adp-cUnypkpwyoOb-mGrDz3PBgGmFAs1fZlNz1rzzUKy60_xmMccQNmBzzEnQ7EK0C0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia5-2.cdninstagram.com&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&oh=00_Af0dcdpMG2HFIg0J05bFcB5us7FWRGIkZyrDx_kT-SDp8w&oe=69DC2102",
                  "width": 750,
                  "is_spatial_image": false
                }
              ],
              "scrubber_spritesheet_info_candidates": {
                "default": {
                  "file_size_kb": 399,
                  "max_thumbnails_per_sprite": 105,
                  "rendered_width": 96,
                  "sprite_height": 1232,
                  "sprite_urls": [
                    "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/655031270_1813608302668544_4756991555773361514_n.jpg?_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=j6Cki5vnLssQ7kNvwH0s7TA&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8BAAAA&ccb=7-5&oh=00_Af3pPdDxWH9U5D8ouNI4LcwgIYHOQNqMLPQbdo8vPRISdA&oe=69DC1E0E&_nc_sid=026283"
                  ],
                  "sprite_width": 1500,
                  "thumbnail_duration": 0.3581333333333333,
                  "thumbnail_height": 176,
                  "thumbnail_width": 100,
                  "thumbnails_per_row": 15,
                  "total_thumbnail_num_per_sprite": 105,
                  "video_length": 37.604
                }
              }
            },
            "wearable_attribution_info": null,
            "clips_timely_event_info": null,
            "media_cropping_info": null,
            "media_type": 2,
            "original_width": 1080,
            "original_height": 1920,
            "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYzEwMjc3ZmE0YjM3NGVjY2E3ODZkZjAzYjRjY2VkYTkzODU4MTE3MDYyNTM4ODM4Mzg4Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1ODAxMDMxOHwzODU4MTE3MDYyNTM4ODM4Mzg4fDM1Mzk0NDM1MDEzfGZkMGJmOTExZDFhMjc0OWJhOGYxOTZmMDc2YWQzODg5NmZmM2IxY2JjZWE4ZjljZGU1OTg5MjJmNDBhNTYzYTAifSwic2lnbmF0dXJlIjoiIn0=",
            "attribution": null,
            "caption_add_on": null,
            "music_metadata": null,
            "clips_trial": null,
            "has_tagged_users": true,
            "is_eligible_for_media_note_recs_nux": null,
            "is_shared_from_basel": null,
            "show_story_deleted_error_label": null,
            "is_dismiss_pending_media_banner": null,
            "clips_tab_pinned_user_ids": [],
            "is_spinnable": null,
            "clips_attribution_info": null,
            "original_lang_for_translations": "en",
            "all_previous_submitters": null,
            "app_install_cta_info": null,
            "archived_media_timestamp": null,
            "can_hype": null,
            "highlights_info": null,
            "igtv_series_info": null,
            "is_fb_only": null,
            "is_internal_only": null,
            "is_open_to_public_submission": false,
            "is_social_ufi_disabled": false,
            "is_viewer_location_nearby": null,
            "previous_submitter": null,
            "timeline_pinned_user_ids": [],
            "title": null,
            "taken_at": 1774198805,
            "usertags": null,
            "photo_of_you": false,
            "can_see_insights_as_brand": false,
            "fundraiser_tag": {
              "has_standalone_fundraiser": false
            },
            "media_notice": null,
            "media_prompt_data": null,
            "text_sticker_content": null,
            "has_translation": null,
            "accessibility_caption": null,
            "content_scheduling_metadata": null,
            "media_appreciation_settings": null,
            "organic_post_id": null,
            "media_gating_info": null,
            "lumen_logging_info": null,
            "display_uri": null,
            "fb_user_tags": {
              "in": []
            },
            "mashup_info": null,
            "visual_replies_info": null,
            "gating": null,
            "preview": null,
            "media_overlay_info": null,
            "is_in_profile_grid": false,
            "profile_grid_control_enabled": false,
            "attribution_content_url": null,
            "channel_tag_data": null,
            "is_artist_pick": false,
            "copyright_attribution_info": null,
            "media_notes": {
              "items": []
            },
            "linked_media_data": null,
            "product_type": "clips",
            "inventory_source": null,
            "story_polls": null,
            "social_context": [],
            "should_have_hscroll_items": null,
            "explore": null,
            "story_poll_voter_infos": null,
            "audio": null,
            "subscribe_cta_visible": false,
            "creative_config": null,
            "is_cutout_sticker_allowed": false,
            "cutout_sticker_info": [],
            "cutout_stickers": null,
            "is_seen": null,
            "main_feed_carousel_starting_media_id": null,
            "main_feed_carousel_has_unseen_cover_media": null,
            "text_with_entities": null,
            "mv_link": null,
            "shimmed_mv_link": null,
            "mv_link_info": null,
            "mv_original_content_review_status": null,
            "story_prompts": null,
            "story_notify_me_stickers": null,
            "immersive_media_metadata": null,
            "text_post_share_to_ig_story_stickers": null,
            "is_tagged_media_shared_to_viewer_profile_grid": false,
            "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
            "impression_token": null,
            "meta_place": null,
            "reminder_info": null,
            "meta_ai_suggested_prompts": [],
            "gen_ai_chat_with_ai_cta_info": null,
            "gen_ai_share_info": null,
            "can_reply": false,
            "floating_context_items": [],
            "is_eligible_content_for_post_roll_ad": false,
            "instream_ad_media_eligibility_info": null,
            "contextual_ads_info": null,
            "item_client_gap_rules": null,
            "explore_context": null,
            "multi_ads_info": null,
            "nearly_complete_copyright_match": null,
            "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
            "related_ads_pivots_organic_search_query": null,
            "geo_gated_countries": null,
            "has_overflow_bubbles": null,
            "tallest_media_aspect_ratio": null,
            "giphy_media_info": null,
            "eligible_insights_entrypoints": "NONE",
            "basel_encoding_timeout": null,
            "media_attributions_data": [],
            "media_ui_attributions_data": [],
            "media_ui_attributions_data_v2": [],
            "clips_on_impression_control": null,
            "snippets_overlays": null,
            "snippets_attribution_info": null,
            "creator_product_links": null,
            "creator_product_link_infos": [],
            "is_eligible_for_poe": true,
            "is_eligible_for_organic_eager_refresh": false,
            "cta_rendering_config": null,
            "commerce_integrity_review_decision": "",
            "is_reuse_allowed": false,
            "goals_toast_info": null,
            "logging_info_token": "GCA2ODI5ZDc1ODI4MmQ0NDMxYTM2YmEyYzE5OTZiOWUwZHgDbmhhAA==",
            "clips_delivery_parameters": null,
            "basel_inspiration_info": null,
            "basel_sticky_note": null,
            "boosted_status": null,
            "boost_unavailable_identifier": null,
            "boost_unavailable_reason": null,
            "boost_unavailable_reason_v2": null,
            "is_currently_promoting_by_sponsor": null,
            "boosted_by_sponsor": null,
            "boosted_post_id": null,
            "branded_content_ads_boost_post_tokens": null,
            "branded_content_project_metadata": null,
            "coauthor_producers": [],
            "coauthor_producer_can_see_organic_insights": false,
            "invited_coauthor_producers": [],
            "collab_follow_button_info": null,
            "product_suggestions": null,
            "igbio_product": null,
            "ig_iab_post_click_data": null,
            "is_eligible_for_shoppable_everything": null,
            "shoppable_everything_detected_objects": null,
            "sponsor_tags": null,
            "is_paid_partnership": false,
            "reshare_count": 1947,
            "has_reshares": null,
            "ig_media_sharing_disabled": false,
            "media_repost_count": 237,
            "score": null,
            "ranking_scores_list": null,
            "recommendation_data": null,
            "feed_delivery_parameters": null,
            "feed_ranking_source_debug_label": null,
            "view_state_item_type": 128,
            "clips_metadata": {
              "clips_creation_entry_point": "",
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
                "best_audio_cluster_id": "1220061383628147"
              },
              "audio_type": "original_sounds",
              "basel_video_composition_model": null,
              "basel_reusable_elements": null,
              "basel_template_info_for_ig_app": {
                "is_basel_template": null,
                "should_show_reuse_setting_for_owner": false,
                "use_template_deeplink": null
              },
              "basel_template_attribution": null,
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
                "is_reuse_allowed": false,
                "mashup_type": null,
                "mashups_allowed": false,
                "mashups_allowed_for_carousel": false,
                "non_privacy_filtered_mashups_media_count": 0,
                "privacy_filtered_mashups_media_count": null,
                "original_media": null
              },
              "merchandising_pill_info": null,
              "music_canonical_id": "18383015785088339",
              "music_info": null,
              "nux_info": null,
              "original_sound_info": {
                "allow_creator_to_rename": true,
                "audio_asset_id": 27387546600834059,
                "attributed_custom_audio_asset_id": null,
                "can_remix_be_shared_to_fb": true,
                "can_remix_be_shared_to_fb_expansion": true,
                "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT37.610668S\" FBManifestTimestamp=\"1775658009\" FBManifestIdentifier=\"FrKQs50NKRby17XfxremByIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT37.610668S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2054842108786169a\" bandwidth=\"64951\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"64951\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-2.cdninstagram.com/o1/v/t2/f2/m78/AQM87tGAxYDcH_vtoAgdbwsOZVfN4WeLw9hmtF_INFSyOfXcnEBoQ7NGjMemGr0C6HP3jrAsY2Z3mrybxMK5KtN_OypOImBTGs9uRJ4.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-2.cdninstagram.com&amp;_nc_ohc=6whQT-A6cosQ7kNvwHgpWQp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6NjUxODEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3Whs36Hr4WLGxKBywnOOXfeScK26vo8Nlc1n4u6tSLSw&amp;oe=69D85429</BaseURL><SegmentBase indexRange=\"824-1083\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "duration_in_ms": 37604,
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
                "original_media_id": 3858117062538838388,
                "progressive_download_url": "https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOV-Ur7ng9jWe--_YcoceqdEwirl6SPWzXU7OLxwNrL_adqoJgRIP-Iq6-LY0GkC1css6LJX77Z9zfPSBsjsYs.mp4?_nc_cat=102&_nc_sid=8bf8fe&_nc_ht=scontent-mia5-1.cdninstagram.com&_nc_ohc=_67fhGgdTgUQ7kNvwHT-ITG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTE1NTIwNTIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxNywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2hUqELiUqe61hoaQZtWjaHJ19C9e-6dCsLZjN1qDXDaw&oe=69D82ACA",
                "should_mute_audio": false,
                "time_created": 1774198811,
                "trend_rank": null,
                "previous_trend_rank": null,
                "overlap_duration_in_ms": 0,
                "audio_asset_start_time_in_ms": 0,
                "derived_content_start_time_in_composition_in_ms": 0,
                "ig_artist": {
                  "strong_id__": "787132",
                  "pk": 787132,
                  "pk_id": "787132",
                  "id": "787132",
                  "username": "natgeo",
                  "full_name": "National Geographic",
                  "is_private": false,
                  "is_verified": true,
                  "profile_pic_id": "3865702555259028436_787132",
                  "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=XbeNvhLXv28Q7kNvwGuzNfJ&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3cephpO5cYpdbzxafS_wTWLLmLch8DZiGu-38W0PxU4A&oe=69DC51E9&_nc_sid=026283"
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
            "story_sliders": null,
            "story_quizs": null,
            "story_slider_voter_infos": null,
            "story_quiz_participant_infos": null,
            "story_questions": null,
            "question_response_reply_stickers_info": null,
            "story_bloks_tappables": null,
            "avatar_stickers": null,
            "clips_karaoke_caption": null,
            "clips_chats": null,
            "clips_captions": null,
            "clips_captions_translations_urls": null,
            "clips_text": null,
            "visual_comment_reply_sticker_info": null,
            "carousel_media_count": null,
            "carousel_media_pending_post_count": null,
            "can_modify_carousel": null,
            "carousel_media_ids": null,
            "carousel_media": null,
            "total_carousel_media_count": null,
            "more_carousel_media_available": null,
            "open_carousel_show_follow_button": null,
            "open_carousel_submission_state": null,
            "like_count": 19257,
            "fb_like_count": null,
            "top_likers": [],
            "facepile_top_likers": null,
            "hidden_likes_string_variant": -1,
            "has_viewer_saved": null,
            "saved_collection_ids": null,
            "save_count": null,
            "caption": {
              "strong_id__": "18143195824436632",
              "background_color": null,
              "bit_flags": 0,
              "created_at": 1774198809,
              "created_at_utc": 1774198809,
              "did_report_as_spam": false,
              "is_ranked_comment": false,
              "pk": "18143195824436632",
              "share_enabled": false,
              "text_size": null,
              "background_color_alpha": null,
              "content_type": "comment",
              "media_id": 3858117062538838388,
              "status": "Active",
              "text_color": null,
              "type": 1,
              "user_id": 787132,
              "has_translation": null,
              "mention_user_list": null,
              "text": "Actress and National Geographic 33 changemaker @priyankachopra is on a mission to make health care more accessible.\n\nThe National Geographic 33—inspired by our 33 founders—is an initiative honoring changemakers who are rising to meet the most critical challenges of our time, making meaningful progress and incredible breakthroughs. See the full list at the link in bio. #NatGeo33",
              "user": {
                "strong_id__": "787132",
                "pk": 787132,
                "pk_id": "787132",
                "id": "787132",
                "coeff_weight": null,
                "is_active": null,
                "is_unpublished": false,
                "fbid_v2": 17841400573960012,
                "username": "natgeo",
                "full_name": "National Geographic",
                "is_private": false,
                "is_verified": true,
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=XbeNvhLXv28Q7kNvwGuzNfJ&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3cephpO5cYpdbzxafS_wTWLLmLch8DZiGu-38W0PxU4A&oe=69DC51E9&_nc_sid=026283",
                "has_onboarded_to_text_post_app": null
              },
              "fb_mentioned_users": null,
              "is_covered": false,
              "mentioned_users": null,
              "private_reply_status": 0,
              "text_translation": null
            },
            "comment_count": 813,
            "commenting_disabled_for_viewer": null,
            "comments_disabled": null,
            "inline_composer_display_condition": null,
            "inline_composer_imp_trigger_time": null,
            "has_hidden_comments": null,
            "comment_inform_treatment": {
              "action_type": null,
              "should_have_inform_treatment": false,
              "text": "",
              "url": null
            },
            "show_keyboard_in_comments": null,
            "is_photo_comments_composer_enabled_for_author": false,
            "fb_comment_count": null,
            "hide_view_all_comment_entrypoint": true,
            "location": null,
            "locations": [],
            "lng": null,
            "lat": null,
            "play_count": 2670433,
            "ig_play_count": 2670433,
            "fb_play_count": null,
            "view_count": null,
            "bucketed_view_count": null,
            "carrera_topic": null,
            "carrera_topic_metadata": null,
            "overflow_carrera_topics": null,
            "are_remixes_crosspostable": true,
            "crosspost": null,
            "crosspost_metadata": {
              "fb_crosspost_deeplink_profile_id": null,
              "fb_crosspost_fbid": null,
              "is_feedback_aggregated": null,
              "is_feed_feedback_aggregated": null,
              "th_unified_feedback_row_tap_target_url": null,
              "unified_feedback_enabled": null,
              "fb_downstream_use_xpost_metadata": {
                "downstream_use_xpost_deny_reason": "NONE"
              }
            },
            "xpost_deny_reason": null,
            "xpost_deny_reason_enum": null,
            "threads_xpost_deny_reason": null,
            "autodub_status": null,
            "byoa_langs": null,
            "is_eligible_for_autodub": false,
            "is_eligible_for_autodub_upsell": false,
            "voice_translations_consumption_data": null,
            "video_subtitles_locale": null,
            "video_subtitles_confidence": null,
            "video_subtitles_enabled": null,
            "video_subtitles_uri": null,
            "video_subtitles_translations_enabled": null,
            "translated_video_subtitles": null,
            "video_sticker_locales": [],
            "transcription_data": null,
            "has_audio": true,
            "video_duration": 37.61000061035156,
            "is_dash_eligible": 1,
            "video_versions": [
              {
                "bandwidth": 591389,
                "height": 1280,
                "id": "1165530622219418v",
                "type": 101,
                "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPwVfdlglvtOj812P15FmBDCW7nx326yjhRtQLrhVJ1CdRXu65XvcOSyEpa_0AKKjMIsHgB4kf2WUF0NEcJ62zoMyYWnU82jvHWjhk.mp4?_nc_cat=107&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=pQISOkPrSb8Q7kNvwHc8Ph5&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTE1NTIwNTIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxNywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=ee5d5b009a3aa7e0&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83MDQzOUQ4NTJCNzhDNUM4NEFERTVDNjBCRjdGNDI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0EzNDVCQzYxOTAxREY3NzIyN0E5Q0RGMUJEMDUwNUIwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWlN2z7bXjPxUCKAJDMywXQELNT987ZFoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3boVNnfRkvwcFjYc3UxcmMCS3pH8PES3NN4pnPjgxhvw&oe=69D840D4",
                "url_expiration_timestamp_us": null,
                "width": 720,
                "fallback": null
              },
              {
                "bandwidth": 591389,
                "height": 1280,
                "id": "1165530622219418v",
                "type": 102,
                "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPwVfdlglvtOj812P15FmBDCW7nx326yjhRtQLrhVJ1CdRXu65XvcOSyEpa_0AKKjMIsHgB4kf2WUF0NEcJ62zoMyYWnU82jvHWjhk.mp4?_nc_cat=107&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=pQISOkPrSb8Q7kNvwHc8Ph5&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTE1NTIwNTIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxNywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=ee5d5b009a3aa7e0&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83MDQzOUQ4NTJCNzhDNUM4NEFERTVDNjBCRjdGNDI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0EzNDVCQzYxOTAxREY3NzIyN0E5Q0RGMUJEMDUwNUIwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWlN2z7bXjPxUCKAJDMywXQELNT987ZFoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=dskAJegcZpmj0Vy1podVGw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3boVNnfRkvwcFjYc3UxcmMCS3pH8PES3NN4pnPjgxhvw&oe=69D840D4",
                "url_expiration_timestamp_us": null,
                "width": 720,
                "fallback": null
              }
            ],
            "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT37.610668S\" FBManifestTimestamp=\"1775658011\" FBManifestIdentifier=\"FraQs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZpszI/u+ijKkDotyLw4iwugS24OGt8M3VBKCdqurpn9cE5tOwqvqmmAXM/ceI66CfBfT41Kyg2awH8OCRhNiD0geQ9rnultWdCriHhfGom7RdIhgmZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlMTIzNF9pYnJfYXVkaW8iLBkYDmxhdGFtX21vZGVyYXRlABYiFAASFAIA\"><Period id=\"0\" duration=\"PT37.610668S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:77.6\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"934795722871334v\" bandwidth=\"158286\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"744031\" FBPlaybackResolutionMos=\"0:100,360:83.1,480:79.1,720:74.8,1080:71.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.5,480:95.6,720:92.7,1080:86.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/400\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOwALZbK4Z2-hWiF-CSexLDqF79HRcqqSkXR4siF-drzmUN0CnAMoQ2o6Y6RXTtF0Swp2jrWXG88bITSyCP2VpZZWCB_axna3z8BQU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=AeBLuI-fB6AQ7kNvwFOl23B&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjE1ODI4NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3qxK4zAyLgAyYJ_MsSa355lp-IA-Yu594TvRhNmPKAIg&amp;oe=69DC4653</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-39540\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-75860\" FBFirstSegmentRange=\"954-101121\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"101122-166750\" FBPrefetchSegmentRange=\"954-101121\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"26291991387087324v\" bandwidth=\"259930\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"1221812\" FBPlaybackResolutionMos=\"0:100,360:87.9,480:84.9,720:81.2,1080:76.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.8,480:97.6,720:97.9,1080:94.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMHE68zYgqvRzeor8Wxi_ybur2uTo7Ar6hsLsHTzhfETCzIprQB37x-rOb7Wtb6cJ1OtbugVCpittc7NCtcV_w_RJI4-HQgn6Jjd7g.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=i2MosldJOpwQ7kNvwGMON13&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjI1OTkzMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Z7wfEdMwlQGkckC2McGcFh_g6R0YkoAwTczRu0c_5ww&amp;oe=69DC4A24</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-60671\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-125281\" FBFirstSegmentRange=\"954-167240\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"167241-273912\" FBPrefetchSegmentRange=\"954-167240\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1460820695717107v\" bandwidth=\"362057\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"1701862\" FBPlaybackResolutionMos=\"0:100,360:90,480:87.2,720:83.8,1080:78.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.4,480:98.4,720:98.93,1080:95.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNBGstUjgCkHXBEz3O4C_zxljZyU9AkdDU85vfiaCCEK-gFiuQ88YQ-0DSh7BJt5kN4W5XP3MEOXPnsIqL7Fv_nHeuR3mK8N7AYcVI.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=lwZ2op-beLEQ7kNvwEAtJTb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjM2MjA1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2NCvU_a6M9TmDTnoKXg8rGTnjg36lTCQzY0ti4YaJ_FQ&amp;oe=69DC409B</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-77385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-173166\" FBFirstSegmentRange=\"954-233283\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"233284-381968\" FBPrefetchSegmentRange=\"954-233283\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2150708099037240v\" bandwidth=\"506743\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"2381963\" FBPlaybackResolutionMos=\"0:100,360:91.5,480:88.8,720:85.7,1080:80.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.84,480:98.94,720:99.537,1080:96.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPiWL8aXblpTq38UZsTU1eitafqyty7JpAL9sXa_U2JrS6ILxtki5SmHBHFPThMc4-PkxUA9JcYcp5wLYtaFfPsNJgylPPImv1hs8k.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=_270KmJ235AQ7kNvwFUUVuL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjUwNjc0MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af33zbw2cwxqCovvoGQCfUFR-q3B22V3r3N5AYzDfjVPxg&amp;oe=69DC3E26</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-95531\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-235238\" FBFirstSegmentRange=\"954-323945\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"323946-531369\" FBPrefetchSegmentRange=\"954-323945\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1317761710376784v\" bandwidth=\"763143\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"3587180\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:90.1,720:87,1080:81.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.226,480:99.418,720:99.854,1080:97.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOcTbLjDfQaONR5BHPWpFlF5aAUbnBsEwfC0fkA8JbyLBQBNobDngwrCf_iC0SNsHyO9nXWsd9nCNkt3YKf3dlQbseHq8M5Q5CtKjQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=i8UFZaAx8ZcQ7kNvwEWQTp6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjc2MzE0MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1BZsNp_5D7hQUly_JIIBYjEWDKgJtCB_63UA-IbmasOg&amp;oe=69DC4BDE</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-114915\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-336132\" FBFirstSegmentRange=\"954-483551\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"483552-804608\" FBPrefetchSegmentRange=\"954-483551\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2068615210376762v\" bandwidth=\"1087528\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"5111963\" FBPlaybackResolutionMos=\"0:100,360:93.3,480:91.1,720:87.9,1080:85.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.421,480:99.719,720:99.959,1080:100\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOcOQ4NKMWkJxtK7hALq0Nwa55xlrhvJ2saTZsLuB82rVw6xGDfLlmCHpy_XaTtiASncYxz6T_RBYeOh3ZVpBJOnDVowr36HTC8sFI.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=KaA6szpxM1gQ7kNvwE4EEwB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjEwODc1MjgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af10D_6Xa4tSyAcoAY0xfSYtF-XwSunYKKr4uaGmwSTgug&amp;oe=69DC4502</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-156174\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-462436\" FBFirstSegmentRange=\"954-669969\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"669970-1135720\" FBPrefetchSegmentRange=\"954-669969\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2879984799006088a\" bandwidth=\"40800\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40800\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"192778\" FBPaqMos=\"88.96\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMIxNtnph-4ud53wUoAkp9EjZhLa0cFErTRXRj3RfP6jM7xduPqCUyzjb0cSXnAoiaEOh4Rlzz-oo6ZKMAxa1eXFNjtt-5yana9Uu4.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=Fpoa71T0T9AQ7kNvwEbyOmj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6NDEwMDQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3XNdhDjPiV_dkSZYcZ7Bt3P9AkikmoFijWinfmusIWxg&amp;oe=69DC4671</BaseURL><SegmentBase indexRange=\"837-964\" timescale=\"48000\" FBMinimumPrefetchRange=\"965-1997\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"965-13925\" FBFirstSegmentRange=\"965-25799\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"25800-51320\" FBPrefetchSegmentRange=\"965-25799\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1254269033477905a\" bandwidth=\"69857\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"69857\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"329387\" FBPaqMos=\"89.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMSFpBOQxw-zzV0kZnQ6GFSlr65oVFelvwaYf_mhiZitVveZ9zmd9zzxEqMNGyLGaTGmf0OudIQAKjSmbdYPW8g9qyO3xrf7GHnU-k.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=RkG-ch48nGcQ7kNvwHRIMP6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6NzAwNjIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1NadQTz8REMkqWW5jI3rhq5I0gz52HLFY7wGEr3MOMSA&amp;oe=69DC2835</BaseURL><SegmentBase indexRange=\"838-965\" timescale=\"48000\" FBMinimumPrefetchRange=\"966-2265\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-23581\" FBFirstSegmentRange=\"966-44722\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"44723-85627\" FBPrefetchSegmentRange=\"966-44722\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1476108730564454a\" bandwidth=\"100153\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"100153\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"471809\" FBPaqMos=\"86.81\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMCQeXtcTeNC7bByzIlweiWaYE1mqvJfG1TW6Uc1-dQNrExFO0nUXfAcrJWhZGHgXwoM219Dp5EGleI8YWIJCCulgomDY8fSTGH18Q.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=ZLu5MrjSL1UQ7kNvwFtz_y1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6MTAwMzU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2V8x3MzcVBqU6nEWycwlXTwokFtHQEgNZsmZ25YLqseA&amp;oe=69DC438B</BaseURL><SegmentBase indexRange=\"833-960\" timescale=\"48000\" FBMinimumPrefetchRange=\"961-2206\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-32428\" FBFirstSegmentRange=\"961-62587\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62588-120492\" FBPrefetchSegmentRange=\"961-62587\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1314154813863963a\" bandwidth=\"124724\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"124724\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"587330\" FBPaqMos=\"88.57\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNTk8k6PvvY2YpsxZmcqByN3qqBP0gYpXQh57NEF2m7ks5pXLmbbuz_aQJ4HHejxQx31uXpw5XXinxvcfCNdUajwe61Hu93dIeNRKE.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=Rf3bJxsjGNsQ7kNvwGuYZ2A&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6MTI0OTI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=dskAJegcZpmj0Vy1podVGw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1w9Q8M_ZmVHg4kuTP_iymiic-hRcTiC49H5vcJcboEdA&amp;oe=69DC4819</BaseURL><SegmentBase indexRange=\"833-960\" timescale=\"48000\" FBMinimumPrefetchRange=\"961-2221\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-39830\" FBFirstSegmentRange=\"961-77199\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"77200-150196\" FBPrefetchSegmentRange=\"961-77199\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "number_of_qualities": 6,
            "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
            "sharing_friction_info": {
              "should_have_sharing_friction": false,
              "bloks_app_url": null,
              "sharing_friction_payload": null
            },
            "gen_ai_detection_method": {
              "detection_method": "NONE"
            },
            "explore_demotion_control": null,
            "clips_demotion_control": {
              "title": "Not interested",
              "enable_word_wrapping": true,
              "confirmation_icon": "none",
              "title_style": "normal",
              "confirmation_title": "Post hidden",
              "confirmation_body": "We'll suggest fewer posts like this.",
              "confirmation_title_style": "large_left",
              "undo_style": "top_right",
              "confirmation_style": "bottomsheet",
              "followup_options": [
                {
                  "text": "Don't suggest posts from natgeo",
                  "style": null,
                  "id": "dislike_author",
                  "data": "author_id:787132",
                  "show_icon": true,
                  "demotion_control": {
                    "confirmation_style": "bottomsheet",
                    "confirmation_icon": "eye-off-pano",
                    "confirmation_body": "We won't suggest posts from natgeo.",
                    "undo_style": "inline"
                  },
                  "subtitle": null
                },
                {
                  "text": "Don't suggest posts with certain words",
                  "id": "hide_all_specific_words",
                  "show_icon": true,
                  "data": null,
                  "style": null,
                  "demotion_control": null,
                  "subtitle": null
                }
              ]
            },
            "text_post_app_info": null,
            "user": {
              "strong_id__": "787132",
              "all_media_count": null,
              "allowed_commenter_type": null,
              "coeff_weight": null,
              "fbid_v2": 17841400573960012,
              "feed_post_reshare_disabled": false,
              "id": "787132",
              "is_active": null,
              "is_unpublished": false,
              "liked_clips_count": null,
              "live_invite_only_branding_enabled": null,
              "pk": 787132,
              "pk_id": "787132",
              "reel_auto_archive": null,
              "show_insights_terms": null,
              "text_post_app_take_a_break_setting": null,
              "third_party_downloads_enabled": 2,
              "eligible_for_text_app_activation_badge": false,
              "account_type": 2,
              "account_badges": [],
              "can_boost_post": null,
              "can_see_organic_insights": null,
              "fan_club_info": {
                "autosave_to_exclusive_highlight": null,
                "connected_member_count": null,
                "fan_club_id": null,
                "fan_club_name": null,
                "has_created_ssc": null,
                "has_enough_subscribers_for_ssc": null,
                "is_fan_club_gifting_eligible": null,
                "is_fan_club_referral_eligible": null,
                "is_free_trial_eligible": null,
                "largest_public_bc_id": null,
                "subscriber_count": null,
                "should_show_playlists_in_profile_tab": null,
                "fan_consideration_page_revamp_eligiblity": null
              },
              "full_name": "National Geographic",
              "friendship_status": {
                "following": false,
                "is_bestie": false,
                "is_feed_favorite": false,
                "is_private": false,
                "is_restricted": false,
                "text_post_app_pre_following": null,
                "followed_by": false,
                "is_muting_reel": false
              },
              "has_anonymous_profile_picture": false,
              "has_onboarded_to_text_post_app": null,
              "interop_messaging_user_fbid": null,
              "is_favorite": false,
              "is_private": false,
              "is_ring_creator": false,
              "show_ring_award": false,
              "aigm_account_label_info": null,
              "is_verified": true,
              "is_ai_user": null,
              "ai_agent_owner_username": null,
              "live_broadcast_id": null,
              "live_broadcast_visibility": null,
              "profile_pic_id": "3865702555259028436_787132",
              "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHwaRlUnEQ41KwZTuaQwzxbipmLizdZc4u4BswSpZn7xY6MgvzKq44GXsds_sKvJA0&_nc_ohc=XbeNvhLXv28Q7kNvwGuzNfJ&_nc_gid=dskAJegcZpmj0Vy1podVGw&edm=AL2I2h8BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3cephpO5cYpdbzxafS_wTWLLmLch8DZiGu-38W0PxU4A&oe=69DC51E9&_nc_sid=026283",
              "reachability_status": null,
              "show_account_transparency_details": true,
              "transparency_product_enabled": false,
              "transparency_product": null,
              "transparency_label": null,
              "username": "natgeo",
              "opal_info": null,
              "latest_reel_media": 1775583063,
              "user_activation_info": {
                "activation_type": null,
                "rings_custom_likes_setting_enabled": null
              },
              "text_post_app_privacy": null
            },
            "community_notes_info": {
              "has_viewer_submitted_note": false,
              "note_submission_disabled": false,
              "enable_submission_friction": false,
              "is_eligible_for_request_a_note": true
            },
            "has_high_risk_gen_ai_inform_treatment": false,
            "caption_is_edited": false,
            "code": "DWKyQb2gEF0",
            "device_timestamp": 177414341574,
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
            "is_comments_gif_composer_enabled": false
          }
        }
      ]
    }
  ],
  "has_more": true,
  "reels_max_id": "r:1265c339e63543febe1aca84d0937492",
  "page_index": 11,
  "rank_token": "01e563eb-d54a-4f29-a20f-f4735102c5a0",
  "status": "ok"
}
```

</details>

---

### GET /v3/fbsearch/topsearch

Search top content by keyword. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `next_max_id` | string | No | Next Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v3/fbsearch/topsearch?query=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v3/fbsearch/topsearch",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v3/fbsearch/topsearch?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "clear_client_cache": false,
      "client_hints": {
        "type": "url_hint",
        "media": [
          {
            "resources": [
              {
                "image": {
                  "estimated_scans_sizes": [
                    26510,
                    53021
                  ],
                  "height": 1332,
                  "scans_profile": "e15",
                  "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.82787-15/588242089_18544441921044233_3161580958584083436_n.jpg?stp=dst-jpg_e15_p750x750_tt6&_nc_cat=110&ig_cache_key=Mzc3MzA3Mjc1MTIwMTE1NTU5MDE4NTQ0NDQxOTE4MDQ0MjMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNTR4MTg3Mi5zZHIuQzMifQ%3D%3D&_nc_ohc=FGXE_FV4fn8Q7kNvwEpjJzx&_nc_oc=AdpOdYFkKQ-UbVNCFuwokhcHobl2hPNeo2cYilnYJtUU0EY_-BfFphWUjBQJoS1hX5Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af3Sygeh220azqzLi3qxl02iU3l7lIfKB_RWl70KkLIFng&oe=69DC3631",
                  "width": 750,
                  "is_spatial_image": false
                }
              }
            ],
            "priority": 0
          },
          {
            "resources": [
              {
                "image": {
                  "estimated_scans_sizes": [
                    22552,
                    45105
                  ],
                  "height": 1333,
                  "scans_profile": "e35",
                  "url": "https://scontent-mia5-2.cdninstagram.com/v/t51.82787-15/655918808_18642480373019133_2706709073646407389_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzg1ODExNzA2MjUzODgzODM4ODE4NjQyNDgwMzY3MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=mR20z9GjA6kQ7kNvwFzvy9B&_nc_oc=Adp-cUnypkpwyoOb-mGrDz3PBgGmFAs1fZlNz1rzzUKy60_xmMccQNmBzzEnQ7EK0C0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia5-2.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af0pqakTzLwiaeVIaku94LBtRU357DCk5zZmUV530GgFvA&oe=69DC2102",
                  "width": 750,
                  "is_spatial_image": false
                }
              }
            ],
            "priority": 0
          }
        ]
      },
      "status": "ok"
    },
    {
      "list": [
        {
          "position": 0,
          "user": {
            "strong_id__": "787132",
            "coeff_weight": null,
            "fbid_v2": 17841400573960012,
            "is_active": null,
            "pk": 787132,
            "pk_id": "787132",
            "all_media_count": null,
            "allowed_commenter_type": null,
            "following_tag_count": null,
            "is_verified_search_boosted": false,
            "liked_clips_count": null,
            "reel_auto_archive": null,
            "search_serp_type": 3,
            "text_post_app_take_a_break_setting": null,
            "third_party_downloads_enabled": 2,
            "live_invite_only_branding_enabled": null,
            "id": "787132",
            "full_name": "National Geographic",
            "has_onboarded_to_text_post_app": null,
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=XbeNvhLXv28Q7kNvwGuzNfJ&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0UlZiSyVVpzFyybovLNogc8RzYrtKrsaz2Q4MRgykwGQ&oe=69DC51E9&_nc_sid=c24a68",
            "username": "natgeo",
            "account_badges": [],
            "ai_agent_owner_username": null,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_private": false,
              "is_restricted": false,
              "text_post_app_pre_following": null,
              "incoming_request": false,
              "outgoing_request": false
            },
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": null,
            "is_ai_user": null,
            "is_ring_creator": false,
            "latest_reel_media": 1775583063,
            "reachability_status": null,
            "reel_media_seen_timestamp": null,
            "should_show_category": true,
            "show_ig_app_switcher_badge": true,
            "show_ring_award": false,
            "show_text_post_app_badge": true,
            "unseen_count": 0,
            "aigm_account_label_info": null,
            "live_broadcast_id": null,
            "live_broadcast_visibility": null,
            "social_context": "274M followers",
            "search_social_context": "274M followers",
            "search_social_context_snippet_type": "typeahead_follow_count",
            "search_social_context_facepiles": null
          }
        },
        {
          "position": 1,
          "user": {
            "strong_id__": "23947096",
            "coeff_weight": null,
            "fbid_v2": 17841400332880374,
            "is_active": null,
            "pk": 23947096,
            "pk_id": "23947096",
            "all_media_count": null,
            "allowed_commenter_type": null,
            "following_tag_count": null,
            "is_verified_search_boosted": false,
            "liked_clips_count": null,
            "reel_auto_archive": null,
            "search_serp_type": 3,
            "text_post_app_take_a_break_setting": null,
            "third_party_downloads_enabled": 2,
            "live_invite_only_branding_enabled": null,
            "id": "23947096",
            "full_name": "National Geographic Travel",
            "has_onboarded_to_text_post_app": null,
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702501739707616_23947096",
            "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=t-DCVZxwtX4Q7kNvwFnnkBq&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af3H0eoYMRHZEivnPwZCjN5aOtz-tFjpPs-JvpYIbcMH5g&oe=69DC2F06&_nc_sid=c24a68",
            "username": "natgeotravel",
            "account_badges": [],
            "ai_agent_owner_username": null,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_private": false,
              "is_restricted": false,
              "text_post_app_pre_following": null,
              "incoming_request": false,
              "outgoing_request": false
            },
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": null,
            "is_ai_user": null,
            "is_ring_creator": false,
            "latest_reel_media": 1775582271,
            "reachability_status": null,
            "reel_media_seen_timestamp": null,
            "should_show_category": true,
            "show_ig_app_switcher_badge": null,
            "show_ring_award": false,
            "show_text_post_app_badge": false,
            "unseen_count": 0,
            "aigm_account_label_info": null,
            "live_broadcast_id": null,
            "live_broadcast_visibility": null,
            "social_context": "45.5M followers",
            "search_social_context": "45.5M followers",
            "search_social_context_snippet_type": "typeahead_follow_count",
            "search_social_context_facepiles": null
          }
        }
      ],
      "rank_token": "a9ffb628-93d6-40dc-bcff-14d57181f6a5",
      "clear_client_cache": false,
      "more_results_header": "Posts",
      "entity_results_header": "Accounts",
      "media_grid": {
        "refinements": {},
        "sections": [
          {
            "layout_type": "media_grid",
            "feed_type": "media",
            "explore_item_info": {
              "num_columns": 3,
              "total_num_columns": 3,
              "autoplay": true
            },
            "layout_content": {
              "medias": [
                {
                  "media": {
                    "strong_id__": "3773072751201155590_47276232",
                    "fbid": 18068167955104780,
                    "device_timestamp": 1764005343564115,
                    "carousel_last_edited_at": null,
                    "dynamic_ad_carousel_card_starting_index": null,
                    "is_sidecar_child": null,
                    "sticker_translations_enabled": null,
                    "segmented_video_group_id": null,
                    "pk": 3773072751201155590,
                    "id": "3773072751201155590_47276232",
                    "is_reel_media": null,
                    "visibility": null,
                    "has_delayed_metadata": true,
                    "code": "DRcpa03DPoG",
                    "play_count": 4821184,
                    "video_versions": [
                      {
                        "bandwidth": 3104086,
                        "height": 1280,
                        "id": "1495177061595317v",
                        "type": 101,
                        "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOj0t4bWY6qEiIQYY2fjPM0ZP-hypYUCa9PnQqN-j1OLfEnpiKG87UN0FksO_HVgNsv6ngtFZnGIkMoDl9OWgCp8WUH5VnqHBvrlPQ.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=Jwfi_WKiEdwQ7kNvwH5BXbG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTIzMTYwNDA4NTQ3MzYwOCwiYXNzZXRfYWdlX2RheXMiOjEzNCwidmlfdXNlY2FzZV9pZCI6MTA4MjcsImR1cmF0aW9uX3MiOjQzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=5688269e4af95591&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GNzRCRDkyNDRFM0E1NTVBMEU3NDgzOTZEREI0N0VBQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQVhQNFNJYWJFSTFSTzBDQUR4cnpMUWVaSGg1YnN0VEFRQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkIWmwOWIsAQVAigCQzMsF0BFqp--dsi0GBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2WWqQEA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2mItZKwEUYTUHf3NciVb59PxdK853goZwNBRCQ0AaXFA&oe=69D82F26",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      },
                      {
                        "bandwidth": 3104086,
                        "height": 1280,
                        "id": "1495177061595317v",
                        "type": 102,
                        "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOj0t4bWY6qEiIQYY2fjPM0ZP-hypYUCa9PnQqN-j1OLfEnpiKG87UN0FksO_HVgNsv6ngtFZnGIkMoDl9OWgCp8WUH5VnqHBvrlPQ.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=Jwfi_WKiEdwQ7kNvwH5BXbG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTIzMTYwNDA4NTQ3MzYwOCwiYXNzZXRfYWdlX2RheXMiOjEzNCwidmlfdXNlY2FzZV9pZCI6MTA4MjcsImR1cmF0aW9uX3MiOjQzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=5688269e4af95591&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GNzRCRDkyNDRFM0E1NTVBMEU3NDgzOTZEREI0N0VBQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQVhQNFNJYWJFSTFSTzBDQUR4cnpMUWVaSGg1YnN0VEFRQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmkIWmwOWIsAQVAigCQzMsF0BFqp--dsi0GBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2WWqQEA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2mItZKwEUYTUHf3NciVb59PxdK853goZwNBRCQ0AaXFA&oe=69D82F26",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      }
                    ],
                    "video_subtitles_confidence": null,
                    "video_subtitles_locale": null,
                    "is_dash_eligible": 1,
                    "video_duration": 43.349998474121094,
                    "has_audio": true,
                    "carousel_media_count": null,
                    "carousel_media_pending_post_count": null,
                    "can_modify_carousel": null,
                    "carousel_media_ids": null,
                    "video_subtitles_enabled": null,
                    "video_subtitles_uri": null,
                    "video_subtitles_translations_enabled": null,
                    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT43.350204S\" FBManifestTimestamp=\"1775657997\" FBManifestIdentifier=\"FpqQs50NGA9yMmF2MS1yMWdlbjJ2cDkZhoLZiJCV8oQDlqf167KQmQSA9fiU7qbjBIC1sr2Nn/cEiMSx0raGsQW6xriOgdK6Be7Rv4To8PIGpruSlYjnog8iGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYDmxhdGFtX21vZGVyYXRlABaMAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT43.350204S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:83.1\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1515237436436740v\" bandwidth=\"349100\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"1890961\" FBPlaybackResolutionMos=\"0:100,360:37.7,480:35.5,720:33.8,1080:34.3,1440:35.2,2160:37.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:67.7,480:58.8,720:46.2,1080:32.9,1440:24.3,2160:13.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNsa1WkwGHwaYQTLAtbv4b7MByH_feHeZ9G5aWV_SkjhADjwqc_35yxO8GlgrIDe5Iix3U9KNj8CFfScqowQG8hAbL8_6NA5t9f2SE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=IE16Rn1r0wMQ7kNvwGpjSxc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjM0OTEwMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1J5PIue15HbyFg8Jl6iPfF2hYLt0EqyvxJeoKouyqX2w&amp;oe=69DC329E</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-16019\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-64496\" FBFirstSegmentRange=\"966-102836\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"102837-291096\" FBPrefetchSegmentRange=\"966-102836\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1344270830083392v\" bandwidth=\"976753\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"5290748\" FBPlaybackResolutionMos=\"0:100,360:64.1,480:59.3,720:53.4,1080:51.3,1440:51.2,2160:51.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.6,480:85.9,720:78.3,1080:68.3,1440:59.9,2160:47.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMRDWpnhBovNEPuhqsJ2xRiT0FD4IN4dP2g3wT8RBSYninYDmFfD7wHRz4as7KOBwlvBlmKu3GheOi6Vt0-t8WM6-I9IXgiJMgqreI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=dke0F2YqSwsQ7kNvwHirvUs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjk3Njc1MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0xcK9hXqDEmcimCbQ1wQ5AbX7sadcn6zErnZUCMIklSg&amp;oe=69DC1B2B</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-32240\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-258610\" FBFirstSegmentRange=\"966-432886\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"432887-1000442\" FBPrefetchSegmentRange=\"966-432886\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1536327131009437v\" bandwidth=\"1393255\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"7546800\" FBPlaybackResolutionMos=\"0:100,360:72.1,480:67.3,720:60.2,1080:57,1440:56.4,2160:56.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.5,480:91.1,720:85.5,1080:77.3,1440:69.8,2160:58.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQM7gWOMxlG8Zo3cs6bLqkLPmfRyx7ywN6PEzVRyWcDvbCi6wNjCo4lL0aLvbNANxdcfBCmt9z00f-OAKW4BmzhXL0huV0ngTimtofQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=WRCizycxgSgQ7kNvwGll-3c&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjEzOTMyNTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2HRSm-51Ak1lddAJ54SCWBR-qOdxun8spJhE9WbPKIpQ&amp;oe=69DC3552</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-40053\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-410190\" FBFirstSegmentRange=\"966-688189\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"688190-1525563\" FBPrefetchSegmentRange=\"966-688189\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"855182363661889v\" bandwidth=\"1903534\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"10310811\" FBPlaybackResolutionMos=\"0:100,360:77.5,480:73.1,720:65.8,1080:61.7,1440:60.7,2160:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.4,480:93.6,720:89.5,1080:82.4,1440:75.7,2160:65\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOVkH6CDtowcCB9haURfdct7bLVG-n2JL8QSZ14vC8l-CGfhdunO2Qr4oDVY_9iuXCAQgEZzrAH2W6ov_ziAWlKn1WIKu_CIG8X-0I.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=f2vaIaCLHTIQ7kNvwEmVhDF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjE5MDM1MzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1voGzYa3kltBCYz7YbFXj1Jg7ml41M9pYLjtlXoOWEiQ&amp;oe=69DC3FCF</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-46389\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-571504\" FBFirstSegmentRange=\"966-969927\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"969928-2158207\" FBPrefetchSegmentRange=\"966-969927\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1181157190183371v\" bandwidth=\"2456971\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"13308597\" FBPlaybackResolutionMos=\"0:100,360:80.9,480:76.2,720:69.5,1080:65.1,1440:63.9,2160:62.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.5,480:95.3,720:92,1080:85.8,1440:79.9,2160:69.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPr-GxM0r1x8Er9sovANffZH5SuP30_4f93S6v6bbK05eoQo2BXND0wnddznZBRTlCllQunAy7irEsZvEor1N2AJ4MsfiXpsMdT00c.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=7wfAY__1GeMQ7kNvwHx9w2P&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjI0NTY5NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0xg8EJhBmNgXIO64S6Z4eI9F1ATCTTN1uIR1FK4Zp27g&amp;oe=69DC4E56</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-51033\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-728865\" FBFirstSegmentRange=\"966-1249505\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1249506-2844600\" FBPrefetchSegmentRange=\"966-1249505\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1941476620104823v\" bandwidth=\"3236225\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"17529554\" FBPlaybackResolutionMos=\"0:100,360:85.1,480:80.7,720:73.8,1080:69,1440:67.7,2160:66.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.2,480:96.4,720:93.9,1080:88.5,1440:83.3,2160:74.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMZocCbzqoSGKwGEXI-j6dx9dCC7b8WLI5dsKRKeDg1dENAUVPt1Ffs9IcckXciyXQW6FyeVlGLlBcclGCtFX5gwni-t1fd-y33-jw.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=1-KoOwi_6bEQ7kNvwEXE-hr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjMyMzYyMjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3lFrrIqDgxMMFebrqZQgvIUzecU--EX6tbdZVi52mbOQ&amp;oe=69DC2CDB</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-56201\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-904989\" FBFirstSegmentRange=\"966-1578295\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1578296-3822187\" FBPrefetchSegmentRange=\"966-1578295\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4298662063787731v\" bandwidth=\"4682144\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"25361616\" FBPlaybackResolutionMos=\"0:100,360:91.4,480:88.7,720:83.9,1080:79.2,1440:77.4,2160:76.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.35,480:98.09,720:97.3,1080:94.9,1440:92.1,2160:86.7\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO0v_puE3WwSPBYMJ5dWM2cER6q0XUu4ks7xkuBnEjtgSA-cCPJS0R4UXjKd7o9uc7iI1qOOQZdSlmf6IwHa-tDtnBgAIkfXIKJuu4.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=HoiB_cqebeYQ7kNvwEF1dXo&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjQ2ODIxNDQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3a38fjw4XD2UY91uW0jymQZzsm2vpavvXS7QX_abyUBw&amp;oe=69DC27B8</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"15360\" FBMinimumPrefetchRange=\"966-83585\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-1319664\" FBFirstSegmentRange=\"966-2334099\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"2334100-5576869\" FBPrefetchSegmentRange=\"966-2334099\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1388118059404608a\" bandwidth=\"74757\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74757\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"406206\" FBPaqMos=\"86.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t16/f2/m69/AQNNB7DglnfOPDJxu7IlZxgUHa1pqKy7W-QDx4zSqU-_2ZZUSTSJjyUtxesGpE9vSZciqgDopVme84YBb51ooz84.mp4?strext=1&amp;_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=yA3Q737n7AEQ7kNvwHaVAaL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMjMxNjA0MDg1NDczNjA4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNywiZHVyYXRpb25fcyI6NDMsImJpdHJhdGUiOjc0OTYyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1MyP2pHjJhL9B0KPYpJPSS8qTKpBDHxII38uPpOPH5aw&amp;oe=69DC2D5C</BaseURL><SegmentBase indexRange=\"824-1119\" timescale=\"44100\" FBMinimumPrefetchRange=\"1120-1463\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1120-31781\" FBFirstSegmentRange=\"1120-27306\" FBFirstSegmentDuration=\"2021\" FBSecondSegmentRange=\"27307-48972\" FBPrefetchSegmentRange=\"1120-48972\" FBPrefetchSegmentDuration=\"4017\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "number_of_qualities": 7,
                    "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                    "carousel_media": null,
                    "open_carousel_submission_state": null,
                    "open_to_public_submission_description_text": null,
                    "total_carousel_media_count": null,
                    "more_carousel_media_available": null,
                    "tallest_media_aspect_ratio": null,
                    "video_sticker_locales": [],
                    "translated_video_subtitles": null,
                    "autodub_status": null,
                    "basel_encoding_timeout": 146,
                    "video_imf_spec": null,
                    "taken_at": 1764005641,
                    "media_type": 2,
                    "view_count": null,
                    "attribution": null,
                    "audio": null,
                    "is_seen": null,
                    "user": {
                      "strong_id__": "47276232",
                      "all_media_count": null,
                      "allowed_commenter_type": null,
                      "coeff_weight": null,
                      "fbid_v2": 17841401326960738,
                      "feed_post_reshare_disabled": false,
                      "id": "47276232",
                      "is_active": null,
                      "is_unpublished": false,
                      "liked_clips_count": null,
                      "live_invite_only_branding_enabled": null,
                      "pk": 47276232,
                      "pk_id": "47276232",
                      "reel_auto_archive": null,
                      "show_insights_terms": null,
                      "text_post_app_take_a_break_setting": null,
                      "third_party_downloads_enabled": 1,
                      "eligible_for_text_app_activation_badge": false,
                      "account_type": 3,
                      "account_badges": [],
                      "can_boost_post": null,
                      "can_see_organic_insights": null,
                      "fan_club_info": {
                        "autosave_to_exclusive_highlight": null,
                        "connected_member_count": null,
                        "fan_club_id": null,
                        "fan_club_name": null,
                        "has_created_ssc": null,
                        "has_enough_subscribers_for_ssc": null,
                        "is_fan_club_gifting_eligible": null,
                        "is_fan_club_referral_eligible": null,
                        "is_free_trial_eligible": null,
                        "largest_public_bc_id": null,
                        "subscriber_count": null,
                        "should_show_playlists_in_profile_tab": null,
                        "fan_consideration_page_revamp_eligiblity": null
                      },
                      "full_name": "Kristina Makeeva↟Kotleta↟Timon",
                      "friendship_status": {
                        "following": false,
                        "is_bestie": false,
                        "is_feed_favorite": false,
                        "is_private": false,
                        "is_restricted": false,
                        "text_post_app_pre_following": null,
                        "followed_by": false,
                        "is_muting_reel": false
                      },
                      "has_anonymous_profile_picture": false,
                      "has_onboarded_to_text_post_app": null,
                      "interop_messaging_user_fbid": null,
                      "is_favorite": false,
                      "is_private": false,
                      "is_ring_creator": false,
                      "show_ring_award": false,
                      "aigm_account_label_info": null,
                      "is_verified": true,
                      "is_ai_user": null,
                      "ai_agent_owner_username": null,
                      "live_broadcast_id": null,
                      "live_broadcast_visibility": null,
                      "profile_pic_id": null,
                      "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.2885-19/11910054_1626257790981501_575133001_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=dfhJaS_x2qUQ7kNvwFjC5sN&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&ig_cache_key=GKa7tQB91fGlEscFAEnVRyIAAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af0ffiQMdf0T_ZJaICsHSDsz-SjbjaeLxCCoL_xPtE68mQ&oe=69DC3C02&_nc_sid=c24a68",
                      "reachability_status": null,
                      "show_account_transparency_details": true,
                      "transparency_product_enabled": false,
                      "transparency_product": null,
                      "transparency_label": null,
                      "username": "hobopeeba",
                      "opal_info": null,
                      "latest_reel_media": null,
                      "user_activation_info": {
                        "activation_type": null,
                        "rings_custom_likes_setting_enabled": null
                      },
                      "text_post_app_privacy": null
                    },
                    "image_versions2": {
                      "additional_candidates": {
                        "first_frame": {
                          "estimated_scans_sizes": [
                            5121,
                            10242
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/587895083_1582451659437904_2371604589830659666_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=5zTeWC8-UaoQ7kNvwEobXcG&_nc_oc=AdqM7NLU_r04kDiQvFrqU_792PT7XXy3dIvzqDH19t4BU6VsU1rxw6-scDhju6dwlas&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af0PwuN79xk7Nb7wTR0Ab4vqgO87uHe3UyZ8A79S9N0N2g&oe=69DC410B",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "igtv_first_frame": {
                          "estimated_scans_sizes": [
                            5121,
                            10242
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/587895083_1582451659437904_2371604589830659666_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=5zTeWC8-UaoQ7kNvwEobXcG&_nc_oc=AdqM7NLU_r04kDiQvFrqU_792PT7XXy3dIvzqDH19t4BU6VsU1rxw6-scDhju6dwlas&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af0PwuN79xk7Nb7wTR0Ab4vqgO87uHe3UyZ8A79S9N0N2g&oe=69DC410B",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "smart_frame": null
                      },
                      "candidates": [
                        {
                          "estimated_scans_sizes": [
                            26510,
                            53021
                          ],
                          "height": 1332,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.82787-15/588242089_18544441921044233_3161580958584083436_n.jpg?stp=dst-jpg_e15_p750x750_tt6&_nc_cat=110&ig_cache_key=Mzc3MzA3Mjc1MTIwMTE1NTU5MDE4NTQ0NDQxOTE4MDQ0MjMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNTR4MTg3Mi5zZHIuQzMifQ%3D%3D&_nc_ohc=FGXE_FV4fn8Q7kNvwEpjJzx&_nc_oc=AdpOdYFkKQ-UbVNCFuwokhcHobl2hPNeo2cYilnYJtUU0EY_-BfFphWUjBQJoS1hX5Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af3Sygeh220azqzLi3qxl02iU3l7lIfKB_RWl70KkLIFng&oe=69DC3631",
                          "width": 750,
                          "is_spatial_image": false
                        }
                      ],
                      "scrubber_spritesheet_info_candidates": {
                        "default": {
                          "file_size_kb": 482,
                          "max_thumbnails_per_sprite": 105,
                          "rendered_width": 96,
                          "sprite_height": 1232,
                          "sprite_urls": [
                            "https://scontent-mia5-1.cdninstagram.com/v/t51.71878-15/586914880_1796498024386526_1689958848606284189_n.jpg?_nc_ht=scontent-mia5-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=IX5fbWWvZmMQ7kNvwHTRkDt&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&oh=00_Af25RvstZsVhtsFVGS63Xw8ijo02XED-ovD2ufFfliIIQg&oe=69DC4E87&_nc_sid=c24a68"
                          ],
                          "sprite_width": 1500,
                          "thumbnail_duration": 0.41269523809523806,
                          "thumbnail_height": 176,
                          "thumbnail_width": 100,
                          "thumbnails_per_row": 15,
                          "total_thumbnail_num_per_sprite": 105,
                          "video_length": 43.333
                        }
                      }
                    },
                    "original_width": 1080,
                    "original_height": 1920,
                    "product_type": "clips",
                    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNzYzODIyNzMzZWM4NGM0NzlkOWUyMzQzOTdjODYwOTgzNzczMDcyNzUxMjAxMTU1NTkwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1Nzk5NjkzNnwzNzczMDcyNzUxMjAxMTU1NTkwfDM1Mzk0NDM1MDEzfDM1NTA4NmM3YjM1NzQwZDAwZGM4ZmZhYjk1MDRlYjk2ZjU4MWIxY2E0NjA3ZWQ3OGVhOGQzZjEwZTg3YjVmOGYifSwic2lnbmF0dXJlIjoiIn0="
                  }
                },
                {
                  "media": {
                    "strong_id__": "3858117062538838388_787132",
                    "fbid": 18143103847436632,
                    "device_timestamp": 177414341574,
                    "carousel_last_edited_at": null,
                    "dynamic_ad_carousel_card_starting_index": null,
                    "is_sidecar_child": null,
                    "sticker_translations_enabled": null,
                    "segmented_video_group_id": null,
                    "pk": 3858117062538838388,
                    "id": "3858117062538838388_787132",
                    "is_reel_media": null,
                    "visibility": null,
                    "has_delayed_metadata": true,
                    "code": "DWKyQb2gEF0",
                    "play_count": 2670433,
                    "video_versions": [
                      {
                        "bandwidth": 591389,
                        "height": 1280,
                        "id": "1165530622219418v",
                        "type": 101,
                        "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPwVfdlglvtOj812P15FmBDCW7nx326yjhRtQLrhVJ1CdRXu65XvcOSyEpa_0AKKjMIsHgB4kf2WUF0NEcJ62zoMyYWnU82jvHWjhk.mp4?_nc_cat=107&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=pQISOkPrSb8Q7kNvwHc8Ph5&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTE1NTIwNTIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxNywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=ee5d5b009a3aa7e0&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83MDQzOUQ4NTJCNzhDNUM4NEFERTVDNjBCRjdGNDI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0EzNDVCQzYxOTAxREY3NzIyN0E5Q0RGMUJEMDUwNUIwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWlN2z7bXjPxUCKAJDMywXQELNT987ZFoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2YSvC63uIRg_pynO-cvkLP1EOK2fKMGLCPiZ4621mcJQ&oe=69D840D4",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      },
                      {
                        "bandwidth": 591389,
                        "height": 1280,
                        "id": "1165530622219418v",
                        "type": 102,
                        "url": "https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPwVfdlglvtOj812P15FmBDCW7nx326yjhRtQLrhVJ1CdRXu65XvcOSyEpa_0AKKjMIsHgB4kf2WUF0NEcJ62zoMyYWnU82jvHWjhk.mp4?_nc_cat=107&_nc_sid=5e9851&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_ohc=pQISOkPrSb8Q7kNvwHc8Ph5&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTE1NTIwNTIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxNywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=ee5d5b009a3aa7e0&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83MDQzOUQ4NTJCNzhDNUM4NEFERTVDNjBCRjdGNDI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0EzNDVCQzYxOTAxREY3NzIyN0E5Q0RGMUJEMDUwNUIwX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWlN2z7bXjPxUCKAJDMywXQELNT987ZFoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2YSvC63uIRg_pynO-cvkLP1EOK2fKMGLCPiZ4621mcJQ&oe=69D840D4",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      }
                    ],
                    "video_subtitles_confidence": null,
                    "video_subtitles_locale": null,
                    "is_dash_eligible": 1,
                    "video_duration": 37.61000061035156,
                    "has_audio": true,
                    "carousel_media_count": null,
                    "carousel_media_pending_post_count": null,
                    "can_modify_carousel": null,
                    "carousel_media_ids": null,
                    "video_subtitles_enabled": null,
                    "video_subtitles_uri": null,
                    "video_subtitles_translations_enabled": null,
                    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT37.610668S\" FBManifestTimestamp=\"1775657997\" FBManifestIdentifier=\"FpqQs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZpszI/u+ijKkDotyLw4iwugS24OGt8M3VBKCdqurpn9cE5tOwqvqmmAXM/ceI66CfBfT41Kyg2awH8OCRhNiD0geQ9rnultWdCriHhfGom7RdIhgmZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlMTIzNF9pYnJfYXVkaW8iLBkYDmxhdGFtX21vZGVyYXRlABYiFAASFAIA\"><Period id=\"0\" duration=\"PT37.610668S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:77.6\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"934795722871334v\" bandwidth=\"158286\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"744031\" FBPlaybackResolutionMos=\"0:100,360:83.1,480:79.1,720:74.8,1080:71.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.5,480:95.6,720:92.7,1080:86.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/400\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOwALZbK4Z2-hWiF-CSexLDqF79HRcqqSkXR4siF-drzmUN0CnAMoQ2o6Y6RXTtF0Swp2jrWXG88bITSyCP2VpZZWCB_axna3z8BQU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=AeBLuI-fB6AQ7kNvwFOl23B&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjE1ODI4NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2hi47LTSouU9xCoC534oxhyPe6z7vdgGmL3tTNxpLWkg&amp;oe=69DC4653</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-39540\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-75860\" FBFirstSegmentRange=\"954-101121\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"101122-166750\" FBPrefetchSegmentRange=\"954-101121\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"26291991387087324v\" bandwidth=\"259930\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"1221812\" FBPlaybackResolutionMos=\"0:100,360:87.9,480:84.9,720:81.2,1080:76.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.8,480:97.6,720:97.9,1080:94.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMHE68zYgqvRzeor8Wxi_ybur2uTo7Ar6hsLsHTzhfETCzIprQB37x-rOb7Wtb6cJ1OtbugVCpittc7NCtcV_w_RJI4-HQgn6Jjd7g.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=i2MosldJOpwQ7kNvwGMON13&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjI1OTkzMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2spRm0CzQd2VIZ6OlOeMouKIZcrAPBjk1kl1YzR8vXuA&amp;oe=69DC4A24</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-60671\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-125281\" FBFirstSegmentRange=\"954-167240\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"167241-273912\" FBPrefetchSegmentRange=\"954-167240\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1460820695717107v\" bandwidth=\"362057\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"1701862\" FBPlaybackResolutionMos=\"0:100,360:90,480:87.2,720:83.8,1080:78.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.4,480:98.4,720:98.93,1080:95.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNBGstUjgCkHXBEz3O4C_zxljZyU9AkdDU85vfiaCCEK-gFiuQ88YQ-0DSh7BJt5kN4W5XP3MEOXPnsIqL7Fv_nHeuR3mK8N7AYcVI.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=lwZ2op-beLEQ7kNvwEAtJTb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjM2MjA1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3nv0B3tuv0I0-azUS6twRkz_4aw1IdnWK6nFZ0l9mlrg&amp;oe=69DC409B</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-77385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-173166\" FBFirstSegmentRange=\"954-233283\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"233284-381968\" FBPrefetchSegmentRange=\"954-233283\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2150708099037240v\" bandwidth=\"506743\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"2381963\" FBPlaybackResolutionMos=\"0:100,360:91.5,480:88.8,720:85.7,1080:80.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.84,480:98.94,720:99.537,1080:96.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPiWL8aXblpTq38UZsTU1eitafqyty7JpAL9sXa_U2JrS6ILxtki5SmHBHFPThMc4-PkxUA9JcYcp5wLYtaFfPsNJgylPPImv1hs8k.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=_270KmJ235AQ7kNvwFUUVuL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjUwNjc0MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1BQ-lpmQGe0fIz28GRRJ1xLg1OJxpfi__L1-AhGje4Aw&amp;oe=69DC3E26</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-95531\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-235238\" FBFirstSegmentRange=\"954-323945\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"323946-531369\" FBPrefetchSegmentRange=\"954-323945\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1317761710376784v\" bandwidth=\"763143\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"3587180\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:90.1,720:87,1080:81.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.226,480:99.418,720:99.854,1080:97.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOcTbLjDfQaONR5BHPWpFlF5aAUbnBsEwfC0fkA8JbyLBQBNobDngwrCf_iC0SNsHyO9nXWsd9nCNkt3YKf3dlQbseHq8M5Q5CtKjQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=i8UFZaAx8ZcQ7kNvwEWQTp6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjc2MzE0MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1l4qEiAPPSgs0GTqMkIyrX1ak_IbX30WM-FTMeB-jG9w&amp;oe=69DC4BDE</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-114915\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-336132\" FBFirstSegmentRange=\"954-483551\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"483552-804608\" FBPrefetchSegmentRange=\"954-483551\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2068615210376762v\" bandwidth=\"1087528\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"5111963\" FBPlaybackResolutionMos=\"0:100,360:93.3,480:91.1,720:87.9,1080:85.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.421,480:99.719,720:99.959,1080:100\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/400\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOcOQ4NKMWkJxtK7hALq0Nwa55xlrhvJ2saTZsLuB82rVw6xGDfLlmCHpy_XaTtiASncYxz6T_RBYeOh3ZVpBJOnDVowr36HTC8sFI.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=KaA6szpxM1gQ7kNvwE4EEwB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1MTU1MjA1MjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjE3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzcsImJpdHJhdGUiOjEwODc1MjgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0L7hLmoLsXusnXahsFWdjvtruqFk_VIY5p3ywYUzSi2w&amp;oe=69DC4502</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-156174\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-462436\" FBFirstSegmentRange=\"954-669969\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"669970-1135720\" FBPrefetchSegmentRange=\"954-669969\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2879984799006088a\" bandwidth=\"40800\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40800\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"192778\" FBPaqMos=\"88.96\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMIxNtnph-4ud53wUoAkp9EjZhLa0cFErTRXRj3RfP6jM7xduPqCUyzjb0cSXnAoiaEOh4Rlzz-oo6ZKMAxa1eXFNjtt-5yana9Uu4.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=Fpoa71T0T9AQ7kNvwEbyOmj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6NDEwMDQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ATvI4Jp3Z95YZrs9BAYAjgFBRA3BiRbHtIBpufP37Kg&amp;oe=69DC4671</BaseURL><SegmentBase indexRange=\"837-964\" timescale=\"48000\" FBMinimumPrefetchRange=\"965-1997\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"965-13925\" FBFirstSegmentRange=\"965-25799\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"25800-51320\" FBPrefetchSegmentRange=\"965-25799\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1254269033477905a\" bandwidth=\"69857\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"69857\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"329387\" FBPaqMos=\"89.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMSFpBOQxw-zzV0kZnQ6GFSlr65oVFelvwaYf_mhiZitVveZ9zmd9zzxEqMNGyLGaTGmf0OudIQAKjSmbdYPW8g9qyO3xrf7GHnU-k.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=RkG-ch48nGcQ7kNvwHRIMP6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6NzAwNjIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3B63qcIBjwcbhAR_PRBPA27G7_P8sB70yHsSCsNdGd5A&amp;oe=69DC2835</BaseURL><SegmentBase indexRange=\"838-965\" timescale=\"48000\" FBMinimumPrefetchRange=\"966-2265\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-23581\" FBFirstSegmentRange=\"966-44722\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"44723-85627\" FBPrefetchSegmentRange=\"966-44722\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1476108730564454a\" bandwidth=\"100153\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"100153\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"471809\" FBPaqMos=\"86.81\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMCQeXtcTeNC7bByzIlweiWaYE1mqvJfG1TW6Uc1-dQNrExFO0nUXfAcrJWhZGHgXwoM219Dp5EGleI8YWIJCCulgomDY8fSTGH18Q.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=ZLu5MrjSL1UQ7kNvwFtz_y1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6MTAwMzU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af18tx3FXE9TeU-qyQfGuCxeA5YGYKdTxKuE3LTW0B4qzQ&amp;oe=69DC438B</BaseURL><SegmentBase indexRange=\"833-960\" timescale=\"48000\" FBMinimumPrefetchRange=\"961-2206\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-32428\" FBFirstSegmentRange=\"961-62587\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62588-120492\" FBPrefetchSegmentRange=\"961-62587\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1314154813863963a\" bandwidth=\"124724\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"124724\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"587330\" FBPaqMos=\"88.57\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNTk8k6PvvY2YpsxZmcqByN3qqBP0gYpXQh57NEF2m7ks5pXLmbbuz_aQJ4HHejxQx31uXpw5XXinxvcfCNdUajwe61Hu93dIeNRKE.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=Rf3bJxsjGNsQ7kNvwGuYZ2A&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTUxNTUyMDUyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MTcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozNywiYml0cmF0ZSI6MTI0OTI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2u7KZer6hEB9F1MJXR3K5DqmnIsaDt6_60Lb5yG4t1jA&amp;oe=69DC4819</BaseURL><SegmentBase indexRange=\"833-960\" timescale=\"48000\" FBMinimumPrefetchRange=\"961-2221\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-39830\" FBFirstSegmentRange=\"961-77199\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"77200-150196\" FBPrefetchSegmentRange=\"961-77199\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "number_of_qualities": 6,
                    "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                    "carousel_media": null,
                    "open_carousel_submission_state": null,
                    "open_to_public_submission_description_text": null,
                    "total_carousel_media_count": null,
                    "more_carousel_media_available": null,
                    "tallest_media_aspect_ratio": null,
                    "video_sticker_locales": [],
                    "translated_video_subtitles": null,
                    "autodub_status": null,
                    "basel_encoding_timeout": null,
                    "video_imf_spec": null,
                    "taken_at": 1774198805,
                    "media_type": 2,
                    "view_count": null,
                    "attribution": null,
                    "audio": null,
                    "is_seen": null,
                    "user": {
                      "strong_id__": "787132",
                      "all_media_count": null,
                      "allowed_commenter_type": null,
                      "coeff_weight": null,
                      "fbid_v2": 17841400573960012,
                      "feed_post_reshare_disabled": false,
                      "id": "787132",
                      "is_active": null,
                      "is_unpublished": false,
                      "liked_clips_count": null,
                      "live_invite_only_branding_enabled": null,
                      "pk": 787132,
                      "pk_id": "787132",
                      "reel_auto_archive": null,
                      "show_insights_terms": null,
                      "text_post_app_take_a_break_setting": null,
                      "third_party_downloads_enabled": 2,
                      "eligible_for_text_app_activation_badge": false,
                      "account_type": 2,
                      "account_badges": [],
                      "can_boost_post": null,
                      "can_see_organic_insights": null,
                      "fan_club_info": {
                        "autosave_to_exclusive_highlight": null,
                        "connected_member_count": null,
                        "fan_club_id": null,
                        "fan_club_name": null,
                        "has_created_ssc": null,
                        "has_enough_subscribers_for_ssc": null,
                        "is_fan_club_gifting_eligible": null,
                        "is_fan_club_referral_eligible": null,
                        "is_free_trial_eligible": null,
                        "largest_public_bc_id": null,
                        "subscriber_count": null,
                        "should_show_playlists_in_profile_tab": null,
                        "fan_consideration_page_revamp_eligiblity": null
                      },
                      "full_name": "National Geographic",
                      "friendship_status": {
                        "following": false,
                        "is_bestie": false,
                        "is_feed_favorite": false,
                        "is_private": false,
                        "is_restricted": false,
                        "text_post_app_pre_following": null,
                        "followed_by": false,
                        "is_muting_reel": false
                      },
                      "has_anonymous_profile_picture": false,
                      "has_onboarded_to_text_post_app": null,
                      "interop_messaging_user_fbid": null,
                      "is_favorite": false,
                      "is_private": false,
                      "is_ring_creator": false,
                      "show_ring_award": false,
                      "aigm_account_label_info": null,
                      "is_verified": true,
                      "is_ai_user": null,
                      "ai_agent_owner_username": null,
                      "live_broadcast_id": null,
                      "live_broadcast_visibility": null,
                      "profile_pic_id": "3865702555259028436_787132",
                      "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=XbeNvhLXv28Q7kNvwGuzNfJ&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0UlZiSyVVpzFyybovLNogc8RzYrtKrsaz2Q4MRgykwGQ&oe=69DC51E9&_nc_sid=c24a68",
                      "reachability_status": null,
                      "show_account_transparency_details": true,
                      "transparency_product_enabled": false,
                      "transparency_product": null,
                      "transparency_label": null,
                      "username": "natgeo",
                      "opal_info": null,
                      "latest_reel_media": null,
                      "user_activation_info": {
                        "activation_type": null,
                        "rings_custom_likes_setting_enabled": null
                      },
                      "text_post_app_privacy": null
                    },
                    "image_versions2": {
                      "additional_candidates": {
                        "first_frame": {
                          "estimated_scans_sizes": [
                            5565,
                            11130
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-1.cdninstagram.com/v/t51.71878-15/655553667_1694908385008299_7686189627358299085_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=qFnrJzP0x5IQ7kNvwFTOeca&_nc_oc=AdqIJnHGKeNT1q6jcMuwBBLqF_PvghhSh6wPK8HmHL0IcAWILgCrq1SbBlePplIA-f4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af26vmi1lFLtsZ_mq6LwiGrYKxnUt_5Ooy6oqmLFuKM8NA&oe=69DC3AA8",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "igtv_first_frame": {
                          "estimated_scans_sizes": [
                            5565,
                            11130
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-1.cdninstagram.com/v/t51.71878-15/655553667_1694908385008299_7686189627358299085_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=qFnrJzP0x5IQ7kNvwFTOeca&_nc_oc=AdqIJnHGKeNT1q6jcMuwBBLqF_PvghhSh6wPK8HmHL0IcAWILgCrq1SbBlePplIA-f4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af26vmi1lFLtsZ_mq6LwiGrYKxnUt_5Ooy6oqmLFuKM8NA&oe=69DC3AA8",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "smart_frame": null
                      },
                      "candidates": [
                        {
                          "estimated_scans_sizes": [
                            22552,
                            45105
                          ],
                          "height": 1333,
                          "scans_profile": "e35",
                          "url": "https://scontent-mia5-2.cdninstagram.com/v/t51.82787-15/655918808_18642480373019133_2706709073646407389_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzg1ODExNzA2MjUzODgzODM4ODE4NjQyNDgwMzY3MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=mR20z9GjA6kQ7kNvwFzvy9B&_nc_oc=Adp-cUnypkpwyoOb-mGrDz3PBgGmFAs1fZlNz1rzzUKy60_xmMccQNmBzzEnQ7EK0C0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia5-2.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af0pqakTzLwiaeVIaku94LBtRU357DCk5zZmUV530GgFvA&oe=69DC2102",
                          "width": 750,
                          "is_spatial_image": false
                        }
                      ],
                      "scrubber_spritesheet_info_candidates": {
                        "default": {
                          "file_size_kb": 399,
                          "max_thumbnails_per_sprite": 105,
                          "rendered_width": 96,
                          "sprite_height": 1232,
                          "sprite_urls": [
                            "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/655031270_1813608302668544_4756991555773361514_n.jpg?_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=j6Cki5vnLssQ7kNvwH0s7TA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&oh=00_Af20rsxIQFk-nlwAwASfQatte7EoLiJVP3qD-eqlLCoymw&oe=69DC1E0E&_nc_sid=c24a68"
                          ],
                          "sprite_width": 1500,
                          "thumbnail_duration": 0.3581333333333333,
                          "thumbnail_height": 176,
                          "thumbnail_width": 100,
                          "thumbnails_per_row": 15,
                          "total_thumbnail_num_per_sprite": 105,
                          "video_length": 37.604
                        }
                      }
                    },
                    "original_width": 1080,
                    "original_height": 1920,
                    "product_type": "clips",
                    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNzYzODIyNzMzZWM4NGM0NzlkOWUyMzQzOTdjODYwOTgzODU4MTE3MDYyNTM4ODM4Mzg4Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1Nzk5NjkzNnwzODU4MTE3MDYyNTM4ODM4Mzg4fDM1Mzk0NDM1MDEzfGVlNzNmNDBmM2QyYTVmNmYxNTMxYzgwNmUxMDA3MzFiMjY2M2UxMjA3NjQ3YTg0YjkzNGMxOGJmZjZkNGQ0NTYifSwic2lnbmF0dXJlIjoiIn0="
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
              "autoplay": true
            },
            "layout_content": {
              "medias": [
                {
                  "media": {
                    "strong_id__": "3804269333950046539_3132929984",
                    "fbid": 17918586363229379,
                    "device_timestamp": 1767724262956994,
                    "carousel_last_edited_at": null,
                    "dynamic_ad_carousel_card_starting_index": null,
                    "is_sidecar_child": null,
                    "sticker_translations_enabled": null,
                    "segmented_video_group_id": null,
                    "pk": 3804269333950046539,
                    "id": "3804269333950046539_3132929984",
                    "is_reel_media": null,
                    "visibility": null,
                    "has_delayed_metadata": true,
                    "code": "DTLes2oASFL",
                    "play_count": 6419056,
                    "video_versions": [
                      {
                        "bandwidth": 3176307,
                        "height": 1280,
                        "id": "1363364408899871v",
                        "type": 101,
                        "url": "https://scontent-mia5-2.cdninstagram.com/o1/v/t2/f2/m86/AQP6mOHtDFqeS6vG1lLtyJYu_6yGMULrR6lBe5uFLMGB0d0ElZ282MgS-UC5xSirQIOayONQbQ4jMTHlkSk17dYv_BEwnekAtre4KCU.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-mia5-2.cdninstagram.com&_nc_ohc=wv_--Bfa92YQ7kNvwFhGlqi&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg0NzU5MTE5NTg2MTMyNywiYXNzZXRfYWdlX2RheXMiOjkxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=179e4095aa7e94aa&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80OTQwNjA5MkE1OTNBNDYyQUUwREU2NTA3RThEOTI5MV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYR2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNjEyMjgzMzIzNDUxNzIwXzM0Njc2MDAzNTY4MzI4NDYzMTMubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJp6F2477l8gGFQIoAkMzLBdAMIhysCDEnBgSZGFzaF9iYXNlbGluZV8xX3YxEQB1_gdl5p0BAA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2CU2oVkTJmwX-sqGA-BKY9ERN_unXvTmNjUr9wluR2MQ&oe=69D8544D",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      },
                      {
                        "bandwidth": 3176307,
                        "height": 1280,
                        "id": "1363364408899871v",
                        "type": 102,
                        "url": "https://scontent-mia5-2.cdninstagram.com/o1/v/t2/f2/m86/AQP6mOHtDFqeS6vG1lLtyJYu_6yGMULrR6lBe5uFLMGB0d0ElZ282MgS-UC5xSirQIOayONQbQ4jMTHlkSk17dYv_BEwnekAtre4KCU.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-mia5-2.cdninstagram.com&_nc_ohc=wv_--Bfa92YQ7kNvwFhGlqi&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg0NzU5MTE5NTg2MTMyNywiYXNzZXRfYWdlX2RheXMiOjkxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=179e4095aa7e94aa&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC80OTQwNjA5MkE1OTNBNDYyQUUwREU2NTA3RThEOTI5MV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYR2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNjEyMjgzMzIzNDUxNzIwXzM0Njc2MDAzNTY4MzI4NDYzMTMubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJp6F2477l8gGFQIoAkMzLBdAMIhysCDEnBgSZGFzaF9iYXNlbGluZV8xX3YxEQB1_gdl5p0BAA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2CU2oVkTJmwX-sqGA-BKY9ERN_unXvTmNjUr9wluR2MQ&oe=69D8544D",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      }
                    ],
                    "video_subtitles_confidence": null,
                    "video_subtitles_locale": null,
                    "is_dash_eligible": 1,
                    "video_duration": 16.55500030517578,
                    "has_audio": true,
                    "carousel_media_count": null,
                    "carousel_media_pending_post_count": null,
                    "can_modify_carousel": null,
                    "carousel_media_ids": null,
                    "video_subtitles_enabled": null,
                    "video_subtitles_uri": null,
                    "video_subtitles_translations_enabled": null,
                    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT16.555828S\" FBManifestTimestamp=\"1775657997\" FBManifestIdentifier=\"FpqQs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxszKgNfxmYIDhujz2sb/hgOK9+Lv572kBPzZnv3WzeoEhNKgi5Wx7ASQs/PFuoL/BIqX9YPyrecF2MuDuN/z7wWu5aHp66D5BvrvzqO8vNYI6K/X/aTK5ArOnvjCtaOjWyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5sYXRhbV9tb2RlcmF0ZQAWtgEUABIUAgA=\"><Period id=\"0\" duration=\"PT16.555828S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:85.6\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"3035928366607348v\" bandwidth=\"660693\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1365433\" FBPlaybackResolutionMos=\"0:100,360:65.4,480:60.5,720:54.6,1080:50.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94,480:89.4,720:81.3,1080:72.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQO_vYZtcbPAQTPdzVQ1tt-c0w6vAXDOoY7igg1IexwRCVOYiZusk2jpFnTv52viONgBYEU2YrOVoKIa1AkeXSy70hxR1Uj81YDmgiI.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=t9KxAULrymoQ7kNvwG25PRG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6NjYwNjkzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Kq34cnU0SDg5DRU1PXWLR_DPOgH4B_7GhMGhTdodELw&amp;oe=69DC1DA7</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-8869\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-193511\" FBFirstSegmentRange=\"906-348812\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"348813-766455\" FBPrefetchSegmentRange=\"906-348812\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1206126657691077v\" bandwidth=\"957698\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1979243\" FBPlaybackResolutionMos=\"0:100,360:71.2,480:66.9,720:60.8,1080:56.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.1,480:94.5,720:87.7,1080:79.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPaBxRG04r3bR4ETqpBEkED3FGutBls7QbAdOIR7u4lgC8ctfr6tF27--TzomYr3ILcoOLKzHAB1-4G2YNYj-oGYu-6fkzYfcP7KOo.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=2aHAiQ9rXxkQ7kNvwHByjOy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6OTU3Njk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0TrEgQMU_0Oa4A6nTAue-SvyEmrynIk2BYfmsI1xgD5Q&amp;oe=69DC20A4</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-10706\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-277169\" FBFirstSegmentRange=\"906-503727\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"503728-1107677\" FBPrefetchSegmentRange=\"906-503727\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1955495901673815v\" bandwidth=\"1169076\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2416091\" FBPlaybackResolutionMos=\"0:100,360:73.9,480:69.7,720:63.8,1080:59.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.9,480:96.4,720:91.1,1080:83.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQM7Xzn9Mu7iIDwt9on3fD55Qrrl9mvW-czkwLw2cPNL0dV7pUHeohBlvvtCBzKKUOmeFnNtcsfAJTCqSY4jPj5734HBjkUvAth5QPM.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=ZbULbWdVIxQQ7kNvwHDnmDO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MTE2OTA3NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1dM4IfX5b-PkViFVZRhDzp2nQdglirzJi8dxToZOj00g&amp;oe=69DC4E46</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-11789\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-339527\" FBFirstSegmentRange=\"906-614825\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"614826-1352359\" FBPrefetchSegmentRange=\"906-614825\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1634662677915077v\" bandwidth=\"1492547\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3084598\" FBPlaybackResolutionMos=\"0:100,360:76.6,480:72.8,720:67.2,1080:62.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.29,480:97.9,720:95,1080:88.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-mia5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPZSi4bW52wdIc8F2SYD1clfuQ5VjAY_ec8_OppuEyGXuJqHnTngC33w2dYerm8BK3hbcL4NbGo1yt-1kw_EsgkatWDpKfjwEax8Y8.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-2.cdninstagram.com&amp;_nc_ohc=58YWA4T0JKQQ7kNvwGCFdkU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MTQ5MjU0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2RHDfzao5uEi20IcszBk6xARrD6Mzpo5I3wbIgqeFeyw&amp;oe=69DC3EA5</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-13441\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-437245\" FBFirstSegmentRange=\"906-790814\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"790815-1729332\" FBPrefetchSegmentRange=\"906-790814\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"25691797173766055v\" bandwidth=\"1890790\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3907634\" FBPlaybackResolutionMos=\"0:100,360:79.1,480:75.1,720:69.7,1080:64.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.6,480:98.3,720:96.9,1080:92.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-mia5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOAEgtBXeovHlKjZotV31qpJowEzV9CJAKIfQE3aT645pLhSnW7kyk1-s6FxWsjkbIbMXcIBpCMH2SKWhPGs6iDbvApWPBnCCrbol8.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-2.cdninstagram.com&amp;_nc_ohc=Lh923Or616kQ7kNvwHYgsA1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MTg5MDc5MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0AYjyrANQLldr5fyGCxtEYH08LtlKc8Odx099DQhOmiA&amp;oe=69DC4601</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-15312\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-557523\" FBFirstSegmentRange=\"906-1008277\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1008278-2198516\" FBPrefetchSegmentRange=\"906-1008277\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"849267731206822v\" bandwidth=\"2283262\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4718743\" FBPlaybackResolutionMos=\"0:100,360:81.4,480:77,720:71.7,1080:66.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.89,480:98.59,720:97.9,1080:94.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPOxxSAhcjqbvkFNC-BF6uINPG4tOwSYPiqsiX1kr6SmzanZC0IVrEFVKDusYSk7VfEpEj3z2nlmrMti_fbDOpgnQCr_LJ9yPWZXfA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=4Bk4BOdvFZ0Q7kNvwFf7B0o&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6MjI4MzI2MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2i_UNcBzoND1oWsR4M3UdhmSexNf8cfJn8Ga2OIu2b-Q&amp;oe=69DC3756</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-17247\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-679262\" FBFirstSegmentRange=\"906-1224439\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1224440-2668874\" FBPrefetchSegmentRange=\"906-1224439\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1405218077961416v\" bandwidth=\"2981007\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6160748\" FBPlaybackResolutionMos=\"0:100,360:83.8,480:79.4,720:74.1,1080:68.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.172,480:99.081,720:98.59,1080:97.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQPUsatiQ58nDZb5hjWdd5vtQ7UpLaHw4DHgk5N7kjyJsXhIrLm-vcs28kwUBeYqshc_cDYahU4pxkDKSHIw0BueJzMxDel_Kf8mhj0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=DLUhtBrOxs8Q7kNvwG_-ZnG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6Mjk4MTAwNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af31CaEimXVhujynmyo3LUwsKOEf_PLfH80GM6KsqsrOpQ&amp;oe=69DC2CBF</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-20772\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-883612\" FBFirstSegmentRange=\"906-1598808\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1598809-3481948\" FBPrefetchSegmentRange=\"906-1598808\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"859810403613187v\" bandwidth=\"4599428\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"9505486\" FBPlaybackResolutionMos=\"0:100,360:87.3,480:84,720:78.8,1080:75.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.487,480:99.499,720:99.356,1080:99.112\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMw1VCAHJXe2hvoUHzhJcrpSey1tIyZ-th8KFmvw6dsLxHGEaZNghQC_d8oerUYlS-EbJNCmMyBkJlSTV1EwFs2Dd4426hXrdFafDs.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=mQaydJ93kBYQ7kNvwF8Q8NY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODQ3NTkxMTk1ODYxMzI3LCJhc3NldF9hZ2VfZGF5cyI6OTEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNiwiYml0cmF0ZSI6NDU5OTQyOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3C_u_bYuR5y7fxkztvSJvqVkgk0_lwoF-PmJ1eCUTokw&amp;oe=69DC2FA1</BaseURL><SegmentBase indexRange=\"826-905\" timescale=\"15360\" FBMinimumPrefetchRange=\"906-33285\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-1395919\" FBFirstSegmentRange=\"906-2539946\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"2539947-5440382\" FBPrefetchSegmentRange=\"906-2539946\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1360330895906430a\" bandwidth=\"35755\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"35755\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"74910\" FBPaqMos=\"82.24\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMdS5dbSFZIWq2N-t1ZOAEbun1DjiqOKdbq3GM22fvESDptQC8iHDEwjQ5F4kT6cWpbX5LxN9l748fNG-UoTln5Jx49F2auWdylY04.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=RdNMtXUe0vsQ7kNvwFueCnX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NDc1OTExOTU4NjEzMjcsImFzc2V0X2FnZV9kYXlzIjo5MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjozNjE5NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0qZCipfXb-ZQHzH_8EtyRvdjhafdu8BHlrUbT47_audQ&amp;oe=69DC38BD</BaseURL><SegmentBase indexRange=\"837-916\" timescale=\"44100\" FBMinimumPrefetchRange=\"917-1986\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"917-12888\" FBFirstSegmentRange=\"917-23297\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"23298-45484\" FBPrefetchSegmentRange=\"917-23297\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1653454959309548a\" bandwidth=\"70846\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"70846\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"147532\" FBPaqMos=\"86.73\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrhBbJLcolsXZbis_ifwxXlV6tWbLJop0add8A6EHtNGPTDjSDibmsOp51wQq_veobd_ikjxhZWrlRaoIn240tHeILT0pNXHv4J4E.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=N9FxmwkcMXsQ7kNvwH8s6i8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NDc1OTExOTU4NjEzMjcsImFzc2V0X2FnZV9kYXlzIjo5MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjo3MTI4OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0UexkVCrfWC4Svt81tqu9-U8kvCXNzjJ5slY26b4bXSg&amp;oe=69DC1E6B</BaseURL><SegmentBase indexRange=\"838-917\" timescale=\"44100\" FBMinimumPrefetchRange=\"918-2762\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-22806\" FBFirstSegmentRange=\"918-44100\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"44101-89202\" FBPrefetchSegmentRange=\"918-44100\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"2441954696223741a\" bandwidth=\"112150\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"112150\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"233005\" FBPaqMos=\"92.30\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0Gdv9QrlXR0Hv7mNioytZxt6wsaoHHDXhnnR9pI5mUjqXVbOl4oPTfs6DG-5t9RZACPQvUNRar_ysQR1SbczrkoMb9pPojfAaVIs.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=7yuOq9Vzu-MQ7kNvwF5vgsu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NDc1OTExOTU4NjEzMjcsImFzc2V0X2FnZV9kYXlzIjo5MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjoxMTI1OTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2GHIjaCMR98_u5ygInTirzmP5yWQDoh4ampY-Kltu-2A&amp;oe=69DC457C</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2324\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-39045\" FBFirstSegmentRange=\"913-72254\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"72255-141871\" FBPrefetchSegmentRange=\"913-72254\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1364239062406274a\" bandwidth=\"128774\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"128774\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"267408\" FBPaqMos=\"93.84\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOW2AJiAHyRBlGhJI6BUkpr2ofuHy6jA9o0EhpvwYRTUAEBmJeOwqaHZ6dmbFzDypqDUAC_oDUgUm2QTj3Tc7fAI8iYK_xqrb6fWDs.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=yZl0tQkQaiIQ7kNvwEfA7p8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NDc1OTExOTU4NjEzMjcsImFzc2V0X2FnZV9kYXlzIjo5MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE2LCJiaXRyYXRlIjoxMjkyMTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af20QLtl_fOpAcU5zijKp07ivbwqelxDjooKKhrf6cZ2Wg&amp;oe=69DC2B6E</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2415\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-43366\" FBFirstSegmentRange=\"913-81440\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"81441-161051\" FBPrefetchSegmentRange=\"913-81440\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "number_of_qualities": 8,
                    "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                    "carousel_media": null,
                    "open_carousel_submission_state": null,
                    "open_to_public_submission_description_text": null,
                    "total_carousel_media_count": null,
                    "more_carousel_media_available": null,
                    "tallest_media_aspect_ratio": null,
                    "video_sticker_locales": [],
                    "translated_video_subtitles": null,
                    "autodub_status": null,
                    "basel_encoding_timeout": null,
                    "video_imf_spec": null,
                    "taken_at": 1767724836,
                    "media_type": 2,
                    "view_count": null,
                    "attribution": null,
                    "audio": null,
                    "is_seen": null,
                    "user": {
                      "strong_id__": "3132929984",
                      "all_media_count": null,
                      "allowed_commenter_type": null,
                      "coeff_weight": null,
                      "fbid_v2": 17841403179521616,
                      "feed_post_reshare_disabled": false,
                      "id": "3132929984",
                      "is_active": null,
                      "is_unpublished": false,
                      "liked_clips_count": null,
                      "live_invite_only_branding_enabled": null,
                      "pk": 3132929984,
                      "pk_id": "3132929984",
                      "reel_auto_archive": null,
                      "show_insights_terms": null,
                      "text_post_app_take_a_break_setting": null,
                      "third_party_downloads_enabled": 1,
                      "eligible_for_text_app_activation_badge": false,
                      "account_type": 3,
                      "account_badges": [],
                      "can_boost_post": null,
                      "can_see_organic_insights": null,
                      "fan_club_info": {
                        "autosave_to_exclusive_highlight": null,
                        "connected_member_count": null,
                        "fan_club_id": null,
                        "fan_club_name": null,
                        "has_created_ssc": null,
                        "has_enough_subscribers_for_ssc": null,
                        "is_fan_club_gifting_eligible": null,
                        "is_fan_club_referral_eligible": null,
                        "is_free_trial_eligible": null,
                        "largest_public_bc_id": null,
                        "subscriber_count": null,
                        "should_show_playlists_in_profile_tab": null,
                        "fan_consideration_page_revamp_eligiblity": null
                      },
                      "full_name": "Will Smith",
                      "friendship_status": {
                        "following": false,
                        "is_bestie": false,
                        "is_feed_favorite": false,
                        "is_private": false,
                        "is_restricted": false,
                        "text_post_app_pre_following": null,
                        "followed_by": false,
                        "is_muting_reel": false
                      },
                      "has_anonymous_profile_picture": false,
                      "has_onboarded_to_text_post_app": null,
                      "interop_messaging_user_fbid": null,
                      "is_favorite": false,
                      "is_private": false,
                      "is_ring_creator": false,
                      "show_ring_award": false,
                      "aigm_account_label_info": null,
                      "is_verified": true,
                      "is_ai_user": null,
                      "ai_agent_owner_username": null,
                      "live_broadcast_id": null,
                      "live_broadcast_visibility": null,
                      "profile_pic_id": "3805091926094576158_3132929984",
                      "profile_pic_url": "https://scontent-mia3-2.cdninstagram.com/v/t51.82787-19/610576131_18443537728105985_6823172465207480614_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=v4iXxn1Hcc8Q7kNvwGRi2Rr&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&ig_cache_key=GAOnZCQBbq-CTIZBACYR69U0x7BebmNDAQAB1501500j-ccb7-5&oh=00_Af2h9PO6kdRU6YPCVYf5-eRllYKDlVm-ITFWdbVH1I1q6A&oe=69DC4599&_nc_sid=c24a68",
                      "reachability_status": null,
                      "show_account_transparency_details": true,
                      "transparency_product_enabled": false,
                      "transparency_product": null,
                      "transparency_label": null,
                      "username": "willsmith",
                      "opal_info": null,
                      "latest_reel_media": null,
                      "user_activation_info": {
                        "activation_type": null,
                        "rings_custom_likes_setting_enabled": null
                      },
                      "text_post_app_privacy": null
                    },
                    "image_versions2": {
                      "additional_candidates": {
                        "first_frame": {
                          "estimated_scans_sizes": [
                            4504,
                            9009
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-1.cdninstagram.com/v/t51.71878-15/610141019_876013735176583_4755567570217260987_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Ndi-HlwAn4MQ7kNvwFprVQn&_nc_oc=Adod-XDcYILltwJo-ivwdkykN93ngrKATCnt637CqIfZenZVNUVSytAjgKLaz578o-I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af2UZFJ6MX0kLcenAz9QLuwPZnmhGf8em1bigGmdM6tfJQ&oe=69DC3BF6",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "igtv_first_frame": {
                          "estimated_scans_sizes": [
                            4504,
                            9009
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-1.cdninstagram.com/v/t51.71878-15/610141019_876013735176583_4755567570217260987_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Ndi-HlwAn4MQ7kNvwFprVQn&_nc_oc=Adod-XDcYILltwJo-ivwdkykN93ngrKATCnt637CqIfZenZVNUVSytAjgKLaz578o-I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af2UZFJ6MX0kLcenAz9QLuwPZnmhGf8em1bigGmdM6tfJQ&oe=69DC3BF6",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "smart_frame": null
                      },
                      "candidates": [
                        {
                          "estimated_scans_sizes": [
                            7275,
                            14550
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-1.cdninstagram.com/v/t51.71878-15/611648715_1237054851651622_522192991498352129_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=MzgwNDI2OTMzMzk1MDA0NjUzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=tt6i8vh3Qn8Q7kNvwHhODv-&_nc_oc=AdqzPArscGO4ODTs6qkAKZPby6kqpzcGGSYB9bkbZ-JGjEGzDWTSxzrw1M-uhQdJNYk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af10EtBOWnQvp3d3TxvYJzGW6aQie0p1LN76BO1KNWAhbQ&oe=69DC2396",
                          "width": 640,
                          "is_spatial_image": false
                        }
                      ],
                      "scrubber_spritesheet_info_candidates": {
                        "default": {
                          "file_size_kb": 372,
                          "max_thumbnails_per_sprite": 105,
                          "rendered_width": 96,
                          "sprite_height": 1232,
                          "sprite_urls": [
                            "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/611330302_2103406610435804_5702456615174351102_n.jpg?_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=NcKVj2FK-0UQ7kNvwFIhjig&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&oh=00_Af2HMde69JGqklCjFaPqBbl829z-mCbEYDT1ETaXNK8AQQ&oe=69DC3A4F&_nc_sid=c24a68"
                          ],
                          "sprite_width": 1500,
                          "thumbnail_duration": 0.15745714285714288,
                          "thumbnail_height": 176,
                          "thumbnail_width": 100,
                          "thumbnails_per_row": 15,
                          "total_thumbnail_num_per_sprite": 105,
                          "video_length": 16.533
                        }
                      }
                    },
                    "original_width": 1080,
                    "original_height": 1920,
                    "product_type": "clips",
                    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNzYzODIyNzMzZWM4NGM0NzlkOWUyMzQzOTdjODYwOTgzODA0MjY5MzMzOTUwMDQ2NTM5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1Nzk5NjkzNnwzODA0MjY5MzMzOTUwMDQ2NTM5fDM1Mzk0NDM1MDEzfDg3OGNlZGYwYTE3YWQ3YzY2ZGFmZGRhNWZiYjg5Yzk5Zjg4MDA4NjA1OTk1OTkyZDAyNzgyMDM1OTRkZDkwZjUifSwic2lnbmF0dXJlIjoiIn0="
                  }
                },
                {
                  "media": {
                    "strong_id__": "3822552044629218933_2220586960",
                    "fbid": 18159011614417029,
                    "device_timestamp": 1769903730443895,
                    "carousel_last_edited_at": null,
                    "dynamic_ad_carousel_card_starting_index": null,
                    "is_sidecar_child": null,
                    "sticker_translations_enabled": null,
                    "segmented_video_group_id": null,
                    "pk": 3822552044629218933,
                    "id": "3822552044629218933_2220586960",
                    "is_reel_media": null,
                    "visibility": null,
                    "has_delayed_metadata": true,
                    "code": "DUMbtTzkVZ1",
                    "play_count": 1645242,
                    "video_versions": [
                      {
                        "bandwidth": 2100395,
                        "height": 1280,
                        "id": "2361917374240336v",
                        "type": 101,
                        "url": "https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMZfhvrysDKiq1DBepcZbToGXFJlliYrpCbJvvE37sqP0CauyhhHdH1v1HlRgnhPhPLhGrhP7zOFADLeM2sTW5GSs-9OxCuFNPhv9s.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_ohc=GooVOsZaanEQ7kNvwH6IEzX&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg1MDg4ODU2MDAwNzQ5NjEsImFzc2V0X2FnZV9kYXlzIjo2NiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=aace559b16c3d7c4&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8yMDQwOUE4RkI1NkNBRTQ4NzZGRTZBRUI4Q0M3QUI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0NDNDM1RkE3NEQyQTRBQjQyMjdGN0IyOThGRDEwNDlFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACai84v29-7gQRUCKAJDMywXQCPul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Bl3Nfm_ijRdFacs95UNXPqgD2kLnmz-NDH80xJbJ-kg&oe=69D8321E",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      },
                      {
                        "bandwidth": 2100395,
                        "height": 1280,
                        "id": "2361917374240336v",
                        "type": 102,
                        "url": "https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMZfhvrysDKiq1DBepcZbToGXFJlliYrpCbJvvE37sqP0CauyhhHdH1v1HlRgnhPhPLhGrhP7zOFADLeM2sTW5GSs-9OxCuFNPhv9s.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_ohc=GooVOsZaanEQ7kNvwH6IEzX&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTg1MDg4ODU2MDAwNzQ5NjEsImFzc2V0X2FnZV9kYXlzIjo2NiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=aace559b16c3d7c4&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8yMDQwOUE4RkI1NkNBRTQ4NzZGRTZBRUI4Q0M3QUI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0NDNDM1RkE3NEQyQTRBQjQyMjdGN0IyOThGRDEwNDlFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACai84v29-7gQRUCKAJDMywXQCPul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Bl3Nfm_ijRdFacs95UNXPqgD2kLnmz-NDH80xJbJ-kg&oe=69D8321E",
                        "url_expiration_timestamp_us": null,
                        "width": 720,
                        "fallback": null
                      }
                    ],
                    "video_subtitles_confidence": null,
                    "video_subtitles_locale": null,
                    "is_dash_eligible": 1,
                    "video_duration": 9.965999603271484,
                    "has_audio": true,
                    "carousel_media_count": null,
                    "carousel_media_pending_post_count": null,
                    "can_modify_carousel": null,
                    "carousel_media_ids": null,
                    "video_subtitles_enabled": null,
                    "video_subtitles_uri": null,
                    "video_subtitles_translations_enabled": null,
                    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT9.966666S\" FBManifestTimestamp=\"1775657997\" FBManifestIdentifier=\"FpqQs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZ1qynqOKw1JYDjqDv+723nwO8p+qogKunBNz9xtTtqqoEmIOlpLOP5gT47tyamaO3Bdit0sbxq+kFprGS57O0gAf+yIzWyuaHB+Tq3cKwkpYH+qHZ2rm77Qu4zN/8r/ONXJCz+fqY2sxcIhgmZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlMTIzNF9pYnJfYXVkaW8iLBkYDmxhdGFtX21vZGVyYXRlABaEARQEEhQCAA==\"><Period id=\"0\" duration=\"PT9.966666S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:88.4\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"26064373163175112v\" bandwidth=\"195201\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"243189\" FBPlaybackResolutionMos=\"0:100,360:46.8,480:39.9,720:33.8,1080:31.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.6,480:89.9,720:85.9,1080:75\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"180p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMHG_UhTveoEtMLPFgWjAy5CcjfoRvWvzrYi5P-fUUHVj-87DDEXqn870ObAUsLFBBS32kMmMielXKYclHmc-AUJgJJtarMyUvnzag.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=F2C6pbOh9H8Q7kNvwEmn6jQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODUwODg4NTYwMDA3NDk2MSwiYXNzZXRfYWdlX2RheXMiOjY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OSwiYml0cmF0ZSI6MTk1MjAxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2eNiQNd3LKlHBo8eEgEpTeLgSim-itWUZn04gwrkwp3A&amp;oe=69DC4674</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"15360\" FBMinimumPrefetchRange=\"882-29233\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-86651\" FBFirstSegmentRange=\"882-127846\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"127847-243188\" FBPrefetchSegmentRange=\"882-127846\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1639026300439404v\" bandwidth=\"312744\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"389627\" FBPlaybackResolutionMos=\"0:100,360:54.8,480:47.4,720:40.3,1080:36\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.2,480:93.3,720:90.2,1080:79.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMWfyZ_e4IfpUFNNVIorFRcLck3G0RRPwPft5ctkSMWbOPuT94DQ52TdM83vx9E05Y4ao-T32rj3aCTk4CO5BVKhQT7HlW_FbHRibM.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=P_vnR7F7d_cQ7kNvwEucas0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODUwODg4NTYwMDA3NDk2MSwiYXNzZXRfYWdlX2RheXMiOjY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OSwiYml0cmF0ZSI6MzEyNzQ0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0iRqJTrdqwAGlg16mztr6ZxH0nAIiHwJMNZN9AbnKOMg&amp;oe=69DC45F0</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"15360\" FBMinimumPrefetchRange=\"882-38046\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-132131\" FBFirstSegmentRange=\"882-203963\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"203964-389626\" FBPrefetchSegmentRange=\"882-203963\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"25926267283698460v\" bandwidth=\"493343\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"614624\" FBPlaybackResolutionMos=\"0:100,360:61.7,480:54.9,720:47.2,1080:42.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95.7,720:93.6,1080:83.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNifN-D4pkOW8Zm9ffKWym_G5wHCGWY6IwUXa3vZs1kCIjFtALCHvy4vsGhWlwWMb0y3F72CdliCEV_bNq5jcJOZJqgP64-xrg2yNQ.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=ym80ciFGZ9EQ7kNvwFQkdin&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODUwODg4NTYwMDA3NDk2MSwiYXNzZXRfYWdlX2RheXMiOjY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OSwiYml0cmF0ZSI6NDkzMzQzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2eET1e2plzmB_gUWhID-gKdnR7ye-bArneJdS93EdUYw&amp;oe=69DC50F6</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"15360\" FBMinimumPrefetchRange=\"882-48391\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-200084\" FBFirstSegmentRange=\"882-321235\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"321236-614623\" FBPrefetchSegmentRange=\"882-321235\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1218995156475758v\" bandwidth=\"733958\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"914390\" FBPlaybackResolutionMos=\"0:100,360:67.4,480:61,720:53.6,1080:47.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.01,480:97.3,720:96.1,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMcipwLirXc4DKCA9adPhy8__9WDHu1tSO98dXRDeQXquujodYiOdYKhNH0tSMpoKtDGcKRTtL4RxTh-CD-DBkNN9KMbW86_3sGxKQ.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=bzmLsvG_uF4Q7kNvwF1iefn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODUwODg4NTYwMDA3NDk2MSwiYXNzZXRfYWdlX2RheXMiOjY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OSwiYml0cmF0ZSI6NzMzOTU4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1AJ08TXkCxiSHkYYSYN8A3LiTtMnSc54ZBgplUuOvVdA&amp;oe=69DC3354</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"15360\" FBMinimumPrefetchRange=\"882-59487\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-287791\" FBFirstSegmentRange=\"882-476613\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"476614-914389\" FBPrefetchSegmentRange=\"882-476613\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1528925841497020v\" bandwidth=\"990055\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"1233444\" FBPlaybackResolutionMos=\"0:100,360:71.2,480:65.4,720:57.8,1080:52\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.55,480:98.17,720:97.6,1080:89.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-mia3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPDJmQRdkeVIw7SDUwBflHdaY6XblQ9nrgQEkHI7C-V2xnKiSZBKZtoOkjP_35S2Y-9gGhP_JYyIjuIiuTlfCgS8wT95Pf7TYlZtFo.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-1.cdninstagram.com&amp;_nc_ohc=ANtBdJAxLTMQ7kNvwG9bli0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODUwODg4NTYwMDA3NDk2MSwiYXNzZXRfYWdlX2RheXMiOjY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OSwiYml0cmF0ZSI6OTkwMDU1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3uR6iw7KTW-rCneyxYmdwdKEcsJ1153v6ab7VtTDG2iA&amp;oe=69DC3A27</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"15360\" FBMinimumPrefetchRange=\"882-68471\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-375720\" FBFirstSegmentRange=\"882-638047\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"638048-1233443\" FBPrefetchSegmentRange=\"882-638047\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"3336939636467837v\" bandwidth=\"1602576\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"1996543\" FBPlaybackResolutionMos=\"0:100,360:76.8,480:71.8,720:65,1080:58.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.22,480:99.138,720:99.23,1080:92.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQN5mE0om4Dkiuvf1hkr6lYx8MXSbs6kC7hfItllKpjvSm15v1rmsSpUSzgvaASbRVYxY2dLCkQn89eFyenczxxgXDVuAypWht5567o.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=zDDi1B40PNMQ7kNvwG4ZKJc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODUwODg4NTYwMDA3NDk2MSwiYXNzZXRfYWdlX2RheXMiOjY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OSwiYml0cmF0ZSI6MTYwMjU3NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2O7dtmEHAmf1Ix6HTtxOiapsFLxlN19bYKxhT8WfHNYw&amp;oe=69DC45E5</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"15360\" FBMinimumPrefetchRange=\"882-83479\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-582514\" FBFirstSegmentRange=\"882-1019302\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1019303-1996542\" FBPrefetchSegmentRange=\"882-1019302\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2019019098667698v\" bandwidth=\"2451141\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"3053714\" FBPlaybackResolutionMos=\"0:100,360:82.6,480:77.1,720:71,1080:64.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.526,480:99.636,720:99.843,1080:95\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-mia5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPQq8QDvmmsHuhr4QmGOggy2u1PQEjlazvIjzidcldDFTh-3kguYo15_6SgUdSt4EB9rdsRtPIZfcV816QvhAQYYWuDQTcZJLGARxk.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-1.cdninstagram.com&amp;_nc_ohc=NyJy0mZb7o8Q7kNvwH8JeX9&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODUwODg4NTYwMDA3NDk2MSwiYXNzZXRfYWdlX2RheXMiOjY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OSwiYml0cmF0ZSI6MjQ1MTE0MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0HQ4XdGLs4h2wsD_xafyi5513oB08ZxllAwR_asdP4hw&amp;oe=69DC2C46</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"15360\" FBMinimumPrefetchRange=\"882-94668\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-857339\" FBFirstSegmentRange=\"882-1541936\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1541937-3053713\" FBPrefetchSegmentRange=\"882-1541936\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1971225143430227v\" bandwidth=\"3380685\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3-hfr_q80\" FBContentLength=\"4208936\" FBPlaybackResolutionMos=\"0:100,360:86.6,480:81.9,720:75.6,1080:69.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.635,480:99.719,720:99.879,1080:96.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/200\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOBHwJRVFIUZdVW5B_OA29WKtS_YtShBX1fSoDqWScglSJyB6IbLJC3sTeFIBpeWW0KHyh03Gwz2SnjtnhWbXuRYijBScUSqPg6Glw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=ONheCO9nE6kQ7kNvwHRjLIF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zLWhmcl9xODAiLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjU2NzA2NzM0MzM1MjQyNywiY2xpZW50X25hbWUiOiJpZyIsInhwdl9hc3NldF9pZCI6MTg1MDg4ODU2MDAwNzQ5NjEsImFzc2V0X2FnZV9kYXlzIjo2NiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjksImJpdHJhdGUiOjMzODA2ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0i5nDCWcRzbRGlL-M7XY5m3thUYeSs3otgm1H6sd7JVg&amp;oe=69DC4F66</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"11988\" FBMinimumPrefetchRange=\"882-101596\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-1091143\" FBFirstSegmentRange=\"882-2100879\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2100880-4208935\" FBPrefetchSegmentRange=\"882-2100879\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1350464860102860v\" bandwidth=\"5144170\" codecs=\"av01.0.09M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3-hfr_q90\" FBContentLength=\"6404466\" FBPlaybackResolutionMos=\"0:100,360:89.9,480:86,720:80.2,1080:75.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.847,480:99.943,720:99.945,1080:100\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/200\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOdM8pKJ4mNXvS622qoxTAuBTCFPCxKeIGGzHrJNZiTQvFf1jrj_ZtJ3MuKvF0KDtrMa5UxOv6mHPxvO1TPWEQ3l4qT9MPAMpLFTPk.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=bBaglUfr62UQ7kNvwGAhU4L&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zLWhmcl9xOTAiLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjU2NzA2NzM0MzM1MjQyNywiY2xpZW50X25hbWUiOiJpZyIsInhwdl9hc3NldF9pZCI6MTg1MDg4ODU2MDAwNzQ5NjEsImFzc2V0X2FnZV9kYXlzIjo2NiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjksImJpdHJhdGUiOjUxNDQxNzAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1uVsiTe8N4ArP8voJAxzqp2nR6b1nIToYpNL3_zAFl8Q&amp;oe=69DC5015</BaseURL><SegmentBase indexRange=\"826-881\" timescale=\"11988\" FBMinimumPrefetchRange=\"882-146138\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"882-1686555\" FBFirstSegmentRange=\"882-3235340\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"3235341-6404465\" FBPrefetchSegmentRange=\"882-3235340\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"894253096307158a\" bandwidth=\"37521\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"37521\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"47515\" FBPaqMos=\"73.77\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOEfC_u-_4IoO5DXIm6IXvMWHRuUG008ZYbwJv7Zsus10NnGcclKbweA_8t052gpU2F3r6CiZZ6IXhJj6EovUDo08S6RUxvgl22Q10.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia5-2.cdninstagram.com&amp;_nc_ohc=v-gAcXqIZ78Q7kNvwFsEuNq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTA4ODg1NjAwMDc0OTYxLCJhc3NldF9hZ2VfZGF5cyI6NjYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5LCJiaXRyYXRlIjozODI0OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1klUHddMne2E-Bp5Z-4jTCNld5wr_PFRFWDAaJlqwzHA&amp;oe=69DC3D3D</BaseURL><SegmentBase indexRange=\"837-904\" timescale=\"44100\" FBMinimumPrefetchRange=\"905-2125\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"905-13263\" FBFirstSegmentRange=\"905-23999\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"24000-46437\" FBPrefetchSegmentRange=\"905-23999\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1212400590997982a\" bandwidth=\"69809\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"69809\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"87627\" FBPaqMos=\"79.96\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNG_d8WR3N-vGwFzMyI5v1OPWBI0otw5Rp1FtfwevOgkYCLEaE-ceOmefSGNioH2xeM0qkF9YgCnGuTv8aLOtV5xrdUkTZ_f9sNKPU.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-2.cdninstagram.com&amp;_nc_ohc=KHP8jNzA1B4Q7kNvwEFLNDf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTA4ODg1NjAwMDc0OTYxLCJhc3NldF9hZ2VfZGF5cyI6NjYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5LCJiaXRyYXRlIjo3MDUzNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1_dB8fMGnVQIgoTX-K_wGiT7VhqvEnE6w-Z4uWMUrJxw&amp;oe=69DC418A</BaseURL><SegmentBase indexRange=\"838-905\" timescale=\"44100\" FBMinimumPrefetchRange=\"906-2777\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-23734\" FBFirstSegmentRange=\"906-44318\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"44319-85807\" FBPrefetchSegmentRange=\"906-44318\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1987480368812607a\" bandwidth=\"107432\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"107432\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"134360\" FBPaqMos=\"90.56\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMj2sR-Lva9PiW4fdVOXKzyvQKLtDTPCF6SXE9JqvSODgDqy50DO-192FTXh4KhDnSg5SxzttMY8qMbGK1kBPaWoOD20B1O00QwA-0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=1udA2TJTljcQ7kNvwFKHvMi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTA4ODg1NjAwMDc0OTYxLCJhc3NldF9hZ2VfZGF5cyI6NjYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5LCJiaXRyYXRlIjoxMDgxNTcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1g7frB7ZSdEvOTDl1VPUY8ItDFTRTYcuuSJwYZVT2ICw&amp;oe=69DC4797</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2539\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-35395\" FBFirstSegmentRange=\"901-65872\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"65873-132517\" FBPrefetchSegmentRange=\"901-65872\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"913547861026823a\" bandwidth=\"118650\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"118650\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"148295\" FBPaqMos=\"92.16\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mia3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNcfcxZNIyBbnK-7GPF2wjKhftBqRA08Ab9Frk030M7Z0ejVfpWKUOzE6fZjR66rIwbQ8qY11q7dN9tDE_zknjr5YBG8XOX8uvCzEo.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mia3-3.cdninstagram.com&amp;_nc_ohc=RpCJ-lns-bEQ7kNvwHm4X3E&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4NTA4ODg1NjAwMDc0OTYxLCJhc3NldF9hZ2VfZGF5cyI6NjYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5LCJiaXRyYXRlIjoxMTkzNzQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af065ih7L8TBAIRdzKv4cc9RJxkzkUetFQjRRhSMQl87Hg&amp;oe=69DC43F7</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2612\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-38547\" FBFirstSegmentRange=\"901-72272\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"72273-146217\" FBPrefetchSegmentRange=\"901-72272\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "number_of_qualities": 9,
                    "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
                    "carousel_media": null,
                    "open_carousel_submission_state": null,
                    "open_to_public_submission_description_text": null,
                    "total_carousel_media_count": null,
                    "more_carousel_media_available": null,
                    "tallest_media_aspect_ratio": null,
                    "video_sticker_locales": [
                      "en",
                      "es"
                    ],
                    "translated_video_subtitles": null,
                    "autodub_status": null,
                    "basel_encoding_timeout": null,
                    "video_imf_spec": null,
                    "taken_at": 1769903786,
                    "media_type": 2,
                    "view_count": null,
                    "attribution": null,
                    "audio": null,
                    "is_seen": null,
                    "user": {
                      "strong_id__": "2220586960",
                      "all_media_count": null,
                      "allowed_commenter_type": null,
                      "coeff_weight": null,
                      "fbid_v2": 17841402248807573,
                      "feed_post_reshare_disabled": false,
                      "id": "2220586960",
                      "is_active": null,
                      "is_unpublished": false,
                      "liked_clips_count": null,
                      "live_invite_only_branding_enabled": null,
                      "pk": 2220586960,
                      "pk_id": "2220586960",
                      "reel_auto_archive": null,
                      "show_insights_terms": null,
                      "text_post_app_take_a_break_setting": null,
                      "third_party_downloads_enabled": 1,
                      "eligible_for_text_app_activation_badge": false,
                      "account_type": 3,
                      "account_badges": [],
                      "can_boost_post": null,
                      "can_see_organic_insights": null,
                      "fan_club_info": {
                        "autosave_to_exclusive_highlight": null,
                        "connected_member_count": null,
                        "fan_club_id": null,
                        "fan_club_name": null,
                        "has_created_ssc": null,
                        "has_enough_subscribers_for_ssc": null,
                        "is_fan_club_gifting_eligible": null,
                        "is_fan_club_referral_eligible": null,
                        "is_free_trial_eligible": null,
                        "largest_public_bc_id": null,
                        "subscriber_count": null,
                        "should_show_playlists_in_profile_tab": null,
                        "fan_consideration_page_revamp_eligiblity": null
                      },
                      "full_name": "Andrea Baratte",
                      "friendship_status": {
                        "following": false,
                        "is_bestie": false,
                        "is_feed_favorite": false,
                        "is_private": false,
                        "is_restricted": false,
                        "text_post_app_pre_following": null,
                        "followed_by": false,
                        "is_muting_reel": false
                      },
                      "has_anonymous_profile_picture": false,
                      "has_onboarded_to_text_post_app": null,
                      "interop_messaging_user_fbid": null,
                      "is_favorite": false,
                      "is_private": false,
                      "is_ring_creator": false,
                      "show_ring_award": false,
                      "aigm_account_label_info": null,
                      "is_verified": true,
                      "is_ai_user": null,
                      "ai_agent_owner_username": null,
                      "live_broadcast_id": null,
                      "live_broadcast_visibility": null,
                      "profile_pic_id": "2767197922582816806_2220586960",
                      "profile_pic_url": "https://scontent-mia3-1.cdninstagram.com/v/t51.2885-19/273372577_3143721249241038_6745431679201440428_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mia3-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gH_GAYOJYc0aS76H0I33zuGk2HZIzKVhWS0cR4HOpE7MevRqWfxeWk16W-FiBjzPyw&_nc_ohc=hBoyVU6EVvkQ7kNvwHYNexI&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&edm=AIJgPg8BAAAA&ccb=7-5&ig_cache_key=GKFVSxDOd1WkMisLAKzyd5dflpxdbkULAAAB1501500j-ccb7-5&oh=00_Af3V6YQi4xJTE2zkR8aHQxAHemML8ENJrYP1IC1PEamjqg&oe=69DC463B&_nc_sid=c24a68",
                      "reachability_status": null,
                      "show_account_transparency_details": true,
                      "transparency_product_enabled": false,
                      "transparency_product": null,
                      "transparency_label": null,
                      "username": "montanawild_",
                      "opal_info": null,
                      "latest_reel_media": null,
                      "user_activation_info": {
                        "activation_type": null,
                        "rings_custom_likes_setting_enabled": null
                      },
                      "text_post_app_privacy": null
                    },
                    "image_versions2": {
                      "additional_candidates": {
                        "first_frame": {
                          "estimated_scans_sizes": [
                            7787,
                            15575
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-2.cdninstagram.com/v/t51.71878-15/624705740_878463898373592_5838872960278088440_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=8xLo0hEZqCUQ7kNvwGMU6Zl&_nc_oc=AdqCIBtNbkwb_8RMGP-whN1dX902hiMLdC4AA2YM8TXbH-1HSLz0hOSjkoWuMWJbb98&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af2p9ddqhsel6mzfrmmx2ijsrmnMTwSTjoYnLnl2HVYlyg&oe=69DC3DBC",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "igtv_first_frame": {
                          "estimated_scans_sizes": [
                            7787,
                            15575
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-2.cdninstagram.com/v/t51.71878-15/624705740_878463898373592_5838872960278088440_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=8xLo0hEZqCUQ7kNvwGMU6Zl&_nc_oc=AdqCIBtNbkwb_8RMGP-whN1dX902hiMLdC4AA2YM8TXbH-1HSLz0hOSjkoWuMWJbb98&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-2.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af2p9ddqhsel6mzfrmmx2ijsrmnMTwSTjoYnLnl2HVYlyg&oe=69DC3DBC",
                          "width": 640,
                          "is_spatial_image": false
                        },
                        "smart_frame": null
                      },
                      "candidates": [
                        {
                          "estimated_scans_sizes": [
                            7368,
                            14737
                          ],
                          "height": 1136,
                          "scans_profile": "e15",
                          "url": "https://scontent-mia3-3.cdninstagram.com/v/t51.71878-15/626603063_3029831130545132_7909957285141760152_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=MzgyMjU1MjA0NDYyOTIxODkzMw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=cEN_6RI15J4Q7kNvwHrarU0&_nc_oc=Adr2MjOqX9C3L0DjsFSokOZ1_h7FlL7ruCpfRe4WSdaTMsCPeBaCHroUlxRCUVoNurc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mia3-3.cdninstagram.com&_nc_gid=_2GQZ9QZn5SfLq81hQ4yGQ&_nc_ss=7a3ba&oh=00_Af0CnUiEd90P-lbb2HSLO3E3o02gjurgKuQ0My_DzZYVHw&oe=69DC42EC",
                          "width": 640,
                          "is_spatial_image": false
                        }
                      ]
                    },
                    "original_width": 1080,
                    "original_height": 1920,
                    "product_type": "clips",
                    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNzYzODIyNzMzZWM4NGM0NzlkOWUyMzQzOTdjODYwOTgzODIyNTUyMDQ0NjI5MjE4OTMzIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1Nzk5NjkzNnwzODIyNTUyMDQ0NjI5MjE4OTMzfDM1Mzk0NDM1MDEzfDdiZDk5ZTUzM2QyY2Q2NTdkYjQxYjJkMzY2MjFkZTNjOWMxOGIxN2UyNWE1Yzg4MjE5M2RhN2I2YjU2NTJhMWEifSwic2lnbmF0dXJlIjoiIn0="
                  }
                }
              ]
            }
          }
        ],
        "rank_token": "a9ffb628-93d6-40dc-bcff-14d57181f6a5",
        "next_max_id": "cbe13d4cab0d410a867bbb6db2f21a29",
        "has_more": true,
        "auto_load_more_enabled": true,
        "grid_post_click_experience": "contextual",
        "topic_status": -1,
        "reels_max_id": "cbe13d4cab0d410a867bbb6db2f21a29",
        "has_more_reels": true,
        "reels_page_index": null,
        "autoplay_type": "single"
      },
      "status": "ok"
    }
  ]
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-track){ target=_blank }
