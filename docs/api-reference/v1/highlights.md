# Highlights Endpoints

Get story highlights by ID or URL.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/highlight/by/id`](#get-v1highlightbyid) | [`/v1/highlight/by/url`](#get-v1highlightbyurl) | [`/v1/user/highlights`](#get-v1userhighlights) | [`/v1/user/highlights/by/username`](#get-v1userhighlightsbyusername)

---

### GET /v1/highlight/by/id

Prefer v2/highlight/by/id. Returns a Highlight object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/highlight/by/id?id=18085475671830440"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/highlight/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"id": "18085475671830440"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/highlight/by/id?id=18085475671830440",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "17893209825281221",
  "id": "highlight:17893209825281221",
  "latest_reel_media": 1752840788,
  "cover_media": {
    "cropped_image_version": {
      "width": 150,
      "height": 150,
      "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=-NOYVJuE190Q7kNvwHbTvBQ&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af3xdNjj-ffr9NjuxkK9udF_8Tz7FGc3ddDEZR0zsiLrGQ&oe=69DC571C&_nc_sid=982cc7",
      "scans_profile": ""
    },
    "crop_rect": null,
    "media_id": null,
    "full_image_version": null,
    "upload_id": null
  },
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=XbeNvhLXv28Q7kNvwE-hbvZ&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0tjuQwSg8pZmC4uhGZmuVHKF-rDv9Kiry7n7PO_0AlFQ&oe=69DC51E9&_nc_sid=982cc7",
    "profile_pic_url_hd": null,
    "is_private": false,
    "is_verified": true
  },
  "title": "Limitless",
  "created_at": "2025-08-08T17:33:52+00:00",
  "is_pinned_highlight": false,
  "media_count": 11,
  "media_ids": [
    3679002956306686062,
    3679012649209069648,
    3679013557938485210
  ],
  "items": [
    {
      "pk": "3679002956306686062",
      "id": "3679002956306686062_787132",
      "code": "DMOcbJSRaBu",
      "taken_at": "2025-07-17T22:29:06+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/520978025_1226610042597033_6340514479679745090_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=MzY3OTAwMjk1NjMwNjY4NjA2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=MimHeG00MjQQ7kNvwHb7FuD&_nc_oc=AdqpDCSnFRsJnWHu6pQo0tef2L39UccQ7bVihvTYiFRw-LGYFbpNntxYdEOWu7sNPv8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&_nc_ss=7a3ba&oh=00_Af1Cg5WQjHmpBompVFcsCkIC4eeswO7mX5iufcgGz647TQ&oe=69DC64EC",
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
      "video_url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNDhHXDqZMqEz2slWNYcNv06IoY5n7k49HZ3iv4nxW5Kw9FpM6EgIUAKO-HPNATzt8wE6X_JGrfEWLi_Ygiv4q9qqXOseNVFOmJJRs.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=wMrxuyskfRQQ7kNvwHeXEZa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTQzNTg5MjI1NDEyNzc5MiwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e5e224354dcd99b5&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC8wOTRGQTM1OURGMkQzRDIwMEM1QTFDRThBRjY3NzJBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRGxTSFI4bGdXZXJOemdDQUFCUmtsZnFJemtjYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm4Nrx-_b7jAUVAigCQzMsF0Avu2RaHKwIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0bmNXvoGs4LTSOfD-qLiVgfd8BDAm-d4yLLJI6B6LwgQ&oe=69DC3F36",
      "video_duration": 15.866000175476074,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "191074609",
            "id": "191074609",
            "username": "hulu",
            "full_name": "Hulu",
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/574400438_18538966897034610_4563057389814688225_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDc5LmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=MW84984-PUoQ7kNvwFAP-zT&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLanPCJyhWaYF91BAOEpoBmFPFM-bmNDAQAB1501500j-ccb7-5&oh=00_Af2LktgSufv9gvO3i6L0xE_2X_ZPt1fcZR4z2oNAj7IVfQ&oe=69DC3924&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=bzOXlq22QsMQ7kNvwF_bRwL&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af0yAgM5H2fw10DkeroCD5T0aHNJDzZY8A9Zzd5z5W1SyQ&oe=69DC42B4&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/307996087_7998957096842118_8167638836968273521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=LbTwwe9N8-IQ7kNvwHdSVXL&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLelWxKGs1RUAmscAHG2LYs-SFlxbkULAAAB1501500j-ccb7-5&oh=00_Af2FxJs6mqTl7prQKDtQPIf8-VF_a2bSElGoHxegHUg0Yw&oe=69DC5025&_nc_sid=982cc7",
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
      "taken_at": "2025-07-17T22:48:24+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/520932106_1074395437998704_3460922945219049185_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ig_cache_key=MzY3OTAxMjY0OTIwOTA2OTY0OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=orZlXTxXLKcQ7kNvwGF2lcg&_nc_oc=AdrfVzORGQTVywsMKoII3OIJah-EfmyQmQgRFS8w8C7ml54DjvE0bs5G8vh-UooYAAQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&_nc_ss=7a3ba&oh=00_Af3--HDeZOe8QlZtpNe4rN3myYON9No6s-EswOqJ_-_jbA&oe=69DC667A",
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
      "video_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNX2SZ7rolsa2mMNfU8rrXbW77J-aIkmrrs5QrABSLE5UKZ5dqbjsg2VMeVrVotOhxt7LY94eJ5jgwXwFBATXOprzYn-Jpza96v9IQ.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=f1S4tEkU7ZMQ7kNvwFJYD48&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTIxNzE0ODIyNjg1MzIzNywiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933dbe7741e9fd11&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC85MzQwNUM0MkZCMThERDY2Rjc1MEQwQzEyOERENEE5Q192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTW9ZSFJfRk0zRGI5cDhDQUpOMW5FVUdRdzBlYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm6uWa-6y_qQQVAigCQzMsF0AQR64UeuFIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Fd9cHEnHtDOLg-wuG3LiDBAW_H6HuRVqoQlPWvsVNWw&oe=69DC433A",
      "video_duration": 4.070000171661377,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "1170082468",
            "id": "1170082468",
            "username": "elsapataky",
            "full_name": "Elsa Pataky",
            "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/432119372_1106101867197260_7840673845755369260_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=wfJ2ujo9ZGYQ7kNvwGFr2Jj&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GEyewRlMM_Fo-u0DACzX8S9Sq89sbkULAAAB1501500j-ccb7-5&oh=00_Af3-ir1VgV3dJPHMTM_7ZgLdDV6O0q_7Mo4P-iDEr9yMzw&oe=69DC6979&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=bzOXlq22QsMQ7kNvwF_bRwL&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af0yAgM5H2fw10DkeroCD5T0aHNJDzZY8A9Zzd5z5W1SyQ&oe=69DC42B4&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/608524124_18326358286253468_1598730757163145361_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41NDAuYzIifQ&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=EiOfBngGzLUQ7kNvwHVTDQW&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GFxXRSScva3LuRtBAJFYMzgn1S8WbmNDAQAB1501500j-ccb7-5&oh=00_Af2YoERUwg_uRNqhSu8TwqSBAWwOpL8frt64G34w5r8fbw&oe=69DC5776&_nc_sid=982cc7",
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
      "taken_at": "2025-07-17T22:50:12+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.71878-15/521950534_1847699322479098_289039560820724406_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=MzY3OTAxMzU1NzkzODQ4NTIxMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=BX4JlLbv6KwQ7kNvwHBTNnb&_nc_oc=Adpp6p8jgcZp0Zz_ihvls0XrFh3aH7B6KKIKmUd75ZglfKO5aIlRR9o4M86pPto1dIg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&_nc_ss=7a3ba&oh=00_Af1ds86NYER1_TGYlWyTPIIYDHN1BXNJ7v2kkn0R8Qf5RQ&oe=69DC5B51",
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
      "video_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m78/AQPDDzw5BIs_Jomnxa098g7e10lADp-w27j-dCUNSASyQ0eYGRIRdTI3daHCmIyg0D4Coul2d_k0xu41yXt7Wc5gnw9i5hVqyJ1Hrj0.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=MrB3YdeTtNIQ7kNvwEUuTgZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuMzYwLmRhc2hfYmFzZWxpbmVfM192MSIsInhwdl9hc3NldF9pZCI6MjEwODE4MjE5MzAyNTgyOSwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=9a2d96f17f1f48b6&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U5NENGRjBERURGMEU3NTAzODI3MTlGOTFGOUM0QTlGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dKdzNDeC11ZjZ3c25xZ0NBTzh5X3lHaEdsdHRicGt3QUFBRhUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbKzOWrrdi-BxUCKAJDMywXQBpDlYEGJN0YEmRhc2hfYmFzZWxpbmVfM192MREAdegHZZSpAQA&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af37_HGg9zZ9zvqjEpXOcsEJ9tQQUTH9SeVCTCC3nkwXuA&oe=69D85CA5",
      "video_duration": 6.539999961853027,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "3057496755",
            "id": "3057496755",
            "username": "bupa",
            "full_name": "Bupa",
            "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/307996087_7998957096842118_8167638836968273521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=LbTwwe9N8-IQ7kNvwHdSVXL&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLelWxKGs1RUAmscAHG2LYs-SFlxbkULAAAB1501500j-ccb7-5&oh=00_Af2FxJs6mqTl7prQKDtQPIf8-VF_a2bSElGoHxegHUg0Yw&oe=69DC5025&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=bzOXlq22QsMQ7kNvwF_bRwL&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af0yAgM5H2fw10DkeroCD5T0aHNJDzZY8A9Zzd5z5W1SyQ&oe=69DC42B4&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/608524124_18326358286253468_1598730757163145361_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41NDAuYzIifQ&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGQmlXVs7jOFcVmB3ieMmSeYveFZ2_SM5zqHQLcXOslgqJZzUJ9QgiGijpC0gE5T8g&_nc_ohc=EiOfBngGzLUQ7kNvwHVTDQW&_nc_gid=u_n_SoN5N3oZfvFzwInFxg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GFxXRSScva3LuRtBAJFYMzgn1S8WbmNDAQAB1501500j-ccb7-5&oh=00_Af2YoERUwg_uRNqhSu8TwqSBAWwOpL8frt64G34w5r8fbw&oe=69DC5776&_nc_sid=982cc7",
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
  ]
}
```

</details>

---

### GET /v1/highlight/by/url

Get highlight object by id. Returns a Highlight object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/18085475671830440/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.highlight_by_url_v1(url="https://www.instagram.com/stories/highlights/18085475671830440/")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/highlight/by/url",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"url": "https://www.instagram.com/stories/highlights/18085475671830440/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/highlight/by/url?url=https://www.instagram.com/stories/highlights/18085475671830440/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "17893209825281221",
  "id": "highlight:17893209825281221",
  "latest_reel_media": 1752840788,
  "cover_media": {
    "cropped_image_version": {
      "width": 150,
      "height": 150,
      "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=-NOYVJuE190Q7kNvwHx0rmN&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&oh=00_Af1HpFY4Sd6_cN3MUd8S0nB-mP_ON5dQwlfTT_WgZx1OUw&oe=69DC571C&_nc_sid=982cc7",
      "scans_profile": ""
    },
    "crop_rect": null,
    "media_id": null,
    "full_image_version": null,
    "upload_id": null
  },
  "user": {
    "pk": "787132",
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=XbeNvhLXv28Q7kNvwHavHOf&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3yTv8rfHhEMlnasynF1uUhmX3ozThe3AcPfRPAOUvbrw&oe=69DC51E9&_nc_sid=982cc7",
    "profile_pic_url_hd": null,
    "is_private": false,
    "is_verified": true
  },
  "title": "Limitless",
  "created_at": "2025-08-08T17:33:52+00:00",
  "is_pinned_highlight": false,
  "media_count": 11,
  "media_ids": [
    3679002956306686062,
    3679012649209069648,
    3679013557938485210
  ],
  "items": [
    {
      "pk": "3679002956306686062",
      "id": "3679002956306686062_787132",
      "code": "DMOcbJSRaBu",
      "taken_at": "2025-07-17T22:29:06+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.71878-15/520978025_1226610042597033_6340514479679745090_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=MzY3OTAwMjk1NjMwNjY4NjA2Mg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=MimHeG00MjQQ7kNvwFTyKbK&_nc_oc=Adrqri4XkW31asHu7FSoqduH2gdqk-9Uuxu8zXUTvnx-tljruTrqKRRkyUZUcDaXz18&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&_nc_ss=7a3ba&oh=00_Af1FHEAQwy1bzB0jZbZ1ic5FuxY2nzJd9urfg1p9Y6wdDQ&oe=69DC64EC",
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
      "video_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNDhHXDqZMqEz2slWNYcNv06IoY5n7k49HZ3iv4nxW5Kw9FpM6EgIUAKO-HPNATzt8wE6X_JGrfEWLi_Ygiv4q9qqXOseNVFOmJJRs.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=wMrxuyskfRQQ7kNvwHtY72V&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTQzNTg5MjI1NDEyNzc5MiwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=e5e224354dcd99b5&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC8wOTRGQTM1OURGMkQzRDIwMEM1QTFDRThBRjY3NzJBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRGxTSFI4bGdXZXJOemdDQUFCUmtsZnFJemtjYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm4Nrx-_b7jAUVAigCQzMsF0Avu2RaHKwIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3FMOVxOCApjRVIkH9Ffr_A6GW7u5Ya3yNZBV4fqW1L-g&oe=69DC3F36",
      "video_duration": 15.866000175476074,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "191074609",
            "id": "191074609",
            "username": "hulu",
            "full_name": "Hulu",
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/574400438_18538966897034610_4563057389814688225_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDc5LmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=MW84984-PUoQ7kNvwGN4qim&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLanPCJyhWaYF91BAOEpoBmFPFM-bmNDAQAB1501500j-ccb7-5&oh=00_Af0k8Ti0FCSgzuHJmei1Q6MLls_-fTs5K3yrdCrbYr8nCA&oe=69DC3924&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=bzOXlq22QsMQ7kNvwF0ATQD&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af0CYop7MrOdAWTWbSZVIb6gk01d_QT05_nYgtIJ52fqeg&oe=69DC42B4&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.2885-19/307996087_7998957096842118_8167638836968273521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=LbTwwe9N8-IQ7kNvwGcIMOg&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLelWxKGs1RUAmscAHG2LYs-SFlxbkULAAAB1501500j-ccb7-5&oh=00_Af0gr4eYPNtnxfz03zsh6esZvZeF3oFRVt_JF4Z25wy7cg&oe=69DC5025&_nc_sid=982cc7",
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
      "taken_at": "2025-07-17T22:48:24+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.71878-15/520932106_1074395437998704_3460922945219049185_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ig_cache_key=MzY3OTAxMjY0OTIwOTA2OTY0OA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=orZlXTxXLKcQ7kNvwGtgRBH&_nc_oc=AdrzKIOt9J2XtyNSHurlqisEgCp91qYtPxcuNm0QAjHNN528zgM-43EMAUCP7KhlBw0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&_nc_ss=7a3ba&oh=00_Af13ye_IW_NlOUWTNwttAydlGn3Fg1zWlldrPbNvgeDliw&oe=69DC667A",
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
      "video_url": "https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNX2SZ7rolsa2mMNfU8rrXbW77J-aIkmrrs5QrABSLE5UKZ5dqbjsg2VMeVrVotOhxt7LY94eJ5jgwXwFBATXOprzYn-Jpza96v9IQ.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_ohc=f1S4tEkU7ZMQ7kNvwESYmZT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTIxNzE0ODIyNjg1MzIzNywiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933dbe7741e9fd11&_nc_vs=HBksFQIYQGlnX2VwaGVtZXJhbC85MzQwNUM0MkZCMThERDY2Rjc1MEQwQzEyOERENEE5Q192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTW9ZSFJfRk0zRGI5cDhDQUpOMW5FVUdRdzBlYnBrd0FBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm6uWa-6y_qQQVAigCQzMsF0AQR64UeuFIGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXoB2WUqQEA&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3F0gL32Y5xfyPJ0ozSXHce3zP6ZDxpP3oP33Gi0iEaSQ&oe=69DC433A",
      "video_duration": 4.070000171661377,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "1170082468",
            "id": "1170082468",
            "username": "elsapataky",
            "full_name": "Elsa Pataky",
            "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.2885-19/432119372_1106101867197260_7840673845755369260_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=wfJ2ujo9ZGYQ7kNvwF1J0wG&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GEyewRlMM_Fo-u0DACzX8S9Sq89sbkULAAAB1501500j-ccb7-5&oh=00_Af3l5gdFssr5HD3KNQ76_KibuQfkrmI-HdS4s34TRY4LPQ&oe=69DC6979&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=bzOXlq22QsMQ7kNvwF0ATQD&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af0CYop7MrOdAWTWbSZVIb6gk01d_QT05_nYgtIJ52fqeg&oe=69DC42B4&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/608524124_18326358286253468_1598730757163145361_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41NDAuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=EiOfBngGzLUQ7kNvwHTzcJS&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GFxXRSScva3LuRtBAJFYMzgn1S8WbmNDAQAB1501500j-ccb7-5&oh=00_Af1rZPs_xq5qGoOaWqCrrr4C6FXoBQnuZ_YLmJDw4JJOwA&oe=69DC5776&_nc_sid=982cc7",
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
      "taken_at": "2025-07-17T22:50:12+00:00",
      "media_type": 2,
      "product_type": "story",
      "thumbnail_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/521950534_1847699322479098_289039560820724406_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=111&ig_cache_key=MzY3OTAxMzU1NzkzODQ4NTIxMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=BX4JlLbv6KwQ7kNvwHwEuza&_nc_oc=Adr5lgvkhfrb7qaCQpWBq2M3jpxs_MfZzI7qYEwmJlPFHtUb9YmfnepNkHouQxQRNlQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&_nc_ss=7a3ba&oh=00_Af2EJhaf_nPI0LgSAKn7nThwuDWhuNSna3atXFTIJ-V5vA&oe=69DC5B51",
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
      "video_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQPDDzw5BIs_Jomnxa098g7e10lADp-w27j-dCUNSASyQ0eYGRIRdTI3daHCmIyg0D4Coul2d_k0xu41yXt7Wc5gnw9i5hVqyJ1Hrj0.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=MrB3YdeTtNIQ7kNvwEL2MAf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuMzYwLmRhc2hfYmFzZWxpbmVfM192MSIsInhwdl9hc3NldF9pZCI6MjEwODE4MjE5MzAyNTgyOSwiYXNzZXRfYWdlX2RheXMiOjI2NCwidmlfdXNlY2FzZV9pZCI6MTA4MjYsImR1cmF0aW9uX3MiOjYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=9a2d96f17f1f48b6&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U5NENGRjBERURGMEU3NTAzODI3MTlGOTFGOUM0QTlGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dKdzNDeC11ZjZ3c25xZ0NBTzh5X3lHaEdsdHRicGt3QUFBRhUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbKzOWrrdi-BxUCKAJDMywXQBpDlYEGJN0YEmRhc2hfYmFzZWxpbmVfM192MREAdegHZZSpAQA&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0AP2s2UXwUF4BF_CrcZKnP8gdumXci9ohNyERagAUCVg&oe=69D85CA5",
      "video_duration": 6.539999961853027,
      "sponsor_tags": [],
      "mentions": [
        {
          "user": {
            "pk": "3057496755",
            "id": "3057496755",
            "username": "bupa",
            "full_name": "Bupa",
            "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.2885-19/307996087_7998957096842118_8167638836968273521_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=LbTwwe9N8-IQ7kNvwGcIMOg&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GLelWxKGs1RUAmscAHG2LYs-SFlxbkULAAAB1501500j-ccb7-5&oh=00_Af0gr4eYPNtnxfz03zsh6esZvZeF3oFRVt_JF4Z25wy7cg&oe=69DC5025&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/91933099_242760747110457_2301125283991781376_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NTAuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=bzOXlq22QsMQ7kNvwF0ATQD&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GKvJegU50BgkytwAAAAAAABBPe8fbkULAAAB1501500j-ccb7-5&oh=00_Af0CYop7MrOdAWTWbSZVIb6gk01d_QT05_nYgtIJ52fqeg&oe=69DC42B4&_nc_sid=982cc7",
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
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/608524124_18326358286253468_1598730757163145361_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41NDAuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEyt_fEeO8XtaQltDHaiqr99GQXLW_xEeJ2GTtl7AiUO030Syf_RtHO1cnARyMmZ40&_nc_ohc=EiOfBngGzLUQ7kNvwHTzcJS&_nc_gid=UQ7q4HcuvUZ2vsFZKUNfSg&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=GFxXRSScva3LuRtBAJFYMzgn1S8WbmNDAQAB1501500j-ccb7-5&oh=00_Af1rZPs_xq5qGoOaWqCrrr4C6FXoBQnuZ_YLmJDw4JJOwA&oe=69DC5776&_nc_sid=982cc7",
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
  ]
}
```

</details>

---

### GET /v1/user/highlights

⚠️ Billing: 2 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/highlights?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/highlights?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17983616051768088",
    "id": "highlight:17983616051768088",
    "latest_reel_media": 1766242839,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gGSZwxnDnUISqs7GNRiZcKp6kNURKMaWlfxxzYNd1_oLHzmDICbgH2OE9tG--_qEZo&_nc_ohc=y1uvOTY1dWMQ7kNvwFTV-Yx&_nc_gid=ZsXyqCR8dU2gdfNHq_HgWg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af2reVbFP951Vc_jHYpliGh0OocXhyjhQIbGsD6OlEWK0A&oe=69DC397C&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGSZwxnDnUISqs7GNRiZcKp6kNURKMaWlfxxzYNd1_oLHzmDICbgH2OE9tG--_qEZo&_nc_ohc=XbeNvhLXv28Q7kNvwHZ2taI&_nc_gid=ZsXyqCR8dU2gdfNHq_HgWg&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af17jpd6qnZeFcsNPm8Djm_XvOTorTLC2ipQDEtHbjAngA&oe=69DC51E9&_nc_sid=847350",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Gift Guide",
    "created_at": "2025-12-04T11:06:31Z",
    "is_pinned_highlight": false,
    "media_count": 12,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "18018069326790931",
    "id": "highlight:18018069326790931",
    "latest_reel_media": 1762870363,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gGSZwxnDnUISqs7GNRiZcKp6kNURKMaWlfxxzYNd1_oLHzmDICbgH2OE9tG--_qEZo&_nc_ohc=KnNItKNMJcAQ7kNvwHMJoJY&_nc_gid=ZsXyqCR8dU2gdfNHq_HgWg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af3xaD5Fac6M5TkfAYH1b5czUHFXJZ81DaGo17omx9_clg&oe=69DC5233&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGSZwxnDnUISqs7GNRiZcKp6kNURKMaWlfxxzYNd1_oLHzmDICbgH2OE9tG--_qEZo&_nc_ohc=XbeNvhLXv28Q7kNvwHZ2taI&_nc_gid=ZsXyqCR8dU2gdfNHq_HgWg&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af17jpd6qnZeFcsNPm8Djm_XvOTorTLC2ipQDEtHbjAngA&oe=69DC51E9&_nc_sid=847350",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "BOTW 2026",
    "created_at": "2025-10-21T13:07:47Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "17893209825281221",
    "id": "highlight:17893209825281221",
    "latest_reel_media": 1752840788,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGSZwxnDnUISqs7GNRiZcKp6kNURKMaWlfxxzYNd1_oLHzmDICbgH2OE9tG--_qEZo&_nc_ohc=-NOYVJuE190Q7kNvwGOT1R5&_nc_gid=ZsXyqCR8dU2gdfNHq_HgWg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af1EgEH3GNqI3K-91PixPp45OXosUFfJNA_giNK5KE1eoQ&oe=69DC571C&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGSZwxnDnUISqs7GNRiZcKp6kNURKMaWlfxxzYNd1_oLHzmDICbgH2OE9tG--_qEZo&_nc_ohc=XbeNvhLXv28Q7kNvwHZ2taI&_nc_gid=ZsXyqCR8dU2gdfNHq_HgWg&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af17jpd6qnZeFcsNPm8Djm_XvOTorTLC2ipQDEtHbjAngA&oe=69DC51E9&_nc_sid=847350",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Limitless",
    "created_at": "2025-08-08T17:33:52Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  }
]
```

</details>

---

### GET /v1/user/highlights/by/username

⚠️ Billing: 3 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/highlights/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_by_username_v1(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/user/highlights/by/username",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/highlights/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17983616051768088",
    "id": "highlight:17983616051768088",
    "latest_reel_media": 1766242839,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-ord5-2.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFFZfy_N9nPCILjCvlwM1NiQhk8NKnc_LYtmixrOJkK6YbF4VC6bDfxyDClK68nlH8&_nc_ohc=y1uvOTY1dWMQ7kNvwHd9TFp&_nc_gid=7oT0qjG-Meoj5VHvDd4HEg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af2Q3TCM4rrgcR1TUg8pR_BO2VHtFj8iw0yGAZQgeZYZRg&oe=69DC397C&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFFZfy_N9nPCILjCvlwM1NiQhk8NKnc_LYtmixrOJkK6YbF4VC6bDfxyDClK68nlH8&_nc_ohc=XbeNvhLXv28Q7kNvwFu6fZa&_nc_gid=7oT0qjG-Meoj5VHvDd4HEg&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0KYKSUOs92qx8Y-T9wFPopmK8o401SZp6Z6gYN2kA0Cg&oe=69DC51E9&_nc_sid=847350",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Gift Guide",
    "created_at": "2025-12-04T11:06:31Z",
    "is_pinned_highlight": false,
    "media_count": 12,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "18018069326790931",
    "id": "highlight:18018069326790931",
    "latest_reel_media": 1762870363,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-ord5-2.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gFFZfy_N9nPCILjCvlwM1NiQhk8NKnc_LYtmixrOJkK6YbF4VC6bDfxyDClK68nlH8&_nc_ohc=KnNItKNMJcAQ7kNvwFnYoK_&_nc_gid=7oT0qjG-Meoj5VHvDd4HEg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af35sKku3TFP9pHVzxnM-SHullCU90Nub3GC3Nzk20d2Wg&oe=69DC5233&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFFZfy_N9nPCILjCvlwM1NiQhk8NKnc_LYtmixrOJkK6YbF4VC6bDfxyDClK68nlH8&_nc_ohc=XbeNvhLXv28Q7kNvwFu6fZa&_nc_gid=7oT0qjG-Meoj5VHvDd4HEg&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0KYKSUOs92qx8Y-T9wFPopmK8o401SZp6Z6gYN2kA0Cg&oe=69DC51E9&_nc_sid=847350",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "BOTW 2026",
    "created_at": "2025-10-21T13:07:47Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  },
  {
    "pk": "17893209825281221",
    "id": "highlight:17893209825281221",
    "latest_reel_media": 1752840788,
    "cover_media": {
      "crop_rect": null,
      "media_id": null,
      "upload_id": null,
      "cropped_image_version": {
        "height": 150,
        "scans_profile": "",
        "url": "https://scontent-ord5-3.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFFZfy_N9nPCILjCvlwM1NiQhk8NKnc_LYtmixrOJkK6YbF4VC6bDfxyDClK68nlH8&_nc_ohc=-NOYVJuE190Q7kNvwFZpeb7&_nc_gid=7oT0qjG-Meoj5VHvDd4HEg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af07q5ZcMgKhfUpJ6PsAAuVHiENREw1gLStE-vN-3eJAig&oe=69DC571C&_nc_sid=847350",
        "width": 150
      },
      "full_image_version": null
    },
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFFZfy_N9nPCILjCvlwM1NiQhk8NKnc_LYtmixrOJkK6YbF4VC6bDfxyDClK68nlH8&_nc_ohc=XbeNvhLXv28Q7kNvwFu6fZa&_nc_gid=7oT0qjG-Meoj5VHvDd4HEg&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0KYKSUOs92qx8Y-T9wFPopmK8o401SZp6Z6gYN2kA0Cg&oe=69DC51E9&_nc_sid=847350",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "title": "Limitless",
    "created_at": "2025-08-08T17:33:52Z",
    "is_pinned_highlight": false,
    "media_count": 11,
    "media_ids": [],
    "items": []
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-highlights){ target=_blank }
