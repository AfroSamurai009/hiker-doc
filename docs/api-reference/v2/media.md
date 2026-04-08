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
            "video_length": 22.313
          }
        }
      },
      "media_type": 2,
      "original_width": 720,
      "original_height": 1280,
      "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZTg5YjM1YmE1YmQ4NGU0NmE3YjVkNTYxY2RlZjNhNGQzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzgxMTg1MnwzNzc2ODMyODk4MjgwMjI4MTQ1fDMyMjA2NDExOTIwfDRhNDc2YzUyYmJiOTk2NGQwYzRkNGI2ZGY5Y2UxOTcxM2UzZGJlOTg3MjkyMWIxNTcxMjE0M2U0NjcyN2M5NTMifSwic2lnbmF0dXJlIjoiIn0=",
      "music_metadata": null,
      "has_tagged_users": false,
      "clips_tab_pinned_user_ids": [],
      "is_open_to_public_submission": false,
      "is_social_ufi_disabled": false,
      "timeline_pinned_user_ids": [],
      "taken_at": 1764453631,
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
      "social_context": [],
      "subscribe_cta_visible": false,
      "creative_config": null,
      "is_cutout_sticker_allowed": false,
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
      "commerce_integrity_review_decision": "",
      "is_reuse_allowed": false,
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "boost_unavailable_reason_v2": null,
      "coauthor_producers": [],
      "coauthor_producer_can_see_organic_insights": false,
      "invited_coauthor_producers": [],
      "igbio_product": null,
      "is_paid_partnership": false,
      "reshare_count": 8346,
      "ig_media_sharing_disabled": false,
      "media_repost_count": 4442,
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
            "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEss1iWvtD6oG30x9rqUuzwTKD0PaRY50-vvupOCfuuy6_TyKHxJZXKI-USEqL6XV4&_nc_ohc=XbeNvhLXv28Q7kNvwEM8ir9&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ra9G83ekKdAnZi1iigKCzP2a0u_QAbZu6bJTfiEiOIQ&oe=69DC51E9&_nc_sid=fc8dfb"
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
      "like_count": 135430,
      "top_likers": [],
      "hidden_likes_string_variant": -1,
      "caption": {
        "strong_id__": "18065011298571522",
        "bit_flags": 0,
        "created_at": 1764453632,
        "created_at_utc": 1764453632,
        "did_report_as_spam": false,
        "is_ranked_comment": false,
        "pk": "18065011298571522",
        "share_enabled": false,
        "content_type": "comment",
        "media_id": 3776832898280228145,
        "status": "Active",
        "type": 1,
        "user_id": 787132,
        "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
        "user": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "is_unpublished": false,
          "fbid_v2": 17841400573960012,
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEss1iWvtD6oG30x9rqUuzwTKD0PaRY50-vvupOCfuuy6_TyKHxJZXKI-USEqL6XV4&_nc_ohc=XbeNvhLXv28Q7kNvwEM8ir9&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ra9G83ekKdAnZi1iigKCzP2a0u_QAbZu6bJTfiEiOIQ&oe=69DC51E9&_nc_sid=fc8dfb"
        },
        "is_covered": false,
        "private_reply_status": 0,
        "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
      },
      "comment_count": 485,
      "can_view_more_preview_comments": false,
      "preview_comments": [],
      "comment_likes_enabled": true,
      "comment_inform_treatment": {
        "action_type": null,
        "should_have_inform_treatment": false,
        "text": "",
        "url": null
      },
      "is_photo_comments_composer_enabled_for_author": false,
      "hide_view_all_comment_entrypoint": true,
      "locations": [],
      "play_count": 2866120,
      "ig_play_count": 2866120,
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
      "video_duration": 22.31399917602539,
      "is_dash_eligible": 1,
      "video_versions": [
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 101,
          "url": "https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwGDJnZf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1a1pcIXFsW8qUWIPodn6G0uZjkhk8SOR6erF-zk9-sKQ&oe=69D8376F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 102,
          "url": "https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwGDJnZf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1a1pcIXFsW8qUWIPodn6G0uZjkhk8SOR6erF-zk9-sKQ&oe=69D8376F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657811\" FBManifestIdentifier=\"FqaNs50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZhojR4r/Q2Y0D0qP4j7HP7gTc7biv2tL1BNy48a7NxpAFnoq59pqbxwX8q/bF7erMBcjV6ur59fAH1O2YhM2R5woiGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABaCAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1563973005025935v\" bandwidth=\"337669\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"941843\" FBPlaybackResolutionMos=\"0:100,360:29.3,480:28.4,720:29.1,1080:31.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:70.9,480:62.6,720:50.4,1080:39.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN6p1XA_FXFLkUVYTtE8Zwx7keoWfwDMyx-B_QxL4pXgZeg8McEumkwF6WDJ4fnzDnBOTY9wUJL7oCRtGW6qjDxoh6M3Qq7Su4omI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=BfloUU35i64Q7kNvwEziFh7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjMzNzY2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0wXEcT1WfIIgzh7cxun6A8Bw3FUJl3zvCFe0-dK3yjig&amp;oe=69DC3392</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-14042\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-89181\" FBFirstSegmentRange=\"891-165373\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"165374-688020\" FBPrefetchSegmentRange=\"891-165373\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1443772230413870v\" bandwidth=\"509752\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1421827\" FBPlaybackResolutionMos=\"0:100,360:40.4,480:38,720:37.2,1080:38.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:80.5,480:73.6,720:62.8,1080:52.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO03YPWFT70GHasKStspUo-nCsZakOgI61xyRI5dJ6BZRsyp4lBEZKTh7qJH33vHao8lA7Gz8jHRXP-xoDvVyNDrlzf18WIgj_ye2E.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=O1KjHuo6qEEQ7kNvwHUInIU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUwOTc1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2pOUrffyFsi4jx6quq3zVpCfTEIaDhZKw5QiyJZnEmiA&amp;oe=69DC2246</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-19700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-153929\" FBFirstSegmentRange=\"891-284632\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"284633-1049599\" FBPrefetchSegmentRange=\"891-284632\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3041551559367530v\" bandwidth=\"722308\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2014698\" FBPlaybackResolutionMos=\"0:100,360:51.1,480:47.8,720:45.4,1080:45.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.5,480:81.3,720:72.1,1080:62.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m367/AQPSpcAxu8AB6FoUvT9edmiINl_OKU0kxsELupA-W7mtlP9_ucOO0LmcFcGoF7nFLPaLtxp6SODqMd31GQF9E68R4xCcOv91YV_Za6U.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=D5k1RwfW4qsQ7kNvwHbNG6j&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjcyMjMwOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3udt877gRMGqfjXxf_kTO70pb6XNN9fvHTWMKIWsmhAg&amp;oe=69DC3677</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-28550\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-246143\" FBFirstSegmentRange=\"891-439881\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"439882-1486392\" FBPrefetchSegmentRange=\"891-439881\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1576336420162302v\" bandwidth=\"989685\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2760477\" FBPlaybackResolutionMos=\"0:100,360:60.9,480:57,720:54.1,1080:53.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91,480:87.2,720:79.7,1080:71.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNWawONH_0ykNRhgXYD5USnUS-2JcDjQ0cKPtzUQ4bmPrDRMRJgACUHEnYvSCFWgDRdksntOheWe4DkpraAAYpYXQpEyt7yK9nS-5A.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=JGpaa8RbgzYQ7kNvwGAmr0E&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjk4OTY4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1IfNNrYXy4YOVbIinnG-eo5Fx5m98aSqDmfTBgULOdJQ&amp;oe=69DC2D08</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-36175\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-368341\" FBFirstSegmentRange=\"891-638853\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"638854-2015969\" FBPrefetchSegmentRange=\"891-638853\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1384606506359662v\" bandwidth=\"1369954\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3821143\" FBPlaybackResolutionMos=\"0:100,360:69.5,480:65.5,720:61.7,1080:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.2,480:91.7,720:86.3,1080:79.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHjz86uKmkZFb6AfTAuNXhaCR5cY5lsEh1FSO9m1gsCdbf2BQ8JMp-g6pMIlhKv6fDPKpemYtUf_SuYjLt-9p7iIGYj7iVdOv9W4k.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=rfIPTL7SCmsQ7kNvwHddjhF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzNjk5NTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0pFM51Gpt6wZaOvOhtQnzHcVeYpUHlYibd1o61G0a04g&amp;oe=69DC297A</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-46923\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-542605\" FBFirstSegmentRange=\"891-915699\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"915700-2726908\" FBPrefetchSegmentRange=\"891-915699\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1369156268001513v\" bandwidth=\"1822480\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"5083349\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:71.6,720:67.7,1080:65.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:94.5,720:90.4,1080:85.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m367/AQMvyH-MQjdKfi00Fl5WSSH-1UKJzwFI8zT_5r_axCxb1zBFH7oejYKyu0sw6aikisn4kwP7Dvea3yfEnFbu9mGB_M3KNvNh7vkIxnY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=OQojGzvwWRUQ7kNvwFb7dD7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE4MjI0ODAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1rMGviJcpko6aAZolB6JYHM_1p1hlk236ozks0EcRWEg&amp;oe=69DC2E21</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-58146\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-759235\" FBFirstSegmentRange=\"891-1253416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1253417-3555514\" FBPrefetchSegmentRange=\"891-1253416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"2218641838658916v\" bandwidth=\"2563525\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"7150307\" FBPlaybackResolutionMos=\"0:100,360:81.3,480:77.1,720:73.4,1080:70.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.9,720:94.1,1080:90.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6gX6iet6wVi2vwiQzpMYKnTkzyIOrnIhhWCeS_HxxTf5k1JEyxtDXBZl3W1nkz-gCcy90W_Uonp2gPqR_zfKL3rzkQ3beNg1DNR0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea5-1.cdninstagram.com&amp;_nc_ohc=ZhVzyNU6d_IQ7kNvwEMAUNc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI1NjM1MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1o36xdP-Au79kTwYAiFLKBi04fvO1QjVtenrsEmYBNpA&amp;oe=69DC2E23</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-74586\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-1107880\" FBFirstSegmentRange=\"891-1794122\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1794123-4835105\" FBPrefetchSegmentRange=\"891-1794122\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"874552045098052a\" bandwidth=\"46857\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46857\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"131698\" FBPaqMos=\"86.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sea1-1.cdninstagram.com/o1/v/t2/f2/m86/AQPkB7GmtjggjHEJa-kd2XK21HSs5MPOBh8Kn_V_b6gCkSbQo9RxM5qstTSXAhy-_70SQiuAW02OQtBnYlPkvoo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sea1-1.cdninstagram.com&amp;_nc_ohc=ZSfr4AA8_vgQ7kNvwErgwO0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ3MjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1OsPtysRxGuA1Q7M_7GXnYUSmy93y_sM2sTekdQ1gTUg&amp;oe=69D859DB</BaseURL><SegmentBase indexRange=\"824-999\" timescale=\"48000\" FBMinimumPrefetchRange=\"1000-1360\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1000-14536\" FBFirstSegmentRange=\"1000-12223\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"12224-22571\" FBPrefetchSegmentRange=\"1000-22571\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "number_of_qualities": 7,
      "video_codec": "vp09.00.30.08.00.02.02.01.00",
      "sharing_friction_info": {
        "should_have_sharing_friction": false,
        "bloks_app_url": null,
        "sharing_friction_payload": null
      },
      "gen_ai_detection_method": {
        "detection_method": "NONE"
      },
      "user": {
        "strong_id__": "787132",
        "fbid_v2": 17841400573960012,
        "feed_post_reshare_disabled": false,
        "id": "787132",
        "is_unpublished": false,
        "pk": 787132,
        "pk_id": "787132",
        "third_party_downloads_enabled": 2,
        "can_see_quiet_post_attribution": true,
        "eligible_for_text_app_activation_badge": false,
        "account_type": 2,
        "account_badges": [],
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
          "followed_by": false,
          "is_muting_reel": false
        },
        "has_anonymous_profile_picture": false,
        "is_favorite": false,
        "is_private": false,
        "is_ring_creator": false,
        "show_ring_award": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEss1iWvtD6oG30x9rqUuzwTKD0PaRY50-vvupOCfuuy6_TyKHxJZXKI-USEqL6XV4&_nc_ohc=XbeNvhLXv28Q7kNvwEM8ir9&_nc_gid=GwVbMJ1xiqL7XPlU-SC7Pw&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ra9G83ekKdAnZi1iigKCzP2a0u_QAbZu6bJTfiEiOIQ&oe=69DC51E9&_nc_sid=fc8dfb",
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "username": "natgeo",
        "text_post_app_is_private": false,
        "is_active_on_text_post_app": true,
        "latest_reel_media": 1775583063,
        "user_activation_info": {}
      },
      "community_notes_info": {
        "has_viewer_submitted_note": false,
        "note_submission_disabled": false,
        "enable_submission_friction": false,
        "is_eligible_for_request_a_note": true
      },
      "has_high_risk_gen_ai_inform_treatment": false,
      "caption_is_edited": false,
      "code": "DRqAYKuAIUx",
      "device_timestamp": 1764453587369,
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
  ],
  "auto_load_more_enabled": true,
  "status": "ok"
}
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
            "video_length": 22.313
          }
        }
      },
      "media_type": 2,
      "original_width": 720,
      "original_height": 1280,
      "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMDczZGFmNzU2NDIwNDczYzkxNWI2OTRiN2JiMTM5MzYzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzgxMjg1MnwzNzc2ODMyODk4MjgwMjI4MTQ1fDMxNzE0NDU2OTY2fDMwMGFkN2YzYjRmMzU1ZjMyZmI0N2RiM2ZiZmM5NjVmZGFhYmJmZTgwZjc5MzJkYTg2N2QxM2UwN2MyZTkyMGIifSwic2lnbmF0dXJlIjoiIn0=",
      "music_metadata": null,
      "has_tagged_users": false,
      "clips_tab_pinned_user_ids": [],
      "is_open_to_public_submission": false,
      "is_social_ufi_disabled": false,
      "timeline_pinned_user_ids": [],
      "taken_at": 1764453631,
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
      "social_context": [],
      "subscribe_cta_visible": false,
      "creative_config": null,
      "is_cutout_sticker_allowed": false,
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
      "commerce_integrity_review_decision": "",
      "is_reuse_allowed": false,
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "boost_unavailable_reason_v2": null,
      "coauthor_producers": [],
      "coauthor_producer_can_see_organic_insights": false,
      "invited_coauthor_producers": [],
      "igbio_product": null,
      "is_paid_partnership": false,
      "reshare_count": 8346,
      "ig_media_sharing_disabled": false,
      "media_repost_count": 4442,
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
            "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFm15zcVP-xSPB8Mugx4KR49byI8iGahbzl7dN1_Hrmfqxg1F3KeOwwfZx1Dd2SQYU&_nc_ohc=XbeNvhLXv28Q7kNvwGzUeEE&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1aMF_U2XxqrIGva4brw0q0bH75A6WDoTP-Pb0tbSSjYQ&oe=69DC51E9&_nc_sid=fc8dfb"
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
      "like_count": 135430,
      "top_likers": [],
      "hidden_likes_string_variant": -1,
      "caption": {
        "strong_id__": "18065011298571522",
        "bit_flags": 0,
        "created_at": 1764453632,
        "created_at_utc": 1764453632,
        "did_report_as_spam": false,
        "is_ranked_comment": false,
        "pk": "18065011298571522",
        "share_enabled": false,
        "content_type": "comment",
        "media_id": 3776832898280228145,
        "status": "Active",
        "type": 1,
        "user_id": 787132,
        "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
        "user": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "is_unpublished": false,
          "fbid_v2": 17841400573960012,
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFm15zcVP-xSPB8Mugx4KR49byI8iGahbzl7dN1_Hrmfqxg1F3KeOwwfZx1Dd2SQYU&_nc_ohc=XbeNvhLXv28Q7kNvwGzUeEE&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1aMF_U2XxqrIGva4brw0q0bH75A6WDoTP-Pb0tbSSjYQ&oe=69DC51E9&_nc_sid=fc8dfb"
        },
        "is_covered": false,
        "private_reply_status": 0,
        "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
      },
      "comment_count": 485,
      "can_view_more_preview_comments": false,
      "preview_comments": [],
      "comment_likes_enabled": true,
      "comment_inform_treatment": {
        "action_type": null,
        "should_have_inform_treatment": false,
        "text": "",
        "url": null
      },
      "is_photo_comments_composer_enabled_for_author": false,
      "hide_view_all_comment_entrypoint": true,
      "locations": [],
      "play_count": 2866120,
      "ig_play_count": 2866120,
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
      "video_duration": 22.31399917602539,
      "is_dash_eligible": 1,
      "video_versions": [
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 101,
          "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwGaz3aS&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2FqKBrIAnEOeca6RuP95A9GisH3C280uHQPKk7oJoDmw&oe=69D8376F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 102,
          "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwGaz3aS&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2FqKBrIAnEOeca6RuP95A9GisH3C280uHQPKk7oJoDmw&oe=69D8376F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657812\" FBManifestIdentifier=\"FqiNs50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZttKj+I+xz+4E3O24r9rS9QTcuPGuzcaQBZ6Kufaam8cF7JqyzN6dzAX8q/bF7erMBZrPsJvI77AGyNXq6vn18AfckvPq2e7SCNTtmITNkecKnuvr86jMyQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyIsGRgFbGlnaHQAFoICFAASFAIA\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1563973005025935v\" bandwidth=\"337669\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"941843\" FBPlaybackResolutionMos=\"0:100,360:29.3,480:28.4,720:29.1,1080:31.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:70.9,480:62.6,720:50.4,1080:39.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN6p1XA_FXFLkUVYTtE8Zwx7keoWfwDMyx-B_QxL4pXgZeg8McEumkwF6WDJ4fnzDnBOTY9wUJL7oCRtGW6qjDxoh6M3Qq7Su4omI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=BfloUU35i64Q7kNvwGby7Mr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjMzNzY2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0BzZ8-aqTrK_onk3wuIBNBUHNChWR90iDa9ieGTyM7YA&amp;oe=69DC3392</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-14042\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-89181\" FBFirstSegmentRange=\"891-165373\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"165374-688020\" FBPrefetchSegmentRange=\"891-165373\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1443772230413870v\" bandwidth=\"509752\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1421827\" FBPlaybackResolutionMos=\"0:100,360:40.4,480:38,720:37.2,1080:38.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:80.5,480:73.6,720:62.8,1080:52.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQO03YPWFT70GHasKStspUo-nCsZakOgI61xyRI5dJ6BZRsyp4lBEZKTh7qJH33vHao8lA7Gz8jHRXP-xoDvVyNDrlzf18WIgj_ye2E.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=O1KjHuo6qEEQ7kNvwFaXuer&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUwOTc1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3yCj-MxyNIfS-yRUkyMzwgdIu0U0maTmXFnSWgOjbkkQ&amp;oe=69DC2246</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-19700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-153929\" FBFirstSegmentRange=\"891-284632\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"284633-1049599\" FBPrefetchSegmentRange=\"891-284632\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3041551559367530v\" bandwidth=\"722308\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2014698\" FBPlaybackResolutionMos=\"0:100,360:51.1,480:47.8,720:45.4,1080:45.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.5,480:81.3,720:72.1,1080:62.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPSpcAxu8AB6FoUvT9edmiINl_OKU0kxsELupA-W7mtlP9_ucOO0LmcFcGoF7nFLPaLtxp6SODqMd31GQF9E68R4xCcOv91YV_Za6U.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=D5k1RwfW4qsQ7kNvwEBK8sP&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjcyMjMwOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af24uCUF1QZ79buS16ZgqrdANBF_mXCxmn4aCts5tBN7ew&amp;oe=69DC3677</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-28550\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-246143\" FBFirstSegmentRange=\"891-439881\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"439882-1486392\" FBPrefetchSegmentRange=\"891-439881\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1576336420162302v\" bandwidth=\"989685\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2760477\" FBPlaybackResolutionMos=\"0:100,360:60.9,480:57,720:54.1,1080:53.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91,480:87.2,720:79.7,1080:71.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNWawONH_0ykNRhgXYD5USnUS-2JcDjQ0cKPtzUQ4bmPrDRMRJgACUHEnYvSCFWgDRdksntOheWe4DkpraAAYpYXQpEyt7yK9nS-5A.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=JGpaa8RbgzYQ7kNvwHTskrs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjk4OTY4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Fp1-nEfqdk4SU4TJ2MJOS_smLDYg6z3pQrn1okVTNsw&amp;oe=69DC2D08</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-36175\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-368341\" FBFirstSegmentRange=\"891-638853\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"638854-2015969\" FBPrefetchSegmentRange=\"891-638853\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1384606506359662v\" bandwidth=\"1369954\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3821143\" FBPlaybackResolutionMos=\"0:100,360:69.5,480:65.5,720:61.7,1080:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.2,480:91.7,720:86.3,1080:79.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHjz86uKmkZFb6AfTAuNXhaCR5cY5lsEh1FSO9m1gsCdbf2BQ8JMp-g6pMIlhKv6fDPKpemYtUf_SuYjLt-9p7iIGYj7iVdOv9W4k.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=rfIPTL7SCmsQ7kNvwHgku2z&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzNjk5NTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2_0QQ-T3KEYLbHYgVeMCMt-qJP05X9gkJmN1tKD2JdrQ&amp;oe=69DC297A</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-46923\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-542605\" FBFirstSegmentRange=\"891-915699\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"915700-2726908\" FBPrefetchSegmentRange=\"891-915699\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1369156268001513v\" bandwidth=\"1822480\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"5083349\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:71.6,720:67.7,1080:65.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:94.5,720:90.4,1080:85.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMvyH-MQjdKfi00Fl5WSSH-1UKJzwFI8zT_5r_axCxb1zBFH7oejYKyu0sw6aikisn4kwP7Dvea3yfEnFbu9mGB_M3KNvNh7vkIxnY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=OQojGzvwWRUQ7kNvwH234Kc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE4MjI0ODAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Oe3wWcJSdOyWQvMKJJPWgYR0Nvgc3icj0faZVGpQEsA&amp;oe=69DC2E21</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-58146\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-759235\" FBFirstSegmentRange=\"891-1253416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1253417-3555514\" FBPrefetchSegmentRange=\"891-1253416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"2218641838658916v\" bandwidth=\"2563525\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"7150307\" FBPlaybackResolutionMos=\"0:100,360:81.3,480:77.1,720:73.4,1080:70.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.9,720:94.1,1080:90.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6gX6iet6wVi2vwiQzpMYKnTkzyIOrnIhhWCeS_HxxTf5k1JEyxtDXBZl3W1nkz-gCcy90W_Uonp2gPqR_zfKL3rzkQ3beNg1DNR0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=ZhVzyNU6d_IQ7kNvwEOfglg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI1NjM1MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3r31Y4_ZEwGrsSSHZZJv1CeqhrH4KzmLN4X9E6FI3gpA&amp;oe=69DC2E23</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-74586\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-1107880\" FBFirstSegmentRange=\"891-1794122\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1794123-4835105\" FBPrefetchSegmentRange=\"891-1794122\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwEKiNC2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Reu2WqnHnWbSI3oZ7VIQu8VTmj66i2yRyuX_1pscGCg&amp;oe=69DC2F41</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwH0WDzk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0SDvNzPkOzcQgYLRVQP9YApit8P70mDH43GdcvJLAGmw&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwFqBFBH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0XUOtSvoCT5cOCcGAMu6HkQtDaZkun6jb2YwvHsJWRMw&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwE0lfer&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=zfaIdoseQF0M-Em8lHCF6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1cbOUgJV2v5U7a3LA4v7OI5RxWdI6qETq0ISLbz99npQ&amp;oe=69DC1A43</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "number_of_qualities": 7,
      "video_codec": "vp09.00.30.08.00.02.02.01.00",
      "sharing_friction_info": {
        "should_have_sharing_friction": false,
        "bloks_app_url": null,
        "sharing_friction_payload": null
      },
      "gen_ai_detection_method": {
        "detection_method": "NONE"
      },
      "user": {
        "strong_id__": "787132",
        "fbid_v2": 17841400573960012,
        "feed_post_reshare_disabled": false,
        "id": "787132",
        "is_unpublished": false,
        "pk": 787132,
        "pk_id": "787132",
        "third_party_downloads_enabled": 2,
        "can_see_quiet_post_attribution": true,
        "eligible_for_text_app_activation_badge": false,
        "account_type": 2,
        "account_badges": [],
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
          "followed_by": false,
          "is_muting_reel": false
        },
        "has_anonymous_profile_picture": false,
        "is_favorite": false,
        "is_private": false,
        "is_ring_creator": false,
        "show_ring_award": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFm15zcVP-xSPB8Mugx4KR49byI8iGahbzl7dN1_Hrmfqxg1F3KeOwwfZx1Dd2SQYU&_nc_ohc=XbeNvhLXv28Q7kNvwGzUeEE&_nc_gid=zfaIdoseQF0M-Em8lHCF6w&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1aMF_U2XxqrIGva4brw0q0bH75A6WDoTP-Pb0tbSSjYQ&oe=69DC51E9&_nc_sid=fc8dfb",
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "username": "natgeo",
        "text_post_app_is_private": false,
        "is_active_on_text_post_app": true,
        "latest_reel_media": 1775583063,
        "user_activation_info": {}
      },
      "community_notes_info": {
        "has_viewer_submitted_note": false,
        "note_submission_disabled": false,
        "enable_submission_friction": false,
        "is_eligible_for_request_a_note": true
      },
      "has_high_risk_gen_ai_inform_treatment": false,
      "caption_is_edited": false,
      "code": "DRqAYKuAIUx",
      "device_timestamp": 1764453587369,
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
  ],
  "auto_load_more_enabled": true,
  "status": "ok"
}
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
            "video_length": 22.313
          }
        }
      },
      "media_type": 2,
      "original_width": 720,
      "original_height": 1280,
      "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYjRiOTMwZTQwZTk5NDFhZjlkM2U4ZjNjNTM3MWQ5MjUzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzgxMzgzOXwzNzc2ODMyODk4MjgwMjI4MTQ1fDMwMDA3OTM4OTM2fDk3ODBmM2E1YTE2MzQyZTZjNjFkZTBlNDJmNzY1NWI2NjAyNDliZjQxNjJhMzE2ODQ5NTBhM2I0OWE0NjIxMTUifSwic2lnbmF0dXJlIjoiIn0=",
      "music_metadata": null,
      "has_tagged_users": false,
      "clips_tab_pinned_user_ids": [],
      "is_open_to_public_submission": false,
      "is_social_ufi_disabled": false,
      "timeline_pinned_user_ids": [],
      "taken_at": 1764453631,
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
      "social_context": [],
      "subscribe_cta_visible": false,
      "creative_config": null,
      "is_cutout_sticker_allowed": false,
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
      "commerce_integrity_review_decision": "",
      "is_reuse_allowed": false,
      "boost_unavailable_identifier": null,
      "boost_unavailable_reason": null,
      "boost_unavailable_reason_v2": null,
      "coauthor_producers": [],
      "coauthor_producer_can_see_organic_insights": false,
      "invited_coauthor_producers": [],
      "igbio_product": null,
      "is_paid_partnership": false,
      "reshare_count": 8346,
      "ig_media_sharing_disabled": false,
      "media_repost_count": 4442,
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
            "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGSog-HAZ_2AlSTH8bSkHUlle044gAHMO5eH8qqfGkfUOKv8eYOx3BFqn1BR0YfTh8&_nc_ohc=XbeNvhLXv28Q7kNvwH5l3lh&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0mEW_lhtCiZutn8EB14a9yaz1WlKkuTzbdzUFBtUbL4Q&oe=69DC51E9&_nc_sid=fc8dfb"
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
      "like_count": 135430,
      "top_likers": [],
      "hidden_likes_string_variant": -1,
      "caption": {
        "strong_id__": "18065011298571522",
        "bit_flags": 0,
        "created_at": 1764453632,
        "created_at_utc": 1764453632,
        "did_report_as_spam": false,
        "is_ranked_comment": false,
        "pk": "18065011298571522",
        "share_enabled": false,
        "content_type": "comment",
        "media_id": 3776832898280228145,
        "status": "Active",
        "type": 1,
        "user_id": 787132,
        "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
        "user": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "is_unpublished": false,
          "fbid_v2": 17841400573960012,
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGSog-HAZ_2AlSTH8bSkHUlle044gAHMO5eH8qqfGkfUOKv8eYOx3BFqn1BR0YfTh8&_nc_ohc=XbeNvhLXv28Q7kNvwH5l3lh&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0mEW_lhtCiZutn8EB14a9yaz1WlKkuTzbdzUFBtUbL4Q&oe=69DC51E9&_nc_sid=fc8dfb"
        },
        "is_covered": false,
        "private_reply_status": 0,
        "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
      },
      "comment_count": 485,
      "can_view_more_preview_comments": false,
      "preview_comments": [],
      "comment_likes_enabled": true,
      "comment_inform_treatment": {
        "action_type": null,
        "should_have_inform_treatment": false,
        "text": "",
        "url": null
      },
      "is_photo_comments_composer_enabled_for_author": false,
      "hide_view_all_comment_entrypoint": true,
      "locations": [],
      "play_count": 2866120,
      "ig_play_count": 2866120,
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
      "video_duration": 22.31399917602539,
      "is_dash_eligible": 1,
      "video_versions": [
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 101,
          "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHRXXKU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af018OIRKhgqwz9AKeHd110LBivqGXtiiCwxTuD4HiXHnA&oe=69D8376F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 102,
          "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHRXXKU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af018OIRKhgqwz9AKeHd110LBivqGXtiiCwxTuD4HiXHnA&oe=69D8376F",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657813\" FBManifestIdentifier=\"FqqNs50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZhojR4r/Q2Y0D0qP4j7HP7gTc7biv2tL1BNy48a7NxpAFnoq59pqbxwX8q/bF7erMBcjV6ur59fAH1O2YhM2R5woiGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABaCAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1563973005025935v\" bandwidth=\"337669\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"941843\" FBPlaybackResolutionMos=\"0:100,360:29.3,480:28.4,720:29.1,1080:31.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:70.9,480:62.6,720:50.4,1080:39.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN6p1XA_FXFLkUVYTtE8Zwx7keoWfwDMyx-B_QxL4pXgZeg8McEumkwF6WDJ4fnzDnBOTY9wUJL7oCRtGW6qjDxoh6M3Qq7Su4omI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=BfloUU35i64Q7kNvwFFoo2D&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjMzNzY2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2VXw6g7Tlr5TCQRzEpq71jkQJZ2DsIN--CIaTObv9iIQ&amp;oe=69DC3392</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-14042\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-89181\" FBFirstSegmentRange=\"891-165373\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"165374-688020\" FBPrefetchSegmentRange=\"891-165373\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1443772230413870v\" bandwidth=\"509752\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1421827\" FBPlaybackResolutionMos=\"0:100,360:40.4,480:38,720:37.2,1080:38.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:80.5,480:73.6,720:62.8,1080:52.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO03YPWFT70GHasKStspUo-nCsZakOgI61xyRI5dJ6BZRsyp4lBEZKTh7qJH33vHao8lA7Gz8jHRXP-xoDvVyNDrlzf18WIgj_ye2E.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=O1KjHuo6qEEQ7kNvwH1mcsg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUwOTc1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3iRhTh1eWp8amhayhdBgCePtCy0I6AcHFLf9egvHGdMw&amp;oe=69DC2246</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-19700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-153929\" FBFirstSegmentRange=\"891-284632\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"284633-1049599\" FBPrefetchSegmentRange=\"891-284632\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3041551559367530v\" bandwidth=\"722308\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2014698\" FBPlaybackResolutionMos=\"0:100,360:51.1,480:47.8,720:45.4,1080:45.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.5,480:81.3,720:72.1,1080:62.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPSpcAxu8AB6FoUvT9edmiINl_OKU0kxsELupA-W7mtlP9_ucOO0LmcFcGoF7nFLPaLtxp6SODqMd31GQF9E68R4xCcOv91YV_Za6U.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=D5k1RwfW4qsQ7kNvwFov2EH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjcyMjMwOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0AFizL5unr-9hAV-za1WiSlL0PJR-EdgPgt-7YIu484g&amp;oe=69DC3677</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-28550\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-246143\" FBFirstSegmentRange=\"891-439881\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"439882-1486392\" FBPrefetchSegmentRange=\"891-439881\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1576336420162302v\" bandwidth=\"989685\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2760477\" FBPlaybackResolutionMos=\"0:100,360:60.9,480:57,720:54.1,1080:53.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91,480:87.2,720:79.7,1080:71.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNWawONH_0ykNRhgXYD5USnUS-2JcDjQ0cKPtzUQ4bmPrDRMRJgACUHEnYvSCFWgDRdksntOheWe4DkpraAAYpYXQpEyt7yK9nS-5A.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=JGpaa8RbgzYQ7kNvwG7lWpZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjk4OTY4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3V85nB1llfkl4KsXiY2-YhvlcMI3B_eRYz9e57Nw-zYA&amp;oe=69DC2D08</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-36175\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-368341\" FBFirstSegmentRange=\"891-638853\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"638854-2015969\" FBPrefetchSegmentRange=\"891-638853\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1384606506359662v\" bandwidth=\"1369954\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3821143\" FBPlaybackResolutionMos=\"0:100,360:69.5,480:65.5,720:61.7,1080:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.2,480:91.7,720:86.3,1080:79.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHjz86uKmkZFb6AfTAuNXhaCR5cY5lsEh1FSO9m1gsCdbf2BQ8JMp-g6pMIlhKv6fDPKpemYtUf_SuYjLt-9p7iIGYj7iVdOv9W4k.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=rfIPTL7SCmsQ7kNvwElnZCr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzNjk5NTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0NbqFdaifC3GJ6JKzaVSeIF888oeLtwCpqs9Vr38BSCA&amp;oe=69DC297A</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-46923\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-542605\" FBFirstSegmentRange=\"891-915699\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"915700-2726908\" FBPrefetchSegmentRange=\"891-915699\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1369156268001513v\" bandwidth=\"1822480\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"5083349\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:71.6,720:67.7,1080:65.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:94.5,720:90.4,1080:85.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMvyH-MQjdKfi00Fl5WSSH-1UKJzwFI8zT_5r_axCxb1zBFH7oejYKyu0sw6aikisn4kwP7Dvea3yfEnFbu9mGB_M3KNvNh7vkIxnY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=OQojGzvwWRUQ7kNvwE55c1n&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE4MjI0ODAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1EzqG4qW-DOhd0UI4L1pqoGLSf6cuBF0J1oyPkgrfi5A&amp;oe=69DC2E21</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-58146\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-759235\" FBFirstSegmentRange=\"891-1253416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1253417-3555514\" FBPrefetchSegmentRange=\"891-1253416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"2218641838658916v\" bandwidth=\"2563525\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"7150307\" FBPlaybackResolutionMos=\"0:100,360:81.3,480:77.1,720:73.4,1080:70.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.9,720:94.1,1080:90.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6gX6iet6wVi2vwiQzpMYKnTkzyIOrnIhhWCeS_HxxTf5k1JEyxtDXBZl3W1nkz-gCcy90W_Uonp2gPqR_zfKL3rzkQ3beNg1DNR0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=ZhVzyNU6d_IQ7kNvwGpi4RX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI1NjM1MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af07bqzCOzFZnvfHYIxibwO-Sh1UACQRzRqMV_q3LTx_cw&amp;oe=69DC2E23</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-74586\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-1107880\" FBFirstSegmentRange=\"891-1794122\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1794123-4835105\" FBPrefetchSegmentRange=\"891-1794122\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"874552045098052a\" bandwidth=\"46857\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46857\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"131698\" FBPaqMos=\"86.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m86/AQPkB7GmtjggjHEJa-kd2XK21HSs5MPOBh8Kn_V_b6gCkSbQo9RxM5qstTSXAhy-_70SQiuAW02OQtBnYlPkvoo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=ZSfr4AA8_vgQ7kNvwF2gUiL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ3MjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2EqUFulFY65cNN7Bchoaku_SV62tjCCfJVqAvyyj433A&amp;oe=69D859DB</BaseURL><SegmentBase indexRange=\"824-999\" timescale=\"48000\" FBMinimumPrefetchRange=\"1000-1360\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1000-14536\" FBFirstSegmentRange=\"1000-12223\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"12224-22571\" FBPrefetchSegmentRange=\"1000-22571\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "number_of_qualities": 7,
      "video_codec": "vp09.00.30.08.00.02.02.01.00",
      "sharing_friction_info": {
        "should_have_sharing_friction": false,
        "bloks_app_url": null,
        "sharing_friction_payload": null
      },
      "gen_ai_detection_method": {
        "detection_method": "NONE"
      },
      "user": {
        "strong_id__": "787132",
        "fbid_v2": 17841400573960012,
        "feed_post_reshare_disabled": false,
        "id": "787132",
        "is_unpublished": false,
        "pk": 787132,
        "pk_id": "787132",
        "third_party_downloads_enabled": 2,
        "can_see_quiet_post_attribution": true,
        "eligible_for_text_app_activation_badge": false,
        "account_type": 2,
        "account_badges": [],
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
          "followed_by": false,
          "is_muting_reel": false
        },
        "has_anonymous_profile_picture": false,
        "is_favorite": false,
        "is_private": false,
        "is_ring_creator": false,
        "show_ring_award": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGSog-HAZ_2AlSTH8bSkHUlle044gAHMO5eH8qqfGkfUOKv8eYOx3BFqn1BR0YfTh8&_nc_ohc=XbeNvhLXv28Q7kNvwH5l3lh&_nc_gid=4vZL5Gb0zyxjhABNtrBaAA&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0mEW_lhtCiZutn8EB14a9yaz1WlKkuTzbdzUFBtUbL4Q&oe=69DC51E9&_nc_sid=fc8dfb",
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "username": "natgeo",
        "text_post_app_is_private": false,
        "is_active_on_text_post_app": true,
        "latest_reel_media": 1775583063,
        "user_activation_info": {}
      },
      "community_notes_info": {
        "has_viewer_submitted_note": false,
        "note_submission_disabled": false,
        "enable_submission_friction": false,
        "is_eligible_for_request_a_note": true
      },
      "has_high_risk_gen_ai_inform_treatment": false,
      "caption_is_edited": false,
      "code": "DRqAYKuAIUx",
      "device_timestamp": 1764453587369,
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
  ],
  "auto_load_more_enabled": true,
  "status": "ok"
}
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
          "pk_id": "1393016141",
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.2885-19/10514103_680727235334784_933888781_a.jpg?stp=dst-jpg_e0_tt6&_nc_cat=107&ig_cache_key=GLduoACAEg0pHmsCAA0DqjcAAAAAYUULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=C0bKK8aX6HUQ7kNvwHU6Edm&_nc_oc=AdpausIlPFAfdTPhe9-lEr70Hi7HJJqK-Wt6e1IQSajeB-AbOEficWmICblZgegBZdU&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af2TsyJuLrwCcs81ZUVkmkzlvjXYw3Y3KoKH2i-2-diQUA&oe=69DC49E1",
          "strong_id__": "1393016141",
          "username": "scubalover14"
        },
        "user_id": 1393016141,
        "has_liked": false,
        "like_count": 66
      },
      {
        "bit_flags": 0,
        "comment_like_count": 4,
        "content_type": "comment",
        "created_at": 1764454818,
        "created_at_for_fb_app": 1764454818,
        "created_at_utc": 1764454818,
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
        "pk": "17992046705899459",
        "preview_child_comments": [],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "17992046705899459",
        "text": "😍😍😍amazing",
        "type": 0,
        "user": {
          "fbid_v2": 17841400961017988,
          "full_name": "Victoria💫",
          "id": "1791264033",
          "is_mentionable": true,
          "is_private": true,
          "is_verified": false,
          "pk": "1791264033",
          "pk_id": "1791264033",
          "profile_pic_id": "3869420660985004114_1791264033",
          "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-19/659112133_18577992958032034_8453764196225005035_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMVASSeiOOcOlgBCAOs16Bq-zVF1bmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy44NzIuQzMifQ%3D%3D&_nc_ohc=DnA_JPkhzXwQ7kNvwGWbQQQ&_nc_oc=AdqlMk5knJ2Jl88bPgA1rRvalLOpqC1gHZC23k-hWsBjjftUnYkzLVwpZ9HSfrElF9E&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=lEjzIWFJ73NaMueeKGtW8w&_nc_ss=7a3ba&oh=00_Af0Q45vGm7gtLA606SbR0FEj1ZHWlN8-qBqyLkWa_r8DyA&oe=69DC247D",
          "strong_id__": "1791264033",
          "username": "victoria.mvr"
        },
        "user_id": 1791264033,
        "has_liked": false,
        "like_count": 4
      }
    ],
    "has_more_comments": false,
    "has_more_headload_comments": true,
    "initiate_at_top": true,
    "insert_new_comment_to_top": true,
    "is_ranked": true,
    "liked_by_media_owner_badge_enabled": true,
    "media_header_display": "none",
    "next_min_id": "{\"cached_comments_cursor\":\"17949943713058869\",\"bifilter_token\":\"GgYYgQEAdW3FVtCNPwDCTHdlxaU_AMP3r9Cr6z8AMhmj3X-VQABTxkydXlBAALsIoOBsG0AAVuTsZEiVPwAhCmFim31AAF4te7MV1T8ALn3Jacx6PwC4U0M0doxAAHQoBSjkgj8AooIF5QCOPwAisdTmR1FAAEjYN1MvNkAAzEOJKKc-QAAA\"}",
    "quick_response_emojis": [
      {
        "unicode": "❤️"
      },
      {
        "unicode": "🙌"
      }
    ],
    "scroll_behavior": 1,
    "filter_options": [],
    "sort_options": [],
    "preview_comments": [],
    "should_render_upsell": false,
    "foundation_improvements_enabled": true,
    "has_more_headload_fb_comments": false,
    "fb_comments": [],
    "ai_topic_filters": [],
    "status": "ok"
  },
  "next_page_id": "IntcImNhY2hlZF9jb21tZW50c19jdXJzb3JcIjpcIjE3OTQ5OTQzNzEzMDU4ODY5XCIsXCJiaWZpbHRlcl90b2tlblwiOlwiR2dZWWdRRUFkVzNGVnRDTlB3RENUSGRseGFVX0FNUDNyOUNyNno4QU1obWozWC1WUUFCVHhreWRYbEJBQUxzSW9PQnNHMEFBVnVUc1pFaVZQd0FoQ21GaW0zMUFBRjR0ZTdNVjFUOEFMbjNKYWN4NlB3QzRVME0wZG94QUFIUW9CU2prZ2o4QW9vSUY1UUNPUHdBaXNkVG1SMUZBQUVqWU4xTXZOa0FBekVPSktLYy1RQUFBXCJ9Ig=="
}
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
    "media_type": 2,
    "original_width": 1080,
    "original_height": 1920,
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZjMxMDIwNGZhMWZlNGM1OTk1MDUyMGRhMzg3ZmUwODMzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzgwMTUxMHwzNzc2ODMyODk4MjgwMjI4MTQ1fDM3MTE0ODUzODk0fGM5ZDA0ZTc5MGVmOTU1ZGVhOTFiNjgzNDA5YTcxNjZlZmMyZmYyYzU5ZTEyNjUzNDk3ZDE5NmZkZjI2MWNmOWYifSwic2lnbmF0dXJlIjoiIn0=",
    "music_metadata": null,
    "has_tagged_users": false,
    "clips_tab_pinned_user_ids": [],
    "is_open_to_public_submission": false,
    "is_social_ufi_disabled": false,
    "timeline_pinned_user_ids": [],
    "taken_at": 1764453631,
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
    "social_context": [],
    "subscribe_cta_visible": false,
    "creative_config": null,
    "is_cutout_sticker_allowed": false,
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
    "commerce_integrity_review_decision": "",
    "prefetch_instructions": {
      "should_force_new_preload_chaining": false
    },
    "boost_unavailable_identifier": null,
    "boost_unavailable_reason": null,
    "boost_unavailable_reason_v2": null,
    "coauthor_producers": [],
    "coauthor_producer_can_see_organic_insights": false,
    "invited_coauthor_producers": [],
    "igbio_product": null,
    "is_paid_partnership": false,
    "reshare_count": 8346,
    "ig_media_sharing_disabled": false,
    "media_repost_count": 4442,
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
          "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHrpnYIq0-QxyWAjEkckZ2VxNOO5B6RXEo_m-QIdSywk9IYF8lI5jDPSvn_YGJ6ots&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=87M24HNrc0sS13EXm3wLVA&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0rSPuMVGUH_PL_TZ7EHnWcWYcNL7xbjUXj77Dgcd217A&oe=69DC51E9&_nc_sid=55bbed"
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
    "like_count": 135430,
    "top_likers": [],
    "hidden_likes_string_variant": -1,
    "caption": {
      "strong_id__": "18065011298571522",
      "bit_flags": 0,
      "created_at": 1764453632,
      "created_at_utc": 1764453632,
      "did_report_as_spam": false,
      "is_ranked_comment": false,
      "pk": "18065011298571522",
      "share_enabled": false,
      "content_type": "comment",
      "media_id": 3776832898280228145,
      "status": "Active",
      "type": 1,
      "user_id": 787132,
      "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "pk_id": "787132",
        "id": "787132",
        "is_unpublished": false,
        "fbid_v2": 17841400573960012,
        "username": "natgeo",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHrpnYIq0-QxyWAjEkckZ2VxNOO5B6RXEo_m-QIdSywk9IYF8lI5jDPSvn_YGJ6ots&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=87M24HNrc0sS13EXm3wLVA&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0rSPuMVGUH_PL_TZ7EHnWcWYcNL7xbjUXj77Dgcd217A&oe=69DC51E9&_nc_sid=55bbed"
      },
      "is_covered": false,
      "private_reply_status": 0,
      "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
    },
    "comment_count": 485,
    "comment_inform_treatment": {
      "action_type": null,
      "should_have_inform_treatment": false,
      "text": "",
      "url": null
    },
    "is_photo_comments_composer_enabled_for_author": false,
    "hide_view_all_comment_entrypoint": true,
    "locations": [],
    "play_count": 2866120,
    "ig_play_count": 2866120,
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
    "video_duration": 22.31399917602539,
    "is_dash_eligible": 1,
    "video_versions": [
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 101,
        "url": "https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHOkiOz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=87M24HNrc0sS13EXm3wLVA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Qr9Ysp0E6rhyz9HiU0xnnc6DMitVVpM3u6kvEzcqPsw&oe=69D8376F",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 102,
        "url": "https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHOkiOz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=87M24HNrc0sS13EXm3wLVA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Qr9Ysp0E6rhyz9HiU0xnnc6DMitVVpM3u6kvEzcqPsw&oe=69D8376F",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657801\" FBManifestIdentifier=\"FpKNs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxozhmaSP8rACovXRl+ao3wKKjIn135CYA5665tXdzJYE6rO+3tWCgQXOuqeDzoi9BeyasszencwFms+wm8jvsAaKn4CC49CdB8SwgOTBoeoH3JLz6tnu0gie6+vzqMzJDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWggIUABIUAgA=\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwElFKbX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2sIycM8veWMTs8DN6ONUfDucPJqVyDeWflDYkdcfRc7w&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=FbvhhE9pHnIQ7kNvwFJzYFm&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3BIlZymewkNkI_Xx4LaRzukX-i4uqXsj3O1j-nyfZw6Q&amp;oe=69DC2829</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwGtHVQK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0zLYGt9mWrKmksfToy8SdnR3lFmWGYNbToK-ftlGPmNw&amp;oe=69DC2100</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwE332KC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0aARXBAw17o11_PetqyWk-7uB0nZxtMuQBAR67ksQCew&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwF_9GNg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1-NL0KG0haugwdcf-9Sf42_qb1uYcX6XNt5k-bKMMn3g&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwF47UH4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0VP0Zq4rHS00JnQ9MNvX_hy_qwurGz7uOy7Mi_fz-z5w&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwHZvNzS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af21eQK7QJ1dxMiDcgwWHq0G9xE0KIgFgAzdNfMCYftClQ&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"897489239614213v\" bandwidth=\"4472890\" codecs=\"av01.0.08M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"12475999\" FBPlaybackResolutionMos=\"0:100,360:87.2,480:83.7,720:78.9,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.536,480:99.415,720:99.167,1080:98.58\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPVgubbzL4GsEHBto9qJ9DKVHDYdRJUIBrbusVYgthsUApFExMmHIPHOP4-rKP0NJU5hwD7ETkAkZNePbo3qf5TReJDHCiOkPRu_hM.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=PMWR1v3uaAgQ7kNvwFsti36&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ0NzI4OTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ldrlwTLJu79cF-5dxIDryvdZvm2sWg5Qx29Q_ChWt5w&amp;oe=69DC25C6</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-105462\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-2456793\" FBFirstSegmentRange=\"899-3691660\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"3691661-8660328\" FBPrefetchSegmentRange=\"899-3691660\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwHYPHOe&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2M0QjDI8ky8pQRJPYnyhyOlzP3_p0XE6HwBBvIpWuV6w&amp;oe=69DC2F41</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwGPFHoR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1aC0Bqx1uNAIykW-LuDvoEVvPHkG3X_oyqGJmoFtnjhw&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwEitRFg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2CHk6mwsujYrkyF2TLo1U1nwDjXV61K06q26AYX37gTA&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwGWbFWU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=87M24HNrc0sS13EXm3wLVA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3RoKwqkT6lqxDPOeQxv1eHuD2NpnD0yFaFfP4apqnD1g&amp;oe=69DC1A43</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "number_of_qualities": 8,
    "video_codec": "av01.0.04M.08",
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null,
      "sharing_friction_payload": null
    },
    "gen_ai_detection_method": {
      "detection_method": "NONE"
    },
    "user": {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "feed_post_reshare_disabled": false,
      "id": "787132",
      "is_unpublished": false,
      "pk": 787132,
      "pk_id": "787132",
      "third_party_downloads_enabled": 2,
      "eligible_for_text_app_activation_badge": false,
      "account_type": 2,
      "account_badges": [],
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
        "followed_by": false,
        "is_muting_reel": false
      },
      "has_anonymous_profile_picture": false,
      "is_favorite": false,
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHrpnYIq0-QxyWAjEkckZ2VxNOO5B6RXEo_m-QIdSywk9IYF8lI5jDPSvn_YGJ6ots&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=87M24HNrc0sS13EXm3wLVA&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0rSPuMVGUH_PL_TZ7EHnWcWYcNL7xbjUXj77Dgcd217A&oe=69DC51E9&_nc_sid=55bbed",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775583063,
      "user_activation_info": {}
    },
    "community_notes_info": {
      "has_viewer_submitted_note": false,
      "note_submission_disabled": false,
      "enable_submission_friction": false,
      "is_eligible_for_request_a_note": true
    },
    "has_high_risk_gen_ai_inform_treatment": false,
    "caption_is_edited": false,
    "code": "DRqAYKuAIUx",
    "device_timestamp": 1764453587369,
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
  },
  "status": "ok"
}
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
    "media_type": 2,
    "original_width": 1080,
    "original_height": 1920,
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNDdmN2Q2ODNlOGNhNDRiODhkNTk2MmUyYmZlYTQyM2QzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzgwMDU2OXwzNzc2ODMyODk4MjgwMjI4MTQ1fDM0MTU2MDU2MzkyfGM5NDVlYmJjMmUzYzc5YWVkYjZkZGYyMjQxYTdjOTIyMGZlNTlkMTgyMzczZDk3YzNkOGM0NTZiNTUyNDFlMDYifSwic2lnbmF0dXJlIjoiIn0=",
    "music_metadata": null,
    "has_tagged_users": false,
    "clips_tab_pinned_user_ids": [],
    "is_open_to_public_submission": false,
    "is_social_ufi_disabled": false,
    "timeline_pinned_user_ids": [],
    "taken_at": 1764453631,
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
    "social_context": [],
    "subscribe_cta_visible": false,
    "creative_config": null,
    "is_cutout_sticker_allowed": false,
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
    "commerce_integrity_review_decision": "",
    "prefetch_instructions": {
      "should_force_new_preload_chaining": false
    },
    "boost_unavailable_identifier": null,
    "boost_unavailable_reason": null,
    "boost_unavailable_reason_v2": null,
    "coauthor_producers": [],
    "coauthor_producer_can_see_organic_insights": false,
    "invited_coauthor_producers": [],
    "igbio_product": null,
    "is_paid_partnership": false,
    "reshare_count": 8346,
    "ig_media_sharing_disabled": false,
    "media_repost_count": 4442,
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
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH1ChdJBoSeGs0Ve_z8ef0EtbaWWXKwmbms-bMCkAVINVU6-EFYlnYLd3hPLv13Mbw&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2p-82DHm7elxPqmbkjWGAl8Hl8VmXsEzz0lsEI-5MHXw&oe=69DC51E9&_nc_sid=55bbed"
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
    "like_count": 135430,
    "top_likers": [],
    "hidden_likes_string_variant": -1,
    "caption": {
      "strong_id__": "18065011298571522",
      "bit_flags": 0,
      "created_at": 1764453632,
      "created_at_utc": 1764453632,
      "did_report_as_spam": false,
      "is_ranked_comment": false,
      "pk": "18065011298571522",
      "share_enabled": false,
      "content_type": "comment",
      "media_id": 3776832898280228145,
      "status": "Active",
      "type": 1,
      "user_id": 787132,
      "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "pk_id": "787132",
        "id": "787132",
        "is_unpublished": false,
        "fbid_v2": 17841400573960012,
        "username": "natgeo",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH1ChdJBoSeGs0Ve_z8ef0EtbaWWXKwmbms-bMCkAVINVU6-EFYlnYLd3hPLv13Mbw&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2p-82DHm7elxPqmbkjWGAl8Hl8VmXsEzz0lsEI-5MHXw&oe=69DC51E9&_nc_sid=55bbed"
      },
      "is_covered": false,
      "private_reply_status": 0,
      "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
    },
    "comment_count": 485,
    "comment_inform_treatment": {
      "action_type": null,
      "should_have_inform_treatment": false,
      "text": "",
      "url": null
    },
    "is_photo_comments_composer_enabled_for_author": false,
    "hide_view_all_comment_entrypoint": true,
    "locations": [],
    "play_count": 2866120,
    "ig_play_count": 2866120,
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
    "video_duration": 22.31399917602539,
    "is_dash_eligible": 1,
    "video_versions": [
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 101,
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwFS_5u9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af20Ma_rkne5CILKR2bmc86LsdrNHVqj0EaffonrQgpeKg&oe=69D8376F",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 102,
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwFS_5u9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af20Ma_rkne5CILKR2bmc86LsdrNHVqj0EaffonrQgpeKg&oe=69D8376F",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657800\" FBManifestIdentifier=\"FpCNs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxozhmaSP8rACovXRl+ao3wKKjIn135CYA5665tXdzJYE6rO+3tWCgQXOuqeDzoi9BeyasszencwFms+wm8jvsAaKn4CC49CdB8SwgOTBoeoH3JLz6tnu0gie6+vzqMzJDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWggIUABIUAgA=\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwEcCHqn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Hpj72smBxJhV07nnwmXeQx_Ae6Hv2K6PwtwAIaRZP5g&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=FbvhhE9pHnIQ7kNvwHBpXts&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af01Wkt4rOQOeIxmHsN_0qtfBGu9gpk-zNspmuuBE_2F9w&amp;oe=69DC2829</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwFferq-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af11qpwq7yyfTiGMjorDroaGoKtZYdSYU9OraV1wTG2kiw&amp;oe=69DC2100</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwHSeuBf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3axndqfH0suqZ6aw41vOdbRAIg61_9H0Ao5vgh7JQ8jg&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwE2UCA2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2N-ZmAVcoFJqgydgo2KFFl46vCvNHyadsuqMcS0746-g&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwFtRawG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1qqIiR-jx4hrJu-eN409MqhjuBBWDa1SkH6FQoY7igvg&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwGRn7Mb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3aGi5xhY1mqisGw5AD7dc3dtQtbcpUSLFzCwAztikIrA&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"897489239614213v\" bandwidth=\"4472890\" codecs=\"av01.0.08M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"12475999\" FBPlaybackResolutionMos=\"0:100,360:87.2,480:83.7,720:78.9,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.536,480:99.415,720:99.167,1080:98.58\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPVgubbzL4GsEHBto9qJ9DKVHDYdRJUIBrbusVYgthsUApFExMmHIPHOP4-rKP0NJU5hwD7ETkAkZNePbo3qf5TReJDHCiOkPRu_hM.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=PMWR1v3uaAgQ7kNvwH5r8N3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ0NzI4OTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af351jdgQuf-RmhJeN9aJHloP0hm7xvwpJ0mICi07SRaEg&amp;oe=69DC25C6</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-105462\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-2456793\" FBFirstSegmentRange=\"899-3691660\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"3691661-8660328\" FBPrefetchSegmentRange=\"899-3691660\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwHP9dtd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3LLl0FCDUKMMJtEqFS0M5V-YMFA-IZMmwYpshUv9InOQ&amp;oe=69DC2F41</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwHf-r04&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0qSjsQ4QiTIUPJxeOfHFSnHmq6nTU1xXDOUQsVbkT2zQ&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwH_Ldzc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af32aLZA5flSElGThnc1GlPa25_MX6ZS6OQ-kTwnf_A7hw&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwHjNA-B&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3eroKiq9hxTs5Y1rAVYyYXtbAVVDYdWokcVJ2UOf5Bdg&amp;oe=69DC1A43</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "number_of_qualities": 8,
    "video_codec": "av01.0.04M.08",
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null,
      "sharing_friction_payload": null
    },
    "gen_ai_detection_method": {
      "detection_method": "NONE"
    },
    "user": {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "feed_post_reshare_disabled": false,
      "id": "787132",
      "is_unpublished": false,
      "pk": 787132,
      "pk_id": "787132",
      "third_party_downloads_enabled": 2,
      "eligible_for_text_app_activation_badge": false,
      "account_type": 2,
      "account_badges": [],
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
        "followed_by": false,
        "is_muting_reel": false
      },
      "has_anonymous_profile_picture": false,
      "is_favorite": false,
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH1ChdJBoSeGs0Ve_z8ef0EtbaWWXKwmbms-bMCkAVINVU6-EFYlnYLd3hPLv13Mbw&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=GVoeoq8uqvvf0lqWV9-xuw&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2p-82DHm7elxPqmbkjWGAl8Hl8VmXsEzz0lsEI-5MHXw&oe=69DC51E9&_nc_sid=55bbed",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775583063,
      "user_activation_info": {}
    },
    "community_notes_info": {
      "has_viewer_submitted_note": false,
      "note_submission_disabled": false,
      "enable_submission_friction": false,
      "is_eligible_for_request_a_note": true
    },
    "has_high_risk_gen_ai_inform_treatment": false,
    "caption_is_edited": false,
    "code": "DRqAYKuAIUx",
    "device_timestamp": 1764453587369,
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
  },
  "status": "ok"
}
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
    "media_type": 2,
    "original_width": 720,
    "original_height": 1280,
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMDViZGE4ZWNiMDIzNDM4MTkwMTYzNzhhOGIzYjNlMmMzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzgwMjIzNnwzNzc2ODMyODk4MjgwMjI4MTQ1fDQ1OTY2MTYzMTMwfDRlOTBhNmVlZTU1ZjM4Y2ZlMDhiOTI0MGYxYjI5YTM5ZWY1N2EzZjdkYzFlOGRhZDhhOTQ1NWViMGY5ZTYxOWUifSwic2lnbmF0dXJlIjoiIn0=",
    "music_metadata": null,
    "has_tagged_users": false,
    "clips_tab_pinned_user_ids": [],
    "is_open_to_public_submission": false,
    "is_social_ufi_disabled": false,
    "timeline_pinned_user_ids": [],
    "taken_at": 1764453631,
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
    "social_context": [],
    "subscribe_cta_visible": false,
    "creative_config": null,
    "is_cutout_sticker_allowed": false,
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
    "commerce_integrity_review_decision": "",
    "prefetch_instructions": {
      "should_force_new_preload_chaining": false
    },
    "boost_unavailable_identifier": null,
    "boost_unavailable_reason": null,
    "boost_unavailable_reason_v2": null,
    "coauthor_producers": [],
    "coauthor_producer_can_see_organic_insights": false,
    "invited_coauthor_producers": [],
    "igbio_product": null,
    "is_paid_partnership": false,
    "reshare_count": 8346,
    "ig_media_sharing_disabled": false,
    "media_repost_count": 4442,
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
          "profile_pic_url": "https://scontent-mad1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGB-qNzYmJRor7N8xX57vBVFllucQDYeHcHoaWZ4WJEDDi36eMJrcRqE3RlSiD1uFs&_nc_ohc=XbeNvhLXv28Q7kNvwH0Fih2&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0SZE3ClMzKm3K-TBHK7rJ6W7IRGCs52_UAsMYDpgTNfg&oe=69DC51E9&_nc_sid=55bbed"
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
    "like_count": 135430,
    "top_likers": [],
    "hidden_likes_string_variant": -1,
    "caption": {
      "strong_id__": "18065011298571522",
      "bit_flags": 0,
      "created_at": 1764453632,
      "created_at_utc": 1764453632,
      "did_report_as_spam": false,
      "is_ranked_comment": false,
      "pk": "18065011298571522",
      "share_enabled": false,
      "content_type": "comment",
      "media_id": 3776832898280228145,
      "status": "Active",
      "type": 1,
      "user_id": 787132,
      "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "pk_id": "787132",
        "id": "787132",
        "is_unpublished": false,
        "fbid_v2": 17841400573960012,
        "username": "natgeo",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-mad1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGB-qNzYmJRor7N8xX57vBVFllucQDYeHcHoaWZ4WJEDDi36eMJrcRqE3RlSiD1uFs&_nc_ohc=XbeNvhLXv28Q7kNvwH0Fih2&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0SZE3ClMzKm3K-TBHK7rJ6W7IRGCs52_UAsMYDpgTNfg&oe=69DC51E9&_nc_sid=55bbed"
      },
      "is_covered": false,
      "private_reply_status": 0,
      "text_translation": "Even the heaviest rain feels peaceful here. \n\n #HostilePlanet is now streaming on @DisneyPlus."
    },
    "comment_count": 485,
    "comment_inform_treatment": {
      "action_type": null,
      "should_have_inform_treatment": false,
      "text": "",
      "url": null
    },
    "is_photo_comments_composer_enabled_for_author": false,
    "hide_view_all_comment_entrypoint": true,
    "locations": [],
    "play_count": 2866120,
    "ig_play_count": 2866120,
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
    "video_duration": 22.31399917602539,
    "is_dash_eligible": 1,
    "video_versions": [
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 101,
        "url": "https://scontent-mad1-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEsBPe7&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0WjzLd_QhYWuAcbSqYt07kv0RcVoHNTW1MPgl91ZoaCw&oe=69D8376F",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 102,
        "url": "https://scontent-mad1-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEsBPe7&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0WjzLd_QhYWuAcbSqYt07kv0RcVoHNTW1MPgl91ZoaCw&oe=69D8376F",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657802\" FBManifestIdentifier=\"FpSNs50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZptKj+I+xz+4E3O24r9rS9QTcuPGuzcaQBZ6Kufaam8cF7JqyzN6dzAX8q/bF7erMBZrPsJvI77AGyNXq6vn18AfU7ZiEzZHnCp7r6/OozMkPIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgUbGF0YW1fbW9kZXJhdGVfZHJpcDIAFoICFAASFAIA\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"1563973005025935v\" bandwidth=\"337669\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"941843\" FBPlaybackResolutionMos=\"0:100,360:29.3,480:28.4,720:29.1,1080:31.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:70.9,480:62.6,720:50.4,1080:39.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-mad1-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN6p1XA_FXFLkUVYTtE8Zwx7keoWfwDMyx-B_QxL4pXgZeg8McEumkwF6WDJ4fnzDnBOTY9wUJL7oCRtGW6qjDxoh6M3Qq7Su4omI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad1-1.cdninstagram.com&amp;_nc_ohc=BfloUU35i64Q7kNvwFupMg4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjMzNzY2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1QtYFJiTF0at5H285HX1EYeiU-zDD1aOwl5F7uoZF7rQ&amp;oe=69DC3392</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-14042\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-89181\" FBFirstSegmentRange=\"891-165373\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"165374-688020\" FBPrefetchSegmentRange=\"891-165373\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1443772230413870v\" bandwidth=\"509752\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1421827\" FBPlaybackResolutionMos=\"0:100,360:40.4,480:38,720:37.2,1080:38.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:80.5,480:73.6,720:62.8,1080:52.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-mad1-1.cdninstagram.com/o1/v/t2/f2/m367/AQO03YPWFT70GHasKStspUo-nCsZakOgI61xyRI5dJ6BZRsyp4lBEZKTh7qJH33vHao8lA7Gz8jHRXP-xoDvVyNDrlzf18WIgj_ye2E.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad1-1.cdninstagram.com&amp;_nc_ohc=O1KjHuo6qEEQ7kNvwGgRMQv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUwOTc1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af36drTV9TxAmqHdWvARlldkHuF46O-4odjzMKDarKGppw&amp;oe=69DC2246</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-19700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-153929\" FBFirstSegmentRange=\"891-284632\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"284633-1049599\" FBPrefetchSegmentRange=\"891-284632\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3041551559367530v\" bandwidth=\"722308\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2014698\" FBPlaybackResolutionMos=\"0:100,360:51.1,480:47.8,720:45.4,1080:45.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.5,480:81.3,720:72.1,1080:62.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-mad1-1.cdninstagram.com/o1/v/t2/f2/m367/AQPSpcAxu8AB6FoUvT9edmiINl_OKU0kxsELupA-W7mtlP9_ucOO0LmcFcGoF7nFLPaLtxp6SODqMd31GQF9E68R4xCcOv91YV_Za6U.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad1-1.cdninstagram.com&amp;_nc_ohc=D5k1RwfW4qsQ7kNvwHHJKr1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjcyMjMwOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3WB4VFSn9VI8a1VjTkp-baf5F1MxQ92lVBZJXQqTsxAA&amp;oe=69DC3677</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-28550\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-246143\" FBFirstSegmentRange=\"891-439881\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"439882-1486392\" FBPrefetchSegmentRange=\"891-439881\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1576336420162302v\" bandwidth=\"989685\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2760477\" FBPlaybackResolutionMos=\"0:100,360:60.9,480:57,720:54.1,1080:53.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91,480:87.2,720:79.7,1080:71.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-mad1-1.cdninstagram.com/o1/v/t2/f2/m367/AQNWawONH_0ykNRhgXYD5USnUS-2JcDjQ0cKPtzUQ4bmPrDRMRJgACUHEnYvSCFWgDRdksntOheWe4DkpraAAYpYXQpEyt7yK9nS-5A.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad1-1.cdninstagram.com&amp;_nc_ohc=JGpaa8RbgzYQ7kNvwEkejX3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjk4OTY4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Y-hlppfihlm6tnIi7xHgXM30N4qKIda1Yc1KJDFFjcg&amp;oe=69DC2D08</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-36175\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-368341\" FBFirstSegmentRange=\"891-638853\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"638854-2015969\" FBPrefetchSegmentRange=\"891-638853\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1384606506359662v\" bandwidth=\"1369954\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3821143\" FBPlaybackResolutionMos=\"0:100,360:69.5,480:65.5,720:61.7,1080:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.2,480:91.7,720:86.3,1080:79.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-mad2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHjz86uKmkZFb6AfTAuNXhaCR5cY5lsEh1FSO9m1gsCdbf2BQ8JMp-g6pMIlhKv6fDPKpemYtUf_SuYjLt-9p7iIGYj7iVdOv9W4k.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad2-1.cdninstagram.com&amp;_nc_ohc=rfIPTL7SCmsQ7kNvwEJiV_H&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzNjk5NTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1TVKt6Qj2xpDHrzkTHdLDo4Zq--bsoK00Y1Y9BSAr-Kw&amp;oe=69DC297A</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-46923\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-542605\" FBFirstSegmentRange=\"891-915699\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"915700-2726908\" FBPrefetchSegmentRange=\"891-915699\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1369156268001513v\" bandwidth=\"1822480\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"5083349\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:71.6,720:67.7,1080:65.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:94.5,720:90.4,1080:85.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-mad2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMvyH-MQjdKfi00Fl5WSSH-1UKJzwFI8zT_5r_axCxb1zBFH7oejYKyu0sw6aikisn4kwP7Dvea3yfEnFbu9mGB_M3KNvNh7vkIxnY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad2-1.cdninstagram.com&amp;_nc_ohc=OQojGzvwWRUQ7kNvwHHITWj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE4MjI0ODAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1TsS1yWmyqqinMkuZyjJhgTWPq5W-_7Bq5-y1bWUw99w&amp;oe=69DC2E21</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-58146\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-759235\" FBFirstSegmentRange=\"891-1253416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1253417-3555514\" FBPrefetchSegmentRange=\"891-1253416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"2218641838658916v\" bandwidth=\"2563525\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"7150307\" FBPlaybackResolutionMos=\"0:100,360:81.3,480:77.1,720:73.4,1080:70.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.9,720:94.1,1080:90.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-mad2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6gX6iet6wVi2vwiQzpMYKnTkzyIOrnIhhWCeS_HxxTf5k1JEyxtDXBZl3W1nkz-gCcy90W_Uonp2gPqR_zfKL3rzkQ3beNg1DNR0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad2-1.cdninstagram.com&amp;_nc_ohc=ZhVzyNU6d_IQ7kNvwFZd0k8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI1NjM1MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1XNMlfPumTvz5jV--7Ds_7vhxz_JUe9LwLT_iqTlJqRw&amp;oe=69DC2E23</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-74586\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-1107880\" FBFirstSegmentRange=\"891-1794122\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1794123-4835105\" FBPrefetchSegmentRange=\"891-1794122\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mad2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad2-1.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwG9Rubv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1XGwL6izj9VK88xg-F3zoSm48mwhrkLFOzE5E9CH6IhQ&amp;oe=69DC2F41</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mad2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad2-1.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwEp4Khg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Fo2d73tNVx9gbqqKz_LakQgM9Gz2_puttP5tLUPAhwA&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-mad2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-mad2-1.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwFWY9ml&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4YSwcLQwujMOBY5I2VrFcw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ZVBWaHmDvOQ-KG0DfFs7M_Yg_qq9TRvBsHLVaRl84gw&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "number_of_qualities": 7,
    "video_codec": "vp09.00.30.08.00.02.02.01.00",
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null,
      "sharing_friction_payload": null
    },
    "gen_ai_detection_method": {
      "detection_method": "NONE"
    },
    "user": {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "feed_post_reshare_disabled": false,
      "id": "787132",
      "is_unpublished": false,
      "pk": 787132,
      "pk_id": "787132",
      "third_party_downloads_enabled": 2,
      "eligible_for_text_app_activation_badge": false,
      "account_type": 2,
      "account_badges": [],
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
        "followed_by": false,
        "is_muting_reel": false
      },
      "has_anonymous_profile_picture": false,
      "is_favorite": false,
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-mad1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGB-qNzYmJRor7N8xX57vBVFllucQDYeHcHoaWZ4WJEDDi36eMJrcRqE3RlSiD1uFs&_nc_ohc=XbeNvhLXv28Q7kNvwH0Fih2&_nc_gid=4YSwcLQwujMOBY5I2VrFcw&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0SZE3ClMzKm3K-TBHK7rJ6W7IRGCs52_UAsMYDpgTNfg&oe=69DC51E9&_nc_sid=55bbed",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775583063,
      "user_activation_info": {}
    },
    "community_notes_info": {
      "has_viewer_submitted_note": false,
      "note_submission_disabled": false,
      "enable_submission_friction": false,
      "is_eligible_for_request_a_note": true
    },
    "has_high_risk_gen_ai_inform_treatment": false,
    "caption_is_edited": false,
    "code": "DRqAYKuAIUx",
    "device_timestamp": 1764453587369,
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
  },
  "status": "ok"
}
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
              "sprite_width": 1500,
              "thumbnail_duration": 0.21250476190476,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "video_length": 22.313
            }
          }
        },
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657808\" FBManifestIdentifier=\"FqCNs50NGBBpZ19kYXNoX2Jhc2VsaW5lGTaI0eK/0NmNA/C698/T17UF7KyC/a+71QUiGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABaCAhQAEhQAAA==\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"2\"/><Representation id=\"1525428988604088v\" bandwidth=\"2268538\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"6327492\" FBPlaybackResolutionMos=\"0:100,360:94.2,480:90.6,720:82.4,1080:75.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.6,720:94.1,1080:90\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/499\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=Ey9Zfx1FVawQ7kNvwE0M_w7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjg1MzgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=BvaGzcv8f72V91p6-OM-vQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0S4h1_2EFYSRpYkEGEz0VGJwSXnA2K0SKM95Xn_fS_MA&amp;oe=69D8376F</BaseURL><SegmentBase indexRange=\"874-965\" timescale=\"11988\" FBMinimumPrefetchRange=\"966-82009\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-832807\" FBFirstSegmentRange=\"966-1651564\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1651565-4297059\" FBPrefetchSegmentRange=\"966-1651564\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-873\"/></SegmentBase></Representation><Representation id=\"1595311911881526v\" bandwidth=\"516706\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"1441216\" FBPlaybackResolutionMos=\"0:100,360:70.1,480:64.5,720:55.5,1080:44.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:84.8,480:79.7,720:70.5,1080:59.6\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"11988/499\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQPT958-vWmEXFo_grVlw2vnBqTKdk9uQHmeTNkCIIC7NdKkZPEJWGTrwPpf3FSw4zpEJJauBM-jUYof9m2tdkX55bI8s38qZHGbGV4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=QwCnrPhQZCAQ7kNvwF9kxRr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUxNjcwNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=BvaGzcv8f72V91p6-OM-vQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3mzPMrssGHPNQULI5-77VFaf55SYmDr996LsdYaO6OSw&amp;oe=69D84B1B</BaseURL><SegmentBase indexRange=\"869-960\" timescale=\"11988\" FBMinimumPrefetchRange=\"961-23752\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-145022\" FBFirstSegmentRange=\"961-317467\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"317468-1041332\" FBPrefetchSegmentRange=\"961-317467\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-868\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"874552045098052a\" bandwidth=\"46857\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46857\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"131698\" FBPaqMos=\"86.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPkB7GmtjggjHEJa-kd2XK21HSs5MPOBh8Kn_V_b6gCkSbQo9RxM5qstTSXAhy-_70SQiuAW02OQtBnYlPkvoo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=ZSfr4AA8_vgQ7kNvwGKkiiQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ3MjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=BvaGzcv8f72V91p6-OM-vQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2QD7lhlXopil9AlyZIEPfQ-qg6Ek6EZ7ezZ0RVL0_apQ&amp;oe=69D859DB</BaseURL><SegmentBase indexRange=\"824-999\" timescale=\"48000\" FBMinimumPrefetchRange=\"1000-1360\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1000-14536\" FBFirstSegmentRange=\"1000-12223\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"12224-22571\" FBPrefetchSegmentRange=\"1000-22571\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "has_audio": true,
        "like_count": 135430,
        "locations": [],
        "is_dash_eligible": 1,
        "is_unified_video": true,
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "enable_media_notes_production": true,
        "play_count": 2866120,
        "ig_play_count": 2866120,
        "is_third_party_downloads_eligible": false,
        "original_width": 720,
        "original_height": 1280,
        "is_reuse_allowed": false,
        "has_shared_to_fb": 0,
        "reshare_count": 8346,
        "has_privately_liked": false,
        "ig_media_sharing_disabled": false,
        "original_media_has_visual_reply_media": false,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQUZyaXNGZGwwUWtaSHZKdWcydE1wOEozNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY1NzgwOTIxOHwzNzc2ODMyODk4MjgwMjI4MTQ1fDc4NzEzMnw4MTFlYzIwOTY3MTY4YzU1YTQyMzQ4YjEyYzg5OTQ2YzliYWQ3ZjA5NGIzZjBhMmM2OTU0MmMzMjE3Mzc1OGRiIn0sInNpZ25hdHVyZSI6IiJ9",
        "has_views_fetching": true,
        "video_duration": 22.314,
        "is_post_live_clips_media": false,
        "is_quiet_post": false,
        "is_comments_gif_composer_enabled": false,
        "has_high_risk_gen_ai_inform_treatment": false,
        "clips_tab_pinned_user_ids": [],
        "clips_metadata": {
          "achievements_info": {
            "show_achievements": false
          },
          "additional_audio_info": {
            "audio_reattribution_info": {
              "should_allow_restore": false
            }
          },
          "audio_ranking_info": {
            "best_audio_cluster_id": "807850148748818"
          },
          "audio_type": "original_sounds",
          "basel_template_info_for_ig_app": {
            "should_show_reuse_setting_for_owner": false
          },
          "branded_content_tag_info": {
            "can_add_tag": false
          },
          "clips_creation_entry_point": "",
          "content_appreciation_info": {
            "enabled": false
          },
          "cutout_sticker_info": [],
          "disable_use_in_clips_client_cache": false,
          "is_fan_club_promo_video": false,
          "is_public_chat_welcome_video": false,
          "is_shared_to_fb": false,
          "mashup_info": {
            "can_toggle_mashups_allowed": false,
            "has_been_mashed_up": false,
            "has_nonmimicable_additional_audio": false,
            "is_creator_requesting_mashup": false,
            "is_light_weight_check": true,
            "is_pivot_page_available": false,
            "is_light_weight_reuse_allowed_check": false,
            "is_reuse_allowed": false,
            "mashups_allowed": false,
            "non_privacy_filtered_mashups_media_count": 0
          },
          "music_canonical_id": "18539901727003707",
          "original_sound_info": {
            "is_eligible_for_vinyl_sticker": true,
            "allow_creator_to_rename": true,
            "overlap_duration_in_ms": 0,
            "audio_asset_start_time_in_ms": 0,
            "derived_content_start_time_in_composition_in_ms": 0,
            "audio_asset_id": 25124554117202919,
            "audio_parts": [],
            "audio_parts_by_filter": [],
            "can_remix_be_shared_to_fb": true,
            "can_remix_be_shared_to_fb_expansion": true,
            "consumption_info": {
              "is_bookmarked": false,
              "is_trending_in_clips": false,
              "should_mute_audio_reason": ""
            },
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775657808\" FBManifestIdentifier=\"FqCNs50NKRaI0eK/0NmNAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"874552045098052a\" bandwidth=\"46857\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46857\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQPkB7GmtjggjHEJa-kd2XK21HSs5MPOBh8Kn_V_b6gCkSbQo9RxM5qstTSXAhy-_70SQiuAW02OQtBnYlPkvoo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=ZSfr4AA8_vgQ7kNvwGKkiiQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6LTEsImNsaWVudF9uYW1lIjoidW5rbm93biIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJiaXRyYXRlIjo0NzIxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=BvaGzcv8f72V91p6-OM-vQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2QD7lhlXopil9AlyZIEPfQ-qg6Ek6EZ7ezZ0RVL0_apQ&amp;oe=69D859DB</BaseURL><SegmentBase indexRange=\"824-999\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "duration_in_ms": 22313,
            "hide_remixing": false,
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            },
            "ig_artist": {
              "pk_id": "787132",
              "id": "787132",
              "full_name": "National Geographic",
              "is_private": false,
              "is_verified": true,
              "pk": 787132,
              "profile_pic_id": "3865702555259028436_787132",
              "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=1&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwG_zDyJ&_nc_oc=AdqhOK0xYiEjYw3V5fDf7G5WmFRCqlD4MTopjxp9VZTjm4VjHFM-K8MHS5nzKegSKKA&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af31ZVOqMZDmch7tobQOvTnsCSUqYbC9Q_y7anVV-CHUSg&oe=69DC51E9",
              "username": "natgeo",
              "strong_id__": "787132"
            },
            "is_audio_automatically_attributed": false,
            "is_eligible_for_audio_effects": true,
            "is_explicit": false,
            "is_original_audio_download_eligible": false,
            "is_reuse_disabled": true,
            "is_xpost_from_fb": false,
            "oa_owner_is_music_artist": false,
            "original_audio_subtype": "default",
            "original_audio_title": "Original audio",
            "original_media_id": 3776832898280228145,
            "progressive_download_url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m69/AQNUQxQiFbTUd-NpZIcRNmMnc9S2fKRmilHMmVeP5Hg1uelz4pX6ycUwiSbbH3ZIlgtpB73IB_VLHDvX8YgT4zPM.mp4?strext=1&_nc_cat=104&_nc_sid=8bf8fe&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=NAtNUSzzeGkQ7kNvwG9EP8H&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af1nsw_YI_ug4_llmvwAJl4PviP8JwD8X3vDBaYKg3BUSg&oe=69DC23AE",
            "should_mute_audio": false,
            "time_created": 1764453634
          },
          "professional_clips_upsell_type": 0,
          "show_achievements": false
        },
        "collaborator_edit_eligibility": false,
        "number_of_qualities": 2,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "is_artist_pick": false,
        "translated_langs_for_autodub": [],
        "subtype_name_for_REST__": "XDTClipsMedia",
        "is_eligible_for_poe": true,
        "eligible_insights_entrypoints": "NONE",
        "clips_demotion_control": {
          "confirmation_body": "We'll suggest fewer posts like this.",
          "confirmation_icon": "none",
          "confirmation_style": "bottomsheet",
          "confirmation_title": "Post hidden",
          "confirmation_title_style": "large_left",
          "enable_word_wrapping": true,
          "followup_options": [
            {
              "data": "author_id:787132",
              "demotion_control": {
                "confirmation_body": "We won't suggest posts from natgeo.",
                "confirmation_icon": "eye-off-pano",
                "confirmation_style": "bottomsheet",
                "undo_style": "inline"
              },
              "id": "dislike_author",
              "show_icon": true,
              "text": "Don't suggest posts from natgeo"
            },
            {
              "id": "hide_all_specific_words",
              "show_icon": true,
              "text": "Don't suggest posts with certain words"
            }
          ],
          "title": "Not interested",
          "title_style": "normal",
          "undo_style": "top_right"
        },
        "hidden_likes_string_variant": -1,
        "is_social_ufi_disabled": false,
        "client_cache_key": "Mzc3NjgzMjg5ODI4MDIyODE0NQ==.3",
        "can_reply": false,
        "media_repost_count": 4442,
        "media_attributions_data": [],
        "media_ui_attributions_data": [],
        "creator_product_link_infos": [],
        "can_view_more_preview_comments": false,
        "video_codec": "avc1.64001f",
        "mezql_token": "",
        "has_tagged_users": false,
        "is_eligible_content_for_post_roll_ad": false,
        "is_cutout_sticker_allowed": false,
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
        "has_liked": false,
        "is_organic_product_tagging_eligible": true,
        "view_state_item_type": 128,
        "top_likers": [],
        "video_sticker_locales": [],
        "is_paid_partnership": false,
        "is_in_profile_grid": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "integrity_review_decision": "pending",
        "has_delayed_metadata": false,
        "filter_type": 0,
        "deleted_reason": 0,
        "device_timestamp": 1764453587369,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "timeline_pinned_user_ids": [],
        "is_open_to_public_submission": false,
        "profile_grid_control_enabled": false,
        "can_see_insights_as_brand": false,
        "media_reposter_bottomsheet_enabled": false,
        "coauthor_producer_can_see_organic_insights": false,
        "share_count_disabled": false,
        "is_visual_reply_commenter_notice_enabled": true,
        "should_request_ads": false,
        "subscribe_cta_visible": false,
        "commerce_integrity_review_decision": "",
        "sharing_friction_info": {
          "should_have_sharing_friction": false
        },
        "media_notes": {
          "items": []
        },
        "fb_user_tags": {
          "in": []
        },
        "coauthor_producers": [],
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "cutout_sticker_info": [],
        "invited_coauthor_producers": [],
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "floating_context_items": [],
        "comment_inform_treatment": {
          "should_have_inform_treatment": false,
          "text": ""
        },
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "caption": {
          "strong_id__": "18065011298571522",
          "pk": "18065011298571522",
          "bit_flags": 0,
          "content_type": "comment",
          "created_at": 1764453632,
          "created_at_utc": 1764453632,
          "did_report_as_spam": false,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": 3776832898280228145,
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
          "type": 1,
          "user": {
            "id": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=1&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwG_zDyJ&_nc_oc=AdqhOK0xYiEjYw3V5fDf7G5WmFRCqlD4MTopjxp9VZTjm4VjHFM-K8MHS5nzKegSKKA&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af31ZVOqMZDmch7tobQOvTnsCSUqYbC9Q_y7anVV-CHUSg&oe=69DC51E9",
            "fbid_v2": 17841400573960012,
            "is_unpublished": false,
            "strong_id__": "787132"
          },
          "user_id": 787132
        },
        "report_info": {
          "has_viewer_submitted_report": false
        },
        "meta_ai_suggested_prompts": [],
        "user": {
          "id": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "fbid_v2": 17841400573960012,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=1&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwG_zDyJ&_nc_oc=AdqhOK0xYiEjYw3V5fDf7G5WmFRCqlD4MTopjxp9VZTjm4VjHFM-K8MHS5nzKegSKKA&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af31ZVOqMZDmch7tobQOvTnsCSUqYbC9Q_y7anVV-CHUSg&oe=69DC51E9",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "is_ring_creator": false,
          "show_ring_award": false,
          "account_badges": [],
          "account_type": 2,
          "has_anonymous_profile_picture": false,
          "latest_reel_media": 1775583063,
          "is_embeds_disabled": false,
          "strong_id__": "787132",
          "eligible_for_text_app_activation_badge": false,
          "interop_messaging_user_fbid": "113671860027320",
          "show_account_transparency_details": true,
          "transparency_product_enabled": false,
          "third_party_downloads_enabled": 2,
          "feed_post_reshare_disabled": false,
          "is_favorite": false,
          "friendship_status": {
            "following": false,
            "is_bestie": false,
            "is_feed_favorite": false,
            "is_private": false,
            "is_restricted": false,
            "is_muting_reel": false,
            "followed_by": false
          },
          "fan_club_info": {},
          "user_activation_info": {}
        }
      }
    }
  ],
  "metadata": {
    "template_clips_media_creator": "natgeo",
    "clips_count": "1 reel",
    "image_versions2": {
      "additional_candidates": {
        "first_frame": {
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGWwcXX&_nc_oc=Ado-A2vQBmUFKGBDfI56Wb_IHzPBlkfp_h78h5E8NNBs7l8q3CblKbaEPE0rt2Ls-i4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af3TEQWHLkzG67UwYgyNnzt3i8W14TlFcbpkjy8z-VVeBw&oe=69DC368F",
          "width": 640
        },
        "igtv_first_frame": {
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwGWwcXX&_nc_oc=Ado-A2vQBmUFKGBDfI56Wb_IHzPBlkfp_h78h5E8NNBs7l8q3CblKbaEPE0rt2Ls-i4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af3TEQWHLkzG67UwYgyNnzt3i8W14TlFcbpkjy8z-VVeBw&oe=69DC368F",
          "width": 640
        }
      },
      "candidates": [
        {
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFgTVfS&_nc_oc=AdpLHoQLXfU0rKWVlWACiYKacy41KnAciNOOdzVeK2iP-h6e1-V0dmyJzUetHDnP_lo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=BvaGzcv8f72V91p6-OM-vQ&_nc_ss=7a3ba&oh=00_Af34OC2Cb-tVsO0XqwIq-aHSHhEV-k9tyA3wt-_GXm3yjw&oe=69DC3E7E",
          "width": 750
        }
      ],
      "scrubber_spritesheet_info_candidates": {
        "default": {
          "file_size_kb": 428,
          "max_thumbnails_per_sprite": 105,
          "rendered_width": 96,
          "sprite_height": 1232,
          "sprite_width": 1500,
          "thumbnail_duration": 0.21250476190476,
          "thumbnail_height": 176,
          "thumbnail_width": 100,
          "thumbnails_per_row": 15,
          "total_thumbnail_num_per_sprite": 105,
          "video_length": 22.313
        }
      }
    },
    "template_title": "Original template"
  },
  "paging_info": {
    "max_id": "GhbilITg1eCA6mgm3M-f161nFAI0AikIGAAaCDoGGQwA",
    "more_available": true
  },
  "status": "ok",
  "status_code": "200"
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-media){ target=_blank }
