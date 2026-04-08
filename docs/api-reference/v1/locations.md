# Location Endpoints

Get location info and media by location ID.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/location/by/id`](#get-v1locationbyid) | [`/v1/location/guides`](#get-v1locationguides) | [`/v1/location/medias/recent`](#get-v1locationmediasrecent) | [`/v1/location/medias/recent/chunk`](#get-v1locationmediasrecentchunk) | [`/v1/location/medias/top`](#get-v1locationmediastop) | [`/v1/location/medias/top/chunk`](#get-v1locationmediastopchunk) | [`/v1/location/search`](#get-v1locationsearch)

---

### GET /v1/location/by/id

Get location object by id. Returns a Location object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/by/id?id=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_by_id_v1(id="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/by/id",
        headers=headers,
        params={"id": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/by/id?id=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 213131048,
  "name": "Berlin, Germany",
  "phone": "",
  "website": "https://www.berlin.de/",
  "category": "Region",
  "hours": {
    "status": "",
    "current_status": "",
    "hours_today": "",
    "schedule": [],
    "is_open": false
  },
  "address": "",
  "city": "",
  "zip": "",
  "lng": null,
  "lat": null,
  "external_id": "111175118906315",
  "external_id_source": null
}
```

</details>

---

### GET /v1/location/guides

Get location guides. Returns location guide data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/guides?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_guides_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/guides",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/guides?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/location/medias/recent

Get location recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/recent?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_recent_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/recent",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/recent?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870820823258908956",
    "id": "3870820823258908956_76902937953",
    "code": "DW36we_iEkc",
    "taken_at": "2026-04-08T14:17:33Z",
    "taken_at_ts": 1775657853,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661578946_17876219574561954_7451617886524604299_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDgyMDgyMzI1ODkwODk1NjE3ODc2MjE5NTY4NTYxOTU0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIyNjh4NDAzMi5zZHIuQzMifQ%3D%3D&_nc_ohc=Ox1ygxfteusQ7kNvwGIM-8a&_nc_oc=AdqkvYnLvmOrX-nHpih8O8Tm6NY5anMBo9gQRpuEVeejvZ5xgR-u643QDd98z4ShxR8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&oh=00_Af3-H9LaOCkAPxIC1sMVwZXrZZfeI7ASQoZE6xZySGkHBw&oe=69DC2AFC",
    "location": {
      "pk": 213131048,
      "name": "Berlin, Germany",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "",
      "city": "",
      "zip": null,
      "lng": 13.401251,
      "lat": 52.518391,
      "external_id": "111175118906315",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "76902937953",
      "id": "76902937953",
      "username": "bocado.berlin",
      "full_name": "BOCADO Berlin",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658045171_17874004323561954_4837055008297918770_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NTUuYzEifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gExvAHvk5K4uYlM41E8Ft1wqfb6wzPsR0_k1ZFnfvuVzxbdwGFKeAG7TStS9pMT9wU&_nc_ohc=nen4APJ7mY0Q7kNvwGN9Ce7&_nc_gid=h9sYNygiEtUZBvWbxira1A&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GPP4OCficWvuT4A-ADIhn-jmqyBDbmNDAQAB1501500j-ccb7-5&oh=00_Af2sxDC8k9_iMaQSA66UrK3oSR-iDzjyuk6CRAEy1XWspQ&oe=69DC4343&_nc_sid=99328a",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 0,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "#restaurant #bocado #tapas #cocktails #berlin",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFKH-zZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2J_dF5LXNe0s9PyNzgE8ikjBwXqy_bxDewoxzHmO2TNQ&oe=69D84485",
    "view_count": 0,
    "video_duration": 11.654000282287598,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          18172,
          36344
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661578946_17876219574561954_7451617886524604299_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDgyMDgyMzI1ODkwODk1NjE3ODc2MjE5NTY4NTYxOTU0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIyNjh4NDAzMi5zZHIuQzMifQ%3D%3D&_nc_ohc=Ox1ygxfteusQ7kNvwGIM-8a&_nc_oc=AdqkvYnLvmOrX-nHpih8O8Tm6NY5anMBo9gQRpuEVeejvZ5xgR-u643QDd98z4ShxR8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&oh=00_Af3-H9LaOCkAPxIC1sMVwZXrZZfeI7ASQoZE6xZySGkHBw&oe=69DC2AFC",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1289954,
        "height": 1280,
        "id": "1712432703502038v",
        "type": 101,
        "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFKH-zZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2J_dF5LXNe0s9PyNzgE8ikjBwXqy_bxDewoxzHmO2TNQ&oe=69D84485",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1289954,
        "height": 1280,
        "id": "1712432703502038v",
        "type": 102,
        "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFKH-zZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2J_dF5LXNe0s9PyNzgE8ikjBwXqy_bxDewoxzHmO2TNQ&oe=69D84485",
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
        "best_audio_cluster_id": "870702934995012"
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
      "music_canonical_id": "18474847939061741",
      "music_info": {
        "music_canonical_id": 18474847939061741,
        "music_asset_info": {
          "allows_saving": false,
          "artist_id": "380520149183744",
          "audio_asset_id": "488157347220983",
          "audio_cluster_id": "870702934995012",
          "cover_artwork_thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/473008528_90029471839766_6388842261549273719_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=tlvG4X34VywQ7kNvwFKr9DW&_nc_oc=AdqqSxQrm823I_ljIOfT7ezj0mTVN3RwVoboxz5guYFpqUjfOT-AiksVnby8YnoEvZc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a39b&oh=00_Af0umjElg3h1c1vNr7u14_2hLRlA58bltqqzhqh7VxtDHw&oe=69DC3071",
          "cover_artwork_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/473008528_90029471839766_6388842261549273719_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=tlvG4X34VywQ7kNvwFKr9DW&_nc_oc=AdqqSxQrm823I_ljIOfT7ezj0mTVN3RwVoboxz5guYFpqUjfOT-AiksVnby8YnoEvZc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a39b&oh=00_Af0umjElg3h1c1vNr7u14_2hLRlA58bltqqzhqh7VxtDHw&oe=69DC3071",
          "dark_message": null,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT213.010727S\"><Period id=\"0\" duration=\"PT213.010727S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1393418698431403a\" bandwidth=\"70811\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"70811\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKkn5gTWGxOOuux5ke4njnm0hKhlGZPEFYkuKNMneJMg2zCYOOvX0dh6iUpa1ni0h4MPx1lUdIeA6HzEMOXkV0.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Izemcy3Vz3AQ7kNvwHn4h5p&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo2NDU3NDUxNDc3ODU5MjQsImFzc2V0X2FnZV9kYXlzIjo0NTksInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMTMsImJpdHJhdGUiOjcwODkxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af08pf-diFTf1LLuwZVEcVYLBiZooj9n_y0YHlwU9QD7Tw&amp;oe=69DC277C</BaseURL><SegmentBase indexRange=\"824-2139\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "display_artist": "Bad Bunny",
          "duration_in_ms": 213010,
          "fast_start_progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKkn5gTWGxOOuux5ke4njnm0hKhlGZPEFYkuKNMneJMg2zCYOOvX0dh6iUpa1ni0h4MPx1lUdIeA6HzEMOXkV0.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Izemcy3Vz3AQ7kNvwHn4h5p&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo2NDU3NDUxNDc3ODU5MjQsImFzc2V0X2FnZV9kYXlzIjo0NTksInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=1dbfbcdccdcec8c3&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQ05oQWlBYTVUX0JXY3NKQUJGQ2tqTXNCd0pqYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmiMuxoqjTpQIVAigCQzMsF0BqoFHrhR64GBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af2BEV4qxzm0y1CrZv2pP_r_sHEkLUh1JyRqDEkA15M-tQ&oe=69DC277C",
          "has_lyrics": true,
          "highlight_start_times_in_ms": [
            40000,
            67500
          ],
          "id": "488157347220983",
          "ig_username": "badbunnypr",
          "is_eligible_for_audio_effects": true,
          "is_eligible_for_vinyl_sticker": true,
          "is_explicit": true,
          "licensed_music_subtype": "DEFAULT",
          "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKkn5gTWGxOOuux5ke4njnm0hKhlGZPEFYkuKNMneJMg2zCYOOvX0dh6iUpa1ni0h4MPx1lUdIeA6HzEMOXkV0.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Izemcy3Vz3AQ7kNvwHn4h5p&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo2NDU3NDUxNDc3ODU5MjQsImFzc2V0X2FnZV9kYXlzIjo0NTksInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=1dbfbcdccdcec8c3&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQ05oQWlBYTVUX0JXY3NKQUJGQ2tqTXNCd0pqYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmiMuxoqjTpQIVAigCQzMsF0BqoFHrhR64GBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af2BEV4qxzm0y1CrZv2pP_r_sHEkLUh1JyRqDEkA15M-tQ&oe=69DC277C",
          "reactive_audio_download_url": null,
          "sanitized_title": null,
          "song_monetization_info": null,
          "subtitle": "",
          "title": "LA MuDANZA",
          "web_30s_preview_download_url": null,
          "lyrics": null,
          "spotify_track_metadata": null,
          "related_audios": null
        },
        "music_consumption_info": {
          "allow_media_creation_with_music": true,
          "music_creation_restriction_reason": null,
          "audio_asset_start_time_in_ms": 41000,
          "derived_content_start_time_in_composition_in_ms": null,
          "contains_lyrics": null,
          "derived_content_id": null,
          "display_labels": null,
          "formatted_clips_media_count": null,
          "is_bookmarked": false,
          "is_trending_in_clips": true,
          "overlap_duration_in_ms": 11000,
          "placeholder_profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gExvAHvk5K4uYlM41E8Ft1wqfb6wzPsR0_k1ZFnfvuVzxbdwGFKeAG7TStS9pMT9wU&_nc_ohc=HMeNVRbt-xsQ7kNvwHX1RXS&_nc_gid=h9sYNygiEtUZBvWbxira1A&edm=AKmAybEAAAAA&ccb=7-5&oh=00_Af2urxitfzzCf795-lk0uD7rl9-36Foa0vMnhypLoQeyow&oe=69DC253D&_nc_sid=99328a",
          "should_allow_music_editing": false,
          "should_mute_audio": false,
          "should_mute_audio_reason": "",
          "should_mute_audio_reason_type": null,
          "should_render_soundwave": false,
          "trend_rank": null,
          "previous_trend_rank": null,
          "ig_artist": {
            "strong_id__": "197260775",
            "pk": 197260775,
            "pk_id": "197260775",
            "id": "197260775",
            "username": "badbunnypr",
            "full_name": "Benito Antonio",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3773136183001949034_197260775",
            "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/588090177_18565248739012776_8615733116563517479_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gExvAHvk5K4uYlM41E8Ft1wqfb6wzPsR0_k1ZFnfvuVzxbdwGFKeAG7TStS9pMT9wU&_nc_ohc=KOZidhOeCukQ7kNvwE8u8PF&_nc_gid=h9sYNygiEtUZBvWbxira1A&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GEGLDSOocEHQ-vRBACdwVhSfO5F3bmNDAQAB1501500j-ccb7-5&oh=00_Af12MeStBbMM3b5m1NVbNQu6tfwwGtoWj7F8AucuV93UoA&oe=69DC4696&_nc_sid=99328a"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT11.654966S\" FBManifestTimestamp=\"1775657869\" FBManifestIdentifier=\"FpqOs50NGBBpZ19kYXNoX2Jhc2VsaW5lGVau/cn9wPWlA6TExNa+tsIDhv+tifbN0gTIndLR/42fBazb8+/Z3IoGIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT11.654966S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.4\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1712432703502038v\" bandwidth=\"1220533\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"1774859\" FBPlaybackResolutionMos=\"0:100,360:95.6,480:93.8,720:87.9,1080:78.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.64,480:97.8,720:95.9,1080:92.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=RuvfyKeoOqoQ7kNvwFKH-zZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3NjIxOTQ3MjU2MTk1NCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMSwiYml0cmF0ZSI6MTIyMDUzMywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3eDnbUsfuohyErIWyGIURN9SDDAJplN_vQffGrVnPX1A&amp;oe=69D84485</BaseURL><SegmentBase indexRange=\"892-959\" timescale=\"15360\" FBMinimumPrefetchRange=\"960-73718\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"960-353780\" FBFirstSegmentRange=\"960-741164\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"741165-1432907\" FBPrefetchSegmentRange=\"960-741164\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-891\"/></SegmentBase></Representation><Representation id=\"927807556894551v\" bandwidth=\"293879\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"427350\" FBPlaybackResolutionMos=\"0:100,360:71.4,480:66.2,720:56.5,1080:45.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86,480:81.2,720:71.7,1080:60.3\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNJV-hGRMSjv_9V4sNiynjbYD03fr9I1hPLjHFc4ZidUqmhiU_615BoLIIsWqUFRolQzxXcP4fVUezD-0HI300lDaqhIgg5x3Ou3EE.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=H4OuwI7d0FkQ7kNvwEXMCDZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3NjIxOTQ3MjU2MTk1NCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMSwiYml0cmF0ZSI6MjkzODc5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3B_Izz4J8meZKCaMIXInmLMVkG0DktxNu3HpftCYr0sA&amp;oe=69D84DBF</BaseURL><SegmentBase indexRange=\"887-954\" timescale=\"15360\" FBMinimumPrefetchRange=\"955-25777\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"955-96590\" FBFirstSegmentRange=\"955-193468\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"193469-349904\" FBPrefetchSegmentRange=\"955-193468\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-886\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1307558511230915a\" bandwidth=\"40146\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40146\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"59392\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNOsmon5Ktr4dQy5UcDcODkMqaDqVBRARyLlIjSuWo5V_8xJnF-zZbhwwpB8cdGYqfQJwztW9UgS0WdMXqLPnPAyS7nk_uhMimZQW4.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=RT-LncbrN1wQ7kNvwF2ihlG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc2MjE5NDcyNTYxOTU0LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjExLCJiaXRyYXRlIjo0MDc2NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0eCL5v7HxOf5O1DgjMPZ7mgwMjZXbja2WGDqSKDBrgZA&amp;oe=69DC4193</BaseURL><SegmentBase indexRange=\"837-904\" timescale=\"44100\" FBMinimumPrefetchRange=\"905-2025\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"905-14593\" FBFirstSegmentRange=\"905-27436\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"27437-49800\" FBPrefetchSegmentRange=\"905-27436\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"990496590172434a\" bandwidth=\"73859\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"73859\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"108509\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNaCQJ0xskQCQISxFdmz1DqEvD9QNZHWHoG0_7KVyPP06BygZErht4YcUllcS2IKXJW6L486TX2_swSKuepT3UMJsYMyEOVsBxnsas.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=TnjOu5W8gUsQ7kNvwF1hnE6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc2MjE5NDcyNTYxOTU0LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjExLCJiaXRyYXRlIjo3NDQ4MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0hRAtccohb1ym0r_I3uKQZky9ERaYXjHGbx07B77Inkw&amp;oe=69DC4557</BaseURL><SegmentBase indexRange=\"838-905\" timescale=\"44100\" FBMinimumPrefetchRange=\"906-2820\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-27819\" FBFirstSegmentRange=\"906-51485\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"51486-92119\" FBPrefetchSegmentRange=\"906-51485\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1475785074034532a\" bandwidth=\"112400\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"112400\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"164653\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNP6rQKXxTZqxWn234KEcr_JrnIJCnW6wtuOGX4rUd1QC6hJHztBRVbFFJq-83-YM8M3L4Xkn5V7ZAByLkwkUleJBGnhIsyNHnO4I8.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=RAaEcZZ4iwkQ7kNvwEOtVSk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc2MjE5NDcyNTYxOTU0LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjExLCJiaXRyYXRlIjoxMTMwMTgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3l1Za3eZ_5N2T5kUL2MIsod5ErMzaz8xNxNzVaIcYNEQ&amp;oe=69DC51DD</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2514\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-38468\" FBFirstSegmentRange=\"901-74655\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"74656-140879\" FBPrefetchSegmentRange=\"901-74655\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870819449918247169",
    "id": "3870819449918247169_7960577209",
    "code": "DW36cf-DNEB",
    "taken_at": "2026-04-08T14:17:13Z",
    "taken_at_ts": 1775657833,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/657349280_2914521065558363_6663566046519062117_n.jpg?stp=dst-jpegr_e15_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxOTQ0OTkxODI0NzE2OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2Lmhkci5DMyJ9&_nc_ohc=dJlRy_7EhOgQ7kNvwEBbq2m&_nc_oc=AdpRTZ2se57n619vTDQmoJPzi6Ed_JuVAvHsfJX9XKJt2VvzmfY20wwBkpt_p9z8TnQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&oh=00_Af15330VWT2iR5sjAmAbW54z4-oJrpNKjI7_36hYuvlFDw&oe=69DC3B83",
    "location": {
      "pk": 213131048,
      "name": "Berlin, Germany",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "",
      "city": "",
      "zip": null,
      "lng": 13.401251,
      "lat": 52.518391,
      "external_id": "111175118906315",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "7960577209",
      "id": "7960577209",
      "username": "talyadinguitar",
      "full_name": "Tal Yadin",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/550287288_18291333835265210_8102525914412951321_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gExvAHvk5K4uYlM41E8Ft1wqfb6wzPsR0_k1ZFnfvuVzxbdwGFKeAG7TStS9pMT9wU&_nc_ohc=T2MfbvF6g5AQ7kNvwHZnAba&_nc_gid=h9sYNygiEtUZBvWbxira1A&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GLi3zCC6FLgH3-tAABkn_99j9HFwbmNDAQAB1501500j-ccb7-5&oh=00_Af0ud71LZTAo7u2L5HJVAe2vuf5jD9G_ibCZmdKwCwrQGw&oe=69DC2A3D&_nc_sid=99328a",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 0,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Cycle Of Seven is 1 year old 🔘\nCome celebrate with us next Wednesday (15.4) at @orangerie_nk",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQP8fgU3CrRVgs9CEcvogRw2N6R0SOMsw6JB0XwCdQw8xgz1qLH_OBENqHJdLIhSpOVL9PtHrNAJ6nxq9alaX4nzWLxTysbEvBgf0KM.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ASumlRcQvJMQ7kNvwExHK1d&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMTc2Nzk1NTYyNjUyMTAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=2dc8f710fc114ab4&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MTQwNzRFRkY0NjA5MTRFNjhCN0MwM0M4QzEwQjA4Nl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzg1NEM2QzYyMjUzMkQzQUM0OUE1Q0YxREVERjlGQTgxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACb0k_zwo_WJQRUCKAJDMywXQFDGZmZmZmYYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af35KQQiaCmjO00qwAoJUqAgosWqF3Q7zSrsvN5Nyk1uFw&oe=69D844E2",
    "view_count": 0,
    "video_duration": 67.10399627685547,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          11933,
          23866
        ],
        "height": 1136,
        "scans_profile": "e15",
        "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/657349280_2914521065558363_6663566046519062117_n.jpg?stp=dst-jpegr_e15_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxOTQ0OTkxODI0NzE2OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2Lmhkci5DMyJ9&_nc_ohc=dJlRy_7EhOgQ7kNvwEBbq2m&_nc_oc=AdpRTZ2se57n619vTDQmoJPzi6Ed_JuVAvHsfJX9XKJt2VvzmfY20wwBkpt_p9z8TnQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=-1&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&oh=00_Af15330VWT2iR5sjAmAbW54z4-oJrpNKjI7_36hYuvlFDw&oe=69DC3B83",
        "width": 640,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 970935,
        "height": 1280,
        "id": "904884142506930v",
        "type": 101,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQP8fgU3CrRVgs9CEcvogRw2N6R0SOMsw6JB0XwCdQw8xgz1qLH_OBENqHJdLIhSpOVL9PtHrNAJ6nxq9alaX4nzWLxTysbEvBgf0KM.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ASumlRcQvJMQ7kNvwExHK1d&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMTc2Nzk1NTYyNjUyMTAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=2dc8f710fc114ab4&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MTQwNzRFRkY0NjA5MTRFNjhCN0MwM0M4QzEwQjA4Nl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzg1NEM2QzYyMjUzMkQzQUM0OUE1Q0YxREVERjlGQTgxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACb0k_zwo_WJQRUCKAJDMywXQFDGZmZmZmYYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af35KQQiaCmjO00qwAoJUqAgosWqF3Q7zSrsvN5Nyk1uFw&oe=69D844E2",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 970935,
        "height": 1280,
        "id": "904884142506930v",
        "type": 102,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQP8fgU3CrRVgs9CEcvogRw2N6R0SOMsw6JB0XwCdQw8xgz1qLH_OBENqHJdLIhSpOVL9PtHrNAJ6nxq9alaX4nzWLxTysbEvBgf0KM.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ASumlRcQvJMQ7kNvwExHK1d&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMTc2Nzk1NTYyNjUyMTAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=2dc8f710fc114ab4&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MTQwNzRFRkY0NjA5MTRFNjhCN0MwM0M4QzEwQjA4Nl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzg1NEM2QzYyMjUzMkQzQUM0OUE1Q0YxREVERjlGQTgxX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACb0k_zwo_WJQRUCKAJDMywXQFDGZmZmZmYYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af35KQQiaCmjO00qwAoJUqAgosWqF3Q7zSrsvN5Nyk1uFw&oe=69D844E2",
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
        "best_audio_cluster_id": "3414292472063098"
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
      "music_canonical_id": "18520296169074383",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26409311022054902,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": false,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT67.104218S\" FBManifestTimestamp=\"1775657869\" FBManifestIdentifier=\"FpqOs50NKRb4+4LggsjTCiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT67.104218S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2998506017021692a\" bandwidth=\"71866\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71866\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m78/AQMOCabzhdFlPMksoGhmk_RFQ8SiAbrVG5Wrf3Pt4aEvg4BXmZtwqV3GQowmZjACqAvqwFEMlh4C8mQYFn_TKuXVwMdQK-_9lG26ZyE.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=LTmYxUPRIJYQ7kNvwGONtaB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE4MzE3Njc5NTU2MjY1MjEwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjY3LCJiaXRyYXRlIjo3MjAxNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0kRtnJ8gOcOk2zhz050qjUYLcJb3uUnidwXFOSzqf6zQ&amp;oe=69D8450D</BaseURL><SegmentBase indexRange=\"824-1263\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 67100,
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
        "oa_owner_is_music_artist": true,
        "original_audio_subtype": "default",
        "original_audio_title": "Original audio",
        "original_media_id": 3870819449918247169,
        "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQMVHVxaNM2iLOQ_k1LEG1FPnbGWPuwMXq3DxumHAVWuCCMjURfnTC2Ef1jcD4PN5FbvZ-W8p6SVdRjHrsBJ8AKB.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=hJqc7_h6pjkQ7kNvwEGEkp9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTgzMTc2Nzk1NTYyNjUyMTAsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af29R3iJNNd5EwoWU5NAfF622jFYItwh5chjESKOgDJwjg&oe=69DC2CAF",
        "should_mute_audio": false,
        "time_created": 1775657835,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "7960577209",
          "pk": 7960577209,
          "pk_id": "7960577209",
          "id": "7960577209",
          "username": "talyadinguitar",
          "full_name": "Tal Yadin",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3724442458345196948_7960577209",
          "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/550287288_18291333835265210_8102525914412951321_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gExvAHvk5K4uYlM41E8Ft1wqfb6wzPsR0_k1ZFnfvuVzxbdwGFKeAG7TStS9pMT9wU&_nc_ohc=T2MfbvF6g5AQ7kNvwHZnAba&_nc_gid=h9sYNygiEtUZBvWbxira1A&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GLi3zCC6FLgH3-tAABkn_99j9HFwbmNDAQAB1501500j-ccb7-5&oh=00_Af0ud71LZTAo7u2L5HJVAe2vuf5jD9G_ibCZmdKwCwrQGw&oe=69DC2A3D&_nc_sid=99328a"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT67.104218S\" FBManifestTimestamp=\"1775657869\" FBManifestIdentifier=\"FpqOs50NGBBpZ19kYXNoX2Jhc2VsaW5lGVb+9LSj6biRA+SOhJ6Yv5sDqPvHo8WSvQOmnPD7oPmiBbaU5o+slrMHIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT67.104218S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:83\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"904884142506930v\" bandwidth=\"898920\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"7539695\" FBPlaybackResolutionMos=\"0:100,360:90.5,480:85,720:78.1,1080:73.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.6,480:95,720:92.1,1080:88.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQP8fgU3CrRVgs9CEcvogRw2N6R0SOMsw6JB0XwCdQw8xgz1qLH_OBENqHJdLIhSpOVL9PtHrNAJ6nxq9alaX4nzWLxTysbEvBgf0KM.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=ASumlRcQvJMQ7kNvwExHK1d&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODMxNzY3OTU1NjI2NTIxMCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2NywiYml0cmF0ZSI6ODk4OTIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1ADUk66mhkDdGrmvx5V4UPC-1XG4mvXZlMZUXlaJL8sA&amp;oe=69D844E2</BaseURL><SegmentBase indexRange=\"892-1091\" timescale=\"15360\" FBMinimumPrefetchRange=\"1092-43363\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1092-266165\" FBFirstSegmentRange=\"1092-494386\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"494387-989616\" FBPrefetchSegmentRange=\"1092-494386\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-891\"/></SegmentBase></Representation><Representation id=\"882784528145727v\" bandwidth=\"201814\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"1692718\" FBPlaybackResolutionMos=\"0:100,360:69.9,480:64.8,720:57.1,1080:48\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:84.7,480:80,720:72.3,1080:62.9\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPRlJ7iu00meHwxlasp3GRZl6YkFm2wi9NyM6Wl5y09uOWCpMusZSNjw6DZWHfYGFMuGamYehW0-cZHA760442Elq0GljPZ99dugjg.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=VUSvcGi3tPkQ7kNvwEdvqUT&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODMxNzY3OTU1NjI2NTIxMCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2NywiYml0cmF0ZSI6MjAxODE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Xwqph8iPPIq7ufy4beSryGlZRtUZdLVBtoIxuLn5mSQ&amp;oe=69D83D09</BaseURL><SegmentBase indexRange=\"887-1086\" timescale=\"15360\" FBMinimumPrefetchRange=\"1087-15925\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1087-63184\" FBFirstSegmentRange=\"1087-111839\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"111840-221781\" FBPrefetchSegmentRange=\"1087-111839\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-886\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2082858902275355a\" bandwidth=\"31286\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"31286\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"263463\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNE7a4pKjrHtvurvURkQxRWB77xTpPH1NYl4Ehm6CfjCuKUMwceQc3lk87gbXdi0_mSKD3WvSJMNumbMgLd6FfmsI017wkmqU_YIBo.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=eGnXdX_gLJgQ7kNvwHxPM_d&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MzE3Njc5NTU2MjY1MjEwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjY3LCJiaXRyYXRlIjozMTQwOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0mqemdVaCzLiNZhFHRFYwM76UJ00qAF1JvcISJzKqMZw&amp;oe=69DC4204</BaseURL><SegmentBase indexRange=\"837-1036\" timescale=\"44100\" FBMinimumPrefetchRange=\"1037-2103\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1037-10854\" FBFirstSegmentRange=\"1037-19581\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"19582-38300\" FBPrefetchSegmentRange=\"1037-19581\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1484224863274771a\" bandwidth=\"59214\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"59214\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"497723\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNaPqgjBOzhrmZ5zrmZeq1u9wO5Pkq2IW5lH1AznSqPCzcS8vn-L4CJEXufmuPOLnaROGuCTkCA_laubKdv4inpnBr-hYDVEzsxAl0.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=ItZzK_yh5I4Q7kNvwEUVA6W&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MzE3Njc5NTU2MjY1MjEwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjY3LCJiaXRyYXRlIjo1OTMzNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1gi6eoXLzaAKTfHEGkKg_Oeq432boT8lN0WFF1DZhuig&amp;oe=69DC1F5E</BaseURL><SegmentBase indexRange=\"838-1037\" timescale=\"44100\" FBMinimumPrefetchRange=\"1038-2862\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1038-19092\" FBFirstSegmentRange=\"1038-35576\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"35577-72014\" FBPrefetchSegmentRange=\"1038-35576\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"978883884678868a\" bandwidth=\"82370\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"82370\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"691954\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMIR4KestShPAc1tYbrQX4v0bx0O_QsFjt-ycj5k947vKbFRAWDOWj6BiYBmib9pOmjD1ypVLPy2zPC-4LFoSIuxKWUXAIDoD7YBJ4.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=E-MbDCycPFgQ7kNvwHWsdPM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMxLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MzE3Njc5NTU2MjY1MjEwLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjY3LCJiaXRyYXRlIjo4MjQ5MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=h9sYNygiEtUZBvWbxira1A&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af19_C5l5f9tZ46mVZV9BYW4FK35VGV3DMTH7t7qBh1ifQ&amp;oe=69DC2ACB</BaseURL><SegmentBase indexRange=\"833-1032\" timescale=\"44100\" FBMinimumPrefetchRange=\"1033-2452\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1033-26489\" FBFirstSegmentRange=\"1033-50333\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"50334-100082\" FBPrefetchSegmentRange=\"1033-50333\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  }
]
```

</details>

---

### GET /v1/location/medias/recent/chunk

Get location chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/recent/chunk?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_recent_chunk_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/recent/chunk",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/recent/chunk?location_pk=213131048",
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
      "pk": "3870820134504117611",
      "id": "3870820134504117611_7556662934",
      "code": "DW36mdijDVr",
      "taken_at": "2026-04-08T14:17:50Z",
      "taken_at_ts": 1775657870,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661225089_1448822322898568_5834653775145915082_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=Mzg3MDgyMDEzNDUwNDExNzYxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=meZzUfZ4sgQQ7kNvwHCQbQG&_nc_oc=Adqx9Gu6VmDRJgF-f1sv6aZKRtPRi6h2dyVpVxXzfC-7Q-1d1wgUQ4YK8Vn5PQDZkUc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&oh=00_Af0UATAXI4d48ZtnFjKXmmAX8OOc2_gKmu6n62zPz95IjA&oe=69DC2177",
      "location": {
        "pk": 213131048,
        "name": "Berlin, Germany",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 13.401251,
        "lat": 52.518391,
        "external_id": "111175118906315",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "7556662934",
        "id": "7556662934",
        "username": "sofia_deol",
        "full_name": "Sofia de Oliveira🦋| NPC Bikini",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/489045697_516419634670208_8361051641537387041_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDEyLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFnOOW94S78cIE8EXJgDwdDEFoscmb5-sBJLaMACCCSXigV-cN0GuL81ha--C8P0Jo&_nc_ohc=P8cs1coqh-4Q7kNvwFQCejt&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GME_Jh2AKuFQrtUBACFaiFIrbAh0bkULAAAB1501500j-ccb7-5&oh=00_Af3nH5fNRVdyoPUPLe4cfcHAGj-_lmISxA_5si75xNKI-A&oe=69DC287E&_nc_sid=99328a",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 0,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Be honest… is this “too much”? 👀\n.\n.\n.\n#gymgirl #stronggirl #selfconfidence #fitnessreel #gymmotivation",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPSLxUdVHCpDSUBUOPmG6gAzNxj1sPH2x1-Vurx7OilISocDthudy2lfqkS8gzYlsQsIJCySs-LIiv1tTtZuGPRwwMkgeGer1ArgQA.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=EQKsO4OWTkEQ7kNvwEmksB0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMjk0MTM5NDUyNTQ5MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=f09d518ab84d6f95&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNzQzODAwOEQzNDQ2MTM5OEY2M0JGQTg3RUE4RkE4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzVENDVBRjYwNDU1MjdFOEYzRDZBMjA5M0M5MEFFNUFCX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaukK_yp6CPQRUCKAJDMywXQBbul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2aAZ9KYdZqGtgzG6y2M4Kv__t_L9SEmA7eRygRvWugtA&oe=69D85BD1",
      "view_count": 0,
      "video_duration": 5.757999897003174,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            4950,
            9900
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661225089_1448822322898568_5834653775145915082_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=Mzg3MDgyMDEzNDUwNDExNzYxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=meZzUfZ4sgQQ7kNvwHCQbQG&_nc_oc=Adqx9Gu6VmDRJgF-f1sv6aZKRtPRi6h2dyVpVxXzfC-7Q-1d1wgUQ4YK8Vn5PQDZkUc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&oh=00_Af0UATAXI4d48ZtnFjKXmmAX8OOc2_gKmu6n62zPz95IjA&oe=69DC2177",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1112289,
          "height": 1280,
          "id": "820219617212334v",
          "type": 101,
          "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPSLxUdVHCpDSUBUOPmG6gAzNxj1sPH2x1-Vurx7OilISocDthudy2lfqkS8gzYlsQsIJCySs-LIiv1tTtZuGPRwwMkgeGer1ArgQA.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=EQKsO4OWTkEQ7kNvwEmksB0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMjk0MTM5NDUyNTQ5MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=f09d518ab84d6f95&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNzQzODAwOEQzNDQ2MTM5OEY2M0JGQTg3RUE4RkE4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzVENDVBRjYwNDU1MjdFOEYzRDZBMjA5M0M5MEFFNUFCX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaukK_yp6CPQRUCKAJDMywXQBbul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2aAZ9KYdZqGtgzG6y2M4Kv__t_L9SEmA7eRygRvWugtA&oe=69D85BD1",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1112289,
          "height": 1280,
          "id": "820219617212334v",
          "type": 102,
          "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPSLxUdVHCpDSUBUOPmG6gAzNxj1sPH2x1-Vurx7OilISocDthudy2lfqkS8gzYlsQsIJCySs-LIiv1tTtZuGPRwwMkgeGer1ArgQA.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=EQKsO4OWTkEQ7kNvwEmksB0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMjk0MTM5NDUyNTQ5MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=f09d518ab84d6f95&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNzQzODAwOEQzNDQ2MTM5OEY2M0JGQTg3RUE4RkE4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzVENDVBRjYwNDU1MjdFOEYzRDZBMjA5M0M5MEFFNUFCX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaukK_yp6CPQRUCKAJDMywXQBbul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2aAZ9KYdZqGtgzG6y2M4Kv__t_L9SEmA7eRygRvWugtA&oe=69D85BD1",
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
          "best_audio_cluster_id": "750209444335687"
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
        "music_canonical_id": "18308258215072770",
        "music_info": {
          "music_canonical_id": 18308258215072770,
          "music_asset_info": {
            "allows_saving": false,
            "artist_id": "396005785206670",
            "audio_asset_id": "1251824759289308",
            "audio_cluster_id": "559790956066033",
            "cover_artwork_thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/651586661_71060857220724_645891713328695157_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=U8jMMHzn1JQQ7kNvwGbwJVw&_nc_oc=Adrn0AhBqjRWEsT3tINkBiy2htYE20kuctpqBzks6x4lZOJ5SpXLNGWUP23zUohnHPM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a39b&oh=00_Af3UUrzfAyUuw6-8Wbe8RYqLz03zlOTkkSGzlZorK5YLYA&oe=69DC4222",
            "cover_artwork_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/651586661_71060857220724_645891713328695157_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=U8jMMHzn1JQQ7kNvwGbwJVw&_nc_oc=Adrn0AhBqjRWEsT3tINkBiy2htYE20kuctpqBzks6x4lZOJ5SpXLNGWUP23zUohnHPM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a39b&oh=00_Af3UUrzfAyUuw6-8Wbe8RYqLz03zlOTkkSGzlZorK5YLYA&oe=69DC4222",
            "dark_message": null,
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT236.319641S\"><Period id=\"0\" duration=\"PT236.319641S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1866510470877112a\" bandwidth=\"70590\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"70590\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPbtGdCM3hhP7T8f_PhnEujMgpWhHW4noriJ5guAXDPcZissP0AWr17pCkuui1NoH2vjnGdWD1iGlbJ9cTBDadv.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=W8YvW8K6h1IQ7kNvwFOSq-z&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo1NjYyMzkyNjU5MTg0MTEsImFzc2V0X2FnZV9kYXlzIjo1NTUsInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMzYsImJpdHJhdGUiOjcwNjY3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2BV0UbucxUUQ6ajWAMqNtGM6990R4-sCNjSw3qg8dDsw&amp;oe=69DC3ADC</BaseURL><SegmentBase indexRange=\"824-2283\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "display_artist": "Narvent, VØJ",
            "duration_in_ms": 236319,
            "fast_start_progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPbtGdCM3hhP7T8f_PhnEujMgpWhHW4noriJ5guAXDPcZissP0AWr17pCkuui1NoH2vjnGdWD1iGlbJ9cTBDadv.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=W8YvW8K6h1IQ7kNvwFOSq-z&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo1NjYyMzkyNjU5MTg0MTEsImFzc2V0X2FnZV9kYXlzIjo1NTUsInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=72a858f9bc80a15f&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HSXhnTmlCNXgzY3ZsOEFDQURIS1hyQjhySHhGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmlrfspLu_gQIVAigCQzMsF0BtijU_fO2RGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af0J7q2s_ISVRrtIzljdyyP4vEUnlvJ5YAu5TL7dJoBdgA&oe=69DC3ADC",
            "has_lyrics": false,
            "highlight_start_times_in_ms": [
              170500,
              35000
            ],
            "id": "1251824759289308",
            "ig_username": "narventof",
            "is_eligible_for_audio_effects": false,
            "is_eligible_for_vinyl_sticker": true,
            "is_explicit": false,
            "licensed_music_subtype": "DEFAULT",
            "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPbtGdCM3hhP7T8f_PhnEujMgpWhHW4noriJ5guAXDPcZissP0AWr17pCkuui1NoH2vjnGdWD1iGlbJ9cTBDadv.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=W8YvW8K6h1IQ7kNvwFOSq-z&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo1NjYyMzkyNjU5MTg0MTEsImFzc2V0X2FnZV9kYXlzIjo1NTUsInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=72a858f9bc80a15f&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HSXhnTmlCNXgzY3ZsOEFDQURIS1hyQjhySHhGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmlrfspLu_gQIVAigCQzMsF0BtijU_fO2RGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af0J7q2s_ISVRrtIzljdyyP4vEUnlvJ5YAu5TL7dJoBdgA&oe=69DC3ADC",
            "reactive_audio_download_url": null,
            "sanitized_title": null,
            "song_monetization_info": null,
            "subtitle": "",
            "title": "Memory Reboot",
            "web_30s_preview_download_url": null,
            "lyrics": null,
            "spotify_track_metadata": null,
            "related_audios": null
          },
          "music_consumption_info": {
            "allow_media_creation_with_music": true,
            "music_creation_restriction_reason": null,
            "audio_asset_start_time_in_ms": 170157,
            "derived_content_start_time_in_composition_in_ms": 0,
            "contains_lyrics": null,
            "derived_content_id": null,
            "display_labels": null,
            "formatted_clips_media_count": null,
            "is_bookmarked": false,
            "is_trending_in_clips": false,
            "overlap_duration_in_ms": 90000,
            "placeholder_profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFnOOW94S78cIE8EXJgDwdDEFoscmb5-sBJLaMACCCSXigV-cN0GuL81ha--C8P0Jo&_nc_ohc=HMeNVRbt-xsQ7kNvwGL20nB&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&edm=AKmAybEAAAAA&ccb=7-5&oh=00_Af0fWJMvyX8IKuae0jkGbMqj97mmG8eoAzefUyzOssG_Hw&oe=69DC253D&_nc_sid=99328a",
            "should_allow_music_editing": false,
            "should_mute_audio": false,
            "should_mute_audio_reason": "",
            "should_mute_audio_reason_type": null,
            "should_render_soundwave": false,
            "trend_rank": null,
            "previous_trend_rank": null,
            "ig_artist": {
              "strong_id__": "48147689300",
              "pk": 48147689300,
              "pk_id": "48147689300",
              "id": "48147689300",
              "username": "narventof",
              "full_name": "Narvent",
              "is_private": false,
              "is_verified": false,
              "profile_pic_id": "3778702631704031583_48147689300",
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/589194210_18070786118601301_3499356059353589427_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gFnOOW94S78cIE8EXJgDwdDEFoscmb5-sBJLaMACCCSXigV-cN0GuL81ha--C8P0Jo&_nc_ohc=ejjuq9gCr88Q7kNvwHDR-oN&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GOJjHiNVSmnDSDNAALOmYazLNZAwbmNDAQAB1501500j-ccb7-5&oh=00_Af0aFjd-7aVfwQXjmAKbARPFeEhB2Ym8G1xEpYA950riuA&oe=69DC5087&_nc_sid=99328a"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT5.758549S\" FBManifestTimestamp=\"1775657881\" FBManifestIdentifier=\"FrKOs50NGBBpZ19kYXNoX2Jhc2VsaW5lGVbc3t+uiP/0ApaI44OdufkCsq3Rqfq20ASMz6PNpfLOBdbpkvzH3+xcIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT5.758549S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:80.3\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"820219617212334v\" bandwidth=\"1042011\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"746775\" FBPlaybackResolutionMos=\"0:100,360:93.8,480:90.5,720:83.8,1080:75.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.8,480:96.6,720:94.5,1080:90.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPSLxUdVHCpDSUBUOPmG6gAzNxj1sPH2x1-Vurx7OilISocDthudy2lfqkS8gzYlsQsIJCySs-LIiv1tTtZuGPRwwMkgeGer1ArgQA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=EQKsO4OWTkEQ7kNvwEmksB0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODMyOTQxMzk0NTI1NDkzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1LCJiaXRyYXRlIjoxMDQyMDExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2API_BmATo4M-2yHaU6Zl8E7FRDitUws1IGaWs42VFxQ&amp;oe=69D85BD1</BaseURL><SegmentBase indexRange=\"892-947\" timescale=\"15360\" FBMinimumPrefetchRange=\"948-50611\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"948-365698\" FBFirstSegmentRange=\"948-644500\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"644501-746774\" FBPrefetchSegmentRange=\"948-644500\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-891\"/></SegmentBase></Representation><Representation id=\"1580862249661382v\" bandwidth=\"256071\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"183518\" FBPlaybackResolutionMos=\"0:100,360:71.5,480:65.2,720:54.8,1080:43.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.1,480:80.3,720:69.9,1080:57.8\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQOlt1Grt09qxI2ZBHRHyR-7X6PjY22q-qFZX-vyfQuEELZ5KSaceUfvq5VKtS01C7y92q4RulyirE1kr294ejUGC66X5AiMkXH2aFA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=5NB2bAgxtrEQ7kNvwG82xUj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODMyOTQxMzk0NTI1NDkzNSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1LCJiaXRyYXRlIjoyNTYwNzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ftzlFjcBV6O_sZeoiO9WHkSvOu9nsY3AN2IAPEWxNFA&amp;oe=69D836F1</BaseURL><SegmentBase indexRange=\"887-942\" timescale=\"15360\" FBMinimumPrefetchRange=\"943-17433\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"943-95992\" FBFirstSegmentRange=\"943-160321\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"160322-183517\" FBPrefetchSegmentRange=\"943-160321\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-886\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"26134834116188779a\" bandwidth=\"46072\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46072\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"34056\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPLRrCyORkwOgx-E4HFGRmzjlRNw-EcpFQYTJIKjONJG26lhXHDLNS50wYphKNpWok-3ukaWDZGDl7t-P33inwCh8l5TTP14VLUDXc.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=SD4jHbxNQlEQ7kNvwESkS-n&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MzI5NDEzOTQ1MjU0OTM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUsImJpdHJhdGUiOjQ3MzExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0BzXa90Gxmv3UQLOY6WnngI_OLKLKFxmwnMKEiDa5t_w&amp;oe=69DC49AE</BaseURL><SegmentBase indexRange=\"837-892\" timescale=\"44100\" FBMinimumPrefetchRange=\"893-2158\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"893-14945\" FBFirstSegmentRange=\"893-28634\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"28635-34055\" FBPrefetchSegmentRange=\"893-28634\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"830014916157963a\" bandwidth=\"81910\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"81910\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"59854\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNMXN6lIoO1nJE4dthLOiip4XNKtXr6lpNs4fDtz34MatjkPaEvyaS8VJVtGLhaUAtegDSqIfvXixyD-r2SIIee0J3B2gQsvWAPEuw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=rm8P_Ty3qKEQ7kNvwE35aK8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MzI5NDEzOTQ1MjU0OTM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUsImJpdHJhdGUiOjgzMTUxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3L_jzeWK-5T1O3dSVUh1mgZ32xvoHoUWYKl4uHGdAYNg&amp;oe=69DC26C5</BaseURL><SegmentBase indexRange=\"838-893\" timescale=\"44100\" FBMinimumPrefetchRange=\"894-2856\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-26549\" FBFirstSegmentRange=\"894-50580\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"50581-59853\" FBPrefetchSegmentRange=\"894-50580\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1302765898443609a\" bandwidth=\"129812\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"129812\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"94330\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO1bRyRGA_3K7e6FGmphobEnmsXtnBQXS_B5Ws10rqFGJYw1gKJgHHPgktRcgu3hhvb9I2d21EMAw8RImb2vybW9h1WsAq7jPbu8AE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=ekoUXCeqMokQ7kNvwFMHDQs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MzI5NDEzOTQ1MjU0OTM1LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjUsImJpdHJhdGUiOjEzMTA0NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0JDVlpSAJ0zc49hLgvOidFZeyuRn9gyL8NmSv2Al8ceQ&amp;oe=69DC4F38</BaseURL><SegmentBase indexRange=\"833-888\" timescale=\"44100\" FBMinimumPrefetchRange=\"889-2553\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"889-39401\" FBFirstSegmentRange=\"889-80157\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"80158-94329\" FBPrefetchSegmentRange=\"889-80157\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870820823258908956",
      "id": "3870820823258908956_76902937953",
      "code": "DW36we_iEkc",
      "taken_at": "2026-04-08T14:17:33Z",
      "taken_at_ts": 1775657853,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661578946_17876219574561954_7451617886524604299_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDgyMDgyMzI1ODkwODk1NjE3ODc2MjE5NTY4NTYxOTU0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIyNjh4NDAzMi5zZHIuQzMifQ%3D%3D&_nc_ohc=Ox1ygxfteusQ7kNvwGQJ9Vb&_nc_oc=AdrATfB5pwVpS9NmYaMZ35r_0qixGJy_vyC1wLc3S4AEz-cTrAecxfdWT1Nshng0Db8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&oh=00_Af1I1wAlTfvoaGtz8V6ryFafwoSE1QKGq8GscQF-xXrj4w&oe=69DC2AFC",
      "location": {
        "pk": 213131048,
        "name": "Berlin, Germany",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 13.401251,
        "lat": 52.518391,
        "external_id": "111175118906315",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "76902937953",
        "id": "76902937953",
        "username": "bocado.berlin",
        "full_name": "BOCADO Berlin",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658045171_17874004323561954_4837055008297918770_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NTUuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gFnOOW94S78cIE8EXJgDwdDEFoscmb5-sBJLaMACCCSXigV-cN0GuL81ha--C8P0Jo&_nc_ohc=nen4APJ7mY0Q7kNvwEMw7ev&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GPP4OCficWvuT4A-ADIhn-jmqyBDbmNDAQAB1501500j-ccb7-5&oh=00_Af0sutj1Q1UrBbZWfWHP7nw4d_W_0BtuoHusmz1g0oE9GQ&oe=69DC4343&_nc_sid=99328a",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 1,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "#restaurant #bocado #tapas #cocktails #berlin",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFpHNem&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0NISplk7NYiO0k95GQJ6oXngqaZhu5iCK8LheqDNki8w&oe=69D84485",
      "view_count": 0,
      "video_duration": 11.654000282287598,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            18172,
            36344
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661578946_17876219574561954_7451617886524604299_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDgyMDgyMzI1ODkwODk1NjE3ODc2MjE5NTY4NTYxOTU0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIyNjh4NDAzMi5zZHIuQzMifQ%3D%3D&_nc_ohc=Ox1ygxfteusQ7kNvwGQJ9Vb&_nc_oc=AdrATfB5pwVpS9NmYaMZ35r_0qixGJy_vyC1wLc3S4AEz-cTrAecxfdWT1Nshng0Db8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&oh=00_Af1I1wAlTfvoaGtz8V6ryFafwoSE1QKGq8GscQF-xXrj4w&oe=69DC2AFC",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1289954,
          "height": 1280,
          "id": "1712432703502038v",
          "type": 101,
          "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFpHNem&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0NISplk7NYiO0k95GQJ6oXngqaZhu5iCK8LheqDNki8w&oe=69D84485",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1289954,
          "height": 1280,
          "id": "1712432703502038v",
          "type": 102,
          "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFpHNem&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0NISplk7NYiO0k95GQJ6oXngqaZhu5iCK8LheqDNki8w&oe=69D84485",
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
          "best_audio_cluster_id": "870702934995012"
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
        "music_canonical_id": "18474847939061741",
        "music_info": {
          "music_canonical_id": 18474847939061741,
          "music_asset_info": {
            "allows_saving": false,
            "artist_id": "380520149183744",
            "audio_asset_id": "488157347220983",
            "audio_cluster_id": "870702934995012",
            "cover_artwork_thumbnail_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/473008528_90029471839766_6388842261549273719_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=tlvG4X34VywQ7kNvwHj3aBX&_nc_oc=AdqWHYZLVXL5FszEbReMrVCu1WzPx8DuUgrRbxWguvNribL1t-8mKUW8GPamcA2fom8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a39b&oh=00_Af2IOcCFhRsF74cG2KK4TtiUaVlTw_ijNiikCyDl2qRzjw&oe=69DC3071",
            "cover_artwork_uri": "https://scontent-dfw6-1.cdninstagram.com/v/t39.30808-6/473008528_90029471839766_6388842261549273719_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=tlvG4X34VywQ7kNvwHj3aBX&_nc_oc=AdqWHYZLVXL5FszEbReMrVCu1WzPx8DuUgrRbxWguvNribL1t-8mKUW8GPamcA2fom8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a39b&oh=00_Af2IOcCFhRsF74cG2KK4TtiUaVlTw_ijNiikCyDl2qRzjw&oe=69DC3071",
            "dark_message": null,
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT213.010727S\"><Period id=\"0\" duration=\"PT213.010727S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1393418698431403a\" bandwidth=\"70811\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"70811\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKkn5gTWGxOOuux5ke4njnm0hKhlGZPEFYkuKNMneJMg2zCYOOvX0dh6iUpa1ni0h4MPx1lUdIeA6HzEMOXkV0.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Izemcy3Vz3AQ7kNvwFTZQGQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo2NDU3NDUxNDc3ODU5MjQsImFzc2V0X2FnZV9kYXlzIjo0NTksInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMTMsImJpdHJhdGUiOjcwODkxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0hlAJTWAQTNmXKRn-LZgukRW06zUMgs2wsRHbif9JI-g&amp;oe=69DC277C</BaseURL><SegmentBase indexRange=\"824-2139\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "display_artist": "Bad Bunny",
            "duration_in_ms": 213010,
            "fast_start_progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKkn5gTWGxOOuux5ke4njnm0hKhlGZPEFYkuKNMneJMg2zCYOOvX0dh6iUpa1ni0h4MPx1lUdIeA6HzEMOXkV0.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Izemcy3Vz3AQ7kNvwFTZQGQ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo2NDU3NDUxNDc3ODU5MjQsImFzc2V0X2FnZV9kYXlzIjo0NTksInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=1dbfbcdccdcec8c3&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQ05oQWlBYTVUX0JXY3NKQUJGQ2tqTXNCd0pqYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmiMuxoqjTpQIVAigCQzMsF0BqoFHrhR64GBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af1J1n7bttddHpeIXfCqJiLZjSHWRy_p_gHPYWv78Gva8A&oe=69DC277C",
            "has_lyrics": true,
            "highlight_start_times_in_ms": [
              40000,
              67500
            ],
            "id": "488157347220983",
            "ig_username": "badbunnypr",
            "is_eligible_for_audio_effects": true,
            "is_eligible_for_vinyl_sticker": true,
            "is_explicit": true,
            "licensed_music_subtype": "DEFAULT",
            "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKkn5gTWGxOOuux5ke4njnm0hKhlGZPEFYkuKNMneJMg2zCYOOvX0dh6iUpa1ni0h4MPx1lUdIeA6HzEMOXkV0.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Izemcy3Vz3AQ7kNvwFTZQGQ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo2NDU3NDUxNDc3ODU5MjQsImFzc2V0X2FnZV9kYXlzIjo0NTksInZpX3VzZWNhc2VfaWQiOjEwNTY4LCJkdXJhdGlvbl9zIjoyMTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=1dbfbcdccdcec8c3&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQ05oQWlBYTVUX0JXY3NKQUJGQ2tqTXNCd0pqYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmiMuxoqjTpQIVAigCQzMsF0BqoFHrhR64GBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_zt=28&_nc_ss=7a39b&oh=00_Af1J1n7bttddHpeIXfCqJiLZjSHWRy_p_gHPYWv78Gva8A&oe=69DC277C",
            "reactive_audio_download_url": null,
            "sanitized_title": null,
            "song_monetization_info": null,
            "subtitle": "",
            "title": "LA MuDANZA",
            "web_30s_preview_download_url": null,
            "lyrics": null,
            "spotify_track_metadata": null,
            "related_audios": null
          },
          "music_consumption_info": {
            "allow_media_creation_with_music": true,
            "music_creation_restriction_reason": null,
            "audio_asset_start_time_in_ms": 41000,
            "derived_content_start_time_in_composition_in_ms": null,
            "contains_lyrics": null,
            "derived_content_id": null,
            "display_labels": null,
            "formatted_clips_media_count": null,
            "is_bookmarked": false,
            "is_trending_in_clips": true,
            "overlap_duration_in_ms": 11000,
            "placeholder_profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.12442-15/43985629_311105916145351_58064759811405776_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFnOOW94S78cIE8EXJgDwdDEFoscmb5-sBJLaMACCCSXigV-cN0GuL81ha--C8P0Jo&_nc_ohc=HMeNVRbt-xsQ7kNvwGL20nB&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&edm=AKmAybEAAAAA&ccb=7-5&oh=00_Af0fWJMvyX8IKuae0jkGbMqj97mmG8eoAzefUyzOssG_Hw&oe=69DC253D&_nc_sid=99328a",
            "should_allow_music_editing": false,
            "should_mute_audio": false,
            "should_mute_audio_reason": "",
            "should_mute_audio_reason_type": null,
            "should_render_soundwave": false,
            "trend_rank": null,
            "previous_trend_rank": null,
            "ig_artist": {
              "strong_id__": "197260775",
              "pk": 197260775,
              "pk_id": "197260775",
              "id": "197260775",
              "username": "badbunnypr",
              "full_name": "Benito Antonio",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3773136183001949034_197260775",
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/588090177_18565248739012776_8615733116563517479_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFnOOW94S78cIE8EXJgDwdDEFoscmb5-sBJLaMACCCSXigV-cN0GuL81ha--C8P0Jo&_nc_ohc=KOZidhOeCukQ7kNvwEpEKwl&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GEGLDSOocEHQ-vRBACdwVhSfO5F3bmNDAQAB1501500j-ccb7-5&oh=00_Af3VBGz0EEjlvVhoQoeXgdUSnV6XO9GuV539nIBzzSaFFg&oe=69DC4696&_nc_sid=99328a"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT11.654966S\" FBManifestTimestamp=\"1775657881\" FBManifestIdentifier=\"FrKOs50NGBBpZ19kYXNoX2Jhc2VsaW5lGVau/cn9wPWlA6TExNa+tsIDhv+tifbN0gTIndLR/42fBazb8+/Z3IoGIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT11.654966S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.4\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1712432703502038v\" bandwidth=\"1220533\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"1774859\" FBPlaybackResolutionMos=\"0:100,360:95.6,480:93.8,720:87.9,1080:78.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.64,480:97.8,720:95.9,1080:92.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=RuvfyKeoOqoQ7kNvwFpHNem&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3NjIxOTQ3MjU2MTk1NCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMSwiYml0cmF0ZSI6MTIyMDUzMywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2NNr9ucNYmE6oLCsFxGjyRJZS8R2RY8_2QSDtVXcS2uw&amp;oe=69D84485</BaseURL><SegmentBase indexRange=\"892-959\" timescale=\"15360\" FBMinimumPrefetchRange=\"960-73718\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"960-353780\" FBFirstSegmentRange=\"960-741164\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"741165-1432907\" FBPrefetchSegmentRange=\"960-741164\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-891\"/></SegmentBase></Representation><Representation id=\"927807556894551v\" bandwidth=\"293879\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"427350\" FBPlaybackResolutionMos=\"0:100,360:71.4,480:66.2,720:56.5,1080:45.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86,480:81.2,720:71.7,1080:60.3\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNJV-hGRMSjv_9V4sNiynjbYD03fr9I1hPLjHFc4ZidUqmhiU_615BoLIIsWqUFRolQzxXcP4fVUezD-0HI300lDaqhIgg5x3Ou3EE.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=H4OuwI7d0FkQ7kNvwGwp4tM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzg3NjIxOTQ3MjU2MTk1NCwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjoxMSwiYml0cmF0ZSI6MjkzODc5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2P-pKwcXu3LHFiMj_mhkIBkd-6RJ-zJFNxK-ZFnS2AIA&amp;oe=69D84DBF</BaseURL><SegmentBase indexRange=\"887-954\" timescale=\"15360\" FBMinimumPrefetchRange=\"955-25777\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"955-96590\" FBFirstSegmentRange=\"955-193468\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"193469-349904\" FBPrefetchSegmentRange=\"955-193468\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-886\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1307558511230915a\" bandwidth=\"40146\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40146\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"59392\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNOsmon5Ktr4dQy5UcDcODkMqaDqVBRARyLlIjSuWo5V_8xJnF-zZbhwwpB8cdGYqfQJwztW9UgS0WdMXqLPnPAyS7nk_uhMimZQW4.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=RT-LncbrN1wQ7kNvwFpAd2n&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc2MjE5NDcyNTYxOTU0LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjExLCJiaXRyYXRlIjo0MDc2NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1FibFPi93ZR1Z742849REbB0JuIM4EikmEdQwqUSy1HQ&amp;oe=69DC4193</BaseURL><SegmentBase indexRange=\"837-904\" timescale=\"44100\" FBMinimumPrefetchRange=\"905-2025\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"905-14593\" FBFirstSegmentRange=\"905-27436\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"27437-49800\" FBPrefetchSegmentRange=\"905-27436\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"990496590172434a\" bandwidth=\"73859\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"73859\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"108509\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNaCQJ0xskQCQISxFdmz1DqEvD9QNZHWHoG0_7KVyPP06BygZErht4YcUllcS2IKXJW6L486TX2_swSKuepT3UMJsYMyEOVsBxnsas.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=TnjOu5W8gUsQ7kNvwEx9Rn-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc2MjE5NDcyNTYxOTU0LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjExLCJiaXRyYXRlIjo3NDQ4MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2VyvHYdT9spJGHrWl2Fjc7-rnMmfBJm7meifn-yySZwg&amp;oe=69DC4557</BaseURL><SegmentBase indexRange=\"838-905\" timescale=\"44100\" FBMinimumPrefetchRange=\"906-2820\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-27819\" FBFirstSegmentRange=\"906-51485\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"51486-92119\" FBPrefetchSegmentRange=\"906-51485\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1475785074034532a\" bandwidth=\"112400\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"112400\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"164653\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNP6rQKXxTZqxWn234KEcr_JrnIJCnW6wtuOGX4rUd1QC6hJHztBRVbFFJq-83-YM8M3L4Xkn5V7ZAByLkwkUleJBGnhIsyNHnO4I8.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=RAaEcZZ4iwkQ7kNvwFQWuGm&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3ODc2MjE5NDcyNTYxOTU0LCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjExLCJiaXRyYXRlIjoxMTMwMTgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0vNlmjhFqT_y3S9alkDfV78rcb1cFCkz1mLv0zsRAFcw&amp;oe=69DC51DD</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2514\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-38468\" FBFirstSegmentRange=\"901-74655\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"74656-140879\" FBPrefetchSegmentRange=\"901-74655\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": true,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WzEsWzM4NzA4MTUwODgxMDIyNzM1MTMsMzg3MDgxNDQyNTA0OTgxNDgyOV0sIlFWRkRXVlI2U1dnNU4zcG9ZMjk2ZEVWdGJtcFlVRU5FYVVkeFVHZEVOMGw0TjI1eFFVcFhiMVZCY2xGaWNXOVhRVjh5TW5VNWFVcFliRzlLTmpSWU1IRnRla0pPUWs1WmVWOHpWVEo2UmtoeFJtRmZMV1ZvTmc9PSJd"
]
```

</details>

---

### GET /v1/location/medias/top

Get location top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/top?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_top_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/top",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/top?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870812423301488664",
    "id": "3870812423301488664_3028562913",
    "code": "DW342P7DeAY",
    "taken_at": "2026-04-08T14:00:20Z",
    "taken_at_ts": 1775656820,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": {
      "pk": 1029352986,
      "name": "Studio2 & Media Library for Dance and Theatre",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "Mariannenplatz 2",
      "city": "",
      "zip": null,
      "lng": 13.42446,
      "lat": 52.5038399,
      "external_id": "412463942289587",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "3028562913",
      "id": "3028562913",
      "username": "lebesheva_maria",
      "full_name": "Мария Лебешева",
      "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/v/t51.2885-19/424576707_1115460392965599_9214457040827163117_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-sin2-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEg40lDKj0H-MW_139g3qD_YXdTxIS4Rv8jX0E6HikXpoJhzt8VXXfcPBkWIGoC3AE&_nc_ohc=Z1v9c_XktXgQ7kNvwHv93Ba&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GMOGThnf1XtcgfYDAO2hmbzbU_B-bkULAAAB1501500j-ccb7-5&oh=00_Af0C3FwwC6f_zv2-KqjViLNpMpj60YLtO7D6YDbF7jNpGw&oe=69DC3C84&_nc_sid=99328a",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 1,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Танцевальная лаборатория Запределье, 2026",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870811310191911595",
        "id": "3870811310191911595_3028562913",
        "video_url": null,
        "thumbnail_url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0WkTAyXdtyOV07emBlwDwyBquXvLc69Sd74mO6rlhprw&oe=69DC5100",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              13647,
              27294
            ],
            "height": 1799,
            "scans_profile": "e35",
            "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0WkTAyXdtyOV07emBlwDwyBquXvLc69Sd74mO6rlhprw&oe=69DC5100",
            "width": 1440,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              6718,
              13437
            ],
            "height": 937,
            "scans_profile": "e35",
            "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af2bUVXdz3m3dsP3aS6cgDYxvGBt6h8Ru67TcsPA5aVHcQ&oe=69DC5100",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870812423301488664_3028562913",
        "commerciality_status": "not_commercial",
        "taken_at": 1775656818
      },
      {
        "pk": "3870811313681579767",
        "id": "3870811313681579767_3028562913",
        "video_url": null,
        "thumbnail_url": "https://scontent-sin11-1.cdninstagram.com/v/t51.82787-15/659260442_18463180105098914_2382922490631793841_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDgxMTMxMzY4MTU3OTc2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=IiJmCmapKx8Q7kNvwGRL4GC&_nc_oc=AdpF0jxi9RHCjdvbA0lkeFJGhtXdeEq0Fq-Ya-Fp2ySEsPH752gmSUCEIUA4HowS_m4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0QhIFNag-vG31vWyBDj7iGkvM9n3qPraroBTu7FUzDhQ&oe=69DC399B",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              17043,
              34086
            ],
            "height": 1799,
            "scans_profile": "e35",
            "url": "https://scontent-sin11-1.cdninstagram.com/v/t51.82787-15/659260442_18463180105098914_2382922490631793841_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDgxMTMxMzY4MTU3OTc2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=IiJmCmapKx8Q7kNvwGRL4GC&_nc_oc=AdpF0jxi9RHCjdvbA0lkeFJGhtXdeEq0Fq-Ya-Fp2ySEsPH752gmSUCEIUA4HowS_m4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0QhIFNag-vG31vWyBDj7iGkvM9n3qPraroBTu7FUzDhQ&oe=69DC399B",
            "width": 1440,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              8390,
              16781
            ],
            "height": 937,
            "scans_profile": "e35",
            "url": "https://scontent-sin11-1.cdninstagram.com/v/t51.82787-15/659260442_18463180105098914_2382922490631793841_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDgxMTMxMzY4MTU3OTc2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=IiJmCmapKx8Q7kNvwGRL4GC&_nc_oc=AdpF0jxi9RHCjdvbA0lkeFJGhtXdeEq0Fq-Ya-Fp2ySEsPH752gmSUCEIUA4HowS_m4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0uyjEyb2jHcmyc__vr3b6B_ryzau3e-PB6Y1IFRLXUZg&oe=69DC399B",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870812423301488664_3028562913",
        "commerciality_status": "not_commercial",
        "taken_at": 1775656818
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          13647,
          27294
        ],
        "height": 1799,
        "scans_profile": "e35",
        "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0WkTAyXdtyOV07emBlwDwyBquXvLc69Sd74mO6rlhprw&oe=69DC5100",
        "width": 1440,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          6718,
          13437
        ],
        "height": 937,
        "scans_profile": "e35",
        "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af2bUVXdz3m3dsP3aS6cgDYxvGBt6h8Ru67TcsPA5aVHcQ&oe=69DC5100",
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
    "pk": "3870820209296730100",
    "id": "3870820209296730100_1648081225",
    "code": "DW36njMiOf0",
    "taken_at": "2026-04-08T14:15:48Z",
    "taken_at_ts": 1775657748,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": {
      "pk": 213131048,
      "name": "Berlin, Germany",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "",
      "city": "",
      "zip": null,
      "lng": 13.401251,
      "lat": 52.518391,
      "external_id": "111175118906315",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "1648081225",
      "id": "1648081225",
      "username": "lubov.fedorennko",
      "full_name": "Certified Language Coach (англійська) | мовний коучинг",
      "profile_pic_url": "https://scontent-sin11-1.cdninstagram.com/v/t51.82787-19/524720170_18516768958017226_3214004893111064111_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gEg40lDKj0H-MW_139g3qD_YXdTxIS4Rv8jX0E6HikXpoJhzt8VXXfcPBkWIGoC3AE&_nc_ohc=O3mm0EatNuQQ7kNvwHxnunj&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GCqYRh-KbiE858hBAC_WQPhrcJosbmNDAQAB1501500j-ccb7-5&oh=00_Af123jeSoVeUUisrwH6nJ5VtcNPB9UjHL2u9HMasLCClDw&oe=69DC2B41&_nc_sid=99328a",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 1,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "If you live in Berlin or want to travel here, this post is for you! Sharing with you some of my favourite coffee places in Berlin☕️☀️\n\nSee photos in the post and here I’ll attach the location📍\n\n1. Amato - Dunckerstraße 69, 10437 \n2. Luuv Café - Dunckerstraße 72, 10437 \n3. Catnip Coffee - Warschauer Str. 69, 10243 \n4. Café im Bode-Museum - Geschwister-Scholl-Straße 6, 10117\n5. Rausch Schokoladenhaus - Charlottenstraße 60, 10117 \n\nWanna see more recommendations? Let me know in the comments😊\n\n#Berlin #berlintravel #traveling #germanytourism #coffee",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870814184606825758",
        "id": "3870814184606825758_1648081225",
        "video_url": null,
        "thumbnail_url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwGbGIWQ&_nc_oc=Adod5o3MDqVW1-JuR40cMhfiaDD_mlwt8XGl86n0nDDEABHVT3MrJ1g6AB4iq2BXGt4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af1smFsAPkyik7PMTS5URThEKkerLZ2dt05Yb7_3fv51Ig&oe=69DC1FCA",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              23401,
              46802
            ],
            "height": 1800,
            "scans_profile": "e35",
            "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwGbGIWQ&_nc_oc=Adod5o3MDqVW1-JuR40cMhfiaDD_mlwt8XGl86n0nDDEABHVT3MrJ1g6AB4iq2BXGt4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af1smFsAPkyik7PMTS5URThEKkerLZ2dt05Yb7_3fv51Ig&oe=69DC1FCA",
            "width": 1440,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              11524,
              23048
            ],
            "height": 938,
            "scans_profile": "e35",
            "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwGbGIWQ&_nc_oc=Adod5o3MDqVW1-JuR40cMhfiaDD_mlwt8XGl86n0nDDEABHVT3MrJ1g6AB4iq2BXGt4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af1QzVl25IisbTr0dKwOsEtDNevsQwRGgFkqgPJqJ9Pdnw&oe=69DC1FCA",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870820209296730100_1648081225",
        "commerciality_status": "not_commercial",
        "taken_at": 1775657745
      },
      {
        "pk": "3870814185873524638",
        "id": "3870814185873524638_1648081225",
        "video_url": null,
        "thumbnail_url": "https://scontent-sin11-1.cdninstagram.com/v/t51.82787-15/661397893_18574820569017226_321544075407863593_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDE4NTg3MzUyNDYzOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=S9JeqDGilp8Q7kNvwF-jUqc&_nc_oc=AdoJNduZxXvEQf-4PZs4etQN3-EpXsF_m1fUH-TWP-s54uNEVC_n-QkdmwjqztVL7CU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af2e51uxaiXe1Wp6kRytarMQZfMFlr5gJg5Mx_92-Pgdtw&oe=69DC446B",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              23827,
              47655
            ],
            "height": 1800,
            "scans_profile": "e35",
            "url": "https://scontent-sin11-1.cdninstagram.com/v/t51.82787-15/661397893_18574820569017226_321544075407863593_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDE4NTg3MzUyNDYzOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=S9JeqDGilp8Q7kNvwF-jUqc&_nc_oc=AdoJNduZxXvEQf-4PZs4etQN3-EpXsF_m1fUH-TWP-s54uNEVC_n-QkdmwjqztVL7CU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af2e51uxaiXe1Wp6kRytarMQZfMFlr5gJg5Mx_92-Pgdtw&oe=69DC446B",
            "width": 1440,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              11734,
              23468
            ],
            "height": 938,
            "scans_profile": "e35",
            "url": "https://scontent-sin11-1.cdninstagram.com/v/t51.82787-15/661397893_18574820569017226_321544075407863593_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDE4NTg3MzUyNDYzOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=S9JeqDGilp8Q7kNvwF-jUqc&_nc_oc=AdoJNduZxXvEQf-4PZs4etQN3-EpXsF_m1fUH-TWP-s54uNEVC_n-QkdmwjqztVL7CU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af3Cro6sBpsCpezyoJ7xeqDWZtzDC4MU_r4Xqe8VrE8-Og&oe=69DC446B",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870820209296730100_1648081225",
        "commerciality_status": "not_commercial",
        "taken_at": 1775657745
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          23401,
          46802
        ],
        "height": 1800,
        "scans_profile": "e35",
        "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwGbGIWQ&_nc_oc=Adod5o3MDqVW1-JuR40cMhfiaDD_mlwt8XGl86n0nDDEABHVT3MrJ1g6AB4iq2BXGt4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af1smFsAPkyik7PMTS5URThEKkerLZ2dt05Yb7_3fv51Ig&oe=69DC1FCA",
        "width": 1440,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          11524,
          23048
        ],
        "height": 938,
        "scans_profile": "e35",
        "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwGbGIWQ&_nc_oc=Adod5o3MDqVW1-JuR40cMhfiaDD_mlwt8XGl86n0nDDEABHVT3MrJ1g6AB4iq2BXGt4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af1QzVl25IisbTr0dKwOsEtDNevsQwRGgFkqgPJqJ9Pdnw&oe=69DC1FCA",
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
]
```

</details>

---

### GET /v1/location/medias/top/chunk

Get location chunk of top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/top/chunk?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_top_chunk_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/top/chunk",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/top/chunk?location_pk=213131048",
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
      "pk": "3870812423301488664",
      "id": "3870812423301488664_3028562913",
      "code": "DW342P7DeAY",
      "taken_at": "2026-04-08T14:00:20Z",
      "taken_at_ts": 1775656820,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": {
        "pk": 1029352986,
        "name": "Studio2 & Media Library for Dance and Theatre",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "Mariannenplatz 2",
        "city": "",
        "zip": null,
        "lng": 13.42446,
        "lat": 52.5038399,
        "external_id": "412463942289587",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "3028562913",
        "id": "3028562913",
        "username": "lebesheva_maria",
        "full_name": "Мария Лебешева",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/424576707_1115460392965599_9214457040827163117_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gE_iIhELGkMHRrqCOxJ4HnWzllW-rhWuZF0plYZdPKIx0Dbs8Hh2K14ppP3tCxThK0&_nc_ohc=Z1v9c_XktXgQ7kNvwGVZCFS&_nc_gid=YN-agi0EhJb6182K1_sHFA&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GMOGThnf1XtcgfYDAO2hmbzbU_B-bkULAAAB1501500j-ccb7-5&oh=00_Af2UQEAkTwC6a0E91grDt62T2Go4zYp9Qc7B3G1Ty1nRpA&oe=69DC3C84&_nc_sid=99328a",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 1,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Танцевальная лаборатория Запределье, 2026",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870811310191911595",
          "id": "3870811310191911595_3028562913",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af1mTY-42vLB9XfJsUk2cimKZjb_NO7xeS6B669VGoO45g&oe=69DC5100",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                13647,
                27294
              ],
              "height": 1799,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af1mTY-42vLB9XfJsUk2cimKZjb_NO7xeS6B669VGoO45g&oe=69DC5100",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                6718,
                13437
              ],
              "height": 937,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af0UNUqSbqhIFVv8xJ0AK3rtWZYBaz2RP7Q-SHSn9i3c6A&oe=69DC5100",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870812423301488664_3028562913",
          "commerciality_status": "not_commercial",
          "taken_at": 1775656818
        },
        {
          "pk": "3870811313681579767",
          "id": "3870811313681579767_3028562913",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/659260442_18463180105098914_2382922490631793841_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDgxMTMxMzY4MTU3OTc2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=IiJmCmapKx8Q7kNvwGVkQz3&_nc_oc=AdqZxHeFa-wy99Y58oF2dUSROYOEN3hmKzdmXyddwcZlkVVW54u2XM7oEEpoNKR3790&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af1mIluECZuZ-M1tlhjdGBHb7PVLLdybrUorOb9I36SLeg&oe=69DC399B",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                17043,
                34086
              ],
              "height": 1799,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/659260442_18463180105098914_2382922490631793841_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDgxMTMxMzY4MTU3OTc2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=IiJmCmapKx8Q7kNvwGVkQz3&_nc_oc=AdqZxHeFa-wy99Y58oF2dUSROYOEN3hmKzdmXyddwcZlkVVW54u2XM7oEEpoNKR3790&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af1mIluECZuZ-M1tlhjdGBHb7PVLLdybrUorOb9I36SLeg&oe=69DC399B",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                8390,
                16781
              ],
              "height": 937,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/659260442_18463180105098914_2382922490631793841_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDgxMTMxMzY4MTU3OTc2Nw%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=IiJmCmapKx8Q7kNvwGVkQz3&_nc_oc=AdqZxHeFa-wy99Y58oF2dUSROYOEN3hmKzdmXyddwcZlkVVW54u2XM7oEEpoNKR3790&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2fEYhY1L7CyiOp2mS24p4aH-gqnQleqc49LZnCm8PXjw&oe=69DC399B",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870812423301488664_3028562913",
          "commerciality_status": "not_commercial",
          "taken_at": 1775656818
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            13647,
            27294
          ],
          "height": 1799,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af1mTY-42vLB9XfJsUk2cimKZjb_NO7xeS6B669VGoO45g&oe=69DC5100",
          "width": 1440,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            6718,
            13437
          ],
          "height": 937,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af0UNUqSbqhIFVv8xJ0AK3rtWZYBaz2RP7Q-SHSn9i3c6A&oe=69DC5100",
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
      "pk": "3870820209296730100",
      "id": "3870820209296730100_1648081225",
      "code": "DW36njMiOf0",
      "taken_at": "2026-04-08T14:15:48Z",
      "taken_at_ts": 1775657748,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": {
        "pk": 213131048,
        "name": "Berlin, Germany",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 13.401251,
        "lat": 52.518391,
        "external_id": "111175118906315",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "1648081225",
        "id": "1648081225",
        "username": "lubov.fedorennko",
        "full_name": "Certified Language Coach (англійська) | мовний коучинг",
        "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/524720170_18516768958017226_3214004893111064111_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gE_iIhELGkMHRrqCOxJ4HnWzllW-rhWuZF0plYZdPKIx0Dbs8Hh2K14ppP3tCxThK0&_nc_ohc=O3mm0EatNuQQ7kNvwGuuGOb&_nc_gid=YN-agi0EhJb6182K1_sHFA&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GCqYRh-KbiE858hBAC_WQPhrcJosbmNDAQAB1501500j-ccb7-5&oh=00_Af2R4D44bdG-I_ZXb5AKQh3Asrq8kcf3Vgu7SyUKbMb1yg&oe=69DC2B41&_nc_sid=99328a",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 1,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "If you live in Berlin or want to travel here, this post is for you! Sharing with you some of my favourite coffee places in Berlin☕️☀️\n\nSee photos in the post and here I’ll attach the location📍\n\n1. Amato - Dunckerstraße 69, 10437 \n2. Luuv Café - Dunckerstraße 72, 10437 \n3. Catnip Coffee - Warschauer Str. 69, 10243 \n4. Café im Bode-Museum - Geschwister-Scholl-Straße 6, 10117\n5. Rausch Schokoladenhaus - Charlottenstraße 60, 10117 \n\nWanna see more recommendations? Let me know in the comments😊\n\n#Berlin #berlintravel #traveling #germanytourism #coffee",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870814184606825758",
          "id": "3870814184606825758_1648081225",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwFUolh0&_nc_oc=Adr_qPka5RqQkN7sBJwRc9lEFw5Els09Kf9HBDio1KBQxqrXSnXPB_uTp1Ew1rk5E3Y&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2KqQROKv_rrm1HvJXf-fPSXpAgHiY1P7Lsp6kHLO6qkQ&oe=69DC1FCA",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                23401,
                46802
              ],
              "height": 1800,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwFUolh0&_nc_oc=Adr_qPka5RqQkN7sBJwRc9lEFw5Els09Kf9HBDio1KBQxqrXSnXPB_uTp1Ew1rk5E3Y&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2KqQROKv_rrm1HvJXf-fPSXpAgHiY1P7Lsp6kHLO6qkQ&oe=69DC1FCA",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                11524,
                23048
              ],
              "height": 938,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwFUolh0&_nc_oc=Adr_qPka5RqQkN7sBJwRc9lEFw5Els09Kf9HBDio1KBQxqrXSnXPB_uTp1Ew1rk5E3Y&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2PddNrgY8dlF3m18EWnDcwHuZO_QsO8Ajtmcj7yD2YrA&oe=69DC1FCA",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870820209296730100_1648081225",
          "commerciality_status": "not_commercial",
          "taken_at": 1775657745
        },
        {
          "pk": "3870814185873524638",
          "id": "3870814185873524638_1648081225",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661397893_18574820569017226_321544075407863593_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDE4NTg3MzUyNDYzOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=S9JeqDGilp8Q7kNvwHZ53aB&_nc_oc=AdqRuPRhzqPf1TtxAsNx41sVsXMcUH3xqHS1YD9ClzzOgtiC4_2mHzMuL1yzZ0rBNuI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2bVp6LrWZ7ebV1xhYPuL_HA4_JvFfaFF3lcHDlvCQ8dA&oe=69DC446B",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                23827,
                47655
              ],
              "height": 1800,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661397893_18574820569017226_321544075407863593_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDE4NTg3MzUyNDYzOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=S9JeqDGilp8Q7kNvwHZ53aB&_nc_oc=AdqRuPRhzqPf1TtxAsNx41sVsXMcUH3xqHS1YD9ClzzOgtiC4_2mHzMuL1yzZ0rBNuI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2bVp6LrWZ7ebV1xhYPuL_HA4_JvFfaFF3lcHDlvCQ8dA&oe=69DC446B",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                11734,
                23468
              ],
              "height": 938,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661397893_18574820569017226_321544075407863593_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgxNDE4NTg3MzUyNDYzOA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=S9JeqDGilp8Q7kNvwHZ53aB&_nc_oc=AdqRuPRhzqPf1TtxAsNx41sVsXMcUH3xqHS1YD9ClzzOgtiC4_2mHzMuL1yzZ0rBNuI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af3OM1TQJ1CSti5cVQeje7fKcT9IfKsHKfE4yonZuSWgWg&oe=69DC446B",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870820209296730100_1648081225",
          "commerciality_status": "not_commercial",
          "taken_at": 1775657745
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            23401,
            46802
          ],
          "height": 1800,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwFUolh0&_nc_oc=Adr_qPka5RqQkN7sBJwRc9lEFw5Els09Kf9HBDio1KBQxqrXSnXPB_uTp1Ew1rk5E3Y&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2KqQROKv_rrm1HvJXf-fPSXpAgHiY1P7Lsp6kHLO6qkQ&oe=69DC1FCA",
          "width": 1440,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            11524,
            23048
          ],
          "height": 938,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/661341856_18574820560017226_5856465557866597170_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=111&ig_cache_key=Mzg3MDgxNDE4NDYwNjgyNTc1OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTgwMC5zZHIuQzMifQ%3D%3D&_nc_ohc=KIhO8C8rVaAQ7kNvwFUolh0&_nc_oc=Adr_qPka5RqQkN7sBJwRc9lEFw5Els09Kf9HBDio1KBQxqrXSnXPB_uTp1Ew1rk5E3Y&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af2PddNrgY8dlF3m18EWnDcwHuZO_QsO8Ajtmcj7yD2YrA&oe=69DC1FCA",
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
  "WzEsWzM4NzA3ODc0MDU4MzgyOTY3OThdLCI3NDE2ZjIwMTJmNWM0YmUwOTZkMDFiOGIyOTZkZTU0ZSJd"
]
```

</details>

---

### GET /v1/location/search

Get locations using lat and long

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `lat` | number | Yes | Lat |
| `lng` | number | Yes | Lng |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/search?lat=40.7128&lng=-74.006"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_search_v1(lat=40.7128, lng=-74.006)
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/search",
        headers=headers,
        params={"lat": 40.7128, "lng": -74.006},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/search?lat=40.7128&lng=-74.006",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": null,
    "name": "Central Park",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "<0.1mi",
    "city": null,
    "zip": null,
    "lng": -74.0059728,
    "lat": 40.7127753,
    "external_id": "2233371183358453",
    "external_id_source": "facebook_places"
  },
  {
    "pk": null,
    "name": "München, Germany",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "<0.1mi",
    "city": null,
    "zip": null,
    "lng": -74.0059728,
    "lat": 40.7127753,
    "external_id": "436749889689403",
    "external_id_source": "facebook_places"
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-locations){ target=_blank }
