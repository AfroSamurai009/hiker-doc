# Search Endpoints

Search across users, hashtags, places, reels.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v2/fbsearch/accounts`](#get-v2fbsearchaccounts) | [`/v2/fbsearch/places`](#get-v2fbsearchplaces) | [`/v2/fbsearch/reels`](#get-v2fbsearchreels) | [`/v2/fbsearch/topsearch`](#get-v2fbsearchtopsearch) | [`/v2/search/accounts`](#get-v2searchaccounts) | [`/v2/search/hashtags`](#get-v2searchhashtags) | [`/v2/search/music`](#get-v2searchmusic) | [`/v2/search/places`](#get-v2searchplaces) | [`/v2/search/reels`](#get-v2searchreels) | [`/v2/search/topsearch`](#get-v2searchtopsearch)

---

### GET /v2/fbsearch/accounts

Search accounts. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `page_token` | string | No | Page Token |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/fbsearch/accounts?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_accounts_v2(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/fbsearch/accounts",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/fbsearch/accounts?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "num_results": 20,
  "users": [
    {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "pk": 787132,
      "pk_id": "787132",
      "is_verified_search_boosted": false,
      "search_serp_type": 3,
      "third_party_downloads_enabled": 2,
      "id": "787132",
      "full_name": "National Geographic",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG_GAQRRgW9ppH96z9R5f9K6vLLS319yE09wlVSGGzp9v6_T1toq5xsB5v53rNIFA4&_nc_ohc=XbeNvhLXv28Q7kNvwGUzvDW&_nc_gid=LbgU-b7d_og8D4bh2cpnKQ&edm=ALgmGsQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1e4u5nkKmfBVKbiPNYrDaEKS9bS_A2wzsqTEto_0_t4g&oe=69DC51E9&_nc_sid=2f557e",
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
    },
    {
      "strong_id__": "18091046",
      "fbid_v2": 17841401291380282,
      "pk": 18091046,
      "pk_id": "18091046",
      "is_verified_search_boosted": false,
      "search_serp_type": 3,
      "third_party_downloads_enabled": 2,
      "id": "18091046",
      "full_name": "National Geographic TV",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865691934048399589_18091046",
      "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG_GAQRRgW9ppH96z9R5f9K6vLLS319yE09wlVSGGzp9v6_T1toq5xsB5v53rNIFA4&_nc_ohc=zov5ST0QeW4Q7kNvwH-olLD&_nc_gid=LbgU-b7d_og8D4bh2cpnKQ&edm=ALgmGsQBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af1YG8Ket7DpORVWBcmsTCbFSInv5olVvJ-plkBi5ewb-g&oe=69DC4D93&_nc_sid=2f557e",
      "username": "natgeotv",
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
      "is_ring_creator": false,
      "latest_reel_media": 1775600255,
      "should_show_category": true,
      "show_ig_app_switcher_badge": false,
      "show_ring_award": false,
      "show_text_post_app_badge": true,
      "unseen_count": 0,
      "social_context": "7.3M followers",
      "search_social_context": "7.3M followers",
      "search_social_context_snippet_type": "typeahead_follow_count"
    }
  ],
  "has_more": true,
  "rank_token": "1775657961434|560efc2272a6c94609fad2a0ff78f23dcea267448420a5f37e9d632dfd88c4fc",
  // ... truncated
```

</details>

---

### GET /v2/fbsearch/places

Search places. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/fbsearch/places?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_places_v2(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/fbsearch/places",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/fbsearch/places?query=natgeo",
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
      "location": {
        "pk": 252923412072688,
        "facebook_places_id": 252923412072688,
        "external_source": "facebook_places",
        "name": "NatGeo Roof Deck",
        "address": "161 6th Ave",
        "city": "",
        "has_viewer_saved": false,
        "short_name": "NatGeo Roof Deck",
        "lng": -74.004295349121,
        "lat": 40.725898742676
      },
      "title": "NatGeo Roof Deck",
      "subtitle": "3.5mi · 161 6th Ave"
    },
    {
      "location": {
        "pk": 617882014,
        "facebook_places_id": 219266724863910,
        "external_source": "facebook_places",
        "name": "أسرار Nat Geo",
        "address": "625 Union St",
        "city": "",
        "has_viewer_saved": false,
        "short_name": "أسرار Nat Geo",
        "lng": -73.98444,
        "lat": 40.67817
      },
      "title": "أسرار Nat Geo",
      "subtitle": "4.9mi · 625 Union St"
    }
  ],
  "has_more": false,
  "rank_token": "1775657963126|a7f8e7e6b90f443139fb9a1d9d0cd17b252acd0a62adedc77841aeee5aa16a33",
  "status": "ok"
}
```

</details>

---

### GET /v2/fbsearch/reels

Search top content by keyword. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `reels_max_id` | string | No | Reels Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/fbsearch/reels?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_reels_v2(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/fbsearch/reels",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/fbsearch/reels?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "reels_serp_modules": [
    {
      "module_type": "clips",
      "clips": [
        {
          "media": {
            "strong_id__": "3862872167406407463_787132",
            "id": "3862872167406407463_787132",
            "disable_caption_and_comment": false,
            "fbid": 18541785190065574,
            "deleted_reason": 0,
            "client_cache_key": "Mzg2Mjg3MjE2NzQwNjQwNzQ2Mw==.3",
            "integrity_review_decision": "pending",
            "pk": 3862872167406407463,
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
                    6319,
                    12638
                  ],
                  "height": 1136,
                  "scans_profile": "e15",
                  "url": "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/658909408_1905912193388666_3112418156369921885_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=103&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=7CReZ6aNvCIQ7kNvwFDBKWE&_nc_oc=AdrSGUT-UfsE9NnsGWOqrgMvWUtZPrF36Web15OYHbZ0XwVNgLglgNZIQQ0gTsuSKJM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=Ib0Xgok9HXKyhDiy3muVyw&_nc_ss=7a3ba&oh=00_Af0-mAzfSd9sCKyou4xcWXdEZon8s0bS4Aq-6TEBZUddmg&oe=69DC4640",
                  "width": 640,
                  "is_spatial_image": false
                },
                "igtv_first_frame": {
                  "estimated_scans_sizes": [
                    6319,
                    12638
                  ],
                  "height": 1136,
                  "scans_profile": "e15",
                  "url": "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/658909408_1905912193388666_3112418156369921885_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=103&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=7CReZ6aNvCIQ7kNvwFDBKWE&_nc_oc=AdrSGUT-UfsE9NnsGWOqrgMvWUtZPrF36Web15OYHbZ0XwVNgLglgNZIQQ0gTsuSKJM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=Ib0Xgok9HXKyhDiy3muVyw&_nc_ss=7a3ba&oh=00_Af0-mAzfSd9sCKyou4xcWXdEZon8s0bS4Aq-6TEBZUddmg&oe=69DC4640",
                  "width": 640,
                  "is_spatial_image": false
                },
                "smart_frame": null
              },
              "candidates": [
                {
                  "estimated_scans_sizes": [
                    30230,
                    60460
                  ],
                  "height": 1333,
                  "scans_profile": "e35",
                  "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/657714755_18644691667019133_1727136956736496715_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg2Mjg3MjE2NzQwNjQwNzQ2MzE4NjQ0NjkxNjYxMDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=YLfTq5Hruj0Q7kNvwEJM_Z_&_nc_oc=AdqEfsH-ec049CTveTvEvjOC6EjaqswxFfGZJAk2eOAKDES26rLN9U5erq5NmFbBMZk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=Ib0Xgok9HXKyhDiy3muVyw&_nc_ss=7a3ba&oh=00_Af0YqjXF31QmO1eILN7Wxz141ppR6CZFpHDsJN0dvGCDBQ&oe=69DC3068",
                  "width": 750,
                  "is_spatial_image": false
                }
              ],
              "scrubber_spritesheet_info_candidates": {
                "default": {
                  "file_size_kb": 668,
                  "max_thumbnails_per_sprite": 105,
                  "rendered_width": 96,
                  "sprite_height": 1232,
                  "sprite_urls": [
                    "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/657370271_1249133154036246_8413747161581570535_n.jpg?_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gFeoHuVL3KijI6yrzn15W48yakA9pEO0n9FrcqNdDgLixOR93zQAEMUfxGpJiOPCPA&_nc_ohc=vF93MVgKN5sQ7kNvwE8HRBK&_nc_gid=Ib0Xgok9HXKyhDiy3muVyw&edm=AL2I2h8BAAAA&ccb=7-5&oh=00_Af3l99qPXoI5ISCwwIn-7Yu_USukyp_92IxY7heNZhpUYQ&oe=69DC1D8A&_nc_sid=026283"
                  ],
                  "sprite_width": 1500,
                  "thumbnail_duration": 0.5164666666666666,
                  "thumbnail_height": 176,
                  "thumbnail_width": 100,
  // ... truncated
```

</details>

---

### GET /v2/fbsearch/topsearch

Search top content by keyword. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `next_max_id` | string | No | Next Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/fbsearch/topsearch?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.fbsearch_topsearch_v2(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/fbsearch/topsearch",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/fbsearch/topsearch?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "list": [
    {
      "position": 0,
      "user": {
        "strong_id__": "787132",
        "fbid_v2": 17841400573960012,
        "pk": 787132,
        "pk_id": "787132",
        "is_verified_search_boosted": false,
        "search_serp_type": 3,
        "third_party_downloads_enabled": 2,
        "id": "787132",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH1E_fStzyc-yCTjmaBOwYrW73ulrENYyO9W2eQC_2Rx-xRACXARZosM1lOQSoW5Wk&_nc_ohc=XbeNvhLXv28Q7kNvwEHq1Il&_nc_gid=z4SaIV5tjlzdeBwIdZEAXA&edm=ACkRbIEBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0uSFY8w7rqClUAKbUGIPkilMWHml_BUSSD4ogvKffofQ&oe=69DC51E9&_nc_sid=cd0945",
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
        "strong_id__": "18091046",
        "fbid_v2": 17841401291380282,
        "pk": 18091046,
        "pk_id": "18091046",
        "is_verified_search_boosted": false,
        "search_serp_type": 3,
        "third_party_downloads_enabled": 2,
        "id": "18091046",
        "full_name": "National Geographic TV",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865691934048399589_18091046",
        "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH1E_fStzyc-yCTjmaBOwYrW73ulrENYyO9W2eQC_2Rx-xRACXARZosM1lOQSoW5Wk&_nc_ohc=zov5ST0QeW4Q7kNvwHV5LGk&_nc_gid=z4SaIV5tjlzdeBwIdZEAXA&edm=ACkRbIEBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af2AcyIb8nKu85jNN28BjEcTXgecPA7i0IgDF1fCsw-FGw&oe=69DC4D93&_nc_sid=cd0945",
        "username": "natgeotv",
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
        "is_ring_creator": false,
        "latest_reel_media": 1775600255,
        "should_show_category": true,
        "show_ig_app_switcher_badge": false,
        "show_ring_award": false,
        "show_text_post_app_badge": true,
        "unseen_count": 0,
        "social_context": "7.3M followers",
        "search_social_context": "7.3M followers",
        "search_social_context_snippet_type": "typeahead_follow_count"
  // ... truncated
```

</details>

---

### GET /v2/search/accounts

Search accounts. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `page_token` | string | No | Page Token |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/search/accounts?query=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/search/accounts",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/search/accounts?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "num_results": 20,
  "users": [
    {
      "strong_id__": "787132",
      "fbid_v2": 17841400573960012,
      "pk": 787132,
      "pk_id": "787132",
      "is_verified_search_boosted": false,
      "search_serp_type": 3,
      "third_party_downloads_enabled": 2,
      "id": "787132",
      "full_name": "National Geographic",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEAZnO1LcMJAEKaYYYczIHNc6pxlwkYNSW5uyI8fxc3y2rLbVe0jf43P58cIg9-e88&_nc_ohc=XbeNvhLXv28Q7kNvwEV32Qq&_nc_gid=8eq-hDx7BIDopD5-99LLHA&edm=ALgmGsQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af16fncYKy7zNZcX1XY9XrFqy7KrGP3pEkRH9KdWdmWz5g&oe=69DC51E9&_nc_sid=2f557e",
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
    },
    {
      "strong_id__": "23947096",
      "fbid_v2": 17841400332880374,
      "pk": 23947096,
      "pk_id": "23947096",
      "is_verified_search_boosted": false,
      "search_serp_type": 3,
      "third_party_downloads_enabled": 2,
      "id": "23947096",
      "full_name": "National Geographic Travel",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865702501739707616_23947096",
      "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEAZnO1LcMJAEKaYYYczIHNc6pxlwkYNSW5uyI8fxc3y2rLbVe0jf43P58cIg9-e88&_nc_ohc=t-DCVZxwtX4Q7kNvwHxs11W&_nc_gid=8eq-hDx7BIDopD5-99LLHA&edm=ALgmGsQBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af3lmPMXy9aHDFo-DAizYTATjZAmYn9SIdJP6zx1yZKnhQ&oe=69DC2F06&_nc_sid=2f557e",
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
  ],
  "has_more": true,
  "rank_token": "1775657967513|6da74df6bfc6049907c0ebfe96431c1ed32be144b96863c9f72fbb15d3685696",
  "clear_client_cache": false,
  // ... truncated
```

</details>

---

### GET /v2/search/hashtags

Search hashtags. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `page_token` | string | No | Page Token |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/search/hashtags?query=love"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_hashtags_v2(query="love")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/search/hashtags",
        headers=headers,
        params={"query": "love"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/search/hashtags?query=love",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "results": [
    {
      "id": 17843826142012701,
      "name": "love",
      "media_count": 2147483647,
      "formatted_media_count": "2.1B",
      "search_result_subtitle": "2.1B posts",
      "use_default_avatar": true,
      "challenge_id": 1
    },
    {
      "id": 17843851987047311,
      "name": "lovehim",
      "media_count": 41383434,
      "formatted_media_count": "41.3M",
      "search_result_subtitle": "41.3M posts",
      "use_default_avatar": true,
      "challenge_id": 1
    }
  ],
  "has_more": false,
  "inform_module": null,
  "rank_token": "1775657966324|05e143d4c8d57e8cc5780c3ca515c8da22be9467033e2a34a6e185571b0be8d0",
  "page_token": null,
  "status": "ok"
}
```

</details>

---

### GET /v2/search/music

Search music. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `next_max_id` | string | No | Next Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/search/music?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.search_music_v2(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/search/music",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/search/music?query=natgeo",
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
      "track": {
        "audio_cluster_id": "2045685665695806",
        "id": "1283502475113803",
        "title": "National Geographic",
        "sanitized_title": null,
        "subtitle": "",
        "display_artist": "Winterlight",
        "artist_id": null,
        "cover_artwork_uri": "https://scontent-iad3-2.cdninstagram.com/v/t39.30808-6/426871115_1505357383342530_7331902838470414874_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=105&ccb=7-5&_nc_sid=2f2557&_nc_ohc=C2HtJGVAWqQQ7kNvwHB481g&_nc_oc=AdrnOHH7O10MAP0aMPoCVGWbI8hLC1fwWN5U7H4-A0U3MuVdC-cKheJ58EqkxRFuhPM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=icg0gOGfNLMWMA_OEqbu0Q&_nc_ss=7a39b&oh=00_Af0bX1z6_qal1GzSJKQMCbzTRubK5t58ELivtucTGK8mVA&oe=69DC3177",
        "cover_artwork_thumbnail_uri": "https://scontent-iad3-2.cdninstagram.com/v/t39.30808-6/426871115_1505357383342530_7331902838470414874_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=105&ccb=7-5&_nc_sid=2f2557&_nc_ohc=C2HtJGVAWqQQ7kNvwHB481g&_nc_oc=AdrnOHH7O10MAP0aMPoCVGWbI8hLC1fwWN5U7H4-A0U3MuVdC-cKheJ58EqkxRFuhPM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=icg0gOGfNLMWMA_OEqbu0Q&_nc_ss=7a39b&oh=00_Af3zAGy__wU8mvGazGjs2x7rJGlb4rxL_KjShBrGAikMgw&oe=69DC3177",
        "progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=sY5HPWJPCK8Q7kNvwFSyO5v&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=1f315079ae391eba&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR1RlV1NEc1V6bGNrWUFDQUVtNnVEcXNyRDB3Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtInB8srQvQMVAigCQzMsF0B1mPXCj1wpGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af1bu3MGBaVn-V8-ZPNu2h9rd9NgxxM-Jbs1CaGmjS3ZfQ&oe=69DC5229",
        "fast_start_progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=sY5HPWJPCK8Q7kNvwFSyO5v&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=1f315079ae391eba&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR1RlV1NEc1V6bGNrWUFDQUVtNnVEcXNyRDB3Ym1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmtInB8srQvQMVAigCQzMsF0B1mPXCj1wpGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af1bu3MGBaVn-V8-ZPNu2h9rd9NgxxM-Jbs1CaGmjS3ZfQ&oe=69DC5229",
        "web_30s_preview_download_url": null,
        "reactive_audio_download_url": null,
        "highlight_start_times_in_ms": [
          113000,
          128500
        ],
        "is_explicit": false,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT345.559998S\" FBManifestTimestamp=\"1775657964\" FBManifestIdentifier=\"FtiPs50NKRa8iKX5/arxBiIYFGF1ZGlvX2FhY19sbl92YnJfbXB4IjaaCxQAEgA=\"><Period id=\"0\" duration=\"PT345.559998S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1938077947044382a\" bandwidth=\"62920\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"62920\" audioSamplingRate=\"44100\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNfwv2Z46Ea9ogJroYTNncrV5n4YwW34uNxeJqaPubKbmg5HCcRq9o-GXq4ifSxTp19LXQKb2JCZhgB8Ua3WrQs.mp4?strext=1&amp;_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=sY5HPWJPCK8Q7kNvwFSyO5v&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5Nzk5NDk3OTA0Mzc5NzgsImFzc2V0X2FnZV9kYXlzIjoyODI2LCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MzQ1LCJiaXRyYXRlIjo2Mjk4NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3lWHPFHcnB6R4-tSswbfq--WSn3k18SxygiyC6o9qv3Q&amp;oe=69DC5229</BaseURL><SegmentBase indexRange=\"824-2931\" timescale=\"44100\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "has_lyrics": false,
        "audio_asset_id": "1283502475113803",
        "duration_in_ms": 345560,
        "dark_message": null,
        "allows_saving": true,
        "ig_username": null,
        "is_eligible_for_audio_effects": false,
        "is_eligible_for_vinyl_sticker": true,
        "lyrics": null,
        "licensed_music_subtype": "DEFAULT",
        "spotify_track_metadata": null,
        "song_monetization_info": null,
        "related_audios": null
      },
      "metadata": {
        "is_bookmarked": false,
        "allow_media_creation_with_music": true,
        "is_trending_in_clips": false,
        "trend_rank": null,
        "previous_trend_rank": null,
        "formatted_clips_media_count": "1,600 reels",
        "display_labels": null,
        "display_media_id": null,
        "user_notes": null,
        "bookmarked_start_time_in_ms": null,
        "inline_audio_label": null,
        "availability_info": null,
        "audio_filter_infos": null,
        "example_medias": null
      }
    },
    {
      "track": {
        "audio_cluster_id": "354492766725899",
        "id": "3071277199804105",
        "title": "Until I Found You",
        "sanitized_title": null,
        "subtitle": "",
        "display_artist": "Stephen Sanchez, Em Beihold",
        "artist_id": null,
        "cover_artwork_uri": "https://scontent-iad6-1.cdninstagram.com/v/t39.30808-6/426406817_917490163390033_8060542730959388333_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=ADJkpyWW1xEQ7kNvwGG7RqF&_nc_oc=Adpa351dCocjNWp0kP5yDjvaY1F58RtuQn7AeMRv114TNMnoDSfWubSNV608D5UTsmk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=icg0gOGfNLMWMA_OEqbu0Q&_nc_ss=7a39b&oh=00_Af1KD7goT-3JjDzuNI5N8QdmRCBWP3BKZgW9nqWefVkoiA&oe=69DC2937",
        "cover_artwork_thumbnail_uri": "https://scontent-iad6-1.cdninstagram.com/v/t39.30808-6/426406817_917490163390033_8060542730959388333_n.jpg?stp=dst-jpg_s168x128_tt6&_nc_cat=1&ccb=7-5&_nc_sid=2f2557&_nc_ohc=ADJkpyWW1xEQ7kNvwGG7RqF&_nc_oc=Adpa351dCocjNWp0kP5yDjvaY1F58RtuQn7AeMRv114TNMnoDSfWubSNV608D5UTsmk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=icg0gOGfNLMWMA_OEqbu0Q&_nc_ss=7a39b&oh=00_Af1oCU6PoxQJyhdkPazFcqxsP9oFvfwekTLWFHJos1oYpg&oe=69DC2937",
        "progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=1u3JU8oeORIQ7kNvwFiVWI_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=78f9e84ff2874f58&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT0xLSlNDOXVyMlRva0VDQU9pdFA2cTJUZVpGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm1KLwyMT5qwMVAigCQzMsF0BmDhR64UeuGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af0oM4jbVUPHQm5W96qwmyaMDrzU4vYQgQ333l1WqHbv6A&oe=69DC3FFC",
        "fast_start_progressive_download_url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&_nc_cat=1&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=1u3JU8oeORIQ7kNvwFiVWI_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5kYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=78f9e84ff2874f58&_nc_vs=HBkcFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HT0xLSlNDOXVyMlRva0VDQU9pdFA2cTJUZVpGYm1FeUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm1KLwyMT5qwMVAigCQzMsF0BmDhR64UeuGBxkYXNoX2xuX2hlYWFjX3ZicjNfbXB4X2F1ZGlvEQB1AGWQpQEA&_nc_ss=7a39b&_nc_zt=28&oh=00_Af0oM4jbVUPHQm5W96qwmyaMDrzU4vYQgQ333l1WqHbv6A&oe=69DC3FFC",
        "web_30s_preview_download_url": null,
        "reactive_audio_download_url": null,
        "highlight_start_times_in_ms": [
          27000,
          93000
        ],
        "is_explicit": false,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT176.440002S\" FBManifestTimestamp=\"1775657964\" FBManifestIdentifier=\"FtiPs50NKRaw1bqrktGSBSIYFGF1ZGlvX2FhY19sbl92YnJfbXB4IjaeCxQAEgA=\"><Period id=\"0\" duration=\"PT176.440002S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1448351333045592a\" bandwidth=\"56442\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"56442\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m69/AQNPuxEN9gcanGDO2QrF8sYOfCkQeudmF42ZNdCtpmxcVaYwUHdXE6ghHezMhGXLp3WQOlFjxnhoCEQHBmc3izIH.mp4?strext=1&amp;_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=1u3JU8oeORIQ7kNvwFiVWI_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19tcHhfYXVkaW8iLCJ2aWRlb19pZCI6bnVsbCwib2lsX3VybGdlbl9hcHBfaWQiOjI1NjI4MTA0MDU1OCwiY2xpZW50X25hbWUiOiJ1bmtub3duIiwieHB2X2Fzc2V0X2lkIjo5NDEwNzA4OTc1MTQ2NjYsImFzc2V0X2FnZV9kYXlzIjoxNDYxLCJ2aV91c2VjYXNlX2lkIjoxMDU2OCwiZHVyYXRpb25fcyI6MTc2LCJiaXRyYXRlIjo1NjUyOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1eFaHLiyL-1PvneSGbGSsoxoxnVhmmVyVWlrp0JAHE9g&amp;oe=69DC3FFC</BaseURL><SegmentBase indexRange=\"824-1923\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "has_lyrics": false,
        "audio_asset_id": "3071277199804105",
        "duration_in_ms": 176440,
        "dark_message": null,
        "allows_saving": true,
  // ... truncated
```

</details>

---

### GET /v2/search/places

Search places. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/search/places?query=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/search/places",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/search/places?query=natgeo",
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
      "location": {
        "pk": 252923412072688,
        "facebook_places_id": 252923412072688,
        "external_source": "facebook_places",
        "name": "NatGeo Roof Deck",
        "address": "161 6th Ave",
        "city": "",
        "has_viewer_saved": false,
        "short_name": "NatGeo Roof Deck",
        "lng": -74.004295349121,
        "lat": 40.725898742676
      },
      "title": "NatGeo Roof Deck",
      "subtitle": "3.5mi · 161 6th Ave"
    },
    {
      "location": {
        "pk": 617882014,
        "facebook_places_id": 219266724863910,
        "external_source": "facebook_places",
        "name": "أسرار Nat Geo",
        "address": "625 Union St",
        "city": "",
        "has_viewer_saved": false,
        "short_name": "أسرار Nat Geo",
        "lng": -73.98444,
        "lat": 40.67817
      },
      "title": "أسرار Nat Geo",
      "subtitle": "4.9mi · 625 Union St"
    }
  ],
  "has_more": false,
  "rank_token": "1775657978706|bdbea4891523c131ff7a9837e240b158c2809882a3e7af2d15926e77cc153ff7",
  "status": "ok"
}
```

</details>

---

### GET /v2/search/reels

Search top content by keyword. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `reels_max_id` | string | No | Reels Max Id |
| `rank_token` | string | No | Rank Token |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/search/reels?query=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/search/reels",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/search/reels?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "reels_serp_modules": [],
  "has_more": false,
  "other_results": {
    "keyword_recommendations": {
      "keywords": [],
      "title": "Popular Searches"
    }
  },
  "status": "ok"
}
```

</details>

---

### GET /v2/search/topsearch

Search top content by keyword. Returns a list of matching results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `next_max_id` | string | No | Next Max Id |
| `rank_token` | string | No | Rank Token |
| `reels_max_id` | string | No | Reels Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/search/topsearch?query=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/search/topsearch",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/search/topsearch?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "list": [
    {
      "position": 0,
      "user": {
        "strong_id__": "787132",
        "fbid_v2": 17841400573960012,
        "pk": 787132,
        "pk_id": "787132",
        "is_verified_search_boosted": false,
        "search_serp_type": 3,
        "third_party_downloads_enabled": 2,
        "id": "787132",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-sin11-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sin11-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEMjYJGVUITC3I0iLpniFI401eXQd_B05hUx8rhEhcTyMbQkyvYWKsR2TqDXSPliys&_nc_ohc=XbeNvhLXv28Q7kNvwH0HBMS&_nc_gid=1CkfO_bfw6htntCcekXkUQ&edm=ACkRbIEBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2JHdKXbmpY7iTahS4uGUVqQd3SHkSaVM3vsJBd4vMu1Q&oe=69DC51E9&_nc_sid=cd0945",
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
        "search_serp_type": 3,
        "third_party_downloads_enabled": 2,
        "id": "23947096",
        "full_name": "National Geographic Travel",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702501739707616_23947096",
        "profile_pic_url": "https://scontent-sin11-2.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sin11-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEMjYJGVUITC3I0iLpniFI401eXQd_B05hUx8rhEhcTyMbQkyvYWKsR2TqDXSPliys&_nc_ohc=t-DCVZxwtX4Q7kNvwH_PzkM&_nc_gid=1CkfO_bfw6htntCcekXkUQ&edm=ACkRbIEBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af0UdfZRdUIM5sKQ6I9CY6s_46jF0dXdW4CsWXw_Ig0M3A&oe=69DC2F06&_nc_sid=cd0945",
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
  // ... truncated
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-search){ target=_blank }
