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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/by/code",
        headers={"x-access-key": "YOUR_TOKEN"},
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
              13678,
              20517
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwH4sfmQ&_nc_oc=Adplu60MXv67YX9WwJ0vXE0YfC3dCTuS6HPN5ev3hd_tTHs-FtwuAVipAVsBdor6HmY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=PiKeHux56scnCksO0eNNdA&_nc_ss=7a3ba&oh=00_Af2cQrxSV88SFzxUM0uQYjduZmwGhRmQUX8YdhWoO4OV5w&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "igtv_first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678,
              20517
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwH4sfmQ&_nc_oc=Adplu60MXv67YX9WwJ0vXE0YfC3dCTuS6HPN5ev3hd_tTHs-FtwuAVipAVsBdor6HmY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=PiKeHux56scnCksO0eNNdA&_nc_ss=7a3ba&oh=00_Af2cQrxSV88SFzxUM0uQYjduZmwGhRmQUX8YdhWoO4OV5w&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "smart_frame": null
        },
        "candidates": [
          {
            "estimated_scans_sizes": [
              27870,
              55740,
              83610
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwH9kd6l&_nc_oc=AdpFdrHUZoGP_P4clc65ZCdimOh4UALsg6WxV1sVowxethVExC_T-OKX8H3z3od1QyY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=PiKeHux56scnCksO0eNNdA&_nc_ss=7a3ba&oh=00_Af0h64qUHxx8Ty30kIUSMu4DhpEhDJ2R7I1yipsC--LLtg&oe=69DC3E7E",
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
              "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFXpwQoUM6Ggz7yu9D-B7SaPVvujUPiZkTIw1lz7YXw-1GMRA1_oArIHov-7ugZHF8&_nc_ohc=7fRK9vLZo4UQ7kNvwGtq7Gr&_nc_gid=PiKeHux56scnCksO0eNNdA&edm=ALQROFkBAAAA&ccb=7-5&oh=00_Af1BAF5txfoWCVWBQSKrvK1A8a4xnvhV5RGx4YoY78_Odw&oe=69DC4C8A&_nc_sid=fc8dfb"
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
      "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZjNjNTJhNDA4NTg1NDhiMDk4NjM1NjliODEyYzVjZGMzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2Mzk2NzgzNnwzNzc2ODMyODk4MjgwMjI4MTQ1fDM1ODkwMjcxNjU4fGNiMTc5OGU1YTQ0ZDlkMTM1NzYzNmYwZmMwNTQ4ZGQ4ZmEwZmFjODQ4YzI5ZWZmMTM4M2ZjZDFkMDI5Y2M1MmYifSwic2lnbmF0dXJlIjoiIn0=",
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
            "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFXpwQoUM6Ggz7yu9D-B7SaPVvujUPiZkTIw1lz7YXw-1GMRA1_oArIHov-7ugZHF8&_nc_ohc=XbeNvhLXv28Q7kNvwH37-Ni&_nc_gid=PiKeHux56scnCksO0eNNdA&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2uzSZTLgLTDFUusUdd7tg8PWE8mhvfBgnte32ohBta_Q&oe=69DC51E9&_nc_sid=fc8dfb"
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
      "like_count": 135429,
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
          "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFXpwQoUM6Ggz7yu9D-B7SaPVvujUPiZkTIw1lz7YXw-1GMRA1_oArIHov-7ugZHF8&_nc_ohc=XbeNvhLXv28Q7kNvwH37-Ni&_nc_gid=PiKeHux56scnCksO0eNNdA&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2uzSZTLgLTDFUusUdd7tg8PWE8mhvfBgnte32ohBta_Q&oe=69DC51E9&_nc_sid=fc8dfb"
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
          "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwELt6iz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=PiKeHux56scnCksO0eNNdA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af284rexbM8OT5E4o1AcA2g9WBNe2506gJnuntyp03tABw&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 102,
          "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwELt6iz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=PiKeHux56scnCksO0eNNdA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af284rexbM8OT5E4o1AcA2g9WBNe2506gJnuntyp03tABw&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 103,
          "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwELt6iz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=PiKeHux56scnCksO0eNNdA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af284rexbM8OT5E4o1AcA2g9WBNe2506gJnuntyp03tABw&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663967\" FBManifestIdentifier=\"Fr7ts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxozhmaSP8rACovXRl+ao3wKKjIn135CYA5665tXdzJYE6rO+3tWCgQXOuqeDzoi9BeyasszencwFms+wm8jvsAaKn4CC49CdB8SwgOTBoeoH3JLz6tnu0gie6+vzqMzJDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWggIUABIUAgA=\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwFaKogl&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ZIucmo7asiWwiSyhbKeZUFTk9dDkUsAQzJALwKyu0PQ&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=bCouttTbvR0Q7kNvwHqI_Fk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3TEueqmjhSK01RBjPbtU6UQOEPavpKhi_FpQmxeuboRg&amp;oe=69DC6069</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwG75KhC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0hlpjTcIwBxT4IFjSz0x9npVGaOIfAx8CpbjLZgOYsMQ&amp;oe=69DC5940</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwFn9SBF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0XfiQkl0dgX42-SdxkF-J7Fzx4_ujQDLcGIwxkevuSxg&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwF3hNhu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2VnagI84x6VbaOldDb5bCb4DUl07Kkd9hSLwYY2bx0Gw&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwGanWIz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2hNKtVwQ2FrIveDhea98mYzlyZdHnpJq-_SLF5DoKSYg&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwHLRxr4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3FF6w2wJJz2mGsYq6RPqDqXxSeXb8IboSMorkCDTv44Q&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"897489239614213v\" bandwidth=\"4472890\" codecs=\"av01.0.08M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"12475999\" FBPlaybackResolutionMos=\"0:100,360:87.2,480:83.7,720:78.9,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.536,480:99.415,720:99.167,1080:98.58\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPVgubbzL4GsEHBto9qJ9DKVHDYdRJUIBrbusVYgthsUApFExMmHIPHOP4-rKP0NJU5hwD7ETkAkZNePbo3qf5TReJDHCiOkPRu_hM.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=PMWR1v3uaAgQ7kNvwHeJVKK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ0NzI4OTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3OT5cZNGU-Yj3Gyh9QnWjDNOthxw6zdfYmPwmOk-4p5g&amp;oe=69DC5E06</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-105462\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-2456793\" FBFirstSegmentRange=\"899-3691660\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"3691661-8660328\" FBPrefetchSegmentRange=\"899-3691660\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwFiKWD2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0roKUzEjr5B_ep-L8F2A-Z_poFInvUAzY_BmQaT0VmSA&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwHEa69A&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1LH7VgTUvbHi-AWOmKPFmdZEBNxYWEy0zyz0u4paf0Mw&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwFHtmI_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0luTUXPJwNIoRI6DGcNCw8-I5F9bh-JjU_uD8zILio3g&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwGuasCU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=PiKeHux56scnCksO0eNNdA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ZxS11PujXrzq9inPg4gRIkOUBlLUYDbM5aGIUj4y_dg&amp;oe=69DC5283</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFXpwQoUM6Ggz7yu9D-B7SaPVvujUPiZkTIw1lz7YXw-1GMRA1_oArIHov-7ugZHF8&_nc_ohc=XbeNvhLXv28Q7kNvwH37-Ni&_nc_gid=PiKeHux56scnCksO0eNNdA&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2uzSZTLgLTDFUusUdd7tg8PWE8mhvfBgnte32ohBta_Q&oe=69DC51E9&_nc_sid=fc8dfb",
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "username": "natgeo",
        "text_post_app_is_private": false,
        "is_active_on_text_post_app": true,
        "latest_reel_media": 1775659002,
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
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
              13678,
              20517
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-fra5-2.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFnDlpJ&_nc_oc=Adq8OjE-E2KCAcdyIpEbXKCUV5GXypxD6ONd3Dfr7qF4gHfYCVd5SA3HWCJ53dooSDc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_gid=rigOKZhp8VVXDZVlOS77mg&_nc_ss=7a3ba&oh=00_Af2xh1P_QC78Rzol2vE5wkVaH5UUvvwLH051o4SxIO5-ZQ&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "igtv_first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678,
              20517
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-fra5-2.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFnDlpJ&_nc_oc=Adq8OjE-E2KCAcdyIpEbXKCUV5GXypxD6ONd3Dfr7qF4gHfYCVd5SA3HWCJ53dooSDc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_gid=rigOKZhp8VVXDZVlOS77mg&_nc_ss=7a3ba&oh=00_Af2xh1P_QC78Rzol2vE5wkVaH5UUvvwLH051o4SxIO5-ZQ&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "smart_frame": null
        },
        "candidates": [
          {
            "estimated_scans_sizes": [
              27870,
              55740,
              83610
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwExc08O&_nc_oc=AdpGewr5QEJby3AiN2Ri18KaYIJmJGgFX1e0fx9ve2XNYKjyoBHyeTrCxz9G42HeOck&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=rigOKZhp8VVXDZVlOS77mg&_nc_ss=7a3ba&oh=00_Af2ol53fXi5Amt0-yCuYVWBhZsZQH3mjJA6oKA63tuUMlA&oe=69DC3E7E",
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
              "https://scontent-fra3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gH9xuZ-jWuVNY-yZadysL3I79ryjoc6GyGVd366s6GzfVNLDqcx1YX5ywEHyYy_4FU&_nc_ohc=7fRK9vLZo4UQ7kNvwEovxTF&_nc_gid=rigOKZhp8VVXDZVlOS77mg&edm=ALQROFkBAAAA&ccb=7-5&oh=00_Af3xMixvGWoQC46fNdph4Q-IDhoADtKf2hkcYLq7el4Eqg&oe=69DC4C8A&_nc_sid=fc8dfb"
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
      "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiZjhhZmQyNTgwYWVkNGFiMThlZGJiOTIwZGMyNGM1YzMzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2Mzk2ODYyNnwzNzc2ODMyODk4MjgwMjI4MTQ1fDMzOTEzNjA1NDc5fDY3NDEyODBkZTk4ZmJlNzVhNTBiNjJjN2MyYWU4Y2E3ZjM3MzMwMWE3ODg4ZWQ3NzZiMGFiMTUxZjBmZTU0YjIifSwic2lnbmF0dXJlIjoiIn0=",
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
            "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH9xuZ-jWuVNY-yZadysL3I79ryjoc6GyGVd366s6GzfVNLDqcx1YX5ywEHyYy_4FU&_nc_ohc=XbeNvhLXv28Q7kNvwEpAgkz&_nc_gid=rigOKZhp8VVXDZVlOS77mg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af03t9txgD6E81aKFnSOtA4O_UkuYVQlQuZgHRzq4PsH5w&oe=69DC51E9&_nc_sid=fc8dfb"
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
      "like_count": 135429,
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
          "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH9xuZ-jWuVNY-yZadysL3I79ryjoc6GyGVd366s6GzfVNLDqcx1YX5ywEHyYy_4FU&_nc_ohc=XbeNvhLXv28Q7kNvwEpAgkz&_nc_gid=rigOKZhp8VVXDZVlOS77mg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af03t9txgD6E81aKFnSOtA4O_UkuYVQlQuZgHRzq4PsH5w&oe=69DC51E9&_nc_sid=fc8dfb"
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
          "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=rigOKZhp8VVXDZVlOS77mg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2jWAPhcLMyndGtasktae1QCj_awBMMtEhu_mZ3a7zdrA&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 102,
          "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=rigOKZhp8VVXDZVlOS77mg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2jWAPhcLMyndGtasktae1QCj_awBMMtEhu_mZ3a7zdrA&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 103,
          "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=rigOKZhp8VVXDZVlOS77mg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2jWAPhcLMyndGtasktae1QCj_awBMMtEhu_mZ3a7zdrA&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663968\" FBManifestIdentifier=\"FsDts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtozhmaSP8rACovXRl+ao3wKeuubV3cyWBOqzvt7VgoEFzrqng86IvQXsmrLM3p3MBZrPsJvI77AGip+AguPQnQfEsIDkwaHqB9yS8+rZ7tIInuvr86jMyQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2ggIUABIUAgA=\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwFcSRLc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af251EJizEN9bwCFzQC20dE9EXDBvrlnPXlec4dIV7_A0Q&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=bCouttTbvR0Q7kNvwHnZk01&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1AGg_EOHW77th9G9ftf5XO1GXLWTZNkxFGvV7IYjkCSA&amp;oe=69DC6069</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwHkxtuX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2vxMk-9AxpX3zUcEL4Tk4tJ6_YBGHS8rMhdckf_RW_zA&amp;oe=69DC5940</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwETlGZ6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2fAsTWU0jS9jyDeGKXIo5zmxw7THTe2YmSiDcwHhq1Qw&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwGC73yn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0HOAqX8sP_r0X0DuXn6LdkpI4g8duHBmd0JAZAovPtSw&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwGfm6hH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1s3W4SZl47VdZsdNIDbW9E5SGtfKA5eKGpcFrLmv4ghw&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwFG4g10&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1DEBLfUmECQ4S3KhRxoMWS-XzrHAIcdKacf4srVmKk8w&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwGp5mTY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1qmxgDt6_7UnXZvBiA6TQ7JsQIYC8CO8VZkYlof9ZHuQ&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-2.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwF-JKa8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ZX-TsBidOj_V4kXf9F8fiPFuwA4z2h5630ZmTzlrN2g&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwGtAQKR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2XpfrAFDmQO0tLmYCJwxxkp_cBj4UjEGq1mxB70aHEUg&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwEhHuDg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=rigOKZhp8VVXDZVlOS77mg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2d6mNI1mtiBThi8TaURiTTa-Elqq1sYieh-3hCUbHsNA&amp;oe=69DC5283</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "number_of_qualities": 7,
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
        "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH9xuZ-jWuVNY-yZadysL3I79ryjoc6GyGVd366s6GzfVNLDqcx1YX5ywEHyYy_4FU&_nc_ohc=XbeNvhLXv28Q7kNvwEpAgkz&_nc_gid=rigOKZhp8VVXDZVlOS77mg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af03t9txgD6E81aKFnSOtA4O_UkuYVQlQuZgHRzq4PsH5w&oe=69DC51E9&_nc_sid=fc8dfb",
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "username": "natgeo",
        "text_post_app_is_private": false,
        "is_active_on_text_post_app": true,
        "latest_reel_media": 1775659002,
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
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
              13678,
              20517
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHv2CBx&_nc_oc=AdryoSd338QS-ndvWI-y68ykrsJL2RdXchiV3K7atnGvnpWbUf25ASJoIPxgNvh2VY4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=P_m-q4sI0e8e5fri6veJMg&_nc_ss=7a3ba&oh=00_Af1Wxv3G0QC2PwEn-U9yBPiLxTszMrLHAyUEHpk7WBgC7w&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "igtv_first_frame": {
            "estimated_scans_sizes": [
              6839,
              13678,
              20517
            ],
            "height": 1136,
            "scans_profile": "e15",
            "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwHv2CBx&_nc_oc=AdryoSd338QS-ndvWI-y68ykrsJL2RdXchiV3K7atnGvnpWbUf25ASJoIPxgNvh2VY4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=P_m-q4sI0e8e5fri6veJMg&_nc_ss=7a3ba&oh=00_Af1Wxv3G0QC2PwEn-U9yBPiLxTszMrLHAyUEHpk7WBgC7w&oe=69DC368F",
            "width": 640,
            "is_spatial_image": false
          },
          "smart_frame": null
        },
        "candidates": [
          {
            "estimated_scans_sizes": [
              27870,
              55740,
              83610
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwHvi1sE&_nc_oc=AdouT8DjYHCdUO5T-TkwO57M1tRluSCKJ1FeBVMF_HeWHDFMsITL-n-tcPjEajEdTFs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=P_m-q4sI0e8e5fri6veJMg&_nc_ss=7a3ba&oh=00_Af2wkvOhiI-i8kDaZzJVvwnzwdXZhY3KXDKVJjggq2M1Gg&oe=69DC3E7E",
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
              "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFotTxQmMsM3NGLs-OQr5aRp6G675KQB1FvfrrE1NnU1iYLXByCqG8Ftk29T3BlsNQ&_nc_ohc=7fRK9vLZo4UQ7kNvwGHrAbs&_nc_gid=P_m-q4sI0e8e5fri6veJMg&edm=ALQROFkBAAAA&ccb=7-5&oh=00_Af3P1NBiaZrJamdqUBo3zieYU7TRjUlxFQJ9uBVCh0C2kA&oe=69DC4C8A&_nc_sid=fc8dfb"
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
      "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMWExNjRmZjg2ODM3NDdjNWEyYTkzMzQzNzNhM2U2MDQzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2Mzk2OTQ2OHwzNzc2ODMyODk4MjgwMjI4MTQ1fDM5MzM4NTEzNjQ3fDlkYzk0YjAwMGM1ZWVlZTY3YzRiNWJjMWQxOTRiNGQwY2FlNDc1NjcyYjEzOWQxZjUxMTI4NjFkYjE0YTE3MGYifSwic2lnbmF0dXJlIjoiIn0=",
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
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFotTxQmMsM3NGLs-OQr5aRp6G675KQB1FvfrrE1NnU1iYLXByCqG8Ftk29T3BlsNQ&_nc_ohc=XbeNvhLXv28Q7kNvwGaY1se&_nc_gid=P_m-q4sI0e8e5fri6veJMg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2cn7uiHefjW7Lt0P9EshzzQ3mI1Z7reF_9CTZd9MHYJQ&oe=69DC51E9&_nc_sid=fc8dfb"
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
      "like_count": 135429,
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
          "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFotTxQmMsM3NGLs-OQr5aRp6G675KQB1FvfrrE1NnU1iYLXByCqG8Ftk29T3BlsNQ&_nc_ohc=XbeNvhLXv28Q7kNvwGaY1se&_nc_gid=P_m-q4sI0e8e5fri6veJMg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2cn7uiHefjW7Lt0P9EshzzQ3mI1Z7reF_9CTZd9MHYJQ&oe=69DC51E9&_nc_sid=fc8dfb"
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
          "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwGUUOUW&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=P_m-q4sI0e8e5fri6veJMg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af22XOLr8WM1pYWvKvvMuh97iPGEhG7Fmf9tnHYk0xj9Kw&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 102,
          "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwGUUOUW&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=P_m-q4sI0e8e5fri6veJMg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af22XOLr8WM1pYWvKvvMuh97iPGEhG7Fmf9tnHYk0xj9Kw&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 2315752,
          "height": 1280,
          "id": "1525428988604088v",
          "type": 103,
          "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwGUUOUW&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=P_m-q4sI0e8e5fri6veJMg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af22XOLr8WM1pYWvKvvMuh97iPGEhG7Fmf9tnHYk0xj9Kw&oe=69D86FAF",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        }
      ],
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663969\" FBManifestIdentifier=\"FsLts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtozhmaSP8rACovXRl+ao3wKeuubV3cyWBOqzvt7VgoEFzrqng86IvQXsmrLM3p3MBZrPsJvI77AGip+AguPQnQfEsIDkwaHqB9yS8+rZ7tIInuvr86jMyQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyIsGRgFbGlnaHQAFoICFAASFAIA\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwEQZV7P&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0QGTx1_EWlC5-mH-sHzBK-o5CvlqRxeqToNvmuj4HQwg&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=bCouttTbvR0Q7kNvwEJWib5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3kN40tJTVWPa1VtImJxb_vC80fRYZMB_7f8uhQqOTD2g&amp;oe=69DC6069</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwE9KoKu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1igHzx8t3zH3MoQl3K4SgPoksMkKvtg85iexk81x49fg&amp;oe=69DC5940</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwGBKyB3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ZCTEd8vAaVjUHrt-GeWLBgincW5vBzQgIaHGyQpmvJw&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwFSCjlx&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af18HhjS4wFjQF1j29V5J-1wriTSD7WGbF_1x-D7t5u_6w&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwEoKXx2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3RHAiYhzHJX4kfccdR15VKJfZHtiX88CfA69F8l7RNyg&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwHSBV-J&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0fIgi5dXqNmWli1DykgChiXF38pMHjGswopD-ENolG-Q&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwEHEMgU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af245LrGSGFVKFKeqQ88d35A0b6MmKoOOHj-hQhTV4dvHQ&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwHeYUA8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3mV5eGibgSo9ecMzKUhu1SMmcIPDve0WPB1Od41u17PQ&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwGV2wfL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3An-4Fb6DgeMEJ6dAdAB7hpYhn8HT4WU0Wkx8X9O7-NQ&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwGuC8go&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=P_m-q4sI0e8e5fri6veJMg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af04Mumbk9-3t-GAKaIdSsUhwNct3a0Ixztn7S9ZsTOqYQ&amp;oe=69DC5283</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "number_of_qualities": 7,
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
        "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFotTxQmMsM3NGLs-OQr5aRp6G675KQB1FvfrrE1NnU1iYLXByCqG8Ftk29T3BlsNQ&_nc_ohc=XbeNvhLXv28Q7kNvwGaY1se&_nc_gid=P_m-q4sI0e8e5fri6veJMg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2cn7uiHefjW7Lt0P9EshzzQ3mI1Z7reF_9CTZd9MHYJQ&oe=69DC51E9&_nc_sid=fc8dfb",
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "username": "natgeo",
        "text_post_app_is_private": false,
        "is_active_on_text_post_app": true,
        "latest_reel_media": 1775659002,
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/comment/offensive",
        headers={"x-access-key": "YOUR_TOKEN"},
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
      "https://api.hikerapi.com/v2/media/comments?id=3691011991037807194"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_v2(id="3691011991037807194")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/comments",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "3691011991037807194"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comments?id=3691011991037807194",
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
      "created_at": 1754223046,
      "created_at_for_fb_app": 1754223046,
      "created_at_utc": 1754223046,
      "did_report_as_spam": false,
      "is_covered": false,
      "is_created_by_media_owner": true,
      "is_ranked_comment": true,
      "media_id": 3691011991037807194,
      "pk": "17850017691525490",
      "private_reply_status": 0,
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "17850017691525490",
      "text": "the way we still did a second round of picks after all the happy screaming…. 🫩🫩🫩",
      "type": 1,
      "user": {
        "fbid_v2": 17841401653390175,
        "full_name": "Adeline Tan ᐧ༚̮ᐧ",
        "id": "11255113",
        "is_private": false,
        "is_unpublished": false,
        "is_verified": false,
        "pk": 11255113,
        "pk_id": "11255113",
        "profile_pic_id": "1992089677481616027_11255113",
        "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NTAuQzMifQ%3D%3D&_nc_ohc=uVBRZd8AAZwQ7kNvwHWnFw2&_nc_oc=AdoAIJeklNEDeX-NjOmRbrwUU5j5aFQqkY_ttuPn797Tzr-bwab7XBdhUAqNTUs_cw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3zATSEgeYmwVYHBwA4bXDkKiJDsSa52j2nKpeuY-nxKw&oe=69DC47F5",
        "strong_id__": "11255113",
        "username": "addie_ble"
      },
      "user_id": 11255113
    },
    "caption_is_edited": false,
    "comment_count": 551,
    "comment_cover_pos": "bottom",
    "comment_filter_param": "no_filter",
    "comment_likes_enabled": true,
    "comments": [
      {
        "bit_flags": 0,
        "comment_has_a_visual_reply_media": true,
        "comment_like_count": 13,
        "content_type": "comment",
        "created_at": 1754749758,
        "created_at_for_fb_app": 1754749758,
        "created_at_utc": 1754749758,
        "did_report_as_spam": false,
        "has_liked_comment": false,
        "has_disliked_comment": false,
        "inline_composer_display_condition": "never",
        "is_covered": false,
        "is_liked_by_media_owner": true,
        "is_pinned": true,
        "is_photo_comments_enabled_for_comment_author": false,
        "is_text_editable": false,
        "is_edited": false,
        "meta_ai_comment_type": "NONE",
        "is_ranked_comment": true,
        "keywords_data": [],
        "liked_by_media_coauthors": [],
        "other_preview_users": [],
        "media_id": 3691011991037807194,
        "pk": "18065401537979604",
        "preview_child_comments": [
          {
            "bit_flags": 0,
            "comment_like_count": 0,
            "content_type": "comment",
            "created_at": 1767006338,
            "created_at_utc": 1767006338,
            "created_at_for_fb_app": 1767006338,
            "did_report_as_spam": false,
            "has_liked_comment": false,
            "has_disliked_comment": false,
            "is_covered": false,
            "is_created_by_media_owner": true,
            "is_photo_comments_enabled_for_comment_author": false,
            "is_text_editable": false,
            "is_edited": false,
            "meta_ai_comment_type": "NONE",
            "is_ranked_comment": false,
            "liked_by_media_coauthors": [],
            "media_id": 3691011991037807194,
            "media_info": {
              "media": {
                "can_see_insights_as_brand": false,
                "caption": {
                  "__typename": "XDTCommentDict",
                  "strong_id__": "17905309164311566",
                  "pk": "17905309164311566",
                  "bit_flags": 0,
                  "content_type": "comment",
                  "created_at": 1767008635,
                  "created_at_utc": 1767008635,
                  "did_report_as_spam": false,
                  "is_covered": false,
                  "is_ranked_comment": false,
                  "media_id": 3798240616569105105,
                  "private_reply_status": 0,
                  "share_enabled": false,
                  "status": "Active",
                  "text": "RIP brackenfern I’ll always love you 🥀 \n\n#korea #family #vlog #jeju #travel",
                  "type": 1,
                  "user": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "11255113",
                    "id": "11255113",
                    "fbid_v2": 17841401653390175,
                    "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                    "is_private": false,
                    "is_verified": false,
                    "pk": 11255113,
                    "profile_pic_id": "1992089677481616027_11255113",
                    "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                    "username": "addie_ble"
                  },
                  "user_id": 11255113
                },
                "clips_demotion_control": {
                  "confirmation_body": "We'll suggest fewer posts like this.",
                  "confirmation_icon": "none",
                  "confirmation_style": "bottomsheet",
                  "confirmation_title": "Post hidden",
                  "confirmation_title_style": "large_left",
                  "enable_word_wrapping": true,
                  "followup_options": [
                    {
                      "data": "author_id:11255113",
                      "demotion_control": {
                        "confirmation_body": "We won't suggest posts from addie_ble.",
                        "confirmation_icon": "eye-off-pano",
                        "confirmation_style": "bottomsheet",
                        "undo_style": "inline"
                      },
                      "id": "dislike_author",
                      "show_icon": true,
                      "text": "Don't suggest posts from addie_ble"
                    },
                    {
                      "id": "hide_all_specific_words",
                      "show_icon": true,
                      "text": "Don't suggest posts with certain words"
                    },
                    {
                      "id": "control_center",
                      "show_icon": true,
                      "text": "Manage content preferences"
                    }
                  ],
                  "title": "Not interested",
                  "title_style": "normal",
                  "undo_style": "top_right"
                },
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
                    "best_audio_cluster_id": "2394396384327151"
                  },
                  "audio_type": "original_sounds",
                  "branded_content_tag_info": {
                    "can_add_tag": false
                  },
                  "clips_creation_entry_point": "clips",
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
                    "mashups_allowed": true,
                    "non_privacy_filtered_mashups_media_count": 0
                  },
                  "music_canonical_id": "18400923181124272",
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": "33101782226134791",
                    "audio_parts": [],
                    "audio_parts_by_filter": [],
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": true,
                    "consumption_info": {
                      "is_bookmarked": false,
                      "is_trending_in_clips": false,
                      "should_mute_audio_reason": ""
                    },
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT156.129517S\" FBManifestTimestamp=\"1775667230\" FBManifestIdentifier=\"FrygtJ0NKRaSh7CWjvPAByIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT156.129517S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2113039912796617a\" bandwidth=\"58121\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"58121\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPV3ZYgZW6FYhy9eYhd7JqCyIBEIMdotFnd2ot3NQHA6p0boXbXs2nV1py5pWAZhFdIREQNXE81TbQ3n_5S5dC_.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=JyzBXGs62pAQ7kNvwH2EVEs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjExODk2MzU0OTMyMzgxOTksImFzc2V0X2FnZV9kYXlzIjoxMDAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjU4MjEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3f53844SKKC0r-7nT2xxcblch70kMFmneo8kmafFearA&amp;oe=69D852F4</BaseURL><SegmentBase indexRange=\"824-1803\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 156133,
                    "hide_remixing": false,
                    "ig_artist": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "11255113",
                      "id": "11255113",
                      "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                      "is_private": false,
                      "is_verified": false,
                      "pk": "11255113",
                      "profile_pic_id": "1992089677481616027_11255113",
                      "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                      "username": "addie_ble"
                    },
                    "is_audio_automatically_attributed": false,
                    "is_eligible_for_audio_effects": true,
                    "is_explicit": false,
                    "is_original_audio_download_eligible": false,
                    "is_reuse_disabled": false,
                    "is_xpost_from_fb": false,
                    "oa_owner_is_music_artist": false,
                    "original_audio_subtype": "default",
                    "original_audio_title": "Original audio",
                    "original_media_id": "3798240616569105105",
                    "progressive_download_url": "https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m69/AQMJxhXdTv9iqGzjnxp816PiLE0Hl8PZggAIfgmvZURKkgNmu2kY2Z0CciKeVm8NI68bNdTaM9i8pIkgSz4JtSYI.mp4?strext=1&_nc_cat=110&_nc_sid=8bf8fe&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ohc=w2Qm4yCw5ywQ7kNvwEx1Aq7&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTE4OTYzNTQ5MzIzODE5OSwiYXNzZXRfYWdlX2RheXMiOjEwMCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2v1M4p9kdr1wYtKg557yFYg7Itxjpouo4FEtgJUrGH8g&oe=69DC5750",
                    "should_mute_audio": false,
                    "time_created": 1767006338
                  },
                  "professional_clips_upsell_type": 0,
                  "show_achievements": false
                },
                "coauthor_producer_can_see_organic_insights": false,
                "coauthor_producers": [],
                "comment_inform_treatment": {
                  "should_have_inform_treatment": false,
                  "text": ""
                },
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "deleted_reason": 0,
                "enable_media_notes_production": true,
                "enable_waist": true,
                "ig_play_count": 4128,
                "reshare_count": 3,
                "fundraiser_tag": {},
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "has_delayed_metadata": false,
                "has_more_comments": false,
                "hide_view_all_comment_entrypoint": true,
                "invited_coauthor_producers": [],
                "is_artist_pick": false,
                "is_cutout_sticker_allowed": true,
                "is_in_profile_grid": false,
                "is_organic_product_tagging_eligible": true,
                "is_paid_partnership": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_reuse_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "is_unified_video": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "media_notes": {
                  "items": []
                },
                "mezql_token": "",
                "owner": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "biography": "⁽̨̡ ¨̮ ⁾̧̢ \n@dee_bakes 🍰\ntiktok: addieblesausage 🌭\nwork with me: adelinetan1996@gmail.com 🧚🏼‍♀️",
                  "can_see_quiet_post_attribution": true,
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "friendship_status": {
                    "following": false,
                    "is_bestie": false,
                    "is_feed_favorite": false,
                    "is_restricted": false
                  },
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "pk": "11255113",
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                  "show_account_transparency_details": true,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble",
                  "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
                },
                "photo_of_you": false,
                "play_count": 4128,
                "profile_grid_control_enabled": false,
                "senders": [],
                "share_count_disabled": false,
                "is_social_ufi_disabled": false,
                "sharing_friction_info": {
                  "should_have_sharing_friction": false
                },
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "floating_context_items": [],
                "subscribe_cta_visible": false,
                "timeline_pinned_user_ids": [],
                "video_codec": "vp09.00.21.08.00.01.01.01.00",
                "video_sticker_locales": [],
                "video_subtitles_uri": "https://scontent-jnb2-1.cdninstagram.com/v/t39.36743-6/607899197_2739168353086603_2509850887076325106_n.srt?_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=bBTLH5PwA7IQ7kNvwEeHukH&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUAAAAA&ccb=7-5&oh=00_Af0wv7qbkc12Gi_XzCW_Jg86W7sZ8MXUAwaytmTz6zngEw&oe=69DC60F2&_nc_sid=10d13b",
                "view_state_item_type": 128,
                "visual_comment_reply_sticker_info": [
                  {
                    "end_time_ms": 7200.9833333333,
                    "height": 0.14124688575434,
                    "is_fb_sticker": 0,
                    "is_hidden": 0,
                    "is_pinned": 0,
                    "is_sticker": 1,
                    "rotation": 0,
                    "start_time_ms": 0,
                    "vcr_sticker": {
                      "can_viewer_link_back_to_original_media_from_vcr": true,
                      "end_background_color": "#FFFFFF",
                      "end_time_ms": 7200.9833333333,
                      "original_comment_author": {
                        "__typename": "XDTUserDict",
                        "strong_id__": "4955997576",
                        "id": "4955997576",
                        "full_name": "Roselie Dumlao",
                        "is_private": true,
                        "is_verified": false,
                        "pk": "4955997576",
                        "profile_pic_id": "3832079386024340448_4955997576",
                        "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.82787-19/630168225_18362391706165577_3086504076158166676_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=kCWdwQ6JE3oQ7kNvwHbLsuU&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKGajyVJYd96fzxBAJTmM7Ead9UqbmNDAQAB1501500j-ccb7-5&oh=00_Af1MoD00Vg46p8FZ-V5yyn-U1EiGGpfnKWmXH1ix6WVf9Q&oe=69DC5765&_nc_sid=10d13b",
                        "username": "jangdan_ja_ju_ru"
                      },
                      "original_comment_id": "18065401537979604",
                      "original_comment_text": "Why did I scream as well ? Haha, as if I'm going with you guys 😂😂😂",
                      "original_media_id": "3691011991037807194",
                      "start_background_color": "#FFFFFF",
                      "start_time_ms": 0,
                      "text_color": ""
                    },
                    "width": 0.5873316831367,
                    "x": 0.5,
                    "y": 0.18525527831541,
                    "z": 0
                  }
                ],
                "visual_replies_info": {
                  "can_viewer_link_back_to_original_media_from_vcr": true,
                  "comment_info": {
                    "comment_id": "18065401537979604",
                    "commenter_username": "jangdan_ja_ju_ru"
                  },
                  "original_media": {
                    "pk": "3691011991037807194"
                  }
                },
                "top_likers": [],
                "__typename": "XDTMediaDict",
                "strong_id__": "3798240616569105105_11255113",
                "id": "3798240616569105105_11255113",
                "are_remixes_crosspostable": true,
                "can_viewer_reshare": true,
                "can_viewer_save": true,
                "caption_is_edited": true,
                "code": "DS2D7eCD-rR",
                "device_timestamp": 1767005556399135,
                "like_count": 57,
                "comment_count": 0,
                "filter_type": 0,
                "has_audio": true,
                "has_high_risk_gen_ai_inform_treatment": false,
                "has_liked": false,
                "has_shared_to_fb": 0,
                "has_views_fetching": true,
                "ig_media_sharing_disabled": false,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/608778464_1408482380685336_3404794673956207894_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=c9cMbLNUrsAQ7kNvwG0V6u8&_nc_oc=AdrSG--5O20xad_SocWqpG-DhdCMhCPU_WQtLm10o-C9jGKz-EiuEqcAA-CZBO3qigk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af0PpjOCraH0fwWPZh1sMBXQkPW49924VpUaT38aeM2PZQ&oe=69DC5DD7",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/608778464_1408482380685336_3404794673956207894_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=c9cMbLNUrsAQ7kNvwG0V6u8&_nc_oc=AdrSG--5O20xad_SocWqpG-DhdCMhCPU_WQtLm10o-C9jGKz-EiuEqcAA-CZBO3qigk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af0PpjOCraH0fwWPZh1sMBXQkPW49924VpUaT38aeM2PZQ&oe=69DC5DD7",
                      "width": 640
                    }
                  },
                  "candidates": [
                    {
                      "height": 1280,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.82787-15/606969139_18546498319055114_8380976248878953011_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=100&ig_cache_key=Mzc5ODI0MDYxNjU2OTEwNTEwNTE4NTQ2NDk4MzE2MDU1MTE0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjcyMHgxMjgwLnNkci5DMyJ9&_nc_ohc=MVBGQh7DI08Q7kNvwF15wpw&_nc_oc=AdrJz9kD8Z0Y-vIityVJ7KTtLJEQ6YKlCh9ffCeYM5LJW_WlYd8E_YIbZMwq3PvJYNg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af08YEKV_jlAqtAiIYN8-uDDH9_mFMZeevEneZCLfA1rCg&oe=69DC45BE",
                      "width": 720
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 812,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_width": 1500,
                      "thumbnail_duration": 1.486980952381,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 156.133
                    }
                  }
                },
                "is_comments_gif_composer_enabled": true,
                "is_dash_eligible": 1,
                "is_post_live_clips_media": false,
                "is_quiet_post": false,
                "is_third_party_downloads_eligible": false,
                "like_and_view_counts_disabled": false,
                "media_type": 2,
                "number_of_qualities": 4,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQUpGaWladTNPcldHVDRtRFJ6UDZ1YWkzNzk4MjQwNjE2NTY5MTA1MTA1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2NzIyOTk4M3wzNzk4MjQwNjE2NTY5MTA1MTA1fDExMjU1MTEzfDcwMTBhODMyODNjYWVjMzlkMzg0Yzg3NWFjYjBhY2Q1MTdjODdmMmMxOTE1MWI1ZDYwZGJlOTZiNjc3YzZkMjMifSwic2lnbmF0dXJlIjoiIn0=",
                "original_height": 1920,
                "original_media_has_visual_reply_media": false,
                "original_width": 1080,
                "product_type": "clips",
                "taken_at": 1767006336,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "friendship_status": {
                    "following": false,
                    "is_bestie": false,
                    "is_feed_favorite": false,
                    "is_restricted": false,
                    "outgoing_request": false
                  },
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_facebook_onboarded_charity": false,
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "merchant_checkout_style": "none",
                  "pk": 11255113,
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NTAuQzMifQ%3D%3D&_nc_ohc=uVBRZd8AAZwQ7kNvwHWnFw2&_nc_oc=AdoAIJeklNEDeX-NjOmRbrwUU5j5aFQqkY_ttuPn797Tzr-bwab7XBdhUAqNTUs_cw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3zATSEgeYmwVYHBwA4bXDkKiJDsSa52j2nKpeuY-nxKw&oe=69DC47F5",
                  "seller_shoppable_feed_type": "none",
                  "show_account_transparency_details": true,
                  "show_shoppable_feed": false,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble"
                },
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT156.133331S\" FBManifestTimestamp=\"1775667229\" FBManifestIdentifier=\"FrqgtJ0NGBFpZ19kYXNoX2Jhc2ljX3ZwORmGuNzxk8Xx2gKOw+P25KOXA/rPk932grYE/M/Ixuz5vwTSzr79pbPYBZ7OzeOxx+kF+Pe07cO4+AW06suprPqfXSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWyAEUABIUAAA=\"><Period id=\"0\" duration=\"PT156.133331S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"762812653516572v\" bandwidth=\"559590\" codecs=\"vp09.00.21.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_360p\" FBContentLength=\"10921333\" FBPlaybackResolutionMos=\"0:100,360:84.1,480:76.9,720:69.5,1080:58.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.7,480:91.3,720:84.3,1080:73.7\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPqzFTsFaOhxCuZziJGNeMRNXKieSWwgdsHEKyM_TLi4cwL_kSaJyKYWKiVhk12OhNf8S0sYF6PGghEKpzOiUx3rPz3qHCx0b0atCILvj8Rrg.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=yeYH-vZYVVcQ7kNvwGXyi_K&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMzYwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMTg5NjM1NDkzMjM4MTk5LCJhc3NldF9hZ2VfZGF5cyI6MTAwLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTU2LCJiaXRyYXRlIjo1NTk1OTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2crYmznrO3O5_Sh9sgL2cVfwFtqj2emUtpL_2A7f_SoA&amp;oe=69DC42D7</BaseURL><SegmentBase indexRange=\"818-1233\" timescale=\"15360\" FBMinimumPrefetchRange=\"1234-51434\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1234-288612\" FBFirstSegmentRange=\"1234-470612\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"470613-749523\" FBPrefetchSegmentRange=\"1234-470612\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1601770201011113v\" bandwidth=\"1436459\" codecs=\"vp09.00.30.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_540p\" FBContentLength=\"28034893\" FBPlaybackResolutionMos=\"0:100,360:95.2,480:94.3,720:90.2,1080:80.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.43,480:98,720:96.5,1080:93.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMK7DFYsC-BMFgmwUxfUDVxnmTjNYDRqC5S08WE8z_mRxHzPEjTcF2qsB5d_3ZdOAV0f75xdE3nww_XXAdfDLQWKY8QD_rvppY02p4M_fTwWg.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=1lVanaxxCEQQ7kNvwHTffBY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNTQwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMTg5NjM1NDkzMjM4MTk5LCJhc3NldF9hZ2VfZGF5cyI6MTAwLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTU2LCJiaXRyYXRlIjoxNDM2NDU5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1fnagbxMI9v80n-udAUvwPS0jge_kRK9nqxMlJF0_I8g&amp;oe=69DC722D</BaseURL><SegmentBase indexRange=\"818-1233\" timescale=\"15360\" FBMinimumPrefetchRange=\"1234-112907\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1234-708367\" FBFirstSegmentRange=\"1234-1191753\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1191754-1906242\" FBPrefetchSegmentRange=\"1234-1191753\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"895617306751175v\" bandwidth=\"2440394\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_720p\" FBContentLength=\"47628374\" FBPlaybackResolutionMos=\"0:100,360:97.7,480:97.3,720:96.7,1080:93.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.489,480:99.354,720:99.101,1080:97.6\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOnv9SH2bEti8jsLbz8GephAhjapCMjVUub3kC26OYpa4NrDt48h9DpFyoINqxZVqE-IYPNHLOCKoPAxq3CD_qpjEOmlOfTjWJF_Y2O-LuPPA.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=Pv6SyNkjJVAQ7kNvwFePs19&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNzIwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxMTg5NjM1NDkzMjM4MTk5LCJhc3NldF9hZ2VfZGF5cyI6MTAwLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTU2LCJiaXRyYXRlIjoyNDQwMzk0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0pj2rrL4kOuBUvajBpOdBqSTu2RY__sSTguVGmb_4vHA&amp;oe=69DC6CD1</BaseURL><SegmentBase indexRange=\"818-1233\" timescale=\"15360\" FBMinimumPrefetchRange=\"1234-164218\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1234-1170874\" FBFirstSegmentRange=\"1234-1982652\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1982653-3173328\" FBPrefetchSegmentRange=\"1234-1982652\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1639498777211791v\" bandwidth=\"3237047\" codecs=\"vp09.00.40.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_1080p\" FBContentLength=\"63176373\" FBPlaybackResolutionMos=\"0:100,360:98.5,480:98.4,720:98.1,1080:97.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.667,480:99.639,720:99.561,1080:99.351\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN4crCHNxwhrdaawc0h9SMvtlkr6n9TGDsosjSNrNqYtWJfZVOqHdUB39kLxaIVRxY5WuhrWS2EkBTR3AV9lJaJv1sLKIRgRKL959iNv20FNA.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=cfpASgelWysQ7kNvwE5PKav&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMTA4MHAiLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjU2NzA2NzM0MzM1MjQyNywiY2xpZW50X25hbWUiOiJpZyIsInhwdl9hc3NldF9pZCI6MTE4OTYzNTQ5MzIzODE5OSwiYXNzZXRfYWdlX2RheXMiOjEwMCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1NiwiYml0cmF0ZSI6MzIzNzA0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1_bVs9Ul0w7nLqKu1pmlymkN0y-BsU4VAWAZrHobHvQQ&amp;oe=69DC544D</BaseURL><SegmentBase indexRange=\"818-1233\" timescale=\"15360\" FBMinimumPrefetchRange=\"1234-190528\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1234-1499818\" FBFirstSegmentRange=\"1234-2544504\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"2544505-4190585\" FBPrefetchSegmentRange=\"1234-2544504\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1244697457751037a\" bandwidth=\"37608\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"37608\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"735211\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOpRTf4tqS-ew3KA23M78rOw2kl2UCl_ZabtdQMLOvOcU8W3-OmN6ObQyOhHastnFHn2oAwodWOkNCS4mlJ457ZdV4TlhtwkSc1Nww.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=nAeQffsvut0Q7kNvwG_fH_V&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjExODk2MzU0OTMyMzgxOTksImFzc2V0X2FnZV9kYXlzIjoxMDAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjM3NjcxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af20lNNFBX4RNtb1XgoDqSPdIX5uOmksL-Q0FdLJPwdVbQ&amp;oe=69DC4687</BaseURL><SegmentBase indexRange=\"837-1252\" timescale=\"44100\" FBMinimumPrefetchRange=\"1253-2348\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1253-13658\" FBFirstSegmentRange=\"1253-24725\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"24726-48106\" FBPrefetchSegmentRange=\"1253-24725\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1266531705623550a\" bandwidth=\"79863\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"79863\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"1559859\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6shG-Svhz1IZ_X-HoisiKrIo4Lz0vNeWq4uRQd9WXtl3gbE4fbutaA4y9fibxQCQDH-hAQ9LBMbrdvgnene4uK_Yfgfzp9ZIF-Qk.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=SY-P1O1F684Q7kNvwETLL-F&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjExODk2MzU0OTMyMzgxOTksImFzc2V0X2FnZV9kYXlzIjoxMDAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjc5OTI2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3D8ubdalNhFNW1lIYtbEuY2UtZyM5RySpfNiIBfH99JA&amp;oe=69DC569D</BaseURL><SegmentBase indexRange=\"838-1253\" timescale=\"44100\" FBMinimumPrefetchRange=\"1254-2851\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1254-26866\" FBFirstSegmentRange=\"1254-51343\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"51344-102546\" FBPrefetchSegmentRange=\"1254-51343\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1672228854210044a\" bandwidth=\"108377\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108377\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"2116350\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNBDXyhOIwcjpbM9vAXwNIXWwvtvwy6QAGYUzvpqy5wCvC_YoNQuXBSN0DDNfRmPSbiqWzOdhyLsOy0L7zIu8_kYFj1YjjAB92GUWQ.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=LF7MdOilpf8Q7kNvwGA37Dj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjExODk2MzU0OTMyMzgxOTksImFzc2V0X2FnZV9kYXlzIjoxMDAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjEwODQ0MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1CromhUnhHJUGpQ3EgYOAazHh6ZiJmbFzNSbOmrJAiXg&amp;oe=69DC496D</BaseURL><SegmentBase indexRange=\"833-1248\" timescale=\"44100\" FBMinimumPrefetchRange=\"1249-2555\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1249-35153\" FBFirstSegmentRange=\"1249-68188\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"68189-136358\" FBPrefetchSegmentRange=\"1249-68188\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"26247444448246426a\" bandwidth=\"127007\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"127007\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"2479927\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPYk7GQL-JsZcbVHOZR-3s2quM1TYS8qa3ei4cLKI-icJbHasY6cB-CY6A0l_-5C1sWkFYJvFe1_rGdd-yZjIQg-VKi3kb0P8jve2A.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=nYrBisYlWfIQ7kNvwGF5NxF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjExODk2MzU0OTMyMzgxOTksImFzc2V0X2FnZV9kYXlzIjoxMDAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjEyNzA3MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1t8vxrA4Hno8OTK_vQeamMJJ5aQYs7cBmG1WM4hLx8tg&amp;oe=69DC644B</BaseURL><SegmentBase indexRange=\"833-1248\" timescale=\"44100\" FBMinimumPrefetchRange=\"1249-2594\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1249-40530\" FBFirstSegmentRange=\"1249-78665\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"78666-157294\" FBPrefetchSegmentRange=\"1249-78665\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "video_subtitles_locale": "en_US",
                "__is_XDTMediaDict": true
              }
            },
            "parent_comment_id": "18065401537979604",
            "pk": "18389134726196231",
            "private_reply_status": 0,
            "replied_to_comment_id": "18065401537979604",
            "share_enabled": true,
            "status": "Active",
            "strong_id__": "18389134726196231",
            "text": "RIP brackenfern I’ll always love you 🥀 \n\n#korea #family #vlog #jeju #travel",
            "type": 2,
            "user": {
              "fbid_v2": 17841401653390175,
              "full_name": "Adeline Tan ᐧ༚̮ᐧ",
              "id": "11255113",
              "is_mentionable": true,
              "is_private": false,
              "is_verified": false,
              "pk": 11255113,
              "pk_id": "11255113",
              "profile_pic_id": "1992089677481616027_11255113",
              "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NTAuQzMifQ%3D%3D&_nc_ohc=uVBRZd8AAZwQ7kNvwHWnFw2&_nc_oc=AdoAIJeklNEDeX-NjOmRbrwUU5j5aFQqkY_ttuPn797Tzr-bwab7XBdhUAqNTUs_cw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3zATSEgeYmwVYHBwA4bXDkKiJDsSa52j2nKpeuY-nxKw&oe=69DC47F5",
              "strong_id__": "11255113",
              "username": "addie_ble"
            },
            "user_id": 11255113
          }
        ],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "18065401537979604",
        "text": "Why did I scream as well ? Haha, as if I'm going with you guys 😂😂😂",
        "type": 0,
        "user": {
          "fbid_v2": 17841404967299499,
          "full_name": "Roselie Dumlao",
          "id": "4955997576",
          "is_mentionable": false,
          "is_private": true,
          "is_verified": false,
          "pk": "4955997576",
          "pk_id": "4955997576",
          "profile_pic_id": "3832079386024340448_4955997576",
          "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.82787-19/630168225_18362391706165577_3086504076158166676_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=105&ig_cache_key=GKGajyVJYd96fzxBAJTmM7Ead9UqbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=fwLkIN302tEQ7kNvwHqe3bN&_nc_oc=Adp6-otA67ioArE0GuMCk0jn8zmMoQHSj0_CB-GVUVmx66ah23Tf1mmYP1Vj8b5xSfM&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af0GVWXZI5qP8WlegAil20MmhbTquReyvwHBeUuKMil4xg&oe=69DC5765",
          "strong_id__": "4955997576",
          "username": "jangdan_ja_ju_ru"
        },
        "user_id": 4955997576,
        "has_liked": false,
        "like_count": 13
      },
      {
        "bit_flags": 0,
        "comment_has_a_visual_reply_media": true,
        "comment_like_count": 2155,
        "content_type": "comment",
        "created_at": 1754310648,
        "created_at_for_fb_app": 1754310648,
        "created_at_utc": 1754310648,
        "did_report_as_spam": false,
        "has_liked_comment": false,
        "has_disliked_comment": false,
        "inline_composer_display_condition": "never",
        "is_covered": false,
        "is_pinned": true,
        "is_photo_comments_enabled_for_comment_author": false,
        "is_text_editable": false,
        "is_edited": false,
        "meta_ai_comment_type": "NONE",
        "is_ranked_comment": true,
        "keywords_data": [],
        "liked_by_media_coauthors": [],
        "other_preview_users": [],
        "media_id": 3691011991037807194,
        "pk": "18090010117735782",
        "preview_child_comments": [
          {
            "bit_flags": 0,
            "comment_like_count": 30,
            "content_type": "comment",
            "created_at": 1759062331,
            "created_at_utc": 1759062331,
            "created_at_for_fb_app": 1759062331,
            "did_report_as_spam": false,
            "has_liked_comment": false,
            "has_disliked_comment": false,
            "is_covered": false,
            "is_created_by_media_owner": true,
            "is_photo_comments_enabled_for_comment_author": false,
            "is_text_editable": false,
            "is_edited": false,
            "meta_ai_comment_type": "NONE",
            "is_ranked_comment": false,
            "liked_by_media_coauthors": [],
            "media_id": 3691011991037807194,
            "media_info": {
              "media": {
                "can_see_insights_as_brand": false,
                "caption": {
                  "__typename": "XDTCommentDict",
                  "strong_id__": "18078813659487757",
                  "pk": "18078813659487757",
                  "bit_flags": 0,
                  "content_type": "comment",
                  "created_at": 1759062329,
                  "created_at_utc": 1759062329,
                  "did_report_as_spam": false,
                  "is_covered": false,
                  "is_ranked_comment": false,
                  "media_id": 3731606998468236217,
                  "private_reply_status": 0,
                  "share_enabled": false,
                  "status": "Active",
                  "text": "I miss busan!!!! 😭😭\n\n#Korea #busan #seoul #family #vlog #travel #cousins",
                  "type": 1,
                  "user": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "11255113",
                    "id": "11255113",
                    "fbid_v2": 17841401653390175,
                    "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                    "is_private": false,
                    "is_verified": false,
                    "pk": 11255113,
                    "profile_pic_id": "1992089677481616027_11255113",
                    "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                    "username": "addie_ble"
                  },
                  "user_id": 11255113
                },
                "clips_demotion_control": {
                  "confirmation_body": "We'll suggest fewer posts like this.",
                  "confirmation_icon": "none",
                  "confirmation_style": "bottomsheet",
                  "confirmation_title": "Post hidden",
                  "confirmation_title_style": "large_left",
                  "enable_word_wrapping": true,
                  "followup_options": [
                    {
                      "data": "author_id:11255113",
                      "demotion_control": {
                        "confirmation_body": "We won't suggest posts from addie_ble.",
                        "confirmation_icon": "eye-off-pano",
                        "confirmation_style": "bottomsheet",
                        "undo_style": "inline"
                      },
                      "id": "dislike_author",
                      "show_icon": true,
                      "text": "Don't suggest posts from addie_ble"
                    },
                    {
                      "id": "hide_all_specific_words",
                      "show_icon": true,
                      "text": "Don't suggest posts with certain words"
                    },
                    {
                      "id": "control_center",
                      "show_icon": true,
                      "text": "Manage content preferences"
                    }
                  ],
                  "title": "Not interested",
                  "title_style": "normal",
                  "undo_style": "top_right"
                },
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
                    "best_audio_cluster_id": "689975787478369"
                  },
                  "audio_type": "original_sounds",
                  "branded_content_tag_info": {
                    "can_add_tag": false
                  },
                  "clips_creation_entry_point": "clips",
                  "cutout_sticker_info": [],
                  "disable_use_in_clips_client_cache": false,
                  "is_fan_club_promo_video": false,
                  "is_public_chat_welcome_video": false,
                  "is_shared_to_fb": true,
                  "mashup_info": {
                    "can_toggle_mashups_allowed": false,
                    "has_been_mashed_up": false,
                    "has_nonmimicable_additional_audio": false,
                    "is_creator_requesting_mashup": false,
                    "is_light_weight_check": true,
                    "is_pivot_page_available": false,
                    "mashups_allowed": true,
                    "non_privacy_filtered_mashups_media_count": 0
                  },
                  "music_canonical_id": "18357588121090557",
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": "1191747029455045",
                    "audio_parts": [],
                    "audio_parts_by_filter": [],
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": false,
                    "consumption_info": {
                      "is_bookmarked": false,
                      "is_trending_in_clips": false,
                      "should_mute_audio_reason": ""
                    },
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT179.929977S\" FBManifestTimestamp=\"1775667230\" FBManifestIdentifier=\"FrygtJ0NKRa8kZWOjambBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT179.929977S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1748929622484062a\" bandwidth=\"58011\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"58011\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m86/AQPDm8JUTBKqfyTHWPeNTAFDwuU7UuwBzyXpv4_el-mreGXdL59TY_c4re6CM8SJslY1FAgWqipBskZZAw8nlR8.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=4GFNvniflucQ7kNvwFFP6NW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjIyODIyMzkyNTIyMjMyMTAsImFzc2V0X2FnZV9kYXlzIjoxOTIsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNzksImJpdHJhdGUiOjU4MDk2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3_3eN-aNfnur-3uDCDDQcBpY8meQ0Oik7I6KYIm20pIw&amp;oe=69D860DC</BaseURL><SegmentBase indexRange=\"824-1935\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 179933,
                    "hide_remixing": false,
                    "ig_artist": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "11255113",
                      "id": "11255113",
                      "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                      "is_private": false,
                      "is_verified": false,
                      "pk": "11255113",
                      "profile_pic_id": "1992089677481616027_11255113",
                      "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                      "username": "addie_ble"
                    },
                    "is_audio_automatically_attributed": false,
                    "is_eligible_for_audio_effects": true,
                    "is_explicit": false,
                    "is_original_audio_download_eligible": false,
                    "is_reuse_disabled": false,
                    "is_xpost_from_fb": false,
                    "oa_owner_is_music_artist": false,
                    "original_audio_subtype": "default",
                    "original_audio_title": "Original audio",
                    "original_media_id": "3731606998468236217",
                    "progressive_download_url": "https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m69/AQPu4Cs0AnwatFaGxuUTwnyhlXqg0azOw8Yd5M0C7stwokNPeB4fVzx-6UkO2SNm68qbErWDHzcOvWdWrp1w4H1u.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ohc=pOvCQcjvyKgQ7kNvwHy0g0-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MjI4MjIzOTI1MjIyMzIxMCwiYXNzZXRfYWdlX2RheXMiOjE5MiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE3OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3p3BsUYU1xPyZtmfCacLdtil3jpgy9mZY5wqk-OWPT9A&oe=69DC465F",
                    "should_mute_audio": false,
                    "time_created": 1759062330
                  },
                  "professional_clips_upsell_type": 0,
                  "show_achievements": false
                },
                "coauthor_producer_can_see_organic_insights": false,
                "coauthor_producers": [],
                "comment_inform_treatment": {
                  "should_have_inform_treatment": false,
                  "text": ""
                },
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "deleted_reason": 0,
                "enable_media_notes_production": true,
                "enable_waist": true,
                "fb_like_count": 0,
                "fb_play_count": 0,
                "ig_play_count": 8570,
                "reshare_count": 11,
                "fundraiser_tag": {},
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "has_delayed_metadata": false,
                "has_more_comments": true,
                "hide_view_all_comment_entrypoint": true,
                "invited_coauthor_producers": [],
                "is_artist_pick": false,
                "is_cutout_sticker_allowed": true,
                "is_in_profile_grid": false,
                "is_organic_product_tagging_eligible": true,
                "is_paid_partnership": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_reuse_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "is_unified_video": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "media_notes": {
                  "items": []
                },
                "mezql_token": "",
                "owner": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "biography": "⁽̨̡ ¨̮ ⁾̧̢ \n@dee_bakes 🍰\ntiktok: addieblesausage 🌭\nwork with me: adelinetan1996@gmail.com 🧚🏼‍♀️",
                  "can_see_quiet_post_attribution": true,
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "friendship_status": {
                    "following": false,
                    "is_bestie": false,
                    "is_feed_favorite": false,
                    "is_restricted": false
                  },
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "pk": "11255113",
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                  "show_account_transparency_details": true,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble",
                  "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
                },
                "photo_of_you": false,
                "play_count": 8570,
                "profile_grid_control_enabled": false,
                "senders": [],
                "share_count_disabled": false,
                "is_social_ufi_disabled": false,
                "sharing_friction_info": {
                  "should_have_sharing_friction": false
                },
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "floating_context_items": [],
                "subscribe_cta_visible": false,
                "timeline_pinned_user_ids": [],
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "video_sticker_locales": [],
                "view_state_item_type": 128,
                "visual_comment_reply_sticker_info": [
                  {
                    "end_time_ms": 4310.5833333333,
                    "height": 0.16009695648062,
                    "is_fb_sticker": 0,
                    "is_hidden": 0,
                    "is_pinned": 0,
                    "is_sticker": 1,
                    "rotation": 0,
                    "start_time_ms": 0,
                    "vcr_sticker": {
                      "can_viewer_link_back_to_original_media_from_vcr": true,
                      "end_background_color": "#FFFFFF",
                      "end_time_ms": 4310.5833333333,
                      "original_comment_author": {
                        "__typename": "XDTUserDict",
                        "strong_id__": "356635012",
                        "id": "356635012",
                        "full_name": "Meenah Tariq",
                        "is_private": false,
                        "is_verified": false,
                        "pk": "356635012",
                        "profile_pic_id": "3495891588465608853_356635012",
                        "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/465833652_1074439747253993_8082654619530362292_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=FBXXwdUTpBAQ7kNvwEO-HEq&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GLQOxBvptnd-MtEDALT9Rn_NWytwbkULAAAB1501500j-ccb7-5&oh=00_Af1JCzgOCpobd4sKw_aMQKGomxzam586pfNmOgWtKrModQ&oe=69DC624F&_nc_sid=10d13b",
                        "username": "meenahtariq"
                      },
                      "original_comment_id": "18090010117735782",
                      "original_comment_text": "Wait so none of y'all's parents stole the land of their siblings, thereby causing a forever-rift in the family?",
                      "original_media_id": "3691011991037807194",
                      "start_background_color": "#FFFFFF",
                      "start_time_ms": 0,
                      "text_color": ""
                    },
                    "width": 0.4741620410425,
                    "x": 0.49864244398711,
                    "y": 0.18581172000568,
                    "z": 0
                  }
                ],
                "visual_replies_info": {
                  "can_viewer_link_back_to_original_media_from_vcr": true,
                  "comment_info": {
                    "comment_id": "18090010117735782",
                    "commenter_username": "meenahtariq"
                  },
                  "original_media": {
                    "pk": "3691011991037807194"
                  }
                },
                "top_likers": [],
                "__typename": "XDTMediaDict",
                "strong_id__": "3731606998468236217_11255113",
                "id": "3731606998468236217_11255113",
                "are_remixes_crosspostable": true,
                "can_viewer_reshare": true,
                "can_viewer_save": true,
                "caption_is_edited": false,
                "code": "DPJVMtRD5O5",
                "device_timestamp": 1759062203666227,
                "like_count": 126,
                "comment_count": 3,
                "filter_type": 0,
                "has_audio": true,
                "has_high_risk_gen_ai_inform_treatment": false,
                "has_liked": false,
                "has_shared_to_fb": 0,
                "has_views_fetching": true,
                "ig_media_sharing_disabled": false,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/556541797_24528357973495890_7653273576408718679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=85tfp1Gv6FMQ7kNvwFc-1pG&_nc_oc=AdpIBJ7DWIqh87xStiOuYEbjHONUcNZ20LXZkBfjAvuFVVQ0PIy1eF3RhZrH75yK10E&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af1MwZNnhQeOQ1LRlKfKJzMi-Jf5THK7RgKyjeWzpYdx-Q&oe=69DC70CE",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/556541797_24528357973495890_7653273576408718679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=85tfp1Gv6FMQ7kNvwFc-1pG&_nc_oc=AdpIBJ7DWIqh87xStiOuYEbjHONUcNZ20LXZkBfjAvuFVVQ0PIy1eF3RhZrH75yK10E&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af1MwZNnhQeOQ1LRlKfKJzMi-Jf5THK7RgKyjeWzpYdx-Q&oe=69DC70CE",
                      "width": 640
                    }
                  },
                  "candidates": [
                    {
                      "height": 1334,
                      "scans_profile": "e35",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.82787-15/557068600_18527664097055114_2042385188664228571_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=103&ig_cache_key=MzczMTYwNjk5ODQ2ODIzNjIxNzE4NTI3NjY0MDkxMDU1MTE0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEyOTB4MjI5NC5zZHIuQzMifQ%3D%3D&_nc_ohc=wiCzqibkV5oQ7kNvwEsGtWm&_nc_oc=Adrmyd8oMyoqkJp1-iGkM2yguty7pfDBJc2N7Icr69HjjzjXoIpIelXxsI1OeZtYim4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af2g7yG3aVHgh2SZa2PDsGWk_Hfg4S_u1UGnwvJHUsznRw&oe=69DC7421",
                      "width": 750
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 446,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_width": 1500,
                      "thumbnail_duration": 1.7136476190476,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 179.933
                    }
                  }
                },
                "is_comments_gif_composer_enabled": true,
                "is_dash_eligible": 1,
                "is_post_live_clips_media": false,
                "is_quiet_post": false,
                "is_third_party_downloads_eligible": false,
                "like_and_view_counts_disabled": false,
                "media_type": 2,
                "number_of_qualities": 8,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQUpGaWladTNPcldHVDRtRFJ6UDZ1YWkzNzMxNjA2OTk4NDY4MjM2MjE3Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2NzIzMDA2M3wzNzMxNjA2OTk4NDY4MjM2MjE3fDExMjU1MTEzfGE5MmI2Y2UzYmJiMmJkMmEyYzM0ZDhmZjJmZjMyMTZlMDcwZWE1OTRkNzJmZGQ0ZTcxOWNkZDQ3YWNjZDJhYjUifSwic2lnbmF0dXJlIjoiIn0=",
                "original_height": 1920,
                "original_media_has_visual_reply_media": false,
                "original_width": 1080,
                "product_type": "clips",
                "taken_at": 1759108437,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "friendship_status": {
                    "following": false,
                    "is_bestie": false,
                    "is_feed_favorite": false,
                    "is_restricted": false,
                    "outgoing_request": false
                  },
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_facebook_onboarded_charity": false,
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "merchant_checkout_style": "none",
                  "pk": 11255113,
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NTAuQzMifQ%3D%3D&_nc_ohc=uVBRZd8AAZwQ7kNvwHWnFw2&_nc_oc=AdoAIJeklNEDeX-NjOmRbrwUU5j5aFQqkY_ttuPn797Tzr-bwab7XBdhUAqNTUs_cw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3zATSEgeYmwVYHBwA4bXDkKiJDsSa52j2nKpeuY-nxKw&oe=69DC47F5",
                  "seller_shoppable_feed_type": "none",
                  "show_account_transparency_details": true,
                  "show_shoppable_feed": false,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble"
                },
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT179.933334S\" FBManifestTimestamp=\"1775667229\" FBManifestIdentifier=\"FrqgtJ0NGA9yMmF2MS1yMWdlbjJ2cDkZxpKSouvn3NIC7tj3/IjQ7AKgmdn6y9i3A7qdt/3X2acExOrejMG8xASSgqSD9ZzUBMLE7PWfjrUF1Mn0k4SDwwXYtbOp1NGeBqTPi7KgxNoG1rq6hJ7O1weYyrW3gO7CCSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWgAMUABIUAAA=\"><Period id=\"0\" duration=\"PT179.933334S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:86.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"744864345244809v\" bandwidth=\"326070\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"7333878\" FBPlaybackResolutionMos=\"0:100,360:57.7,480:49.5,720:39.3,1080:35.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:90.4,480:86.6,720:77.8,1080:67.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN1Nm3NRnD2pKWKqPCyonAlz1PPLgDPAbu5e3P8seambiigyka7AkkZjzlVNG5M-L86o10HtDDp0-9pTw9nK8ux5rbO2Pz7Z_qzCxA.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=tSdCeuP02voQ7kNvwF4sXyU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjozMjYwNzAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1ABC1pzS5KQ79NZZjGLNCT8X9KGrSYQbaIJy4Zq5EviQ&amp;oe=69DC5620</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-17857\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-133318\" FBFirstSegmentRange=\"1290-187173\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"187174-299226\" FBPrefetchSegmentRange=\"1290-187173\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"801820059301431v\" bandwidth=\"400769\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"9013979\" FBPlaybackResolutionMos=\"0:100,360:62,480:54.4,720:45.3,1080:41.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.1,480:88.9,720:83.2,1080:75.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOdex0KstNjhfpxHA_boc7QDNpIf8DUCDqQjvpThoUXKioD_YRcKppdw76qo9qs4e8zCwO3DJLxCu_PSyhXTOH2QPJ6RlDDLBjx330.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=91NcIMycYuMQ7kNvwE6oDXx&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjo0MDA3NjksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af24xtTtnnnF9lABnVSlrCnw6kUJEkoLyxzVtUw_kGXrgw&amp;oe=69DC4080</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-21431\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-162156\" FBFirstSegmentRange=\"1290-229743\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"229744-364431\" FBPrefetchSegmentRange=\"1290-229743\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1756223445036396v\" bandwidth=\"628883\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"14144630\" FBPlaybackResolutionMos=\"0:100,360:70.9,480:64,720:55.3,1080:50.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.1,480:93.3,720:88.8,1080:81.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN3h6JJYlds_yoH1k_Guhq0nh5fkMWOZcfKVvIrYYbIGHgqIbusnGccVXoDNP20KA9m_8BlrmlOuDg2ekpd4NaqG0lyxaW2eTOvpxU.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=skczyzsnSIAQ7kNvwE1eJy_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjo2Mjg4ODMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0M5-faIbYxaoO0VFhboqcoi2sh14M5fSCcsYOz3dfMaw&amp;oe=69DC61F4</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-28208\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-239900\" FBFirstSegmentRange=\"1290-352244\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"352245-556287\" FBPrefetchSegmentRange=\"1290-352244\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1311114603561097v\" bandwidth=\"833525\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"18747375\" FBPlaybackResolutionMos=\"0:100,360:75.4,480:69.4,720:61.1,1080:55.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.6,480:95.3,720:91.9,1080:85.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPIYk7Onq_Fxo4odqeVNe_yO4kxCfHuB07Ev1xHD9BmExf_iJYdl4SDnpyV6ayzMqt3GDTxQiIrgiwoLVA8-B0-wyg3VcPXJpJL8qk.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=DVYkc6q5UfQQ7kNvwH1OLsh&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjo4MzM1MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3dvUj-AnFz6SgQ6JYyVmC2L6xpC7V2wll1tWgLZ5-P9A&amp;oe=69DC495B</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-32771\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-303162\" FBFirstSegmentRange=\"1290-455926\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"455927-717002\" FBPrefetchSegmentRange=\"1290-455926\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1524167918588193v\" bandwidth=\"979414\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"22028674\" FBPlaybackResolutionMos=\"0:100,360:77.6,480:72.3,720:64.3,1080:58.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.1,480:96.1,720:93.2,1080:87.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPaVBgedL6Ej4b1xqUFyQmo8Al3afGVmifTlWc0LSP6EiDNtzgyrCGPD4o1CZYtddU2QbX9rDC3lOSKpt1_dkjCt4FQWofhYq5h5xM.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=kCV7PTs9UBQQ7kNvwGMhcz4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjo5Nzk0MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1128W2pciCORAgcJCMOB-eV15rQsjtry_k6VB33kgM3w&amp;oe=69DC67C1</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-35858\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-346042\" FBFirstSegmentRange=\"1290-531123\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"531124-835359\" FBPrefetchSegmentRange=\"1290-531123\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1554761539031658v\" bandwidth=\"1270420\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"28573885\" FBPlaybackResolutionMos=\"0:100,360:81.3,480:75.7,720:68.6,1080:62.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:97.1,720:95.1,1080:89.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOxnPtT2_cPxjjsMksck_r4WWyqvdoAmQ_EvhocB2KaF8ePHlXaCMFiNtOffhLhZWE5paWYdBKwex1eyQsM840rhO725XTkSf_RfOc.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=7xnHUszVITMQ7kNvwFHaP0k&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjoxMjcwNDIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af16F2O8_JQzJ-uuZ7s01m6EMJwlIb4rFuGfV6KrU8lODQ&amp;oe=69DC5D91</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-42944\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-425728\" FBFirstSegmentRange=\"1290-674544\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"674545-1060808\" FBPrefetchSegmentRange=\"1290-674544\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2680300168983180v\" bandwidth=\"1700328\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"38243233\" FBPlaybackResolutionMos=\"0:100,360:84.8,480:79.4,720:72.7,1080:66.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.23,480:97.7,720:96.4,1080:92\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOLJg-A66gQIeqZn7B55mu86k_rm2E491N_YRjcK1_nrPo5QLnu1OogFDEJxjJk_yEl2BkCIbPi4etCQKIXW5f6TlI4cZo_IeP7CQ8.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=k521n6815l0Q7kNvwGdTM8-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjoxNzAwMzI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1r4CSFERaez_InYHBd7yfSf9G-EkbYhcPU6DSAFOgtaA&amp;oe=69DC42DB</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-51062\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-530340\" FBFirstSegmentRange=\"1290-876028\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"876029-1394595\" FBPrefetchSegmentRange=\"1290-876028\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1213202630633309v\" bandwidth=\"2405268\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"54098495\" FBPlaybackResolutionMos=\"0:100,360:88.1,480:84.2,720:77.8,1080:74.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.42,480:98.08,720:97.5,1080:96.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPmCBy1Kc_eDD2_QNLBEOh8cE8SqNvOs4iDm8DlXStGph7Ig2UAgn7YRB5RpiL-3TwBkG-idNjOvkVMPNMHvU0lApOp9AZjQ9tJJL8.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=nvELG_tI6F8Q7kNvwF6VB8M&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyMjgyMjM5MjUyMjIzMjEwLCJhc3NldF9hZ2VfZGF5cyI6MTkyLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTc5LCJiaXRyYXRlIjoyNDA1MjY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2-wKXeBvqHB41qFGDu1Wz-33t04KEzOkMzgFuDqMTq0Q&amp;oe=69DC609F</BaseURL><SegmentBase indexRange=\"826-1289\" timescale=\"15360\" FBMinimumPrefetchRange=\"1290-67429\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1290-722193\" FBFirstSegmentRange=\"1290-1226322\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1226323-1956379\" FBPrefetchSegmentRange=\"1290-1226322\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1887934531859410a\" bandwidth=\"37680\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"37680\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"848767\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNogrwc0e-U30c57YZc6jhteCdx_U6dPpt-hJTyQ7nutG-UmXM2C6MX7klJzL06uNDvWdwtq9SR5exIr0wMY0NOfFIKhVaPoErmkXI.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=8e8mqSrODMoQ7kNvwEv2ssC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjIyODIyMzkyNTIyMjMyMTAsImFzc2V0X2FnZV9kYXlzIjoxOTIsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNzksImJpdHJhdGUiOjM3NzM3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af03Ldz2I6mxbWSggt3sRsk9GKCQZ2iSEkZlMgGKd19XGw&amp;oe=69DC75EE</BaseURL><SegmentBase indexRange=\"837-1312\" timescale=\"44100\" FBMinimumPrefetchRange=\"1313-2211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1313-13872\" FBFirstSegmentRange=\"1313-24859\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"24860-52151\" FBPrefetchSegmentRange=\"1313-24859\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2162983921209003a\" bandwidth=\"80830\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"80830\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"1819262\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHxthcZfvRttPzzcA92iWKy-w2MgMGWIWORKeb4icY0Aw7SQJCQmVaxeM3pDK1L8O47V422SLk_ItwIrNL-pf405mM6DF-KPYub5Q.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=5lbJgB6DsQkQ7kNvwFLBiWb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjIyODIyMzkyNTIyMjMyMTAsImFzc2V0X2FnZV9kYXlzIjoxOTIsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNzksImJpdHJhdGUiOjgwODg3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3P1BW5_cfL_fmE6RCcAQJkugf3P1l3HyHSmURnnXR_Yg&amp;oe=69DC72BA</BaseURL><SegmentBase indexRange=\"838-1313\" timescale=\"44100\" FBMinimumPrefetchRange=\"1314-2622\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1314-27088\" FBFirstSegmentRange=\"1314-49521\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"49522-98039\" FBPrefetchSegmentRange=\"1314-49521\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1276473017883298a\" bandwidth=\"108900\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108900\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"2450588\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN4Cz5KCPJ6j_WJLR2mJSL_ogN17tXJMKa13shpbzy8SRzv2pMEjSVd82-dPneCmBLjpywPEASWP0i2lZDkSEN6BvBzrAIgVllq0z0.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=5xeQlZmfYF4Q7kNvwFLCVgL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjIyODIyMzkyNTIyMjMyMTAsImFzc2V0X2FnZV9kYXlzIjoxOTIsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNzksImJpdHJhdGUiOjEwODk1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1lJUS4zg3alC10ejcSRIio2XozE4iOYqp_IFv6hRRBqg&amp;oe=69DC659A</BaseURL><SegmentBase indexRange=\"833-1308\" timescale=\"44100\" FBMinimumPrefetchRange=\"1309-2405\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1309-35488\" FBFirstSegmentRange=\"1309-66439\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"66440-137988\" FBPrefetchSegmentRange=\"1309-66439\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"966893232662096a\" bandwidth=\"127566\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"127566\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"2870425\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOTQ-FgFLsvsPfrMfERDmcdLXDJEzYHYSHdstOCo61mxNQ6IApbZm4qSxhhQTBRqoYj--xkLcpBSXOiA0avNZMh4IsQL25cKHciFZI.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=j8rCG25RjmkQ7kNvwEUrra0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjIyODIyMzkyNTIyMjMyMTAsImFzc2V0X2FnZV9kYXlzIjoxOTIsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNzksImJpdHJhdGUiOjEyNzYyNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3qDcj8Ya7MGqBbNXx3zflfm8IEqILSOoRikrp3DCTdmQ&amp;oe=69DC5033</BaseURL><SegmentBase indexRange=\"833-1308\" timescale=\"44100\" FBMinimumPrefetchRange=\"1309-2409\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1309-41114\" FBFirstSegmentRange=\"1309-79260\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"79261-170295\" FBPrefetchSegmentRange=\"1309-79260\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "__is_XDTMediaDict": true
              }
            },
            "parent_comment_id": "18090010117735782",
            "pk": "18286499842276264",
            "private_reply_status": 0,
            "replied_to_comment_id": "18090010117735782",
            "share_enabled": true,
            "status": "Active",
            "strong_id__": "18286499842276264",
            "text": "I miss busan!!!! 😭😭\n\n#Korea #busan #seoul #family #vlog #travel #cousins",
            "type": 2,
            "user": {
              "fbid_v2": 17841401653390175,
              "full_name": "Adeline Tan ᐧ༚̮ᐧ",
              "id": "11255113",
              "is_mentionable": true,
              "is_private": false,
              "is_verified": false,
              "pk": 11255113,
              "pk_id": "11255113",
              "profile_pic_id": "1992089677481616027_11255113",
              "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NTAuQzMifQ%3D%3D&_nc_ohc=uVBRZd8AAZwQ7kNvwHWnFw2&_nc_oc=AdoAIJeklNEDeX-NjOmRbrwUU5j5aFQqkY_ttuPn797Tzr-bwab7XBdhUAqNTUs_cw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3zATSEgeYmwVYHBwA4bXDkKiJDsSa52j2nKpeuY-nxKw&oe=69DC47F5",
              "strong_id__": "11255113",
              "username": "addie_ble"
            },
            "user_id": 11255113
          }
        ],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "18090010117735782",
        "text": "Wait so none of y'all's parents stole the land of their siblings, thereby causing a forever-rift in the family?",
        "type": 0,
        "user": {
          "fbid_v2": 17841400810365572,
          "full_name": "Meenah Tariq",
          "id": "356635012",
          "is_mentionable": true,
          "is_private": false,
          "is_verified": false,
          "pk": "356635012",
          "pk_id": "356635012",
          "profile_pic_id": "3495891588465608853_356635012",
          "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/465833652_1074439747253993_8082654619530362292_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=108&ig_cache_key=GLQOxBvptnd-MtEDALT9Rn_NWytwbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=JO1aAwSMOEoQ7kNvwGUnPWi&_nc_oc=AdoMg_MvmW2TRIZ27sEqf9YLOH257bPoTSI6_RENRlEzPTWz0S7UFMXI-Ld3cQu5fRQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af1tXPFybIaWchSskKqrYmbjjW_Ea4Pa2e7CRMW3rfJlWA&oe=69DC624F",
          "strong_id__": "356635012",
          "username": "meenahtariq"
        },
        "user_id": 356635012,
        "has_liked": false,
        "like_count": 2155
      },
      {
        "bit_flags": 0,
        "comment_has_a_visual_reply_media": true,
        "comment_like_count": 340,
        "content_type": "comment",
        "created_at": 1757693209,
        "created_at_for_fb_app": 1757693209,
        "created_at_utc": 1757693209,
        "did_report_as_spam": false,
        "has_liked_comment": false,
        "has_disliked_comment": false,
        "inline_composer_display_condition": "never",
        "is_covered": false,
        "is_liked_by_media_owner": true,
        "is_pinned": true,
        "is_photo_comments_enabled_for_comment_author": false,
        "is_text_editable": false,
        "is_edited": false,
        "meta_ai_comment_type": "NONE",
        "is_ranked_comment": true,
        "keywords_data": [],
        "liked_by_media_coauthors": [],
        "other_preview_users": [],
        "media_id": 3691011991037807194,
        "pk": "17893429782322413",
        "preview_child_comments": [
          {
            "bit_flags": 0,
            "comment_like_count": 27,
            "content_type": "comment",
            "created_at": 1762860355,
            "created_at_utc": 1762860355,
            "created_at_for_fb_app": 1762860355,
            "did_report_as_spam": false,
            "has_liked_comment": false,
            "has_disliked_comment": false,
            "is_covered": false,
            "is_created_by_media_owner": true,
            "is_photo_comments_enabled_for_comment_author": false,
            "is_text_editable": false,
            "is_edited": false,
            "meta_ai_comment_type": "NONE",
            "is_ranked_comment": false,
            "liked_by_media_coauthors": [],
            "media_id": 3691011991037807194,
            "media_info": {
              "media": {
                "can_see_insights_as_brand": false,
                "caption": {
                  "__typename": "XDTCommentDict",
                  "strong_id__": "17920330227054327",
                  "pk": "17920330227054327",
                  "bit_flags": 0,
                  "content_type": "comment",
                  "created_at": 1762860353,
                  "created_at_utc": 1762860353,
                  "did_report_as_spam": false,
                  "is_covered": false,
                  "is_ranked_comment": false,
                  "media_id": 3763466966498528063,
                  "private_reply_status": 0,
                  "share_enabled": false,
                  "status": "Active",
                  "text": "I will always love u brackenfern…… 🥀❤️‍🩹\n\n#korea #travel #family #busan #jeju #holiday #vlog #cousins",
                  "type": 1,
                  "user": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "11255113",
                    "id": "11255113",
                    "fbid_v2": 17841401653390175,
                    "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                    "is_private": false,
                    "is_verified": false,
                    "pk": 11255113,
                    "profile_pic_id": "1992089677481616027_11255113",
                    "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                    "username": "addie_ble"
                  },
                  "user_id": 11255113
                },
                "clips_demotion_control": {
                  "confirmation_body": "We'll suggest fewer posts like this.",
                  "confirmation_icon": "none",
                  "confirmation_style": "bottomsheet",
                  "confirmation_title": "Post hidden",
                  "confirmation_title_style": "large_left",
                  "enable_word_wrapping": true,
                  "followup_options": [
                    {
                      "data": "author_id:11255113",
                      "demotion_control": {
                        "confirmation_body": "We won't suggest posts from addie_ble.",
                        "confirmation_icon": "eye-off-pano",
                        "confirmation_style": "bottomsheet",
                        "undo_style": "inline"
                      },
                      "id": "dislike_author",
                      "show_icon": true,
                      "text": "Don't suggest posts from addie_ble"
                    },
                    {
                      "id": "hide_all_specific_words",
                      "show_icon": true,
                      "text": "Don't suggest posts with certain words"
                    },
                    {
                      "id": "control_center",
                      "show_icon": true,
                      "text": "Manage content preferences"
                    }
                  ],
                  "title": "Not interested",
                  "title_style": "normal",
                  "undo_style": "top_right"
                },
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
                    "best_audio_cluster_id": "1543742239966749"
                  },
                  "audio_type": "original_sounds",
                  "branded_content_tag_info": {
                    "can_add_tag": false
                  },
                  "clips_creation_entry_point": "clips",
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
                    "mashups_allowed": true,
                    "non_privacy_filtered_mashups_media_count": 0
                  },
                  "music_canonical_id": "18537467692032860",
                  "original_sound_info": {
                    "allow_creator_to_rename": true,
                    "audio_asset_id": "854155170904035",
                    "audio_parts": [],
                    "audio_parts_by_filter": [],
                    "can_remix_be_shared_to_fb": true,
                    "can_remix_be_shared_to_fb_expansion": true,
                    "consumption_info": {
                      "is_bookmarked": false,
                      "is_trending_in_clips": false,
                      "should_mute_audio_reason": ""
                    },
                    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT156.129517S\" FBManifestTimestamp=\"1775667230\" FBManifestIdentifier=\"FrygtJ0NKRbcgaqPisihBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT156.129517S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1481180959817838a\" bandwidth=\"58121\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"58121\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m86/AQNAo-2xc6MpwR6THPBO0Kj17naZ_nznS3wVcHiNognhRSVnuy5wsh4XEFaJxcUfmQhstBufpLKvxAB_Pha8ag.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=bgufJRRtPgsQ7kNvwFVFXrL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjgyMjg4Mzk0NzEzMzM4MiwiYXNzZXRfYWdlX2RheXMiOjE0OCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1NiwiYml0cmF0ZSI6NTgyMTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2JuIsBR7l465ifcrX1ev1qG8HTP5AAowXDp49__Qf5fQ&amp;oe=69D8569E</BaseURL><SegmentBase indexRange=\"824-1803\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                    "duration_in_ms": 156133,
                    "hide_remixing": false,
                    "ig_artist": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "11255113",
                      "id": "11255113",
                      "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                      "is_private": false,
                      "is_verified": false,
                      "pk": "11255113",
                      "profile_pic_id": "1992089677481616027_11255113",
                      "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                      "username": "addie_ble"
                    },
                    "is_audio_automatically_attributed": false,
                    "is_eligible_for_audio_effects": true,
                    "is_explicit": false,
                    "is_original_audio_download_eligible": false,
                    "is_reuse_disabled": false,
                    "is_xpost_from_fb": false,
                    "oa_owner_is_music_artist": false,
                    "original_audio_subtype": "default",
                    "original_audio_title": "Original audio",
                    "original_media_id": "3763466966498528063",
                    "progressive_download_url": "https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m69/AQMwgUl5s4puoDJpjiO3sqSnoay6DGPXKZ3jRhWCUN0DJjgVHZOKwv1ipCGyztcMTShCC6gBX4DSbK1MB6YhuIdz.mp4?strext=1&_nc_cat=110&_nc_sid=8bf8fe&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ohc=D3jUeltv6ycQ7kNvwFWdJxk&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6ODIyODgzOTQ3MTMzMzgyLCJhc3NldF9hZ2VfZGF5cyI6MTQ4LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0gfNbg7Z96oampuf2M1L5H7PG-hLTsQJuWwh6d47ze6A&oe=69DC4688",
                    "should_mute_audio": false,
                    "time_created": 1762860354
                  },
                  "professional_clips_upsell_type": 0,
                  "show_achievements": false
                },
                "coauthor_producer_can_see_organic_insights": false,
                "coauthor_producers": [],
                "comment_inform_treatment": {
                  "should_have_inform_treatment": false,
                  "text": ""
                },
                "crosspost_metadata": {
                  "unified_feedback_enabled": true,
                  "is_feedback_aggregated": true,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "deleted_reason": 0,
                "enable_media_notes_production": true,
                "enable_waist": true,
                "fb_comment_count": 0,
                "fb_like_count": 0,
                "fb_play_count": 3,
                "ig_play_count": 5380,
                "reshare_count": 9,
                "fundraiser_tag": {},
                "gen_ai_detection_method": {
                  "detection_method": "NONE"
                },
                "has_delayed_metadata": false,
                "has_more_comments": false,
                "hide_view_all_comment_entrypoint": true,
                "invited_coauthor_producers": [],
                "is_artist_pick": false,
                "is_cutout_sticker_allowed": true,
                "is_in_profile_grid": false,
                "is_organic_product_tagging_eligible": true,
                "is_paid_partnership": false,
                "is_reshare_of_text_post_app_media_in_ig": false,
                "is_reuse_allowed": true,
                "is_tagged_media_shared_to_viewer_profile_grid": false,
                "is_unified_video": false,
                "is_visual_reply_commenter_notice_enabled": true,
                "media_notes": {
                  "items": []
                },
                "mezql_token": "",
                "owner": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "biography": "⁽̨̡ ¨̮ ⁾̧̢ \n@dee_bakes 🍰\ntiktok: addieblesausage 🌭\nwork with me: adelinetan1996@gmail.com 🧚🏼‍♀️",
                  "can_see_quiet_post_attribution": true,
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "friendship_status": {
                    "following": false,
                    "is_bestie": false,
                    "is_feed_favorite": false,
                    "is_restricted": false
                  },
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "pk": "11255113",
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NTAuYzIifQ&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=UIiEspW3z0kQ7kNvwF1ibm9&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&oh=00_Af15ETmtV6fAS4mUg00ExOtjXfd1Z2AbqwP3190Nnmo4cQ&oe=69DC47F5&_nc_sid=10d13b",
                  "show_account_transparency_details": true,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble",
                  "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
                },
                "photo_of_you": false,
                "play_count": 5383,
                "profile_grid_control_enabled": false,
                "senders": [],
                "share_count_disabled": false,
                "is_social_ufi_disabled": false,
                "sharing_friction_info": {
                  "should_have_sharing_friction": false
                },
                "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
                "floating_context_items": [],
                "subscribe_cta_visible": false,
                "timeline_pinned_user_ids": [],
                "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
                "video_sticker_locales": [],
                "video_subtitles_uri": "https://scontent-jnb2-1.cdninstagram.com/v/t39.36743-6/580635850_698046846263194_5914425684830297166_n.srt?_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=_PADOwaEab0Q7kNvwHdlNJm&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUAAAAA&ccb=7-5&oh=00_Af0d4arPaHuILNZKDlVk_tmI3uKcAhqLotSXdV6faU0Y4g&oe=69DC64C4&_nc_sid=10d13b",
                "view_state_item_type": 128,
                "visual_comment_reply_sticker_info": [
                  {
                    "end_time_ms": 5601.6,
                    "height": 0.18095930232558,
                    "is_fb_sticker": 0,
                    "is_hidden": 0,
                    "is_pinned": 0,
                    "is_sticker": 1,
                    "rotation": 0,
                    "start_time_ms": 0,
                    "vcr_sticker": {
                      "can_viewer_link_back_to_original_media_from_vcr": true,
                      "end_background_color": "#FF81B1",
                      "end_time_ms": 5601.6,
                      "original_comment_author": {
                        "__typename": "XDTUserDict",
                        "strong_id__": "259645306",
                        "id": "259645306",
                        "full_name": "에밀리 ✨",
                        "is_private": false,
                        "is_verified": false,
                        "pk": "259645306",
                        "profile_pic_id": "3855655870168638939_259645306",
                        "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.82787-19/654024898_18577132519061307_7893361867462414935_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHZU_wwZNw8P_wX7fjUA4ZrRbB8YgR1K-amJPK7m6-N9Sa3b_4E9VHszmIRFYsvAM0&_nc_ohc=Np8pTQ3YRgMQ7kNvwFDpMQw&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GMKg_yY7d764zf9BAFcStjHM2optbmNDAQAB1501500j-ccb7-5&oh=00_Af0GPKDQh0-L8epxxMyjhLuZIvIXd9HDRQr0HBWyoKitCA&oe=69DC4FA7&_nc_sid=10d13b",
                        "username": "emilyrcrespo"
                      },
                      "original_comment_id": "17893429782322413",
                      "original_comment_text": "LETS GOOOOOO!! I shouted through the screen as if I were apart of this",
                      "original_media_id": "3691011991037807194",
                      "start_background_color": "#9658FF",
                      "start_time_ms": 0,
                      "text_color": ""
                    },
                    "width": 0.6077519379845,
                    "x": 0.5,
                    "y": 0.19513081395349,
                    "z": 0
                  }
                ],
                "visual_replies_info": {
                  "can_viewer_link_back_to_original_media_from_vcr": true,
                  "comment_info": {
                    "comment_id": "17893429782322413",
                    "commenter_username": "emilyrcrespo"
                  },
                  "original_media": {
                    "pk": "3691011991037807194"
                  }
                },
                "top_likers": [],
                "__typename": "XDTMediaDict",
                "strong_id__": "3763466966498528063_11255113",
                "id": "3763466966498528063_11255113",
                "are_remixes_crosspostable": true,
                "can_viewer_reshare": true,
                "can_viewer_save": true,
                "caption_is_edited": false,
                "code": "DQ6hUQuD8s_",
                "device_timestamp": 1762860209982184,
                "like_count": 94,
                "comment_count": 0,
                "filter_type": 0,
                "has_audio": true,
                "has_high_risk_gen_ai_inform_treatment": false,
                "has_liked": false,
                "has_shared_to_fb": 0,
                "has_views_fetching": true,
                "ig_media_sharing_disabled": false,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/576087483_851196801191753_8123322739762290395_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m3dJLeBoyc4Q7kNvwFRTa0R&_nc_oc=Adrr1qssPkRBHS755s9kIRx1il6gwZkB0eYzLw2ui8O9E_eFxFqNadxS98LA4X4YR7k&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af2IrTOwHi9x9xkmg_qyZEwCHBc_yd8UCj4bo9uSVxmg6A&oe=69DC5063",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.71878-15/576087483_851196801191753_8123322739762290395_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m3dJLeBoyc4Q7kNvwFRTa0R&_nc_oc=Adrr1qssPkRBHS755s9kIRx1il6gwZkB0eYzLw2ui8O9E_eFxFqNadxS98LA4X4YR7k&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af2IrTOwHi9x9xkmg_qyZEwCHBc_yd8UCj4bo9uSVxmg6A&oe=69DC5063",
                      "width": 640
                    }
                  },
                  "candidates": [
                    {
                      "height": 1280,
                      "scans_profile": "e15",
                      "url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.82787-15/581799976_18536615677055114_3773883212194281531_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ig_cache_key=Mzc2MzQ2Njk2NjQ5ODUyODA2MzE4NTM2NjE1Njc0MDU1MTE0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjcyMHgxMjgwLnNkci5DMyJ9&_nc_ohc=KGs_mmG2VXEQ7kNvwFyGUJz&_nc_oc=AdpopssHfLmRMu2Dr2cpYtzZXxJn6VEc_EHh_KkQ0WvNeG4jwr6TsRJs9jE74i10LMM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af3XbBZQgfaRG3TVTUfqNqnccOhkFNwfLVxyFnwHeP_Jwg&oe=69DC492F",
                      "width": 720
                    }
                  ],
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "file_size_kb": 472,
                      "max_thumbnails_per_sprite": 105,
                      "rendered_width": 96,
                      "sprite_height": 1232,
                      "sprite_width": 1500,
                      "thumbnail_duration": 1.486980952381,
                      "thumbnail_height": 176,
                      "thumbnail_width": 100,
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "video_length": 156.133
                    }
                  }
                },
                "is_comments_gif_composer_enabled": true,
                "is_dash_eligible": 1,
                "is_post_live_clips_media": false,
                "is_quiet_post": false,
                "is_third_party_downloads_eligible": false,
                "like_and_view_counts_disabled": false,
                "media_type": 2,
                "number_of_qualities": 8,
                "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQUpGaWladTNPcldHVDRtRFJ6UDZ1YWkzNzYzNDY2OTY2NDk4NTI4MDYzIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2NzIyOTk3NHwzNzYzNDY2OTY2NDk4NTI4MDYzfDExMjU1MTEzfDUwYzQ2ZTkxZWViYTk2YjJiYjkwZDI2ZTMzYTQ5NjUxOWYyNjVlYTJjY2JiMDljMDNmODUzMTUxYmMyZGU2OGYifSwic2lnbmF0dXJlIjoiIn0=",
                "original_height": 1920,
                "original_media_has_visual_reply_media": false,
                "original_width": 1080,
                "product_type": "clips",
                "taken_at": 1763031207,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "11255113",
                  "id": "11255113",
                  "account_badges": [],
                  "fan_club_info": {},
                  "fbid_v2": 17841401653390175,
                  "feed_post_reshare_disabled": false,
                  "friendship_status": {
                    "following": false,
                    "is_bestie": false,
                    "is_feed_favorite": false,
                    "is_restricted": false,
                    "outgoing_request": false
                  },
                  "full_name": "Adeline Tan ᐧ༚̮ᐧ",
                  "has_anonymous_profile_picture": false,
                  "interop_messaging_user_fbid": "113099470085044",
                  "is_facebook_onboarded_charity": false,
                  "is_favorite": false,
                  "is_private": false,
                  "is_unpublished": false,
                  "is_verified": false,
                  "merchant_checkout_style": "none",
                  "pk": 11255113,
                  "profile_pic_id": "1992089677481616027_11255113",
                  "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NTAuQzMifQ%3D%3D&_nc_ohc=uVBRZd8AAZwQ7kNvwHWnFw2&_nc_oc=AdoAIJeklNEDeX-NjOmRbrwUU5j5aFQqkY_ttuPn797Tzr-bwab7XBdhUAqNTUs_cw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3zATSEgeYmwVYHBwA4bXDkKiJDsSa52j2nKpeuY-nxKw&oe=69DC47F5",
                  "seller_shoppable_feed_type": "none",
                  "show_account_transparency_details": true,
                  "show_shoppable_feed": false,
                  "third_party_downloads_enabled": 2,
                  "transparency_product_enabled": false,
                  "username": "addie_ble"
                },
                "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT156.133331S\" FBManifestTimestamp=\"1775667229\" FBManifestIdentifier=\"FrqgtJ0NGA9yMmF2MS1yMWdlbjJ2cDkZxtrL+bTOwvgChIiD+9bejgOe4ov7r8uZA4jhi+fXo7kD+MyL+uq0wgPwvI+rgtyHBOaY4YqtvvAEkrDct76CogXAmdOFscfnBrr9oM+egbMHvPPa+8K5tQjE8Zmi8vC6DSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eQAWqAIUABIUAAA=\"><Period id=\"0\" duration=\"PT156.133331S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.9\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1916575608890976v\" bandwidth=\"230964\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"4507662\" FBPlaybackResolutionMos=\"0:100,360:37.7,480:33.2,720:29.9,1080:29.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:84.7,480:78.8,720:68.6,1080:57.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMvK5ZlR5bglotbq9InH3SPunHkIC4jL1Un5flNYp0zJUqkGm7GVEGrn4ehkN3cyAhBvdB3yef0MTdwy0hZrFyH78BdDUqHZ5j1kno.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=L0OQjLDL30EQ7kNvwGcDAOb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjIzMDk2NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3heHWlUQ28nrnmZ8tCs0g7nrNSB0X7n_ZP0fs7_uWRag&amp;oe=69DC4421</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-12435\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-112084\" FBFirstSegmentRange=\"1242-170503\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"170504-282670\" FBPrefetchSegmentRange=\"1242-170503\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2082496312516445v\" bandwidth=\"324663\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"6336340\" FBPlaybackResolutionMos=\"0:100,360:48.7,480:42.6,720:37.4,1080:35.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:90.3,480:85.6,720:76.7,1080:66.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPct6za7B14pZhK5sy7UzW1gJcvEQFIEiYfuYqueZX5K3MA-Y4XgSnv9fG71cKwcK_E4nFzAcfFVYhy5hjlJ55QdFc9Rieb99fmks0.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=gr5TvvZrvukQ7kNvwHskFrM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjMyNDY2MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Q2CG_VoP2fkgVcXpRT2W5l1-Q05REPGQboISxq26_Aw&amp;oe=69DC4DA5</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-14921\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-159272\" FBFirstSegmentRange=\"1242-245925\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"245926-403453\" FBPrefetchSegmentRange=\"1242-245925\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"827977139958509v\" bandwidth=\"380657\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"7429161\" FBPlaybackResolutionMos=\"0:100,360:52.8,480:46.3,720:41.2,1080:39\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.4,480:88.4,720:80.7,1080:71.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNCGGwARWpDDJtIlDBVr_kjc4X8Ar4JzHrJ29NSFtcdDmU6hMTgBMDfGbiq4YJnD862H1a6aUjOtNMSSp8pIht4C6Z09x2m3p5Me20.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=V12u1vKSk-wQ7kNvwGqFZqi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjM4MDY1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2OE0RkrpussF3kjLLVkQiRFl-9KwOUS41gv-OcPIzEsA&amp;oe=69DC5FDE</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-16324\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-189558\" FBFirstSegmentRange=\"1242-292574\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"292575-476623\" FBPrefetchSegmentRange=\"1242-292574\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1142873931247416v\" bandwidth=\"584547\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"11408414\" FBPlaybackResolutionMos=\"0:100,360:63.6,480:57.5,720:51.9,1080:48.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:94.1,720:88.7,1080:80.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPn1vmrALZt-3xAGgcw4OFKZgbyZHBpFKrJfWEje21Yg_IVpmuCmW5V5lDvTqJk0meLqCbSQ9lhPrSzzKGXRQfWrk0Z6N0r6OGTpXM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=J1kwHoiI8qIQ7kNvwGFDaC2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjU4NDU0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af34KYGnN4Fv6ixzY80qbryySQ_he7IFZjfreQsirIMwsg&amp;oe=69DC6A88</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-22024\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-293958\" FBFirstSegmentRange=\"1242-458242\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"458243-745212\" FBPrefetchSegmentRange=\"1242-458242\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1482184413907977v\" bandwidth=\"812878\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"15864671\" FBPlaybackResolutionMos=\"0:100,360:71.3,480:65.9,720:59.8,1080:55.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.7,720:93.7,1080:86.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMa8WYMX1wHWs01gdNX2Lyp0Em4KjP0jX1SDu4nWZQ8O6d5M_-s6ykKbshV7Zq5WkyJopPq1bXFUjtZZZx1AjyzpQ4JS-daSB-6z8M.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=4D1ZCMryoWUQ7kNvwH_nMx-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjgxMjg3OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1MajELopF2WBdXWLUftf2M1cBpFOaaQXIUEt_xOgXVhg&amp;oe=69DC7547</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-25648\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-413149\" FBFirstSegmentRange=\"1242-646922\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"646923-1049304\" FBPrefetchSegmentRange=\"1242-646922\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"3788657528093794v\" bandwidth=\"1005971\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"19633216\" FBPlaybackResolutionMos=\"0:100,360:75.1,480:70.1,720:64.3,1080:59.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.28,480:97.5,720:95.3,1080:89.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMJ3N8_AwlbY81DEeIgpXCqpWxxUGv6a9WF86hOPHF2BKmZPpz9lj994rNiM95V8HHnvmdXyKQV72-uTsQAn-f7Jf4AA5xFU1hz1B4.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=MtGHEbpdIfwQ7kNvwHrbeMG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjEwMDU5NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ZKPvzqCXddm_DsYvtHOUu65ibcXU4sC5gmEIRbjLW8g&amp;oe=69DC72F8</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-28821\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-517171\" FBFirstSegmentRange=\"1242-812084\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"812085-1307880\" FBPrefetchSegmentRange=\"1242-812084\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1373261714433587v\" bandwidth=\"1315920\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"25682388\" FBPlaybackResolutionMos=\"0:100,360:79,480:74.4,720:69,1080:64.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.83,480:98.39,720:96.9,1080:92.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQO15uXtp2gzg6yvEBaiObmwIwgsOEvCrotJ20gWgvxoeIm49zEZDnIRcDrntnUI1x-ipxQroE4weGRbEq6-quhETNd3Y0RIY-3yqjg.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=aUJxO_MyIE0Q7kNvwFj-b9N&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjEzMTU5MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0xBcB1-x9LBdGdn8VJRvdCuG6crEfddCE4ZvinKp4rcg&amp;oe=69DC44C3</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-33801\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-676765\" FBFirstSegmentRange=\"1242-1067762\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1067763-1718055\" FBPrefetchSegmentRange=\"1242-1067762\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"990468173296444v\" bandwidth=\"1859103\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"36283499\" FBPlaybackResolutionMos=\"0:100,360:84.9,480:80.4,720:75.6,1080:72.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.24,480:99.104,720:98.43,1080:97.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPPOOoQgnxnGDsbc0KTSpn-9PWqA8dyd0XieUDiDyhWGNpGFIE2fxxuv-P-4Et1VwSXtoZxIu2XbAYAAS5ahadRwfsFETDYREdwxcw.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=0enLoXdj7vUQ7kNvwEReQRk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjo4MjI4ODM5NDcxMzMzODIsImFzc2V0X2FnZV9kYXlzIjoxNDgsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxNTYsImJpdHJhdGUiOjE4NTkxMDMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2tF1xYLMOqvK2GfcRjoeSLHmxBdhLCqKykp6yW_SAaqA&amp;oe=69DC67B7</BaseURL><SegmentBase indexRange=\"826-1241\" timescale=\"15360\" FBMinimumPrefetchRange=\"1242-46480\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1242-907250\" FBFirstSegmentRange=\"1242-1441992\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1441993-2350083\" FBPrefetchSegmentRange=\"1242-1441992\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"970382336161860a\" bandwidth=\"37608\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"37608\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"735211\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPEYdW0PxVuhwY-Dr399DDPIFzrojYcKhOkaIeNw7oYbxY5LKHrJQCr9UdOO83FoGOQm3-Oz_Pn-oIQ1e1kIWSeONGJ4FZ38LQeXk0.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=o9YS2Dj2BJEQ7kNvwHui9Pb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjgyMjg4Mzk0NzEzMzM4MiwiYXNzZXRfYWdlX2RheXMiOjE0OCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1NiwiYml0cmF0ZSI6Mzc2NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1hnN57kdG_HV_9dfzNwfTCpBjO7iIB1rR_rFi6CSGrZA&amp;oe=69DC4480</BaseURL><SegmentBase indexRange=\"837-1252\" timescale=\"44100\" FBMinimumPrefetchRange=\"1253-2348\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1253-13658\" FBFirstSegmentRange=\"1253-24725\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"24726-48106\" FBPrefetchSegmentRange=\"1253-24725\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"876837835137538a\" bandwidth=\"79863\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"79863\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"1559859\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNlJW6TLv-KO4C7TDy2xhhAsmIilxYylXMCsKij1iDu1baDScuVQJoOHnCi3mX-tPg43gKIwLnhlC-RbSC3gLdgNuLHvH6tAeegmhA.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=HW21S-KQk4UQ7kNvwEOWqWX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjgyMjg4Mzk0NzEzMzM4MiwiYXNzZXRfYWdlX2RheXMiOjE0OCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1NiwiYml0cmF0ZSI6Nzk5MjYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af18V0zpPm_SBOT6mvqteS08D95vwfw3K9hr1enrJKdcnw&amp;oe=69DC714C</BaseURL><SegmentBase indexRange=\"838-1253\" timescale=\"44100\" FBMinimumPrefetchRange=\"1254-2851\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1254-26866\" FBFirstSegmentRange=\"1254-51343\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"51344-102546\" FBPrefetchSegmentRange=\"1254-51343\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"900695439014031a\" bandwidth=\"108377\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108377\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"2116350\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP2W405VaNQp_-wqOcuC2m4wnNIeZBlzY6A7RxjJFTtcqmiBAljVlp4oql1Z9cigj-SUPR7oVlRa_b5AAQ16HVBRadzCtzIzMmNL78.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=n9eqiqVBCCoQ7kNvwFgv_oK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjgyMjg4Mzk0NzEzMzM4MiwiYXNzZXRfYWdlX2RheXMiOjE0OCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1NiwiYml0cmF0ZSI6MTA4NDQwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2zxA0jRnfDySPhh8IKUFDK-zy4ULL4tQQ3s-QzD1PGFw&amp;oe=69DC41F2</BaseURL><SegmentBase indexRange=\"833-1248\" timescale=\"44100\" FBMinimumPrefetchRange=\"1249-2555\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1249-35153\" FBFirstSegmentRange=\"1249-68188\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"68189-136358\" FBPrefetchSegmentRange=\"1249-68188\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2369336286862558a\" bandwidth=\"127007\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"127007\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"2479927\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-jnb2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNCoCz5LDhD1BadCWmackbHxSiVCP4_kcb7rVgjp6L8C1j9xPGANMZiGGNNkb0RXf-H4itrqAnSCTtJspMenDjERC88OWv3lnC7g4c.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-jnb2-1.cdninstagram.com&amp;_nc_ohc=dpFTqpWzhcMQ7kNvwF32g0j&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjgyMjg4Mzk0NzEzMzM4MiwiYXNzZXRfYWdlX2RheXMiOjE0OCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjE1NiwiYml0cmF0ZSI6MTI3MDcwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3bDrR-LAkk4boavaED9wdY0tCTjdtgydza-UVenVtjdQ&amp;oe=69DC5212</BaseURL><SegmentBase indexRange=\"833-1248\" timescale=\"44100\" FBMinimumPrefetchRange=\"1249-2594\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1249-40530\" FBFirstSegmentRange=\"1249-78665\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"78666-157294\" FBPrefetchSegmentRange=\"1249-78665\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                "video_subtitles_locale": "en_US",
                "__is_XDTMediaDict": true
              }
            },
            "parent_comment_id": "17893429782322413",
            "pk": "18086930504508184",
            "private_reply_status": 0,
            "replied_to_comment_id": "17893429782322413",
            "share_enabled": true,
            "status": "Active",
            "strong_id__": "18086930504508184",
            "text": "I will always love u brackenfern…… 🥀❤️‍🩹\n\n#korea #travel #family #busan #jeju #holiday #vlog #cousins",
            "type": 2,
            "user": {
              "fbid_v2": 17841401653390175,
              "full_name": "Adeline Tan ᐧ༚̮ᐧ",
              "id": "11255113",
              "is_mentionable": true,
              "is_private": false,
              "is_verified": false,
              "pk": 11255113,
              "pk_id": "11255113",
              "profile_pic_id": "1992089677481616027_11255113",
              "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.2885-19/52183978_551406722046419_1487584497317707776_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GKpDHAPTWcthgPUBAAAAAAA49qQUbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NTAuQzMifQ%3D%3D&_nc_ohc=uVBRZd8AAZwQ7kNvwHWnFw2&_nc_oc=AdoAIJeklNEDeX-NjOmRbrwUU5j5aFQqkY_ttuPn797Tzr-bwab7XBdhUAqNTUs_cw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af3zATSEgeYmwVYHBwA4bXDkKiJDsSa52j2nKpeuY-nxKw&oe=69DC47F5",
              "strong_id__": "11255113",
              "username": "addie_ble"
            },
            "user_id": 11255113
          }
        ],
        "private_reply_status": 0,
        "share_enabled": true,
        "status": "Active",
        "strong_id__": "17893429782322413",
        "text": "LETS GOOOOOO!! I shouted through the screen as if I were apart of this",
        "type": 0,
        "user": {
          "fbid_v2": 17841401839184056,
          "full_name": "에밀리 ✨",
          "id": "259645306",
          "is_mentionable": true,
          "is_private": false,
          "is_verified": false,
          "pk": "259645306",
          "pk_id": "259645306",
          "profile_pic_id": "3855655870168638939_259645306",
          "profile_pic_url": "https://scontent-jnb2-1.cdninstagram.com/v/t51.82787-19/654024898_18577132519061307_7893361867462414935_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=103&ig_cache_key=GMKg_yY7d764zf9BAFcStjHM2optbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=1BWsLt86SKQQ7kNvwEORgUx&_nc_oc=AdrjU7va1GW6jv_0ZVnHVSU5nb3Ukr977zCSqFT_3kOqZVvwRQZfcSB4Mm1r3txPV48&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-jnb2-1.cdninstagram.com&_nc_gid=1mRu0bzb2vjCWLT7qS9JOg&_nc_ss=7a3ba&oh=00_Af0MXYvWlqfg-TpPat0FUL1odP6tHhS9GrcoQB2NhLw_Cw&oe=69DC4FA7",
          "strong_id__": "259645306",
          "username": "emilyrcrespo"
        },
        "user_id": 259645306,
        "has_liked": false,
        "like_count": 340
      }
    ],
    "has_more_comments": false,
    "has_more_headload_comments": true,
    "initiate_at_top": true,
    "insert_new_comment_to_top": true,
    "is_ranked": true,
    "liked_by_media_owner_badge_enabled": true,
    "media_header_display": "none",
    "next_min_id": "{\"cached_comments_cursor\":\"18119184721490611\",\"bifilter_token\":\"GgYYeQBX4v_Bmcs_AGYFDbPEREAAZ-L6hA-MPwDUZGURYy5AABn8S53Bwz8AO8BGHgeOQADtHP3F-pE_AADjAmOcAkAA63vNEIdiQAARdR_H-Ns_ABXd9WKlnT8AaG9RB2KJPwCLYBq4Ez1AABqfCHGH9z8ABHR-8uiaPwAA\"}",
    "pinned_comment_count": 3,
    "quick_response_emojis": [
      {
        "unicode": "❤️"
      },
      {
        "unicode": "🙌"
      },
      {
        "unicode": "🔥"
      }
    ],
    "scroll_behavior": 1,
    "disclaimer_text": "addie_ble initially shared this reel to non-followers first on Aug 4, so some comments may be older than the reel's post date.",
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
  "next_page_id": "IntcImNhY2hlZF9jb21tZW50c19jdXJzb3JcIjpcIjE4MTE5MTg0NzIxNDkwNjExXCIsXCJiaWZpbHRlcl90b2tlblwiOlwiR2dZWWVRQlg0dl9CbWNzX0FHWUZEYlBFUkVBQVotTDZoQS1NUHdEVVpHVVJZeTVBQUJuOFM1M0J3ejhBTzhCR0hnZU9RQUR0SFAzRi1wRV9BQURqQW1PY0FrQUE2M3ZORUlkaVFBQVJkUl9ILU5zX0FCWGQ5V0tsblQ4QWFHOVJCMktKUHdDTFlCcTRFejFBQUJxZkNIR0g5ejhBQkhSLTh1aWFQd0FBXCJ9Ig=="
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
      "https://api.hikerapi.com/v2/media/comments/replies?media_id=3864286541032633353&comment_id=18142813870496178"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_comments_replies_v2(media_id="3864286541032633353", comment_id="18142813870496178")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/media/comments/replies",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"media_id": "3864286541032633353", "comment_id": "18142813870496178"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/media/comments/replies?media_id=3864286541032633353&comment_id=18142813870496178",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "child_comment_count": 6,
  "child_comments": [
    {
      "bit_flags": 0,
      "child_comment_index": 0,
      "comment_like_count": 0,
      "content_type": "comment",
      "created_at": 1775154407,
      "created_at_for_fb_app": 1775154407,
      "created_at_utc": 1775154407,
      "did_report_as_spam": false,
      "has_disliked_comment": false,
      "has_liked_comment": false,
      "is_covered": false,
      "is_photo_comments_enabled_for_comment_author": false,
      "is_text_editable": false,
      "is_edited": false,
      "meta_ai_comment_type": "NONE",
      "is_ranked_comment": false,
      "liked_by_media_coauthors": [],
      "media_id": 3864286541032633353,
      "media_info": {
        "media": {
          "can_see_insights_as_brand": false,
          "clips_demotion_control": {
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_icon": "none",
            "confirmation_style": "bottomsheet",
            "confirmation_title": "Post hidden",
            "confirmation_title_style": "large_left",
            "enable_word_wrapping": true,
            "followup_options": [
              {
                "data": "author_id:6752523055",
                "demotion_control": {
                  "confirmation_body": "We won't suggest posts from caldeironuria70.",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_style": "bottomsheet",
                  "undo_style": "inline"
                },
                "id": "dislike_author",
                "show_icon": true,
                "text": "Don't suggest posts from caldeironuria70"
              },
              {
                "id": "hide_all_specific_words",
                "show_icon": true,
                "text": "Don't suggest posts with certain words"
              },
              {
                "id": "control_center",
                "show_icon": true,
                "text": "Manage content preferences"
              }
            ],
            "title": "Not interested",
            "title_style": "normal",
            "undo_style": "top_right"
          },
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
              "best_audio_cluster_id": "916787237656437"
            },
            "audio_type": "original_sounds",
            "branded_content_tag_info": {
              "can_add_tag": false
            },
            "clips_creation_entry_point": "clips",
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
              "mashups_allowed": true,
              "non_privacy_filtered_mashups_media_count": 0
            },
            "music_canonical_id": "18445822114118958",
            "original_sound_info": {
              "allow_creator_to_rename": true,
              "audio_asset_id": "35297598506521672",
              "audio_parts": [],
              "audio_parts_by_filter": [],
              "can_remix_be_shared_to_fb": true,
              "can_remix_be_shared_to_fb_expansion": true,
              "consumption_info": {
                "is_bookmarked": false,
                "is_trending_in_clips": false,
                "should_mute_audio_reason": ""
              },
              "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT52.941498S\" FBManifestTimestamp=\"1775667227\" FBManifestIdentifier=\"FragtJ0NKRaKhvuGlajbBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT52.941498S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1608176020447621a\" bandwidth=\"50570\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"50570\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m78/AQOzSxvuQ30QeJwkWIeEs9HvMrj97CleSfQ1CLqv05TWJ2K9LyEe8MIDZPjt2o9EPUU4kzJvHPJz5950OCNUivvGbjji-bo4k2ccxlM.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=oPrrRjSyUEYQ7kNvwFbM_VW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgyNjUwMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUyLCJiaXRyYXRlIjo1MDc0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2t5TU4xRnz369Rh75DmCk2s7lvlaQVy16CX8Cn-Ay8hQ&amp;oe=69D86352</BaseURL><SegmentBase indexRange=\"824-1179\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
              "duration_in_ms": 52962,
              "hide_remixing": false,
              "ig_artist": {
                "__typename": "XDTUserDict",
                "strong_id__": "6752523055",
                "id": "6752523055",
                "full_name": "Nuria Taboada",
                "is_private": false,
                "is_verified": false,
                "pk": "6752523055",
                "profile_pic_id": "3869835622605851526_6752523055",
                "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=oqAN6glkE8gQ7kNvwFHGDBB&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&oh=00_Af2kGQJEyYuVLL1uF7-lqYNcrhYUhOukmrz-vuKB81k8tA&oe=69DC561A&_nc_sid=10d13b",
                "username": "caldeironuria70"
              },
              "is_audio_automatically_attributed": false,
              "is_eligible_for_audio_effects": true,
              "is_explicit": false,
              "is_original_audio_download_eligible": true,
              "is_reuse_disabled": false,
              "is_xpost_from_fb": false,
              "oa_owner_is_music_artist": false,
              "original_audio_subtype": "default",
              "original_audio_title": "Original audio",
              "original_media_id": "3866597721931422240",
              "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQOnw1GCxnKWkJ_RwdQgCRY47iEmmY4VWBZzBKIqJCEkYxizFx0SbahSsV3IzPjFlY4iMh-VpM62H1nFEQq1Ge2y.mp4?strext=1&_nc_cat=100&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=sMuGsSkc9o0Q7kNvwEZ4fOJ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5MTAzODI2NTAzNjgwMjcsImFzc2V0X2FnZV9kYXlzIjo1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0NNwRBTqDTkE3INXi1TMR0AEr01ZfBdhRMezIJHFycYQ&oe=69DC4EB2",
              "should_mute_audio": false,
              "time_created": 1775154412
            },
            "professional_clips_upsell_type": 0,
            "show_achievements": false
          },
          "coauthor_producer_can_see_organic_insights": false,
          "coauthor_producers": [],
          "comment_inform_treatment": {
            "should_have_inform_treatment": false,
            "text": ""
          },
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "deleted_reason": 0,
          "enable_media_notes_production": true,
          "enable_waist": true,
          "ig_play_count": 83,
          "fundraiser_tag": {},
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "has_delayed_metadata": false,
          "has_more_comments": false,
          "hide_view_all_comment_entrypoint": true,
          "invited_coauthor_producers": [],
          "is_artist_pick": false,
          "is_cutout_sticker_allowed": true,
          "is_in_profile_grid": false,
          "is_organic_product_tagging_eligible": true,
          "is_paid_partnership": false,
          "is_reshare_of_text_post_app_media_in_ig": false,
          "is_reuse_allowed": true,
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "is_unified_video": false,
          "is_visual_reply_commenter_notice_enabled": true,
          "media_notes": {
            "items": []
          },
          "mezql_token": "",
          "owner": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "biography": "Galega de  pura cepa",
            "can_see_quiet_post_attribution": true,
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_restricted": false
            },
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "pk": "6752523055",
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=oqAN6glkE8gQ7kNvwFHGDBB&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&oh=00_Af2kGQJEyYuVLL1uF7-lqYNcrhYUhOukmrz-vuKB81k8tA&oe=69DC561A&_nc_sid=10d13b",
            "show_account_transparency_details": true,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70",
            "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
          },
          "play_count": 83,
          "profile_grid_control_enabled": false,
          "senders": [],
          "share_count_disabled": false,
          "is_social_ufi_disabled": false,
          "sharing_friction_info": {
            "should_have_sharing_friction": false
          },
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "floating_context_items": [],
          "subscribe_cta_visible": false,
          "timeline_pinned_user_ids": [],
          "video_codec": "avc1.64001f",
          "video_sticker_locales": [],
          "view_state_item_type": 128,
          "visual_comment_reply_sticker_info": [
            {
              "end_time_ms": 38677,
              "height": 0.178125,
              "is_fb_sticker": 0,
              "is_hidden": 0,
              "is_pinned": 0,
              "is_sticker": 1,
              "rotation": 0,
              "start_time_ms": 0,
              "vcr_sticker": {
                "can_viewer_link_back_to_original_media_from_vcr": true,
                "end_background_color": "#ffffff",
                "end_time_ms": 38677,
                "original_comment_author": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "46193898922",
                  "id": "46193898922",
                  "full_name": "Natalia Vega Garcia",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "46193898922",
                  "profile_pic_id": "2518281128395959898_46193898922",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/151792571_774741103247720_206392669820779548_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NDcuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=rIwyf_qD2C0Q7kNvwG1H9pi&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GLsrDAlogUB4n8ACABx86SgKQd0CbkULAAAB1501500j-ccb7-5&oh=00_Af3MB5Hy1woUDEi6ccd06y73SAu3W1bejYztP0CdrEDTPQ&oe=69DC6033&_nc_sid=10d13b",
                  "username": "vegagarcianatalia"
                },
                "original_comment_id": "18142813870496178",
                "original_comment_text": "Ya está bien tapar estás palabras: violación y violencia etc",
                "original_media_id": "3864286541032633353",
                "start_background_color": "#ffffff",
                "start_time_ms": 0,
                "text_color": ""
              },
              "width": 0.7222222,
              "x": 0.5,
              "y": 0.29453126,
              "z": 0
            }
          ],
          "visual_replies_info": {
            "can_viewer_link_back_to_original_media_from_vcr": true,
            "comment_info": {
              "comment_id": "18142813870496178",
              "commenter_username": "vegagarcianatalia"
            },
            "original_media": {
              "pk": "3864286541032633353"
            }
          },
          "top_likers": [],
          "__typename": "XDTMediaDict",
          "strong_id__": "3866597721931422240_6752523055",
          "id": "3866597721931422240_6752523055",
          "are_remixes_crosspostable": true,
          "can_viewer_reshare": true,
          "can_viewer_save": true,
          "caption_is_edited": false,
          "code": "DWo6iRZDpog",
          "device_timestamp": 11031814077916,
          "like_count": 0,
          "comment_count": 0,
          "filter_type": 0,
          "has_audio": true,
          "has_high_risk_gen_ai_inform_treatment": false,
          "has_liked": false,
          "has_shared_to_fb": 0,
          "has_views_fetching": true,
          "ig_media_sharing_disabled": false,
          "image_versions2": {
            "additional_candidates": {
              "first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/657368091_949438854160568_8819782369698382914_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=106&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=t2z-rdiHkzQQ7kNvwHjesh_&_nc_oc=Adodlp_UoWyaxa8iIpim9MgLSckRdJBvHfeRC_2TLy5kDN7KT7z8K5gz5A4gKpLB-eU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0pfEfA-WyYYMeb1YeN3ToWaldIlHsmRxQpjIJpT-y-EQ&oe=69DC4F3C",
                "width": 640
              },
              "igtv_first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/657368091_949438854160568_8819782369698382914_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=106&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=t2z-rdiHkzQQ7kNvwHjesh_&_nc_oc=Adodlp_UoWyaxa8iIpim9MgLSckRdJBvHfeRC_2TLy5kDN7KT7z8K5gz5A4gKpLB-eU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0pfEfA-WyYYMeb1YeN3ToWaldIlHsmRxQpjIJpT-y-EQ&oe=69DC4F3C",
                "width": 640
              }
            },
            "candidates": [
              {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/657885435_1990745658185096_1353365794254293831_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=103&ig_cache_key=Mzg2NjU5NzcyMTkzMTQyMjI0MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=qwadgvEIsK4Q7kNvwExkeuR&_nc_oc=AdrZzcwt6pmTkC1w96kbs7NIjFqCBj2kqzJ90O9CNww4RzcVdZiIDXLojsTyrO-KkAM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af3KkCoKKA_--BMq4iAK__qQofNt0c0bgYWjFrOPjnGHFw&oe=69DC7160",
                "width": 640
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 598,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_width": 1500,
                "thumbnail_duration": 0.5044,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 52.962
              }
            }
          },
          "is_comments_gif_composer_enabled": true,
          "is_dash_eligible": 1,
          "is_post_live_clips_media": false,
          "is_quiet_post": false,
          "is_third_party_downloads_eligible": true,
          "like_and_view_counts_disabled": false,
          "media_type": 2,
          "number_of_qualities": 2,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQTlTVGJjaXF6SGNnYXdVU3FMWFkzTnIzODY2NTk3NzIxOTMxNDIyMjQwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2NzIyNzQ2M3wzODY2NTk3NzIxOTMxNDIyMjQwfDY3NTI1MjMwNTV8MGU2NDMwNGYxNzAyMjI2NjZjY2I0MjhkYThkMWNlZTA4ZDgyZGQzNTdiOTkxMWMxMTJhNDZkN2NmMmUzMDc1ZCJ9LCJzaWduYXR1cmUiOiIifQ==",
          "original_height": 1280,
          "original_media_has_visual_reply_media": false,
          "original_width": 720,
          "product_type": "clips",
          "taken_at": 1775154422,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_restricted": false,
              "outgoing_request": false
            },
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_facebook_onboarded_charity": false,
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "merchant_checkout_style": "none",
            "pk": 6752523055,
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=E_ajg83nLc4Q7kNvwGyZyDc&_nc_oc=AdoL30aqQvXaK84Z-JA7zJkYuwPAaFX60_8jXZKVL6Cmp9d6teapeR7jP_yCwSlwot8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0qjDjO1ASpPmGjwl2h6Os-RWmQxKc4IdOC_JhCt6iNiQ&oe=69DC561A",
            "seller_shoppable_feed_type": "none",
            "show_account_transparency_details": true,
            "show_shoppable_feed": false,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70"
          },
          "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT52.941498S\" FBManifestTimestamp=\"1775667227\" FBManifestIdentifier=\"FragtJ0NGBBpZ19kYXNoX2Jhc2VsaW5lGVa0hOrPrYmUA7CIxfu2/rEDwLH07KeSuQOEhMeWvP/mBoCk2baQ56YHIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFaGVhdnkAFgoUABIUAAA=\"><Period id=\"0\" duration=\"PT52.941498S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:73.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1915340152430850v\" bandwidth=\"645088\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"4251131\" FBPlaybackResolutionMos=\"0:100,360:94.6,480:93.4,720:89.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.18,480:97.6,720:96.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMgLuEBJEpBga3s-KKzDFmyoJ2xDQQCAsppRxltQExQFGz2A2H3tvtjY_jCgP6Zkv-7XsUzkVMTu8JrD3GS-DxW1RxYLl_zk_r1zBU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=J1aUCXkQ7EYQ7kNvwHMvfjI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkxMDM4MjY1MDM2ODAyNywiYXNzZXRfYWdlX2RheXMiOjUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1MiwiYml0cmF0ZSI6NjQ1MDg4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0hTiDyZvp89pIPfWC7HWTeoYS1k-awwDaMV4SliaX1mA&amp;oe=69D85887</BaseURL><SegmentBase indexRange=\"892-1055\" timescale=\"12800\" FBMinimumPrefetchRange=\"1056-46930\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1056-175572\" FBFirstSegmentRange=\"1056-290404\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"290405-591165\" FBPrefetchSegmentRange=\"1056-290404\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-891\"/></SegmentBase></Representation><Representation id=\"970083842034784v\" bandwidth=\"172414\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"1136209\" FBPlaybackResolutionMos=\"0:100,360:73.7,480:67.4,720:57.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.2,480:82.3,720:72.5\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"12800/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPUAibA_lftXq4rBriWbz3K9gEMHAdSKV5VQMv5vySMF8g22DVk5rVUszHPhHcEDTY49BfKxm-W9t0S3fLMrCL-5Oauuut1jBtKre0.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=fwr1BMTfdCIQ7kNvwEXLblJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkxMDM4MjY1MDM2ODAyNywiYXNzZXRfYWdlX2RheXMiOjUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1MiwiYml0cmF0ZSI6MTcyNDE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1MhLf-1X1rlVaUlbbNruheQueQXUeVLQVriHuPBFx80A&amp;oe=69D88241</BaseURL><SegmentBase indexRange=\"888-1051\" timescale=\"12800\" FBMinimumPrefetchRange=\"1052-16821\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1052-46774\" FBFirstSegmentRange=\"1052-75395\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"75396-160969\" FBPrefetchSegmentRange=\"1052-75395\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-887\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2055659452049664a\" bandwidth=\"39059\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"39059\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"259476\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPrestU3bdBz5JE1Hvwa9AvjOq-JL28QR1wDWVAlfCAyaK53VY2UNaSlTWOU1Ls-z-y8A0KWoTbONVPl26ECMZew2C-7WpWIqYJPno.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=J_g--BmTxVkQ7kNvwF4YISp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgyNjUwMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUyLCJiaXRyYXRlIjozOTIwOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2l_TGuqyjd8gex8N9RgrUm_0pon6IldHugTZ5E5PFNrQ&amp;oe=69DC5397</BaseURL><SegmentBase indexRange=\"837-1000\" timescale=\"44100\" FBMinimumPrefetchRange=\"1001-1699\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1001-14309\" FBFirstSegmentRange=\"1001-25517\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"25518-51526\" FBPrefetchSegmentRange=\"1001-25517\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"954349110469144a\" bandwidth=\"75473\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"75473\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"500454\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQM4urTjuuqOHnyufeNlJrYtxkV4HYlDSrv8BZNuo95N5e2EMiIkInxBNWStamAOM33FQyHkwgbPQpnpuYHJJ6mMuIe2OKsNu-9X28w.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=lKhJLjn7-WUQ7kNvwGWPyDm&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgyNjUwMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUyLCJiaXRyYXRlIjo3NTYyMywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2T4tGr9wNjLVUeaybBE-OJ8ahxvpzpTtszhmP0-jcVuQ&amp;oe=69DC6C57</BaseURL><SegmentBase indexRange=\"838-1001\" timescale=\"44100\" FBMinimumPrefetchRange=\"1002-1731\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-25394\" FBFirstSegmentRange=\"1002-48734\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"48735-94486\" FBPrefetchSegmentRange=\"1002-48734\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"888566137569562a\" bandwidth=\"96098\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"96098\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"636938\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMTziR9CF-TTf5KJvj0NqAjujG33Fy7PBdkokfZEGp0Xt_uY4Uwy5Yl4Pl6RLFRBlg7-9ScV9yDmS4b2c0CrIyAGr-TqrmMLdK9-tY.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=k01dee9qCEAQ7kNvwHmJmK0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgyNjUwMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUyLCJiaXRyYXRlIjo5NjI0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af07yPsioC3jYvG-C17u5HDBAIwrMuk0jhFYnMhqH0BZnw&amp;oe=69DC6E97</BaseURL><SegmentBase indexRange=\"833-996\" timescale=\"44100\" FBMinimumPrefetchRange=\"997-2050\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"997-31150\" FBFirstSegmentRange=\"997-61655\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"61656-116336\" FBPrefetchSegmentRange=\"997-61655\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "video_subtitles_locale": "es_CL",
          "__is_XDTMediaDict": true
        }
      },
      "parent_comment_id": "18142813870496178",
      "pk": "18061290119485558",
      "private_reply_status": 0,
      "replied_to_comment_id": "18142813870496178",
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "18061290119485558",
      "text": "@vegagarcianatalia",
      "type": 2,
      "user": {
        "fbid_v2": 17841406811654065,
        "full_name": "Nuria Taboada",
        "id": "6752523055",
        "is_mentionable": true,
        "is_private": false,
        "is_verified": false,
        "pk": 6752523055,
        "pk_id": "6752523055",
        "profile_pic_id": "3869835622605851526_6752523055",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=E_ajg83nLc4Q7kNvwGyZyDc&_nc_oc=AdoL30aqQvXaK84Z-JA7zJkYuwPAaFX60_8jXZKVL6Cmp9d6teapeR7jP_yCwSlwot8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0qjDjO1ASpPmGjwl2h6Os-RWmQxKc4IdOC_JhCt6iNiQ&oe=69DC561A",
        "strong_id__": "6752523055",
        "username": "caldeironuria70"
      },
      "user_id": 6752523055
    },
    {
      "bit_flags": 0,
      "child_comment_index": 1,
      "comment_like_count": 0,
      "content_type": "comment",
      "created_at": 1775154575,
      "created_at_for_fb_app": 1775154575,
      "created_at_utc": 1775154575,
      "did_report_as_spam": false,
      "has_disliked_comment": false,
      "has_liked_comment": false,
      "is_covered": false,
      "is_photo_comments_enabled_for_comment_author": false,
      "is_text_editable": false,
      "is_edited": false,
      "meta_ai_comment_type": "NONE",
      "is_ranked_comment": false,
      "liked_by_media_coauthors": [],
      "media_id": 3864286541032633353,
      "media_info": {
        "media": {
          "can_see_insights_as_brand": false,
          "clips_demotion_control": {
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_icon": "none",
            "confirmation_style": "bottomsheet",
            "confirmation_title": "Post hidden",
            "confirmation_title_style": "large_left",
            "enable_word_wrapping": true,
            "followup_options": [
              {
                "data": "author_id:6752523055",
                "demotion_control": {
                  "confirmation_body": "We won't suggest posts from caldeironuria70.",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_style": "bottomsheet",
                  "undo_style": "inline"
                },
                "id": "dislike_author",
                "show_icon": true,
                "text": "Don't suggest posts from caldeironuria70"
              },
              {
                "id": "hide_all_specific_words",
                "show_icon": true,
                "text": "Don't suggest posts with certain words"
              },
              {
                "id": "control_center",
                "show_icon": true,
                "text": "Manage content preferences"
              }
            ],
            "title": "Not interested",
            "title_style": "normal",
            "undo_style": "top_right"
          },
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
              "best_audio_cluster_id": "1483890799854250"
            },
            "audio_type": "original_sounds",
            "branded_content_tag_info": {
              "can_add_tag": false
            },
            "clips_creation_entry_point": "clips",
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
              "mashups_allowed": true,
              "non_privacy_filtered_mashups_media_count": 0
            },
            "music_canonical_id": "18543629686067165",
            "original_sound_info": {
              "allow_creator_to_rename": true,
              "audio_asset_id": "26439092105750123",
              "audio_parts": [],
              "audio_parts_by_filter": [],
              "can_remix_be_shared_to_fb": true,
              "can_remix_be_shared_to_fb_expansion": true,
              "consumption_info": {
                "is_bookmarked": false,
                "is_trending_in_clips": false,
                "should_mute_audio_reason": ""
              },
              "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT38.916645S\" FBManifestTimestamp=\"1775667227\" FBManifestIdentifier=\"FragtJ0NKRa60aWpwq7aDCIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT38.916645S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"3576410989179997a\" bandwidth=\"49533\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"49533\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m78/AQMHZhT-Wvz1hVn_VCe-NxYw9ktsNE2eORKlJZ3oO537GqkjHe-Bh4wTLcC7m4mx5POWxXmm9Xv989t6LGZgJh4ZuBZLLGNfPNPApd4.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=qEoq-CtZLD0Q7kNvwGWOqUI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMDUyMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM4LCJiaXRyYXRlIjo0OTc1OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0TJKzB06LjW7nF_Y1jptO4k7iIydBvaA4vriTnSdHY6g&amp;oe=69D8511A</BaseURL><SegmentBase indexRange=\"824-1095\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
              "duration_in_ms": 38932,
              "hide_remixing": false,
              "ig_artist": {
                "__typename": "XDTUserDict",
                "strong_id__": "6752523055",
                "id": "6752523055",
                "full_name": "Nuria Taboada",
                "is_private": false,
                "is_verified": false,
                "pk": "6752523055",
                "profile_pic_id": "3869835622605851526_6752523055",
                "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=oqAN6glkE8gQ7kNvwFHGDBB&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&oh=00_Af2kGQJEyYuVLL1uF7-lqYNcrhYUhOukmrz-vuKB81k8tA&oe=69DC561A&_nc_sid=10d13b",
                "username": "caldeironuria70"
              },
              "is_audio_automatically_attributed": false,
              "is_eligible_for_audio_effects": true,
              "is_explicit": false,
              "is_original_audio_download_eligible": true,
              "is_reuse_disabled": false,
              "is_xpost_from_fb": false,
              "oa_owner_is_music_artist": false,
              "original_audio_subtype": "default",
              "original_audio_title": "Original audio",
              "original_media_id": "3866599194518014185",
              "progressive_download_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m69/AQOMSrJPUufYAl52jmI4biJmiw1PkQFLyhdYQP0tDl3E57LY2SDFWleGP4dp7XzBIwGiVWCTSPGGkdWjYWC0xx9f.mp4?strext=1&_nc_cat=105&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=gkZJTS92GlAQ7kNvwHacxl-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5MTAzODMwNTIzNjgwMjcsImFzc2V0X2FnZV9kYXlzIjo1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0EgMPzBJfbBInJCA_TDv6bGMfQRZ-CriELghh4X7_I6A&oe=69DC4F09",
              "should_mute_audio": false,
              "time_created": 1775154579
            },
            "professional_clips_upsell_type": 0,
            "show_achievements": false
          },
          "coauthor_producer_can_see_organic_insights": false,
          "coauthor_producers": [],
          "comment_inform_treatment": {
            "should_have_inform_treatment": false,
            "text": ""
          },
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "deleted_reason": 0,
          "enable_media_notes_production": true,
          "enable_waist": true,
          "ig_play_count": 148,
          "fundraiser_tag": {},
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "has_delayed_metadata": false,
          "has_more_comments": false,
          "hide_view_all_comment_entrypoint": true,
          "invited_coauthor_producers": [],
          "is_artist_pick": false,
          "is_cutout_sticker_allowed": true,
          "is_in_profile_grid": false,
          "is_organic_product_tagging_eligible": true,
          "is_paid_partnership": false,
          "is_reshare_of_text_post_app_media_in_ig": false,
          "is_reuse_allowed": true,
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "is_unified_video": false,
          "is_visual_reply_commenter_notice_enabled": true,
          "media_notes": {
            "items": []
          },
          "mezql_token": "",
          "owner": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "biography": "Galega de  pura cepa",
            "can_see_quiet_post_attribution": true,
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_restricted": false
            },
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "pk": "6752523055",
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=oqAN6glkE8gQ7kNvwFHGDBB&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&oh=00_Af2kGQJEyYuVLL1uF7-lqYNcrhYUhOukmrz-vuKB81k8tA&oe=69DC561A&_nc_sid=10d13b",
            "show_account_transparency_details": true,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70",
            "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
          },
          "play_count": 148,
          "profile_grid_control_enabled": false,
          "senders": [],
          "share_count_disabled": false,
          "is_social_ufi_disabled": false,
          "sharing_friction_info": {
            "should_have_sharing_friction": false
          },
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "floating_context_items": [],
          "subscribe_cta_visible": false,
          "timeline_pinned_user_ids": [],
          "video_codec": "avc1.64001f",
          "video_sticker_locales": [],
          "view_state_item_type": 128,
          "visual_comment_reply_sticker_info": [
            {
              "end_time_ms": 38886,
              "height": 0.178125,
              "is_fb_sticker": 0,
              "is_hidden": 0,
              "is_pinned": 0,
              "is_sticker": 1,
              "rotation": 0,
              "start_time_ms": 0,
              "vcr_sticker": {
                "can_viewer_link_back_to_original_media_from_vcr": true,
                "end_background_color": "#ffffff",
                "end_time_ms": 38886,
                "original_comment_author": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "46193898922",
                  "id": "46193898922",
                  "full_name": "Natalia Vega Garcia",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "46193898922",
                  "profile_pic_id": "2518281128395959898_46193898922",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/151792571_774741103247720_206392669820779548_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NDcuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=rIwyf_qD2C0Q7kNvwG1H9pi&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GLsrDAlogUB4n8ACABx86SgKQd0CbkULAAAB1501500j-ccb7-5&oh=00_Af3MB5Hy1woUDEi6ccd06y73SAu3W1bejYztP0CdrEDTPQ&oe=69DC6033&_nc_sid=10d13b",
                  "username": "vegagarcianatalia"
                },
                "original_comment_id": "18142813870496178",
                "original_comment_text": "Ya está bien tapar estás palabras: violación y violencia etc",
                "original_media_id": "3864286541032633353",
                "start_background_color": "#ffffff",
                "start_time_ms": 0,
                "text_color": ""
              },
              "width": 0.7222222,
              "x": 0.5,
              "y": 0.29453126,
              "z": 0
            }
          ],
          "visual_replies_info": {
            "can_viewer_link_back_to_original_media_from_vcr": true,
            "comment_info": {
              "comment_id": "18142813870496178",
              "commenter_username": "vegagarcianatalia"
            },
            "original_media": {
              "pk": "3864286541032633353"
            }
          },
          "top_likers": [],
          "__typename": "XDTMediaDict",
          "strong_id__": "3866599194518014185_6752523055",
          "id": "3866599194518014185_6752523055",
          "are_remixes_crosspostable": true,
          "can_viewer_reshare": true,
          "can_viewer_save": true,
          "caption_is_edited": false,
          "code": "DWo63s2Dsjp",
          "device_timestamp": 11217188893707,
          "like_count": 0,
          "comment_count": 0,
          "filter_type": 0,
          "has_audio": true,
          "has_high_risk_gen_ai_inform_treatment": false,
          "has_liked": false,
          "has_shared_to_fb": 0,
          "has_views_fetching": true,
          "ig_media_sharing_disabled": false,
          "image_versions2": {
            "additional_candidates": {
              "first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/658926857_1553712959754602_1699263508747240128_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=103&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bYm-GCEN2SwQ7kNvwFqIJIE&_nc_oc=AdrY0yklEZoeZjT5yJfR6x8qwhDuXjm-0H_VYhByuR7LXwXdOj6Hxmmv79lW507Auqg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0wOOIt5ycH6INEAM8I6zDnvl5S5L06Q_RHeSyOeADBgA&oe=69DC43BA",
                "width": 640
              },
              "igtv_first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/658926857_1553712959754602_1699263508747240128_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=103&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bYm-GCEN2SwQ7kNvwFqIJIE&_nc_oc=AdrY0yklEZoeZjT5yJfR6x8qwhDuXjm-0H_VYhByuR7LXwXdOj6Hxmmv79lW507Auqg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0wOOIt5ycH6INEAM8I6zDnvl5S5L06Q_RHeSyOeADBgA&oe=69DC43BA",
                "width": 640
              }
            },
            "candidates": [
              {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/658728478_1254675350128035_7953608433408713088_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=100&ig_cache_key=Mzg2NjU5OTE5NDUxODAxNDE4NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Wm-t3l7AjqQQ7kNvwHU0WNn&_nc_oc=AdrgsItx8ibjhw6e8nJFTtWEmmvblLxxe3bPdJnPbBiKcvS2q5Ikzq502ota1g5DnbM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af39MXJCA9m4RMnGGyK-wi35hxpLDjS0Jh9kwlqveLcUKw&oe=69DC43D9",
                "width": 640
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 583,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_width": 1500,
                "thumbnail_duration": 0.37078095238095,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 38.932
              }
            }
          },
          "is_comments_gif_composer_enabled": true,
          "is_dash_eligible": 1,
          "is_post_live_clips_media": false,
          "is_quiet_post": false,
          "is_third_party_downloads_eligible": true,
          "like_and_view_counts_disabled": false,
          "media_type": 2,
          "number_of_qualities": 2,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQTlTVGJjaXF6SGNnYXdVU3FMWFkzTnIzODY2NTk5MTk0NTE4MDE0MTg1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2NzIyNzQ2MHwzODY2NTk5MTk0NTE4MDE0MTg1fDY3NTI1MjMwNTV8YTM5ZTc3Yzk5NmJiODg4ODc1ZDNiZjQxOTQ3ZGVkNmFmZjkxOTc0MWRlNjJkMmVmYzZkOTJhNGRlMzkxM2YyMyJ9LCJzaWduYXR1cmUiOiIifQ==",
          "original_height": 1280,
          "original_media_has_visual_reply_media": false,
          "original_width": 720,
          "product_type": "clips",
          "taken_at": 1775154589,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_restricted": false,
              "outgoing_request": false
            },
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_facebook_onboarded_charity": false,
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "merchant_checkout_style": "none",
            "pk": 6752523055,
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=E_ajg83nLc4Q7kNvwGyZyDc&_nc_oc=AdoL30aqQvXaK84Z-JA7zJkYuwPAaFX60_8jXZKVL6Cmp9d6teapeR7jP_yCwSlwot8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0qjDjO1ASpPmGjwl2h6Os-RWmQxKc4IdOC_JhCt6iNiQ&oe=69DC561A",
            "seller_shoppable_feed_type": "none",
            "show_account_transparency_details": true,
            "show_shoppable_feed": false,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70"
          },
          "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT38.916645S\" FBManifestTimestamp=\"1775667227\" FBManifestIdentifier=\"FragtJ0NGBBpZ19kYXNoX2Jhc2VsaW5lGVbgu4SRl6imA+z26+WYvZIE/KaukJW+rAWwi/vPzILzBfqK6Ivvg6YGIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFaGVhdnkAFgoUABIUAAA=\"><Period id=\"0\" duration=\"PT38.916645S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:72.6\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"928678113480432v\" bandwidth=\"726385\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"3492705\" FBPlaybackResolutionMos=\"0:100,360:97.9,480:97.3,720:96\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.516,480:99.349,720:98.81\" FBAbrPolicyTags=\"avoid_on_cellular\" width=\"720\" height=\"1280\" frameRate=\"15360/1024\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQNyqxPyRt-mS0SbP4oV-zyqvVIXJqKjWM2IkoqKogSK3yLLqEgZMOkpCGCPioHUTA9qN6u6oMo-AIRBTSc1-O4ArDzyAWe2BK-pIlM.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=tdZwGvhBHD8Q7kNvwEShPwq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkxMDM4MzA1MjM2ODAyNywiYXNzZXRfYWdlX2RheXMiOjUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOCwiYml0cmF0ZSI6NzI2Mzg1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3NA6Wm0JrlT2Ya1eBzLV7jWxCzkvJPfF9mNRj8RQWVgw&amp;oe=69D85CC8</BaseURL><SegmentBase indexRange=\"892-1019\" timescale=\"15360\" FBMinimumPrefetchRange=\"1020-35775\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1020-223372\" FBFirstSegmentRange=\"1020-425813\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"425814-912294\" FBPrefetchSegmentRange=\"1020-425813\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-891\"/></SegmentBase></Representation><Representation id=\"1660307202073304v\" bandwidth=\"185343\" codecs=\"avc1.4d0016\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"891193\" FBPlaybackResolutionMos=\"0:100,360:77.7,480:71.4,720:59.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.9,480:86,720:75\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/1024\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPS_2PtTqUU8FMc_83rimYvcwUOPX6WwS5NgwbYJSQIdh8dnUlRCEOltnUYLITAlg4oOiq7YK_ARTVFWSlPcsFineAgcu-8mYbuqXA.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=OEQgbAB2jKYQ7kNvwE5VWyk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkxMDM4MzA1MjM2ODAyNywiYXNzZXRfYWdlX2RheXMiOjUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOCwiYml0cmF0ZSI6MTg1MzQzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af31fqDdhpSCcRSGPFRoUDioqYmttYLT5qK34aolEuwSSQ&amp;oe=69D870A1</BaseURL><SegmentBase indexRange=\"888-1015\" timescale=\"15360\" FBMinimumPrefetchRange=\"1016-11791\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1016-57365\" FBFirstSegmentRange=\"1016-109211\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"109212-236463\" FBPrefetchSegmentRange=\"1016-109211\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-887\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1772479194137277a\" bandwidth=\"34752\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"34752\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"170016\" FBPaqMos=\"92.65\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPEWSvZ1GVgXkIAfhbJqkwdBETIwIlmVsdmOh0wohncmce7NmOZnZ_GH8gFsQcPjaEHhxQ9gEGboo79XgtZ2B0UYBq0tYl6i8qC7ac.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=VxOqIYW1GyUQ7kNvwH4uG7u&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMDUyMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM4LCJiaXRyYXRlIjozNDk0OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af02F6HzW7XH2Yph3FAb3PYwKTaQa9Avisk3meD89rw-pA&amp;oe=69DC4626</BaseURL><SegmentBase indexRange=\"837-964\" timescale=\"44100\" FBMinimumPrefetchRange=\"965-1663\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"965-12817\" FBFirstSegmentRange=\"965-24407\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"24408-48782\" FBPrefetchSegmentRange=\"965-24407\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1505199894415806a\" bandwidth=\"71108\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71108\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"346873\" FBPaqMos=\"93.10\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMeFXWBAmIt8X6jdP1m2PL-EuY1SsWYSmKldKF8UwthGlkkr-Vb1Pt4Jru8-K0MR80aFye0fFnWjVqxh4BPm6SGsZx5xby0iZGixtQ.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=t32lCDRvfNIQ7kNvwG76_n-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMDUyMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM4LCJiaXRyYXRlIjo3MTMwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Niht5TkF_3TByRXR4KFpCK2mUfjMyoy-ndxo04umIvA&amp;oe=69DC4313</BaseURL><SegmentBase indexRange=\"838-965\" timescale=\"44100\" FBMinimumPrefetchRange=\"966-1695\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-23852\" FBFirstSegmentRange=\"966-46733\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"46734-98664\" FBPrefetchSegmentRange=\"966-46733\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1166533625478582a\" bandwidth=\"93311\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"93311\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"454878\" FBPaqMos=\"94.46\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMu6fk7b1ikRiHfizbFjsl2SCJkr5mhQkkWCsYo1dCQ7ggL2sdp6kxsvdii-OzrgDgVIsPMqMqspidap5tDHwH4pB1HJdTgdC-EaoM.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=b6cEqDqTjc0Q7kNvwEZprQE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMDUyMzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM4LCJiaXRyYXRlIjo5MzUwOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af31aSRHRI8BDKwZcaADuZ4PbbPsn4boip6jar0vr1b8dA&amp;oe=69DC4FEA</BaseURL><SegmentBase indexRange=\"833-960\" timescale=\"44100\" FBMinimumPrefetchRange=\"961-2014\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-31528\" FBFirstSegmentRange=\"961-61709\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"61710-129129\" FBPrefetchSegmentRange=\"961-61709\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "video_subtitles_locale": "es_CL",
          "__is_XDTMediaDict": true
        }
      },
      "parent_comment_id": "18142813870496178",
      "pk": "18121513129619994",
      "private_reply_status": 0,
      "replied_to_comment_id": "18142813870496178",
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "18121513129619994",
      "text": "@vegagarcianatalia",
      "type": 2,
      "user": {
        "fbid_v2": 17841406811654065,
        "full_name": "Nuria Taboada",
        "id": "6752523055",
        "is_mentionable": true,
        "is_private": false,
        "is_verified": false,
        "pk": 6752523055,
        "pk_id": "6752523055",
        "profile_pic_id": "3869835622605851526_6752523055",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=E_ajg83nLc4Q7kNvwGyZyDc&_nc_oc=AdoL30aqQvXaK84Z-JA7zJkYuwPAaFX60_8jXZKVL6Cmp9d6teapeR7jP_yCwSlwot8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0qjDjO1ASpPmGjwl2h6Os-RWmQxKc4IdOC_JhCt6iNiQ&oe=69DC561A",
        "strong_id__": "6752523055",
        "username": "caldeironuria70"
      },
      "user_id": 6752523055
    },
    {
      "bit_flags": 0,
      "child_comment_index": 2,
      "comment_like_count": 0,
      "content_type": "comment",
      "created_at": 1775154735,
      "created_at_for_fb_app": 1775154735,
      "created_at_utc": 1775154735,
      "did_report_as_spam": false,
      "has_disliked_comment": false,
      "has_liked_comment": false,
      "is_covered": false,
      "is_photo_comments_enabled_for_comment_author": false,
      "is_text_editable": false,
      "is_edited": false,
      "meta_ai_comment_type": "NONE",
      "is_ranked_comment": false,
      "liked_by_media_coauthors": [],
      "media_id": 3864286541032633353,
      "media_info": {
        "media": {
          "can_see_insights_as_brand": false,
          "clips_demotion_control": {
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_icon": "none",
            "confirmation_style": "bottomsheet",
            "confirmation_title": "Post hidden",
            "confirmation_title_style": "large_left",
            "enable_word_wrapping": true,
            "followup_options": [
              {
                "data": "author_id:6752523055",
                "demotion_control": {
                  "confirmation_body": "We won't suggest posts from caldeironuria70.",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_style": "bottomsheet",
                  "undo_style": "inline"
                },
                "id": "dislike_author",
                "show_icon": true,
                "text": "Don't suggest posts from caldeironuria70"
              },
              {
                "id": "hide_all_specific_words",
                "show_icon": true,
                "text": "Don't suggest posts with certain words"
              },
              {
                "id": "control_center",
                "show_icon": true,
                "text": "Manage content preferences"
              }
            ],
            "title": "Not interested",
            "title_style": "normal",
            "undo_style": "top_right"
          },
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
              "best_audio_cluster_id": "831662125913235"
            },
            "audio_type": "original_sounds",
            "branded_content_tag_info": {
              "can_add_tag": false
            },
            "clips_creation_entry_point": "clips",
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
              "mashups_allowed": true,
              "non_privacy_filtered_mashups_media_count": 0
            },
            "music_canonical_id": "18574290643035211",
            "original_sound_info": {
              "allow_creator_to_rename": true,
              "audio_asset_id": "26840280762231828",
              "audio_parts": [],
              "audio_parts_by_filter": [],
              "can_remix_be_shared_to_fb": true,
              "can_remix_be_shared_to_fb_expansion": true,
              "consumption_info": {
                "is_bookmarked": false,
                "is_trending_in_clips": false,
                "should_mute_audio_reason": ""
              },
              "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT53.127254S\" FBManifestTimestamp=\"1775667227\" FBManifestIdentifier=\"FragtJ0NKRb+3+fS04i9AyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT53.127254S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"978714014578687a\" bandwidth=\"73654\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"73654\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m78/AQMSR65jwIBtptYn0B0SZbrnv0MQqggvUirRW435ZwEMbJlf5Gh-xjzmJNcxFUSw9IVsjgdyyttMQtJalRKCa3_UmqYmMNCkEzN2lLU.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=1D5DR4XnXa8Q7kNvwG4muyL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMzU1MzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUzLCJiaXRyYXRlIjo3MzgzMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af26H1BGtzkEmFsDlFPON7O80cy13wg1pr88GUUgTZl21w&amp;oe=69D859C4</BaseURL><SegmentBase indexRange=\"824-1179\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
              "duration_in_ms": 53148,
              "hide_remixing": false,
              "ig_artist": {
                "__typename": "XDTUserDict",
                "strong_id__": "6752523055",
                "id": "6752523055",
                "full_name": "Nuria Taboada",
                "is_private": false,
                "is_verified": false,
                "pk": "6752523055",
                "profile_pic_id": "3869835622605851526_6752523055",
                "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=oqAN6glkE8gQ7kNvwFHGDBB&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&oh=00_Af2kGQJEyYuVLL1uF7-lqYNcrhYUhOukmrz-vuKB81k8tA&oe=69DC561A&_nc_sid=10d13b",
                "username": "caldeironuria70"
              },
              "is_audio_automatically_attributed": false,
              "is_eligible_for_audio_effects": true,
              "is_explicit": false,
              "is_original_audio_download_eligible": true,
              "is_reuse_disabled": false,
              "is_xpost_from_fb": false,
              "oa_owner_is_music_artist": false,
              "original_audio_subtype": "default",
              "original_audio_title": "Original audio",
              "original_media_id": "3866600359091686055",
              "progressive_download_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m69/AQOY_AJNjpdwlplPgrkF3feXHNk18LS7ikJbzSe3Jmg3oqOgQY0gAAQoqt5Z0W4FZANpXokdQIdKB2OdJhwNCa9s.mp4?strext=1&_nc_cat=109&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=sBvSLuvPdvwQ7kNvwE4nmAY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5MTAzODMzNTUzNjgwMjcsImFzc2V0X2FnZV9kYXlzIjo1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0R20DLkUPdST5ZcQq2GM_eGWZG2pOMQnqJPhO_XJ2NSw&oe=69DC4E8D",
              "should_mute_audio": false,
              "time_created": 1775154741
            },
            "professional_clips_upsell_type": 0,
            "show_achievements": false
          },
          "coauthor_producer_can_see_organic_insights": false,
          "coauthor_producers": [],
          "comment_inform_treatment": {
            "should_have_inform_treatment": false,
            "text": ""
          },
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "deleted_reason": 0,
          "enable_media_notes_production": true,
          "enable_waist": true,
          "ig_play_count": 17,
          "fundraiser_tag": {},
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "has_delayed_metadata": false,
          "has_more_comments": false,
          "hide_view_all_comment_entrypoint": true,
          "invited_coauthor_producers": [],
          "is_artist_pick": false,
          "is_cutout_sticker_allowed": true,
          "is_in_profile_grid": false,
          "is_organic_product_tagging_eligible": true,
          "is_paid_partnership": false,
          "is_reshare_of_text_post_app_media_in_ig": false,
          "is_reuse_allowed": true,
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "is_unified_video": false,
          "is_visual_reply_commenter_notice_enabled": true,
          "media_notes": {
            "items": []
          },
          "mezql_token": "",
          "owner": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "biography": "Galega de  pura cepa",
            "can_see_quiet_post_attribution": true,
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_restricted": false
            },
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "pk": "6752523055",
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=oqAN6glkE8gQ7kNvwFHGDBB&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&oh=00_Af2kGQJEyYuVLL1uF7-lqYNcrhYUhOukmrz-vuKB81k8tA&oe=69DC561A&_nc_sid=10d13b",
            "show_account_transparency_details": true,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70",
            "views_on_grid_status": "SHOW_VIEWS_ON_GRID"
          },
          "play_count": 17,
          "profile_grid_control_enabled": false,
          "senders": [],
          "share_count_disabled": false,
          "is_social_ufi_disabled": false,
          "sharing_friction_info": {
            "should_have_sharing_friction": false
          },
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "floating_context_items": [],
          "subscribe_cta_visible": false,
          "timeline_pinned_user_ids": [],
          "video_codec": "avc1.64001f",
          "video_sticker_locales": [],
          "view_state_item_type": 128,
          "visual_comment_reply_sticker_info": [
            {
              "end_time_ms": 38677,
              "height": 0.178125,
              "is_fb_sticker": 0,
              "is_hidden": 0,
              "is_pinned": 0,
              "is_sticker": 1,
              "rotation": 0,
              "start_time_ms": 0,
              "vcr_sticker": {
                "can_viewer_link_back_to_original_media_from_vcr": true,
                "end_background_color": "#ffffff",
                "end_time_ms": 38677,
                "original_comment_author": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "46193898922",
                  "id": "46193898922",
                  "full_name": "Natalia Vega Garcia",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "46193898922",
                  "profile_pic_id": "2518281128395959898_46193898922",
                  "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/151792571_774741103247720_206392669820779548_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NDcuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEmn-meajteRx6YCXIUeitthiuqY5L1vOXBpOyUVjs8Z8oary9zePRI829t8X3NGjc&_nc_ohc=rIwyf_qD2C0Q7kNvwG1H9pi&_nc_gid=l57lw0MqR621IRoUPY9vpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=GLsrDAlogUB4n8ACABx86SgKQd0CbkULAAAB1501500j-ccb7-5&oh=00_Af3MB5Hy1woUDEi6ccd06y73SAu3W1bejYztP0CdrEDTPQ&oe=69DC6033&_nc_sid=10d13b",
                  "username": "vegagarcianatalia"
                },
                "original_comment_id": "18142813870496178",
                "original_comment_text": "Ya está bien tapar estás palabras: violación y violencia etc",
                "original_media_id": "3864286541032633353",
                "start_background_color": "#ffffff",
                "start_time_ms": 0,
                "text_color": ""
              },
              "width": 0.7222222,
              "x": 0.5,
              "y": 0.29453126,
              "z": 0
            }
          ],
          "visual_replies_info": {
            "can_viewer_link_back_to_original_media_from_vcr": true,
            "comment_info": {
              "comment_id": "18142813870496178",
              "commenter_username": "vegagarcianatalia"
            },
            "original_media": {
              "pk": "3864286541032633353"
            }
          },
          "top_likers": [],
          "__typename": "XDTMediaDict",
          "strong_id__": "3866600359091686055_6752523055",
          "id": "3866600359091686055_6752523055",
          "are_remixes_crosspostable": true,
          "can_viewer_reshare": true,
          "can_viewer_save": true,
          "caption_is_edited": false,
          "code": "DWo7IpcDsqn",
          "device_timestamp": 11341063266541,
          "like_count": 0,
          "comment_count": 0,
          "filter_type": 0,
          "has_audio": true,
          "has_high_risk_gen_ai_inform_treatment": false,
          "has_liked": false,
          "has_shared_to_fb": 0,
          "has_views_fetching": true,
          "ig_media_sharing_disabled": false,
          "image_versions2": {
            "additional_candidates": {
              "first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/657890705_2285271555294595_6835517889432916428_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=em59qG2Nc5sQ7kNvwGXSrdp&_nc_oc=Adrlw4eZxd4QVyyYtH1flVqnmqHTxrW8XAlRGGtI3sWCHMt6N_skVLVWiNClq0tc4B0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af32OUDyJZSyWmmudFpW3s9DHF0WrPj2ccQu8evjYlyhzQ&oe=69DC416A",
                "width": 640
              },
              "igtv_first_frame": {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/657890705_2285271555294595_6835517889432916428_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=110&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=em59qG2Nc5sQ7kNvwGXSrdp&_nc_oc=Adrlw4eZxd4QVyyYtH1flVqnmqHTxrW8XAlRGGtI3sWCHMt6N_skVLVWiNClq0tc4B0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af32OUDyJZSyWmmudFpW3s9DHF0WrPj2ccQu8evjYlyhzQ&oe=69DC416A",
                "width": 640
              }
            },
            "candidates": [
              {
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/658121967_949001457615163_419601300774826918_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg2NjYwMDM1OTA5MTY4NjA1NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=kMeyljGsjPkQ7kNvwG-d6lE&_nc_oc=AdrX4Jjj13FgOK7lomcTSjdJYVuk4tD38Lo0wOY5waqpf04xrMl10daUoUf-dJaIsGA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af31Cd1Xtbwke7KxhntnSghB60fQ4uuEFBTbZGOpp4WgUQ&oe=69DC5332",
                "width": 640
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 669,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_width": 1500,
                "thumbnail_duration": 0.50617142857143,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 53.148
              }
            }
          },
          "is_comments_gif_composer_enabled": true,
          "is_dash_eligible": 1,
          "is_post_live_clips_media": false,
          "is_quiet_post": false,
          "is_third_party_downloads_eligible": true,
          "like_and_view_counts_disabled": false,
          "media_type": 2,
          "number_of_qualities": 2,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQTlTVGJjaXF6SGNnYXdVU3FMWFkzTnIzODY2NjAwMzU5MDkxNjg2MDU1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2NzIyNzQ2MnwzODY2NjAwMzU5MDkxNjg2MDU1fDY3NTI1MjMwNTV8YTkyM2NiNmI2M2Q3ZmFmMWI1MThiNTNjYmQ4N2VmYzEyNzc0OWIyYjlhMDllM2UzNWNkNGE2MmU2YWQ4NjhjOCJ9LCJzaWduYXR1cmUiOiIifQ==",
          "original_height": 1280,
          "original_media_has_visual_reply_media": false,
          "original_width": 720,
          "product_type": "clips",
          "taken_at": 1775154752,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "6752523055",
            "id": "6752523055",
            "account_badges": [],
            "fan_club_info": {},
            "fbid_v2": 17841406811654065,
            "feed_post_reshare_disabled": false,
            "friendship_status": {
              "following": false,
              "is_bestie": false,
              "is_feed_favorite": false,
              "is_restricted": false,
              "outgoing_request": false
            },
            "full_name": "Nuria Taboada",
            "has_anonymous_profile_picture": false,
            "interop_messaging_user_fbid": "110265577029021",
            "is_facebook_onboarded_charity": false,
            "is_favorite": false,
            "is_private": false,
            "is_unpublished": false,
            "is_verified": false,
            "merchant_checkout_style": "none",
            "pk": 6752523055,
            "profile_pic_id": "3869835622605851526_6752523055",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=E_ajg83nLc4Q7kNvwGyZyDc&_nc_oc=AdoL30aqQvXaK84Z-JA7zJkYuwPAaFX60_8jXZKVL6Cmp9d6teapeR7jP_yCwSlwot8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0qjDjO1ASpPmGjwl2h6Os-RWmQxKc4IdOC_JhCt6iNiQ&oe=69DC561A",
            "seller_shoppable_feed_type": "none",
            "show_account_transparency_details": true,
            "show_shoppable_feed": false,
            "third_party_downloads_enabled": 1,
            "transparency_product_enabled": false,
            "username": "caldeironuria70"
          },
          "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT53.127254S\" FBManifestTimestamp=\"1775667227\" FBManifestIdentifier=\"FragtJ0NGBBpZ19kYXNoX2Jhc2VsaW5lGVbo0vrk6+efA5r85tLY0b0EjIrfp/2a2Qb26fGvvc+rC7qmuO3ft/JdIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFaGVhdnkAFgoUABIUAAA=\"><Period id=\"0\" duration=\"PT53.127254S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.2\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1261443792822029v\" bandwidth=\"1621306\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"10718079\" FBPlaybackResolutionMos=\"0:100,360:95.4,480:94,720:89.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.52,480:97.9,720:96.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/399\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQP7AQiyt9CYVpvjIWYIk1IhA2CFs2hRaPlPP9a-bVAS3VY3P5TobyhgHr4uojwMAQP7-tOgeq1G6fT0Otw73terqxU2QE4uqecwePQ.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=MgUg0hrvzdMQ7kNvwHKUouq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkxMDM4MzM1NTM2ODAyNywiYXNzZXRfYWdlX2RheXMiOjUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1MywiYml0cmF0ZSI6MTYyMTMwNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af26MCHD6nKXb4wOR1-gJtT4VFIzKok7FXP05-fCCR2EsA&amp;oe=69D84AFC</BaseURL><SegmentBase indexRange=\"893-1056\" timescale=\"11988\" FBMinimumPrefetchRange=\"1057-41069\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1057-480175\" FBFirstSegmentRange=\"1057-1055684\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1055685-1912196\" FBPrefetchSegmentRange=\"1057-1055684\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-892\"/></SegmentBase></Representation><Representation id=\"1885026425496198v\" bandwidth=\"370880\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"2451805\" FBPlaybackResolutionMos=\"0:100,360:71.8,480:65.7,720:54.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.4,480:80.8,720:69.9\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"11988/399\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMdAGS45Z71W55tHU5j-QMxkEk4h4SKkVv4GC-ASdTTkAt7NhyNx2BNCALrxuItd9h_F2tj5kt6MdpAlwTM9UT3E-DHCvRXc8xPciU.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=toErI9LhazcQ7kNvwHb0VUr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzkxMDM4MzM1NTM2ODAyNywiYXNzZXRfYWdlX2RheXMiOjUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1MywiYml0cmF0ZSI6MzcwODgwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3WwpqcVLF4SBCxAgXUx6ue1gNGlCH8zX7McQh-HdeEqw&amp;oe=69D86AF3</BaseURL><SegmentBase indexRange=\"888-1051\" timescale=\"11988\" FBMinimumPrefetchRange=\"1052-15252\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1052-119656\" FBFirstSegmentRange=\"1052-252863\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"252864-459377\" FBPrefetchSegmentRange=\"1052-252863\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-887\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"914378644739252a\" bandwidth=\"39903\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"39903\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"265989\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOj1BRbsePAoEcTk2f6cwX23Jzya2r1UB-Xw5oGv-oEUSJH5lkHBRrUfjyvYyO_yN-BYcE0fpIabMNnVKE1Mbe5TagQCDpyArCt2ZE.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=RpAabF4pSzkQ7kNvwH2sjuF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMzU1MzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUzLCJiaXRyYXRlIjo0MDA1MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Y5z8GXlsM-M6b8uuRt86oijcR2_nQ1tt2wwLhQfakVw&amp;oe=69DC4C77</BaseURL><SegmentBase indexRange=\"837-1000\" timescale=\"44100\" FBMinimumPrefetchRange=\"1001-1699\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1001-13523\" FBFirstSegmentRange=\"1001-25248\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"25249-49777\" FBPrefetchSegmentRange=\"1001-25248\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"26428819243469213a\" bandwidth=\"74585\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74585\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"496311\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPmxXJRaxWGZd11_JobOeLBww0OWVVY2KyDdKZ7UThyo7o0Sh4DKqEPunjFveeOG-7PRN1qvd2HsUUQvU1PFro6rKjUVTfay8qeIrE.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=Z5VOEy--qvEQ7kNvwH58ckO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMzU1MzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUzLCJiaXRyYXRlIjo3NDczNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3LBqOhoXn4QIL10mO3EEZrjiHfOHQVMQCnNJ7UrqoMsQ&amp;oe=69DC6A59</BaseURL><SegmentBase indexRange=\"838-1001\" timescale=\"44100\" FBMinimumPrefetchRange=\"1002-1731\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-25390\" FBFirstSegmentRange=\"1002-48490\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"48491-94829\" FBPrefetchSegmentRange=\"1002-48490\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"3192148190968443a\" bandwidth=\"103749\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"103749\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"689979\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN0WB5JH2CkyygyXyWJ6D1hl7-Jx_0dByoLo5aC6uvE2heWRd-3bb5HZ5KX6vkwX1GW8XkoCyjX50F7z2ceAGmtoMGMo0WGE6B1uQA.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=xGHN05NYpZEQ7kNvwEBQGm3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTEwMzgzMzU1MzY4MDI3LCJhc3NldF9hZ2VfZGF5cyI6NSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUzLCJiaXRyYXRlIjoxMDM4OTgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=l57lw0MqR621IRoUPY9vpQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ZnqNzX5TyqLG5bXZbiNLW6jw56EoanGeR5n5ek2tiGg&amp;oe=69DC53FA</BaseURL><SegmentBase indexRange=\"833-996\" timescale=\"44100\" FBMinimumPrefetchRange=\"997-2050\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"997-35293\" FBFirstSegmentRange=\"997-67634\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"67635-132508\" FBPrefetchSegmentRange=\"997-67634\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "video_subtitles_locale": "es_CL",
          "__is_XDTMediaDict": true
        }
      },
      "parent_comment_id": "18142813870496178",
      "pk": "18088027280262150",
      "private_reply_status": 0,
      "replied_to_comment_id": "18142813870496178",
      "share_enabled": true,
      "status": "Active",
      "strong_id__": "18088027280262150",
      "text": "@vegagarcianatalia",
      "type": 2,
      "user": {
        "fbid_v2": 17841406811654065,
        "full_name": "Nuria Taboada",
        "id": "6752523055",
        "is_mentionable": true,
        "is_private": false,
        "is_verified": false,
        "pk": 6752523055,
        "pk_id": "6752523055",
        "profile_pic_id": "3869835622605851526_6752523055",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/660105665_18353241988227056_2402161562898716353_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=104&ig_cache_key=GMFpWCfwXy8lLTRBAMHWrNk2MVYhbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=E_ajg83nLc4Q7kNvwGyZyDc&_nc_oc=AdoL30aqQvXaK84Z-JA7zJkYuwPAaFX60_8jXZKVL6Cmp9d6teapeR7jP_yCwSlwot8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=l57lw0MqR621IRoUPY9vpQ&_nc_ss=7a3ba&oh=00_Af0qjDjO1ASpPmGjwl2h6Os-RWmQxKc4IdOC_JhCt6iNiQ&oe=69DC561A",
        "strong_id__": "6752523055",
        "username": "caldeironuria70"
      },
      "user_id": 6752523055
    }
  ],
  "has_more_head_child_comments": false,
  "has_more_tail_child_comments": false,
  "is_ranked_replies": false,
  "liked_by_media_owner_badge_enabled": true,
  "parent_comment": {
    "bit_flags": 0,
    "comment_has_a_visual_reply_media": true,
    "comment_like_count": 2,
    "content_type": "comment",
    "created_at": 1774989022,
    "created_at_for_fb_app": 1774989022,
    "created_at_utc": 1774989022,
    "did_report_as_spam": false,
    "has_disliked_comment": false,
    "has_liked_comment": false,
    "has_translation": true,
    "is_covered": false,
    "is_photo_comments_enabled_for_comment_author": false,
    "is_text_editable": false,
    "is_edited": false,
    "meta_ai_comment_type": "NONE",
    "is_ranked_comment": false,
    "liked_by_media_coauthors": [],
    "media_id": 3864286541032633353,
    "pk": "18142813870496178",
    "private_reply_status": 0,
    "share_enabled": true,
    "status": "Active",
    "strong_id__": "18142813870496178",
    "text": "Ya está bien tapar estás palabras: violación y violencia etc",
    "type": 0,
    "user": {
      "fbid_v2": 17841446167674237,
      "full_name": "Natalia Vega Garcia",
      "id": "46193898922",
      "is_mentionable": true,
      "is_private": false,
      "is_verified": false,
      "pk": 46193898922,
      "pk_id": "46193898922",
      "profile_pic_id": "2518281128395959898_46193898922",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/151792571_774741103247720_206392669820779548_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=101&ig_cache_key=GLsrDAlogUB4n8ACABx86SgKQd0CbkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy43NDcuQzMifQ%3D%3D&_nc_ohc=k9oKjXegbQkQ7kNvwETc_mR&_nc_oc=AdpMXsGevdoZ03ybfvVlc8FxOYXzSirinhooc4c8bHH2zYDdXYvVufBhdd8wsme8Bl8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af2L5yS_eW0UvdFpq1Jq8Y9NxvNU_QjXEEZqiMd39vwJkw&oe=69DC6033",
      "strong_id__": "46193898922",
      "username": "vegagarcianatalia"
    },
    "user_id": 46193898922
  },
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/code",
        headers={"x-access-key": "YOUR_TOKEN"},
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
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwEasgoV&_nc_oc=AdrXLYULDUTazCkhZ34bDArZEwtOaiXsaASHlTiYbeQwYVQwG82lZedJuhcmUC60I9c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=6CcdKECBoEcIWsIXB4foTg&_nc_ss=7a3ba&oh=00_Af0ypYpvoBwQUWH6QB6Vh7KYUXBmn_YW3LDgLDcv3eDxtQ&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwEasgoV&_nc_oc=AdrXLYULDUTazCkhZ34bDArZEwtOaiXsaASHlTiYbeQwYVQwG82lZedJuhcmUC60I9c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=6CcdKECBoEcIWsIXB4foTg&_nc_ss=7a3ba&oh=00_Af0ypYpvoBwQUWH6QB6Vh7KYUXBmn_YW3LDgLDcv3eDxtQ&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740,
            83610
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwEA0SON&_nc_oc=AdpuMWLQ0LVD1FABzSYyhgCgr-hs0n4XEYPnss51NKSi5lutT3ZY8YmvtO5SUerMt6Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=6CcdKECBoEcIWsIXB4foTg&_nc_ss=7a3ba&oh=00_Af35u0-C9E4m5-eeb4OCUS-UsCNfA-aN-nvVPDz5i1I5lg&oe=69DC3E7E",
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
            "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHlYGnI2PAFBfob7VvbjWcoOQdwvTqsT8NatUNbM10IjQT2PavSSPlZz9aodjoVwCs&_nc_ohc=7fRK9vLZo4UQ7kNvwHHoubs&_nc_gid=6CcdKECBoEcIWsIXB4foTg&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af276eMQmgpoGGRABrXx9bVYiKKiWI5Vxn655EBD9aOUaQ&oe=69DC4C8A&_nc_sid=55bbed"
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
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOWVhMDg1NmNjYmUzNGVkMmI4MzdhYTQ2Nzc5OTg0OWYzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2Mzk1OTI3MHwzNzc2ODMyODk4MjgwMjI4MTQ1fDI5NTI1MTA0NTk4fGE5NmE0ODEwNjE1MTk3OWRkNmMyZTAxYzJjMGE5N2RhMDZkMjNhZjdlNWZlNjhjNzY1NGQwNjJlYmM3ZGJiYjMifSwic2lnbmF0dXJlIjoiIn0=",
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
          "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHlYGnI2PAFBfob7VvbjWcoOQdwvTqsT8NatUNbM10IjQT2PavSSPlZz9aodjoVwCs&_nc_ohc=XbeNvhLXv28Q7kNvwEVnidP&_nc_gid=6CcdKECBoEcIWsIXB4foTg&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2YUwYFVr3FBKoxPuqq_-mckKtpWTth3b82CqPBeU2OZQ&oe=69DC51E9&_nc_sid=55bbed"
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
    "like_count": 135429,
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
        "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHlYGnI2PAFBfob7VvbjWcoOQdwvTqsT8NatUNbM10IjQT2PavSSPlZz9aodjoVwCs&_nc_ohc=XbeNvhLXv28Q7kNvwEVnidP&_nc_gid=6CcdKECBoEcIWsIXB4foTg&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2YUwYFVr3FBKoxPuqq_-mckKtpWTth3b82CqPBeU2OZQ&oe=69DC51E9&_nc_sid=55bbed"
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
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEg96MI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=6CcdKECBoEcIWsIXB4foTg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af351fBUUQhXJaMEenuQ0U6MsWVUXr5KbrbArqSRzsl72g&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 102,
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEg96MI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=6CcdKECBoEcIWsIXB4foTg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af351fBUUQhXJaMEenuQ0U6MsWVUXr5KbrbArqSRzsl72g&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 103,
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEg96MI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=6CcdKECBoEcIWsIXB4foTg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af351fBUUQhXJaMEenuQ0U6MsWVUXr5KbrbArqSRzsl72g&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663959\" FBManifestIdentifier=\"Fq7ts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxozhmaSP8rACovXRl+ao3wKKjIn135CYA5665tXdzJYE6rO+3tWCgQXOuqeDzoi9BeyasszencwFms+wm8jvsAaKn4CC49CdB8SwgOTBoeoH3JLz6tnu0gie6+vzqMzJDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWggIUABIUAgA=\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwFpI8fw&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1iDS8ZqMbCHxlYxIa-pTBez7RwR-gg2yg2uAP_Aoxr9Q&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=bCouttTbvR0Q7kNvwGv80n1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2NsO2slcDC7JcGLytVH47LOJ3TsgeiyMw_ORu6YdWLsQ&amp;oe=69DC6069</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwElkzss&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0wvRmeZDBlLzPfjqupsfU5ScVdjPV5mvpVzcIRUvR07g&amp;oe=69DC5940</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwEATAFP&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Xnzzpp70QBi_zXg-8AX-Nnf47noPmS-Yo7hadr_n7Fw&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwFZsii7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3NPVW2MKeSNuxBnmSE1GohKWgeMhb8X_bl93w6nkuJPw&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwFZfE_M&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2gTwigbWUC0aCxw5_gBGhyPye3EZJT5zF-YSwektBLXA&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwEKjjrz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2rF6jpeA3MACKtplXEzo90eXMOmQbUp_bXM6Eg613FEQ&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"897489239614213v\" bandwidth=\"4472890\" codecs=\"av01.0.08M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"12475999\" FBPlaybackResolutionMos=\"0:100,360:87.2,480:83.7,720:78.9,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.536,480:99.415,720:99.167,1080:98.58\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPVgubbzL4GsEHBto9qJ9DKVHDYdRJUIBrbusVYgthsUApFExMmHIPHOP4-rKP0NJU5hwD7ETkAkZNePbo3qf5TReJDHCiOkPRu_hM.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=PMWR1v3uaAgQ7kNvwE8p4_a&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ0NzI4OTAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1pNpO1lfGZSgXt8JAN6W560mZm1FS8jONn6jUpbySrtA&amp;oe=69DC5E06</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-105462\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-2456793\" FBFirstSegmentRange=\"899-3691660\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"3691661-8660328\" FBPrefetchSegmentRange=\"899-3691660\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwF9hhVR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Uv_xZyG9GyL6gOi0kafnsldVHfocauFnvPRNAyp-1Ow&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwFefOON&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af38-yXVk5nM1czK100lIGQvflBvprx9Wsb_088881Qslg&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwE2e87j&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2UiFCHhh2UqD-ctn8SPXf-XmlQZHbHa2z-O3Nh-IWI4Q&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwFH1L2X&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=6CcdKECBoEcIWsIXB4foTg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0WXCok3IXKPmeltP1WRQPEXKeRwWOi5dMhyrcjJmx7ag&amp;oe=69DC5283</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHlYGnI2PAFBfob7VvbjWcoOQdwvTqsT8NatUNbM10IjQT2PavSSPlZz9aodjoVwCs&_nc_ohc=XbeNvhLXv28Q7kNvwEVnidP&_nc_gid=6CcdKECBoEcIWsIXB4foTg&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2YUwYFVr3FBKoxPuqq_-mckKtpWTth3b82CqPBeU2OZQ&oe=69DC51E9&_nc_sid=55bbed",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775659002,
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
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
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFoIfUB&_nc_oc=AdrdLA36UIKPg06fstexgArf5PRVgzUh8YSi4fdRojdkNct71A1erwaniknSPaJiTjE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=kwATG0fynHSPd3W4N62eAQ&_nc_ss=7a3ba&oh=00_Af32CAOjLsiOc5px4jGwMcSowDLnW4yE7TPTkOjVAOAxlQ&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFoIfUB&_nc_oc=AdrdLA36UIKPg06fstexgArf5PRVgzUh8YSi4fdRojdkNct71A1erwaniknSPaJiTjE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=kwATG0fynHSPd3W4N62eAQ&_nc_ss=7a3ba&oh=00_Af32CAOjLsiOc5px4jGwMcSowDLnW4yE7TPTkOjVAOAxlQ&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740,
            83610
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFst-qN&_nc_oc=AdqfiiHYiuZCwGLvaN6mm2wvFBGAN9LWn-9qCuYOPorCDbcgamXUXXhYtsaR4wFijec&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=kwATG0fynHSPd3W4N62eAQ&_nc_ss=7a3ba&oh=00_Af3tJaImM7ho02H9kHirYprCAa3rb-EG-klUnx-s0UlhBw&oe=69DC3E7E",
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
            "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gG_XwoMHcPUWyzL_ON6zjGhFPO2GsrxAHcDzLJILIRCZEZJkM2LgbeSfrvqScoTeME&_nc_ohc=7fRK9vLZo4UQ7kNvwGtRppA&_nc_gid=kwATG0fynHSPd3W4N62eAQ&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af2tA3xORtuDKWRXYexENpZZotpc0V4ZVGnjDVmSoYk1AA&oe=69DC4C8A&_nc_sid=55bbed"
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
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNDVhZDQ3ZjM3NTBlNDIyMGIyMTRlM2FiNGVhOGRiZDQzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2Mzk1ODIzNHwzNzc2ODMyODk4MjgwMjI4MTQ1fDM4ODM2NTUyNzI4fGJiYzFmOTJjOWFlYTU0ODRhOGQ0ZjQwNjRiM2E3ZWFlMTc0NDdkOTQwNWZlYzBkNzU4NDU3ODVmMzlhNzY5ZjAifSwic2lnbmF0dXJlIjoiIn0=",
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
          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG_XwoMHcPUWyzL_ON6zjGhFPO2GsrxAHcDzLJILIRCZEZJkM2LgbeSfrvqScoTeME&_nc_ohc=XbeNvhLXv28Q7kNvwGm64wx&_nc_gid=kwATG0fynHSPd3W4N62eAQ&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af214S8lcRRSXC01NRpuxYCMFohMXZzf4Bz7ZJ08ff1WWQ&oe=69DC51E9&_nc_sid=55bbed"
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
    "like_count": 135429,
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
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG_XwoMHcPUWyzL_ON6zjGhFPO2GsrxAHcDzLJILIRCZEZJkM2LgbeSfrvqScoTeME&_nc_ohc=XbeNvhLXv28Q7kNvwGm64wx&_nc_gid=kwATG0fynHSPd3W4N62eAQ&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af214S8lcRRSXC01NRpuxYCMFohMXZzf4Bz7ZJ08ff1WWQ&oe=69DC51E9&_nc_sid=55bbed"
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
        "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHlJOF9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=kwATG0fynHSPd3W4N62eAQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0pGBqB-Y3WxbykJP9Aw02VL3sJvB_1KUf9IpYp4Bg5uQ&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 102,
        "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHlJOF9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=kwATG0fynHSPd3W4N62eAQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0pGBqB-Y3WxbykJP9Aw02VL3sJvB_1KUf9IpYp4Bg5uQ&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 103,
        "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHlJOF9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=kwATG0fynHSPd3W4N62eAQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0pGBqB-Y3WxbykJP9Aw02VL3sJvB_1KUf9IpYp4Bg5uQ&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663958\" FBManifestIdentifier=\"Fqzts50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZhojR4r/Q2Y0D0qP4j7HP7gTc7biv2tL1BNy48a7NxpAFnoq59pqbxwX8q/bF7erMBcjV6ur59fAH1O2YhM2R5woiGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABaCAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1563973005025935v\" bandwidth=\"337669\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"941843\" FBPlaybackResolutionMos=\"0:100,360:29.3,480:28.4,720:29.1,1080:31.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:70.9,480:62.6,720:50.4,1080:39.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMN6p1XA_FXFLkUVYTtE8Zwx7keoWfwDMyx-B_QxL4pXgZeg8McEumkwF6WDJ4fnzDnBOTY9wUJL7oCRtGW6qjDxoh6M3Qq7Su4omI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=BfloUU35i64Q7kNvwHOm9bZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjMzNzY2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1m9VtOAI_Tn2wGhcIjTwpI-9pFhIcvzhcHk_NP0LQafg&amp;oe=69DC3392</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-14042\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-89181\" FBFirstSegmentRange=\"891-165373\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"165374-688020\" FBPrefetchSegmentRange=\"891-165373\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1443772230413870v\" bandwidth=\"509752\" codecs=\"vp09.00.30.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1421827\" FBPlaybackResolutionMos=\"0:100,360:40.4,480:38,720:37.2,1080:38.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:80.5,480:73.6,720:62.8,1080:52.4\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO03YPWFT70GHasKStspUo-nCsZakOgI61xyRI5dJ6BZRsyp4lBEZKTh7qJH33vHao8lA7Gz8jHRXP-xoDvVyNDrlzf18WIgj_ye2E.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=O1KjHuo6qEEQ7kNvwGSadke&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUwOTc1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ke2UkrQC6Xx2TgF87aSlw3WJyju9nJO1OLy7zmH1X5Q&amp;oe=69DC5A86</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-19700\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-153929\" FBFirstSegmentRange=\"891-284632\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"284633-1049599\" FBPrefetchSegmentRange=\"891-284632\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3041551559367530v\" bandwidth=\"722308\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2014698\" FBPlaybackResolutionMos=\"0:100,360:51.1,480:47.8,720:45.4,1080:45.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.5,480:81.3,720:72.1,1080:62.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPSpcAxu8AB6FoUvT9edmiINl_OKU0kxsELupA-W7mtlP9_ucOO0LmcFcGoF7nFLPaLtxp6SODqMd31GQF9E68R4xCcOv91YV_Za6U.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=D5k1RwfW4qsQ7kNvwG9pYiT&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjcyMjMwOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3W0pzJR9mEsuM47UCXXlDjrex9Unkl-xwu8Utw4WNiTQ&amp;oe=69DC3677</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-28550\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-246143\" FBFirstSegmentRange=\"891-439881\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"439882-1486392\" FBPrefetchSegmentRange=\"891-439881\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1576336420162302v\" bandwidth=\"989685\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2760477\" FBPlaybackResolutionMos=\"0:100,360:60.9,480:57,720:54.1,1080:53.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91,480:87.2,720:79.7,1080:71.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNWawONH_0ykNRhgXYD5USnUS-2JcDjQ0cKPtzUQ4bmPrDRMRJgACUHEnYvSCFWgDRdksntOheWe4DkpraAAYpYXQpEyt7yK9nS-5A.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=JGpaa8RbgzYQ7kNvwFsqyRD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjk4OTY4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2VuFjr2YkscJclnb7KewkkfCy7kyvkBQU0zXoBls_DbA&amp;oe=69DC6548</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-36175\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-368341\" FBFirstSegmentRange=\"891-638853\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"638854-2015969\" FBPrefetchSegmentRange=\"891-638853\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1384606506359662v\" bandwidth=\"1369954\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3821143\" FBPlaybackResolutionMos=\"0:100,360:69.5,480:65.5,720:61.7,1080:60\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.2,480:91.7,720:86.3,1080:79.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPHjz86uKmkZFb6AfTAuNXhaCR5cY5lsEh1FSO9m1gsCdbf2BQ8JMp-g6pMIlhKv6fDPKpemYtUf_SuYjLt-9p7iIGYj7iVdOv9W4k.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=waJfS4YiB8AQ7kNvwHIklHU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzNjk5NTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3VsuLK0IQZ7a-uP9hRqcNaVA_JYzDC1oRit-pVgLg4_g&amp;oe=69DC61BA</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-46923\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-542605\" FBFirstSegmentRange=\"891-915699\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"915700-2726908\" FBPrefetchSegmentRange=\"891-915699\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1369156268001513v\" bandwidth=\"1822480\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"5083349\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:71.6,720:67.7,1080:65.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:94.5,720:90.4,1080:85.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMvyH-MQjdKfi00Fl5WSSH-1UKJzwFI8zT_5r_axCxb1zBFH7oejYKyu0sw6aikisn4kwP7Dvea3yfEnFbu9mGB_M3KNvNh7vkIxnY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=cgpTCsrJnfQQ7kNvwHR9quZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE4MjI0ODAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3498DWX-Tvw7gkfUqAqx1ctwaYGgk4zkuPDAGpoLf0tQ&amp;oe=69DC6661</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-58146\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-759235\" FBFirstSegmentRange=\"891-1253416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1253417-3555514\" FBPrefetchSegmentRange=\"891-1253416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"2218641838658916v\" bandwidth=\"2563525\" codecs=\"vp09.00.31.08.00.02.02.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"7150307\" FBPlaybackResolutionMos=\"0:100,360:81.3,480:77.1,720:73.4,1080:70.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.9,720:94.1,1080:90.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6gX6iet6wVi2vwiQzpMYKnTkzyIOrnIhhWCeS_HxxTf5k1JEyxtDXBZl3W1nkz-gCcy90W_Uonp2gPqR_zfKL3rzkQ3beNg1DNR0.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=ZhVzyNU6d_IQ7kNvwHG4W0X&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI1NjM1MjUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3oPraoDbo25VlWwlylRnZCwZt3_MIP8TvGMR0AGdvWPQ&amp;oe=69DC6663</BaseURL><SegmentBase indexRange=\"799-890\" timescale=\"11988\" FBMinimumPrefetchRange=\"891-74586\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"891-1107880\" FBFirstSegmentRange=\"891-1794122\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1794123-4835105\" FBPrefetchSegmentRange=\"891-1794122\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"874552045098052a\" bandwidth=\"46857\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46857\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"131698\" FBPaqMos=\"86.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQPkB7GmtjggjHEJa-kd2XK21HSs5MPOBh8Kn_V_b6gCkSbQo9RxM5qstTSXAhy-_70SQiuAW02OQtBnYlPkvoo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=ZSfr4AA8_vgQ7kNvwEqwS4c&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjQ3MjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=kwATG0fynHSPd3W4N62eAQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Lu-vglTKz-qQHi2DdFBtheVBjwRCcdvdV0FpuQvPMQw&amp;oe=69D859DB</BaseURL><SegmentBase indexRange=\"824-999\" timescale=\"48000\" FBMinimumPrefetchRange=\"1000-1360\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1000-14536\" FBFirstSegmentRange=\"1000-12223\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"12224-22571\" FBPrefetchSegmentRange=\"1000-22571\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG_XwoMHcPUWyzL_ON6zjGhFPO2GsrxAHcDzLJILIRCZEZJkM2LgbeSfrvqScoTeME&_nc_ohc=XbeNvhLXv28Q7kNvwGm64wx&_nc_gid=kwATG0fynHSPd3W4N62eAQ&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af214S8lcRRSXC01NRpuxYCMFohMXZzf4Bz7ZJ08ff1WWQ&oe=69DC51E9&_nc_sid=55bbed",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775659002,
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/info/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
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
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwEFgDvK&_nc_oc=AdrduPN8TxgVW_y8ZTzxF_WNybg-7DpKhLcl0QEFvj0GhCIdhex5g99qDNhF-unrwBw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&_nc_ss=7a3ba&oh=00_Af2LtWChF_LfnYXLMHdjIsQhnmJgg2yzrBqSMyi5y-W77A&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "igtv_first_frame": {
          "estimated_scans_sizes": [
            6839,
            13678,
            20517
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwEFgDvK&_nc_oc=AdrduPN8TxgVW_y8ZTzxF_WNybg-7DpKhLcl0QEFvj0GhCIdhex5g99qDNhF-unrwBw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&_nc_ss=7a3ba&oh=00_Af2LtWChF_LfnYXLMHdjIsQhnmJgg2yzrBqSMyi5y-W77A&oe=69DC368F",
          "width": 640,
          "is_spatial_image": false
        },
        "smart_frame": null
      },
      "candidates": [
        {
          "estimated_scans_sizes": [
            27870,
            55740,
            83610
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFlm9ux&_nc_oc=Ado9IEtVNj64p_n2NHpaH2Pau_MyZ8bKanXklmdM9FM_l_yCbeQ9jkGQQedvx21RXdM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&_nc_ss=7a3ba&oh=00_Af08LlChSY7k_CLzbA6kHkZVbF_LNQENrJ5lz3fCj-Sfmg&oe=69DC3E7E",
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
            "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEcRouKc74kUBdBvxBj59wE_473wfipchsFPz__g5nyrLm9Jet_ytX6cbFQv1krBO8&_nc_ohc=7fRK9vLZo4UQ7kNvwGcaD7b&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&edm=AEcnVisBAAAA&ccb=7-5&oh=00_Af2Xp5dWOOhBMRmF8F2qZ1VcJCV8bVAOiQb3sJD9WNLjcg&oe=69DC4C8A&_nc_sid=55bbed"
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
    "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiOTVhY2ZmZWY0NzUwNGI0ZGIyYTk1NGUzNTc5YjkwMjYzNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2Mzk2MDYyN3wzNzc2ODMyODk4MjgwMjI4MTQ1fDM4MzM3ODgyNDg4fGM0M2IwZTBiNDRjYTAxOGMzM2Q3ZGM3NGM1OGEzM2RhN2RhMDc5YTU3MzcwMDhlYjQxZWQwY2E0NTAxYTk5ODgifSwic2lnbmF0dXJlIjoiIn0=",
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
          "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEcRouKc74kUBdBvxBj59wE_473wfipchsFPz__g5nyrLm9Jet_ytX6cbFQv1krBO8&_nc_ohc=XbeNvhLXv28Q7kNvwHo-kWA&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3vm6sVtLiUBzkWMj0uwE62VvN88DrbNR1aGVL6AaPVKQ&oe=69DC51E9&_nc_sid=55bbed"
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
    "like_count": 135429,
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
        "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEcRouKc74kUBdBvxBj59wE_473wfipchsFPz__g5nyrLm9Jet_ytX6cbFQv1krBO8&_nc_ohc=XbeNvhLXv28Q7kNvwHo-kWA&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3vm6sVtLiUBzkWMj0uwE62VvN88DrbNR1aGVL6AaPVKQ&oe=69DC51E9&_nc_sid=55bbed"
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
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwETM_dl&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2Iud8nAL_xdlPxcRHnTzrUrAgVNDkhMjtAecg0rFx9cw&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 102,
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwETM_dl&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2Iud8nAL_xdlPxcRHnTzrUrAgVNDkhMjtAecg0rFx9cw&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 2315752,
        "height": 1280,
        "id": "1525428988604088v",
        "type": 103,
        "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwETM_dl&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2Iud8nAL_xdlPxcRHnTzrUrAgVNDkhMjtAecg0rFx9cw&oe=69D86FAF",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      }
    ],
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663960\" FBManifestIdentifier=\"FrDts50NGBBpZ19kYXNoX2Jhc2VsaW5lGVbwuvfP09e1BeyasszencwF7KyC/a+71QWaz7CbyO+wBp7r6/OozMkPIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFoICFAASFAIA\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"2\"/><Representation id=\"1525428988604088v\" bandwidth=\"2268538\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"6327492\" FBPlaybackResolutionMos=\"0:100,360:94.2,480:90.6,720:82.4,1080:75.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:96.6,720:94.1,1080:90\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/499\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=Ey9Zfx1FVawQ7kNvwETM_dl&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjg1MzgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Gx8hSnsSQSo073qE3aiUz9iOPd5BtHCA3kR6A6Dzo-A&amp;oe=69D86FAF</BaseURL><SegmentBase indexRange=\"874-965\" timescale=\"11988\" FBMinimumPrefetchRange=\"966-82009\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-832807\" FBFirstSegmentRange=\"966-1651564\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1651565-4297059\" FBPrefetchSegmentRange=\"966-1651564\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-873\"/></SegmentBase></Representation><Representation id=\"1595311911881526v\" bandwidth=\"516706\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"1441216\" FBPlaybackResolutionMos=\"0:100,360:70.1,480:64.5,720:55.5,1080:44.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:84.8,480:79.7,720:70.5,1080:59.6\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"11988/499\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQPT958-vWmEXFo_grVlw2vnBqTKdk9uQHmeTNkCIIC7NdKkZPEJWGTrwPpf3FSw4zpEJJauBM-jUYof9m2tdkX55bI8s38qZHGbGV4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=QwCnrPhQZCAQ7kNvwE7xyl5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjUxNjcwNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af04fKt4gDknrDD_RJb-sHfI1DPrhxI0Pk--5xOpng1Chw&amp;oe=69D84B1B</BaseURL><SegmentBase indexRange=\"869-960\" timescale=\"11988\" FBMinimumPrefetchRange=\"961-23752\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-145022\" FBFirstSegmentRange=\"961-317467\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"317468-1041332\" FBPrefetchSegmentRange=\"961-317467\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-868\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwHZZFyy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0kpwzXJYsNbWrQAN99eXtJNMH476Qyfqh75yX4Ggr2cQ&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwEjIo9P&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3f8H2xCVKyv4bZW1erh-hQFc62aTVnbtw3VxyrT_WPbA&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwFAwf-i&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1FLESz3QmFLkl_M2t9n7ef97gJP5t7__NlVV2dfoWEiA&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "number_of_qualities": 2,
    "video_codec": "avc1.64001f",
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
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEcRouKc74kUBdBvxBj59wE_473wfipchsFPz__g5nyrLm9Jet_ytX6cbFQv1krBO8&_nc_ohc=XbeNvhLXv28Q7kNvwHo-kWA&_nc_gid=B2r1z2_8QDFwUqbL8EQYhg&edm=AEcnVisBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3vm6sVtLiUBzkWMj0uwE62VvN88DrbNR1aGVL6AaPVKQ&oe=69DC51E9&_nc_sid=55bbed",
      "show_account_transparency_details": true,
      "transparency_product_enabled": false,
      "username": "natgeo",
      "latest_reel_media": 1775659002,
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/likers",
        headers={"x-access-key": "YOUR_TOKEN"},
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
      "profile_pic_url": "https://scontent-sof1-1.cdninstagram.com/v/t51.2885-19/324069253_5836767539705305_7097116477300814733_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gEFIGY5ewfIqZ1WJEOpda57ffNJOaJFiQMaOpbSoJ88y_gQihRTH2-_uihFZFj9-ig&_nc_ohc=hKoACuZrKRgQ7kNvwHqe1fq&_nc_gid=OfMXW-QPPyFt3U-qi2LX1Q&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GIXnUBPZNddXgrwUAI0zFn-VBX5ibkULAAAB1501500j-ccb7-5&oh=00_Af0gAY6vlINzSz5fIqrj1ny4tZK3LMRSI7SsJLRnVayfnw&oe=69DC5D58&_nc_sid=bc52df",
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
      "profile_pic_url": "https://scontent-sof1-1.cdninstagram.com/v/t51.82787-19/656236846_18037016978606429_8176123182175805432_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gEFIGY5ewfIqZ1WJEOpda57ffNJOaJFiQMaOpbSoJ88y_gQihRTH2-_uihFZFj9-ig&_nc_ohc=8hgiqdDnz8cQ7kNvwFT2b8-&_nc_gid=OfMXW-QPPyFt3U-qi2LX1Q&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GC5hHSddSdFFkhRAAPjfbBm3bHdxbmNDAQAB1501500j-ccb7-5&oh=00_Af17pvJE_xbkAEG5DGBXa2Ujqy4N6ZdnDu5dyMiQCBzWvg&oe=69DC48D9&_nc_sid=bc52df",
      "username": "only_looking_at_fashionpeople",
      "is_new": false,
      "latest_reel_media": 0
    },
    {
      "strong_id__": "77145556919",
      "pk": 77145556919,
      "pk_id": "77145556919",
      "id": "77145556919",
      "full_name": "張心瑋",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3832460928504522162_77145556919",
      "profile_pic_url": "https://scontent-sof1-1.cdninstagram.com/v/t51.82787-19/633458779_17865824814572920_9097672624501223816_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gEFIGY5ewfIqZ1WJEOpda57ffNJOaJFiQMaOpbSoJ88y_gQihRTH2-_uihFZFj9-ig&_nc_ohc=lxk5Sn6BeMsQ7kNvwEjhxU5&_nc_gid=OfMXW-QPPyFt3U-qi2LX1Q&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GFvQwSV4JbF933g-AIjxMOoMbUF_bmNDAQAB1501500j-ccb7-5&oh=00_Af0okdvO2i5q8EIGJwnuYzhfxLy_HzmXBCRsn5C31v0FYQ&oe=69DC4D0A&_nc_sid=bc52df",
      "username": "xin.wei.chang261891",
      "is_new": false,
      "latest_reel_media": 1775634127
    }
  ],
  "user_count": 135429,
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

    response = requests.get(
        "https://api.hikerapi.com/v2/media/template",
        headers={"x-access-key": "YOUR_TOKEN"},
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
            "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3OwAfyXCatB_TYCzuwNZaxGj294BxH1td5S9mQJd2OvA&oe=69D86FAF",
            "height": 1280,
            "width": 720,
            "type": 101,
            "id": "1525428988604088v",
            "bandwidth": 2315752
          },
          {
            "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3OwAfyXCatB_TYCzuwNZaxGj294BxH1td5S9mQJd2OvA&oe=69D86FAF",
            "height": 1280,
            "width": 720,
            "type": 102,
            "id": "1525428988604088v",
            "bandwidth": 2315752
          },
          {
            "url": "https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHFMaNr&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3OwAfyXCatB_TYCzuwNZaxGj294BxH1td5S9mQJd2OvA&oe=69D86FAF",
            "height": 1280,
            "width": 720,
            "type": 103,
            "id": "1525428988604088v",
            "bandwidth": 2315752
          }
        ],
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                27870,
                55740,
                83610
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwExc08O&_nc_oc=AdpGewr5QEJby3AiN2Ri18KaYIJmJGgFX1e0fx9ve2XNYKjyoBHyeTrCxz9G42HeOck&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af3aQ0pPyCbBNBRJ7VWBl3qCNRx_LHCesmrwLo3CxfkZNw&oe=69DC3E7E",
              "width": 750
            }
          ],
          "additional_candidates": {
            "first_frame": {
              "estimated_scans_sizes": [
                6839,
                13678,
                20517
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-fra5-2.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFnDlpJ&_nc_oc=Adq8OjE-E2KCAcdyIpEbXKCUV5GXypxD6ONd3Dfr7qF4gHfYCVd5SA3HWCJ53dooSDc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af2Pv3pNUt2myiU6-eA47zvtG9kgb_lDjvmH6CPsMG-v4A&oe=69DC368F",
              "width": 640
            },
            "igtv_first_frame": {
              "estimated_scans_sizes": [
                6839,
                13678,
                20517
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-fra5-2.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFnDlpJ&_nc_oc=Adq8OjE-E2KCAcdyIpEbXKCUV5GXypxD6ONd3Dfr7qF4gHfYCVd5SA3HWCJ53dooSDc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af2Pv3pNUt2myiU6-eA47zvtG9kgb_lDjvmH6CPsMG-v4A&oe=69DC368F",
              "width": 640
            }
          },
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "sprite_urls": [
                "https://scontent-fra5-1.cdninstagram.com/v/t51.71878-15/587943902_1168846084884579_7547684066139534601_n.jpg?_nc_cat=102&ccb=7-5&_nc_sid=efdbef&_nc_ohc=pyZiGYy3BegQ7kNvwG7Cld-&_nc_oc=AdoCAQycpyNIq_24zpDtkm2kV084_hgMDG1SmiSx140V4NfmM_7LZ3AV2YLLqu6550I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af3nQ0m3SWnGTSTD_wgG3ghExjYYM28vSauPL2qwNNByUw&oe=69DC4C8A"
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
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663965\" FBManifestIdentifier=\"Frrts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtozhmaSP8rACovXRl+ao3wKeuubV3cyWBOqzvt7VgoEFzrqng86IvQXsmrLM3p3MBZrPsJvI77AGip+AguPQnQfEsIDkwaHqB9yS8+rZ7tIInuvr86jMyQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2ggIUABIUAAA=\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.8\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"1541663213547175v\" bandwidth=\"564017\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1573185\" FBPlaybackResolutionMos=\"0:100,360:43.5,480:41.3,720:40.8,1080:42.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:83.5,480:77.8,720:69,1080:60.7\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO6PWWwWCdIt-L6QC4IMH-mJD8nTfoNqTo8uCADWxYOcbq3vZOvxJAgyBOxkl69SRHR1wb9sel9ZBsHx3Ih8cFZ_oETuy4C9w5X-cY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=y6Q-y0jSGHMQ7kNvwFcSRLc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjU2NDAxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3gcbZSG3TSZJzE_xz3I6hkSlL0ddKPwwVJuj79jqZhwg&amp;oe=69DC3410</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-25807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-202967\" FBFirstSegmentRange=\"899-325225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"325226-1153754\" FBPrefetchSegmentRange=\"899-325225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1175596660739727v\" bandwidth=\"763527\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2129667\" FBPlaybackResolutionMos=\"0:100,360:52.7,480:49.2,720:47.5,1080:48.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.7,480:83.3,720:76,1080:68.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO-yRmUYdWMpWT2pkKoNLmA9TBYEsRFFLMvu8LfOIoTuFwwS19CjUxFy221zonqEEJE03R2bFFsZ5HfpQ7C3I9NN_iRbJ2M7D2M3HA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=bCouttTbvR0Q7kNvwHnZk01&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjc2MzUyNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2EOUbT19C-0waHgZ8KyJhCxuz0mWq6oKanqRlTu-o__A&amp;oe=69DC6069</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-29871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-285263\" FBFirstSegmentRange=\"899-462372\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"462373-1587016\" FBPrefetchSegmentRange=\"899-462372\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2203997066759202v\" bandwidth=\"1044985\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2914723\" FBPlaybackResolutionMos=\"0:100,360:61.3,480:57.6,720:54.8,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:88.9,720:83.2,1080:77.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOuHvisswSr2d9TAqfVHUu8SjtBy0m4oYHsx89CnWos2yiaopXfpGqs0fKLQDKfCF01ql0sj7dmKATomyproECnD2ePBI6CTXewcQM.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=D4pLsnA7sYMQ7kNvwHkxtuX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEwNDQ5ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2p1oj4H5jvakUZU60g_u_tkTkeMduOaroJ3ja6HEAoeg&amp;oe=69DC5940</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-40709\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-427557\" FBFirstSegmentRange=\"899-678729\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"678730-2195077\" FBPrefetchSegmentRange=\"899-678729\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"772558072462673v\" bandwidth=\"1324719\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3694971\" FBPlaybackResolutionMos=\"0:100,360:67.5,480:63.7,720:59.9,1080:58.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.6,720:87.1,1080:82.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrG1qSjCfz4F0V9NR2YvAOseaemUUjZcZsHn5DH-R-UvvVMdUeyquW0ljHjqf9VyEWHsU0Tw6ep2m_bQLnbi9BBgFEFeYwo2m2eGc.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=ovgW3DKb8-EQ7kNvwETlGZ6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjEzMjQ3MTksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2_eAl5j8_zksH5EUVmwfHjKZ06iytwrdArlQ2_tWlobQ&amp;oe=69DC3990</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-47080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-565391\" FBFirstSegmentRange=\"899-894413\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"894414-2820558\" FBPrefetchSegmentRange=\"899-894413\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"1409619774131445v\" bandwidth=\"1679147\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4683559\" FBPlaybackResolutionMos=\"0:100,360:72.2,480:68.5,720:64.4,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.3,720:90.8,1080:86.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNUTnYy_ncqW4UrLF1LOZzW7gnU9R79RSudCrgvmRfr3Vn5MbS1F83HuPCi7Iubc7aAJXhOfTiq96mHQnyJLeYBKQzBYUZVNlXBBvQ.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=x65UMp5Cfp0Q7kNvwGC73yn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjE2NzkxNDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af39Wi0iOr6whdmoOIwzj0tpv07QbGC855nO_to2ngaoxg&amp;oe=69DC4712</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-54357\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-752279\" FBFirstSegmentRange=\"899-1181387\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1181388-3599083\" FBPrefetchSegmentRange=\"899-1181387\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"2035484190574533v\" bandwidth=\"2263616\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6313788\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.1,720:70,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.8,720:94.5,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNKzyZUHjaMkeckK4l8aXSdKLGOgSl7at0rn1fQuPOlrllY8zmzNZzsmQO17VKhhEnd4cnYaJDIDcS0Fx51fY-NzvoVgur0Ps7F8UA.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=BKArKS5cIG0Q7kNvwGfm6hH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjIyNjM2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Nqh_yNSVoOUB9YAkO-JAAUYRYXSbXjhGkZfyFL9ekAA&amp;oe=69DC4DAE</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-63616\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1075022\" FBFirstSegmentRange=\"899-1669843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1669844-4818250\" FBPrefetchSegmentRange=\"899-1669843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation><Representation id=\"670463626000454v\" bandwidth=\"2978054\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8306532\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.3,720:73.3,1080:70.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.44,720:97.4,1080:95.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNSEBPYialPOm5_luiMOG6Vfcc6zat4pYpYrya8UXkSzDUYJsLsZ__WNUegvo025ztYun_QgtQGYVNWpxRlj8xh_jnwIvJbGZhQZcU.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=f4ujq28n01EQ7kNvwFG4g10&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoyOTgzMzI5MDUxODU2NDc0LCJhc3NldF9hZ2VfZGF5cyI6MTI5LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MjIsImJpdHJhdGUiOjI5NzgwNTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af22twblSezBChrZGPXp0C8dFFKi2QTFApN7ADTIPZ2Ciw&amp;oe=69DC3B21</BaseURL><SegmentBase indexRange=\"807-898\" timescale=\"11988\" FBMinimumPrefetchRange=\"899-72564\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"899-1529819\" FBFirstSegmentRange=\"899-2350118\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"2350119-6113038\" FBPrefetchSegmentRange=\"899-2350118\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-806\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4383964508551887a\" bandwidth=\"45539\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45539\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"127951\" FBPaqMos=\"86.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOKVl250exQ9N_jquBnFt2K06bc5HpSGecdkuwAmPXwk6YEobQy-ZuoDXGmA7Cb0yXcv9wt2F3bT7YW5Ksz2YsnQiIw3oRK637MZyo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=fudZ2m7YRDEQ7kNvwGp5mTY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6NDU4NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3gDfEyn_75_KjGJqRvcwRkdBKK5o7UQ8o6KHctIOPg_w&amp;oe=69DC6781</BaseURL><SegmentBase indexRange=\"837-928\" timescale=\"48000\" FBMinimumPrefetchRange=\"929-1893\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"929-15137\" FBFirstSegmentRange=\"929-27959\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27960-56025\" FBPrefetchSegmentRange=\"929-27959\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1796319634396109a\" bandwidth=\"84443\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"84443\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"236469\" FBPaqMos=\"89.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPMDYIjPLCt0rhQL0M3qyPkj9E909cTAWobvdkfa6dDec7JF5BdxE0qrQQ0K2w_UybJkqrvZRFl330Avfwo1mZ3QHBqrsszpGh-Kvw.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-2.cdninstagram.com&amp;_nc_ohc=5AmBeg7W-LwQ7kNvwF-JKa8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6ODQ3NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0wm3cwEtJJbZX0s_CqVIh70rpdi4MqDaTNKgBLipk1lA&amp;oe=69DC3EE6</BaseURL><SegmentBase indexRange=\"838-929\" timescale=\"48000\" FBMinimumPrefetchRange=\"930-2476\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"930-27556\" FBFirstSegmentRange=\"930-52010\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"52011-104107\" FBPrefetchSegmentRange=\"930-52010\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1575011563751094a\" bandwidth=\"119916\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"119916\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"335410\" FBPaqMos=\"94.09\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP0NQ4u5NDwIvWzIsiIMysrNHvEMzoG3PdZ0QM7hjSpMlf_Na5dP3G-ufFjXlpunBw0dYJFkO9ipd8iyIqpgg-cZJryONml6RADAcM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=kta25mTdqGAQ7kNvwGtAQKR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTIwMjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1LBHncVtR4YhJ03q90vPjpaTyZK4H5Zbptd8WEMW7BLA&amp;oe=69DC4031</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2147\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-38529\" FBFirstSegmentRange=\"925-73622\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"73623-147516\" FBPrefetchSegmentRange=\"925-73622\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2434021563720878a\" bandwidth=\"137582\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137582\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"384687\" FBPaqMos=\"94.44\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPG9fyjOfvNXGoSATuijRDtFWSdQZHmeuTQ62YwIdAgM9UpiVsSIfo-xAslvyXrQlUAcFw73ye6mtN2JfFeCc3TdaGevzf0S0BbJzI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=JtTVYEL_d8wQ7kNvwEhHuDg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmlnd3d3LUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjI5ODMzMjkwNTE4NTY0NzQsImFzc2V0X2FnZV9kYXlzIjoxMjksInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoyMiwiYml0cmF0ZSI6MTM3OTEzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1bJBZgMv0gqko5BmNlhU_6uxFEcPDKJMb4yZobFZ3X3w&amp;oe=69DC5283</BaseURL><SegmentBase indexRange=\"833-924\" timescale=\"48000\" FBMinimumPrefetchRange=\"925-2173\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"925-44125\" FBFirstSegmentRange=\"925-84601\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84602-169375\" FBPrefetchSegmentRange=\"925-84601\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "has_audio": true,
        "like_count": 135429,
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
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo2LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiQTdlSGZxbHJXNnZjYjdUWW5Ceko2WV8zNzc2ODMyODk4MjgwMjI4MTQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2Mzk2NjAyN3wzNzc2ODMyODk4MjgwMjI4MTQ1fDc4NzEzMnxjMmFhMmUxNTczZDY5OTJiMTZiMWRmMjljY2UyYjNhZDI0ZDg5NmRiZWU4NzIyMjhhZmFmMzAzYzU0MWU3MDZlIn0sInNpZ25hdHVyZSI6IiJ9",
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
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT22.314667S\" FBManifestTimestamp=\"1775663965\" FBManifestIdentifier=\"Frrts50NKRaI0eK/0NmNAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT22.314667S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"874552045098052a\" bandwidth=\"46857\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46857\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m86/AQPkB7GmtjggjHEJa-kd2XK21HSs5MPOBh8Kn_V_b6gCkSbQo9RxM5qstTSXAhy-_70SQiuAW02OQtBnYlPkvoo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=ZSfr4AA8_vgQ7kNvwEYtPxo&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6LTEsImNsaWVudF9uYW1lIjoidW5rbm93biIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJiaXRyYXRlIjo0NzIxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=VDX5WIvpilVs4LlvGqzswQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0JW2QgoujC9vMmX_gLnn7L4fJUgjefm6bCZmTceYXPPw&amp;oe=69D859DB</BaseURL><SegmentBase indexRange=\"824-999\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
              "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=1&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwFGssZp&_nc_oc=AdrgM5kcz86WA8k_NPri-CNqebYRKeUl_S1jsVD7-GFxjeJ7F46tZCSrgKYOr7Acwwk&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af2hfE6wsojZvkAE7M-ug8hkacyje9tmUkAsnfDHmQYCsQ&oe=69DC51E9",
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
            "progressive_download_url": "https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m69/AQNUQxQiFbTUd-NpZIcRNmMnc9S2fKRmilHMmVeP5Hg1uelz4pX6ycUwiSbbH3ZIlgtpB73IB_VLHDvX8YgT4zPM.mp4?strext=1&_nc_cat=104&_nc_sid=8bf8fe&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_ohc=NAtNUSzzeGkQ7kNvwE2MaPD&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2TCN5RzSJ6iWGXnloCFWeujYIdlbsY5jDZLm0EcFDELQ&oe=69DC5BEE",
            "should_mute_audio": false,
            "time_created": 1764453634
          },
          "professional_clips_upsell_type": 0,
          "show_achievements": false
        },
        "collaborator_edit_eligibility": false,
        "number_of_qualities": 7,
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
            },
            {
              "id": "control_center",
              "show_icon": true,
              "text": "Manage content preferences"
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
        "video_codec": "av01.0.04M.08",
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
            "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=1&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwFGssZp&_nc_oc=AdrgM5kcz86WA8k_NPri-CNqebYRKeUl_S1jsVD7-GFxjeJ7F46tZCSrgKYOr7Acwwk&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af2hfE6wsojZvkAE7M-ug8hkacyje9tmUkAsnfDHmQYCsQ&oe=69DC51E9",
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
          "profile_pic_url": "https://scontent-fra3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=1&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwFGssZp&_nc_oc=AdrgM5kcz86WA8k_NPri-CNqebYRKeUl_S1jsVD7-GFxjeJ7F46tZCSrgKYOr7Acwwk&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af2hfE6wsojZvkAE7M-ug8hkacyje9tmUkAsnfDHmQYCsQ&oe=69DC51E9",
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
          "latest_reel_media": 1775659002,
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
          "url": "https://scontent-fra5-2.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFnDlpJ&_nc_oc=Adq8OjE-E2KCAcdyIpEbXKCUV5GXypxD6ONd3Dfr7qF4gHfYCVd5SA3HWCJ53dooSDc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af2Pv3pNUt2myiU6-eA47zvtG9kgb_lDjvmH6CPsMG-v4A&oe=69DC368F",
          "width": 640
        },
        "igtv_first_frame": {
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-fra5-2.cdninstagram.com/v/t51.71878-15/586669104_1216013000387548_1857633437886151276_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=KulqEiwimwIQ7kNvwFnDlpJ&_nc_oc=Adq8OjE-E2KCAcdyIpEbXKCUV5GXypxD6ONd3Dfr7qF4gHfYCVd5SA3HWCJ53dooSDc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af2Pv3pNUt2myiU6-eA47zvtG9kgb_lDjvmH6CPsMG-v4A&oe=69DC368F",
          "width": 640
        }
      },
      "candidates": [
        {
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwExc08O&_nc_oc=AdpGewr5QEJby3AiN2Ri18KaYIJmJGgFX1e0fx9ve2XNYKjyoBHyeTrCxz9G42HeOck&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=VDX5WIvpilVs4LlvGqzswQ&_nc_ss=7a3ba&oh=00_Af3aQ0pPyCbBNBRJ7VWBl3qCNRx_LHCesmrwLo3CxfkZNw&oe=69DC3E7E",
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
    "max_id": "GhbilITg1eCA6mgmjpOP3a1nFAI0AikIGAAaCDoGGQwA",
    "more_available": true
  },
  "status": "ok",
  "status_code": "200"
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-media){ target=_blank }
