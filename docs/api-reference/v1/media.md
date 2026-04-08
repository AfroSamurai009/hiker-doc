# Media Endpoints

Get posts, reels, likes, comments, and media details.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/media/by/code`](#get-v1mediabycode) | [`/v1/media/by/id`](#get-v1mediabyid) | [`/v1/media/by/url`](#get-v1mediabyurl) | [`/v1/media/code/from/pk`](#get-v1mediacodefrompk) | [`/v1/media/comments`](#get-v1mediacomments) | [`/v1/media/comments/chunk`](#get-v1mediacommentschunk) | [`/v1/media/download/photo`](#get-v1mediadownloadphoto) | [`/v1/media/download/photo/by/url`](#get-v1mediadownloadphotobyurl) | [`/v1/media/download/video`](#get-v1mediadownloadvideo) | [`/v1/media/download/video/by/url`](#get-v1mediadownloadvideobyurl) | [`/v1/media/insight`](#get-v1mediainsight) | [`/v1/media/likers`](#get-v1medialikers) | [`/v1/media/oembed`](#get-v1mediaoembed) | [`/v1/media/pk/from/code`](#get-v1mediapkfromcode) | [`/v1/media/pk/from/url`](#get-v1mediapkfromurl) | [`/v1/media/user`](#get-v1mediauser)

---

### GET /v1/media/by/code

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/by/code?code=DRqAYKuAIUx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_by_code_v1(code="DRqAYKuAIUx")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/code",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"code": "DRqAYKuAIUx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/by/code?code=DRqAYKuAIUx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "3776832898280228145",
  "id": "3776832898280228145_787132",
  "code": "DRqAYKuAIUx",
  "taken_at": "2025-11-29T22:00:31Z",
  "taken_at_ts": 1764453631,
  "media_type": 2,
  "product_type": "clips",
  "thumbnail_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFNzG35&_nc_oc=AdplF-PD1RhLkRXYKeGgnzRUi3Rn8Q4KOXBxPFzbSK8HA_KvEK8IOQJTlQvo7-P8JGY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&_nc_ss=7a3ba&oh=00_Af0VkeB2sLNPmzjvPjG03urNn2c9-hZC87NwkqHpxYLIYw&oe=69DC3E7E",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFcgo5wX0wM5DUb9bTFbfqnaeFaSuWsxyWsjWE1hhLfqppeS9pcMdxY-rVzhDBn2sg&_nc_ohc=XbeNvhLXv28Q7kNvwEWvhSV&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3KkGVXsdluxYIn_H6hXZDMZRA-XzRd0pI2rX2-J-HYhA&oe=69DC51E9&_nc_sid=fc8dfb",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135429,
  "play_count": 2866120,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwFHvczA&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2CH9jD1ZcpiykjYSPYicLzpa3p-CaKj-MZIoFa4amQaA&oe=69D86FAF",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740,
        83610
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFNzG35&_nc_oc=AdplF-PD1RhLkRXYKeGgnzRUi3Rn8Q4KOXBxPFzbSK8HA_KvEK8IOQJTlQvo7-P8JGY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&_nc_ss=7a3ba&oh=00_Af0VkeB2sLNPmzjvPjG03urNn2c9-hZC87NwkqHpxYLIYw&oe=69DC3E7E",
      "width": 750,
      "is_spatial_image": false
    }
  ],
  "video_versions": [
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 101,
      "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwFHvczA&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2CH9jD1ZcpiykjYSPYicLzpa3p-CaKj-MZIoFa4amQaA&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 102,
      "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwFHvczA&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2CH9jD1ZcpiykjYSPYicLzpa3p-CaKj-MZIoFa4amQaA&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 103,
      "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwFHvczA&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2CH9jD1ZcpiykjYSPYicLzpa3p-CaKj-MZIoFa4amQaA&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    }
  ],
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
      "best_audio_cluster_id": "807850148748818"
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
      "is_reuse_allowed": false,
      "mashup_type": null,
      "mashups_allowed": false,
      "mashups_allowed_for_carousel": false,
      "non_privacy_filtered_mashups_media_count": 0,
      "privacy_filtered_mashups_media_count": null,
      "original_media": null
    },
    "merchandising_pill_info": null,
    "music_canonical_id": "18539901727003707",
    "music_info": null,
    "nux_info": null,
    "original_sound_info": {
      "allow_creator_to_rename": true,
      "audio_asset_id": 25124554117202919,
      "attributed_custom_audio_asset_id": null,
      "can_remix_be_shared_to_fb": true,
      "can_remix_be_shared_to_fb_expansion": true,
      "dash_manifest": "",
      "duration_in_ms": 22313,
      "formatted_clips_media_count": null,
      "hide_remixing": false,
      "is_audio_automatically_attributed": false,
      "is_eligible_for_audio_effects": true,
      "is_eligible_for_vinyl_sticker": true,
      "is_explicit": false,
      "is_original_audio_download_eligible": false,
      "is_reuse_disabled": true,
      "is_xpost_from_fb": false,
      "music_canonical_id": null,
      "oa_owner_is_music_artist": false,
      "original_audio_subtype": "default",
      "original_audio_title": "Original audio",
      "original_media_id": 3776832898280228145,
      "progressive_download_url": "N/A",
      "should_mute_audio": false,
      "time_created": 1764453634,
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
        "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFcgo5wX0wM5DUb9bTFbfqnaeFaSuWsxyWsjWE1hhLfqppeS9pcMdxY-rVzhDBn2sg&_nc_ohc=XbeNvhLXv28Q7kNvwEWvhSV&_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3KkGVXsdluxYIn_H6hXZDMZRA-XzRd0pI2rX2-J-HYhA&oe=69DC51E9&_nc_sid=fc8dfb"
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
  "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663946\" FBManifestIdentifier=\"FpTts50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZhojR4r/Q2Y0D0qP4j7HP7gTc7biv2tL1BNy48a7NxpAFnoq59pqbxwX8q/bF7erMBcjV6ur59fAH1O2YhM2R5woiGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABaCAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1563973005025935v\" bandwidth=\"337669\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"941843\" FBPlaybackResolutionMos=\"0:100,360:29.3,480:28.4,720:29.1,1080:31.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:70.9,480:62.6,720:50.4,1080:39.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN6p1XA_FXFLkUVYTtE8Zwx7keoWfwDMyx-B_QxL4pXgZeg8McEumkwF6WDJ4fnzDnBOTY9wUJL7oCRtGW6qjDxoh6M3Qq7Su4omI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=BfloUU35i64Q7kNvwFy-0BX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjMzNzY2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3_1M9VvNSKPjdU-z0zHoWgyDQAZ9xZ74a1R2aZXGIHgQ&amp;oe=69DC3392</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-14042\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-89181\" FBFirstSegmentRange=\"891-165373\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"165374-688020\" FBPrefetchSegmentRange=\"891-165373\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1443772230413870v\" bandwidth=\"509752\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1421827\" FBPlaybackResolutionMos=\"0:100,360:40.4,480:38,720:37.2,1080:38.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:80.5,480:73.6,720:62.8,1080:52.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO03YPWFT70GHasKStspUo-nCsZakOgI61xyRI5dJ6BZRsyp4lBEZKTh7qJH33vHao8lA7Gz8jHRXP-xoDvVyNDrlzf18WIgj_ye2E.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=O1KjHuo6qEEQ7kNvwF-o99L&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUwOTc1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3fWMDMXGP-rD0S0AFLmawvmLjcEztvmhulCiXmP9sftg&amp;oe=69DC5A86</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-19700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-153929\" FBFirstSegmentRange=\"891-284632\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"284633-1049599\" FBPrefetchSegmentRange=\"891-284632\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3041551559367530v\" bandwidth=\"722308\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2014698\" FBPlaybackResolutionMos=\"0:100,360:51.1,480:47.8,720:45.4,1080:45.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.5,480:81.3,720:72.1,1080:62.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPSpcAxu8AB6FoUvT9edmiINl_OKU0kxsELupA-W7mtlP9_ucOO0LmcFcGoF7nFLPaLtxp6SODqMd31GQF9E68R4xCcOv91YV_Za6U.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=D5k1RwfW4qsQ7kNvwF8ZMll&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjcyMjMwOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1niu6dpbEo02N8hbsesU1yB8ybAkF7juar7it4q5hY3g&amp;oe=69DC3677</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-28550\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-246143\" FBFirstSegmentRange=\"891-439881\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"439882-1486392\" FBPrefetchSegmentRange=\"891-439881\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1576336420162302v\" bandwidth=\"989685\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2760477\" FBPlaybackResolutionMos=\"0:100,360:60.9,480:57,720:54.1,1080:53.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91,480:87.2,720:79.7,1080:71.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNWawONH_0ykNRhgXYD5USnUS-2JcDjQ0cKPtzUQ4bmPrDRMRJgACUHEnYvSCFWgDRdksntOheWe4DkpraAAYpYXQpEyt7yK9nS-5A.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=JGpaa8RbgzYQ7kNvwFlpGVf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjk4OTY4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1-EL0lLDkqYgvOHPfSCYCAqSSMWK3SHgdgNGIc6P67bg&amp;oe=69DC6548</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-36175\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-368341\" FBFirstSegmentRange=\"891-638853\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"638854-2015969\" FBPrefetchSegmentRange=\"891-638853\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1384606506359662v\" bandwidth=\"1369954\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3821143\" FBPlaybackResolutionMos=\"0:100,360:69.5,480:65.5,720:61.7,1080:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.2,480:91.7,720:86.3,1080:79.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHjz86uKmkZFb6AfTAuNXhaCR5cY5lsEh1FSO9m1gsCdbf2BQ8JMp-g6pMIlhKv6fDPKpemYtUf_SuYjLt-9p7iIGYj7iVdOv9W4k.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=waJfS4YiB8AQ7kNvwE1TGO_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzNjk5NTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1DEJ0xtSXeqjWVxC2M5L27sS1t1FezkaHlh7JxXh6ccA&amp;oe=69DC61BA</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-46923\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-542605\" FBFirstSegmentRange=\"891-915699\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"915700-2726908\" FBPrefetchSegmentRange=\"891-915699\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1369156268001513v\" bandwidth=\"1822480\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"5083349\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:71.6,720:67.7,1080:65.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:94.5,720:90.4,1080:85.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMvyH-MQjdKfi00Fl5WSSH-1UKJzwFI8zT_5r_axCxb1zBFH7oejYKyu0sw6aikisn4kwP7Dvea3yfEnFbu9mGB_M3KNvNh7vkIxnY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=cgpTCsrJnfQQ7kNvwHUSlDD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE4MjI0ODAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af28c3Y4yNvymLrXYvfBq5FOmYObCBe_Cq8vxFqgxVZ2Nw&amp;oe=69DC6661</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-58146\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-759235\" FBFirstSegmentRange=\"891-1253416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1253417-3555514\" FBPrefetchSegmentRange=\"891-1253416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"2218641838658916v\" bandwidth=\"2563525\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"7150307\" FBPlaybackResolutionMos=\"0:100,360:81.3,480:77.1,720:73.4,1080:70.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.9,720:94.1,1080:90.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6gX6iet6wVi2vwiQzpMYKnTkzyIOrnIhhWCeS_HxxTf5k1JEyxtDXBZl3W1nkz-gCcy90W_Uonp2gPqR_zfKL3rzkQ3beNg1DNR0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=ZhVzyNU6d_IQ7kNvwFhljua&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI1NjM1MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3BGXkVfmA4JFl5JHxj9tOjhSi3_lf7wGCPYa5rvrg5GA&amp;oe=69DC6663</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-74586\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-1107880\" FBFirstSegmentRange=\"891-1794122\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1794123-4835105\" FBPrefetchSegmentRange=\"891-1794122\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"874552045098052a\" bandwidth=\"46857\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46857\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"131698\" FBPaqMos=\"86.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m86/AQPkB7GmtjggjHEJa-kd2XK21HSs5MPOBh8Kn_V_b6gCkSbQo9RxM5qstTSXAhy-_70SQiuAW02OQtBnYlPkvoo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=ZSfr4AA8_vgQ7kNvwF8JPkT&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ3MjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=BMZ1_-ZZqTqODGPdsIgcRg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Cee0gkrOFjoeNGsmemQdHu-oukkIJuWWUGGOKbRWZFQ&amp;oe=69D859DB</BaseURL><SegmentBase indexRange=\"824-999\" timescale=\"48000\" FBMinimumPrefetchRange=\"1000-1360\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1000-14536\" FBFirstSegmentRange=\"1000-12223\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"12224-22571\" FBPrefetchSegmentRange=\"1000-22571\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
  "like_and_view_counts_disabled": false,
  "coauthor_producers": [],
  "is_paid_partnership": false
}
```

</details>

---

### GET /v1/media/by/id

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/by/id?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_by_id_v1(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/by/id?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "3776832898280228145",
  "id": "3776832898280228145_787132",
  "code": "DRqAYKuAIUx",
  "taken_at": "2025-11-29T22:00:31Z",
  "taken_at_ts": 1764453631,
  "media_type": 2,
  "product_type": "clips",
  "thumbnail_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwExc08O&_nc_oc=AdpGewr5QEJby3AiN2Ri18KaYIJmJGgFX1e0fx9ve2XNYKjyoBHyeTrCxz9G42HeOck&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&_nc_ss=7a3ba&oh=00_Af1K8VpSKzokEaXzhCCjPiCd-_TBWwfUYGrsfoLNnkfgIQ&oe=69DC3E7E",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEq9mHyDon2akJVcpG4wm9ruwo1QxcTnvij-kB2fJOYMTFhYcTyxZ6WW-F2G7XxOdY&_nc_ohc=XbeNvhLXv28Q7kNvwEpAgkz&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3qsvbgcRQymVMXkz6krW2j1mIugktrvvr6xlqypnl3dg&oe=69DC51E9&_nc_sid=fc8dfb",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135429,
  "play_count": 2866120,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2P1AW0iaPyXrCkqj3QCvbs2wVCVXcpeQitGz3hTNQtvA&oe=69D86FAF",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740,
        83610
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwExc08O&_nc_oc=AdpGewr5QEJby3AiN2Ri18KaYIJmJGgFX1e0fx9ve2XNYKjyoBHyeTrCxz9G42HeOck&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&_nc_ss=7a3ba&oh=00_Af1K8VpSKzokEaXzhCCjPiCd-_TBWwfUYGrsfoLNnkfgIQ&oe=69DC3E7E",
      "width": 750,
      "is_spatial_image": false
    }
  ],
  "video_versions": [
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 101,
      "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2P1AW0iaPyXrCkqj3QCvbs2wVCVXcpeQitGz3hTNQtvA&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 102,
      "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2P1AW0iaPyXrCkqj3QCvbs2wVCVXcpeQitGz3hTNQtvA&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 103,
      "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2P1AW0iaPyXrCkqj3QCvbs2wVCVXcpeQitGz3hTNQtvA&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    }
  ],
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
      "best_audio_cluster_id": "807850148748818"
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
    "content_appreciation_info": {
      "enabled": false,
      "entry_point_container": null
    },
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
    "music_canonical_id": "18539901727003707",
    "music_info": null,
    "nux_info": null,
    "original_sound_info": {
      "allow_creator_to_rename": true,
      "audio_asset_id": 25124554117202919,
      "attributed_custom_audio_asset_id": null,
      "can_remix_be_shared_to_fb": true,
      "can_remix_be_shared_to_fb_expansion": true,
      "dash_manifest": "",
      "duration_in_ms": 22313,
      "formatted_clips_media_count": null,
      "hide_remixing": false,
      "is_audio_automatically_attributed": false,
      "is_eligible_for_audio_effects": true,
      "is_eligible_for_vinyl_sticker": true,
      "is_explicit": false,
      "is_original_audio_download_eligible": false,
      "is_reuse_disabled": true,
      "is_xpost_from_fb": false,
      "music_canonical_id": null,
      "oa_owner_is_music_artist": false,
      "original_audio_subtype": "default",
      "original_audio_title": "Original audio",
      "original_media_id": 3776832898280228145,
      "progressive_download_url": "N/A",
      "should_mute_audio": false,
      "time_created": 1764453634,
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
        "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEq9mHyDon2akJVcpG4wm9ruwo1QxcTnvij-kB2fJOYMTFhYcTyxZ6WW-F2G7XxOdY&_nc_ohc=XbeNvhLXv28Q7kNvwEpAgkz&_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3qsvbgcRQymVMXkz6krW2j1mIugktrvvr6xlqypnl3dg&oe=69DC51E9&_nc_sid=fc8dfb"
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
  "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663944\" FBManifestIdentifier=\"FpDts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtozhmaSP8rACovXRl+ao3wKeuubV3cyWBOqzvt7VgoEFzrqng86IvQXsmrLM3p3MBZrPsJvI77AGip+AguPQnQfEsIDkwaHqB9yS8+rZ7tIInuvr86jMyQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2ggIUABIUAgA=\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwFcSRLc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3szRCNl1ybxclMNrmr4cScSRL7dhi0EBEeD18BZ_Jezg&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=bCouttTbvR0Q7kNvwHnZk01&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0PVVaPmfh5rqeSUKE4cH042TfgvcHxzmTdpeoNU0_uZg&amp;oe=69DC6069</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwHkxtuX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Sd6D3YTugfIP64Xy7tDy5AaZKqGV8g5HpANZdtfZeGQ&amp;oe=69DC5940</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwETlGZ6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af04SOhkd_ghQXw2VO9HI8r2mL10nU50_68BhJIQ0QB-uA&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwGC73yn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af201eayuqLVIAGGqEAwJcGswnHUwnw9LX52VZtaOju4Rw&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwGfm6hH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3rNaXyWq_m476ydMirva5nB6_y9kO7E6MB4E2mgoJ9EA&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwFG4g10&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2X6apl4BcWapYc_KU_Y4oZG96KkwGhnUfPQuvxadNGIw&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwGp5mTY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3TFyuuX3Sh56Yqb76UTpITsDOWbkbwEWAoVFSl3sg3HQ&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-2.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwF-JKa8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3j8qdN-Us2lYb9ebtBo4efdwl3Qvw1iP-G1PARTbVaNg&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwGtAQKR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Z_cvG5aGaxT_iguxH0Bx5h8FWgWHEg-JuSSE-blxGRw&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwEhHuDg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0iQu0ERNY_KFOgL6CDw7sg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af20se3y4fMPP7eIcBLfvV51yphTTgZ9qfkSeUWYPPihgA&amp;oe=69DC5283</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
  "like_and_view_counts_disabled": false,
  "coauthor_producers": [],
  "is_paid_partnership": false
}
```

</details>

---

### GET /v1/media/by/url

Get media object. Returns a Media object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_by_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "3776832898280228145",
  "id": "3776832898280228145_787132",
  "code": "DRqAYKuAIUx",
  "taken_at": "2025-11-29T22:00:31Z",
  "taken_at_ts": 1764453631,
  "media_type": 2,
  "product_type": "clips",
  "thumbnail_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwGcrK0p&_nc_oc=Adp8zu6rGquRbfea6CCNRvK5HWx_C4iO01fV89WrPGzoZg5sdFOGV3SZ56-u9qQUFuA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&_nc_ss=7a3ba&oh=00_Af290HtUjR9TlPaBdnGIiayEY8djrhkaoHO7pyN6KyJRew&oe=69DC3E7E",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFecMKTl2uiYU56XCxZZNJqaI8ZPjAkmsJZvCyAJnWj3p5tov-jq7Aas4OP77XFnR4&_nc_ohc=XbeNvhLXv28Q7kNvwH8DFwT&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2msyZvuTbRQLsoHubskKc5-6oxwE8z2hSJ0owqwXrtMA&oe=69DC51E9&_nc_sid=fc8dfb",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135429,
  "play_count": 2866120,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHdeFnY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1i7NjaFvq70z-gaGu0Ki42QuG4pRYKqHOI5qfTIFE_Fw&oe=69D86FAF",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740,
        83610
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwGcrK0p&_nc_oc=Adp8zu6rGquRbfea6CCNRvK5HWx_C4iO01fV89WrPGzoZg5sdFOGV3SZ56-u9qQUFuA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&_nc_ss=7a3ba&oh=00_Af290HtUjR9TlPaBdnGIiayEY8djrhkaoHO7pyN6KyJRew&oe=69DC3E7E",
      "width": 750,
      "is_spatial_image": false
    }
  ],
  "video_versions": [
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 101,
      "url": "https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHdeFnY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1i7NjaFvq70z-gaGu0Ki42QuG4pRYKqHOI5qfTIFE_Fw&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 102,
      "url": "https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHdeFnY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1i7NjaFvq70z-gaGu0Ki42QuG4pRYKqHOI5qfTIFE_Fw&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 103,
      "url": "https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHdeFnY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1i7NjaFvq70z-gaGu0Ki42QuG4pRYKqHOI5qfTIFE_Fw&oe=69D86FAF",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    }
  ],
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
      "best_audio_cluster_id": "807850148748818"
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
      "is_reuse_allowed": false,
      "mashup_type": null,
      "mashups_allowed": false,
      "mashups_allowed_for_carousel": false,
      "non_privacy_filtered_mashups_media_count": 0,
      "privacy_filtered_mashups_media_count": null,
      "original_media": null
    },
    "merchandising_pill_info": null,
    "music_canonical_id": "18539901727003707",
    "music_info": null,
    "nux_info": null,
    "original_sound_info": {
      "allow_creator_to_rename": true,
      "audio_asset_id": 25124554117202919,
      "attributed_custom_audio_asset_id": null,
      "can_remix_be_shared_to_fb": true,
      "can_remix_be_shared_to_fb_expansion": true,
      "dash_manifest": "",
      "duration_in_ms": 22313,
      "formatted_clips_media_count": null,
      "hide_remixing": false,
      "is_audio_automatically_attributed": false,
      "is_eligible_for_audio_effects": true,
      "is_eligible_for_vinyl_sticker": true,
      "is_explicit": false,
      "is_original_audio_download_eligible": false,
      "is_reuse_disabled": true,
      "is_xpost_from_fb": false,
      "music_canonical_id": null,
      "oa_owner_is_music_artist": false,
      "original_audio_subtype": "default",
      "original_audio_title": "Original audio",
      "original_media_id": 3776832898280228145,
      "progressive_download_url": "N/A",
      "should_mute_audio": false,
      "time_created": 1764453634,
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
        "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFecMKTl2uiYU56XCxZZNJqaI8ZPjAkmsJZvCyAJnWj3p5tov-jq7Aas4OP77XFnR4&_nc_ohc=XbeNvhLXv28Q7kNvwH8DFwT&_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2msyZvuTbRQLsoHubskKc5-6oxwE8z2hSJ0owqwXrtMA&oe=69DC51E9&_nc_sid=fc8dfb"
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
  "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663947\" FBManifestIdentifier=\"Fpbts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtozhmaSP8rACovXRl+ao3wKeuubV3cyWBOqzvt7VgoEFzrqng86IvQXsmrLM3p3MBZrPsJvI77AGip+AguPQnQfEsIDkwaHqB9yS8+rZ7tIInuvr86jMyQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyIsGRgFbGlnaHQAFoICFAASFAIA\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwHvLMkX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1-czxUx988eVW4_-BTrvggvyD9wZT26b6YmH6q3Pdt0A&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-ord5-3.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-3.cdninstagram.com&amp;_nc_ohc=bCouttTbvR0Q7kNvwFzAMGV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3wfc3ABI4X2z8xpN28rTpmQW2Bc6G0VEc7zxkal0uXYw&amp;oe=69DC6069</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ord5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwHc-y2H&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0GCgHAkVZy1tMKWLBc4Z_EX0x3mMlNkC4uGospedO4Hw&amp;oe=69DC5940</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwFJvMvW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3znzTAh4-sdX0aZXNknNP_SN8pYM0WZTMof5wPsOazCQ&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwGdKvf5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2L36JQpSs2uV4UDLcINxcyLVCrw60SACOuvs8x9xyGog&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-ord5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-1.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwFMKKSp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0rbRXdGRD9M_ed_h9EGx2y0t5KyqWjLds0NAspbw-zZw&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-ord5-3.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-3.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwHK4geL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1ntpdZ_NFdKJQEdeaOO71lnaMiuGztxopKTb1z7RAPXg&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ord5-3.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-3.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwFjyId8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2TPDhwjq6kVa4GBmNwV55O5uGF77gJlAMgcqjhQ9DAew&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ord5-3.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-3.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwGPv5RM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3KHIRkaQz0Z2sdKuZObTQYO1CiJICK4ZPeLL3F8Dvo6A&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ord5-3.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-3.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwHhtOYI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0E5G0gScJQ1Nq4FQ775fQAmzSxNQzvGNZlEM4Oxe95fw&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ord5-2.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwEuTvWz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=-Xzg-qXfwloqdvTd4RJymQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af27pc6INvzHRsDlWKNTZ5fawGXDnOXaXYCKfv-he7Rj4w&amp;oe=69DC5283</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
  "like_and_view_counts_disabled": false,
  "coauthor_producers": [],
  "is_paid_partnership": false
}
```

</details>

---

### GET /v1/media/code/from/pk

Get media code from pk

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pk` | string | Yes | Pk |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/code/from/pk?pk=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_code_from_pk_v1(pk="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/code/from/pk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"pk": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/code/from/pk?pk=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
"DRqAYKuAIUx"
```

</details>

---

### GET /v1/media/comments

Get comments on a media. Returns a list of Comment objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/comments?id=3776832898280228145"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/comments",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/comments?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17992046705899459",
    "text": "😍😍😍amazing",
    "user": {
      "pk": "1791264033",
      "id": "1791264033",
      "username": "victoria.mvr",
      "full_name": "Victoria💫",
      "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/659112133_18577992958032034_8453764196225005035_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMVASSeiOOcOlgBCAOs16Bq-zVF1bmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy44NzIuQzMifQ%3D%3D&_nc_ohc=DnA_JPkhzXwQ7kNvwFpi1nE&_nc_oc=AdpDwYHHgIShRxmA2H2ul_rJaKbj0BcYaMWcxGTzJIfEI6ckGBD-1O2c6QFWrY3nPcc&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=QBdplyWd-AyE9yxJYF5tvw&_nc_ss=7a3ba&oh=00_Af0HCnCFsfxf6zFdnrJpCAHG_Mm35L1p65i80RzaEvw6mA&oe=69DC5CBD",
      "profile_pic_url_hd": null,
      "is_private": true,
      "is_verified": false
    },
    "created_at_utc": "2025-11-29T22:20:18Z",
    "content_type": "comment",
    "status": "Active",
    "has_liked": false,
    "like_count": 4
  },
  {
    "pk": "17915190762228930",
    "text": "Nature is brilliantly beautiful!🤩",
    "user": {
      "pk": "1393016141",
      "id": "1393016141",
      "username": "scubalover14",
      "full_name": "Karen",
      "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/10514103_680727235334784_933888781_a.jpg?stp=dst-jpg_e0_tt6&_nc_cat=107&ig_cache_key=GLduoACAEg0pHmsCAA0DqjcAAAAAYUULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=C0bKK8aX6HUQ7kNvwH0Hhjd&_nc_oc=Adqbml8YaTASl56pfqa5cUHaACIyxJIbtLgNeZaJh0wSsmMiXxSZBC_aBctRLFYlSpw&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af2KfkvpPePJoqeTT6h2s6ftW6bTPa493zn9yn_pUn0Pdw&oe=69DC49E1",
      "profile_pic_url_hd": null,
      "is_private": true,
      "is_verified": false
    },
    "created_at_utc": "2025-11-29T22:36:22Z",
    "content_type": "comment",
    "status": "Active",
    "has_liked": false,
    "like_count": 66
  },
  {
    "pk": "18178774921320754",
    "text": "God bless our planet 💚🙏",
    "user": {
      "pk": "5646775780",
      "id": "5646775780",
      "username": "adriana.prn.71",
      "full_name": "Adriana Peñaloza",
      "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-19/540685604_18397468009191781_5796551439984130253_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=103&ig_cache_key=GCQ1OiBlWXRRZlxBAM14iL7SfHFQbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=Y17pObw-puwQ7kNvwEDNJz4&_nc_oc=Adp19M9SX8zX-jaaSjURCwn8BBzy_ju7CAscRYx2wU_J5bW0HzeT8vM1XSQrfSyjthI&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_gid=QBdplyWd-AyE9yxJYF5tvw&_nc_ss=7a3ba&oh=00_Af1DGob3Z2evgga3623OIR7CaAKDJKD6dfpdEzNBMXC4Hg&oe=69DC5E72",
      "profile_pic_url_hd": null,
      "is_private": true,
      "is_verified": false
    },
    "created_at_utc": "2025-11-30T00:38:59Z",
    "content_type": "comment",
    "status": "Active",
    "has_liked": false,
    "like_count": 35
  }
]
```

</details>

---

### GET /v1/media/comments/chunk

Get comments on a media. Returns a list of Comment objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |
| `min_id` | string | No | Min Id |
| `max_id` | string | No | Max Id |
| `can_support_threading` | boolean | No | Can Support Threading |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/comments/chunk?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_chunk_v1(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/comments/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/comments/chunk?id=3776832898280228145",
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
      "pk": "17915190762228930",
      "text": "Nature is brilliantly beautiful!🤩",
      "user": {
        "pk": "1393016141",
        "id": "1393016141",
        "username": "scubalover14",
        "full_name": "Karen",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/10514103_680727235334784_933888781_a.jpg?stp=dst-jpg_e0_tt6&_nc_cat=107&ig_cache_key=GLduoACAEg0pHmsCAA0DqjcAAAAAYUULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=C0bKK8aX6HUQ7kNvwGIQg_P&_nc_oc=AdrUx22jb49DJSPQeRRoEi3nqeWS59Dp0-60BfqPqOzB_TA9j_o8bU_H1yzQ1RisyH8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3JiZ8gxSkWvMVMOLqLNcUeK1U9eDtRpLPq-8w68c40cg&oe=69DC49E1",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false
      },
      "created_at_utc": "2025-11-29T22:36:22Z",
      "content_type": "comment",
      "status": "Active",
      "has_liked": false,
      "like_count": 66
    },
    {
      "pk": "17992046705899459",
      "text": "😍😍😍amazing",
      "user": {
        "pk": "1791264033",
        "id": "1791264033",
        "username": "victoria.mvr",
        "full_name": "Victoria💫",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/659112133_18577992958032034_8453764196225005035_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMVASSeiOOcOlgBCAOs16Bq-zVF1bmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy44NzIuQzMifQ%3D%3D&_nc_ohc=DnA_JPkhzXwQ7kNvwHCcAPN&_nc_oc=AdqO3tnSLYkAPZxf8A3XDhc_kwANbhyge_EXvF08b0uPZsJpUD4O29YHJIAa8PQorgk&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=opr7Sh11RSso2as_E4wvkQ&_nc_ss=7a3ba&oh=00_Af0Q__FBKurhodXXSOXbCb9FLfq4t2XYMyBKy3WHJQqeVA&oe=69DC5CBD",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false
      },
      "created_at_utc": "2025-11-29T22:20:18Z",
      "content_type": "comment",
      "status": "Active",
      "has_liked": false,
      "like_count": 4
    },
    {
      "pk": "18053905025662507",
      "text": "Thank you for the 0:22 second chill and calm :-)\nGreetings",
      "user": {
        "pk": "1741252659",
        "id": "1741252659",
        "username": "meadow.full.of.daisies",
        "full_name": "𝕾𝖆𝖗𝖎𝖓𝖆",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/287457604_1180575629387445_3767985181133999870_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=102&ig_cache_key=GERBIhG1JgUvujEEAP6ObQCPkko0bkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=zqTYFkjEg6sQ7kNvwHs89KE&_nc_oc=AdojklIKWzItZBDI7TnBxNBlYns0llTD0AKQ_9IgIjcjYklLD8joHeeKd9HJGdO5CRw&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af1RhwfSR_UVOVT4ngL552GAy9x-gdCcgJBXtlpeJ7WDuw&oe=69DC4393",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "created_at_utc": "2025-11-29T22:07:39Z",
      "content_type": "comment",
      "status": "Active",
      "has_liked": false,
      "like_count": 194
    }
  ],
  "IntcImNhY2hlZF9jb21tZW50c19jdXJzb3JcIjpcIjE4MzMzOTY0NTQ2MjE1MjM1XCIsXCJiaWZpbHRlcl90b2tlblwiOlwiR2dZWWdRRUFkVzNGVnRDTlB3RENUSGRseGFVX0FNUDNyOUNyNno4QUtfN2NVLTRqUUFCVHhreWRYbEJBQURJWm85MV9sVUFBVnVUc1pFaVZQd0FoQ21GaW0zMUFBTjYtN3E5bXh6OEF1d2lnNEd3YlFBRFdDUWJvTkJCQUFDNTl5V25NZWo4QVdpNGVwdjFBUVFDNFUwTTBkb3hBQUQ2VkotbTZlRUVBSXJIVTVrZFJRQUFBXCJ9Ig==",
  null
]
```

</details>

---

### GET /v1/media/download/photo

Download photo using media pk

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/download/photo?id=3776832898280228145"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/photo",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/download/photo?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/media/download/photo/by/url

Download photo using URL

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/download/photo/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/photo/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/download/photo/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/media/download/video

Download video using media pk

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/download/video?id=3776832898280228145"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/video",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/download/video?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/media/download/video/by/url

Download video using URL

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/download/video/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/video/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/download/video/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/media/insight

Get media insight

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/insight?media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_insight_v1(media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/insight",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/insight?media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "id": "18065011277571522",
  "creation_time": 1764453631,
  "has_product_tags": false,
  "instagram_media_id": "3776832898280228145",
  "instagram_media_owner_id": "787132",
  "instagram_actor": {
    "instagram_actor_id": "503011999733264",
    "id": "17841400573960012"
  },
  "inline_insights_node": null,
  "display_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=100&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwHGCE4Z&_nc_oc=AdqZ5-0SRTHKPhOO2fxaEAC3R76X8g6pXWcdUU2YyKYwKFWIkCB8uVgge52kP4Bcu9E&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=9KHEFXZDAOf8Q-jHgda-2g&_nc_ss=7a39b&oh=00_Af3QkBkLvswljaxQHYBIGiUr86CB_dy1kDgh3lHqhGsc0w&oe=69DC3E7E",
  "instagram_media_type": "VIDEO",
  "image": {
    "height": 640,
    "width": 360
  },
  "comment_count": 485,
  "like_count": 135429,
  "save_count": null,
  "ad_media": null,
  "organic_instagram_media_id": "3776832898280228145",
  "shopping_outbound_click_count": null,
  "shopping_product_click_count": null,
  "shopping_product_insights": {
    "shopping_product_by_tag_click_count": [],
    "shopping_product_by_tag_outbound_click_count": []
  }
}
```

</details>

---

### GET /v1/media/likers

Get user's likers. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/likers?id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_likers_v1(id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/likers",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/likers?id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "1469722832",
    "id": "1469722832",
    "username": "jorge10.ds",
    "full_name": "🅙orge Delgado 🦖",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.2885-19/324069253_5836767539705305_7097116477300814733_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGkjT-72wQqXvnycFIE-NbN2C4iMETmAU4q0lBfLOyvmKQ2Op_sUH5KuWI1Q3_fVe8&_nc_ohc=hKoACuZrKRgQ7kNvwE8ddlG&_nc_gid=wHdQtCudBnO3Ks_JB0VJBA&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GIXnUBPZNddXgrwUAI0zFn-VBX5ibkULAAAB1501500j-ccb7-5&oh=00_Af1I94dLBMd3h933mrv180oojntjykOcKjPNmNfLnChkDA&oe=69DC5D58&_nc_sid=bc52df",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "48158574428",
    "id": "48158574428",
    "username": "only_looking_at_fashionpeople",
    "full_name": "",
    "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/656236846_18037016978606429_8176123182175805432_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gGkjT-72wQqXvnycFIE-NbN2C4iMETmAU4q0lBfLOyvmKQ2Op_sUH5KuWI1Q3_fVe8&_nc_ohc=8hgiqdDnz8cQ7kNvwGBa5Vn&_nc_gid=wHdQtCudBnO3Ks_JB0VJBA&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GC5hHSddSdFFkhRAAPjfbBm3bHdxbmNDAQAB1501500j-ccb7-5&oh=00_Af1ZceLpB1tfNY010hMsUB4I2SdDbN6Ff31r5nVrvXGIPQ&oe=69DC48D9&_nc_sid=bc52df",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "77145556919",
    "id": "77145556919",
    "username": "xin.wei.chang261891",
    "full_name": "張心瑋",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/633458779_17865824814572920_9097672624501223816_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gGkjT-72wQqXvnycFIE-NbN2C4iMETmAU4q0lBfLOyvmKQ2Op_sUH5KuWI1Q3_fVe8&_nc_ohc=lxk5Sn6BeMsQ7kNvwHw61as&_nc_gid=wHdQtCudBnO3Ks_JB0VJBA&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GFvQwSV4JbF933g-AIjxMOoMbUF_bmNDAQAB1501500j-ccb7-5&oh=00_Af2QX18TKOLkK7PWhyNXBtGU_8YEYMZCUY0lCxPDokeWTQ&oe=69DC4D0A&_nc_sid=bc52df",
    "is_private": false,
    "is_verified": true
  }
]
```

</details>

---

### GET /v1/media/oembed

Return info about media and user from post URL

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/oembed?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_oembed_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/oembed",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/oembed?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "title": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "author_name": "natgeo",
  "author_url": "https://www.instagram.com/natgeo",
  "author_id": "787132",
  "media_id": "3776832898280228145_787132",
  "provider_name": "Instagram",
  "provider_url": "https://www.instagram.com",
  "type": "rich",
  "width": 658,
  "height": null,
  "html": "<blockquote class=\"instagram-media\" data-instgrm-captioned data-instgrm-permalink=\"https://www.instagram.com/reel/DRqAYKuAIUx/?utm_source=ig_embed&amp;utm_campaign=loading\" data-instgrm-version=\"14\" style=\" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);\"><div style=\"padding:16px;\"> <a href=\"https://www.instagram.com/reel/DRqAYKuAIUx/?utm_source=ig_embed&amp;utm_campaign=loading\" style=\" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;\" target=\"_blank\"> <div style=\" display: flex; flex-direction: row; align-items: center;\"> <div style=\"background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;\"></div> <div style=\"display: flex; flex-direction: column; flex-grow: 1; justify-content: center;\"> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;\"></div> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;\"></div></div></div><div style=\"padding: 19% 0;\"></div> <div style=\"display:block; height:50px; margin:0 auto 12px; width:50px;\"><svg width=\"50px\" height=\"50px\" viewBox=\"0 0 60 60\" version=\"1.1\" xmlns=\"https://www.w3.org/2000/svg\" xmlns:xlink=\"https://www.w3.org/1999/xlink\"><g stroke=\"none\" stroke-width=\"1\" fill=\"none\" fill-rule=\"evenodd\"><g transform=\"translate(-511.000000, -20.000000)\" fill=\"#000000\"><g><path d=\"M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631\"></path></g></g></g></svg></div><div style=\"padding-top: 8px;\"> <div style=\" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;\">View this post on Instagram</div></div><div style=\"padding: 12.5% 0;\"></div> <div style=\"display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;\"><div> <div style=\"background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);\"></div> <div style=\"background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;\"></div> <div style=\"background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);\"></div></div><div style=\"margin-left: 8px;\"> <div style=\" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;\"></div> <div style=\" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)\"></div></div><div style=\"margin-left: auto;\"> <div style=\" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);\"></div> <div style=\" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);\"></div> <div style=\" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);\"></div></div></div> <div style=\"display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;\"> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;\"></div> <div style=\" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;\"></div></div></a><p style=\" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;\"><a href=\"https://www.instagram.com/reel/DRqAYKuAIUx/?utm_source=ig_embed&amp;utm_campaign=loading\" style=\" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;\" target=\"_blank\">A post shared by National Geographic (@natgeo)</a></p></div></blockquote>\n<script async src=\"//www.instagram.com/embed.js\"></script>",
  "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p640x640_sh0.08_tt6&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2gFpOWhP0H1v3-44pDYiucObaQxcweKwQae_SoCP2wT1qSil94Lakw0m8QMGnt-wJLg&_nc_ohc=hXWOKyUXNLwQ7kNvwG9mkzS&_nc_gid=nlzTEEiC8zk8ehBFgFI87w&edm=ALY_pVYBAAAA&ccb=7-5&oh=00_Af0NgObkyqD99IEm8MzX4VnG5Q8s8ePTooEw_EYyA5irPA&oe=69DC3E7E&_nc_sid=57e406",
  "thumbnail_width": 640,
  "thumbnail_height": 1137,
  "can_view": null
}
```

</details>

---

### GET /v1/media/pk/from/code

Get media pk from code

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/pk/from/code?code=DRqAYKuAIUx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_pk_from_code_v1(code="DRqAYKuAIUx")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/pk/from/code",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"code": "DRqAYKuAIUx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/pk/from/code?code=DRqAYKuAIUx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
"3776832898280228145"
```

</details>

---

### GET /v1/media/pk/from/url

Get Media pk from URL

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/pk/from/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_pk_from_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/pk/from/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/pk/from/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
"3776832898280228145"
```

</details>

---

### GET /v1/media/user

Get author of the media

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/media/user?media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_user_v1(media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/media/user",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/media/user?media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "787132",
  "id": "787132",
  "username": "natgeo",
  "full_name": "National Geographic",
  "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFd1_WACvtDRcFkyUQINt3ULkHDIJ9YFZefwHo2ofqu0GPd1NFSjTVNVD8YId7MZhI&_nc_ohc=XbeNvhLXv28Q7kNvwHVwYTQ&_nc_gid=eCFFYkFHCOVCNx6xWuRXFA&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1uT9mzdqyzcjnZvSnI0ENVa-NaggHjvk4GOiWKN3SEgg&oe=69DC51E9&_nc_sid=fc8dfb",
  "is_private": false,
  "is_verified": true
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-media){ target=_blank }
