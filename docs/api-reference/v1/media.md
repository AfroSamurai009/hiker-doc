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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/code",
        headers=headers,
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
  "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFu9GQ3&_nc_oc=AdpippriixJXAGwD15RT1EjSoiWMpP5S0OMgwoK2e5lKMx6IYjFe0l0oy85LYCzvDHs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=84AtMEJsfwsr1Mbjrh6ZOQ&_nc_ss=7a3ba&oh=00_Af0t57vufLPimRsdFAoApWhwKsE5IjPJzXarTqGMJirePg&oe=69DC3E7E",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gELkam7XNQ9TuVYRiMgLmO-1qSxhCYejNE5ooANEtY_759Y8ndOajjvzkoEpwkCseg&_nc_ohc=XbeNvhLXv28Q7kNvwFICEUk&_nc_gid=84AtMEJsfwsr1Mbjrh6ZOQ&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1L2sSiaE0YU236I7CfFHh6YMj4QtqbbNw4uWfAdE7yyA&oe=69DC51E9&_nc_sid=fc8dfb",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135430,
  "play_count": 2866120,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEHSHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=84AtMEJsfwsr1Mbjrh6ZOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af17TciztcEgR1DrbgCoq-UTAn3QwzDbeMK50jYa0cBSLQ&oe=69D8376F",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwFu9GQ3&_nc_oc=AdpippriixJXAGwD15RT1EjSoiWMpP5S0OMgwoK2e5lKMx6IYjFe0l0oy85LYCzvDHs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=84AtMEJsfwsr1Mbjrh6ZOQ&_nc_ss=7a3ba&oh=00_Af0t57vufLPimRsdFAoApWhwKsE5IjPJzXarTqGMJirePg&oe=69DC3E7E",
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
      "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEHSHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=84AtMEJsfwsr1Mbjrh6ZOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af17TciztcEgR1DrbgCoq-UTAn3QwzDbeMK50jYa0cBSLQ&oe=69D8376F",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 102,
      "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwEHSHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=84AtMEJsfwsr1Mbjrh6ZOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af17TciztcEgR1DrbgCoq-UTAn3QwzDbeMK50jYa0cBSLQ&oe=69D8376F",
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
  // ... truncated
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/id",
        headers=headers,
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
  "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwHDKaGX&_nc_oc=AdpAjY6UHQbcsc5zMaXr40yvtcU-ip6gOc-RNon_c77IFOy-PWtyQCS1nlqoDXmFU6o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=KutRJGnMj_hbUuAC-8-Wtg&_nc_ss=7a3ba&oh=00_Af2euMoxis86-hTDLd-WdY2zOgLLaq5BmNQvjT7-PZ8eSw&oe=69DC3E7E",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbw7XvK-hWJXBEu1VD69PotVmoBoLgAH9jZKTTJKrAkL1IxsRcwxhPCebziDyyYI4&_nc_ohc=XbeNvhLXv28Q7kNvwHZF6T6&_nc_gid=KutRJGnMj_hbUuAC-8-Wtg&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0lZduY7Ji4QyT1zsQ6xxn2j0L9C5XrffRwMlc2go8pOg&oe=69DC51E9&_nc_sid=fc8dfb",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135430,
  "play_count": 2866120,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwE00G9W&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=KutRJGnMj_hbUuAC-8-Wtg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2GTta4Lg-w6fGegDzwRwj62ft1ahSKky6ANLs84o_0Rw&oe=69D8376F",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwHDKaGX&_nc_oc=AdpAjY6UHQbcsc5zMaXr40yvtcU-ip6gOc-RNon_c77IFOy-PWtyQCS1nlqoDXmFU6o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=KutRJGnMj_hbUuAC-8-Wtg&_nc_ss=7a3ba&oh=00_Af2euMoxis86-hTDLd-WdY2zOgLLaq5BmNQvjT7-PZ8eSw&oe=69DC3E7E",
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
      "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwE00G9W&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=KutRJGnMj_hbUuAC-8-Wtg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2GTta4Lg-w6fGegDzwRwj62ft1ahSKky6ANLs84o_0Rw&oe=69D8376F",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 102,
      "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwE00G9W&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=KutRJGnMj_hbUuAC-8-Wtg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2GTta4Lg-w6fGegDzwRwj62ft1ahSKky6ANLs84o_0Rw&oe=69D8376F",
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
  // ... truncated
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/by/url",
        headers=headers,
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
  "thumbnail_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwGsb10O&_nc_oc=Ado9uyMKPq1m7U4vMfVQb7sOcGMeM8MXIbFh3WsxKrFqlLqV-Fu_zeW4LSzKThGYRmU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=RQHclyb2Ji3WKkED1HDEIQ&_nc_ss=7a3ba&oh=00_Af3yisZEc32LagJTXyJS9NYom11zrDUj7iiMtSPYxE8rrg&oe=69DC3E7E",
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGO4aHzxtzc5yhuRl4aJB1Oc2LcjGDnGorCvuT1Vtqc6mB0vSGF-FwaZXton_06LYM&_nc_ohc=XbeNvhLXv28Q7kNvwHP2JBi&_nc_gid=RQHclyb2Ji3WKkED1HDEIQ&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0piZ8xIeHDzVTIk_7d8k1qikdnnmUAFanNe2pnHgojrA&oe=69DC51E9&_nc_sid=fc8dfb",
    "is_private": false,
    "is_verified": true
  },
  "comment_count": 485,
  "comments_disabled": false,
  "like_count": 135430,
  "play_count": 2866120,
  "has_liked": false,
  "caption_text": "Even the heaviest rain feels peaceful here.\n\n#HostilePlanet is now streaming on @DisneyPlus.",
  "usertags": [],
  "sponsor_tags": [],
  "video_url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHxoaMa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=RQHclyb2Ji3WKkED1HDEIQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2894bi7msO6SaXUBMb2I4fdjX-I7cwT0nyvgMF7xBH2A&oe=69D8376F",
  "view_count": 0,
  "video_duration": 22.31399917602539,
  "title": "",
  "resources": [],
  "image_versions": [
    {
      "estimated_scans_sizes": [
        27870,
        55740
      ],
      "height": 1333,
      "scans_profile": "e35",
      "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzc3NjgzMjg5ODI4MDIyODE0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwGsb10O&_nc_oc=Ado9uyMKPq1m7U4vMfVQb7sOcGMeM8MXIbFh3WsxKrFqlLqV-Fu_zeW4LSzKThGYRmU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=RQHclyb2Ji3WKkED1HDEIQ&_nc_ss=7a3ba&oh=00_Af3yisZEc32LagJTXyJS9NYom11zrDUj7iiMtSPYxE8rrg&oe=69DC3E7E",
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
      "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHxoaMa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=RQHclyb2Ji3WKkED1HDEIQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2894bi7msO6SaXUBMb2I4fdjX-I7cwT0nyvgMF7xBH2A&oe=69D8376F",
      "url_expiration_timestamp_us": null,
      "width": 720,
      "fallback": null
    },
    {
      "bandwidth": 2315752,
      "height": 1280,
      "id": "1525428988604088v",
      "type": 102,
      "url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m86/AQMvRAmXAXHYSLt2sH1ZltDjre00G-tjzkYOeM8hqXTDwZWq2yWFXWqUGh9JUkBr7jSQ_wH8srCCIuqv2o1QDJO1ep5O-KoD1HBy-5E.mp4?_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=Ey9Zfx1FVawQ7kNvwHxoaMa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6Mjk4MzMyOTA1MTg1NjQ3NCwiYXNzZXRfYWdlX2RheXMiOjEyOSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjIyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=48af01c8cb018ecf&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNjQyOEZERTQ4NDYwRUFFOEVCM0UxNUM4QjhGOUZBMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYRmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NzQ1NTIwNDUwOTgwNTJfNTk1MTgxNTcxNDA3OTUxNDEwOS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtLmSxs3UzAoVAigCQzMsF0A2UCDEm6XjGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&_nc_gid=RQHclyb2Ji3WKkED1HDEIQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2894bi7msO6SaXUBMb2I4fdjX-I7cwT0nyvgMF7xBH2A&oe=69D8376F",
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
  // ... truncated
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/code/from/pk",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/comments",
        headers=headers,
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
    "pk": "18178774921320754",
    "text": "God bless our planet 💚🙏",
    "user": {
      "pk": "5646775780",
      "id": "5646775780",
      "username": "adriana.prn.71",
      "full_name": "Adriana Peñaloza",
      "profile_pic_url": "https://scontent-mad1-1.cdninstagram.com/v/t51.82787-19/540685604_18397468009191781_5796551439984130253_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=103&ig_cache_key=GCQ1OiBlWXRRZlxBAM14iL7SfHFQbmNDAQAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=Y17pObw-puwQ7kNvwEZIfCl&_nc_oc=AdpzwMymkzksmncIgYtSE3NBuDXhWqTOZCowRqa31arYJgmDlroZmnQKzuIj-VXL0s4&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_gid=KmQ3EtKEjydDQFYcnvdafQ&_nc_ss=7a3ba&oh=00_Af2VeVvSCEOjOEaasR1okl2FzLT8VH69_Mau8nq__GAgfw&oe=69DC2632",
      "profile_pic_url_hd": null,
      "is_private": true,
      "is_verified": false
    },
    "created_at_utc": "2025-11-30T00:38:59Z",
    "content_type": "comment",
    "status": "Active",
    "has_liked": false,
    "like_count": 35
  },
  {
    "pk": "17915190762228930",
    "text": "Nature is brilliantly beautiful!🤩",
    "user": {
      "pk": "1393016141",
      "id": "1393016141",
      "username": "scubalover14",
      "full_name": "Karen",
      "profile_pic_url": "https://scontent-mad1-1.cdninstagram.com/v/t51.2885-19/10514103_680727235334784_933888781_a.jpg?stp=dst-jpg_e0_tt6&_nc_cat=107&ig_cache_key=GLduoACAEg0pHmsCAA0DqjcAAAAAYUULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=C0bKK8aX6HUQ7kNvwEZpAmp&_nc_oc=Adp3VBasQ2lu44v6GrGHc1Hc5Rh_IKeTiYxtI2KRxWg1YRij6tfM48oiisfOneYFVP0&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af0vMS998vfVs0iLtM8wgNLRUkswTboKoh7V-SB6RpBCGA&oe=69DC49E1",
      "profile_pic_url_hd": null,
      "is_private": true,
      "is_verified": false
    },
    "created_at_utc": "2025-11-29T22:36:22Z",
    "content_type": "comment",
    "status": "Active",
    "has_liked": false,
    "like_count": 66
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/comments/chunk",
        headers=headers,
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
        "profile_pic_url": "https://scontent-syd2-1.cdninstagram.com/v/t51.2885-19/10514103_680727235334784_933888781_a.jpg?stp=dst-jpg_e0_tt6&_nc_cat=107&ig_cache_key=GLduoACAEg0pHmsCAA0DqjcAAAAAYUULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xNTAuQzMifQ%3D%3D&_nc_ohc=C0bKK8aX6HUQ7kNvwHfCb_p&_nc_oc=AdqQVcpKKPUN7fhnp0wyp4OHasOToUyx3x7F6Fp2eX3yoaAr716hQNcvPO9vajUi3d8&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af2HTB69AHGuEadaWBPGnDSnlZrzBIfU69O4sG8xobZnNA&oe=69DC49E1",
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
      "pk": "18032217926535638",
      "text": "This is wonderful 👏👏👏",
      "user": {
        "pk": "48614973638",
        "id": "48614973638",
        "username": "ranaghaedi_25",
        "full_name": "Raha Azadi",
        "profile_pic_url": "https://scontent-syd2-1.cdninstagram.com/v/t51.2885-19/461976566_513884421550377_7990592686193571192_n.jpg?stp=dst-jpg_e0_s150x150_tt6&_nc_cat=102&ig_cache_key=GPYziRsp8WYKYNMBAHj1Zk22SeRubkULAAAB1501500j-ccb7-5&ccb=7-5&_nc_sid=669407&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=B0ZM19naosEQ7kNvwFuF-dK&_nc_oc=AdqMBF4X5JXLUePMrKtGjkgrSEZPk4aML0Ru92ZjaF2RWnHwcC4zmjDv25KgneNXPVQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=24&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_ss=7a3ba&oh=00_Af2dW4mw0Cg93J6RlYqJ93061ivwjR32-YKSNnOV3bk_rw&oe=69DC2EB9",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false
      },
      "created_at_utc": "2025-12-01T18:58:53Z",
      "content_type": "comment",
      "status": "Active",
      "has_liked": false,
      "like_count": 2
    }
  ],
  "IntcImNhY2hlZF9jb21tZW50c19jdXJzb3JcIjpcIjE4MTY4ODM3ODIwMzM5MTI4XCIsXCJiaWZpbHRlcl90b2tlblwiOlwiR2dZWWdRRUFkVzNGVnRDTlB3RENUSGRseGFVX0FOWUpCdWcwRUVBQUtfN2NVLTRqUUFBeUdhUGRmNVZBQUZQR1RKMWVVRUFBd19ldjBLdnJQd0M3Q0tEZ2JCdEFBSXo5TlJXQXZUOEE2YlhPdV8wLVFBQWo0NHNLRm5JX0FONi03cTlteHo4QVBFVjBab0VvUUFBaENtRmltMzFBQUN2bHpWdjdQRUFBUXcwYXhLUWlRUUFBXCJ9Ig=="
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/photo",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/photo/by/url",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/video",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/download/video/by/url",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/insight",
        headers=headers,
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
  "display_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=100&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=hrcmFfN5eMYQ7kNvwHRY7tt&_nc_oc=Ado7Ye09Ka9b-SVHbW-ojMN-TvnP1z8nkF2YcYuslgL1xq6wMoW2lvlfYrSdmDjm6zM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=fl9u8XJVvvpA55bP-aO0eg&_nc_ss=7a39b&oh=00_Af0ZZoKcCoCbfc3nwTAig9m76SC1ViWW7gdjz-3pj3DTAg&oe=69DC3E7E",
  "instagram_media_type": "VIDEO",
  "image": {
    "height": 640,
    "width": 360
  },
  "comment_count": 485,
  "like_count": 135430,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/likers",
        headers=headers,
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
    "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/324069253_5836767539705305_7097116477300814733_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGE3JteoLJin0VEi6MJYhyxoyLaQY6TpjsaulXEHVBLptWz2rP8laQAMJrPJ8qQYjg&_nc_ohc=hKoACuZrKRgQ7kNvwEwPmw7&_nc_gid=_85y_fxCJbmgM8Pjey222A&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GIXnUBPZNddXgrwUAI0zFn-VBX5ibkULAAAB1501500j-ccb7-5&oh=00_Af1hoS4vj1l6zlTqfXQkIARZ6WupF8bh3RLHuzFTM4VcMg&oe=69DC2518&_nc_sid=bc52df",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "48158574428",
    "id": "48158574428",
    "username": "only_looking_at_fashionpeople",
    "full_name": "",
    "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-19/656236846_18037016978606429_8176123182175805432_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gGE3JteoLJin0VEi6MJYhyxoyLaQY6TpjsaulXEHVBLptWz2rP8laQAMJrPJ8qQYjg&_nc_ohc=8hgiqdDnz8cQ7kNvwEXgxJE&_nc_gid=_85y_fxCJbmgM8Pjey222A&edm=AHUBisUBAAAA&ccb=7-5&ig_cache_key=GC5hHSddSdFFkhRAAPjfbBm3bHdxbmNDAQAB1501500j-ccb7-5&oh=00_Af0CCwr23pa_m_4JaVepvie8WuVwMMeaJnR6L5gI5s_ZdA&oe=69DC48D9&_nc_sid=bc52df",
    "is_private": true,
    "is_verified": false
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/oembed",
        headers=headers,
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
  "thumbnail_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-15/587060691_18613030030019133_432201833451528127_n.jpg?stp=dst-jpg_e35_p640x640_sh0.08_tt6&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2gGvTs836_3WvK-KjlG5fXEa265-hTLdSxKZFcZj5XQKhQr0rRg_85m6NfHzQyt08Gk&_nc_ohc=hXWOKyUXNLwQ7kNvwE0uZP-&_nc_gid=Q4VjJI4BiTJ6bqcdmcIt-Q&edm=ALY_pVYBAAAA&ccb=7-5&oh=00_Af1SjSI5drcUk-ZKKWnPFZgEMAXSohjyiH8fj-FcTTZTdg&oe=69DC3E7E&_nc_sid=57e406",
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/pk/from/code",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/pk/from/url",
        headers=headers,
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

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/media/user",
        headers=headers,
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
  "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGE6MRiwm0VFJpXCP6uXdp4zmT8jIwOZ331AVe_akwoTHUNjcK4bHmjbPtbg5Sq4Mw&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=kWdBOfUX-g22xG8ANuJVDQ&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3MGgftIHLijyxBSEBArU9yIS-dL0QvQ2TSZ0eB8bTSzw&oe=69DC51E9&_nc_sid=fc8dfb",
  "is_private": false,
  "is_verified": true
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-media){ target=_blank }
