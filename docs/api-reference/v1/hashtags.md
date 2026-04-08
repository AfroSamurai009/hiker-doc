# Hashtag Endpoints

Get hashtag info, top and recent media.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/hashtag/by/name`](#get-v1hashtagbyname) | [`/v1/hashtag/medias/clips`](#get-v1hashtagmediasclips) | [`/v1/hashtag/medias/clips/chunk`](#get-v1hashtagmediasclipschunk) | [`/v1/hashtag/medias/recent`](#get-v1hashtagmediasrecent) | [`/v1/hashtag/medias/recent/chunk`](#get-v1hashtagmediasrecentchunk) | [`/v1/hashtag/medias/top`](#get-v1hashtagmediastop) | [`/v1/hashtag/medias/top/chunk`](#get-v1hashtagmediastopchunk) | [`/v1/hashtag/medias/top/recent/chunk`](#get-v1hashtagmediastoprecentchunk)

---

### GET /v1/hashtag/by/name

Get hashtag object by name. Returns a Hashtag object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/by/name?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_by_name_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/by/name",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/by/name?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "id": "17843826142012701",
  "name": "love",
  "media_count": 2147483647,
  "allow_following": false,
  "profile_pic_url": null
}
```

</details>

---

### GET /v1/hashtag/medias/clips

Get hashtag clips (reels). Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/clips?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_clips_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/clips",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/clips?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870711225189699935",
    "id": "3870711225189699935_501243330",
    "code": "DW3h1n1jJFf",
    "taken_at": "2026-04-08T10:40:30Z",
    "taken_at_ts": 1775644830,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwGtoMIc&_nc_oc=Adp1_liK9CsQNmtO77zecLiRk64oF9Ku_ZDIDKIJlchX5oqc_tguCtJvSvSl0tWyU6c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af0UHG02eXEsEoafbEZo1PUiuDIgPEdOs4shaldkx9jZLw&oe=69DC2620",
    "location": {
      "pk": 1031791313,
      "name": "Davies Coaches LTD",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "The Old Colliery",
      "city": "",
      "zip": null,
      "lng": -4.0678841390208,
      "lat": 51.774418090574,
      "external_id": "272344219549251",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "501243330",
      "id": "501243330",
      "username": "gkfentonn",
      "full_name": "Georgina Fenton",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFnnpySmXw1k1aK86pbe4MoxlhmxXM1Os4rwQBDOhZPEEVBlRdgot8qTkMlWJ_OIG4&_nc_ohc=n-uwrwSVU3kQ7kNvwE0Iokh&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af13lX2tTuFzgncW4FK_dZtI_gDx8h4EzSHIwK0FBE67rA&oe=69DC425F&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 279,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Summer Pending🕶️☀️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n#love\n#instagood\n#photooftheday\n#viral \n#beautiful",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          54433,
          108867
        ],
        "height": 1820,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwGtoMIc&_nc_oc=Adp1_liK9CsQNmtO77zecLiRk64oF9Ku_ZDIDKIJlchX5oqc_tguCtJvSvSl0tWyU6c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af0UHG02eXEsEoafbEZo1PUiuDIgPEdOs4shaldkx9jZLw&oe=69DC2620",
        "width": 1365,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          28402,
          56804
        ],
        "height": 1000,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwGtoMIc&_nc_oc=Adp1_liK9CsQNmtO77zecLiRk64oF9Ku_ZDIDKIJlchX5oqc_tguCtJvSvSl0tWyU6c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af1PB_5Tkzy4gLhQnwt79jACQEkk12Vm4xW0TNhwg7GbLg&oe=69DC2620",
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
    "pk": "3870764609041488625",
    "id": "3870764609041488625_78271797955",
    "code": "DW3t-dbElrx",
    "taken_at": "2026-04-08T12:29:31Z",
    "taken_at_ts": 1775651371,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/669431258_17864434017613956_8282760181895932089_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc2NDYwOTA0MTQ4ODYyNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=ntVDJ-oP18cQ7kNvwEojqWR&_nc_oc=AdoQGPIS0p6KcCeI-Lv4iv47NlIFc4la9F1j_4O3R1dndBosFu6k85We0OJQRCzzgJM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af3JVhb8nx-LYDIWywfQ8gJ-QptB_Ta5k-jK6ZgJpsSH1g&oe=69DC4A1D",
    "location": {
      "pk": 1271876592870320,
      "name": "அருள்மிகு பழனி ஆண்டவர் திருக்கோயில் சன்னதி",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "",
      "city": "",
      "zip": null,
      "lng": 77.520518302917,
      "lat": 10.438720723335,
      "external_id": "1271876592870320",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "78271797955",
      "id": "78271797955",
      "username": "life_with_murugan_",
      "full_name": "life_with_murugan_",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/657876395_17863436862613956_7878740436612381417_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFnnpySmXw1k1aK86pbe4MoxlhmxXM1Os4rwQBDOhZPEEVBlRdgot8qTkMlWJ_OIG4&_nc_ohc=XM8-yGGbd7gQ7kNvwEQFi0N&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GKtlNifE6amAs3Y-AOl6yQmv6FZtbmNDAQAB1501500j-ccb7-5&oh=00_Af11Hxx3L2-llcfLQWgLOIlTcJVC8wSl6fznuxpZf_IWKg&oe=69DC392F&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 731,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "யாமிருக்க பயமேன்🦚🥹💯🛐\n.\n.\n#murugan #palani #lordmurugan #trending #love",
    "accessibility_caption": null,
    "usertags": [
      {
        "user": {
          "pk": "34328168544",
          "id": "34328168544",
          "username": "palani94_official",
          "full_name": "𝐖𝐨𝐫𝐥𝐝 𝐨𝐟 𝐩𝐚𝐥𝐚𝐧𝐢..!❤️",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/582096616_18080552873144545_8148477502297939851_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gFnnpySmXw1k1aK86pbe4MoxlhmxXM1Os4rwQBDOhZPEEVBlRdgot8qTkMlWJ_OIG4&_nc_ohc=uCx56mgwTB0Q7kNvwHSANwo&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GOgWsiLhsFjDKjxAAIsfu6gdNRVxbmNDAQAB1501500j-ccb7-5&oh=00_Af2pwfJcm-AhM1GijOhLTZ7IyTtbiV4hIiAbvyvJmPAZXg&oe=69DC4CE0&_nc_sid=472314",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "x": 0.5487701442,
        "y": 0.9833191971
      },
      {
        "user": {
          "pk": "67153067400",
          "id": "67153067400",
          "username": "_mahi_explorer",
          "full_name": "Irai_Sirappugal",
          "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/661255438_17931942633235401_6260976575726210289_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2gFnnpySmXw1k1aK86pbe4MoxlhmxXM1Os4rwQBDOhZPEEVBlRdgot8qTkMlWJ_OIG4&_nc_ohc=AsfMY4jylpYQ7kNvwETiCn2&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GA71aSfJY8m_AbU-APHMMwcGdeNWbmNDAQAB1501500j-ccb7-5&oh=00_Af3YuFmg3NXiV-X5vjvp8GkbIC8FJuxg-aY-xRPR4oG4Hg&oe=69DC3885&_nc_sid=472314",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "x": 0.2994062765,
        "y": 0.9833191971
      }
    ],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          47347,
          94694
        ],
        "height": 1080,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/669431258_17864434017613956_8282760181895932089_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc2NDYwOTA0MTQ4ODYyNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=ntVDJ-oP18cQ7kNvwEojqWR&_nc_oc=AdoQGPIS0p6KcCeI-Lv4iv47NlIFc4la9F1j_4O3R1dndBosFu6k85We0OJQRCzzgJM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af3JVhb8nx-LYDIWywfQ8gJ-QptB_Ta5k-jK6ZgJpsSH1g&oe=69DC4A1D",
        "width": 1440,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          23321,
          46642
        ],
        "height": 563,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/669431258_17864434017613956_8282760181895932089_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc2NDYwOTA0MTQ4ODYyNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=ntVDJ-oP18cQ7kNvwEojqWR&_nc_oc=AdoQGPIS0p6KcCeI-Lv4iv47NlIFc4la9F1j_4O3R1dndBosFu6k85We0OJQRCzzgJM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&_nc_ss=7a3ba&oh=00_Af3wGY33gxPnKmmlLD2fnFjNbVp24Sg0ZO91T3hxFYM03Q&oe=69DC4A1D",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "clips_metadata": {},
    "video_dash_manifest": "",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "67153067400",
        "pk": 67153067400,
        "pk_id": "67153067400",
        "id": "67153067400",
        "username": "_mahi_explorer",
        "full_name": "Irai_Sirappugal",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "3870790995549959703_67153067400",
        "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/661255438_17931942633235401_6260976575726210289_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2gFnnpySmXw1k1aK86pbe4MoxlhmxXM1Os4rwQBDOhZPEEVBlRdgot8qTkMlWJ_OIG4&_nc_ohc=AsfMY4jylpYQ7kNvwETiCn2&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GA71aSfJY8m_AbU-APHMMwcGdeNWbmNDAQAB1501500j-ccb7-5&oh=00_Af3YuFmg3NXiV-X5vjvp8GkbIC8FJuxg-aY-xRPR4oG4Hg&oe=69DC3885&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      },
      {
        "strong_id__": "34328168544",
        "pk": 34328168544,
        "pk_id": "34328168544",
        "id": "34328168544",
        "username": "palani94_official",
        "full_name": "𝐖𝐨𝐫𝐥𝐝 𝐨𝐟 𝐩𝐚𝐥𝐚𝐧𝐢..!❤️",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "3769545231781009117_34328168544",
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/582096616_18080552873144545_8148477502297939851_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gFnnpySmXw1k1aK86pbe4MoxlhmxXM1Os4rwQBDOhZPEEVBlRdgot8qTkMlWJ_OIG4&_nc_ohc=uCx56mgwTB0Q7kNvwHSANwo&_nc_gid=RSDFCkWycvLR0mNNFlKvTA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GOgWsiLhsFjDKjxAAIsfu6gdNRVxbmNDAQAB1501500j-ccb7-5&oh=00_Af2pwfJcm-AhM1GijOhLTZ7IyTtbiV4hIiAbvyvJmPAZXg&oe=69DC4CE0&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      }
    ],
    "is_paid_partnership": false
  }
]
```

</details>

---

### GET /v1/hashtag/medias/clips/chunk

Get hashtag chunk of clips (reels). Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_clips_chunk_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/clips/chunk?name=love",
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
      "pk": "3870711225189699935",
      "id": "3870711225189699935_501243330",
      "code": "DW3h1n1jJFf",
      "taken_at": "2026-04-08T10:40:30Z",
      "taken_at_ts": 1775644830,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af3aVaGPcPVah9SWtBfSPfZLCLptSUYpx_kJ-JMtIVapcA&oe=69DC2620",
      "location": {
        "pk": 1031791313,
        "name": "Davies Coaches LTD",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "The Old Colliery",
        "city": "",
        "zip": null,
        "lng": -4.0678841390208,
        "lat": 51.774418090574,
        "external_id": "272344219549251",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "501243330",
        "id": "501243330",
        "username": "gkfentonn",
        "full_name": "Georgina Fenton",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gEMZhIY_bp9WhwlOZusB2mSHSOTcr0ePVCgbsEI8n_UbAqkaLduP06FK89T4CQDQro&_nc_ohc=n-uwrwSVU3kQ7kNvwGSmQX6&_nc_gid=BYVilSGza8tgyflbIMxAYA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af3f9_gzF-lK61K5PGbqpmAHybX2UvB9_ClZRNUpeMvE1w&oe=69DC425F&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 279,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Summer Pending🕶️☀️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n#love\n#instagood\n#photooftheday\n#viral \n#beautiful",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            54433,
            108867
          ],
          "height": 1820,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af3aVaGPcPVah9SWtBfSPfZLCLptSUYpx_kJ-JMtIVapcA&oe=69DC2620",
          "width": 1365,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            28402,
            56804
          ],
          "height": 1000,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEUCVOb&_nc_oc=AdreA6ghzm9UGebxVkIdqlII12ukmQSFPwfz6ETxj5tmZbXtY_9h7eUrQ-Jyw_3aPgs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af0fDaOpl852zkqCXzllFCbnD_hWzPKTchhbfdnaEIZJsA&oe=69DC2620",
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
      "pk": "3870771007451871805",
      "id": "3870771007451871805_375121505",
      "code": "DW3vbkaDLo9",
      "taken_at": "2026-04-08T12:38:17Z",
      "taken_at_ts": 1775651897,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af0xK2MGIqlTuWYFWsdQFXlVDsPH5gUKIk3L2c-R9x1JOg&oe=69DC1EC3",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEMZhIY_bp9WhwlOZusB2mSHSOTcr0ePVCgbsEI8n_UbAqkaLduP06FK89T4CQDQro&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=BYVilSGza8tgyflbIMxAYA&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af0c_2oOsZwL7Km1MoBOynR5GmiyP3yP0ioCxqSjq233Rg&oe=69DC3771&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 299,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Disney Princess irl",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            11766,
            23532
          ],
          "height": 1101,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af0xK2MGIqlTuWYFWsdQFXlVDsPH5gUKIk3L2c-R9x1JOg&oe=69DC1EC3",
          "width": 1079,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            7924,
            15848
          ],
          "height": 765,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=BYVilSGza8tgyflbIMxAYA&_nc_ss=7a3ba&oh=00_Af02iXQlnwFiHjsjTNtL1uWtsArKJE2kGE8SifY0c1UsAA&oe=69DC1EC3",
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
  "WyJiOGRkNzU3YjlkNmM0YWJmOGEzOThkMDFiZTA4MDkxMiIsW10sMV0="
]
```

</details>

---

### GET /v1/hashtag/medias/recent

Get hashtag medias top. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/recent?name=love"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/recent",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/recent?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[]
```

</details>

---

### GET /v1/hashtag/medias/recent/chunk

Get hashtag chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk?name=love"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/recent/chunk?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  [],
  ""
]
```

</details>

---

### GET /v1/hashtag/medias/top

Get hashtag medias top. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/top?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top?name=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870711225189699935",
    "id": "3870711225189699935_501243330",
    "code": "DW3h1n1jJFf",
    "taken_at": "2026-04-08T10:40:30Z",
    "taken_at_ts": 1775644830,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEtNuo_&_nc_oc=AdrpL-Xh5mGpeKy3MVPBJ3hfhQgWRjmRxy8pBoE2kIIOIL4ZgZgLNkGEMhBebi2wIRA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af2sVvc6mrsDuPW3PXQbNvyVTcjTytgOJ1WxIXq5MF1tzw&oe=69DC2620",
    "location": {
      "pk": 1031791313,
      "name": "Davies Coaches LTD",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "The Old Colliery",
      "city": "",
      "zip": null,
      "lng": -4.0678841390208,
      "lat": 51.774418090574,
      "external_id": "272344219549251",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "501243330",
      "id": "501243330",
      "username": "gkfentonn",
      "full_name": "Georgina Fenton",
      "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/651853253_18561129277059331_6539402620871739238_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDI0LmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFIqItSnC7PcCl-LBL7YA5WcVzuLyiEXGi1Hak8YXh66eiCRX3MjohNtBe9JDA0Huk&_nc_ohc=n-uwrwSVU3kQ7kNvwEvZN6g&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GMV92iYDcTCtP-FBAGaHUVQJoMBabmNDAQAB1501500j-ccb7-5&oh=00_Af1YIalcelNhhL2oUUl31uTPBBrdzT9hObuGwMAwZJ-aEg&oe=69DC425F&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 279,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Summer Pending🕶️☀️\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n\n#love\n#instagood\n#photooftheday\n#viral \n#beautiful",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          54433,
          108867
        ],
        "height": 1820,
        "scans_profile": "e35",
        "url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEtNuo_&_nc_oc=AdrpL-Xh5mGpeKy3MVPBJ3hfhQgWRjmRxy8pBoE2kIIOIL4ZgZgLNkGEMhBebi2wIRA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af2sVvc6mrsDuPW3PXQbNvyVTcjTytgOJ1WxIXq5MF1tzw&oe=69DC2620",
        "width": 1365,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          28402,
          56804
        ],
        "height": 1000,
        "scans_profile": "e35",
        "url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-15/661861874_18567855772059331_2211970304262378169_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDcxMTIyNTE4OTY5OTkzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEzNjV4MTgyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=JhzZqjodqOAQ7kNvwEtNuo_&_nc_oc=AdrpL-Xh5mGpeKy3MVPBJ3hfhQgWRjmRxy8pBoE2kIIOIL4ZgZgLNkGEMhBebi2wIRA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af3LQehtMF54SrEF7b1Db3BkUDzeYkep5pTgtbdeW8nRkQ&oe=69DC2620",
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
    "pk": "3870764609041488625",
    "id": "3870764609041488625_78271797955",
    "code": "DW3t-dbElrx",
    "taken_at": "2026-04-08T12:29:31Z",
    "taken_at_ts": 1775651371,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/669431258_17864434017613956_8282760181895932089_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc2NDYwOTA0MTQ4ODYyNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=ntVDJ-oP18cQ7kNvwFz4tm_&_nc_oc=AdorFwWPeMijk7K6c0quwI_85WPy_a3VJQdW01AA9sBcsvyuWFfgYMA9q__o7efAhbw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af2UGGvfQdBJ6XG-RQDk7yfgal8dgh_pT-ad6AqfhkIjog&oe=69DC4A1D",
    "location": {
      "pk": 1271876592870320,
      "name": "அருள்மிகு பழனி ஆண்டவர் திருக்கோயில் சன்னதி",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "",
      "city": "",
      "zip": null,
      "lng": 77.520518302917,
      "lat": 10.438720723335,
      "external_id": "1271876592870320",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "78271797955",
      "id": "78271797955",
      "username": "life_with_murugan_",
      "full_name": "life_with_murugan_",
      "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/657876395_17863436862613956_7878740436612381417_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFIqItSnC7PcCl-LBL7YA5WcVzuLyiEXGi1Hak8YXh66eiCRX3MjohNtBe9JDA0Huk&_nc_ohc=XM8-yGGbd7gQ7kNvwE0qJr_&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GKtlNifE6amAs3Y-AOl6yQmv6FZtbmNDAQAB1501500j-ccb7-5&oh=00_Af2nl5oDhv-O4pNkHKcqmQWh_Pqgadbj4gQT3dnbc3CnUg&oe=69DC392F&_nc_sid=472314",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 729,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "யாமிருக்க பயமேன்🦚🥹💯🛐\n.\n.\n#murugan #palani #lordmurugan #trending #love",
    "accessibility_caption": null,
    "usertags": [
      {
        "user": {
          "pk": "34328168544",
          "id": "34328168544",
          "username": "palani94_official",
          "full_name": "𝐖𝐨𝐫𝐥𝐝 𝐨𝐟 𝐩𝐚𝐥𝐚𝐧𝐢..!❤️",
          "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/582096616_18080552873144545_8148477502297939851_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gFIqItSnC7PcCl-LBL7YA5WcVzuLyiEXGi1Hak8YXh66eiCRX3MjohNtBe9JDA0Huk&_nc_ohc=uCx56mgwTB0Q7kNvwEdJqkG&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GOgWsiLhsFjDKjxAAIsfu6gdNRVxbmNDAQAB1501500j-ccb7-5&oh=00_Af0RYIGywWhQGnl7RNNHbytTH18T2cpxYQtVjW6I3nk8DQ&oe=69DC4CE0&_nc_sid=472314",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "x": 0.5487701442,
        "y": 0.9833191971
      },
      {
        "user": {
          "pk": "67153067400",
          "id": "67153067400",
          "username": "_mahi_explorer",
          "full_name": "Irai_Sirappugal",
          "profile_pic_url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-19/661255438_17931942633235401_6260976575726210289_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2gFIqItSnC7PcCl-LBL7YA5WcVzuLyiEXGi1Hak8YXh66eiCRX3MjohNtBe9JDA0Huk&_nc_ohc=AsfMY4jylpYQ7kNvwH-oW5K&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GA71aSfJY8m_AbU-APHMMwcGdeNWbmNDAQAB1501500j-ccb7-5&oh=00_Af22xu0IoUJYbwZ1noNYy-HcUagUPZz5RSeaVFseG3EIkA&oe=69DC3885&_nc_sid=472314",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "x": 0.2994062765,
        "y": 0.9833191971
      }
    ],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          47347,
          94694
        ],
        "height": 1080,
        "scans_profile": "e35",
        "url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/669431258_17864434017613956_8282760181895932089_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc2NDYwOTA0MTQ4ODYyNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=ntVDJ-oP18cQ7kNvwFz4tm_&_nc_oc=AdorFwWPeMijk7K6c0quwI_85WPy_a3VJQdW01AA9sBcsvyuWFfgYMA9q__o7efAhbw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af2UGGvfQdBJ6XG-RQDk7yfgal8dgh_pT-ad6AqfhkIjog&oe=69DC4A1D",
        "width": 1440,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          23321,
          46642
        ],
        "height": 563,
        "scans_profile": "e35",
        "url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/669431258_17864434017613956_8282760181895932089_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc2NDYwOTA0MTQ4ODYyNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=ntVDJ-oP18cQ7kNvwFz4tm_&_nc_oc=AdorFwWPeMijk7K6c0quwI_85WPy_a3VJQdW01AA9sBcsvyuWFfgYMA9q__o7efAhbw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&_nc_ss=7a3ba&oh=00_Af2lftLZwAU0NtqXK7OalydRnaKIwawddMGfG_LSmJnnlA&oe=69DC4A1D",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "clips_metadata": {},
    "video_dash_manifest": "",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "67153067400",
        "pk": 67153067400,
        "pk_id": "67153067400",
        "id": "67153067400",
        "username": "_mahi_explorer",
        "full_name": "Irai_Sirappugal",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "3870790995549959703_67153067400",
        "profile_pic_url": "https://scontent-waw2-1.cdninstagram.com/v/t51.82787-19/661255438_17931942633235401_6260976575726210289_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2gFIqItSnC7PcCl-LBL7YA5WcVzuLyiEXGi1Hak8YXh66eiCRX3MjohNtBe9JDA0Huk&_nc_ohc=AsfMY4jylpYQ7kNvwH-oW5K&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GA71aSfJY8m_AbU-APHMMwcGdeNWbmNDAQAB1501500j-ccb7-5&oh=00_Af22xu0IoUJYbwZ1noNYy-HcUagUPZz5RSeaVFseG3EIkA&oe=69DC3885&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      },
      {
        "strong_id__": "34328168544",
        "pk": 34328168544,
        "pk_id": "34328168544",
        "id": "34328168544",
        "username": "palani94_official",
        "full_name": "𝐖𝐨𝐫𝐥𝐝 𝐨𝐟 𝐩𝐚𝐥𝐚𝐧𝐢..!❤️",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "3769545231781009117_34328168544",
        "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/582096616_18080552873144545_8148477502297939851_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gFIqItSnC7PcCl-LBL7YA5WcVzuLyiEXGi1Hak8YXh66eiCRX3MjohNtBe9JDA0Huk&_nc_ohc=uCx56mgwTB0Q7kNvwEdJqkG&_nc_gid=3QqP0UO1JMXesBAUPxJ-1A&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GOgWsiLhsFjDKjxAAIsfu6gdNRVxbmNDAQAB1501500j-ccb7-5&oh=00_Af0RYIGywWhQGnl7RNNHbytTH18T2cpxYQtVjW6I3nk8DQ&oe=69DC4CE0&_nc_sid=472314",
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "incoming_request": false,
          "outgoing_request": false,
          "followed_by": false,
          "muting": false,
          "blocking": false,
          "is_eligible_to_subscribe": false,
          "subscribed": false
        }
      }
    ],
    "is_paid_partnership": false
  }
]
```

</details>

---

### GET /v1/hashtag/medias/top/chunk

Get hashtag chunk of top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/top/chunk?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_chunk_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top/chunk?name=love",
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
      "pk": "3870771007451871805",
      "id": "3870771007451871805_375121505",
      "code": "DW3vbkaDLo9",
      "taken_at": "2026-04-08T12:38:17Z",
      "taken_at_ts": 1775651897,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af2QoX-FDYeb18bZIu54qlCp5LtNWbYiKBuhA-OJX5uWTA&oe=69DC1EC3",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gG9tmIVEDWPJ7LLSy6oCQAIL59WpG29UKCAgojAuhRUXe0QH2WYMGE3cqmO3C5cuzE&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=sr9EZbdQVEkBThdVobfVVg&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af309ypqZRK3f4ZxjQ1eJWZP9glWdsu3ratLz2HSM8PRhQ&oe=69DC3771&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 299,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Disney Princess irl",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            11766,
            23532
          ],
          "height": 1101,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af2QoX-FDYeb18bZIu54qlCp5LtNWbYiKBuhA-OJX5uWTA&oe=69DC1EC3",
          "width": 1079,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            7924,
            15848
          ],
          "height": 765,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af1QxuQ1T63hLz4U5uPK9iU75PM-7G66P1fZFt0bQDW4iA&oe=69DC1EC3",
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
      "pk": "3870796662037942390",
      "id": "3870796662037942390_56596768220",
      "code": "DW31Q5GihB2",
      "taken_at": "2026-04-08T13:29:39Z",
      "taken_at_ts": 1775654979,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/658030355_18005902142880221_4311317524523702353_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc5NjY2MjAzNzk0MjM5MDE4MDA1OTAyMTM2ODgwMjIx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RvLG2O_PqqkQ7kNvwG08eE1&_nc_oc=AdqVAN9AhvNtkbC8yeO31-xt8MlR2IfggNdHNZElPa2BaPqC-ePUyBaixAAJiDGTSkc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af0otvPeaZYt2i_yzbTAwrmf5CUDzmgQHWWNzHfnhSnzGg&oe=69DC49F6",
      "location": null,
      "user": {
        "pk": "56596768220",
        "id": "56596768220",
        "username": "thihachhattisgarh",
        "full_name": "Thiha Chhattisgarh",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/412637139_895122222141985_849878795049946468_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG9tmIVEDWPJ7LLSy6oCQAIL59WpG29UKCAgojAuhRUXe0QH2WYMGE3cqmO3C5cuzE&_nc_ohc=C6rr3CVhV3cQ7kNvwHZ8L_x&_nc_gid=sr9EZbdQVEkBThdVobfVVg&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GNNXmBgh0hTiGy4DAGTNFuFCYMsLbkULAAAB1501500j-ccb7-5&oh=00_Af1QZ-qE3JmJR_Sqn2Tt9KWxc6W7SvGHcNPIvIs7g8ROMw&oe=69DC25FF&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 26,
      "comments_disabled": false,
      "like_count": 1433,
      "play_count": 34354,
      "has_liked": false,
      "caption_text": "रायपुर शहर के आरोपियों\n में है फुल Attitude ! \n#cg #cgreels #cgsongs #chhattisgarh #raipur #cgnews #shorts #cgshorts #ytshorts #cgvideo \n#cgvideo #cgfam #cgfamily #cgviral #instagram #bhilai #bilaspur #trending #love #cgcomedy #cgraipur #cglover #cgstatus #chhattisgarhi #instagood2",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNQNdrTDQbHiQn_j9xKNJ79AIC4p8HCrblcW8wDGYJuB9BzLSIRxG601BS72tQI3gUFuwQmWwct9xDmCDKLjrgA5j1V2go2TYPtb6o.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=Uj5M2jhbdNcQ7kNvwG2VCPj&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwMDU5MDIwMjg4ODAyMjEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5d33bb7f161d454c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9FRjRDRTlCRUI3ODcxNEFFNjEwMzhCOUU5NDJERjQ5RF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzY3NEFGQjBEQjdEMDdDMjdFQjYzODM4M0I5OUQyNTg4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACa65dWkuJH8PxUCKAJDMywXQFdzU_fO2RcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0eccaxqeZdd1OHuzadw16JOT8FgyvcSV-pxWKONQBvgg&oe=69D8493A",
      "view_count": 0,
      "video_duration": 93.802001953125,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            24697,
            49394
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/658030355_18005902142880221_4311317524523702353_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDc5NjY2MjAzNzk0MjM5MDE4MDA1OTAyMTM2ODgwMjIx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RvLG2O_PqqkQ7kNvwG08eE1&_nc_oc=AdqVAN9AhvNtkbC8yeO31-xt8MlR2IfggNdHNZElPa2BaPqC-ePUyBaixAAJiDGTSkc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&oh=00_Af0otvPeaZYt2i_yzbTAwrmf5CUDzmgQHWWNzHfnhSnzGg&oe=69DC49F6",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1096268,
          "height": 1280,
          "id": "1238367931442406v",
          "type": 101,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNQNdrTDQbHiQn_j9xKNJ79AIC4p8HCrblcW8wDGYJuB9BzLSIRxG601BS72tQI3gUFuwQmWwct9xDmCDKLjrgA5j1V2go2TYPtb6o.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=Uj5M2jhbdNcQ7kNvwG2VCPj&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwMDU5MDIwMjg4ODAyMjEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5d33bb7f161d454c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9FRjRDRTlCRUI3ODcxNEFFNjEwMzhCOUU5NDJERjQ5RF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzY3NEFGQjBEQjdEMDdDMjdFQjYzODM4M0I5OUQyNTg4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACa65dWkuJH8PxUCKAJDMywXQFdzU_fO2RcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0eccaxqeZdd1OHuzadw16JOT8FgyvcSV-pxWKONQBvgg&oe=69D8493A",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1096268,
          "height": 1280,
          "id": "1238367931442406v",
          "type": 102,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNQNdrTDQbHiQn_j9xKNJ79AIC4p8HCrblcW8wDGYJuB9BzLSIRxG601BS72tQI3gUFuwQmWwct9xDmCDKLjrgA5j1V2go2TYPtb6o.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=Uj5M2jhbdNcQ7kNvwG2VCPj&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgwMDU5MDIwMjg4ODAyMjEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5d33bb7f161d454c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9FRjRDRTlCRUI3ODcxNEFFNjEwMzhCOUU5NDJERjQ5RF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzY3NEFGQjBEQjdEMDdDMjdFQjYzODM4M0I5OUQyNTg4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACa65dWkuJH8PxUCKAJDMywXQFdzU_fO2RcYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0eccaxqeZdd1OHuzadw16JOT8FgyvcSV-pxWKONQBvgg&oe=69D8493A",
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
          "best_audio_cluster_id": "1288955113228865"
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
        "music_canonical_id": "18453827410128417",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26087244847644453,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": true,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT93.802666S\" FBManifestTimestamp=\"1775657895\" FBManifestIdentifier=\"Fs6Os50NKRaGntCWicW/AyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT93.802666S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"984150037890947a\" bandwidth=\"51719\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"51719\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m78/AQPX2D2K4hwcyNk8mIQC0aMUhF1RBjTDL-yGWKYQlheuGj5JUAFJCfQvgHIRHzGdRdTUmqxD5POqyj9fWoIEQxBGuZflxkZyM_SSnio.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=FbOBU_iObdcQ7kNvwGQerj2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE4MDA1OTAyMDI4ODgwMjIxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjkzLCJiaXRyYXRlIjo1MTgzOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0NKhfn_WPLLJrQnqKw3EqXnDTQh0_TtagB74aIyYQmZg&amp;oe=69D83E4D</BaseURL><SegmentBase indexRange=\"824-1419\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 93802,
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
          "original_media_id": 3870796662037942390,
          "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQMiZZ_50LHVO9vwOtRVSSqiTDMW0QBcd3UznZoKwpG512gKfL4g-haLIZ17EQ9Mv0Z9CgdTE-vpkkmh00Vzj_ac.mp4?strext=1&_nc_cat=100&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=jrfLUJlfvJUQ7kNvwGuwmVR&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTgwMDU5MDIwMjg4ODAyMjEsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6OTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=sr9EZbdQVEkBThdVobfVVg&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0N-0YO6crZW6WlyKGru3fjYljAf9Zz6vCghPQpNXEksg&oe=69DC2FE2",
          "should_mute_audio": false,
          "time_created": 1775654987,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "56596768220",
            "pk": 56596768220,
            "pk_id": "56596768220",
            "id": "56596768220",
            "username": "thihachhattisgarh",
            "full_name": "Thiha Chhattisgarh",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3265425626597034291_56596768220",
            "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/412637139_895122222141985_849878795049946468_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG9tmIVEDWPJ7LLSy6oCQAIL59WpG29UKCAgojAuhRUXe0QH2WYMGE3cqmO3C5cuzE&_nc_ohc=C6rr3CVhV3cQ7kNvwHZ8L_x&_nc_gid=sr9EZbdQVEkBThdVobfVVg&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GNNXmBgh0hTiGy4DAGTNFuFCYMsLbkULAAAB1501500j-ccb7-5&oh=00_Af1QZ-qE3JmJR_Sqn2Tt9KWxc6W7SvGHcNPIvIs7g8ROMw&oe=69DC25FF&_nc_sid=472314"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT93.802666S\" FBManifestTimestamp=\"1775657895\" FBManifestIdentifier=\"Fs6Os50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxsaOnvWj1I8D/rTYkIuJkQO61auk36ykA5LniYbe1JwElpHC5fvPngTa8I/F+YCfBf670JGDpvoFsPCopP7o1QasidzY7PyfB86rx/u9zdAKxJzZl8fwvQygqtiVtJfwYSIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT93.802666S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.1\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"2992002794318567v\" bandwidth=\"154339\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1809670\" FBPlaybackResolutionMos=\"0:100,360:74.7,480:70,720:57.3,1080:46.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.8,480:96.6,720:92.9,1080:85.6\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPDIg0nCFUxsk_pXjQp2fnpdQo5cQXH202MBPvIPh6es_3timEO-ooeSEx-ob--XuxHuGksB0dVHJ8QzQqwSKn8-CX4g7T6AfX2aOw.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=CE2LAbOsFrQQ7kNvwFgzr5a&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6MTU0MzM5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0gdNctEO-6fvEQdgBV6iI8kiWtixK9gvj3xcyLCivAMg&amp;oe=69DC3355</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-31252\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-37303\" FBFirstSegmentRange=\"1086-75702\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"75703-168535\" FBPrefetchSegmentRange=\"1086-75702\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"3513773838772002v\" bandwidth=\"220071\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2580397\" FBPlaybackResolutionMos=\"0:100,360:78.5,480:74.4,720:68.1,1080:55.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.74,480:98.34,720:97.7,1080:92.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOs2otYQ6Iyvczz7XAmT3O1WYAlgEIcGDGbRQE5c4EVRsQUGvYoS1iOXC0mhaQDTdCs_UjjJVJMQFk1UG9Zx0Doup4vs3voK41C4k4.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=N3K-gKzacekQ7kNvwHx993E&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6MjIwMDcxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0z-WiJbMbe3Sfb7KHAFOVJv4kK37lf8QPyVOl4sIl-YQ&amp;oe=69DC2298</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-41441\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-49195\" FBFirstSegmentRange=\"1086-103500\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"103501-231980\" FBPrefetchSegmentRange=\"1086-103500\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1188928289847753v\" bandwidth=\"309345\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3627155\" FBPlaybackResolutionMos=\"0:100,360:83.2,480:78.2,720:72,1080:58.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.386,480:99.377,720:99.382,1080:95.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMiTnMgS4iObATUN_PIPP-_uYG74qYmjN-IJJiKjTC6gpymmRD9mL2MTM5O-1uIqf7ZAXxNGRhH8m7L3TQTIn3BKty8e3txbpP3la4.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=dszGBxEj_XwQ7kNvwFzJPPu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6MzA5MzQ1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0JBgfkuFgWoxVOFxKewVD0rJ9I-k7CUiEUtogDaRnG3w&amp;oe=69DC4D96</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-54102\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-64093\" FBFirstSegmentRange=\"1086-139679\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"139680-315949\" FBPrefetchSegmentRange=\"1086-139679\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1475560917302317v\" bandwidth=\"419196\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"4915185\" FBPlaybackResolutionMos=\"0:100,360:86.5,480:82.1,720:75,1080:60.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.653,480:99.753,720:99.875,1080:97\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxWKYx2WSkP75h3r9HI2fdBLQXIR_vkvnZ_jXA-bABXoDwIUO20PFc4mvFaxHTQsw_NWARGHDXe9PBnc3apwYHhL4tt9r_bbrIyd8.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=06EOzzkkmDEQ7kNvwG9SnGM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6NDE5MTk2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2sJpKtqP8bNSjhLV6FtbB9ZTCSFHDMORIQNZ_-33so9g&amp;oe=69DC3F94</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-67492\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-80864\" FBFirstSegmentRange=\"1086-183636\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"183637-419824\" FBPrefetchSegmentRange=\"1086-183636\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1676308976897791v\" bandwidth=\"602754\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"7067463\" FBPlaybackResolutionMos=\"0:100,360:89.3,480:85.3,720:77.5,1080:62.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.812,480:99.887,720:99.997,1080:98.52\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNCTnYiiG0gu7DnvLd9YWrPWG4gpL9UYt35wQ84xiqQ7IpBQ4eOJj9PMhWgXlVi8HsfqHbUI5O0IdtEGmQK8SiFFjOWOTmwuKRuLS8.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=b9O6inHEYFMQ7kNvwFJJcaU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6NjAyNzU0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3NDrcU_jy1hKUFSDe-EBEWuSfUUABEjZh5YeyzB5mt4g&amp;oe=69DC44B6</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-86347\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-105820\" FBFirstSegmentRange=\"1086-255795\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"255796-588188\" FBPrefetchSegmentRange=\"1086-255795\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"878858208527267v\" bandwidth=\"836154\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"9804137\" FBPlaybackResolutionMos=\"0:100,360:91,480:87.3,720:79.9,1080:64\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.864,480:99.928,720:100,1080:99.155\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNyUI_R_Nttcwxz2uiotSPYwnnouGiCJvoGO3IDqnxslcCbXuxsbmbzykLpgM8jCzH_WAXZVijmdZG5noIhlzNZZFfdQYpBBZFkfpE.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=w1IXXc7GQUMQ7kNvwHK3TtZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6ODM2MTU0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0fDD3PsEMWEGOJsitbPUbEjf19d7pQC95gJgaB-9GdDg&amp;oe=69DC45CD</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-102628\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-128896\" FBFirstSegmentRange=\"1086-335084\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"335085-780114\" FBPrefetchSegmentRange=\"1086-335084\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"881964438195519v\" bandwidth=\"1222431\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"14333340\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:89.1,720:82.1,1080:65.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.904,480:99.959,720:100,1080:99.583\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMNNTnrnF643SnEzVIA7ag27OoNZJBiAVRmO4bR7X8rVH3ux0E3Q6AR-eKhOF5nE1AXSKwDItuSvpb0j1BnfTTxV2ChZy9UI7s5Qgk.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=pevyxTu31mUQ7kNvwE-UCy4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6MTIyMjQzMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3btdqSAaq2UkM9Vhe79GTLbmTs7fGTMYnRBconUf6HFg&amp;oe=69DC3E22</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-122169\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-165381\" FBFirstSegmentRange=\"1086-463673\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"463674-1080330\" FBPrefetchSegmentRange=\"1086-463673\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1193244429403211v\" bandwidth=\"1955883\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"22933260\" FBPlaybackResolutionMos=\"0:100,360:94.5,480:91.9,720:85.7,1080:78.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.921,480:99.973,720:100,1080:100\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPmeVuyXAP1NpQKgla46TvMQJ0yF3OBXSxypmaxskf1lVjYN07DKeWlUYxtE55XptKk65Gs7MVfKig7miNF5zgI6ExH2a8Q1dVLmVE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=aOtUdhoSytQQ7kNvwEQzI0O&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxODAwNTkwMjAyODg4MDIyMSwiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo5MywiYml0cmF0ZSI6MTk1NTg4MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0sirQFtFsAeF5H1aLQqVk9jN9jgr0V-7fEWPhtum7Flw&amp;oe=69DC2F66</BaseURL><SegmentBase indexRange=\"826-1085\" timescale=\"11988\" FBMinimumPrefetchRange=\"1086-178603\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1086-291646\" FBFirstSegmentRange=\"1086-776604\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"776605-1729557\" FBPrefetchSegmentRange=\"1086-776604\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"924358470366557a\" bandwidth=\"40767\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40767\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"479099\" FBPaqMos=\"91.96\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMh4MMfWA598hid0mlahLVR84yokg5LWeu6g2XoWwotAIZxW1Rsj93tUi5Qo_rZrXnwkAjRFQKzK6MO5yVJk5C9P6ce4ogUJgrhN9w.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=uF7XClqS2mwQ7kNvwEXDNRU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDA1OTAyMDI4ODgwMjIxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjkzLCJiaXRyYXRlIjo0MDg2MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1TjJ8Tlh381fo8FTdGWmeYxNrAhPcY6FgcT-F7NjqjQA&amp;oe=69DC2A3F</BaseURL><SegmentBase indexRange=\"837-1096\" timescale=\"48000\" FBMinimumPrefetchRange=\"1097-2207\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1097-15268\" FBFirstSegmentRange=\"1097-27235\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27236-53023\" FBPrefetchSegmentRange=\"1097-27235\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2040639450219094a\" bandwidth=\"60906\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"60906\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"715238\" FBPaqMos=\"91.88\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPG9WiCeiHJUf-v75UP30xFfBA2-TnlnLYL74K4dyu8JCYCeKITVVcZOpAfJu-EByVOM4Kk3r7Og-cPqoaOBU67EXpv2jyTMvxCQ0M.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=IU4PEZ6Pr90Q7kNvwGplrpS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDA1OTAyMDI4ODgwMjIxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjkzLCJiaXRyYXRlIjo2MDk5OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Mk-Zjqz4zwE64WOElV6LCqFP-V-vmD_5f-QRugcqJWw&amp;oe=69DC2703</BaseURL><SegmentBase indexRange=\"838-1097\" timescale=\"48000\" FBMinimumPrefetchRange=\"1098-2645\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1098-21006\" FBFirstSegmentRange=\"1098-38922\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"38923-76848\" FBPrefetchSegmentRange=\"1098-38922\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1877570492898328a\" bandwidth=\"86696\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"86696\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"1017631\" FBPaqMos=\"93.51\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrf-DYcveTe5eaSvAwvw2Glb-X3ohatz7QOzPouTiIgxhS4VuGl3EdQtFs_1Y5KjX1TeG3IbWYH7LwQnA4dqLSlwlQ_fogrEk9oM4.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=f8SzgLITKJMQ7kNvwHQ4xBH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDA1OTAyMDI4ODgwMjIxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjkzLCJiaXRyYXRlIjo4Njc4OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2T_I3PtODrnMIaFrXi58Kl2lw0lAf5FPDB7-FkBySYbQ&amp;oe=69DC2560</BaseURL><SegmentBase indexRange=\"833-1092\" timescale=\"48000\" FBMinimumPrefetchRange=\"1093-2443\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1093-29322\" FBFirstSegmentRange=\"1093-55274\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"55275-109484\" FBPrefetchSegmentRange=\"1093-55274\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"27549765484612240a\" bandwidth=\"102014\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"102014\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1197238\" FBPaqMos=\"93.79\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPIrdfp0a0zm9lTADsdHOYSNRiBn1mzgTNflQCvvrqW1D8PXQD9vXWHaNCJP6h1BscorejDEpEte8hQylEy1URhnrcc4ZjFpZK5COk.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=A-i9np-Ggv4Q7kNvwFXb1He&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE4MDA1OTAyMDI4ODgwMjIxLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjkzLCJiaXRyYXRlIjoxMDIxMDYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=sr9EZbdQVEkBThdVobfVVg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3W6y8lyjZVXxFO6n0cog0z55tqeacV7xvMSYJcJOPEAA&amp;oe=69DC215F</BaseURL><SegmentBase indexRange=\"833-1092\" timescale=\"48000\" FBMinimumPrefetchRange=\"1093-2491\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1093-34717\" FBFirstSegmentRange=\"1093-65172\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"65173-128781\" FBPrefetchSegmentRange=\"1093-65172\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WyIxYmRmMmQyOTI1ZTY0NTU2YWEzZWRmYjM5YjVlNzBjNSIsW10sMV0="
]
```

</details>

---

### GET /v1/hashtag/medias/top/recent/chunk

Get hashtag chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes | Please make sure to use a clean hashtag without any special symbols. **Good one**: love, sea, dog, 공구 **Bad one**: #dog, sea_., tanjung.., #공구. |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk?name=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.hashtag_medias_top_recent_chunk_v1(name="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk",
        headers=headers,
        params={"name": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/hashtag/medias/top/recent/chunk?name=love",
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
      "pk": "3870797517055833010",
      "id": "3870797517055833010_47906970587",
      "code": "DW31dVZk7Oy",
      "taken_at": "2026-04-08T13:30:43Z",
      "taken_at_ts": 1775655043,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": null,
      "user": {
        "pk": "47906970587",
        "id": "47906970587",
        "username": "nani_kranthi_07",
        "full_name": "𝐍𝐚𝐧𝐢_𝐊𝐫𝐚𝐧𝐭𝐡𝐢💗",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/633049469_18079785680594588_8147815449926346534_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFsnXq-IF3enaJnlXzEWVetMlpXOxRTwSNe4AciIv9wutVSg1WOub7voOEQ3o8QmZ8&_nc_ohc=B4ltc3Tug3cQ7kNvwGju5lg&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GH2RuyWcZhsjeDtAACanTJT72hJxbmNDAQAB1501500j-ccb7-5&oh=00_Af2lYfwX93SFcV1vOxiJRgqQDmSGT3iyfsXwtjZxRDdKXQ&oe=69DC1E90&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 30,
      "comments_disabled": false,
      "like_count": 3,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "✨🖤\n\n#new #post #love #fyp #viral",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870797366237059175",
          "id": "3870797366237059175_47906970587",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af0e23xooBLwuubg8YD-fA-MlwVvdB-sOW0Fev0zdAou6A&oe=69DC2D35",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                21233,
                42467
              ],
              "height": 1440,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af0e23xooBLwuubg8YD-fA-MlwVvdB-sOW0Fev0zdAou6A&oe=69DC2D35",
              "width": 1080,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                14288,
                28577
              ],
              "height": 1000,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af1IrtHkxIZTIyp04_2oFx4HUZ_T6Bm_S-YKVwS6_1p7_A&oe=69DC2D35",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870797517055833010_47906970587",
          "commerciality_status": "not_commercial",
          "taken_at": 1775655042
        },
        {
          "pk": "3870797366941648411",
          "id": "3870797366941648411_47906970587",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661703299_18086365946594588_7065368417728275359_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc5NzM2Njk0MTY0ODQxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=h-RHe-FqlLgQ7kNvwGSpwwJ&_nc_oc=AdqtYRv8Ed4SzzP26mvWZ7PZVYr7smotU5lv35xgzOi44A14305RedWT5RvulcF8Anw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af2cy3Si90Pdau17LUOF82-RT6glfTYn8R_gWJSx4WAhaw&oe=69DC3BF1",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                18011,
                36023
              ],
              "height": 1440,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661703299_18086365946594588_7065368417728275359_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc5NzM2Njk0MTY0ODQxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=h-RHe-FqlLgQ7kNvwGSpwwJ&_nc_oc=AdqtYRv8Ed4SzzP26mvWZ7PZVYr7smotU5lv35xgzOi44A14305RedWT5RvulcF8Anw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af2cy3Si90Pdau17LUOF82-RT6glfTYn8R_gWJSx4WAhaw&oe=69DC3BF1",
              "width": 1080,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                12120,
                24241
              ],
              "height": 1000,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661703299_18086365946594588_7065368417728275359_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg3MDc5NzM2Njk0MTY0ODQxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=h-RHe-FqlLgQ7kNvwGSpwwJ&_nc_oc=AdqtYRv8Ed4SzzP26mvWZ7PZVYr7smotU5lv35xgzOi44A14305RedWT5RvulcF8Anw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af3vrmcHMPPoakRXUFFmwDtUDKl6mRsXybxy_TjrOnk2oQ&oe=69DC3BF1",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870797517055833010_47906970587",
          "commerciality_status": "not_commercial",
          "taken_at": 1775655042
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            21233,
            42467
          ],
          "height": 1440,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af0e23xooBLwuubg8YD-fA-MlwVvdB-sOW0Fev0zdAou6A&oe=69DC2D35",
          "width": 1080,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            14288,
            28577
          ],
          "height": 1000,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/660829455_18086365937594588_5698550194396681998_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg3MDc5NzM2NjIzNzA1OTE3NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTQ0MC5zZHIuQzMifQ%3D%3D&_nc_ohc=HStzzUiVaPAQ7kNvwEq5oS1&_nc_oc=AdrrlVssjzdV2jUzK3U3MIgQvfQiuiSV9k6fwQYkMbcS-gcqAr0xbfrUFKUc-S1-lO4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af1IrtHkxIZTIyp04_2oFx4HUZ_T6Bm_S-YKVwS6_1p7_A&oe=69DC2D35",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "clips_metadata": {},
      "video_dash_manifest": "",
      "like_and_view_counts_disabled": true,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870771007451871805",
      "id": "3870771007451871805_375121505",
      "code": "DW3vbkaDLo9",
      "taken_at": "2026-04-08T12:38:17Z",
      "taken_at_ts": 1775651897,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af0w6HAHqJdTPtTzXe3_KfH-Zl1StFT8SmaQE2T5icZelw&oe=69DC1EC3",
      "location": null,
      "user": {
        "pk": "375121505",
        "id": "375121505",
        "username": "fallinginsociety",
        "full_name": "FallingInSociety",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/56832669_365153704120407_6044589393019142144_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzguYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFsnXq-IF3enaJnlXzEWVetMlpXOxRTwSNe4AciIv9wutVSg1WOub7voOEQ3o8QmZ8&_nc_ohc=8UGwMTx74pgQ7kNvwGL3yv9&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&edm=AMKDjl4BAAAA&ccb=7-5&ig_cache_key=GJ0yYwNXkNL4GkwBAAAAAAAHsuJTbkULAAAB1501500j-ccb7-5&oh=00_Af2ys2V6XLkwAIk5n_P_Jf166myUzOdSh5NtGIPf4-lS2w&oe=69DC3771&_nc_sid=472314",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 5,
      "comments_disabled": false,
      "like_count": 299,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Disney Princess irl",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            11766,
            23532
          ],
          "height": 1101,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af0w6HAHqJdTPtTzXe3_KfH-Zl1StFT8SmaQE2T5icZelw&oe=69DC1EC3",
          "width": 1079,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            7924,
            15848
          ],
          "height": 765,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/658862388_18596029096017506_6327650136241708566_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=110&ig_cache_key=Mzg3MDc3MTAwNzQ1MTg3MTgwNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwNzl4MTEwMS5zZHIuQzMifQ%3D%3D&_nc_ohc=mSXsiryJndQQ7kNvwFRg-FS&_nc_oc=AdpSZmc9UFNfKHGwqaC3Fj_Uq5fRH2RIZ-pz0kC4WW0mc94JuD7Zp1O5ztRjnB--Jsw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=Lw4Qydw54_jEKg-GqddH_w&_nc_ss=7a3ba&oh=00_Af39EuBIP4rv9FPkhDkAwWy_6gSAfD3r6x5Cq_HaZC_J3w&oe=69DC1EC3",
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
  "WyJlNTVlMmMwNzhkMzg0MWEzYTQzZGI2NjZkYjBhNGI5MSIsW10sMV0="
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-hashtags){ target=_blank }
