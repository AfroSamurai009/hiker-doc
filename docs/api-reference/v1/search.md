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
    "pk": 191282531790847,
    "name": "Natgeo",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "",
    "city": "",
    "zip": null,
    "lng": -34.90634,
    "lat": -8.113927,
    "external_id": "191282531790847",
    "external_id_source": "facebook_places"
  },
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
    "pk": 502960502,
    "name": "\"NatGeo WILD\"",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "",
    "city": "",
    "zip": null,
    "lng": 106.59584,
    "lat": -6.21039,
    "external_id": "562692613755935",
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
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHrUPKPe3BK7s7L8mPsB-RGzjjveH_wzTGGOOHaF8VeHCsITL7932YJaiwlqYSl4mE&_nc_ohc=XbeNvhLXv28Q7kNvwGaUhgD&_nc_gid=xlMwQ3EaPCHRN-jkAzu6ag&edm=AP9-OL4BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3muXuXwi-kFfrSQ5HEZ7VHKyUnp9BL6m3vWO1j65z6Eg&oe=69DC51E9&_nc_sid=a62bc8",
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
      "latest_reel_media": 1775659002,
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
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHrUPKPe3BK7s7L8mPsB-RGzjjveH_wzTGGOOHaF8VeHCsITL7932YJaiwlqYSl4mE&_nc_ohc=t-DCVZxwtX4Q7kNvwF8ANLe&_nc_gid=xlMwQ3EaPCHRN-jkAzu6ag&edm=AP9-OL4BAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af28hAyLsTHhyQXAAIfs0ood_Qpytu93Mjb-WUPnFis8lw&oe=69DC6746&_nc_sid=a62bc8",
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
  },
  {
    "position": 2,
    "user": {
      "strong_id__": "414805671",
      "fbid_v2": 17841400650136481,
      "pk": 414805671,
      "pk_id": "414805671",
      "is_verified_search_boosted": false,
      "third_party_downloads_enabled": 2,
      "id": "414805671",
      "full_name": "National Geographic Science",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865701954660099001_414805671",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658043965_18575534785021672_4145157128631909093_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHrUPKPe3BK7s7L8mPsB-RGzjjveH_wzTGGOOHaF8VeHCsITL7932YJaiwlqYSl4mE&_nc_ohc=ocufCJtUTR4Q7kNvwFE2Ckn&_nc_gid=xlMwQ3EaPCHRN-jkAzu6ag&edm=AP9-OL4BAAAA&ccb=7-5&ig_cache_key=GD30OCfoxl_4Wf5BAOV6SE5yjoY5bmNDAQAB1501500j-ccb7-5&oh=00_Af3NN_aWofVniNzKmBem6US58PE0VG0J7RS5EEdWxbCOdg&oe=69DC3785&_nc_sid=a62bc8",
      "username": "natgeoscience",
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
      "latest_reel_media": 1775642636,
      "should_show_category": true,
      "show_ring_award": false,
      "show_text_post_app_badge": false,
      "unseen_count": 0,
      "social_context": "9.8M followers",
      "search_social_context": "9.8M followers",
      "search_social_context_snippet_type": "typeahead_follow_count"
    }
  }
]
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
    "media_count": 41384131,
    "allow_following": false,
    "profile_pic_url": null
  },
  {
    "id": "17843776981016110",
    "name": "lovestory",
    "media_count": 38694885,
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
    "cover_artwork_uri": "https://scontent-iad3-2.cdninstagram.com/v/t39.30808-6/426871115_1505357383342530_7331902838470414874_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=105&ccb=7-5&_nc_sid=2f2557&_nc_ohc=C2HtJGVAWqQQ7kNvwFmrJgg&_nc_oc=Adpk8XYw_8_9ItrGKoc15YjhzNZJEJNbCsQQ4VsFzg_W68eX5IH4_NjP0mKC_vW8h_U&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=P2Qh0rO0OM-s4eT67e4WlQ&_nc_ss=7a39b&oh=00_Af1EZIpaasr6vRn-PiMDlYg0OPmHlnMDNDpjsLSKkLnmUA&oe=69DC69B7",
    "cover_artwork_thumbnail_uri": "https://scontent-iad3-2.cdninstagram.com/v/t39.30808-6/426871115_1505357383342530_7331902838470414874_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=105&ccb=7-5&_nc_sid=2f2557&_nc_ohc=C2HtJGVAWqQQ7kNvwFmrJgg&_nc_oc=Adpk8XYw_8_9ItrGKoc15YjhzNZJEJNbCsQQ4VsFzg_W68eX5IH4_NjP0mKC_vW8h_U&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=P2Qh0rO0OM-s4eT67e4WlQ&_nc_ss=7a39b&oh=00_Af0zYCq5ftYURrzn4MKwTCNApEVSXjJy4tkoRjdjcsfjgw&oe=69DC69B7",
    "progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=sY5HPWJPCK8Q7kNvwElgc1g&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=1f315079ae391eba&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR1RlV1NEc1V6bGNrWUFDQUVtNnVEcXNyRDB3Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtInB8srQvQMVAigCQzMsF0B1mPXCj1wpGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af24wogNh51tpNC36EkPtGeu46_bhqrt79mMLcn9EiN3mA&oe=69DC5229",
    "fast_start_progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=sY5HPWJPCK8Q7kNvwElgc1g&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=1f315079ae391eba&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR1RlV1NEc1V6bGNrWUFDQUVtNnVEcXNyRDB3Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtInB8srQvQMVAigCQzMsF0B1mPXCj1wpGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af24wogNh51tpNC36EkPtGeu46_bhqrt79mMLcn9EiN3mA&oe=69DC5229",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      113000,
      128500,
      1500
    ],
    "is_explicit": false,
    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT345.559998S\" FBManifestTimestamp=\"1775664104\" FBManifestIdentifier=\"FtDvs50NKRa8iKX5/arxBiIYFGF1ZGlvX2FhY19sbl92YnJfbXB4IjaaCxQAEgA=\"><Period id=\"0\" duration=\"PT345.559998S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1938077947044382a\" bandwidth=\"62920\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"62920\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&amp;_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=sY5HPWJPCK8Q7kNvwElgc1g&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJiaXRyYXRlIjo2Mjk4NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af06JQJ29cr7nGad9GhsaleiHkSw8lfQ9PwGmnKYuQYP9w&amp;oe=69DC5229</BaseURL><SegmentBase indexRange=\"824-2931\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
    "cover_artwork_uri": "https://scontent-xxc1-1.cdninstagram.com/v/t39.30808-6/426406817_917490163390033_8060542730959388333_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=ADJkpyWW1xEQ7kNvwEDoshs&_nc_oc=AdpIA70HtLm9OHy85A-oefkh79u6kyRJ8DAEVErsUD0TLixYmVmiC57kur8Qe4_WZ3Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_gid=P2Qh0rO0OM-s4eT67e4WlQ&_nc_ss=7a39b&oh=00_Af0TJMxpNj4J0WtRug5yBf-_l7zPWMuK8_TwzesP8thbug&oe=69DC6177",
    "cover_artwork_thumbnail_uri": "https://scontent-xxc1-1.cdninstagram.com/v/t39.30808-6/426406817_917490163390033_8060542730959388333_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=ADJkpyWW1xEQ7kNvwEDoshs&_nc_oc=AdpIA70HtLm9OHy85A-oefkh79u6kyRJ8DAEVErsUD0TLixYmVmiC57kur8Qe4_WZ3Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_gid=P2Qh0rO0OM-s4eT67e4WlQ&_nc_ss=7a39b&oh=00_Af3LcIDNILZAjeo4WRcSmItYk-OcSAI5tfnZ3pny1zWRtQ&oe=69DC6177",
    "progressive_download_url": "https://scontent-xxc1-1.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_ohc=1u3JU8oeORIQ7kNvwFve06a&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=78f9e84ff2874f58&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT0xLSlNDOXVyMlRva0VDQU9pdFA2cTJUZVpGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm1KLwyMT5qwMVAigCQzMsF0BmDhR64UeuGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af2BmJYUkCXHVBrOdqtEMzBmue9cXMLSEuRbzBeWkZcwPg&oe=69DC3FFC",
    "fast_start_progressive_download_url": "https://scontent-xxc1-1.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_ohc=1u3JU8oeORIQ7kNvwFve06a&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=78f9e84ff2874f58&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT0xLSlNDOXVyMlRva0VDQU9pdFA2cTJUZVpGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm1KLwyMT5qwMVAigCQzMsF0BmDhR64UeuGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af2BmJYUkCXHVBrOdqtEMzBmue9cXMLSEuRbzBeWkZcwPg&oe=69DC3FFC",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      27000,
      93000,
      66500
    ],
    "is_explicit": false,
    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT176.440002S\" FBManifestTimestamp=\"1775664104\" FBManifestIdentifier=\"FtDvs50NKRaw1bqrktGSBSIYFGF1ZGlvX2FhY19sbl92YnJfbXB4IjaeCxQAEgA=\"><Period id=\"0\" duration=\"PT176.440002S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1448351333045592a\" bandwidth=\"56442\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"56442\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-xxc1-1.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxc1-1.cdninstagram.com&amp;_nc_ohc=1u3JU8oeORIQ7kNvwFve06a&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJiaXRyYXRlIjo1NjUyOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af04abyeacriWCB0nW8MdU7ujJ6gHiEd3QdwywuTOQlSHQ&amp;oe=69DC3FFC</BaseURL><SegmentBase indexRange=\"824-1923\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "has_lyrics": false,
    "audio_asset_id": "3071277199804105",
    "duration_in_ms": 176440,
    "dark_message": null,
    "allows_saving": false,
    "territory_validity_periods": null
  },
  {
    "id": "796720467705509",
    "title": "Nanila",
    "subtitle": "",
    "display_artist": "Sukhishvili Georgian National Ballet",
    "audio_cluster_id": "521947385822142",
    "artist_id": null,
    "cover_artwork_uri": "https://scontent-iad6-1.cdninstagram.com/v/t39.30808-6/417539549_1343884206328266_172065523988983385_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=102&ccb=7-5&_nc_sid=2f2557&_nc_ohc=SZmKOaqIG5sQ7kNvwFq_jSW&_nc_oc=AdpuLL9I9DzCkBTjf0ZacR7Ug9SHvekmerIhbD8SfSGpJVv1-9J6iJz67gykEFIBVxM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=P2Qh0rO0OM-s4eT67e4WlQ&_nc_ss=7a39b&oh=00_Af2vozP96AikpFyqfLyWvwQrZD2jvdaOVKu_GKhnZ9D6yQ&oe=69DC5825",
    "cover_artwork_thumbnail_uri": "https://scontent-iad6-1.cdninstagram.com/v/t39.30808-6/417539549_1343884206328266_172065523988983385_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=102&ccb=7-5&_nc_sid=2f2557&_nc_ohc=SZmKOaqIG5sQ7kNvwFq_jSW&_nc_oc=AdpuLL9I9DzCkBTjf0ZacR7Ug9SHvekmerIhbD8SfSGpJVv1-9J6iJz67gykEFIBVxM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=P2Qh0rO0OM-s4eT67e4WlQ&_nc_ss=7a39b&oh=00_Af3DhO8QTOJ3HcWXM1t7faixwUiRM9b9moW7Fgh9OhwWQg&oe=69DC5825",
    "progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQP4KbfWSBPd0FhNxwGSKIEp-le1hH3G0aC5KH5PkKJSAmFvOC3ibkQ1XGK7WT4AeYCV61LJ3uYax-uHP2jHKDGk.mp4?strext=1&_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=j56NAYKmH_QQ7kNvwF9zrJI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo0NTQ3NzM2NjM3Nzg5NDUsImFzc2V0X2FnZV9kYXlzIjoxNzUxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=debcc18c6dba69b2&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRmV5RlNDS2hkZVNoRFlDQUk3QTc4ZjRLbTR4Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmgqL26qfnzgEVAigCQzMsF0Bu9cKPXCj2GBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af2yhZo_tj5JOnCsYyp8vvI2L_MsXngpjTZPN12FSBcAmw&oe=69DC5FA4",
    "fast_start_progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQP4KbfWSBPd0FhNxwGSKIEp-le1hH3G0aC5KH5PkKJSAmFvOC3ibkQ1XGK7WT4AeYCV61LJ3uYax-uHP2jHKDGk.mp4?strext=1&_nc_cat=102&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=j56NAYKmH_QQ7kNvwF9zrJI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo0NTQ3NzM2NjM3Nzg5NDUsImFzc2V0X2FnZV9kYXlzIjoxNzUxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=debcc18c6dba69b2&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HRmV5RlNDS2hkZVNoRFlDQUk3QTc4ZjRLbTR4Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmgqL26qfnzgEVAigCQzMsF0Bu9cKPXCj2GBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af2yhZo_tj5JOnCsYyp8vvI2L_MsXngpjTZPN12FSBcAmw&oe=69DC5FA4",
    "reactive_audio_download_url": null,
    "highlight_start_times_in_ms": [
      45000,
      91000,
      60000
    ],
    "is_explicit": false,
    "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT247.679993S\" FBManifestTimestamp=\"1775664104\" FBManifestIdentifier=\"FtDvs50NKRbq7dWe0c79CCIYFGF1ZGlvX2FhY19sbl92YnJfbXB4IjaeCxQAEgA=\"><Period id=\"0\" duration=\"PT247.679993S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2528028654222197a\" bandwidth=\"56923\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"56923\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQP4KbfWSBPd0FhNxwGSKIEp-le1hH3G0aC5KH5PkKJSAmFvOC3ibkQ1XGK7WT4AeYCV61LJ3uYax-uHP2jHKDGk.mp4?strext=1&amp;_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=j56NAYKmH_QQ7kNvwF9zrJI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo0NTQ3NzM2NjM3Nzg5NDUsImFzc2V0X2FnZV9kYXlzIjoxNzUxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MjQ3LCJiaXRyYXRlIjo1Njk5NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1WE0isGLNxtCnGRtY9P2Uv9k2zGPSREu95lvGPC-ggJw&amp;oe=69DC5FA4</BaseURL><SegmentBase indexRange=\"824-2343\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "has_lyrics": false,
    "audio_asset_id": "796720467705509",
    "duration_in_ms": 247680,
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
    "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFhD_J45rnVzhT_i5dIxvNoTYzwg8mSDyAbxvw7rwfy-XbXUt5vwOMtmKwI5wMOLMw&_nc_ohc=XbeNvhLXv28Q7kNvwHBvQaA&_nc_gid=ur6c7LWrgTMHBb2OqkIo6A&edm=ANei9xoBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ASP3QitklF3omUKj-dsKmeV2tPUmS7ViXGRm2VV5DXg&oe=69DC51E9&_nc_sid=3b96ff",
    "profile_pic_url_hd": null,
    "is_private": null,
    "is_verified": null
  },
  {
    "pk": 23947096,
    "id": "23947096",
    "username": "natgeotravel",
    "full_name": "National Geographic Travel",
    "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFhD_J45rnVzhT_i5dIxvNoTYzwg8mSDyAbxvw7rwfy-XbXUt5vwOMtmKwI5wMOLMw&_nc_ohc=t-DCVZxwtX4Q7kNvwHqpzGq&_nc_gid=ur6c7LWrgTMHBb2OqkIo6A&edm=ANei9xoBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af1n7D2c1mnaYRvBabKiRhbINwz-gaov6CngMPwg3hTWow&oe=69DC6746&_nc_sid=3b96ff",
    "profile_pic_url_hd": null,
    "is_private": null,
    "is_verified": null
  },
  {
    "pk": 57601166705,
    "id": "57601166705",
    "username": "natgeobooks",
    "full_name": "Nat Geo Books",
    "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.2885-19/375071684_834134081404702_4235507074871478129_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zNjAuYzIifQ&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFhD_J45rnVzhT_i5dIxvNoTYzwg8mSDyAbxvw7rwfy-XbXUt5vwOMtmKwI5wMOLMw&_nc_ohc=uukKuvJR6fAQ7kNvwFBQyzS&_nc_gid=ur6c7LWrgTMHBb2OqkIo6A&edm=ANei9xoBAAAA&ccb=7-5&ig_cache_key=GMQjWxYe-535o-YCAHFHXnE_i8c6bkULAAAB1501500j-ccb7-5&oh=00_Af3lPr7C2SoLw0hDOTB0CLAsVMaXtcLg_hMGC88qPHpyHw&oe=69DC3B6C&_nc_sid=3b96ff",
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
