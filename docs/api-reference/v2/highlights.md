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
      "https://api.hikerapi.com/v2/highlight/by/id?id=18085475671830440"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.highlight_by_id_v2(id="18085475671830440")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v2/highlight/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "18085475671830440"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/highlight/by/id?id=18085475671830440",
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
      "highlight:18085475671830440": {
        "id": "highlight:18085475671830440",
        "strong_id__": "highlight:18085475671830440",
        "latest_reel_media": 1773304526,
        "seen": null,
        "can_reply": true,
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
            "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/649485671_17878703184529120_5378486390545016366_n.jpg?stp=c0.772.1440.1440a_dst-jpg_e15_s150x150_tt6&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gFBckMKO3umBazAXDJ82ywD9xrbD3I0Yvfo_OacCgltVFQXkDEmaEw1Y9UoizeFFts&_nc_ohc=MJ8q8O6o15UQ7kNvwGBrH_Z&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af19PY1frDyQwPkBQF5SSxvXzuYMv0Sx0BfvW4wRA8fe1Q&oe=69DC5BBB&_nc_sid=982cc7",
            "scans_profile": ""
          },
          "crop_rect": [
            0.0,
            0.30167106,
            1.0
          ],
          "media_id": "3849652044117864571_75885841119",
          "full_image_version": null,
          "upload_id": null
        },
        "user": {
          "strong_id__": "75885841119",
          "pk": "75885841119",
          "pk_id": "75885841119",
          "id": "75885841119",
          "username": "salwaaa_ki",
          "full_name": "𓆩سلوى 𓆪",
          "is_private": false,
          "is_ring_creator": false,
          "show_ring_award": false,
          "is_verified": false,
          "profile_pic_id": "3868671456830255699_75885841119",
          "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/660301771_17883534429529120_6857519161323086524_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gFBckMKO3umBazAXDJ82ywD9xrbD3I0Yvfo_OacCgltVFQXkDEmaEw1Y9UoizeFFts&_nc_ohc=NP_MmBl4lA4Q7kNvwHyOIEs&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GMtnWycgJADV_og-ALziGDNYzSpfbmNDAQAB1501500j-ccb7-5&oh=00_Af07SMjbHdHX5psMVFVpfR5VbIeun70Y4l8uX89PbjdH4g&oe=69DC55BF&_nc_sid=982cc7",
          "interop_messaging_user_fbid": 17843112720529120,
          "is_creator_agent_enabled": false,
          "transparency_product_enabled": false,
          "is_screenshot_blocking_enabled": false
        },
        "items": [
          {
            "pk": "3772053608293416704",
            "id": "3772053608293416704_75885841119",
            "code": "DRZBsWEDz8A",
            "taken_at": "2025-11-23T07:44:11Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/588461508_17863934817529120_8595336332983327927_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzc3MjA1MzYwODI5MzQxNjcwNA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=SdDsQh8WTPEQ7kNvwG__N2r&_nc_oc=Adr_z7-GYiJCeObffvmdjAkk3Ckm46jL3mC-57aBX3tlrp1Sp_23Tmt2MxiWeoF48oM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&_nc_ss=7a3ba&oh=00_Af3EX3JWBIBFNmIM2R4bACBG5_7TVEB8PoNYKk7_J6jvww&oe=69DC576A",
            "user": {
              "pk": "75885841119",
              "id": "75885841119",
              "username": null,
              "full_name": "",
              "profile_pic_url": null,
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": null
            },
            "video_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m78/AQM4454MqF2Hx4p0JOmr3z8YBeoIoKV09Zv1Olvgqw_q2QRA6kfJgBdXiqE4RRda5R47rkZ_juiMq8rESlIW7MTaiVtMAW7MVqFWiB4.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=tRKBzKqdrfUQ7kNvwGQbLEP&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MjMyMTQyMzEwNDk3NDkxNywiYXNzZXRfYWdlX2RheXMiOjEzNiwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=2f4246a0f95d8fbd&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0Q4NEM4REM2MzE0QTQzRUZEQjk0QzA1RjUxOTVDOEJGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhHaWdfeHB2X3JlZWxzX3Blcm1hbmVudF9zcl9wcm9kLzEzNzg3MjcxNTAyNzY4MDZfMzgxOTMxOTgwNjgzNzc0MDMzNy5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmioHd-M3UnwgVAigCQzMsF0A0AAAAAAAAGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2vJh579H4_o7XeJZQHQ5djlIsaqj9-z8EFi4N2BN-cEw&oe=69D84EAA",
            "video_duration": 20.014999389648438,
            "sponsor_tags": [],
            "mentions": [],
            "links": [],
            "hashtags": [],
            "locations": [],
            "stickers": [],
            "medias": []
          },
          {
            "pk": "3773586006193708855",
            "id": "3773586006193708855_75885841119",
            "code": "DReeHq0j583",
            "taken_at": "2025-11-25T10:28:38Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/588154318_728190939725494_5950880813983757081_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ig_cache_key=Mzc3MzU4NjAwNjE5MzcwODg1NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM4LnNkci5DMyJ9&_nc_ohc=RpPP-rAs06gQ7kNvwH_TmB8&_nc_oc=AdohEH70va5462TRXt0VBKioZFMNMzQnqWugeCxOV464yTi3xwCT9cYbW7FkCIXMqF8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&_nc_ss=7a3ba&oh=00_Af1FotyCbY54tZtmcBG38Sjv3yTxqo1PFDjeCYJO7JT-MQ&oe=69DC641B",
            "user": {
              "pk": "75885841119",
              "id": "75885841119",
              "username": null,
              "full_name": "",
              "profile_pic_url": null,
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": null
            },
            "video_url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m78/AQOUjhHv0lGqQdnEa9pFVkGCLHQivW23hFrzQ-TB2B3PJmkSnN-NxgSpslUdeQJ8KwoJqD6eZR_OPbq3LL9dHr0zmBEyTbnCf9Qj034.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=zW5wPjAQE64Q7kNvwHKYG6d&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzE2LmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6ODU0MTY0MTcwMzQzODg4LCJhc3NldF9hZ2VfZGF5cyI6MTM0LCJ2aV91c2VjYXNlX2lkIjoxMDgyNiwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7c7b1bf68b739e99&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U3NDE5QTczMkI3OTAyNjhDRDkzMkFBQTdDNkM2RUExX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhHaWdfeHB2X3JlZWxzX3Blcm1hbmVudF9zcl9wcm9kLzIyMzE2MDE3MDM5ODU4MzBfMjY0MTYyNDkzODUxMzg1OTQ3NS5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmoJeg__K2hAMVAigCQzMsF0A0CHKwIMScGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0TQFpyeupJ2nJ_h9YjclwNbmeiQC0vTA4-LPIgU5NI4g&oe=69D850A2",
            "video_duration": 20.038000106811523,
            "sponsor_tags": [],
            "mentions": [],
            "links": [],
            "hashtags": [],
            "locations": [],
            "stickers": [],
            "medias": []
          },
          {
            "pk": "3777839902093167269",
            "id": "3777839902093167269_75885841119",
            "code": "DRtlWAGj0ql",
            "taken_at": "2025-12-01T07:20:23Z",
            "media_type": 2,
            "product_type": "story",
            "thumbnail_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.71878-15/589062762_864740615926830_8379534102917113604_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ig_cache_key=Mzc3NzgzOTkwMjA5MzE2NzI2OQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bnnfAV02fxIQ7kNvwEsYtXU&_nc_oc=Adp4cUZaqGysmMu12QxhPtGh-IOK0oVWn7_yoZPT1kddFvcZPgEHQ5t2BUzFduhZF5o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&_nc_ss=7a3ba&oh=00_Af2A_jMqcFQli4Qw9Urwb9gr3hF0ZId04ODYHL0vaUQtlg&oe=69DC7303",
            "user": {
              "pk": "75885841119",
              "id": "75885841119",
              "username": null,
              "full_name": "",
              "profile_pic_url": null,
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": null
            },
            "video_url": "https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m78/AQNau6RzELEtOR24qqPISXbOIelAiUNKJjmKX_X_yUtkBJP3icxa9oT4O4uBmWmzXk0ZC1GXflrrKzgK9-_NlP8WwsVSmb6_4yTWJY8.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_ohc=CCbe4i66DY8Q7kNvwGzc6qk&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6ODgxNjg1NTc3NjU4NDg1LCJhc3NldF9hZ2VfZGF5cyI6MTI4LCJ2aV91c2VjYXNlX2lkIjoxMDgyNiwiZHVyYXRpb25fcyI6MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=f44d8c2c62e8f694&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzM5NDQyMkEyQTk2Njg3RTBCNDFEODY2NTkyM0IzQjlCX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhGaWdfeHB2X3JlZWxzX3Blcm1hbmVudF9zcl9wcm9kLzg2NTg2NzgyOTMxMzQ2Nl8yMzQ3NTc0MzExNjc1MDk1OTc3Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbqwce67fiQAxUCKAJDMywXQDQIcrAgxJwYEmRhc2hfYmFzZWxpbmVfMV92MREAdegHZZSpAQA&_nc_gid=SL1au9Z7vomZlSGu-Hwl4w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3IYmlL3eo-OSVwqGgL9OZVNqDjnsQSU5bQZa5tap_IZQ&oe=69D87217",
            "video_duration": 20.038000106811523,
            "sponsor_tags": [],
            "mentions": [],
            "links": [],
            "hashtags": [],
            "locations": [],
            "stickers": [],
            "medias": []
          }
        ],
        "is_nux": false,
        "title": "me 🦋",
        "created_at": 1764138733,
        "is_pinned_highlight": false,
        "media_count": 98,
        "media_ids": [
          3772053608293416704,
          3773586006193708855,
          3777839902093167269
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
        "pk": "18085475671830440"
      }
    },
    "status": "ok"
  }
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-highlights){ target=_blank }
