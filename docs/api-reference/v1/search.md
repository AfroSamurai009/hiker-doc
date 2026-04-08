# Search Endpoints

Search users, hashtags, locations, and music.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/fbsearch/places`](#get-v1fbsearchplaces) | [`/v1/fbsearch/topsearch`](#get-v1fbsearchtopsearch) | [`/v1/fbsearch/topsearch/hashtags`](#get-v1fbsearchtopsearchhashtags) | [`/v1/search/hashtags`](#get-v1searchhashtags) | [`/v1/search/music`](#get-v1searchmusic) | [`/v1/search/users`](#get-v1searchusers) | [`/v1/share/by/code`](#get-v1sharebycode) | [`/v1/share/by/url`](#get-v1sharebyurl) | [`/v1/share/reel/by/url`](#get-v1sharereelbyurl)

---

### GET /v1/fbsearch/places

Search locations. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `lat` | number | No | Lat |
| `lng` | number | No | Lng |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/fbsearch/places?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_places_v1(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/fbsearch/places",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/fbsearch/places?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": 252923412072688,
    "name": "NatGeo Roof Deck",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "161 6th Ave",
    "city": "",
    "zip": null,
    "lng": -74.004295349121,
    "lat": 40.725898742676,
    "external_id": "252923412072688",
    "external_id_source": "facebook_places"
  },
  {
    "pk": 617882014,
    "name": "أسرار Nat Geo",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "625 Union St",
    "city": "",
    "zip": null,
    "lng": -73.98444,
    "lat": 40.67817,
    "external_id": "219266724863910",
    "external_id_source": "facebook_places"
  }
]
```

</details>

---

### GET /v1/fbsearch/topsearch

Topsearch. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/fbsearch/topsearch?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_topsearch_v1(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/fbsearch/topsearch",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/fbsearch/topsearch?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "position": 0,
    "user": {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "pk": 787132,
      "pk_id": "787132",
      "is_verified_search_boosted": false,
      "third_party_downloads_enabled": 2,
      "id": "787132",
      "full_name": "National Geographic",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGFCvghkBlbEyjrBDa933p3U8QYNIy_nJtFuFkOKxDfbRpe7JzIDQrNqYmb1VvPaDk&_nc_ohc=XbeNvhLXv28Q7kNvwGCsqVG&_nc_gid=5qaRx7jufY4ewdydDV7IZA&edm=AP9-OL4BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0bkdBqNVX8wil3OfL3y3oeSfusfU72yC9xPZuxNxIcLA&oe=69DC51E9&_nc_sid=a62bc8",
      "username": "natgeo",
      "account_badges": [],
      "friendship_status": {
        "following": false,
        "is_bestie": false,
        "is_feed_favorite": false,
        "is_private": false,
        "is_restricted": false,
        "incoming_request": false,
        "outgoing_request": false
      },
      "has_anonymous_profile_picture": false,
      "has_opt_eligible_shop": false,
      "is_ring_creator": false,
      "latest_reel_media": 1775583063,
      "should_show_category": true,
      "show_ig_app_switcher_badge": true,
      "show_ring_award": false,
      "show_text_post_app_badge": true,
      "unseen_count": 0,
      "social_context": "274M followers",
      "search_social_context": "274M followers",
      "search_social_context_snippet_type": "typeahead_follow_count"
    }
  },
  {
    "position": 1,
    "user": {
      "strong_id__": "23947096",
      "fbid_v2": 17841400332880374,
      "pk": 23947096,
      "pk_id": "23947096",
      "is_verified_search_boosted": false,
      "third_party_downloads_enabled": 2,
      "id": "23947096",
      "full_name": "National Geographic Travel",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865702501739707616_23947096",
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGFCvghkBlbEyjrBDa933p3U8QYNIy_nJtFuFkOKxDfbRpe7JzIDQrNqYmb1VvPaDk&_nc_ohc=t-DCVZxwtX4Q7kNvwG3Ttjp&_nc_gid=5qaRx7jufY4ewdydDV7IZA&edm=AP9-OL4BAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af1yCXSqRf3aD2pUft8eNUbwi6m0gYW-IjrFF98LbdYlgQ&oe=69DC2F06&_nc_sid=a62bc8",
      "username": "natgeotravel",
      "account_badges": [],
      "friendship_status": {
        "following": false,
        "is_bestie": false,
        "is_feed_favorite": false,
        "is_private": false,
        "is_restricted": false,
        "incoming_request": false,
        "outgoing_request": false
      },
      "has_anonymous_profile_picture": false,
      "has_opt_eligible_shop": false,
      "is_ring_creator": false,
      "latest_reel_media": 1775582271,
      "should_show_category": true,
      "show_ring_award": false,
      "show_text_post_app_badge": false,
      "unseen_count": 0,
      "social_context": "45.5M followers",
      "search_social_context": "45.5M followers",
      "search_social_context_snippet_type": "typeahead_follow_count"
    }
  }
  // ... truncated
```

</details>

---

### GET /v1/fbsearch/topsearch/hashtags

Search hashtags via topsearch. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/fbsearch/topsearch/hashtags?query=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_topsearch_hashtags_v1(query="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/fbsearch/topsearch/hashtags",
        headers=headers,
        params={"query": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/fbsearch/topsearch/hashtags?query=love",
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

### GET /v1/search/hashtags

Search hashtags. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/search/hashtags?query=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_hashtags_v1(query="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/search/hashtags",
        headers=headers,
        params={"query": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/search/hashtags?query=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "id": "17843826142012701",
    "name": "love",
    "media_count": 2147483647,
    "allow_following": false,
    "profile_pic_url": null
  },
  {
    "id": "17843851987047311",
    "name": "lovehim",
    "media_count": 41383430,
    "allow_following": false,
    "profile_pic_url": null
  }
]
```

</details>

---

### GET /v1/search/music

Search music. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/search/music?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_music_v1(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/search/music",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/search/music?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "id": "1283502475113803",
    "title": "National Geographic",
    "subtitle": "",
    "display_artist": "Winterlight",
    "audio_cluster_id": "2045685665695806",
    "artist_id": null,
    "cover_artwork_uri": "https://scontent-lga3-2.cdninstagram.com/v/t39.30808-6/426871115_1505357383342530_7331902838470414874_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=105&ccb=7-5&_nc_sid=2f2557&_nc_ohc=C2HtJGVAWqQQ7kNvwHn59EO&_nc_oc=AdqwXp6CtRyzeDZCCALNyQ9sMjnSS77p6tXqQ1VZZSryUda_iEBKV7zhplS3vmH3wYU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=ADjEw42Q9CuxcTnN6FkcAQ&_nc_ss=7a39b&oh=00_Af0KWhznSbKqd3-poiwy4c4pclIpF1mJTug9X4_M_lWfYA&oe=69DC3177",
    "cover_artwork_thumbnail_uri": "https://scontent-lga3-2.cdninstagram.com/v/t39.30808-6/426871115_1505357383342530_7331902838470414874_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=105&ccb=7-5&_nc_sid=2f2557&_nc_ohc=C2HtJGVAWqQQ7kNvwHn59EO&_nc_oc=AdqwXp6CtRyzeDZCCALNyQ9sMjnSS77p6tXqQ1VZZSryUda_iEBKV7zhplS3vmH3wYU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=ADjEw42Q9CuxcTnN6FkcAQ&_nc_ss=7a39b&oh=00_Af2rdTqIUyjnk0rS8SI8ChoIWdK_tqldFv5_Xonr-K04hg&oe=69DC3177",
    "progressive_download_url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=sY5HPWJPCK8Q7kNvwEy8wmG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=1f315079ae391eba&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR1RlV1NEc1V6bGNrWUFDQUVtNnVEcXNyRDB3Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtInB8srQvQMVAigCQzMsF0B1mPXCj1wpGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af1lkb0EOQPuF8JNPsHSeDyU32-soD20xvwNL7wKMvziZw&oe=69DC5229",
    "fast_start_progressive_download_url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=sY5HPWJPCK8Q7kNvwEy8wmG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=1f315079ae391eba&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR1RlV1NEc1V6bGNrWUFDQUVtNnVEcXNyRDB3Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtInB8srQvQMVAigCQzMsF0B1mPXCj1wpGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af1lkb0EOQPuF8JNPsHSeDyU32-soD20xvwNL7wKMvziZw&oe=69DC5229",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      113000,
      128500
    ],
    "is_explicit": false,
    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT345.559998S\"><Period id=\"0\" duration=\"PT345.559998S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1938077947044382a\" bandwidth=\"62920\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"62920\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&amp;_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=sY5HPWJPCK8Q7kNvwEy8wmG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJiaXRyYXRlIjo2Mjk4NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3tCk0M9gutrmEpzEJZuzDMYOTPar7_r78hvFz1ifHsYA&amp;oe=69DC5229</BaseURL><SegmentBase indexRange=\"824-2931\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "has_lyrics": false,
    "audio_asset_id": "1283502475113803",
    "duration_in_ms": 345560,
    "dark_message": null,
    "allows_saving": false,
    "territory_validity_periods": null
  },
  {
    "id": "3071277199804105",
    "title": "Until I Found You",
    "subtitle": "",
    "display_artist": "Stephen Sanchez, Em Beihold",
    "audio_cluster_id": "354492766725899",
    "artist_id": null,
    "cover_artwork_uri": "https://scontent-lga3-2.cdninstagram.com/v/t39.30808-6/426406817_917490163390033_8060542730959388333_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=ADJkpyWW1xEQ7kNvwF9CmMt&_nc_oc=AdqKT-P7Z0vyefIJ5NW7ccRie65JGnK8tlzk6jy_Z6kmDkJClQjplI0M8Sta90_GhVA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=ADjEw42Q9CuxcTnN6FkcAQ&_nc_ss=7a39b&oh=00_Af1-XWn81tj6AzRv_v05l0yRyhNkS0ejG5POiuI8vjewxw&oe=69DC2937",
    "cover_artwork_thumbnail_uri": "https://scontent-lga3-2.cdninstagram.com/v/t39.30808-6/426406817_917490163390033_8060542730959388333_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=ADJkpyWW1xEQ7kNvwF9CmMt&_nc_oc=AdqKT-P7Z0vyefIJ5NW7ccRie65JGnK8tlzk6jy_Z6kmDkJClQjplI0M8Sta90_GhVA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=ADjEw42Q9CuxcTnN6FkcAQ&_nc_ss=7a39b&oh=00_Af03W9-NtED44uwrCorWAHru3suiJlpEDdxpx7phknVzeg&oe=69DC2937",
    "progressive_download_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=1u3JU8oeORIQ7kNvwG878EO&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=78f9e84ff2874f58&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT0xLSlNDOXVyMlRva0VDQU9pdFA2cTJUZVpGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm1KLwyMT5qwMVAigCQzMsF0BmDhR64UeuGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af1LS80zDOIFWVzBDnNhqWW4qnMM0_lrSRQ80Y7LeNT2oQ&oe=69DC3FFC",
    "fast_start_progressive_download_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=1u3JU8oeORIQ7kNvwG878EO&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=78f9e84ff2874f58&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT0xLSlNDOXVyMlRva0VDQU9pdFA2cTJUZVpGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm1KLwyMT5qwMVAigCQzMsF0BmDhR64UeuGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af1LS80zDOIFWVzBDnNhqWW4qnMM0_lrSRQ80Y7LeNT2oQ&oe=69DC3FFC",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      27000,
      93000
    ],
    "is_explicit": false,
    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT176.440002S\"><Period id=\"0\" duration=\"PT176.440002S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1448351333045592a\" bandwidth=\"56442\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"56442\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=1u3JU8oeORIQ7kNvwG878EO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJiaXRyYXRlIjo1NjUyOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2QRB4JaLLQfYKmQkGxs9ZOBnWF5eBHlOBenue2s-Qqmw&amp;oe=69DC3FFC</BaseURL><SegmentBase indexRange=\"824-1923\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "has_lyrics": false,
    "audio_asset_id": "3071277199804105",
    "duration_in_ms": 176440,
    "dark_message": null,
    "allows_saving": false,
    "territory_validity_periods": null
  }
]
```

</details>

---

### GET /v1/search/users

Search users. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/search/users?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_users_v1(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/search/users",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/search/users?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": 787132,
    "id": "787132",
    "username": "natgeo",
    "full_name": "National Geographic",
    "profile_pic_url": "https://scontent-ord5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&cb=8438d1d6-eb76aa66&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE3f4Fe1xVmmSkNJr79tKjfnA9HB8PLql0ZhjvK0FBaCWAWNd5qFX9I6zpoXiyEwFk&_nc_ohc=XbeNvhLXv28Q7kNvwEVwZRJ&_nc_gid=PJ3PdHOFDODL9Vk_ZrK5yA&edm=ANei9xoBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5-cb8438d1d6-eb76aa66&oh=00_Af0MhrfACXMdtBcPlp1xRH0BUCM-ZU7Q2foaTdcCSTgRRQ&oe=69DC51E9&_nc_sid=3b96ff",
    "profile_pic_url_hd": null,
    "is_private": null,
    "is_verified": null
  },
  {
    "pk": 23947096,
    "id": "23947096",
    "username": "natgeotravel",
    "full_name": "National Geographic Travel",
    "profile_pic_url": "https://scontent-ord5-1.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&cb=8438d1d6-eb76aa66&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE3f4Fe1xVmmSkNJr79tKjfnA9HB8PLql0ZhjvK0FBaCWAWNd5qFX9I6zpoXiyEwFk&_nc_ohc=t-DCVZxwtX4Q7kNvwFV5Rgf&_nc_gid=PJ3PdHOFDODL9Vk_ZrK5yA&edm=ANei9xoBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5-cb8438d1d6-eb76aa66&oh=00_Af2AgRBrKY1xBjlmYS55FXWflVW5NiOdQb_oQWPlYAzzPg&oe=69DC2F06&_nc_sid=3b96ff",
    "profile_pic_url_hd": null,
    "is_private": null,
    "is_verified": null
  }
]
```

</details>

---

### GET /v1/share/by/code

Get share object by code (aGlnaGxpZ2h0OjE4MTQ2MjE2Njk4MDIyMTc0 ->
{"pk": 18146216698022176, "type": "highlight"}). Returns shared content data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | Code |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/share/by/code?code=aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.share_by_code_v1(code="aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/share/by/code",
        headers=headers,
        params={"code": "aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/share/by/code?code=aGlnaGxpZ2h0OjE3ODkzMjA5ODI1MjgxMjIx",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": "17893209825281221",
  "type": "highlight"
}
```

</details>

---

### GET /v1/share/by/url

Get share object by url (
https://www.ins...ram.com/s/aGlnaGxpZ2h0OjE4MTQ2MjE2Njk4MDIyMTc0 ->
{"pk": 18146216698022176, "type": "highlight"}). Returns shared content data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/share/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.share_by_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/share/by/url",
        headers=headers,
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/share/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/share/reel/by/url

Returns shared content data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/share/reel/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.share_reel_by_url_v1(url="https://www.instagram.com/p/DRqAYKuAIUx/")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/share/reel/by/url",
        headers=headers,
        params={"url": "https://www.instagram.com/p/DRqAYKuAIUx/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/share/reel/by/url?url=https://www.instagram.com/p/DRqAYKuAIUx/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-search){ target=_blank }
