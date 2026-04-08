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
            "url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGjDuAtDBssQ1VNb5vdw7yrv4PkJ3t7B_di78SkHiTRaevv269SjeKb6Cd_fv05FBU&_nc_ohc=-NOYVJuE190Q7kNvwG31QQ-&_nc_gid=veINrrRMSbYuNJhDLqgxQg&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af3R8j79gHQwf2zOk_EADq-AF1T2jt-fkXztsFL-CGVIYQ&oe=69DC1EDC&_nc_sid=982cc7",
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
          "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGjDuAtDBssQ1VNb5vdw7yrv4PkJ3t7B_di78SkHiTRaevv269SjeKb6Cd_fv05FBU&_nc_ohc=XbeNvhLXv28Q7kNvwHiwpg4&_nc_gid=veINrrRMSbYuNJhDLqgxQg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2wt0-Ye2mItlg2N-ZkqkaGAA_Ho2tKzDOg0aXhWiSnrA&oe=69DC51E9&_nc_sid=982cc7",
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
            "thumbnail_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/520978025_1226610042597033_6340514479679745090_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=MzY3OTAwMjk1NjMwNjY4NjA2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=MimHeG00MjQQ7kNvwEZKOaJ&_nc_oc=AdoamBVo7PY1eRLI9K8Rq4rfwc0cg7yU-BYFKqNUxGsm47DMNxD-IDTZT5-xBFFzTew&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=veINrrRMSbYuNJhDLqgxQg&_nc_ss=7a3ba&oh=00_Af32pcPk3bSjD1WUCwkpDOX5DrZZgcOqY_-P4-rt1jIEiw&oe=69DC2CAC",
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
            "video_url": "https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNDhHXDqZMqEz2slWNYcNv06IoY5n7k49HZ3iv4nxW5Kw9FpM6EgIUAKO-HPNATzt8wE6X_JGrfEWLi_Ygiv4q9qqXOseNVFOmJJRs.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_ohc=wMrxuyskfRQQ7kNvwECYWgN&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTQzNTg5MjI1NDEyNzc5MiwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e5e224354dcd99b5&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC8wOTRGQTM1OURGMkQzRDIwMEM1QTFDRThBRjY3NzJBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRGxTSFI4bGdXZXJOemdDQUFCUmtsZnFJemtjYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm4Nrx-_b7jAUVAigCQzMsF0Avu2RaHKwIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=veINrrRMSbYuNJhDLqgxQg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3FyeT55P4MfImqXFvNBjjPKoHek_VLGVsDs70oarcSSQ&oe=69DC3F36",
            "video_duration": 15.866000175476074,
            "sponsor_tags": [],
            "mentions": [
              {
                "user": {
                  "pk": "191074609",
                  "id": "191074609",
                  "username": "hulu",
                  "full_name": "Hulu",
                  "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/574400438_18538966897034610_4563057389814688225_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDc5LmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGjDuAtDBssQ1VNb5vdw7yrv4PkJ3t7B_di78SkHiTRaevv269SjeKb6Cd_fv05FBU&_nc_ohc=MW84984-PUoQ7kNvwGNLS_n&_nc_gid=veINrrRMSbYuNJhDLqgxQg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLanPCJyhWaYF91BAOEpoBmFPFM-bmNDAQAB1501500j-ccb7-5&oh=00_Af0MtHowWjyeK5j2-QFhlNzZUWmwvHf5mIsK41hGDFQtvA&oe=69DC3924&_nc_sid=982cc7",
                  "profile_pic_url_hd": null,
                  "is_private": false,
  // ... truncated
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-highlights){ target=_blank }
