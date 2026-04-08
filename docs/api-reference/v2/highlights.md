# Highlights Endpoints

Get story highlights by ID.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/highlight/by/id`](#get-v2highlightbyid)

---

### GET /v2/highlight/by/id

Get highlight object by id. Returns a Highlight object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/highlight/by/id?id=17893209825281221"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.highlight_by_id_v2(id="17893209825281221")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/highlight/by/id",
        headers=headers,
        params={"id": "17893209825281221"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/highlight/by/id?id=17893209825281221",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "reels": {
      "highlight:17893209825281221": {
        "id": "highlight:17893209825281221",
        "strong_id__": "highlight:17893209825281221",
        "latest_reel_media": 1752840788,
        "seen": null,
        "can_reply": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "reel_type": "highlight_reel",
        "ad_expiry_timestamp_in_millis": null,
        "is_cta_sticker_available": null,
        "should_treat_link_sticker_as_cta": null,
        "pool_refresh_ttl_in_sec": null,
        "can_react_with_avatar": false,
        "prefetch_count": 0,
        "cover_media": {
          "cropped_image_version": {
            "width": 150,
            "height": 150,
            "url": "https://scontent-ord5-3.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=-NOYVJuE190Q7kNvwFZpeb7&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af3TE4kn3wEiYfXx2ic72Qe3Zrq_vaj0p_X5uoKt1jMGQQ&oe=69DC571C&_nc_sid=982cc7",
            "scans_profile": ""
          },
          "crop_rect": null,
          "media_id": null,
          "full_image_version": null,
          "upload_id": null
        },
        "user": {
          "strong_id__": "787132",
          "pk": "787132",
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_ring_creator": false,
          "show_ring_award": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=XbeNvhLXv28Q7kNvwFu6fZa&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1GuZUNz7pFUiUpZ9dQCgO8QB_8bF_f_h-PGlAs7nq87w&oe=69DC51E9&_nc_sid=982cc7",
          "interop_messaging_user_fbid": 113671860027320,
          "is_creator_agent_enabled": false,
          "transparency_product_enabled": false,
          "is_screenshot_blocking_enabled": false
        },
        "items": [
          {
            "pk": "3679002956306686062",
            "id": "3679002956306686062_787132",
            "code": "DMOcbJSRaBu",
            "taken_at": "2025-07-17T22:29:06Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-ord5-1.cdninstagram.com/v/t51.71878-15/520978025_1226610042597033_6340514479679745090_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=MzY3OTAwMjk1NjMwNjY4NjA2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=MimHeG00MjQQ7kNvwEfmWpB&_nc_oc=AdqA8l6xpCbIfb9V_lRK4h6IU6MnaSiPBaX5OuDhAxNCrx78rbJ2FKaChbs95NrHHUM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ord5-1.cdninstagram.com&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&_nc_ss=7a3ba&oh=00_Af3z7DnPRMKAB4RHND5yQVnOqFAPtTxI2iG_zKjfQ6ljkw&oe=69DC64EC",
            "user": {
              "pk": "787132",
              "id": "787132",
              "username": null,
              "full_name": "",
              "profile_pic_url": null,
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": null
            },
            "video_url": "https://scontent-ord5-3.cdninstagram.com/o1/v/t2/f2/m367/AQNDhHXDqZMqEz2slWNYcNv06IoY5n7k49HZ3iv4nxW5Kw9FpM6EgIUAKO-HPNATzt8wE6X_JGrfEWLi_Ygiv4q9qqXOseNVFOmJJRs.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_ohc=wMrxuyskfRQQ7kNvwF7Ua5p&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTQzNTg5MjI1NDEyNzc5MiwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e5e224354dcd99b5&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC8wOTRGQTM1OURGMkQzRDIwMEM1QTFDRThBRjY3NzJBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRGxTSFI4bGdXZXJOemdDQUFCUmtsZnFJemtjYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm4Nrx-_b7jAUVAigCQzMsF0Avu2RaHKwIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2zaTZ0qgS3D9F7pQOzW1m3h8o4gM6JsnR4TiGxrs6gZw&oe=69DC3F36",
            "video_duration": 15.866000175476074,
            "sponsor_tags": [],
            "mentions": [
              {
                "user": {
                  "pk": "191074609",
                  "id": "191074609",
                  "username": "hulu",
                  "full_name": "Hulu",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/574400438_18538966897034610_4563057389814688225_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDc5LmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=MW84984-PUoQ7kNvwE18dvy&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLanPCJyhWaYF91BAOEpoBmFPFM-bmNDAQAB1501500j-ccb7-5&oh=00_Af3xK8jxXF5hyxB7bPPAMI5KDSXjJ-BA2XO8bkk_X6WSBg&oe=69DC3924&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              },
              {
                "user": {
                  "pk": "1822594644",
                  "id": "1822594644",
                  "username": "chrishemsworth",
                  "full_name": "Chris Hemsworth",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=bzOXlq22QsMQ7kNvwHXEg-V&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af3h36zuuXtMdAdtLT0i2vYMWdn2yh4J8gaJhVFRm3_tBQ&oe=69DC42B4&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              },
              {
                "user": {
                  "pk": "3057496755",
                  "id": "3057496755",
                  "username": "bupa",
                  "full_name": "Bupa",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.2885-19/307996087_7998957096842118_8167638836968273521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=LbTwwe9N8-IQ7kNvwGxHlip&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLelWxKGs1RUAmscAHG2LYs-SFlxbkULAAAB1501500j-ccb7-5&oh=00_Af2GnL4vlek1cz3MxluLjLGixwvlusXZo2aiXpXz1m9MAQ&oe=69DC5025&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              }
            ],
            "links": [],
            "hashtags": [],
            "locations": [],
            "stickers": [],
            "medias": []
          },
          {
            "pk": "3679012649209069648",
            "id": "3679012649209069648_787132",
            "code": "DMOeoMgRoBQ",
            "taken_at": "2025-07-17T22:48:24Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.71878-15/520932106_1074395437998704_3460922945219049185_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ig_cache_key=MzY3OTAxMjY0OTIwOTA2OTY0OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=orZlXTxXLKcQ7kNvwHmmjU6&_nc_oc=Adpuxjtj6inZzI_FXafIQVMalhE0lSaS1zan6v3FMNd1G72Hy1dyiZ73Ul6WWGOZGHo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&_nc_ss=7a3ba&oh=00_Af27_JodMJIW-8I662qphj3XUgcGZ-ppXblzfx5x9_GDAQ&oe=69DC667A",
            "user": {
              "pk": "787132",
              "id": "787132",
              "username": null,
              "full_name": "",
              "profile_pic_url": null,
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": null
            },
            "video_url": "https://scontent-ord5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNX2SZ7rolsa2mMNfU8rrXbW77J-aIkmrrs5QrABSLE5UKZ5dqbjsg2VMeVrVotOhxt7LY94eJ5jgwXwFBATXOprzYn-Jpza96v9IQ.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_ohc=f1S4tEkU7ZMQ7kNvwGxd0Js&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTIxNzE0ODIyNjg1MzIzNywiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933dbe7741e9fd11&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC85MzQwNUM0MkZCMThERDY2Rjc1MEQwQzEyOERENEE5Q192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTW9ZSFJfRk0zRGI5cDhDQUpOMW5FVUdRdzBlYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm6uWa-6y_qQQVAigCQzMsF0AQR64UeuFIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1TQt1OWmXOcOVTpL66xcp9hXJxvGytoTxGLo_WAgiSnA&oe=69DC433A",
            "video_duration": 4.099999904632568,
            "sponsor_tags": [],
            "mentions": [
              {
                "user": {
                  "pk": "1170082468",
                  "id": "1170082468",
                  "username": "elsapataky",
                  "full_name": "Elsa Pataky",
                  "profile_pic_url": "https://scontent-ord5-1.cdninstagram.com/v/t51.2885-19/432119372_1106101867197260_7840673845755369260_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=wfJ2ujo9ZGYQ7kNvwHHAxDJ&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GEyewRlMM_Fo-u0DACzX8S9Sq89sbkULAAAB1501500j-ccb7-5&oh=00_Af3YqGU3_EqY0mEbcLeM4taVEWQgbKc8zuAc2HtBrKaxyA&oe=69DC6979&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              },
              {
                "user": {
                  "pk": "1822594644",
                  "id": "1822594644",
                  "username": "chrishemsworth",
                  "full_name": "Chris Hemsworth",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=bzOXlq22QsMQ7kNvwHXEg-V&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af3h36zuuXtMdAdtLT0i2vYMWdn2yh4J8gaJhVFRm3_tBQ&oe=69DC42B4&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              },
              {
                "user": {
                  "pk": "7522677467",
                  "id": "7522677467",
                  "username": "disneyplus",
                  "full_name": "Disney+",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/608524124_18326358286253468_1598730757163145361_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41NDAuYzIifQ&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=EiOfBngGzLUQ7kNvwFeKH1h&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GFxXRSScva3LuRtBAJFYMzgn1S8WbmNDAQAB1501500j-ccb7-5&oh=00_Af2BRCbVws1_5F7UHG6MBtL_TpB9J82VdpAmxW3lw-OZXg&oe=69DC5776&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              }
            ],
            "links": [],
            "hashtags": [],
            "locations": [],
            "stickers": [],
            "medias": []
          },
          {
            "pk": "3679013557938485210",
            "id": "3679013557938485210_787132",
            "code": "DMOe1a0xPfa",
            "taken_at": "2025-07-17T22:50:12Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-ord5-1.cdninstagram.com/v/t51.71878-15/521950534_1847699322479098_289039560820724406_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=MzY3OTAxMzU1NzkzODQ4NTIxMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=BX4JlLbv6KwQ7kNvwE-UhZq&_nc_oc=AdpxLeA8Tg8IOywKgiWAdRuHzLguWEj5yvlA-g_azpIMIiFBDAR_-UvJeOjgtOXGS_8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ord5-1.cdninstagram.com&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&_nc_ss=7a3ba&oh=00_Af3kXSnbmmpfnBTCIhX-EMYbJhfghSlM-bssoIO8jv0szw&oe=69DC5B51",
            "user": {
              "pk": "787132",
              "id": "787132",
              "username": null,
              "full_name": "",
              "profile_pic_url": null,
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": null
            },
            "video_url": "https://scontent-ord5-3.cdninstagram.com/o1/v/t2/f2/m78/AQPDDzw5BIs_Jomnxa098g7e10lADp-w27j-dCUNSASyQ0eYGRIRdTI3daHCmIyg0D4Coul2d_k0xu41yXt7Wc5gnw9i5hVqyJ1Hrj0.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_ohc=MrB3YdeTtNIQ7kNvwEZfwbf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuMzYwLmRhc2hfYmFzZWxpbmVfM192MSIsInhwdl9hc3NldF9pZCI6MjEwODE4MjE5MzAyNTgyOSwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=9a2d96f17f1f48b6&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U5NENGRjBERURGMEU3NTAzODI3MTlGOTFGOUM0QTlGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dKdzNDeC11ZjZ3c25xZ0NBTzh5X3lHaEdsdHRicGt3QUFBRhUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbKzOWrrdi-BxUCKAJDMywXQBpDlYEGJN0YEmRhc2hfYmFzZWxpbmVfM192MREAdegHZZSpAQA&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3eGd3eArhZ0aKywc-WtyC5RAsQZnImk7CYbwHXd09SpA&oe=69D85CA5",
            "video_duration": 6.54,
            "sponsor_tags": [],
            "mentions": [
              {
                "user": {
                  "pk": "3057496755",
                  "id": "3057496755",
                  "username": "bupa",
                  "full_name": "Bupa",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.2885-19/307996087_7998957096842118_8167638836968273521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=LbTwwe9N8-IQ7kNvwGxHlip&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLelWxKGs1RUAmscAHG2LYs-SFlxbkULAAAB1501500j-ccb7-5&oh=00_Af2GnL4vlek1cz3MxluLjLGixwvlusXZo2aiXpXz1m9MAQ&oe=69DC5025&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": false
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              },
              {
                "user": {
                  "pk": "1822594644",
                  "id": "1822594644",
                  "username": "chrishemsworth",
                  "full_name": "Chris Hemsworth",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=bzOXlq22QsMQ7kNvwHXEg-V&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af3h36zuuXtMdAdtLT0i2vYMWdn2yh4J8gaJhVFRm3_tBQ&oe=69DC42B4&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              },
              {
                "user": {
                  "pk": "7522677467",
                  "id": "7522677467",
                  "username": "disneyplus",
                  "full_name": "Disney+",
                  "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/608524124_18326358286253468_1598730757163145361_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41NDAuYzIifQ&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEbGWOE3_ef8GraC6zsdO7OeAXBNMRmYWlKIaYSXhMJOm_aNvsiVaWDcCyBCA73KAE&_nc_ohc=EiOfBngGzLUQ7kNvwFeKH1h&_nc_gid=Is0QimDZI4dmd_dlz8A-dA&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GFxXRSScva3LuRtBAJFYMzgn1S8WbmNDAQAB1501500j-ccb7-5&oh=00_Af2BRCbVws1_5F7UHG6MBtL_TpB9J82VdpAmxW3lw-OZXg&oe=69DC5776&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
                  "is_verified": true
                },
                "x": 0.0,
                "y": 0.0,
                "width": 0.0,
                "height": 0.0
              }
            ],
            "links": [],
            "hashtags": [],
            "locations": [],
            "stickers": [],
            "medias": []
          }
        ],
        "is_nux": false,
        "title": "Limitless",
        "created_at": 1754674432,
        "is_pinned_highlight": false,
        "media_count": 11,
        "media_ids": [
          3679002956306686062,
          3679012649209069648,
          3679013557938485210
        ],
        "is_cacheable": true,
        "is_converted_to_clips": false,
        "disabled_reply_types": [
          "story_remix_reply",
          "story_selfie_reply",
          "story_voice_reply"
        ],
        "highlight_reel_type": "DEFAULT",
        "is_added_to_main_grid": false,
        "is_archived": false,
        "show_expiration_tray_signal": false,
        "pk": "17893209825281221"
      }
    },
    "status": "ok"
  }
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-highlights){ target=_blank }
