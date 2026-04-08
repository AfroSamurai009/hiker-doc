# User Endpoints

Get user profiles, followers, following lists, and search.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/user/about`](#get-v1userabout) | [`/v1/user/by/id`](#get-v1userbyid) | [`/v1/user/by/url`](#get-v1userbyurl) | [`/v1/user/by/username`](#get-v1userbyusername) | [`/v1/user/clips`](#get-v1userclips) | [`/v1/user/clips/chunk`](#get-v1userclipschunk) | [`/v1/user/followers`](#get-v1userfollowers) | [`/v1/user/followers/chunk`](#get-v1userfollowerschunk) | [`/v1/user/following`](#get-v1userfollowing) | [`/v1/user/following/chunk`](#get-v1userfollowingchunk) | [`/v1/user/guides`](#get-v1userguides) | [`/v1/user/medias`](#get-v1usermedias) | [`/v1/user/medias/chunk`](#get-v1usermediaschunk) | [`/v1/user/medias/pinned`](#get-v1usermediaspinned) | [`/v1/user/search/followers`](#get-v1usersearchfollowers) | [`/v1/user/search/following`](#get-v1usersearchfollowing) | [`/v1/user/tag/medias`](#get-v1usertagmedias) | [`/v1/user/tag/medias/chunk`](#get-v1usertagmediaschunk) | [`/v1/user/videos`](#get-v1uservideos) | [`/v1/user/videos/chunk`](#get-v1uservideoschunk) | [`/v1/user/web_profile_info`](#get-v1userweb_profile_info)

---

### GET /v1/user/about

Get user object by id. Returns user about info.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/about?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_about_v1(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/about",
        headers=headers,
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/about?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "username": "natgeo",
  "is_verified": true,
  "country": "United States",
  "date": "November 2010",
  "former_usernames": ""
}
```

</details>

---

### GET /v1/user/by/id

Get user object by id. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/id?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_id_v1(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/by/id",
        headers=headers,
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/by/id?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 787132,
  "username": "natgeo",
  "full_name": "National Geographic",
  "is_private": false,
  "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJ_SxN9VkHDXz3DTIpNQ1KTQfXoEOJ_pKTgzNcCbZsA4VKYYNOYuR6giZLUKyR6p0&_nc_ohc=XbeNvhLXv28Q7kNvwHtfJeG&_nc_gid=GvqM2A9HlBbVZSBBBpktiw&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0TpopTI4ofSf9nbChkLAqFh-Bj6KiYgLOlf5PUcd3uiw&oe=69DC51E9&_nc_sid=6c5dea",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274984769,
  "following_count": 193,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "external_url": "http://visitstore.bio/natgeo",
  "account_type": 2,
  "is_business": true,
  "public_email": "",
  "contact_phone_number": "",
  "public_phone_country_code": "",
  "public_phone_number": "",
  "business_contact_method": "UNKNOWN",
  "business_category_name": null,
  "category_name": null,
  "category": "",
  "address_street": "",
  "city_id": "0",
  "city_name": "",
  "latitude": null,
  "longitude": null,
  "zip": "",
  "instagram_location_id": "",
  "interop_messaging_user_fbid": 113671860027320
}
```

</details>

---

### GET /v1/user/by/url

Get user object by URL. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Url |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/url?url=https://www.instagram.com/natgeo/"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_url_v1(url="https://www.instagram.com/natgeo/")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/by/url",
        headers=headers,
        params={"url": "https://www.instagram.com/natgeo/"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/by/url?url=https://www.instagram.com/natgeo/",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 787132,
  "username": "natgeo",
  "full_name": "National Geographic",
  "is_private": false,
  "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFgle3MlaZHF4NwoewYMV5KBSdG5RPxFLSD_UsnIzFfqBgFvlVlvBvwRRP5bbXLgHw&_nc_ohc=XbeNvhLXv28Q7kNvwHOiAWe&_nc_gid=Xy89o_XJY4CDgXnHBGkBXw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0M07MK9LN1-qel8A7bDxVkaeTn-tdvyj7zoiLUXEG5KA&oe=69DC51E9&_nc_sid=164c1d",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274984769,
  "following_count": 193,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "external_url": "http://visitstore.bio/natgeo",
  "account_type": 2,
  "is_business": true,
  "public_email": "",
  "contact_phone_number": "",
  "public_phone_country_code": "",
  "public_phone_number": "",
  "business_contact_method": "UNKNOWN",
  "business_category_name": null,
  "category_name": null,
  "category": "",
  "address_street": "",
  "city_id": "0",
  "city_name": "",
  "latitude": null,
  "longitude": null,
  "zip": "",
  "instagram_location_id": "",
  "interop_messaging_user_fbid": 113671860027320
}
```

</details>

---

### GET /v1/user/by/username

Get user object by username. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_username_v1(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/by/username",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 787132,
  "username": "natgeo",
  "full_name": "National Geographic",
  "is_private": false,
  "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHAJKeMBl68Ur1ibjqC8ojD3n9PK3sPTt7eE0C4WyOhFP69lLBpXd3WDW7Ce1P-5ro&_nc_ohc=XbeNvhLXv28Q7kNvwFCmIGK&_nc_gid=af0BXoGCv49hkNPmBRuRbA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2SeTb8O1P4kuDMVgxIbS0p6aSf9J-C1MLiz46uS9jzzw&oe=69DC51E9&_nc_sid=164c1d",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274984769,
  "following_count": 193,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "external_url": "http://visitstore.bio/natgeo",
  "account_type": 2,
  "is_business": true,
  "public_email": "",
  "contact_phone_number": "",
  "public_phone_country_code": "",
  "public_phone_number": "",
  "business_contact_method": "UNKNOWN",
  "business_category_name": null,
  "category_name": null,
  "category": "",
  "address_street": "",
  "city_id": "0",
  "city_name": "",
  "latitude": null,
  "longitude": null,
  "zip": "",
  "instagram_location_id": "",
  "interop_messaging_user_fbid": 113671860027320
}
```

</details>

---

### GET /v1/user/clips

Get user clips. Returns a list of Media objects (Reels).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/clips?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/clips",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/clips?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870025531093850440",
    "id": "3870025531093850440_1029649300",
    "code": "DW1F7dciplI",
    "taken_at": "2026-04-07T13:00:04Z",
    "taken_at_ts": 1775566804,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwEyGeEL&_nc_oc=AdocPcgHduqeTffWd-lo8_juwea-DKZkGYcU8ru_OG69lS-g3oAaJZ7e6lH_lBN5j6I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&oh=00_Af2TG7O7V5MKNU_KMgKwqG1kxwI2VZhXCsDvPcAJDscLeA&oe=69DC46E1",
    "location": null,
    "user": {
      "pk": "1029649300",
      "id": "1029649300",
      "username": "natgeoanimals",
      "full_name": "National Geographic Animals",
      "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=ic5ODsLE2O8Q7kNvwF3mRjn&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af1YfUW7xPNHoQJlE_Opv797K8kZQ2ShOnyPxezRqQ8zyA&oe=69DC588C&_nc_sid=c024bc",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 493,
    "comments_disabled": false,
    "like_count": 50450,
    "play_count": 2594257,
    "has_liked": false,
    "caption_text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwEvaUYT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3I1zhwhT0RX6BBR_N-HpV3Ptn0YbqSRhphgBfeMPWCIQ&oe=69D853EC",
    "view_count": 0,
    "video_duration": 60.736000061035156,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          18248,
          36496,
          54745
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwEyGeEL&_nc_oc=AdocPcgHduqeTffWd-lo8_juwea-DKZkGYcU8ru_OG69lS-g3oAaJZ7e6lH_lBN5j6I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&oh=00_Af2TG7O7V5MKNU_KMgKwqG1kxwI2VZhXCsDvPcAJDscLeA&oe=69DC46E1",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1579353,
        "height": 1280,
        "id": "4284559321859069v",
        "type": 101,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwEvaUYT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3I1zhwhT0RX6BBR_N-HpV3Ptn0YbqSRhphgBfeMPWCIQ&oe=69D853EC",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1579353,
        "height": 1280,
        "id": "4284559321859069v",
        "type": 102,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwEvaUYT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3I1zhwhT0RX6BBR_N-HpV3Ptn0YbqSRhphgBfeMPWCIQ&oe=69D853EC",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1579353,
        "height": 1280,
        "id": "4284559321859069v",
        "type": 103,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwEvaUYT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3I1zhwhT0RX6BBR_N-HpV3Ptn0YbqSRhphgBfeMPWCIQ&oe=69D853EC",
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
        "best_audio_cluster_id": "1359881209309073"
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
        "is_reuse_allowed": false,
        "mashup_type": null,
        "mashups_allowed": false,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18548020762066838",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26338877092460506,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663890\" FBManifestIdentifier=\"FqTss50NKRbMrPbB5Z2pBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1498046678354726a\" bandwidth=\"66810\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66810\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m78/AQOElke-XjvO2ixFipAMNby9AqC5CZmOcY8PcbQDmAwEGdrdvbD58TPi5A5RKS7WbXpTrVlZQip3DhNxjBI2vRela2S063MA11oc5y0.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=XLhOSrzrzoUQ7kNvwGhMKlk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2dXhU8niabX7uqkMC4Q6Szf9kn5c6VWR-IlY7Gis_w5g&amp;oe=69D8589E</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 60727,
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
        "original_media_id": 3870025531093850440,
        "progressive_download_url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m69/AQPYF2mAhRbYzYMrI560MWB9XBJqAACyr7szcVbj1WFwaneaOm5BlFHWUM37z1AaOh6Oyo4BIq6T2yeHyTeibfXn.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=wTkgipWqtN0Q7kNvwE_bZme&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1DVNeRWuRIx3DrkgJ8LgXm-EesjPEgswfhI39tAuAkuQ&oe=69DC5663",
        "should_mute_audio": false,
        "time_created": 1775566809,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "1029649300",
          "pk": 1029649300,
          "pk_id": "1029649300",
          "id": "1029649300",
          "username": "natgeoanimals",
          "full_name": "National Geographic Animals",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865698702530758137_1029649300",
          "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=ic5ODsLE2O8Q7kNvwF3mRjn&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af1YfUW7xPNHoQJlE_Opv797K8kZQ2ShOnyPxezRqQ8zyA&oe=69DC588C&_nc_sid=c024bc"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663890\" FBManifestIdentifier=\"FqTss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZts71ud+73IoDiqC0wu3LjwPImKTi/7u7BL6Zk9OwssAE/t+w5JmOxQSSmNLH6cjSBZieqsPIy8gGkI+H2vHNqQfE+ZDoxqy3B4agj+zZt7wHqpzd2fSFoQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2AhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.1\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"868003729587559v\" bandwidth=\"178266\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1353206\" FBPlaybackResolutionMos=\"0:100,360:56.7,480:54.4,720:53.2,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.1,720:83.8,1080:76.2\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOsCsgfDrcn7Gsyqj04T425mPWmeq8-MeX07h5wqKf_ykgUXeoigrvG2JQeRp4Wd_MdM-ZLa9ORl60gPpY3e_JZiFGCQ5EL6KkXMnk.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=Uh48tAtlw1sQ7kNvwGDeQkO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTc4MjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2x8GcE8SY4LGbLpeXRt8WrsMOg0moJw5SzAUIlEEl9XA&amp;oe=69DC51D7</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10892\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-78531\" FBFirstSegmentRange=\"1014-106281\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106282-221200\" FBPrefetchSegmentRange=\"1014-106281\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2092036534705762v\" bandwidth=\"240856\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1828322\" FBPlaybackResolutionMos=\"0:100,360:63.6,480:60.6,720:58.1,1080:58.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95,480:93.1,720:88.4,1080:81.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPRuSajZ_hFnjDpVSn1TY6XCtP7Zo9QzDsXmaKDU4mXL33dQv9cZzKhXl7Y_oeRcW9BNsObRl_FpdyfkSlu8ArGYU5-l43-uxy7_sg.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=-0z8YeyvyDgQ7kNvwHdGsma&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjQwODU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1q5BFgRNFppR3Nvy9s0FNplC2y24xfVhAtAeHqLA6wfA&amp;oe=69DC6448</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-12646\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-105375\" FBFirstSegmentRange=\"1014-143432\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"143433-293318\" FBPrefetchSegmentRange=\"1014-143432\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1267502918297183v\" bandwidth=\"326220\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2476312\" FBPlaybackResolutionMos=\"0:100,360:69,480:66,720:63.5,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.4,480:95.3,720:93.4,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBZheSdr-Op1k9B7pYwuciRaL5RCC2XcBVLkVwDPXAKrAhlrALgBooKgZk6nCMZz5AvNoGknQE18-kCW9-RNH_qVgCyawe5etIWbE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=4ClMe01ofx0Q7kNvwFExq_Y&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzI2MjIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3KlUtR37Tw6evlu6daiPnqkKsAU6O4NBrSvXcxPXv7bQ&amp;oe=69DC57D8</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-15483\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-142126\" FBFirstSegmentRange=\"1014-195190\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"195191-393663\" FBPrefetchSegmentRange=\"1014-195190\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1277876490344447v\" bandwidth=\"409602\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3109259\" FBPlaybackResolutionMos=\"0:100,360:73,480:69.8,720:67,1080:65.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.7,720:95.4,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxkQrl5cFyNncjOUGRq3XWMGmEnR7xzXjtdkfQlw0oreW4eSXmKA9eBGchHF9ByGL1ldZ-V_-LDFLMXxx4oytbIqVxuBwnRf-_tR0.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=5YrnOUUJMr4Q7kNvwGZgfkn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDA5NjAyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0JfsY_KY-nagrs4B0vhfND1J7JFuM1m0Iazw-1xKKQYw&amp;oe=69DC3457</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16985\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-176185\" FBFirstSegmentRange=\"1014-244141\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"244142-487399\" FBPrefetchSegmentRange=\"1014-244141\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1848477759129484v\" bandwidth=\"540603\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4103680\" FBPlaybackResolutionMos=\"0:100,360:77,480:74,720:70.7,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.24,480:98,720:97.4,1080:93.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP2bW0aIfz99a4ARx2Q2fPwwUvSZlmUT1jxqzlfSPxqDy_XKQdY1A9deJRHs78I9y2z_ngWT2zfhDIKZ8-XZxBrQWFF9SDm2muWNnE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=M35pMpEQ64sQ7kNvwG4ySdJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NTQwNjAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af09OtHG6Lw6KGR0N2ubPIqqGXOwwiY3THKxCqR9Puji-A&amp;oe=69DC4906</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-18644\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-229855\" FBFirstSegmentRange=\"1014-321368\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"321369-630140\" FBPrefetchSegmentRange=\"1014-321368\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1588945909073417v\" bandwidth=\"681362\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"5172172\" FBPlaybackResolutionMos=\"0:100,360:80.4,480:76.6,720:73.2,1080:70.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.62,480:98.37,720:98.59,1080:95.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPuKZF2qKICjs08-k_G1H8gucF1aCSpWB6stiwUGXWNvKfX5Hm_pNaY4z6GYTR0ZmsxXCYFw3SGDP8cejuR9yWwzxdzv-J159SieXo.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=jd4D7ZlmtxMQ7kNvwG03BhB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjgxMzYyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0vnI6_7axUGhC62YGMNqIdNUFvLSz_ppb-S5SbAGsQcA&amp;oe=69DC4007</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-20592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-288895\" FBFirstSegmentRange=\"1014-405533\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"405534-781198\" FBPrefetchSegmentRange=\"1014-405533\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2061822901412808v\" bandwidth=\"912497\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6926702\" FBPlaybackResolutionMos=\"0:100,360:83.9,480:79.9,720:75.7,1080:72.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.077,480:98.93,720:99.306,1080:97.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOjiwsO48rCaOF6m6s4bgg66iRhLGj5CKjR4DDmQ8T9kE2SvEWALkKtR50Wk2wGAMLc1Ws3pNhZSA9Y-QIiggu_wdfx_Bl0gwfgXDQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=fEsXwzzt-3AQ7kNvwEQu5f3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6OTEyNDk3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2u_CKJIU6MCVWpWkS-F4osH84fdITrXnmd6Q-Lp_fOPg&amp;oe=69DC387A</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-23580\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-385865\" FBFirstSegmentRange=\"1014-544870\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"544871-1019514\" FBPrefetchSegmentRange=\"1014-544870\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4294793980782357a\" bandwidth=\"46380\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46380\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"353137\" FBPaqMos=\"87.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9GI-VauacxM2tCfwmiCOijhyH33zBWrM0Dr4JwD6i2FjABcTvvBGOXIydEyGVXVx6wkUjNuDAtapI93ufxCNL1tRZuAP-HRtBv50.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=Uo8ixeKIRUsQ7kNvwEPxKw2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjUxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3KeenqoqgTh0U6o-Q2oANi9j9wp-M_a4__NrbHYsUQwQ&amp;oe=69DC60EA</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2136\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-14938\" FBFirstSegmentRange=\"1025-28400\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28401-56361\" FBPrefetchSegmentRange=\"1025-28400\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1256673039910436a\" bandwidth=\"74812\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74812\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"568992\" FBPaqMos=\"89.65\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPA0IU4X5qD93OmmaSc1st7oueEaOmYwYCBhH3T3wOKN7WutkRMOZ1TDwC1ugFmlc5yKEeuM_xeo_vD4IzH2AbUDhA7xa2uuL_kti8.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=H10A9jvUydQQ7kNvwGFnEMG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NDk0NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0gCO1279BgoW9sQg-sxaZ7T-k_v5Z6n2xtYW6yCTlgWw&amp;oe=69DC6622</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21486\" FBFirstSegmentRange=\"1026-43481\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"43482-90615\" FBPrefetchSegmentRange=\"1026-43481\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"878713468520453a\" bandwidth=\"108352\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108352\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"823623\" FBPaqMos=\"83.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOhb37d5jmr5MvSl8eT28PWBputzk-lecQ-RBUBedLEv96EozZbcoK_AR-dP3eFTj3ZDuOnoWe6DiibSbh3Vjc_rcGupQpI3Z2uCnA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=qIB9a-mC_CIQ7kNvwFDXUHE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDg0ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af11_-rb4QqozYNRpYPPTJyfmNdBuht15bUgfdrqqHrTsg&amp;oe=69DC55C7</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2395\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-30757\" FBFirstSegmentRange=\"1021-62738\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62739-132935\" FBPrefetchSegmentRange=\"1021-62738\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2103223183861763a\" bandwidth=\"143947\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"143947\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1093864\" FBPaqMos=\"87.00\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOgH1TOj2U7Ucn9wQoBfkebTHLZ9A_EoIFXsEJ2CkC1MsQUoWoasexRt0uwJQMyHQr8MmjxA15OisXxvCobhDmp05SCyaFAKp2_vFI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=Kg8UNuEeTkcQ7kNvwEo-IAN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxNDQwODEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Go96Hc598JTH3SfsVkGTc05M7k9-acwuGpABUTTT7tw&amp;oe=69DC5327</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-45040\" FBFirstSegmentRange=\"1021-86500\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"86501-176000\" FBPrefetchSegmentRange=\"1021-86500\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "787132",
        "pk": 787132,
        "pk_id": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=XbeNvhLXv28Q7kNvwGZf0kV&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ZEUteDZE7lAxoLY-Ilxtx1bHPPQet2OgNS6ZWtIbcKA&oe=69DC51E9&_nc_sid=c024bc",
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
  },
  {
    "pk": "3869494020385423326",
    "id": "3869494020385423326_787132",
    "code": "DWzNE9hkj_e",
    "taken_at": "2026-04-06T19:00:16Z",
    "taken_at_ts": 1775502016,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwHG0_T8&_nc_oc=AdoFPz4KAGTR7JPC20TYOGu_xoz39bazQ8EVKvdecfaTxs5FhMWcy-71Bs83MOwfA0o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&oh=00_Af1hCoseil6wDeGYLYbCX0qqm-CF-OrMfxb4Ecbb8ZXx3Q&oe=69DC6315",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=XbeNvhLXv28Q7kNvwGZf0kV&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ZEUteDZE7lAxoLY-Ilxtx1bHPPQet2OgNS6ZWtIbcKA&oe=69DC51E9&_nc_sid=c024bc",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 65,
    "comments_disabled": false,
    "like_count": 11121,
    "play_count": 1488992,
    "has_liked": false,
    "caption_text": "In Hoppers, Piper Curda’s character Mabel explored her sense of wonder for the natural world with the help of hopping technology. For now, we still have to do it the old-fashioned way.\n\nSee Disney and Pixar’s new movie Hoppers, now playing, only in theaters, and step into wonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHfe7ml&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0qF9hcREHesPFuyzi_oCGeWMptxvvYI8iTFux-5Gc8Dg&oe=69D86DB8",
    "view_count": 0,
    "video_duration": 55.44499969482422,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          13479,
          26958,
          40438
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwHG0_T8&_nc_oc=AdoFPz4KAGTR7JPC20TYOGu_xoz39bazQ8EVKvdecfaTxs5FhMWcy-71Bs83MOwfA0o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&oh=00_Af1hCoseil6wDeGYLYbCX0qqm-CF-OrMfxb4Ecbb8ZXx3Q&oe=69DC6315",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1113315,
        "height": 1280,
        "id": "2358585431274531v",
        "type": 101,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHfe7ml&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0qF9hcREHesPFuyzi_oCGeWMptxvvYI8iTFux-5Gc8Dg&oe=69D86DB8",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1113315,
        "height": 1280,
        "id": "2358585431274531v",
        "type": 102,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHfe7ml&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0qF9hcREHesPFuyzi_oCGeWMptxvvYI8iTFux-5Gc8Dg&oe=69D86DB8",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1113315,
        "height": 1280,
        "id": "2358585431274531v",
        "type": 103,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHfe7ml&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0qF9hcREHesPFuyzi_oCGeWMptxvvYI8iTFux-5Gc8Dg&oe=69D86DB8",
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
        "best_audio_cluster_id": "2426975461070348"
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
        "is_reuse_allowed": false,
        "mashup_type": null,
        "mashups_allowed": false,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18606311365032744",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26295324880076257,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775663890\" FBManifestIdentifier=\"FqTss50NKRbEl5Tt0tWmAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"929459223037410a\" bandwidth=\"60820\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"60820\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m78/AQN38tw9LWdIk_CWlJ0ze2Ayn07LgXtA4TMaLXc-6SODK58HBqKnlOKk8_LTSIHFsE3VGUlntYj8FPrehpb5VftWJE3s0U_LvQcQ0p4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=ZHLfVpYSwAwQ7kNvwF1Y_OO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo2MDk5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3Xb8kbLp8sfA_zIt6xeTSTaQlocGe7FFya-wy-Vbj-UQ&amp;oe=69D865B3</BaseURL><SegmentBase indexRange=\"824-1191\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 55430,
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
        "original_media_id": 3869494020385423326,
        "progressive_download_url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKBMTmsUUaSlY28FrQeX4c4T6dijF6gtmaEyTFBN6pFY5bZ5DsQbcUjfr7pEffSR4eVHh1ugsHyMjH1cbkv8Kz.mp4?strext=1&_nc_cat=106&_nc_sid=8bf8fe&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=VR1-k3frXTsQ7kNvwF1Zsr8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af11fa8P_VK9TxePgp8F6kvVIa1_dDwFRnbS3eWGnlAmxw&oe=69DC53CC",
        "should_mute_audio": false,
        "time_created": 1775502020,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=XbeNvhLXv28Q7kNvwGZf0kV&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ZEUteDZE7lAxoLY-Ilxtx1bHPPQet2OgNS6ZWtIbcKA&oe=69DC51E9&_nc_sid=c024bc"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775663890\" FBManifestIdentifier=\"FqTss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZttbm7f2IgpUD7OHlgsygpwOI9qGs6c69A4K35IPMyMEDsI3CoKTHvgSc252C4sXBBPyF6YussKgF9KKOwMXurwXYlsvU5LXeBdjS1K7XuegF6PTG0/GH9wUiGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2AhQAEhQCAA==\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:73.2\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"890639983950251v\" bandwidth=\"148183\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1026735\" FBPlaybackResolutionMos=\"0:100,360:77,480:75.4,720:74.2,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:93.1,720:92.5,1080:88.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxVTdb31AW_INujP1IDvNHV263--MPtveeFNN3GUuUVYCWKFeS7YZ9ZN2G12w1BpIi_FdawNocSzgpCnZ_RmsvfPjiy1uTBHb9oZw.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=Azv6S-cYlSkQ7kNvwFlR2Wm&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTQ4MTgzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3E6jbF4jMOqMhxt_xyqXfPeLmYJptS7DtUMaqmVOtTRQ&amp;oe=69DC684E</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-11627\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-38956\" FBFirstSegmentRange=\"1002-59102\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"59103-123876\" FBPrefetchSegmentRange=\"1002-59102\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1496166365471102v\" bandwidth=\"217161\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1504667\" FBPlaybackResolutionMos=\"0:100,360:81.6,480:79.3,720:77.4,1080:76.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:95.5,720:95.4,1080:91.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0yhiq2c2nWFCoYYsXHyN0n4pQ1H3Bf1PillRJPvA7F7s4T2vZEWWlnN1ab7wlhBx2qkPUdSqWmZq9YiCbgQr1iy6TnVK92GJFM7E.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=-GnWOEbhFFMQ7kNvwE8tXig&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MjE3MTYxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1IndHaILfrYAymxTEgP0h-517-vfWXlLwqeakkooci9A&amp;oe=69DC5F5A</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-15046\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-52809\" FBFirstSegmentRange=\"1002-81554\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"81555-172554\" FBPrefetchSegmentRange=\"1002-81554\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1637064280544428v\" bandwidth=\"297468\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2061099\" FBPlaybackResolutionMos=\"0:100,360:85.4,480:83.2,720:81,1080:79.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.5,480:97.1,720:97.8,1080:94\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNmpoeNdw7yb2DNMihh-Q2G15Y477O-Sk1OLg5Yvc1SF5s2DvEEWcyZxNMIPHB9gTiEJuesLauW023efqZ9CuKWYNgVahVJF3UIkRc.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=DWIM7dIPpcYQ7kNvwG-Mrhf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mjk3NDY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af00gTJWMoIMZE-qQEN2HgE0yKAj7hut1khVZt_D7RzXDw&amp;oe=69DC3FEE</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-18788\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-68106\" FBFirstSegmentRange=\"1002-106801\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106802-227120\" FBPrefetchSegmentRange=\"1002-106801\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"930746796390518v\" bandwidth=\"386132\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2675439\" FBPlaybackResolutionMos=\"0:100,360:87.4,480:85.4,720:83.2,1080:81\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.11,480:98,720:98.9,1080:95.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOqmazZV0GgC-FMAgX5Uo4Hzr4dpsUwPLWUSkWVzIH2EIopdalxgjleoQbUfcUfP1apdP-4Gsa_iSGhTS3l313F1z6FbA8TyS6K2AY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=XpZ2XTBJDXAQ7kNvwGamRaj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mzg2MTMyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2uAE3WajSpmjq56ricd3_ZQKD9wMbcl9wHM6powZNxCQ&amp;oe=69DC5F0C</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-22235\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-83355\" FBFirstSegmentRange=\"1002-132950\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"132951-285253\" FBPrefetchSegmentRange=\"1002-132950\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1263463985333080v\" bandwidth=\"479911\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3325212\" FBPlaybackResolutionMos=\"0:100,360:88.9,480:86.9,720:84.7,1080:82.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.46,480:98.4,720:99.414,1080:96.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN5Sl_4u8bg21xVtk-cIUfm9Z6DIbmrVvFA9a9N55F9NWJNHo03righvcgXtgSk_3JVH4wvKy4OTeNsgcwEtoacof_IARGxdKkAT-A.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=P7dFgXaWfIwQ7kNvwEucBd8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NDc5OTExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2I6fGotfMx0wOuQKQLJEfJ89SZQU__iODjHZnsUnWcPw&amp;oe=69DC5DE8</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-26049\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-100642\" FBFirstSegmentRange=\"1002-162120\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"162121-346006\" FBPrefetchSegmentRange=\"1002-162120\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1669194164264244v\" bandwidth=\"600336\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4159614\" FBPlaybackResolutionMos=\"0:100,360:90.2,480:88.2,720:86,1080:83.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.75,480:98.79,720:99.619,1080:97.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOkSM-p5C4-U6nKoTCQGR9QEo9t8_5IVg-ngkZWi13nRqVLUyRlAs1Es-YozyB9s8bjtNsK18hWCL1Of88sI3ZDe_gO2S45lP4yjWI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=8zqHITencNwQ7kNvwHNTzJN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NjAwMzM2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3hILPim_cR_kxQl4j_2macRGUUs_my-mLpl_JAFoIxTA&amp;oe=69DC3AC3</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-30771\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-121891\" FBFirstSegmentRange=\"1002-198284\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"198285-422683\" FBPrefetchSegmentRange=\"1002-198284\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"988608596839873v\" bandwidth=\"797098\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"5522936\" FBPlaybackResolutionMos=\"0:100,360:91.3,480:89.4,720:87.2,1080:84.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.026,480:99.172,720:99.732,1080:97.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMf3Rx8OOzEgPrCPNBR-0Nt-fwNaR6LdwmdWPUwzv4ulTwm_6h2bijtJ5Bjd87z0Jr-dXFj9FkGKtlRGWG6WeJW59Fiu3efb5LsrRI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=B11mdo9l0D0Q7kNvwHkrHHR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Nzk3MDk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af269dowvXs-5sa-R02241P52OPy2_RKyt-5NFDx_1BvRw&amp;oe=69DC4992</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-37057\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-156105\" FBFirstSegmentRange=\"1002-256214\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"256215-544176\" FBPrefetchSegmentRange=\"1002-256214\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1615007113110956a\" bandwidth=\"45829\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45829\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"318635\" FBPaqMos=\"90.73\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOq8zAQzpeRCoSQuovKRKQeNbycFlDBjsuggCgJzVUNsydkP6wpqSMV87VACc6egwIxdyoZ9qyuATjsxvSkWgWUtLCaKeDUW5vI2l0.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=n8c3OFNcOe4Q7kNvwG-Z_JB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo0NTk3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1fZyX5srk8CWco3DpXxKH9VMakJUOBWz27oTcQlJLS0A&amp;oe=69DC5B70</BaseURL><SegmentBase indexRange=\"837-1012\" timescale=\"48000\" FBMinimumPrefetchRange=\"1013-2182\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1013-15598\" FBFirstSegmentRange=\"1013-28913\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28914-57244\" FBPrefetchSegmentRange=\"1013-28913\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1270034985105102a\" bandwidth=\"72011\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"72011\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"500096\" FBPaqMos=\"90.72\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNETgTPe23OWiy-KGFj4O0xaNmi9xW8k8We4jlz_Lesh43O4RfyZWEg4kgQ77avCmAh4dhCO9ERkZrtXpEBa1nLDn-iaNXSGANeubo.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=wOOs-JEmecsQ7kNvwHtBGMv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo3MjE1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0aS-LnBta48jK4DJTz4Xw25rN3q4aCFeX11hxPNF9oVA&amp;oe=69DC5EFF</BaseURL><SegmentBase indexRange=\"838-1013\" timescale=\"48000\" FBMinimumPrefetchRange=\"1014-2538\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-26077\" FBFirstSegmentRange=\"1014-48598\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48599-97300\" FBPrefetchSegmentRange=\"1014-48598\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"979919517793668a\" bandwidth=\"103761\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"103761\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"720138\" FBPaqMos=\"88.08\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNOpf9BEo2_A4jYtakOEtpNQQZDYD9C0aIFAN-Q6y8Ina7CtFSkF_92RvlAvk1DGfzRoyEa6eCluUBrw77Kir2QY9JUObENLk8IZsE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=sGdWzzK2ve0Q7kNvwFy8MdS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMDM5MDYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0m5bduldIBxXEqvhah3MiXMt8TVyMQTgJ1QG_2xs7VEA&amp;oe=69DC564E</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2467\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-36815\" FBFirstSegmentRange=\"1009-70144\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"70145-139522\" FBPrefetchSegmentRange=\"1009-70144\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1512628090423482a\" bandwidth=\"134031\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"134031\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"929932\" FBPaqMos=\"90.49\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMDkCHmLVEnsU6T5_aC7ZlGvMakuRW1O3OnJZfxZuCHE1fs0cf1weWXn_tPspjek6E1p7CHcVLpGZLRSFGGTuIaxYNUE1SlwG3YTc4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=sKJdfZK9eLkQ7kNvwF8vW0V&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMzQxNzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af31hWsrw_B7JxNi999AiNtmgNeI2llUA4HnxXCJa4zWhA&amp;oe=69DC5209</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2532\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-44659\" FBFirstSegmentRange=\"1009-85613\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85614-170092\" FBPrefetchSegmentRange=\"1009-85613\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "284634753",
        "pk": 284634753,
        "pk_id": "284634753",
        "id": "284634753",
        "username": "pixar",
        "full_name": "Pixar",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3715495057937025462_284634753",
        "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/543579175_18522017512026754_6429363176312325029_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzQuYzIifQ&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=v0quYpmBS-oQ7kNvwH5nOFf&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GCdcZiCC8lNCrc1BAKXDEqC_rzlZbmNDAQAB1501500j-ccb7-5&oh=00_Af0mdBJ_H7LjQq9LSePZ313c_iCtPLH8Xzvx9UNEaHgR8A&oe=69DC4FB3&_nc_sid=c024bc",
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
        "strong_id__": "18091046",
        "pk": 18091046,
        "pk_id": "18091046",
        "id": "18091046",
        "username": "natgeotv",
        "full_name": "National Geographic TV",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865691934048399589_18091046",
        "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=zov5ST0QeW4Q7kNvwGEHDM7&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af3zM6Ys5N4GFuiye0RHIeyHD3C8N69_PkUlu2GjO6c9MA&oe=69DC4D93&_nc_sid=c024bc",
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
  },
  {
    "pk": "3868170261056492782",
    "id": "3868170261056492782_787132",
    "code": "DWugFulAJTu",
    "taken_at": "2026-04-05T16:00:10Z",
    "taken_at_ts": 1775404810,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwGlgvD_&_nc_oc=AdrcrvmEMOz0qa_vAlhJ2b7Qk4XiSpbvxc-ySHwvIoWPQEWP_DZV568YH4u0ZlPdv60&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&oh=00_Af26fc3To5Jqse1eyNKI5lH_aUvwiVxgvNaqQ1BImkYLPg&oe=69DC4951",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=XbeNvhLXv28Q7kNvwGZf0kV&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ZEUteDZE7lAxoLY-Ilxtx1bHPPQet2OgNS6ZWtIbcKA&oe=69DC51E9&_nc_sid=c024bc",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 78,
    "comments_disabled": false,
    "like_count": 7479,
    "play_count": 1304824,
    "has_liked": false,
    "caption_text": "Spotted hyenas are a powerful example of the resilience and strength found in nature. For wildlife ecologist, conservation scientist, and National Geographic Explorer Dr. Christine Wilkinson (@christine_eleanor), these reminders are what wonder is all about. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwF9S36r&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3tfFXMoUkM98uvJflQcmW9OjVV8TcrfncrKDMTzrI0JQ&oe=69D87233",
    "view_count": 0,
    "video_duration": 47.893001556396484,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          18831,
          37662,
          56494
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwGlgvD_&_nc_oc=AdrcrvmEMOz0qa_vAlhJ2b7Qk4XiSpbvxc-ySHwvIoWPQEWP_DZV568YH4u0ZlPdv60&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&oh=00_Af26fc3To5Jqse1eyNKI5lH_aUvwiVxgvNaqQ1BImkYLPg&oe=69DC4951",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1064730,
        "height": 1280,
        "id": "799234956583164v",
        "type": 101,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwF9S36r&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3tfFXMoUkM98uvJflQcmW9OjVV8TcrfncrKDMTzrI0JQ&oe=69D87233",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1064730,
        "height": 1280,
        "id": "799234956583164v",
        "type": 102,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwF9S36r&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3tfFXMoUkM98uvJflQcmW9OjVV8TcrfncrKDMTzrI0JQ&oe=69D87233",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1064730,
        "height": 1280,
        "id": "799234956583164v",
        "type": 103,
        "url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwF9S36r&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3tfFXMoUkM98uvJflQcmW9OjVV8TcrfncrKDMTzrI0JQ&oe=69D87233",
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
        "best_audio_cluster_id": "919303480943593"
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
        "is_reuse_allowed": false,
        "mashup_type": null,
        "mashups_allowed": false,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18439666597118965",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26074550038833869,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBManifestTimestamp=\"1775663890\" FBManifestIdentifier=\"FqTss50NKRa4sr3lnNynAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"931771249568924a\" bandwidth=\"66894\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66894\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m78/AQObEBSySE0AGNBbG4lxf162Q155i5gTcG0OizHqB4rRxcGyySZDjummT0z9r1wsiCbVlaRrtWqIqFWzQVPE7UxmQ1lTMC4PQzMnv0M.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=8_2Uu26HoJkQ7kNvwE_BeMO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo2NzA4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2ZhvVSMn6FD5RHP3gYnpssPqfFulvQBxAbvzMeaw1Lgg&amp;oe=69D86E19</BaseURL><SegmentBase indexRange=\"824-1143\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 47881,
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
        "original_media_id": 3868170261056492782,
        "progressive_download_url": "https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m69/AQNsTvlWrX5b5jAnAagr-VEkXvHgjuh1R7UtSI3qunavCZFTpObST3AI8L-cDc_wZTw8bAKRL2XuixVvoM6ISAHt.mp4?strext=1&_nc_cat=100&_nc_sid=8bf8fe&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_ohc=TbFtdnyPN3QQ7kNvwFe2NxD&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0FKZZ7JCyfTOWKUeaZf0quzJ2svl9pF3eJW_OMtmWybw&oe=69DC4132",
        "should_mute_audio": false,
        "time_created": 1775404814,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=XbeNvhLXv28Q7kNvwGZf0kV&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1ZEUteDZE7lAxoLY-Ilxtx1bHPPQet2OgNS6ZWtIbcKA&oe=69DC51E9&_nc_sid=c024bc"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBManifestTimestamp=\"1775663890\" FBManifestIdentifier=\"FqTss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtqr2ipOkqaoE/uzmi+DUwQTY/ZqykLWzBYzui9+dy7oFvIKCpeXcugWC0LLG/6qIBpj24ID70pQG8K/21+KE9AaElZWwnoaCB6q17qvriZ0H2LbOkLaErFsiGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2BhQAEhQCAA==\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.7\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1536512375144606v\" bandwidth=\"125041\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"748393\" FBPlaybackResolutionMos=\"0:100,360:68.6,480:63.5,720:57.2,1080:52.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.7,480:90.2,720:86.7,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOC-37dngJq90Dyy1_JazUnnPGdWCHskETHnxkRIIJCSOlZF1fVQ-6mAFGNhj2z93WeeIs714OUklQmfut9nIzTnVBICEHS1YfCoAw.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=e25xSTehHgsQ7kNvwGl1Agt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTI1MDQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1RcQ64jIBqFCYArD6ZanAE0SwO3B47IXM2ZgwZfkbepQ&amp;oe=69DC5053</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-11379\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-53195\" FBFirstSegmentRange=\"978-73681\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"73682-177801\" FBPrefetchSegmentRange=\"978-73681\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1707180720280577v\" bandwidth=\"268984\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1609913\" FBPlaybackResolutionMos=\"0:100,360:82.1,480:77.4,720:72,1080:65\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:96,720:94.9,1080:90.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOoI_Qc5Hb567q3s03DZ7hurU3EPc934bMb3FmMMVaHXDUYxsb4QiUQt8F8TcKitfPDLHzHey1wENKGp-vSnIF1hHoyzJ4LrrK2kjM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=ajpqDB5imFoQ7kNvwGxO3nu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MjY4OTg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af28h-BPAkBbKTirmxzkjZyl5ct6ZatWu9PDOxXnz-wCfg&amp;oe=69DC64EB</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-19527\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-105884\" FBFirstSegmentRange=\"978-157985\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"157986-375189\" FBPrefetchSegmentRange=\"978-157985\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1944018522917880v\" bandwidth=\"368764\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2207110\" FBPlaybackResolutionMos=\"0:100,360:85.9,480:81.7,720:75.8,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.04,480:97.6,720:97.2,1080:93.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQM3ITI-kIVflLXqBQCMcqSKriqhB8j74oqGUj6f3pYWDnqOC18MUJJNe0oZbKf0kPXddx31PP3oAzTIyNssN5V0g7YFH89E5A-Ij6s.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=Mwx1ng6pC6sQ7kNvwELHRWa&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MzY4NzY0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af37T7FGay04fjL9Gwm57nBe_2PdjCF6lS02woKCDwZD1g&amp;oe=69DC662F</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-24075\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-141715\" FBFirstSegmentRange=\"978-216596\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"216597-512096\" FBPrefetchSegmentRange=\"978-216596\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1218968110062997v\" bandwidth=\"442503\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2648452\" FBPlaybackResolutionMos=\"0:100,360:87.7,480:83.8,720:77.5,1080:70.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.61,480:98.35,720:98.31,1080:95.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOYTMwguxNmYzts7ztqP3uq8QYqnySSAGvKGU84jFkz30lRwgwLYRu68NUaE4CuVcCCkccg0gJEpbQIdwnc6OfTFFkYbjN5LqbfVG4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=KFTAZdhAk40Q7kNvwGhZ65e&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NDQyNTAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0e7Z7SMP5rX81mI4djCWdcW_8qPflG-21O7TOKkrRCoQ&amp;oe=69DC56A1</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-27189\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-169993\" FBFirstSegmentRange=\"978-261689\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"261690-617097\" FBPrefetchSegmentRange=\"978-261689\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1734255584222604v\" bandwidth=\"593051\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3549501\" FBPlaybackResolutionMos=\"0:100,360:89.9,480:86.3,720:80.5,1080:72.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99,480:98.97,720:99.193,1080:97.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9lx9WGs0aObQ1f5j5Tn6y1xVQXR-Dwub7W_SxmroZb4LDoDVxPW13tmY1vHIkgBkSqIxvS44m4qTOlQHuogzz-fjvXsOFNStGw5o.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=IG_0Np9TPzEQ7kNvwF1DP-S&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NTkzMDUxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0rqRufhqsX0ekn7jmbetWGpjpVNLsrYzYXwPLKcC_jRA&amp;oe=69DC5BBE</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-32309\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-227501\" FBFirstSegmentRange=\"978-353323\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"353324-811886\" FBPrefetchSegmentRange=\"978-353323\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1974830039737666v\" bandwidth=\"808049\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4836297\" FBPlaybackResolutionMos=\"0:100,360:91.5,480:88.1,720:82.7,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.177,480:99.289,720:99.419,1080:98.77\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNxzz3B_d6VnnNmwILSsdhY1b8WYAyEq1nGyoBddc0-zErqxX-3eoxHWRJoRjzW8rt7CPCOSi7aXg9mJJvD7MDk23Y4mXgSrDlMMp0.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=1oWA7fT-WaIQ7kNvwFUENQG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6ODA4MDQ5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3DkBSvhMApt8wJubHKTwmdJfFhTcc1xa80ja6EpmeAgg&amp;oe=69DC3E3B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-37690\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-306742\" FBFirstSegmentRange=\"978-478293\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"478294-1073273\" FBPrefetchSegmentRange=\"978-478293\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2034265537498453v\" bandwidth=\"1150676\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6886972\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:89.4,720:84.3,1080:75.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.316,480:99.475,720:99.604,1080:99.184\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO8nzMmBULFzOq0Uc221nMlzpRXdUpXzRan5dqj-VDzxkIrtzc1nz0dI1BX50zPIMwgzzgD9a0zuNNVJoHjAR_qboR3srHbCUwAf98.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=AJfwxCErVuwQ7kNvwEqAmXI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTE1MDY3NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2akBU1GQHpYomt4qhAexWM6nzjMaoOqL9YFN7UKIsBpg&amp;oe=69DC467B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-42521\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-414721\" FBFirstSegmentRange=\"978-651076\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"651077-1467135\" FBPrefetchSegmentRange=\"978-651076\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"25711055888567724a\" bandwidth=\"43137\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"43137\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"259233\" FBPaqMos=\"86.23\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPwGwzN_jZWTG5g53W6HPaq6prVW3aFxZFUMoApdF5Bb07alTzINwfJIHhTt2__EB0B73uktjzHCPmfysFRIfXNu5jyUMQk7HQ2MAA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=D8aq4uZD0HoQ7kNvwFljLca&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo0MzMwMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af35S48LBDRUCZhHL2UE87Tcez5J2CHPEBDM_CWZl9nQjg&amp;oe=69DC3521</BaseURL><SegmentBase indexRange=\"837-988\" timescale=\"48000\" FBMinimumPrefetchRange=\"989-2211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"989-15011\" FBFirstSegmentRange=\"989-27427\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27428-53863\" FBPrefetchSegmentRange=\"989-27427\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1520437802786668a\" bandwidth=\"71500\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71500\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"429033\" FBPaqMos=\"87.36\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQM1qgyiYipO3nTb3Q4w_ENJZ3IxJuj0VPo2tuNaBczlM_oHVqwMkDYBW3T0y1773ATnvblNT7r_xf3TsujSnPIypzOSKbCvToAOuws.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=hwhUj3NemRQQ7kNvwHO7ZI9&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo3MTY2NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3L2qejTPhJVwJcsR1NLDn7HfszBS0PQqt3r4dWvAxA0Q&amp;oe=69DC4C06</BaseURL><SegmentBase indexRange=\"838-989\" timescale=\"48000\" FBMinimumPrefetchRange=\"990-2669\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"990-24617\" FBFirstSegmentRange=\"990-45672\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"45673-89246\" FBPrefetchSegmentRange=\"990-45672\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1270292424743743a\" bandwidth=\"104937\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"104937\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"629205\" FBPaqMos=\"81.20\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOSZPTrQoZvEzpNyz3hhbxCnafm4XAlkTPd_h7zn5N1n6R0Ga6E8UgDUI08GX-XKGcGJAxmhV-HhXGeeaJ0XyTdLAqhdbtcuwmB8ms.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=L_y6Qh90gVgQ7kNvwGJos5I&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMDUxMDEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af27E1csm0HZce4r9NKv5jY9QhtfUt0BzzTBgpP6WTAZgA&amp;oe=69DC5BBA</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2362\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-35155\" FBFirstSegmentRange=\"985-65716\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"65717-128980\" FBPrefetchSegmentRange=\"985-65716\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1536210714590086a\" bandwidth=\"136838\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"136838\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"820186\" FBPaqMos=\"83.96\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-bos5-1.cdninstagram.com/o1/v/t2/f2/m367/AQO7KXm8TEDvhztA9v_PIl-O0CaShP5_2iBO4ggZMBeDRGTOTXVI3umPjYEK9ju_ZrOe1b_AWcnu75HARzg6Y6KbrJQ7pMmp_w0mKfU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-bos5-1.cdninstagram.com&amp;_nc_ohc=itqu0TbKGQYQ7kNvwEfUFI4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMzcwMDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0c71fgW3HfX-l77IbrkiQdaXWv3zAUOAFHyvxEmQTcEw&amp;oe=69DC4117</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2442\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-44989\" FBFirstSegmentRange=\"985-85365\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85366-166815\" FBPrefetchSegmentRange=\"985-85365\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "271370325",
        "pk": 271370325,
        "pk_id": "271370325",
        "id": "271370325",
        "username": "christine_eleanor",
        "full_name": "christine wilkinson, phd",
        "is_private": false,
        "is_verified": false,
        "profile_pic_id": "3245086179333885169_271370325",
        "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.2885-19/404288054_706561544741164_8609495828476348252_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44ODguYzIifQ&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gE8DNEFleB0LjIYRBcRsarcwi1Jxy1wSgnbhEomo4tNFvBiy0eWuNBbXueCW4bl6Ls&_nc_ohc=9NDLLLLwDV8Q7kNvwFndsBk&_nc_gid=ZV6lKwjFNOoTqmKOY_Gvqw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GDbyGBgs4eItnYICAFxHikfXEnt3bkULAAAB1501500j-ccb7-5&oh=00_Af2FOYblm1gIHb1gilNKJSMTcv3Gr6P8JA1fIcfSu0yVjw&oe=69DC57AB&_nc_sid=c024bc",
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

### GET /v1/user/clips/chunk

Get part of user clips with cursor

The response includes trial publications
https://help.instagram.com/1013292530224018

Trial publications have no "reshare_count" field if you need to filter them. Returns a list of Media objects (Reels).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/clips/chunk?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_clips_chunk_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/clips/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/clips/chunk?user_id=787132",
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
      "pk": "3870025531093850440",
      "id": "3870025531093850440_1029649300",
      "code": "DW1F7dciplI",
      "taken_at": "2026-04-07T13:00:04Z",
      "taken_at_ts": 1775566804,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwHJBKTX&_nc_oc=AdqMGkVBJQV0g4kzcZQFj2avVJ95a23K_Eq7zBqLFhl1BeiuWfr7WsG8Z2jS_7uTpV8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&oh=00_Af0mrZYsncHJp3h66MmiyDR0rSZvOIaO762Jn6GCPDbrQA&oe=69DC46E1",
      "location": null,
      "user": {
        "pk": "1029649300",
        "id": "1029649300",
        "username": "natgeoanimals",
        "full_name": "National Geographic Animals",
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=ic5ODsLE2O8Q7kNvwE4irrr&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af1xmPrOOqpPmS1hb5QYIn2V-L58FGA0IJbhP-34YaL7ow&oe=69DC588C&_nc_sid=c024bc",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 493,
      "comments_disabled": false,
      "like_count": 50449,
      "play_count": 2594210,
      "has_liked": false,
      "caption_text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwF2MMNd&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1sxtsik89W8-sraMxVV1PJu9V_NGexau2Q5BYyU5yiPw&oe=69D853EC",
      "view_count": 0,
      "video_duration": 60.736000061035156,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            18248,
            36496,
            54745
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwHJBKTX&_nc_oc=AdqMGkVBJQV0g4kzcZQFj2avVJ95a23K_Eq7zBqLFhl1BeiuWfr7WsG8Z2jS_7uTpV8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&oh=00_Af0mrZYsncHJp3h66MmiyDR0rSZvOIaO762Jn6GCPDbrQA&oe=69DC46E1",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1579353,
          "height": 1280,
          "id": "4284559321859069v",
          "type": 101,
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwF2MMNd&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1sxtsik89W8-sraMxVV1PJu9V_NGexau2Q5BYyU5yiPw&oe=69D853EC",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1579353,
          "height": 1280,
          "id": "4284559321859069v",
          "type": 102,
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwF2MMNd&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1sxtsik89W8-sraMxVV1PJu9V_NGexau2Q5BYyU5yiPw&oe=69D853EC",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1579353,
          "height": 1280,
          "id": "4284559321859069v",
          "type": 103,
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwF2MMNd&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1sxtsik89W8-sraMxVV1PJu9V_NGexau2Q5BYyU5yiPw&oe=69D853EC",
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
          "best_audio_cluster_id": "1359881209309073"
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
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18548020762066838",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26338877092460506,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": true,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663876\" FBManifestIdentifier=\"Fojss50NKRbMrPbB5Z2pBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1498046678354726a\" bandwidth=\"66810\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66810\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m78/AQOElke-XjvO2ixFipAMNby9AqC5CZmOcY8PcbQDmAwEGdrdvbD58TPi5A5RKS7WbXpTrVlZQip3DhNxjBI2vRela2S063MA11oc5y0.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=XLhOSrzrzoUQ7kNvwFqmIWd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3QuePP38pCPYCVUhnWxXEQm_39JzM2NFnZSViC_SJvZA&amp;oe=69D8589E</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 60727,
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
          "original_media_id": 3870025531093850440,
          "progressive_download_url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m69/AQPYF2mAhRbYzYMrI560MWB9XBJqAACyr7szcVbj1WFwaneaOm5BlFHWUM37z1AaOh6Oyo4BIq6T2yeHyTeibfXn.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=wTkgipWqtN0Q7kNvwEgGFwO&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2S3CbhbVxvFB6z3lMOPy3WmpnhL-h_Y_j0JTG8AAjZyA&oe=69DC5663",
          "should_mute_audio": false,
          "time_created": 1775566809,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "1029649300",
            "pk": 1029649300,
            "pk_id": "1029649300",
            "id": "1029649300",
            "username": "natgeoanimals",
            "full_name": "National Geographic Animals",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865698702530758137_1029649300",
            "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=ic5ODsLE2O8Q7kNvwE4irrr&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af1xmPrOOqpPmS1hb5QYIn2V-L58FGA0IJbhP-34YaL7ow&oe=69DC588C&_nc_sid=c024bc"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663876\" FBManifestIdentifier=\"Fojss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxs71ud+73IoDiqC0wu3LjwPImKTi/7u7BL6Zk9OwssAE/t+w5JmOxQSSmNLH6cjSBerci73BkuQFmJ6qw8jLyAaQj4fa8c2pB8T5kOjGrLcHhqCP7Nm3vAeqnN3Z9IWhDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.1\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"868003729587559v\" bandwidth=\"178266\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1353206\" FBPlaybackResolutionMos=\"0:100,360:56.7,480:54.4,720:53.2,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.1,720:83.8,1080:76.2\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOsCsgfDrcn7Gsyqj04T425mPWmeq8-MeX07h5wqKf_ykgUXeoigrvG2JQeRp4Wd_MdM-ZLa9ORl60gPpY3e_JZiFGCQ5EL6KkXMnk.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=Uh48tAtlw1sQ7kNvwHFkci2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTc4MjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0d3gxmkfV9GfhjcVlC07zKEBeUlJqdEU1atMre-pACdw&amp;oe=69DC51D7</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10892\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-78531\" FBFirstSegmentRange=\"1014-106281\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106282-221200\" FBPrefetchSegmentRange=\"1014-106281\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2092036534705762v\" bandwidth=\"240856\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1828322\" FBPlaybackResolutionMos=\"0:100,360:63.6,480:60.6,720:58.1,1080:58.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95,480:93.1,720:88.4,1080:81.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQPRuSajZ_hFnjDpVSn1TY6XCtP7Zo9QzDsXmaKDU4mXL33dQv9cZzKhXl7Y_oeRcW9BNsObRl_FpdyfkSlu8ArGYU5-l43-uxy7_sg.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=-0z8YeyvyDgQ7kNvwGpUIZf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjQwODU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0K-BNZ-h7nVhxQyJS1iQMOJIFjp1NBin5OCioS-GQkZw&amp;oe=69DC6448</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-12646\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-105375\" FBFirstSegmentRange=\"1014-143432\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"143433-293318\" FBPrefetchSegmentRange=\"1014-143432\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1267502918297183v\" bandwidth=\"326220\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2476312\" FBPlaybackResolutionMos=\"0:100,360:69,480:66,720:63.5,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.4,480:95.3,720:93.4,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBZheSdr-Op1k9B7pYwuciRaL5RCC2XcBVLkVwDPXAKrAhlrALgBooKgZk6nCMZz5AvNoGknQE18-kCW9-RNH_qVgCyawe5etIWbE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=4ClMe01ofx0Q7kNvwFndbnU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzI2MjIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2agugScwDkYr6xEUfSPlHRYmYp9BBNFHmjwMfeNQeGzg&amp;oe=69DC57D8</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-15483\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-142126\" FBFirstSegmentRange=\"1014-195190\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"195191-393663\" FBPrefetchSegmentRange=\"1014-195190\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1277876490344447v\" bandwidth=\"409602\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3109259\" FBPlaybackResolutionMos=\"0:100,360:73,480:69.8,720:67,1080:65.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.7,720:95.4,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxkQrl5cFyNncjOUGRq3XWMGmEnR7xzXjtdkfQlw0oreW4eSXmKA9eBGchHF9ByGL1ldZ-V_-LDFLMXxx4oytbIqVxuBwnRf-_tR0.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=5YrnOUUJMr4Q7kNvwHD2VKD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDA5NjAyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1_ds1uKY8U9T2wIOIf0IeKLY14GAC7NuiJJjzPPETLMw&amp;oe=69DC3457</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16985\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-176185\" FBFirstSegmentRange=\"1014-244141\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"244142-487399\" FBPrefetchSegmentRange=\"1014-244141\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1848477759129484v\" bandwidth=\"540603\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4103680\" FBPlaybackResolutionMos=\"0:100,360:77,480:74,720:70.7,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.24,480:98,720:97.4,1080:93.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP2bW0aIfz99a4ARx2Q2fPwwUvSZlmUT1jxqzlfSPxqDy_XKQdY1A9deJRHs78I9y2z_ngWT2zfhDIKZ8-XZxBrQWFF9SDm2muWNnE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=M35pMpEQ64sQ7kNvwGFj0mk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NTQwNjAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2FVn_ruR37iw-vF3nxiRNcwXWCYKp67lxvrhszlxjXaw&amp;oe=69DC4906</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-18644\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-229855\" FBFirstSegmentRange=\"1014-321368\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"321369-630140\" FBPrefetchSegmentRange=\"1014-321368\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1588945909073417v\" bandwidth=\"681362\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"5172172\" FBPlaybackResolutionMos=\"0:100,360:80.4,480:76.6,720:73.2,1080:70.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.62,480:98.37,720:98.59,1080:95.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPuKZF2qKICjs08-k_G1H8gucF1aCSpWB6stiwUGXWNvKfX5Hm_pNaY4z6GYTR0ZmsxXCYFw3SGDP8cejuR9yWwzxdzv-J159SieXo.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=jd4D7ZlmtxMQ7kNvwEnCzRi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjgxMzYyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0onlhWe2b4CLVPi_vpH646E1A9E4oFT4c-EUElRMPy3w&amp;oe=69DC4007</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-20592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-288895\" FBFirstSegmentRange=\"1014-405533\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"405534-781198\" FBPrefetchSegmentRange=\"1014-405533\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2061822901412808v\" bandwidth=\"912497\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6926702\" FBPlaybackResolutionMos=\"0:100,360:83.9,480:79.9,720:75.7,1080:72.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.077,480:98.93,720:99.306,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOjiwsO48rCaOF6m6s4bgg66iRhLGj5CKjR4DDmQ8T9kE2SvEWALkKtR50Wk2wGAMLc1Ws3pNhZSA9Y-QIiggu_wdfx_Bl0gwfgXDQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=fEsXwzzt-3AQ7kNvwHJ9lHG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6OTEyNDk3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3XqHpLpyeCQm0V6LAjOoYRGFrH3IWeuPmW52UilD6CVw&amp;oe=69DC387A</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-23580\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-385865\" FBFirstSegmentRange=\"1014-544870\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"544871-1019514\" FBPrefetchSegmentRange=\"1014-544870\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1627595234965301v\" bandwidth=\"1235000\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"9374797\" FBPlaybackResolutionMos=\"0:100,360:86.4,480:82.8,720:77.8,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.386,480:99.342,720:99.569,1080:99.632\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQM_p3Fq6rDYprSjJ8-MUlNGuff4JfkbCcT-LYH34W9o85XM1tWSkDeCFiP_sdVayBjAG_vXE0vYkHj0noxXvuN1eESyaLJtPOQ3Rmg.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=YK0MlTWtfdIQ7kNvwGD3h6k&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTIzNTAwMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0uX3DK3MjGnC6vhUmKOPwIR_nyfT4e5nnuY_HhoH4NNw&amp;oe=69DC4156</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-32211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-518374\" FBFirstSegmentRange=\"1014-739833\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"739834-1405190\" FBPrefetchSegmentRange=\"1014-739833\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4294793980782357a\" bandwidth=\"46380\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46380\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"353137\" FBPaqMos=\"87.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQN9GI-VauacxM2tCfwmiCOijhyH33zBWrM0Dr4JwD6i2FjABcTvvBGOXIydEyGVXVx6wkUjNuDAtapI93ufxCNL1tRZuAP-HRtBv50.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=Uo8ixeKIRUsQ7kNvwErssVb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjUxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1IOlF7xDMlp4hMUyg_MeRAbdNWQqlU_VwMdkKPi56sJQ&amp;oe=69DC60EA</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2136\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-14938\" FBFirstSegmentRange=\"1025-28400\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28401-56361\" FBPrefetchSegmentRange=\"1025-28400\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1256673039910436a\" bandwidth=\"74812\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74812\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"568992\" FBPaqMos=\"89.65\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPA0IU4X5qD93OmmaSc1st7oueEaOmYwYCBhH3T3wOKN7WutkRMOZ1TDwC1ugFmlc5yKEeuM_xeo_vD4IzH2AbUDhA7xa2uuL_kti8.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=H10A9jvUydQQ7kNvwHmsarO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NDk0NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0x_AoUTJc7AF-j3ADLAf_74Br5_qnlG2aUjm5trR_uQQ&amp;oe=69DC6622</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21486\" FBFirstSegmentRange=\"1026-43481\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"43482-90615\" FBPrefetchSegmentRange=\"1026-43481\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"878713468520453a\" bandwidth=\"108352\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108352\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"823623\" FBPaqMos=\"83.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOhb37d5jmr5MvSl8eT28PWBputzk-lecQ-RBUBedLEv96EozZbcoK_AR-dP3eFTj3ZDuOnoWe6DiibSbh3Vjc_rcGupQpI3Z2uCnA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=qIB9a-mC_CIQ7kNvwGWJ4Dp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDg0ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0-11_gPJDCqQmUinY-D8_aCZ1spowrkppTlouAMsmNnA&amp;oe=69DC55C7</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2395\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-30757\" FBFirstSegmentRange=\"1021-62738\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62739-132935\" FBPrefetchSegmentRange=\"1021-62738\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2103223183861763a\" bandwidth=\"143947\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"143947\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1093864\" FBPaqMos=\"87.00\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOgH1TOj2U7Ucn9wQoBfkebTHLZ9A_EoIFXsEJ2CkC1MsQUoWoasexRt0uwJQMyHQr8MmjxA15OisXxvCobhDmp05SCyaFAKp2_vFI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=Kg8UNuEeTkcQ7kNvwHuDH1n&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxNDQwODEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af14rxkPJKo3VaYIrxXzSlXdjLvReEV41LcKktl1K3U-Lw&amp;oe=69DC5327</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-45040\" FBFirstSegmentRange=\"1021-86500\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"86501-176000\" FBPrefetchSegmentRange=\"1021-86500\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1_UAVWfD7LIMqNL8JCI2zn-G8XQUq1PZstP-8odjCXPQ&oe=69DC51E9&_nc_sid=c024bc",
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
    },
    {
      "pk": "3869494020385423326",
      "id": "3869494020385423326_787132",
      "code": "DWzNE9hkj_e",
      "taken_at": "2026-04-06T19:00:16Z",
      "taken_at_ts": 1775502016,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-atl3-2.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwGQn0cN&_nc_oc=AdrDJR244YVUPq5qHZcNdDP6wJcyQuwiqZR2wybQZ-US1jjq0dTHbQpIdrudE1aDqew&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&oh=00_Af1tuKMIDRk2jG7bBjtulRA5_4hui_PHIeaql3g61qRfAA&oe=69DC6315",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1_UAVWfD7LIMqNL8JCI2zn-G8XQUq1PZstP-8odjCXPQ&oe=69DC51E9&_nc_sid=c024bc",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 65,
      "comments_disabled": false,
      "like_count": 11121,
      "play_count": 1488984,
      "has_liked": false,
      "caption_text": "In Hoppers, Piper Curda’s character Mabel explored her sense of wonder for the natural world with the help of hopping technology. For now, we still have to do it the old-fashioned way.\n\nSee Disney and Pixar’s new movie Hoppers, now playing, only in theaters, and step into wonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHzva65&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0BSBFVOvbLN1ZgK3UzPQfS3_Mhh7qav29M3pvNNY-cog&oe=69D86DB8",
      "view_count": 0,
      "video_duration": 55.44499969482422,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            13479,
            26958,
            40438
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-atl3-2.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwGQn0cN&_nc_oc=AdrDJR244YVUPq5qHZcNdDP6wJcyQuwiqZR2wybQZ-US1jjq0dTHbQpIdrudE1aDqew&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&oh=00_Af1tuKMIDRk2jG7bBjtulRA5_4hui_PHIeaql3g61qRfAA&oe=69DC6315",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1113315,
          "height": 1280,
          "id": "2358585431274531v",
          "type": 101,
          "url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHzva65&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0BSBFVOvbLN1ZgK3UzPQfS3_Mhh7qav29M3pvNNY-cog&oe=69D86DB8",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1113315,
          "height": 1280,
          "id": "2358585431274531v",
          "type": 102,
          "url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHzva65&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0BSBFVOvbLN1ZgK3UzPQfS3_Mhh7qav29M3pvNNY-cog&oe=69D86DB8",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1113315,
          "height": 1280,
          "id": "2358585431274531v",
          "type": 103,
          "url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwHzva65&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0BSBFVOvbLN1ZgK3UzPQfS3_Mhh7qav29M3pvNNY-cog&oe=69D86DB8",
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
          "best_audio_cluster_id": "2426975461070348"
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
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18606311365032744",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26295324880076257,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": true,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775663876\" FBManifestIdentifier=\"Fojss50NKRbEl5Tt0tWmAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"929459223037410a\" bandwidth=\"60820\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"60820\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m78/AQN38tw9LWdIk_CWlJ0ze2Ayn07LgXtA4TMaLXc-6SODK58HBqKnlOKk8_LTSIHFsE3VGUlntYj8FPrehpb5VftWJE3s0U_LvQcQ0p4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=ZHLfVpYSwAwQ7kNvwGN0EB8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo2MDk5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0ceGcffoHFiEwAO2KNe0WKkreY8mRwKAwhTFUWDL-H4A&amp;oe=69D865B3</BaseURL><SegmentBase indexRange=\"824-1191\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 55430,
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
          "original_media_id": 3869494020385423326,
          "progressive_download_url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKBMTmsUUaSlY28FrQeX4c4T6dijF6gtmaEyTFBN6pFY5bZ5DsQbcUjfr7pEffSR4eVHh1ugsHyMjH1cbkv8Kz.mp4?strext=1&_nc_cat=106&_nc_sid=8bf8fe&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=VR1-k3frXTsQ7kNvwHP1XVZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3rrjKaKE6G3hFRP_MZA3iEsBrILhSiVjAKjVpHx94w3A&oe=69DC53CC",
          "should_mute_audio": false,
          "time_created": 1775502020,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1_UAVWfD7LIMqNL8JCI2zn-G8XQUq1PZstP-8odjCXPQ&oe=69DC51E9&_nc_sid=c024bc"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775663876\" FBManifestIdentifier=\"Fojss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxtbm7f2IgpUD7OHlgsygpwOI9qGs6c69A4K35IPMyMEDsI3CoKTHvgSc252C4sXBBPyF6YussKgF9KKOwMXurwXYlsvU5LXeBdjS1K7XuegF6PTG0/GH9wW+g9vN5+3SByIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:73.2\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"890639983950251v\" bandwidth=\"148183\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1026735\" FBPlaybackResolutionMos=\"0:100,360:77,480:75.4,720:74.2,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:93.1,720:92.5,1080:88.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxVTdb31AW_INujP1IDvNHV263--MPtveeFNN3GUuUVYCWKFeS7YZ9ZN2G12w1BpIi_FdawNocSzgpCnZ_RmsvfPjiy1uTBHb9oZw.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=Azv6S-cYlSkQ7kNvwEKgGzW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTQ4MTgzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1WcuuL_pVt04jfX5gu_X7X_9ARSPxkwDUjWvgC0mR0Eg&amp;oe=69DC684E</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-11627\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-38956\" FBFirstSegmentRange=\"1002-59102\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"59103-123876\" FBPrefetchSegmentRange=\"1002-59102\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1496166365471102v\" bandwidth=\"217161\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1504667\" FBPlaybackResolutionMos=\"0:100,360:81.6,480:79.3,720:77.4,1080:76.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:95.5,720:95.4,1080:91.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP0yhiq2c2nWFCoYYsXHyN0n4pQ1H3Bf1PillRJPvA7F7s4T2vZEWWlnN1ab7wlhBx2qkPUdSqWmZq9YiCbgQr1iy6TnVK92GJFM7E.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=-GnWOEbhFFMQ7kNvwFbz6FU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MjE3MTYxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1RyQFa9dIam3YdnuyKNptPsZPle49Fcc0pAORTdEpoXA&amp;oe=69DC5F5A</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-15046\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-52809\" FBFirstSegmentRange=\"1002-81554\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"81555-172554\" FBPrefetchSegmentRange=\"1002-81554\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1637064280544428v\" bandwidth=\"297468\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2061099\" FBPlaybackResolutionMos=\"0:100,360:85.4,480:83.2,720:81,1080:79.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.5,480:97.1,720:97.8,1080:94\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNmpoeNdw7yb2DNMihh-Q2G15Y477O-Sk1OLg5Yvc1SF5s2DvEEWcyZxNMIPHB9gTiEJuesLauW023efqZ9CuKWYNgVahVJF3UIkRc.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=DWIM7dIPpcYQ7kNvwH6Q_9U&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mjk3NDY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af05X2ZJdaMoXBxDwAqiey2Y8kFJsgNzGNgZbcq5-kXrBA&amp;oe=69DC3FEE</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-18788\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-68106\" FBFirstSegmentRange=\"1002-106801\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106802-227120\" FBPrefetchSegmentRange=\"1002-106801\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"930746796390518v\" bandwidth=\"386132\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2675439\" FBPlaybackResolutionMos=\"0:100,360:87.4,480:85.4,720:83.2,1080:81\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.11,480:98,720:98.9,1080:95.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOqmazZV0GgC-FMAgX5Uo4Hzr4dpsUwPLWUSkWVzIH2EIopdalxgjleoQbUfcUfP1apdP-4Gsa_iSGhTS3l313F1z6FbA8TyS6K2AY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=XpZ2XTBJDXAQ7kNvwFNbP3o&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mzg2MTMyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0OLSoLqh1oYRl7OryK4Uu-4tiIi90roVQOov_zaf2JSA&amp;oe=69DC5F0C</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-22235\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-83355\" FBFirstSegmentRange=\"1002-132950\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"132951-285253\" FBPrefetchSegmentRange=\"1002-132950\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1263463985333080v\" bandwidth=\"479911\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3325212\" FBPlaybackResolutionMos=\"0:100,360:88.9,480:86.9,720:84.7,1080:82.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.46,480:98.4,720:99.414,1080:96.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQN5Sl_4u8bg21xVtk-cIUfm9Z6DIbmrVvFA9a9N55F9NWJNHo03righvcgXtgSk_3JVH4wvKy4OTeNsgcwEtoacof_IARGxdKkAT-A.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=P7dFgXaWfIwQ7kNvwGUmUEN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NDc5OTExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1V_44Inw7x_A-c-xKkDt6kwV_xRglUf1VNC4Hg9i99rA&amp;oe=69DC5DE8</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-26049\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-100642\" FBFirstSegmentRange=\"1002-162120\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"162121-346006\" FBPrefetchSegmentRange=\"1002-162120\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1669194164264244v\" bandwidth=\"600336\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4159614\" FBPlaybackResolutionMos=\"0:100,360:90.2,480:88.2,720:86,1080:83.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.75,480:98.79,720:99.619,1080:97.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOkSM-p5C4-U6nKoTCQGR9QEo9t8_5IVg-ngkZWi13nRqVLUyRlAs1Es-YozyB9s8bjtNsK18hWCL1Of88sI3ZDe_gO2S45lP4yjWI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=8zqHITencNwQ7kNvwFBNFCh&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NjAwMzM2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0JYgXPLeBc1XnRcILOGe6rXChWwset580E6Ajwiz6qfg&amp;oe=69DC3AC3</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-30771\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-121891\" FBFirstSegmentRange=\"1002-198284\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"198285-422683\" FBPrefetchSegmentRange=\"1002-198284\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"988608596839873v\" bandwidth=\"797098\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"5522936\" FBPlaybackResolutionMos=\"0:100,360:91.3,480:89.4,720:87.2,1080:84.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.026,480:99.172,720:99.732,1080:97.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMf3Rx8OOzEgPrCPNBR-0Nt-fwNaR6LdwmdWPUwzv4ulTwm_6h2bijtJ5Bjd87z0Jr-dXFj9FkGKtlRGWG6WeJW59Fiu3efb5LsrRI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=B11mdo9l0D0Q7kNvwHvo58e&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Nzk3MDk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3_oq9dxD7ZVWFxIZf2vKFOy0qAVILObR1KUhefyv41Dg&amp;oe=69DC4992</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-37057\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-156105\" FBFirstSegmentRange=\"1002-256214\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"256215-544176\" FBPrefetchSegmentRange=\"1002-256214\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2152531255582943v\" bandwidth=\"1154217\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"7997347\" FBPlaybackResolutionMos=\"0:100,360:92.4,480:90.7,720:88.4,1080:87\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.557,480:99.564,720:99.814,1080:99.824\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNSJdZpIRgVNqEBZdYq3cRarDru00HEWTghNg_iisXPQJn1ZojfEEAKYKMxJ1XCUfUglkRb6_gx6l6OzyKpZWsTXEQRU05M7RCeihQ.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=K8EwAJQ3wUIQ7kNvwGKTzMc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTE1NDIxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1kFV_9Dnud7i9qrY6bHBcxL3qr7Pvs9ZHWGlGcv-rYNQ&amp;oe=69DC40FD</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-50470\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-211892\" FBFirstSegmentRange=\"1002-345895\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"345896-752596\" FBPrefetchSegmentRange=\"1002-345895\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1615007113110956a\" bandwidth=\"45829\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45829\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"318635\" FBPaqMos=\"90.73\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOq8zAQzpeRCoSQuovKRKQeNbycFlDBjsuggCgJzVUNsydkP6wpqSMV87VACc6egwIxdyoZ9qyuATjsxvSkWgWUtLCaKeDUW5vI2l0.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=n8c3OFNcOe4Q7kNvwH5EFOP&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo0NTk3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1zWOQSroLceq7s7FuMq7HlrqnuOvSBEnEuHywlZtN8fw&amp;oe=69DC5B70</BaseURL><SegmentBase indexRange=\"837-1012\" timescale=\"48000\" FBMinimumPrefetchRange=\"1013-2182\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1013-15598\" FBFirstSegmentRange=\"1013-28913\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28914-57244\" FBPrefetchSegmentRange=\"1013-28913\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1270034985105102a\" bandwidth=\"72011\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"72011\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"500096\" FBPaqMos=\"90.72\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNETgTPe23OWiy-KGFj4O0xaNmi9xW8k8We4jlz_Lesh43O4RfyZWEg4kgQ77avCmAh4dhCO9ERkZrtXpEBa1nLDn-iaNXSGANeubo.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=wOOs-JEmecsQ7kNvwGZt_QL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo3MjE1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2SvpHZdk5yLz32Qn1Up5bikdPaGBMskBbu8NPT1H5JOQ&amp;oe=69DC5EFF</BaseURL><SegmentBase indexRange=\"838-1013\" timescale=\"48000\" FBMinimumPrefetchRange=\"1014-2538\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-26077\" FBFirstSegmentRange=\"1014-48598\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48599-97300\" FBPrefetchSegmentRange=\"1014-48598\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"979919517793668a\" bandwidth=\"103761\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"103761\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"720138\" FBPaqMos=\"88.08\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNOpf9BEo2_A4jYtakOEtpNQQZDYD9C0aIFAN-Q6y8Ina7CtFSkF_92RvlAvk1DGfzRoyEa6eCluUBrw77Kir2QY9JUObENLk8IZsE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=sGdWzzK2ve0Q7kNvwFl0Vuv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMDM5MDYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1zZr_aY12Ooy4oMRMjRiFHgfCu8IxQHy51u9BHiARMmA&amp;oe=69DC564E</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2467\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-36815\" FBFirstSegmentRange=\"1009-70144\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"70145-139522\" FBPrefetchSegmentRange=\"1009-70144\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1512628090423482a\" bandwidth=\"134031\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"134031\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"929932\" FBPaqMos=\"90.49\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMDkCHmLVEnsU6T5_aC7ZlGvMakuRW1O3OnJZfxZuCHE1fs0cf1weWXn_tPspjek6E1p7CHcVLpGZLRSFGGTuIaxYNUE1SlwG3YTc4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=sKJdfZK9eLkQ7kNvwET1vJU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMzQxNzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1hyKWZIStFcS-CQKa6hRccO21UdRyYQgGehH8hh1tv7A&amp;oe=69DC5209</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2532\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-44659\" FBFirstSegmentRange=\"1009-85613\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85614-170092\" FBPrefetchSegmentRange=\"1009-85613\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "284634753",
          "pk": 284634753,
          "pk_id": "284634753",
          "id": "284634753",
          "username": "pixar",
          "full_name": "Pixar",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3715495057937025462_284634753",
          "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/543579175_18522017512026754_6429363176312325029_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzQuYzIifQ&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=v0quYpmBS-oQ7kNvwE_0JJP&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GCdcZiCC8lNCrc1BAKXDEqC_rzlZbmNDAQAB1501500j-ccb7-5&oh=00_Af1Lk9pw7rUxafk2ksOfsb1EcbuhpuyH7P0L3VkM8An10g&oe=69DC4FB3&_nc_sid=c024bc",
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
          "strong_id__": "18091046",
          "pk": 18091046,
          "pk_id": "18091046",
          "id": "18091046",
          "username": "natgeotv",
          "full_name": "National Geographic TV",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865691934048399589_18091046",
          "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=zov5ST0QeW4Q7kNvwHRijig&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af2BtlTIrikE_Q93U4B9XkTIRCHrq1YWpmJsTfoNRBne0g&oe=69DC4D93&_nc_sid=c024bc",
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
    },
    {
      "pk": "3868170261056492782",
      "id": "3868170261056492782_787132",
      "code": "DWugFulAJTu",
      "taken_at": "2026-04-05T16:00:10Z",
      "taken_at_ts": 1775404810,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-atl3-3.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwHedkoS&_nc_oc=AdraZKNOXKDsJRTUpQAjcwwsXqvYeo33zXEi5kxDwyM-Qy0LKZ4QEH2G7zDKbfcR6X4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&oh=00_Af03Tr-UIdwJ5KxMsanSuxZ_ViPrbTsZR3g-4BYJLTqRLA&oe=69DC4951",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1_UAVWfD7LIMqNL8JCI2zn-G8XQUq1PZstP-8odjCXPQ&oe=69DC51E9&_nc_sid=c024bc",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 78,
      "comments_disabled": false,
      "like_count": 7479,
      "play_count": 1304804,
      "has_liked": false,
      "caption_text": "Spotted hyenas are a powerful example of the resilience and strength found in nature. For wildlife ecologist, conservation scientist, and National Geographic Explorer Dr. Christine Wilkinson (@christine_eleanor), these reminders are what wonder is all about. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwE-VILf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vxD9xX1D9D_bqPFc4OMr8epGyGA3uLAUbScxUYkM7-w&oe=69D87233",
      "view_count": 0,
      "video_duration": 47.893001556396484,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            18831,
            37662,
            56494
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-atl3-3.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwHedkoS&_nc_oc=AdraZKNOXKDsJRTUpQAjcwwsXqvYeo33zXEi5kxDwyM-Qy0LKZ4QEH2G7zDKbfcR6X4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&oh=00_Af03Tr-UIdwJ5KxMsanSuxZ_ViPrbTsZR3g-4BYJLTqRLA&oe=69DC4951",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1064730,
          "height": 1280,
          "id": "799234956583164v",
          "type": 101,
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwE-VILf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vxD9xX1D9D_bqPFc4OMr8epGyGA3uLAUbScxUYkM7-w&oe=69D87233",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1064730,
          "height": 1280,
          "id": "799234956583164v",
          "type": 102,
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwE-VILf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vxD9xX1D9D_bqPFc4OMr8epGyGA3uLAUbScxUYkM7-w&oe=69D87233",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1064730,
          "height": 1280,
          "id": "799234956583164v",
          "type": 103,
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwE-VILf&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vxD9xX1D9D_bqPFc4OMr8epGyGA3uLAUbScxUYkM7-w&oe=69D87233",
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
          "best_audio_cluster_id": "919303480943593"
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
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18439666597118965",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26074550038833869,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": true,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBManifestTimestamp=\"1775663876\" FBManifestIdentifier=\"Fojss50NKRa4sr3lnNynAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"931771249568924a\" bandwidth=\"66894\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66894\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m78/AQObEBSySE0AGNBbG4lxf162Q155i5gTcG0OizHqB4rRxcGyySZDjummT0z9r1wsiCbVlaRrtWqIqFWzQVPE7UxmQ1lTMC4PQzMnv0M.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=8_2Uu26HoJkQ7kNvwHXIqW5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo2NzA4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af20AWzlHN3AqeELi0tPfT--tdPakSm1i0g21QlVokxJ2w&amp;oe=69D86E19</BaseURL><SegmentBase indexRange=\"824-1143\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 47881,
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
          "original_media_id": 3868170261056492782,
          "progressive_download_url": "https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m69/AQNsTvlWrX5b5jAnAagr-VEkXvHgjuh1R7UtSI3qunavCZFTpObST3AI8L-cDc_wZTw8bAKRL2XuixVvoM6ISAHt.mp4?strext=1&_nc_cat=100&_nc_sid=8bf8fe&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_ohc=TbFtdnyPN3QQ7kNvwHuIWaM&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0W4Uq2ZI0A8KsIcAfNBnXNI8P2KzP6rsmXz8P7HfBskQ&oe=69DC4132",
          "should_mute_audio": false,
          "time_created": 1775404814,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=XbeNvhLXv28Q7kNvwFNEOGq&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1_UAVWfD7LIMqNL8JCI2zn-G8XQUq1PZstP-8odjCXPQ&oe=69DC51E9&_nc_sid=c024bc"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBManifestTimestamp=\"1775663876\" FBManifestIdentifier=\"Fojss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxqbV6aDR+bYDqvaKk6SpqgT+7OaL4NTBBNj9mrKQtbMFjO6L353LugW8goKl5dy6BYLQssb/qogGmPbggPvSlAbwr/bX4oT0BoSVlbCehoIHqrXuq+uJnQfYts6QtoSsWyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWBhQAEhQCAA==\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1536512375144606v\" bandwidth=\"125041\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"748393\" FBPlaybackResolutionMos=\"0:100,360:68.6,480:63.5,720:57.2,1080:52.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.7,480:90.2,720:86.7,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOC-37dngJq90Dyy1_JazUnnPGdWCHskETHnxkRIIJCSOlZF1fVQ-6mAFGNhj2z93WeeIs714OUklQmfut9nIzTnVBICEHS1YfCoAw.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=e25xSTehHgsQ7kNvwEHAHiy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTI1MDQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Gf6y7AKqjAHv1bUFho-NtJBLsp5_OMGMb3HZx8AW3Sw&amp;oe=69DC5053</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-11379\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-53195\" FBFirstSegmentRange=\"978-73681\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"73682-177801\" FBPrefetchSegmentRange=\"978-73681\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1707180720280577v\" bandwidth=\"268984\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1609913\" FBPlaybackResolutionMos=\"0:100,360:82.1,480:77.4,720:72,1080:65\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:96,720:94.9,1080:90.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOoI_Qc5Hb567q3s03DZ7hurU3EPc934bMb3FmMMVaHXDUYxsb4QiUQt8F8TcKitfPDLHzHey1wENKGp-vSnIF1hHoyzJ4LrrK2kjM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=ajpqDB5imFoQ7kNvwEM8hD6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MjY4OTg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2nwCgf7hFaaIONERdFUIAxfCq3i8DrKA4ipNJ7C8eklg&amp;oe=69DC64EB</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-19527\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-105884\" FBFirstSegmentRange=\"978-157985\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"157986-375189\" FBPrefetchSegmentRange=\"978-157985\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1944018522917880v\" bandwidth=\"368764\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2207110\" FBPlaybackResolutionMos=\"0:100,360:85.9,480:81.7,720:75.8,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.04,480:97.6,720:97.2,1080:93.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQM3ITI-kIVflLXqBQCMcqSKriqhB8j74oqGUj6f3pYWDnqOC18MUJJNe0oZbKf0kPXddx31PP3oAzTIyNssN5V0g7YFH89E5A-Ij6s.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=Mwx1ng6pC6sQ7kNvwE7PUXT&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MzY4NzY0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3S5qdo_8yew8q0YI6K4eFH3j_dLoFmG12PJNK33hHVgw&amp;oe=69DC662F</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-24075\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-141715\" FBFirstSegmentRange=\"978-216596\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"216597-512096\" FBPrefetchSegmentRange=\"978-216596\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1218968110062997v\" bandwidth=\"442503\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2648452\" FBPlaybackResolutionMos=\"0:100,360:87.7,480:83.8,720:77.5,1080:70.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.61,480:98.35,720:98.31,1080:95.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOYTMwguxNmYzts7ztqP3uq8QYqnySSAGvKGU84jFkz30lRwgwLYRu68NUaE4CuVcCCkccg0gJEpbQIdwnc6OfTFFkYbjN5LqbfVG4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=KFTAZdhAk40Q7kNvwENcFjJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NDQyNTAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2q1EvL5KzFet5VNgQ8gPNC6lXEC0RWa-B7xkRpWU5W0Q&amp;oe=69DC56A1</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-27189\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-169993\" FBFirstSegmentRange=\"978-261689\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"261690-617097\" FBPrefetchSegmentRange=\"978-261689\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1734255584222604v\" bandwidth=\"593051\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3549501\" FBPlaybackResolutionMos=\"0:100,360:89.9,480:86.3,720:80.5,1080:72.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99,480:98.97,720:99.193,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQN9lx9WGs0aObQ1f5j5Tn6y1xVQXR-Dwub7W_SxmroZb4LDoDVxPW13tmY1vHIkgBkSqIxvS44m4qTOlQHuogzz-fjvXsOFNStGw5o.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=IG_0Np9TPzEQ7kNvwEO1CG5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NTkzMDUxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3D14sGUqcnnw52-m-MnXfTaRouG-S7g0a8j57BGXy1Ig&amp;oe=69DC5BBE</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-32309\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-227501\" FBFirstSegmentRange=\"978-353323\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"353324-811886\" FBPrefetchSegmentRange=\"978-353323\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1974830039737666v\" bandwidth=\"808049\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4836297\" FBPlaybackResolutionMos=\"0:100,360:91.5,480:88.1,720:82.7,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.177,480:99.289,720:99.419,1080:98.77\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNxzz3B_d6VnnNmwILSsdhY1b8WYAyEq1nGyoBddc0-zErqxX-3eoxHWRJoRjzW8rt7CPCOSi7aXg9mJJvD7MDk23Y4mXgSrDlMMp0.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=1oWA7fT-WaIQ7kNvwGVxm3E&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6ODA4MDQ5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af169pR7Ouk2G-1vSgMdxDw-jVcxu8XUeqCvMXSexCwS3w&amp;oe=69DC3E3B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-37690\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-306742\" FBFirstSegmentRange=\"978-478293\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"478294-1073273\" FBPrefetchSegmentRange=\"978-478293\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2034265537498453v\" bandwidth=\"1150676\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6886972\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:89.4,720:84.3,1080:75.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.316,480:99.475,720:99.604,1080:99.184\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO8nzMmBULFzOq0Uc221nMlzpRXdUpXzRan5dqj-VDzxkIrtzc1nz0dI1BX50zPIMwgzzgD9a0zuNNVJoHjAR_qboR3srHbCUwAf98.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=AJfwxCErVuwQ7kNvwF0v6fB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTE1MDY3NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3f3zQxp3PcAslu7x9AJIidv7vLc_LteXUb93L0xkMskw&amp;oe=69DC467B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-42521\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-414721\" FBFirstSegmentRange=\"978-651076\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"651077-1467135\" FBPrefetchSegmentRange=\"978-651076\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"965261856159059v\" bandwidth=\"1802418\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"10787749\" FBPlaybackResolutionMos=\"0:100,360:93.6,480:91,720:86.4,1080:81.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.439,480:99.57,720:99.699,1080:99.627\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNl6wEb07Ks3JIhuPO2wCPZMvypoiru-vDavX2ZbnVx8EmjXzlq5vNBYsVwM0MoQtRL7pguuPZmXv_tnRPUIgRfIL00yZnEyV3zjZQ.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=WeUmuiwzlkoQ7kNvwG_HHI6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTgwMjQxOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1sDSHSffiuZeSMKNiEi5BHchDkqEwg6Ds3WYFKWnpWcQ&amp;oe=69DC591C</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-62167\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-590586\" FBFirstSegmentRange=\"978-956290\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"956291-2465586\" FBPrefetchSegmentRange=\"978-956290\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"25711055888567724a\" bandwidth=\"43137\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"43137\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"259233\" FBPaqMos=\"86.23\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPwGwzN_jZWTG5g53W6HPaq6prVW3aFxZFUMoApdF5Bb07alTzINwfJIHhTt2__EB0B73uktjzHCPmfysFRIfXNu5jyUMQk7HQ2MAA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=D8aq4uZD0HoQ7kNvwGo8Upa&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo0MzMwMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af27VQWhGY_-_BO8tr-wMB5zHoGcjWwQWjQx-F5rkR2GVA&amp;oe=69DC3521</BaseURL><SegmentBase indexRange=\"837-988\" timescale=\"48000\" FBMinimumPrefetchRange=\"989-2211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"989-15011\" FBFirstSegmentRange=\"989-27427\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27428-53863\" FBPrefetchSegmentRange=\"989-27427\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1520437802786668a\" bandwidth=\"71500\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71500\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"429033\" FBPaqMos=\"87.36\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQM1qgyiYipO3nTb3Q4w_ENJZ3IxJuj0VPo2tuNaBczlM_oHVqwMkDYBW3T0y1773ATnvblNT7r_xf3TsujSnPIypzOSKbCvToAOuws.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=hwhUj3NemRQQ7kNvwE6ILqw&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo3MTY2NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2qAEL5oG0nxmr0b6bdJc3VZmEeqGo3srNuOk8_iKd5yQ&amp;oe=69DC4C06</BaseURL><SegmentBase indexRange=\"838-989\" timescale=\"48000\" FBMinimumPrefetchRange=\"990-2669\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"990-24617\" FBFirstSegmentRange=\"990-45672\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"45673-89246\" FBPrefetchSegmentRange=\"990-45672\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1270292424743743a\" bandwidth=\"104937\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"104937\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"629205\" FBPaqMos=\"81.20\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOSZPTrQoZvEzpNyz3hhbxCnafm4XAlkTPd_h7zn5N1n6R0Ga6E8UgDUI08GX-XKGcGJAxmhV-HhXGeeaJ0XyTdLAqhdbtcuwmB8ms.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=L_y6Qh90gVgQ7kNvwHbk-I-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMDUxMDEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2r7rbDR1NpkSILUadn31Ax5CAtxjScoXM7MUg68NKd-g&amp;oe=69DC5BBA</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2362\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-35155\" FBFirstSegmentRange=\"985-65716\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"65717-128980\" FBPrefetchSegmentRange=\"985-65716\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1536210714590086a\" bandwidth=\"136838\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"136838\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"820186\" FBPaqMos=\"83.96\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO7KXm8TEDvhztA9v_PIl-O0CaShP5_2iBO4ggZMBeDRGTOTXVI3umPjYEK9ju_ZrOe1b_AWcnu75HARzg6Y6KbrJQ7pMmp_w0mKfU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=itqu0TbKGQYQ7kNvwFSQq95&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMzcwMDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3IsshBvDr-APuJau-JcWC0qiK2Gf2eZVXhQnhybK_yzg&amp;oe=69DC4117</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2442\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-44989\" FBFirstSegmentRange=\"985-85365\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85366-166815\" FBPrefetchSegmentRange=\"985-85365\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "271370325",
          "pk": 271370325,
          "pk_id": "271370325",
          "id": "271370325",
          "username": "christine_eleanor",
          "full_name": "christine wilkinson, phd",
          "is_private": false,
          "is_verified": false,
          "profile_pic_id": "3245086179333885169_271370325",
          "profile_pic_url": "https://scontent-atl3-2.cdninstagram.com/v/t51.2885-19/404288054_706561544741164_8609495828476348252_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44ODguYzIifQ&_nc_ht=scontent-atl3-2.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gHgNK2cU0tLtlKq4aX_ZLD411vD6LtroopTwtwxbKXXySfOHuUJtipl5MgMf2Ep7J0&_nc_ohc=9NDLLLLwDV8Q7kNvwGuBLXu&_nc_gid=YyGPsk4iVUIoasQqtZ0Ruw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GDbyGBgs4eItnYICAFxHikfXEnt3bkULAAAB1501500j-ccb7-5&oh=00_Af21n8Nhn7dvs9nbGJt6N7Mq_2WmDnLRki6Kp-6U5YSddw&oe=69DC57AB&_nc_sid=c024bc",
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
  ],
  "QVFEbjdjZ2JRZmxmWmdxYXBSOTgwUFR1emF1OXlGM2MzWUx3WVdNb0lnbmIzMDJhcWZyMTVFcXRxRWgwOWRBNnh6VGt0Tzd1UUV4NWFSa0pGZnFPdWp1UA=="
]
```

</details>

---

### GET /v1/user/followers

Get followers users. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/followers?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/followers",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/followers?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "43374964307",
    "id": "43374964307",
    "username": "postedbynj",
    "full_name": "",
    "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658260017_18063616745444308_1491397800595950837_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gERAwuCPwXHt_2eSO-aErYhC9gTsHR-LfZ_KktavWPtseZFqy5nNAd-7V_l1GIVen4&_nc_ohc=Qs_lKy2sErgQ7kNvwHNnPD4&_nc_gid=XQA0LtRAZxraShuBXytlPA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GDFAPCfUk3iDwyxAAPUMUttlgrIUbmNDAQAB1501500j-ccb7-5&oh=00_Af19U-Cfxo1Lec2vD9HmMGHKi_rk3aDlCpn3YQ2QasSVtg&oe=69DC35EE&_nc_sid=6ff7c8",
    "is_private": false,
    "is_verified": false
  },
  {
    "pk": "69025436922",
    "id": "69025436922",
    "username": "pedroqduarte",
    "full_name": "Pedro Duarte",
    "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.2885-19/491416168_662266566416516_4619764470022606481_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MjAuYzEifQ&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gERAwuCPwXHt_2eSO-aErYhC9gTsHR-LfZ_KktavWPtseZFqy5nNAd-7V_l1GIVen4&_nc_ohc=J452D13OposQ7kNvwEFS_4r&_nc_gid=XQA0LtRAZxraShuBXytlPA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GGhqSh2EGHDzU1oCAJEOqxVPsxxAbkULAAAB1501500j-ccb7-5&oh=00_Af0jT__T2Lld0uLnigwRYiyjGOwcKIGTsYojRRn_oZr7zw&oe=69DC5FDF&_nc_sid=6ff7c8",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "35814620919",
    "id": "35814620919",
    "username": "praguosphere",
    "full_name": "PRAGUOSPHERE",
    "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/660140245_18074573600196920_3208973545650305425_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gERAwuCPwXHt_2eSO-aErYhC9gTsHR-LfZ_KktavWPtseZFqy5nNAd-7V_l1GIVen4&_nc_ohc=N0ogvpr6pBAQ7kNvwEChzKH&_nc_gid=XQA0LtRAZxraShuBXytlPA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GNXwWCc4CeiaujZAAJG5HBpwkIgsbmNDAQAB1501500j-ccb7-5&oh=00_Af028Vg951jil1x0Tb4v8iPvAx71o7Lk6bsHVCls3dvS8g&oe=69DC549C&_nc_sid=6ff7c8",
    "is_private": false,
    "is_verified": false
  }
]
```

</details>

---

### GET /v1/user/followers/chunk

Get part (one page) of followers users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/followers/chunk?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_followers_chunk_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/followers/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/followers/chunk?user_id=787132",
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
      "pk": "43374964307",
      "id": "43374964307",
      "username": "postedbynj",
      "full_name": "",
      "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/658260017_18063616745444308_1491397800595950837_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gGoDoBZ08ex5DYyQhqdCgWmZ9_tM3QHEUIusxH8LL_ppGCxYx9q1NdnAkW2Mx9t7w4&_nc_ohc=Qs_lKy2sErgQ7kNvwHNnPD4&_nc_gid=iQQ26RbG38f6g09ljTRFLA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GDFAPCfUk3iDwyxAAPUMUttlgrIUbmNDAQAB1501500j-ccb7-5&oh=00_Af0hKuSdAsB0ngtX0Tawz0PEuaGUp3JQKQBryIqR86G79g&oe=69DC35EE&_nc_sid=6ff7c8",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "69025436922",
      "id": "69025436922",
      "username": "pedroqduarte",
      "full_name": "Pedro Duarte",
      "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.2885-19/491416168_662266566416516_4619764470022606481_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MjAuYzEifQ&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGoDoBZ08ex5DYyQhqdCgWmZ9_tM3QHEUIusxH8LL_ppGCxYx9q1NdnAkW2Mx9t7w4&_nc_ohc=J452D13OposQ7kNvwEFS_4r&_nc_gid=iQQ26RbG38f6g09ljTRFLA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GGhqSh2EGHDzU1oCAJEOqxVPsxxAbkULAAAB1501500j-ccb7-5&oh=00_Af1PTImN0cYH5f1OkjwkBjJEjpVVaPjNxp_ro-9THPldiA&oe=69DC5FDF&_nc_sid=6ff7c8",
      "is_private": true,
      "is_verified": false
    },
    {
      "pk": "35814620919",
      "id": "35814620919",
      "username": "praguosphere",
      "full_name": "PRAGUOSPHERE",
      "profile_pic_url": "https://scontent-bos5-1.cdninstagram.com/v/t51.82787-19/660140245_18074573600196920_3208973545650305425_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-bos5-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGoDoBZ08ex5DYyQhqdCgWmZ9_tM3QHEUIusxH8LL_ppGCxYx9q1NdnAkW2Mx9t7w4&_nc_ohc=N0ogvpr6pBAQ7kNvwEChzKH&_nc_gid=iQQ26RbG38f6g09ljTRFLA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GNXwWCc4CeiaujZAAJG5HBpwkIgsbmNDAQAB1501500j-ccb7-5&oh=00_Af3I9AHE58Xo3vul0E5E-X11UCeEHdQj208Y1VeyI8eYwA&oe=69DC549C&_nc_sid=6ff7c8",
      "is_private": false,
      "is_verified": false
    }
  ],
  null
]
```

</details>

---

### GET /v1/user/following

Get following users. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/following?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/following",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/following?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "1573199054",
    "id": "1573199054",
    "username": "prasen.yadav",
    "full_name": "Prasenjeet Yadav",
    "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/v/t51.2885-19/288857217_2005973429587050_7315592429396790931_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42MTYuYzIifQ&_nc_ht=scontent-lhr8-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gEGJEhxI2gPbFz5tTw9BkGdG3o7I8bCKTy0G2vw535f-hwzSpPQOpP_OxNLoq4nE2I&_nc_ohc=DzSR3P_lWkkQ7kNvwHtna_4&_nc_gid=wA-9QYPv9WMDkOSCXJezvw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GIGcNxFqDLMVbCAHAJOOuwuONIZlbkULAAAB1501500j-ccb7-5&oh=00_Af1e7On14E8j7wI1ObQy8swXesPmpKRedtZwGON8pIQc6A&oe=69DC4C23&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "1993951421",
    "id": "1993951421",
    "username": "spencerlowell_",
    "full_name": "Spencer Lowell",
    "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/v/t51.2885-19/241500723_1655366887992954_4902963915361527679_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lhr8-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gEGJEhxI2gPbFz5tTw9BkGdG3o7I8bCKTy0G2vw535f-hwzSpPQOpP_OxNLoq4nE2I&_nc_ohc=utZmLSpun-UQ7kNvwGN3T6z&_nc_gid=wA-9QYPv9WMDkOSCXJezvw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GDMCZQ567lQjjOEFAH_nrjm00wpEbkULAAAB1501500j-ccb7-5&oh=00_Af06NYLc5vzyfT2oII_20X6tahkhDHs_KVHPs_f_lzXEBg&oe=69DC5B92&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "284213951",
    "id": "284213951",
    "username": "acacia.johnson",
    "full_name": "Acacia Johnson",
    "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/v/t51.2885-19/287240805_594289215195385_8575604715526875452_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lhr8-2.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gEGJEhxI2gPbFz5tTw9BkGdG3o7I8bCKTy0G2vw535f-hwzSpPQOpP_OxNLoq4nE2I&_nc_ohc=vggoi7--cjoQ7kNvwGmlWcf&_nc_gid=wA-9QYPv9WMDkOSCXJezvw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GGXyHhH5yJC9gBwCADzpJKMNqwJ3bkULAAAB1501500j-ccb7-5&oh=00_Af1JuckO5FPW7z732pj55Qfadu7BLUqnZsIU9N2uVIR8RA&oe=69DC3467&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": true
  }
]
```

</details>

---

### GET /v1/user/following/chunk

Get part (one page) of following users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/following/chunk?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_following_chunk_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/following/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/following/chunk?user_id=787132",
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
      "pk": "8958735",
      "id": "8958735",
      "username": "christiehemmklok",
      "full_name": "Christie Hemm Klok",
      "profile_pic_url": "https://scontent-lhr6-2.cdninstagram.com/v/t51.2885-19/439586899_1933783770387040_7648789920126959876_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lhr6-2.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gF-HlSNYBOpeKySa_93kENO1OTepSJG1WWTHuDy4gW9Zk8B0oM1jnXi20ivcIG8JNw&_nc_ohc=78gK351qr6gQ7kNvwGuh1ts&_nc_gid=HLAoi86C_3Ipbu5q7TDpIw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GFOQMxpg0rQexN4GAASBwUbo9SVqbkULAAAB1501500j-ccb7-5&oh=00_Af3D4jIQbkGgN34XFEXvKXvuZHJxDsWOR4DPhYcz-hvSDQ&oe=69DC42DC&_nc_sid=ce9561",
      "is_private": false,
      "is_verified": true
    },
    {
      "pk": "12802178",
      "id": "12802178",
      "username": "stephaniemeiling",
      "full_name": "Stephanie Mei-Ling",
      "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/v/t51.2885-19/416867607_774634348037538_4645960129122799142_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lhr8-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gF-HlSNYBOpeKySa_93kENO1OTepSJG1WWTHuDy4gW9Zk8B0oM1jnXi20ivcIG8JNw&_nc_ohc=9cpBf5YDNfEQ7kNvwEKTTUj&_nc_gid=HLAoi86C_3Ipbu5q7TDpIw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GBfl2BiiRSWdhsACACYO-kAfxHlAbkULAAAB1501500j-ccb7-5&oh=00_Af185OMR_sNtXawJTgrzmdNMKziw3wS7lx8AEoMaPwRq9w&oe=69DC38FB&_nc_sid=ce9561",
      "is_private": false,
      "is_verified": true
    },
    {
      "pk": "14331657700",
      "id": "14331657700",
      "username": "natgeomagjp",
      "full_name": "ナショナルジオグラフィック日本版",
      "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/v/t51.2885-19/65160972_483182759115510_2590728031043584000_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MDAuYzIifQ&_nc_ht=scontent-lhr8-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gF-HlSNYBOpeKySa_93kENO1OTepSJG1WWTHuDy4gW9Zk8B0oM1jnXi20ivcIG8JNw&_nc_ohc=7ujGFVqjyKQQ7kNvwFh_x0A&_nc_gid=HLAoi86C_3Ipbu5q7TDpIw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GAxH4gP2_rfAc7cBAAAAAABrHfQjbkULAAAB1501500j-ccb7-5&oh=00_Af1Sa1MdNHAsz2xLp5zvpeee2oJWbZ1891Y60zN6pafI5A&oe=69DC5A2D&_nc_sid=ce9561",
      "is_private": false,
      "is_verified": false
    }
  ],
  "25"
]
```

</details>

---

### GET /v1/user/guides

Get user guides. Returns guide data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/guides?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/guides",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/guides?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/user/medias

Get user medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/medias?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/medias",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/medias?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3865659729796199935",
    "id": "3865659729796199935_787132",
    "code": "DWllQsJCPX_",
    "taken_at": "2026-04-01T13:00:03Z",
    "taken_at_ts": 1775048403,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwFl32Gs&_nc_oc=Adq9WBao_LhDtMDdsmgQ8h9nUUrmsvg1gn07m_6duXK6CP5JI-ZqJo6CTfEoHJ4XYxs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af1aE9xk7_KkClbFxHLQIHZfOnRQ1QCCbS9FfcT0sDC9Bg&oe=69DC65F1",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ISyQc8pt6zrtXlkEB5QaRVGsZgW0XPDgdxDaTpnYOWw&oe=69DC51E9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 236,
    "comments_disabled": false,
    "like_count": 35859,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vv7MGWT_LSQ8ikA8idtvNUmrwW_wcERl2sytXl7NNmw&oe=69D84A2E",
    "view_count": 0,
    "video_duration": 60.10100173950195,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          24827,
          49654,
          74482
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwFl32Gs&_nc_oc=Adq9WBao_LhDtMDdsmgQ8h9nUUrmsvg1gn07m_6duXK6CP5JI-ZqJo6CTfEoHJ4XYxs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af1aE9xk7_KkClbFxHLQIHZfOnRQ1QCCbS9FfcT0sDC9Bg&oe=69DC65F1",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 101,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vv7MGWT_LSQ8ikA8idtvNUmrwW_wcERl2sytXl7NNmw&oe=69D84A2E",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 102,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vv7MGWT_LSQ8ikA8idtvNUmrwW_wcERl2sytXl7NNmw&oe=69D84A2E",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 103,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0vv7MGWT_LSQ8ikA8idtvNUmrwW_wcERl2sytXl7NNmw&oe=69D84A2E",
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
        "best_audio_cluster_id": "1378215947658482"
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
        "is_reuse_allowed": false,
        "mashup_type": null,
        "mashups_allowed": false,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18456784822103981",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26356368770680868,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.02S\" FBManifestTimestamp=\"1775663895\" FBManifestIdentifier=\"Fq7ss50NKRbkmJfH7/yMBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.02S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwFbNmcK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njc5NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af16Dyfr26HEpE--xWEKXVZxfkc7vgSIWEEBOV7a-we1GQ&amp;oe=69D873C7</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 60101,
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
        "original_media_id": 3865659729796199935,
        "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQM3BWmWT9DCIR_4a6ETqY74iK_vSJ0mGCY5KURpD0ZI6aeamU2Fve1dXA5lCRBiztE1g_SEXMn_Iq_pDtwv8Zw.mp4?_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=3yv_Gp1gyOgQ7kNvwEBDMnN&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3lSljUAlD2jjyR2ucM7VykslNXmO49CsHoOTNvjqj_xA&oe=69D8476D",
        "should_mute_audio": false,
        "time_created": 1775048409,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ISyQc8pt6zrtXlkEB5QaRVGsZgW0XPDgdxDaTpnYOWw&oe=69DC51E9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.101768S\" FBManifestTimestamp=\"1775663895\" FBManifestIdentifier=\"Fq7ss50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZhvqW8/S+xeQEgpGBqJewoQXkmJfH7/yMBoa64qTa1eUGnIqa4KeDiwes8M2L68zyB6qAsLy5tYsKpNyD9fH5gw8iGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABYOFAASFAIA\"><Period id=\"0\" duration=\"PT60.101768S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1912423616106115v\" bandwidth=\"166877\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"1253701\" FBPlaybackResolutionMos=\"0:100,360:45.1,480:40.4,720:35.9,1080:35\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:82.8,480:77.6,720:69.7,1080:61\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQN7bvgXP3EERrcFHV-1fzXBQM1B_9zyFprEaczO3CcVJH51ops-BaT6-AB2k1O0FvXFPPD2X7C2vGgstKAX_lUDqtPt_BBmr3DTx2E.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=1wt_F1UXMNIQ7kNvwE8QoMh&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTY2ODc3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1n6TzrkitIe2Ie3TxtgQ6yQNDYgzDcTQKWEqvP7Y1Y0A&amp;oe=69DC627D</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-6063\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-67802\" FBFirstSegmentRange=\"1006-96225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"96226-176795\" FBPrefetchSegmentRange=\"1006-96225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"2222333531634710v\" bandwidth=\"235880\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1772106\" FBPlaybackResolutionMos=\"0:100,360:53.3,480:47.5,720:42.4,1080:40.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.4,480:83.6,720:76.9,1080:69.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMxCLZAMZYTTX850gil00dm2ioBo0drmeTqH8LuaWvnzqyeGZJZP8J_cQ20AfxeWCg7AC068zNIS6I65UBB_hF8joElUCDd82X01Go.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=PKUFPD2uIVkQ7kNvwFiBTXM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjM1ODgwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ixRbzkM9PGYsj5e9t2ehg7RsBAvUj8jtEMHboLiXj3Q&amp;oe=69DC5898</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-7165\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-97051\" FBFirstSegmentRange=\"1006-136329\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"136330-250577\" FBPrefetchSegmentRange=\"1006-136329\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1346996087449021v\" bandwidth=\"344253\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2586277\" FBPlaybackResolutionMos=\"0:100,360:60.4,480:54.8,720:48.9,1080:45.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.4,480:88.4,720:83,1080:75.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPyrERzJR93bmM5sO3ncLVP0I0OisCfS5PUToFBIqxTUroxmHrokOOOImjJtJ9NQoCgG2ffbBOZ4d8i3jjPy89AcBgMEBW7rlacpSA.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=PXFqSr-LPV0Q7kNvwF1e9J9&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzQ0MjUzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0sba1zuutM3Y5Fyrdu9CJITHXeXxhvcOWyrZJbD08LEA&amp;oe=69DC31A0</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-8337\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-142091\" FBFirstSegmentRange=\"1006-199329\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"199330-361546\" FBPrefetchSegmentRange=\"1006-199329\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"2839857269702677v\" bandwidth=\"478610\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"3595664\" FBPlaybackResolutionMos=\"0:100,360:66.5,480:60.9,720:54.8,1080:51.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.7,480:91.5,720:87.2,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNiAaP40VbnrziEA7hzJ8oQwo0TnIJXWfp96DakLB1VsnbIkeQh1hfkbBQZHlYlzGkAGsp6ekcMCdTGcKucLa4lMZZK3kxAw5vXYH0.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=IV1KWSvHCRoQ7kNvwGRNF-Z&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDc4NjEwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3RRUud3jVVOxwITBfyF3KHp0AJ5-lOGCFp0lmO0_IhIw&amp;oe=69DC34FB</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-9562\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-199566\" FBFirstSegmentRange=\"1006-277896\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"277897-496955\" FBPrefetchSegmentRange=\"1006-277896\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1480770413667393v\" bandwidth=\"660384\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"4961287\" FBPlaybackResolutionMos=\"0:100,360:71.5,480:66.3,720:59.9,1080:56.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.4,480:93.7,720:90.2,1080:84.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMx890oqh8uzWFtsN_eFr7rba3UGYuBWOyYURXs8cEqGprQ-uukGBWZeiSRC_gNmVlaTJm5U0TL1RPBWXN1lkRLg_H5dZahO9hWAc0.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=9gGw3aKQD-UQ7kNvwHGRRW6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjYwMzg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0k1K9FGY8th80QIGofqNSJJGUsipoFNIBsfoDd_-ddUA&amp;oe=69DC5FD5</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-10557\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-273394\" FBFirstSegmentRange=\"1006-384838\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"384839-682697\" FBPrefetchSegmentRange=\"1006-384838\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1994570967761550v\" bandwidth=\"910868\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"6843099\" FBPlaybackResolutionMos=\"0:100,360:75.6,480:70.9,720:64.8,1080:60.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:95.2,720:92.5,1080:87.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMiapH1AYzNLqYDeqtzlFEXwA8s4V5OkLxU9l0tMtwSSulT9IGU5j3LVMWJrp_XYtv6fKnq4TM6m9Yf4XG1E__kucjZC3c3eIHnYW0.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=_Xjbc55RSvAQ7kNvwGGeDi1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6OTEwODY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af17SCeC9fB4HKvHxoSskYIxzB8oHMPHbYJU9urC-3FPlQ&amp;oe=69DC4B42</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-11609\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-367830\" FBFirstSegmentRange=\"1006-525554\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"525555-933446\" FBPrefetchSegmentRange=\"1006-525554\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"4230815773914898v\" bandwidth=\"1318016\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"9901890\" FBPlaybackResolutionMos=\"0:100,360:80.1,480:75.4,720:69.5,1080:65.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.3,480:96.5,720:94.8,1080:90.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOVXmOyihR7FmuIWxtZ4w5Kacv6h93vRQNpPKMiS6kgmPTRziO9TmVM6d0FaUbUB_W6f5LlOVzvb2R6Amrqt5yA_WvvaTjq_o1zgpA.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=fGTSsPSwh5UQ7kNvwFMW59F&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTMxODAxNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3YlTcX5DewOaHtTW9awUX5Ip3VxsFNNP45tFHKTkHF0w&amp;oe=69DC4934</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-12986\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-509326\" FBFirstSegmentRange=\"1006-751276\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"751277-1331719\" FBPrefetchSegmentRange=\"1006-751276\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"501139\" FBPaqMos=\"88.19\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwFbNmcK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjY3OTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1gB_oMBl9ZZQI36gAN7bIkK7ae_XQpUuaQ3qd0ahkmfw&amp;oe=69D873C7</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\" FBMinimumPrefetchRange=\"1228-1588\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1228-23446\" FBFirstSegmentRange=\"1228-20301\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"20302-37270\" FBPrefetchSegmentRange=\"1228-37270\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "18091046",
        "pk": 18091046,
        "pk_id": "18091046",
        "id": "18091046",
        "username": "natgeotv",
        "full_name": "National Geographic TV",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865691934048399589_18091046",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=zov5ST0QeW4Q7kNvwF3oR9m&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af3Zb6HvEepYqN0-U3gBFBmQX5DJ_NCd_nnXLcCIs0l7tQ&oe=69DC4D93&_nc_sid=b41fef",
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
        "strong_id__": "284634734",
        "pk": 284634734,
        "pk_id": "284634734",
        "id": "284634734",
        "username": "disney",
        "full_name": "Disney",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3859143390382675003_284634734",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/656558113_18577653481026735_1735858011052165396_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=HX8JmLcZS9cQ7kNvwHRH-cI&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCFIIievNH8ERwBCABTJRwGqARcYbmNDAQAB1501500j-ccb7-5&oh=00_Af0asRwQPVAJBj_MvfgUEjDtFRvi5nhzrQRVYwHwKJIkFQ&oe=69DC5A43&_nc_sid=b41fef",
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
  },
  {
    "pk": "3844732796656436386",
    "id": "3844732796656436386_787132",
    "code": "DVbPBu5AESi",
    "taken_at": "2026-03-03T15:00:04Z",
    "taken_at_ts": 1772550004,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwG4F5vT&_nc_oc=Ado2xX9Aq_Myu54ApiZkvwxrkm5T8dPp4H7NpQtw8i6WlGFiFY6Fmn5z0i_YIEvzO4g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af2CxB4DIcP_1U_x9tyDlfCVJ1eTOvgxhpiBKLfLimrTdw&oe=69DC51CA",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ISyQc8pt6zrtXlkEB5QaRVGsZgW0XPDgdxDaTpnYOWw&oe=69DC51E9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 614,
    "comments_disabled": false,
    "like_count": 66069,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3GWyXM0kWaiWTdKdG_YYdCNjZbJC8JWuNvPPoZ0NiYmQ&oe=69D848EB",
    "view_count": 0,
    "video_duration": 60.07400131225586,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          48270,
          96540,
          144811
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwG4F5vT&_nc_oc=Ado2xX9Aq_Myu54ApiZkvwxrkm5T8dPp4H7NpQtw8i6WlGFiFY6Fmn5z0i_YIEvzO4g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af2CxB4DIcP_1U_x9tyDlfCVJ1eTOvgxhpiBKLfLimrTdw&oe=69DC51CA",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 101,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3GWyXM0kWaiWTdKdG_YYdCNjZbJC8JWuNvPPoZ0NiYmQ&oe=69D848EB",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 102,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3GWyXM0kWaiWTdKdG_YYdCNjZbJC8JWuNvPPoZ0NiYmQ&oe=69D848EB",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 103,
        "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3GWyXM0kWaiWTdKdG_YYdCNjZbJC8JWuNvPPoZ0NiYmQ&oe=69D848EB",
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
        "best_audio_cluster_id": "2285888061908806"
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
        "is_reuse_allowed": false,
        "mashup_type": null,
        "mashups_allowed": false,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18531263347067949",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26397325093213654,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663895\" FBManifestIdentifier=\"Fq7ss50NKRb65a+KkPmzCSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwHIIuno&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af07YjTRp5TGDAK7TM32RnLkSSP2sti4GXpBeXgUNReyTA&amp;oe=69D86283</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 60074,
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
        "original_media_id": 3844732796656436386,
        "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQOu1cJkIUYpfLz5hsq6b4bAI93Dsnj-0FVN5QJfDUtHrdxoyYljTBeDYR-FHSZ5LvVWtD_zp4sNL8fsO46SW16u.mp4?_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=zRv5taEP1NwQ7kNvwE22s8k&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0h4y6pF9gnmROunE6Q47wyUg4ItLpicTezPi8mz0TCSw&oe=69D8409F",
        "should_mute_audio": false,
        "time_created": 1772550012,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ISyQc8pt6zrtXlkEB5QaRVGsZgW0XPDgdxDaTpnYOWw&oe=69DC51E9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663895\" FBManifestIdentifier=\"Fq7ss50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZlsratODCzrQCgpGvuY7mpQPc6NjMprirBOCA5uCtu+YG+uWvipD5swmo0qnPweKbDKrMkpjEg4dcirnQvPLp4F2C8dTlwpDpXSIYGGRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsGRgFbGlnaHQAFkgUABIUAgA=\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1221425160198702v\" bandwidth=\"88841\" codecs=\"vp09.00.30.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"666981\" FBPlaybackResolutionMos=\"0:100,360:42.4,480:42.2,720:44.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:69.2,480:64.6,720:59.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"180p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMkUUBoVi_ub6duvm9o0zVD3FqHqNnfmFIIUyYMopmyOCFovt0jt7tT0MWjPJMry7gxFaH81JHTAu-3ZsBjAa08euE0JvQRfX8f4dA.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=j62NyMr0qVAQ7kNvwH_KDJR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjg4ODQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1yBsXllwRsTiOxTUO0lMfu8a3Oq8pLSC3WgGaDLQmg0w&amp;oe=69DC3B5B</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-6649\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-27353\" FBFirstSegmentRange=\"975-49463\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"49464-99920\" FBPrefetchSegmentRange=\"975-49463\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"678648151971493v\" bandwidth=\"131405\" codecs=\"vp09.00.30.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"986526\" FBPlaybackResolutionMos=\"0:100,360:52.6,480:51.3,720:52.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:79.2,480:74.7,720:68.5\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMTuYIt8uIN7FmfcNiMEmM088p1ojFhfWyppf1rCqdoRnEZjOBAVQKnl7tVDa0fwYoD97P-LJMcQtFCa_4zgosvXzmasUGqWrTn-sY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=jFPdYIunJWIQ7kNvwGGnwcu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjEzMTQwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2SU6jdorOPF2H8htyhdO9dEy33dfwkoHkdHNQ2YJiRtg&amp;oe=69DC4289</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-8510\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-38020\" FBFirstSegmentRange=\"975-66869\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"66870-139717\" FBPrefetchSegmentRange=\"975-66869\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"25911151711900437v\" bandwidth=\"184219\" codecs=\"vp09.00.30.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"1383031\" FBPlaybackResolutionMos=\"0:100,360:59.3,480:57.4,720:57.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86,480:82.2,720:76.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOa7vEXhZzWkoB91BY5wDbDQdoXHnkoGyd8Ns96jD4yd7jAWprXqb5mzrIbFoySj2dYDK3E-dzFtFEQeWiqb83bvc8K3aMox3Ayx80.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=cM_uL1WGyoQQ7kNvwHcKAvV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjE4NDIxOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1WuJzROodFR-KK-_HqZpP4L-KxVt-7nWY0uRmWcEsISA&amp;oe=69DC679A</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-10436\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-51508\" FBFirstSegmentRange=\"975-91478\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"91479-190792\" FBPrefetchSegmentRange=\"975-91478\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1914169985908784v\" bandwidth=\"255147\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"1915519\" FBPlaybackResolutionMos=\"0:100,360:65.8,480:63.6,720:63.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.3,480:86.1,720:82.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN8qcFGph18DKn73VhWMnVPZOS1edh-4P60ufMg_K-9kKgeanK_-wqY-jkmYGto_BTysGZp9O7nBLVpuEs_b2c19AT4i-V9JciDMOY.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=-Ey_NjPUsO4Q7kNvwHsqqbL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjI1NTE0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1JfokhW0kdG2ct3camFQtU1ZGcc2BBY0S2TGJJKkC_iQ&amp;oe=69DC39EC</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-13375\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-70737\" FBFirstSegmentRange=\"975-126204\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"126205-265560\" FBPrefetchSegmentRange=\"975-126204\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3438765782938772v\" bandwidth=\"365520\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"2744149\" FBPlaybackResolutionMos=\"0:100,360:72.9,480:70.7,720:69.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.5,720:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO4qM-cNuoLnfZlUy_IiVAT2Z8qF4wrxqNpNVQglEAoWPC13m_tPg_VquKp8yGWLlyNwPMfnVScpHlWvfWhweLyg2_AGpj83oZwtcA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=J_ubYeNVjJoQ7kNvwHaAkoF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjM2NTUyMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0HAwYxD8Ps4WySpx4KkZnd0J2hef1QHhS2yM0ZkevUdw&amp;oe=69DC688F</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-16766\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-100600\" FBFirstSegmentRange=\"975-179508\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"179509-376002\" FBPrefetchSegmentRange=\"975-179508\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"26408354118802497v\" bandwidth=\"508971\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"3821111\" FBPlaybackResolutionMos=\"0:100,360:77.8,480:75.7,720:74.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:94.6,720:92.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrD8S2IOYGSxcDRdQB0cAB4U_2mcQDXZdYVS3cDu_u_3CiV7RvCKeTHyc6Ei4ymT7PLdCW85vxrpSIQHl8ACI6dX49R5aLmoiBH24.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=0oJbYhI0MV4Q7kNvwEbFg8J&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjUwODk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af29rZPJIAxrKl__xX9UyxKQWW8K8m9TIsQZb_wvXSPISw&amp;oe=69DC576C</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-20846\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-140870\" FBFirstSegmentRange=\"975-255834\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"255835-524275\" FBPrefetchSegmentRange=\"975-255834\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"927543076447297v\" bandwidth=\"714491\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"5364051\" FBPlaybackResolutionMos=\"0:100,360:83.3,480:80.7,720:78.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.5,720:94.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNzuP-dxHHhCDOgE42W3DRgip3HC6kXW0Ky3-f5EEMINfKrpfaaxYyAaSB2Icf90jqmZr2q5J0Ve1sJqNkqV4OXkx9wDjN9W8yD_-A.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=rJolK-0juxQQ7kNvwG7DAOd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjcxNDQ5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3g9ZWqH4NXEPvRUhdg_dwwCJo6M_ztbh5dUcc_Jhs4kA&amp;oe=69DC46F9</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-26038\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-200467\" FBFirstSegmentRange=\"975-363535\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"363536-745087\" FBPrefetchSegmentRange=\"975-363535\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"26390098317282885v\" bandwidth=\"1089671\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q90\" FBContentLength=\"8180714\" FBPlaybackResolutionMos=\"0:100,360:87.8,480:85.5,720:83.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.35,720:97.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOIpKrCiWGBk_joSA25fivPUcx8XxdxvYeXBRUehwR8r8vE5v_3nsJ6A1r--74ibf2AAtfFSX7nP0Ym2GccV3oDZOulvkHEUiMZ0Js.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=GWW-iUt-eaMQ7kNvwEPYENN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjEwODk2NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1dWmZ6JhxCGEgeNnzfoJRvHIRWteUgUQTI-trwM-jymA&amp;oe=69DC4E02</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-34968\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-311296\" FBFirstSegmentRange=\"975-565432\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"565433-1149907\" FBPrefetchSegmentRange=\"975-565432\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"537214\" FBPaqMos=\"90.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwHIIuno&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjcxNTM5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=lasApcWPqP27dyGHG-x6Fw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2tS3EHtW5rajvMOi3vaHvxxMNHTNAYagkQDmNktbVR8Q&amp;oe=69D86283</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\" FBMinimumPrefetchRange=\"1228-1588\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1228-22518\" FBFirstSegmentRange=\"1228-18944\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"18945-36496\" FBPrefetchSegmentRange=\"1228-36496\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "10506924608",
        "pk": 10506924608,
        "pk_id": "10506924608",
        "id": "10506924608",
        "username": "jamescameronofficial",
        "full_name": "James Cameron",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "1964371814524155358_10506924608",
        "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=TYSekVkP8Y0Q7kNvwEzpw-g&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af1NynzJ5TX3i6nJjUjRgeZmhNwWksnYWPuJgR-w6PDJqw&oe=69DC6398&_nc_sid=b41fef",
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
        "strong_id__": "1029649300",
        "pk": 1029649300,
        "pk_id": "1029649300",
        "id": "1029649300",
        "username": "natgeoanimals",
        "full_name": "National Geographic Animals",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865698702530758137_1029649300",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=ic5ODsLE2O8Q7kNvwHES09N&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af1EH16D4S2N9LFVobRRlRVds-J_uXoFVJ4J70xP39T3bQ&oe=69DC588C&_nc_sid=b41fef",
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
  },
  {
    "pk": "3870670793969876810",
    "id": "3870670793969876810_787132",
    "code": "DW3YpRVDb9K",
    "taken_at": "2026-04-08T10:00:01Z",
    "taken_at_ts": 1775642401,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE1CM940aLNQQhY4DJZ1oKQPt0gQqwlTyDMoSKYxDY8rmLmb3NYo2kxqXSPuQqV7No&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=lasApcWPqP27dyGHG-x6Fw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ISyQc8pt6zrtXlkEB5QaRVGsZgW0XPDgdxDaTpnYOWw&oe=69DC51E9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 104,
    "comments_disabled": false,
    "like_count": 39865,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870670683399590370",
        "id": "3870670683399590370_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=109&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af0i9DN20RoTa62cEqzmE60L2RKAJzcu1oylVjwfw1dlSA&oe=69DC4AFB",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              56778,
              113556,
              170335
            ],
            "height": 959,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=109&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af0i9DN20RoTa62cEqzmE60L2RKAJzcu1oylVjwfw1dlSA&oe=69DC4AFB",
            "width": 1439,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              27979,
              55958,
              83938
            ],
            "height": 500,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=109&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af3VK-eQ8EhhQ2tp9AMTL9wlYN2Q842khFEANcoqg86tNg&oe=69DC4AFB",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      },
      {
        "pk": "3870670679968669302",
        "id": "3870670679968669302_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHUEQvY&_nc_oc=AdrTEh6bShOipdLW3jXQmv3DJ7nlLcBP7RD-RzH-xALHxcBSih6hvEUEaYTKbzZCsuo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af3vJP1Q8OZYr0Y_Ye-3hA_BP9hjdLVlhmI6QR5cYagLuw&oe=69DC54D1",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              40239,
              80479,
              120719
            ],
            "height": 959,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHUEQvY&_nc_oc=AdrTEh6bShOipdLW3jXQmv3DJ7nlLcBP7RD-RzH-xALHxcBSih6hvEUEaYTKbzZCsuo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af3vJP1Q8OZYr0Y_Ye-3hA_BP9hjdLVlhmI6QR5cYagLuw&oe=69DC54D1",
            "width": 1439,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              19829,
              39659,
              59488
            ],
            "height": 500,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHUEQvY&_nc_oc=AdrTEh6bShOipdLW3jXQmv3DJ7nlLcBP7RD-RzH-xALHxcBSih6hvEUEaYTKbzZCsuo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af0SkGDL6IEVg81wzodqWJsEehVM1osF3cDdSzVsxovguQ&oe=69DC54D1",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      },
      {
        "pk": "3870670694816531730",
        "id": "3870670694816531730_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwGNLa1X&_nc_oc=AdqUd3B1Nnj5B8CwbTDFHK2mXqj5g49dmO2dtZHvh6ExyzXIdTwkmyejEE6AswbHreg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af3X9NvbfHeyZ-kpEpBW04YLUq_8KOUO5xwXssSr40erLA&oe=69DC46CA",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              51971,
              103943,
              155915
            ],
            "height": 1080,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwGNLa1X&_nc_oc=AdqUd3B1Nnj5B8CwbTDFHK2mXqj5g49dmO2dtZHvh6ExyzXIdTwkmyejEE6AswbHreg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af3X9NvbfHeyZ-kpEpBW04YLUq_8KOUO5xwXssSr40erLA&oe=69DC46CA",
            "width": 1440,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              25599,
              51198,
              76797
            ],
            "height": 563,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwGNLa1X&_nc_oc=AdqUd3B1Nnj5B8CwbTDFHK2mXqj5g49dmO2dtZHvh6ExyzXIdTwkmyejEE6AswbHreg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af0y2va034LYWHIaz_jqq_CeCfiza5wLZCaLhMPXjpmBDw&oe=69DC46CA",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          56778,
          113556,
          170335
        ],
        "height": 959,
        "scans_profile": "e35",
        "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af1Tqem90NWcrFuDuphXXnqoJy60GH6-x7bfhyuV0mzK3A&oe=69DC4AFB",
        "width": 1439,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          27979,
          55958,
          83938
        ],
        "height": 500,
        "scans_profile": "e35",
        "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=lasApcWPqP27dyGHG-x6Fw&_nc_ss=7a3ba&oh=00_Af0fyCE1fIZQSMHNBn_0bke4RfL-TPeNyclTJ38eKW7gXQ&oe=69DC4AFB",
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

### GET /v1/user/medias/chunk

Get part of user medias with cursor. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/medias/chunk?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_medias_chunk_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/medias/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/medias/chunk?user_id=787132",
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
      "pk": "3865659729796199935",
      "id": "3865659729796199935_787132",
      "code": "DWllQsJCPX_",
      "taken_at": "2026-04-01T13:00:03Z",
      "taken_at_ts": 1775048403,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwFl32Gs&_nc_oc=Adq9WBao_LhDtMDdsmgQ8h9nUUrmsvg1gn07m_6duXK6CP5JI-ZqJo6CTfEoHJ4XYxs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af3r9pcbOn4mB9Su9PETctzghJ9eytBuyP2nybe4tZTHWw&oe=69DC65F1",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1oUt1ISLpzLpLM6_XTIC7QFC0meaMhYfXpzUHRHnlucw&oe=69DC51E9&_nc_sid=b41fef",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 236,
      "comments_disabled": false,
      "like_count": 35858,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2roHfcHszzeP-oE2LS8JURM11xcXDygXjUV3p9BN3PMA&oe=69D84A2E",
      "view_count": 0,
      "video_duration": 60.10100173950195,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            24827,
            49654,
            74482
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwFl32Gs&_nc_oc=Adq9WBao_LhDtMDdsmgQ8h9nUUrmsvg1gn07m_6duXK6CP5JI-ZqJo6CTfEoHJ4XYxs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af3r9pcbOn4mB9Su9PETctzghJ9eytBuyP2nybe4tZTHWw&oe=69DC65F1",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1568436,
          "height": 1280,
          "id": "1258679306414510v",
          "type": 101,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2roHfcHszzeP-oE2LS8JURM11xcXDygXjUV3p9BN3PMA&oe=69D84A2E",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1568436,
          "height": 1280,
          "id": "1258679306414510v",
          "type": 102,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2roHfcHszzeP-oE2LS8JURM11xcXDygXjUV3p9BN3PMA&oe=69D84A2E",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1568436,
          "height": 1280,
          "id": "1258679306414510v",
          "type": 103,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwHah8C4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2roHfcHszzeP-oE2LS8JURM11xcXDygXjUV3p9BN3PMA&oe=69D84A2E",
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
          "best_audio_cluster_id": "1378215947658482"
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
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18456784822103981",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26356368770680868,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": true,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.02S\" FBManifestTimestamp=\"1775663872\" FBManifestIdentifier=\"FoDss50NKRbkmJfH7/yMBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.02S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwFbNmcK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njc5NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0o1e53IANHQWzVeX-N7WcB4G5dxuuhElI0Rex-02j_RA&amp;oe=69D873C7</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 60101,
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
          "original_media_id": 3865659729796199935,
          "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQM3BWmWT9DCIR_4a6ETqY74iK_vSJ0mGCY5KURpD0ZI6aeamU2Fve1dXA5lCRBiztE1g_SEXMn_Iq_pDtwv8Zw.mp4?_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=3yv_Gp1gyOgQ7kNvwEBDMnN&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af15Gj69HN_nyXTYllL9AVCAHH68UYgS5Sqgczys5pFTsA&oe=69D8476D",
          "should_mute_audio": false,
          "time_created": 1775048409,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1oUt1ISLpzLpLM6_XTIC7QFC0meaMhYfXpzUHRHnlucw&oe=69DC51E9&_nc_sid=b41fef"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.101768S\" FBManifestTimestamp=\"1775663872\" FBManifestIdentifier=\"FoDss50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZhvqW8/S+xeQEgpGBqJewoQXkmJfH7/yMBoa64qTa1eUGnIqa4KeDiwes8M2L68zyB6qAsLy5tYsKpNyD9fH5gw8iGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABYOFAASFAIA\"><Period id=\"0\" duration=\"PT60.101768S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1912423616106115v\" bandwidth=\"166877\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"1253701\" FBPlaybackResolutionMos=\"0:100,360:45.1,480:40.4,720:35.9,1080:35\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:82.8,480:77.6,720:69.7,1080:61\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQN7bvgXP3EERrcFHV-1fzXBQM1B_9zyFprEaczO3CcVJH51ops-BaT6-AB2k1O0FvXFPPD2X7C2vGgstKAX_lUDqtPt_BBmr3DTx2E.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=1wt_F1UXMNIQ7kNvwE8QoMh&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTY2ODc3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2rfb9xnQdhS2Ft9vj6x5DDo87pAqMHNDDIazYkGuQEKg&amp;oe=69DC627D</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-6063\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-67802\" FBFirstSegmentRange=\"1006-96225\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"96226-176795\" FBPrefetchSegmentRange=\"1006-96225\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"2222333531634710v\" bandwidth=\"235880\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1772106\" FBPlaybackResolutionMos=\"0:100,360:53.3,480:47.5,720:42.4,1080:40.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:87.4,480:83.6,720:76.9,1080:69.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMxCLZAMZYTTX850gil00dm2ioBo0drmeTqH8LuaWvnzqyeGZJZP8J_cQ20AfxeWCg7AC068zNIS6I65UBB_hF8joElUCDd82X01Go.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=PKUFPD2uIVkQ7kNvwFiBTXM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjM1ODgwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3bL-emFLUa8sgll8CtdZ4SxlZ2dZXO9bMGDQOg9KtP_Q&amp;oe=69DC5898</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-7165\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-97051\" FBFirstSegmentRange=\"1006-136329\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"136330-250577\" FBPrefetchSegmentRange=\"1006-136329\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1346996087449021v\" bandwidth=\"344253\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"2586277\" FBPlaybackResolutionMos=\"0:100,360:60.4,480:54.8,720:48.9,1080:45.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.4,480:88.4,720:83,1080:75.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPyrERzJR93bmM5sO3ncLVP0I0OisCfS5PUToFBIqxTUroxmHrokOOOImjJtJ9NQoCgG2ffbBOZ4d8i3jjPy89AcBgMEBW7rlacpSA.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=PXFqSr-LPV0Q7kNvwF1e9J9&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzQ0MjUzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Th2AH1syPVEty70e3d4Ul5st_vDxrW6_z1xLQZlVURA&amp;oe=69DC31A0</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-8337\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-142091\" FBFirstSegmentRange=\"1006-199329\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"199330-361546\" FBPrefetchSegmentRange=\"1006-199329\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"2839857269702677v\" bandwidth=\"478610\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"3595664\" FBPlaybackResolutionMos=\"0:100,360:66.5,480:60.9,720:54.8,1080:51.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.7,480:91.5,720:87.2,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNiAaP40VbnrziEA7hzJ8oQwo0TnIJXWfp96DakLB1VsnbIkeQh1hfkbBQZHlYlzGkAGsp6ekcMCdTGcKucLa4lMZZK3kxAw5vXYH0.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=IV1KWSvHCRoQ7kNvwGRNF-Z&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDc4NjEwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af30he3V7tHXf57i28iBkT5QP1K1GINFcYXMRXKozJPGhQ&amp;oe=69DC34FB</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-9562\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-199566\" FBFirstSegmentRange=\"1006-277896\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"277897-496955\" FBPrefetchSegmentRange=\"1006-277896\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1480770413667393v\" bandwidth=\"660384\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"4961287\" FBPlaybackResolutionMos=\"0:100,360:71.5,480:66.3,720:59.9,1080:56.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.4,480:93.7,720:90.2,1080:84.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMx890oqh8uzWFtsN_eFr7rba3UGYuBWOyYURXs8cEqGprQ-uukGBWZeiSRC_gNmVlaTJm5U0TL1RPBWXN1lkRLg_H5dZahO9hWAc0.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=9gGw3aKQD-UQ7kNvwHGRRW6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjYwMzg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2yFWLNMJ3XtEU1mumdN7NitbepaWErinFllq3gEiqupQ&amp;oe=69DC5FD5</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-10557\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-273394\" FBFirstSegmentRange=\"1006-384838\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"384839-682697\" FBPrefetchSegmentRange=\"1006-384838\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1994570967761550v\" bandwidth=\"910868\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"6843099\" FBPlaybackResolutionMos=\"0:100,360:75.6,480:70.9,720:64.8,1080:60.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:95.2,720:92.5,1080:87.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQMiapH1AYzNLqYDeqtzlFEXwA8s4V5OkLxU9l0tMtwSSulT9IGU5j3LVMWJrp_XYtv6fKnq4TM6m9Yf4XG1E__kucjZC3c3eIHnYW0.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=_Xjbc55RSvAQ7kNvwGGeDi1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6OTEwODY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3r96e-480dg9sVb2BtdnligW01HLjafutiT9-BNnkUrw&amp;oe=69DC4B42</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-11609\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-367830\" FBFirstSegmentRange=\"1006-525554\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"525555-933446\" FBPrefetchSegmentRange=\"1006-525554\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"4230815773914898v\" bandwidth=\"1318016\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"9901890\" FBPlaybackResolutionMos=\"0:100,360:80.1,480:75.4,720:69.5,1080:65.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.3,480:96.5,720:94.8,1080:90.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOVXmOyihR7FmuIWxtZ4w5Kacv6h93vRQNpPKMiS6kgmPTRziO9TmVM6d0FaUbUB_W6f5LlOVzvb2R6Amrqt5yA_WvvaTjq_o1zgpA.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=fGTSsPSwh5UQ7kNvwFMW59F&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTMxODAxNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3kF5ozL5vc8gIfl3GLrfr1xWJBMqqx_ocBN0XR9nYJkQ&amp;oe=69DC4934</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-12986\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-509326\" FBFirstSegmentRange=\"1006-751276\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"751277-1331719\" FBPrefetchSegmentRange=\"1006-751276\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"501139\" FBPaqMos=\"88.19\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwFbNmcK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjY3OTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af29thVa0VxB23GopJx247DpGu9tYT3sZDL0bF1CgQ2lQg&amp;oe=69D873C7</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\" FBMinimumPrefetchRange=\"1228-1588\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1228-23446\" FBFirstSegmentRange=\"1228-20301\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"20302-37270\" FBPrefetchSegmentRange=\"1228-37270\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "18091046",
          "pk": 18091046,
          "pk_id": "18091046",
          "id": "18091046",
          "username": "natgeotv",
          "full_name": "National Geographic TV",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865691934048399589_18091046",
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=zov5ST0QeW4Q7kNvwF3oR9m&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af1yFbiYQFMEe7DZxv782j7oICHdNQ8AAnmhw7ugAlOF0g&oe=69DC4D93&_nc_sid=b41fef",
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
          "strong_id__": "284634734",
          "pk": 284634734,
          "pk_id": "284634734",
          "id": "284634734",
          "username": "disney",
          "full_name": "Disney",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3859143390382675003_284634734",
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/656558113_18577653481026735_1735858011052165396_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=HX8JmLcZS9cQ7kNvwHRH-cI&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCFIIievNH8ERwBCABTJRwGqARcYbmNDAQAB1501500j-ccb7-5&oh=00_Af3h4MZZfzjmSbalPMvP9F_r5Vs0L03I2QU48vgZQAGvuA&oe=69DC5A43&_nc_sid=b41fef",
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
    },
    {
      "pk": "3844732796656436386",
      "id": "3844732796656436386_787132",
      "code": "DVbPBu5AESi",
      "taken_at": "2026-03-03T15:00:04Z",
      "taken_at_ts": 1772550004,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwG4F5vT&_nc_oc=Ado2xX9Aq_Myu54ApiZkvwxrkm5T8dPp4H7NpQtw8i6WlGFiFY6Fmn5z0i_YIEvzO4g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af29VdU8lYk20RmNPNMpKbWsv9bGf7GdUvEUiQnyMadjOA&oe=69DC51CA",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1oUt1ISLpzLpLM6_XTIC7QFC0meaMhYfXpzUHRHnlucw&oe=69DC51E9&_nc_sid=b41fef",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 614,
      "comments_disabled": false,
      "like_count": 66069,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3OTqJ87vJqQzWseIGr0Ovau_qGt6UUW-W6QGOcHb-H6A&oe=69D848EB",
      "view_count": 0,
      "video_duration": 60.07400131225586,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            48270,
            96540,
            144811
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwG4F5vT&_nc_oc=Ado2xX9Aq_Myu54ApiZkvwxrkm5T8dPp4H7NpQtw8i6WlGFiFY6Fmn5z0i_YIEvzO4g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af29VdU8lYk20RmNPNMpKbWsv9bGf7GdUvEUiQnyMadjOA&oe=69DC51CA",
          "width": 750,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1607971,
          "height": 1280,
          "id": "1791310395606912v",
          "type": 101,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3OTqJ87vJqQzWseIGr0Ovau_qGt6UUW-W6QGOcHb-H6A&oe=69D848EB",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1607971,
          "height": 1280,
          "id": "1791310395606912v",
          "type": 102,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3OTqJ87vJqQzWseIGr0Ovau_qGt6UUW-W6QGOcHb-H6A&oe=69D848EB",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1607971,
          "height": 1280,
          "id": "1791310395606912v",
          "type": 103,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwF_hqOe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3OTqJ87vJqQzWseIGr0Ovau_qGt6UUW-W6QGOcHb-H6A&oe=69D848EB",
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
          "best_audio_cluster_id": "2285888061908806"
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
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "merchandising_pill_info": null,
        "music_canonical_id": "18531263347067949",
        "music_info": null,
        "nux_info": null,
        "original_sound_info": {
          "allow_creator_to_rename": true,
          "audio_asset_id": 26397325093213654,
          "attributed_custom_audio_asset_id": null,
          "can_remix_be_shared_to_fb": true,
          "can_remix_be_shared_to_fb_expansion": true,
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663872\" FBManifestIdentifier=\"FoDss50NKRb65a+KkPmzCSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwHIIuno&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1dOWbCYSe5nP9JgjeoTtzGH-VooMQ_ZQ9HDK6F_ZDFeg&amp;oe=69D86283</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "duration_in_ms": 60074,
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
          "original_media_id": 3844732796656436386,
          "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQOu1cJkIUYpfLz5hsq6b4bAI93Dsnj-0FVN5QJfDUtHrdxoyYljTBeDYR-FHSZ5LvVWtD_zp4sNL8fsO46SW16u.mp4?_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=zRv5taEP1NwQ7kNvwE22s8k&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0G21_m7YLmCskDQASGms06y7zKGcGPbQEl9LzdfGohlg&oe=69D8409F",
          "should_mute_audio": false,
          "time_created": 1772550012,
          "trend_rank": null,
          "previous_trend_rank": null,
          "overlap_duration_in_ms": 0,
          "audio_asset_start_time_in_ms": 0,
          "derived_content_start_time_in_composition_in_ms": 0,
          "ig_artist": {
            "strong_id__": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1oUt1ISLpzLpLM6_XTIC7QFC0meaMhYfXpzUHRHnlucw&oe=69DC51E9&_nc_sid=b41fef"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663872\" FBManifestIdentifier=\"FoDss50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZlsratODCzrQCgpGvuY7mpQPc6NjMprirBOCA5uCtu+YG+uWvipD5swmo0qnPweKbDKrMkpjEg4dcirnQvPLp4F2C8dTlwpDpXSIYGGRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsGRgFbGlnaHQAFkgUABIUAgA=\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1221425160198702v\" bandwidth=\"88841\" codecs=\"vp09.00.30.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"666981\" FBPlaybackResolutionMos=\"0:100,360:42.4,480:42.2,720:44.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:69.2,480:64.6,720:59.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"180p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMkUUBoVi_ub6duvm9o0zVD3FqHqNnfmFIIUyYMopmyOCFovt0jt7tT0MWjPJMry7gxFaH81JHTAu-3ZsBjAa08euE0JvQRfX8f4dA.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=j62NyMr0qVAQ7kNvwH_KDJR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjg4ODQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2YtiJ_ghYXUZMIn-oQ4DakIFAvpydubBe-WGLXysdDXA&amp;oe=69DC3B5B</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-6649\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-27353\" FBFirstSegmentRange=\"975-49463\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"49464-99920\" FBPrefetchSegmentRange=\"975-49463\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"678648151971493v\" bandwidth=\"131405\" codecs=\"vp09.00.30.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"986526\" FBPlaybackResolutionMos=\"0:100,360:52.6,480:51.3,720:52.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:79.2,480:74.7,720:68.5\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMTuYIt8uIN7FmfcNiMEmM088p1ojFhfWyppf1rCqdoRnEZjOBAVQKnl7tVDa0fwYoD97P-LJMcQtFCa_4zgosvXzmasUGqWrTn-sY.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=jFPdYIunJWIQ7kNvwGGnwcu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjEzMTQwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0bbV2JMXhTacyhkk_HarMVzvoMkhHu2ZA2-QRLot-STg&amp;oe=69DC4289</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-8510\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-38020\" FBFirstSegmentRange=\"975-66869\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"66870-139717\" FBPrefetchSegmentRange=\"975-66869\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"25911151711900437v\" bandwidth=\"184219\" codecs=\"vp09.00.30.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"1383031\" FBPlaybackResolutionMos=\"0:100,360:59.3,480:57.4,720:57.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86,480:82.2,720:76.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOa7vEXhZzWkoB91BY5wDbDQdoXHnkoGyd8Ns96jD4yd7jAWprXqb5mzrIbFoySj2dYDK3E-dzFtFEQeWiqb83bvc8K3aMox3Ayx80.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=cM_uL1WGyoQQ7kNvwHcKAvV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjE4NDIxOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af07RDEtgaxqbMjQ9J1fjLiuooN5ggPpKR98cvtwuP5K8g&amp;oe=69DC679A</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-10436\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-51508\" FBFirstSegmentRange=\"975-91478\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"91479-190792\" FBPrefetchSegmentRange=\"975-91478\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"1914169985908784v\" bandwidth=\"255147\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"1915519\" FBPlaybackResolutionMos=\"0:100,360:65.8,480:63.6,720:63.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.3,480:86.1,720:82.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN8qcFGph18DKn73VhWMnVPZOS1edh-4P60ufMg_K-9kKgeanK_-wqY-jkmYGto_BTysGZp9O7nBLVpuEs_b2c19AT4i-V9JciDMOY.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=-Ey_NjPUsO4Q7kNvwHsqqbL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjI1NTE0NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3DQwW_DPURXpJXE22oGrUF7cGqGM9AxwKInswMhiDJ3A&amp;oe=69DC39EC</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-13375\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-70737\" FBFirstSegmentRange=\"975-126204\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"126205-265560\" FBPrefetchSegmentRange=\"975-126204\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"3438765782938772v\" bandwidth=\"365520\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"2744149\" FBPlaybackResolutionMos=\"0:100,360:72.9,480:70.7,720:69.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.8,480:91.5,720:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO4qM-cNuoLnfZlUy_IiVAT2Z8qF4wrxqNpNVQglEAoWPC13m_tPg_VquKp8yGWLlyNwPMfnVScpHlWvfWhweLyg2_AGpj83oZwtcA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=J_ubYeNVjJoQ7kNvwHaAkoF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjM2NTUyMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af19YiGnlV0mRymUJAg8n47C0q1cf7APFIvl7Rz2W-c4_w&amp;oe=69DC688F</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-16766\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-100600\" FBFirstSegmentRange=\"975-179508\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"179509-376002\" FBPrefetchSegmentRange=\"975-179508\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"26408354118802497v\" bandwidth=\"508971\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"3821111\" FBPlaybackResolutionMos=\"0:100,360:77.8,480:75.7,720:74.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:94.6,720:92.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrD8S2IOYGSxcDRdQB0cAB4U_2mcQDXZdYVS3cDu_u_3CiV7RvCKeTHyc6Ei4ymT7PLdCW85vxrpSIQHl8ACI6dX49R5aLmoiBH24.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=0oJbYhI0MV4Q7kNvwEbFg8J&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjUwODk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1cb8OFBcLZWDdfdZyU4JC4jOsUqJFVRtNMhkv_6C1Dog&amp;oe=69DC576C</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-20846\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-140870\" FBFirstSegmentRange=\"975-255834\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"255835-524275\" FBPrefetchSegmentRange=\"975-255834\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"927543076447297v\" bandwidth=\"714491\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"5364051\" FBPlaybackResolutionMos=\"0:100,360:83.3,480:80.7,720:78.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.5,720:94.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNzuP-dxHHhCDOgE42W3DRgip3HC6kXW0Ky3-f5EEMINfKrpfaaxYyAaSB2Icf90jqmZr2q5J0Ve1sJqNkqV4OXkx9wDjN9W8yD_-A.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=rJolK-0juxQQ7kNvwG7DAOd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjcxNDQ5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0NC0yFLu2KsRXKjlHgDuw2yJWT2DnBkeuU1RvbW-hyuw&amp;oe=69DC46F9</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-26038\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-200467\" FBFirstSegmentRange=\"975-363535\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"363536-745087\" FBPrefetchSegmentRange=\"975-363535\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation><Representation id=\"26390098317282885v\" bandwidth=\"1089671\" codecs=\"vp09.00.31.08.00.02.02.02.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q90\" FBContentLength=\"8180714\" FBPlaybackResolutionMos=\"0:100,360:87.8,480:85.5,720:83.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.81,480:98.35,720:97.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOIpKrCiWGBk_joSA25fivPUcx8XxdxvYeXBRUehwR8r8vE5v_3nsJ6A1r--74ibf2AAtfFSX7nP0Ym2GccV3oDZOulvkHEUiMZ0Js.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=GWW-iUt-eaMQ7kNvwEPYENN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjEwODk2NzEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0CGagaw0O9JziquKpIXUadJb0HrLAwo8aX7voqxlXcng&amp;oe=69DC4E02</BaseURL><SegmentBase indexRange=\"799-974\" timescale=\"11988\" FBMinimumPrefetchRange=\"975-34968\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"975-311296\" FBFirstSegmentRange=\"975-565432\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"565433-1149907\" FBPrefetchSegmentRange=\"975-565432\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-798\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"537214\" FBPaqMos=\"90.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwHIIuno&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjcxNTM5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3oCEo_1F9mfHv81ggbRv_0690EkZhfIw7zeSQMs0VpNg&amp;oe=69D86283</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\" FBMinimumPrefetchRange=\"1228-1588\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1228-22518\" FBFirstSegmentRange=\"1228-18944\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"18945-36496\" FBPrefetchSegmentRange=\"1228-36496\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [
        {
          "strong_id__": "10506924608",
          "pk": 10506924608,
          "pk_id": "10506924608",
          "id": "10506924608",
          "username": "jamescameronofficial",
          "full_name": "James Cameron",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "1964371814524155358_10506924608",
          "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=TYSekVkP8Y0Q7kNvwEzpw-g&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af2k2cV5HKxQrklTSNCSXok9ovRCvrhbnzYWhK5Qe-iCfw&oe=69DC6398&_nc_sid=b41fef",
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
          "strong_id__": "1029649300",
          "pk": 1029649300,
          "pk_id": "1029649300",
          "id": "1029649300",
          "username": "natgeoanimals",
          "full_name": "National Geographic Animals",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865698702530758137_1029649300",
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=ic5ODsLE2O8Q7kNvwHES09N&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af05UegPM8QaR-IVdNHzZDDoWSL8H1Jlc-_QN1diWyUqKw&oe=69DC588C&_nc_sid=b41fef",
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
    },
    {
      "pk": "3870670793969876810",
      "id": "3870670793969876810_787132",
      "code": "DW3YpRVDb9K",
      "taken_at": "2026-04-08T10:00:01Z",
      "taken_at_ts": 1775642401,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFxQkBDINyzdIvAMcC-LjBo2gx3qQuBLvd4s-23es6q-EydTCx_FhRjC9UiPteKuWk&_nc_ohc=XbeNvhLXv28Q7kNvwG379KA&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1oUt1ISLpzLpLM6_XTIC7QFC0meaMhYfXpzUHRHnlucw&oe=69DC51E9&_nc_sid=b41fef",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 104,
      "comments_disabled": false,
      "like_count": 39842,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870670683399590370",
          "id": "3870670683399590370_787132",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af0z1UOvDMyAaP3P-8Usy7ALLH609dXUbqBABUkI31QXZw&oe=69DC4AFB",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                56778,
                113556,
                170335
              ],
              "height": 959,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af0z1UOvDMyAaP3P-8Usy7ALLH609dXUbqBABUkI31QXZw&oe=69DC4AFB",
              "width": 1439,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                27979,
                55958,
                83938
              ],
              "height": 500,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af2soxdKtVkoBJxpaXKO18X28rV9-21bJU60wXI8ddvQ0Q&oe=69DC4AFB",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870670793969876810_787132",
          "commerciality_status": "not_commercial",
          "taken_at": 1775642401
        },
        {
          "pk": "3870670679968669302",
          "id": "3870670679968669302_787132",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHUEQvY&_nc_oc=AdrTEh6bShOipdLW3jXQmv3DJ7nlLcBP7RD-RzH-xALHxcBSih6hvEUEaYTKbzZCsuo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af2R_SRn7osfYk7nv0Yl5S31dHdQjIXifGFRnDEdJkhuVw&oe=69DC54D1",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                40239,
                80479,
                120719
              ],
              "height": 959,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=104&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHUEQvY&_nc_oc=AdrTEh6bShOipdLW3jXQmv3DJ7nlLcBP7RD-RzH-xALHxcBSih6hvEUEaYTKbzZCsuo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af2R_SRn7osfYk7nv0Yl5S31dHdQjIXifGFRnDEdJkhuVw&oe=69DC54D1",
              "width": 1439,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                19829,
                39659,
                59488
              ],
              "height": 500,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=104&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHUEQvY&_nc_oc=AdrTEh6bShOipdLW3jXQmv3DJ7nlLcBP7RD-RzH-xALHxcBSih6hvEUEaYTKbzZCsuo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af2DAZtZTTqMsItrMUkdRu-gRjX5WYGu31kUMDEmzy-VNA&oe=69DC54D1",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870670793969876810_787132",
          "commerciality_status": "not_commercial",
          "taken_at": 1775642401
        },
        {
          "pk": "3870670694816531730",
          "id": "3870670694816531730_787132",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwGNLa1X&_nc_oc=AdqUd3B1Nnj5B8CwbTDFHK2mXqj5g49dmO2dtZHvh6ExyzXIdTwkmyejEE6AswbHreg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af2ww50iDxByZTFn9QuEdhT45dnNHwsKH8QcCOh45FdPpA&oe=69DC46CA",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                51971,
                103943,
                155915
              ],
              "height": 1080,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwGNLa1X&_nc_oc=AdqUd3B1Nnj5B8CwbTDFHK2mXqj5g49dmO2dtZHvh6ExyzXIdTwkmyejEE6AswbHreg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af2ww50iDxByZTFn9QuEdhT45dnNHwsKH8QcCOh45FdPpA&oe=69DC46CA",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                25599,
                51198,
                76797
              ],
              "height": 563,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwGNLa1X&_nc_oc=AdqUd3B1Nnj5B8CwbTDFHK2mXqj5g49dmO2dtZHvh6ExyzXIdTwkmyejEE6AswbHreg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af3G9TypHYiuc9DKTthpp5DJ0B-2iLigeAVBxK7rhmUJQw&oe=69DC46CA",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870670793969876810_787132",
          "commerciality_status": "not_commercial",
          "taken_at": 1775642401
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            56778,
            113556,
            170335
          ],
          "height": 959,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af0z1UOvDMyAaP3P-8Usy7ALLH609dXUbqBABUkI31QXZw&oe=69DC4AFB",
          "width": 1439,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            27979,
            55958,
            83938
          ],
          "height": 500,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGGdFxN&_nc_oc=AdpH4Ia791A9s5a1CG8SYKAQSM4oi4WE1CKiw863euSZW80k9dMBH4y5kBZwgpMKrb4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=4Wz1ttcOhaP1zxHS2ptwHw&_nc_ss=7a3ba&oh=00_Af2soxdKtVkoBJxpaXKO18X28rV9-21bJU60wXI8ddvQ0Q&oe=69DC4AFB",
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
  "3868170261056492782_787132"
]
```

</details>

---

### GET /v1/user/medias/pinned

Get user medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/medias/pinned?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_medias_pinned_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/medias/pinned",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/medias/pinned?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3865659729796199935",
    "id": "3865659729796199935_787132",
    "code": "DWllQsJCPX_",
    "taken_at": "2026-04-01T13:00:03Z",
    "taken_at_ts": 1775048403,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwEp0241&_nc_oc=AdovkTgm6WAVEMVch5zmy0Cv2M4CPWcTE1hq2mWHyIaf_YK3zJUccVWhem60kyVL10U&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af2VCsot92DrI44PxsqDn4g_MP7v-TRcVduWdgo5whyTqA&oe=69DC65F1",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=XbeNvhLXv28Q7kNvwHHKU1J&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3leXgZ8wptuDekiNCR5Y7VlJfCnga7n3VBpJ7-HY2NVg&oe=69DC51E9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 236,
    "comments_disabled": false,
    "like_count": 35858,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwFCQn07&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af17u5V2dTrXCeLAuzSjdaKDidV3p_thjyl6LmRVnRSreQ&oe=69D84A2E",
    "view_count": 0,
    "video_duration": 60.10100173950195,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          24827,
          49654,
          74482
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwEp0241&_nc_oc=AdovkTgm6WAVEMVch5zmy0Cv2M4CPWcTE1hq2mWHyIaf_YK3zJUccVWhem60kyVL10U&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af2VCsot92DrI44PxsqDn4g_MP7v-TRcVduWdgo5whyTqA&oe=69DC65F1",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 101,
        "url": "https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwFCQn07&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af17u5V2dTrXCeLAuzSjdaKDidV3p_thjyl6LmRVnRSreQ&oe=69D84A2E",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 102,
        "url": "https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwFCQn07&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af17u5V2dTrXCeLAuzSjdaKDidV3p_thjyl6LmRVnRSreQ&oe=69D84A2E",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 103,
        "url": "https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwFCQn07&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af17u5V2dTrXCeLAuzSjdaKDidV3p_thjyl6LmRVnRSreQ&oe=69D84A2E",
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
        "best_audio_cluster_id": "1378215947658482"
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
        "is_reuse_allowed": false,
        "mashup_type": null,
        "mashups_allowed": false,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18456784822103981",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26356368770680868,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.02S\" FBManifestTimestamp=\"1775663874\" FBManifestIdentifier=\"FoTss50NKRbkmJfH7/yMBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.02S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwE0cDon&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njc5NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af362BY6C4sWJlBNsuhMC4mqYtFKeFabsG5TJ1Lo9DQg-Q&amp;oe=69D873C7</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 60101,
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
        "original_media_id": 3865659729796199935,
        "progressive_download_url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQM3BWmWT9DCIR_4a6ETqY74iK_vSJ0mGCY5KURpD0ZI6aeamU2Fve1dXA5lCRBiztE1g_SEXMn_Iq_pDtwv8Zw.mp4?_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=3yv_Gp1gyOgQ7kNvwEr4aR3&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0ROYklmSEovDwu5Yggo5CmabmWp1rDHBM7LtPrTYEWfQ&oe=69D8476D",
        "should_mute_audio": false,
        "time_created": 1775048409,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=XbeNvhLXv28Q7kNvwHHKU1J&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3leXgZ8wptuDekiNCR5Y7VlJfCnga7n3VBpJ7-HY2NVg&oe=69DC51E9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.101685S\" FBManifestTimestamp=\"1775663874\" FBManifestIdentifier=\"FoTss50NGBBpZ19kYXNoX2Jhc2VsaW5lGTbcpo/P47C8BKaPqNH7tNQE5JiXx+/8jAYiGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABYOFAASFAIA\"><Period id=\"0\" duration=\"PT60.101685S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1258679306414510v\" bandwidth=\"1501640\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"11281389\" FBPlaybackResolutionMos=\"0:100,360:94.7,480:91.3,720:83.4,1080:75.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.21,480:96.8,720:94.4,1080:89.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/499\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=ZO8AcE1k9sEQ7kNvwFCQn07&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTUwMTY0MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af34mWtvrzrUNsj3KdK0omvsQZDv-82qtoNZhck4OwVvQw&amp;oe=69D84A2E</BaseURL><SegmentBase indexRange=\"893-1080\" timescale=\"11988\" FBMinimumPrefetchRange=\"1081-20619\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1081-452827\" FBFirstSegmentRange=\"1081-800082\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"800083-1560610\" FBPrefetchSegmentRange=\"1081-800082\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-892\"/></SegmentBase></Representation><Representation id=\"1311527807550419v\" bandwidth=\"327614\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"2461270\" FBPlaybackResolutionMos=\"0:100,360:70.9,480:64.9,720:56.1,1080:45.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:85.6,480:80,720:71.3,1080:60.7\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"11988/499\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQNl5Y1bVgI4X9t33UpT-w7ZjUpD9lolg43jM1c9ZSymAeyIP82ivdceULgFirMCivz2JuXhPWjcSx2nApS-e3pZuzy5Tc4T0B_V6cc.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=t6SGQgqnJ3MQ7kNvwEJL-hJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzI3NjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0fAQTidgQ-h5RkuPydgh6QdMzGsIJlw7lmjSiY26rz_w&amp;oe=69D850E7</BaseURL><SegmentBase indexRange=\"888-1075\" timescale=\"11988\" FBMinimumPrefetchRange=\"1076-7713\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1076-99076\" FBFirstSegmentRange=\"1076-177793\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"177794-323859\" FBPrefetchSegmentRange=\"1076-177793\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-887\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"501139\" FBPaqMos=\"88.19\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwE0cDon&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjY3OTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1oBz_OADpco-w3fmTjuHNh92Uudad6bcXieVj-_QacLg&amp;oe=69D873C7</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\" FBMinimumPrefetchRange=\"1228-1588\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1228-23446\" FBFirstSegmentRange=\"1228-20301\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"20302-37270\" FBPrefetchSegmentRange=\"1228-37270\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "18091046",
        "pk": 18091046,
        "pk_id": "18091046",
        "id": "18091046",
        "username": "natgeotv",
        "full_name": "National Geographic TV",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865691934048399589_18091046",
        "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=zov5ST0QeW4Q7kNvwENuCM3&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af29-SInOCynDjCPqRIWHgz_gh_bvyUCdaEk-wGFrIa2Nw&oe=69DC4D93&_nc_sid=b41fef",
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
        "strong_id__": "284634734",
        "pk": 284634734,
        "pk_id": "284634734",
        "id": "284634734",
        "username": "disney",
        "full_name": "Disney",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3859143390382675003_284634734",
        "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/656558113_18577653481026735_1735858011052165396_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=HX8JmLcZS9cQ7kNvwHZ3Yny&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCFIIievNH8ERwBCABTJRwGqARcYbmNDAQAB1501500j-ccb7-5&oh=00_Af3SRcWWX6kRPK-tDuG32oBN_a5z6kZAW9G4L7JC8AR7Vg&oe=69DC5A43&_nc_sid=b41fef",
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
  },
  {
    "pk": "3844732796656436386",
    "id": "3844732796656436386_787132",
    "code": "DVbPBu5AESi",
    "taken_at": "2026-03-03T15:00:04Z",
    "taken_at_ts": 1772550004,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwEOC7ON&_nc_oc=AdrGAm-1OPPZKPC05ltmEcbcpjQrQ9ZuVr80UperREXfLKeY-sZWW04NiqfSPkkXoxM&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af1mWrIneKYmYSNnse10Pm3fufsKH4ZH5eMqh7Mgr7qbuA&oe=69DC51CA",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=XbeNvhLXv28Q7kNvwHHKU1J&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3leXgZ8wptuDekiNCR5Y7VlJfCnga7n3VBpJ7-HY2NVg&oe=69DC51E9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 614,
    "comments_disabled": false,
    "like_count": 66069,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwH_cHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ3YXRjaF90aW1lX3MiOjI5MDY1NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af11s6iKfmdHlMhxuuMXxQhc5RET6_Iuwcft8L7SUFi0iQ&oe=69D848EB",
    "view_count": 0,
    "video_duration": 60.07400131225586,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          48270,
          96540,
          144811
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwEOC7ON&_nc_oc=AdrGAm-1OPPZKPC05ltmEcbcpjQrQ9ZuVr80UperREXfLKeY-sZWW04NiqfSPkkXoxM&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af1mWrIneKYmYSNnse10Pm3fufsKH4ZH5eMqh7Mgr7qbuA&oe=69DC51CA",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 101,
        "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwH_cHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ3YXRjaF90aW1lX3MiOjI5MDY1NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af11s6iKfmdHlMhxuuMXxQhc5RET6_Iuwcft8L7SUFi0iQ&oe=69D848EB",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 102,
        "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwH_cHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ3YXRjaF90aW1lX3MiOjI5MDY1NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af11s6iKfmdHlMhxuuMXxQhc5RET6_Iuwcft8L7SUFi0iQ&oe=69D848EB",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 103,
        "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwH_cHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ3YXRjaF90aW1lX3MiOjI5MDY1NzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af11s6iKfmdHlMhxuuMXxQhc5RET6_Iuwcft8L7SUFi0iQ&oe=69D848EB",
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
        "best_audio_cluster_id": "2285888061908806"
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
        "is_reuse_allowed": false,
        "mashup_type": null,
        "mashups_allowed": false,
        "mashups_allowed_for_carousel": false,
        "non_privacy_filtered_mashups_media_count": 0,
        "privacy_filtered_mashups_media_count": null,
        "original_media": null
      },
      "merchandising_pill_info": null,
      "music_canonical_id": "18531263347067949",
      "music_info": null,
      "nux_info": null,
      "original_sound_info": {
        "allow_creator_to_rename": true,
        "audio_asset_id": 26397325093213654,
        "attributed_custom_audio_asset_id": null,
        "can_remix_be_shared_to_fb": true,
        "can_remix_be_shared_to_fb_expansion": true,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663874\" FBManifestIdentifier=\"FoTss50NKRb65a+KkPmzCSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwF8yxBy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0wmbHrq-yN9h_jykiogh5NnCmyFzDUKKVd9RYYlg84EQ&amp;oe=69D86283</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "duration_in_ms": 60074,
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
        "original_media_id": 3844732796656436386,
        "progressive_download_url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOu1cJkIUYpfLz5hsq6b4bAI93Dsnj-0FVN5QJfDUtHrdxoyYljTBeDYR-FHSZ5LvVWtD_zp4sNL8fsO46SW16u.mp4?_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=zRv5taEP1NwQ7kNvwE7X4F-&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2CCQJVd_5UiHSFB3iern6lpWbgjaH_P2TUap8AY6uqSA&oe=69D8409F",
        "should_mute_audio": false,
        "time_created": 1772550012,
        "trend_rank": null,
        "previous_trend_rank": null,
        "overlap_duration_in_ms": 0,
        "audio_asset_start_time_in_ms": 0,
        "derived_content_start_time_in_composition_in_ms": 0,
        "ig_artist": {
          "strong_id__": "787132",
          "pk": 787132,
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=XbeNvhLXv28Q7kNvwHHKU1J&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3leXgZ8wptuDekiNCR5Y7VlJfCnga7n3VBpJ7-HY2NVg&oe=69DC51E9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663874\" FBManifestIdentifier=\"FoTss50NGBBpZ19kYXNoX2Jhc2VsaW5lGTbwnqDz8N3RBICegL3+y64G+uWvipD5swkiGBhkYXNoX2xuX2hlYWFjX3ZicjNfYXVkaW8iLBkYBWxpZ2h0ABZIFAASFAIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1791310395606912v\" bandwidth=\"1536432\" codecs=\"avc1.64001f\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_1_v1\" FBContentLength=\"11534763\" FBPlaybackResolutionMos=\"0:100,360:97.3,480:96,720:92.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.378,480:98.8,720:97.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/499\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=yD3DtfJ9jaEQ7kNvwH_cHm9&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfMV92MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsIndhdGNoX3RpbWVfcyI6MjkwNjU3OSwiYml0cmF0ZSI6MTUzNjQzMiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2X_a9yaU-ih72Ir5NmRnz6U7QSD1DTItOtbTKGvlYh9Q&amp;oe=69D848EB</BaseURL><SegmentBase indexRange=\"868-1043\" timescale=\"11988\" FBMinimumPrefetchRange=\"1044-47453\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1044-444876\" FBFirstSegmentRange=\"1044-774661\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"774662-1666091\" FBPrefetchSegmentRange=\"1044-774661\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-867\"/></SegmentBase></Representation><Representation id=\"1305633671612344v\" bandwidth=\"335944\" codecs=\"avc1.4d001e\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_baseline_3_v1\" FBContentLength=\"2522102\" FBPlaybackResolutionMos=\"0:100,360:71.8,480:65.9,720:57.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:86.5,480:81,720:72.7\" FBAbrPolicyTags=\"\" width=\"360\" height=\"640\" frameRate=\"11988/499\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQNWTdXLBEIYzSj60Rvfu84VjI_Qr77GPLV594CFoA1UnuhWcmswgNMC-LsGnvhd17n6gEvCq7PEdkB2JYNyq6_gwdF_m3dlflPmMzE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=zf-YewhdB80Q7kNvwHQ8CtE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYmFzZWxpbmVfM192MSIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsIndhdGNoX3RpbWVfcyI6MjkwNjU3OSwiYml0cmF0ZSI6MzM1OTQ0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Y6ZTkxORxtEhIOW6hYdrXdwNTD5T9HLELRQbj1Q7Jtg&amp;oe=69D84192</BaseURL><SegmentBase indexRange=\"865-1040\" timescale=\"11988\" FBMinimumPrefetchRange=\"1041-14488\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1041-91675\" FBFirstSegmentRange=\"1041-169661\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"169662-357062\" FBPrefetchSegmentRange=\"1041-169661\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-864\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_ln_heaac_vbr3_audio\" FBContentLength=\"537214\" FBPaqMos=\"90.07\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwF8yxBy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsIndhdGNoX3RpbWVfcyI6MjkwNjU3OSwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0tIFaq1hmY1UjIr_qRvOQcqDXUDTgAjw1qBw3siVB9kw&amp;oe=69D86283</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\" FBMinimumPrefetchRange=\"1228-1588\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1228-22518\" FBFirstSegmentRange=\"1228-18944\" FBFirstSegmentDuration=\"2027\" FBSecondSegmentRange=\"18945-36496\" FBPrefetchSegmentRange=\"1228-36496\" FBPrefetchSegmentDuration=\"4032\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [
      {
        "strong_id__": "10506924608",
        "pk": 10506924608,
        "pk_id": "10506924608",
        "id": "10506924608",
        "username": "jamescameronofficial",
        "full_name": "James Cameron",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "1964371814524155358_10506924608",
        "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=TYSekVkP8Y0Q7kNvwHT1z6W&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af01oTlJdci8zCNWZ9OBVbHjPckb5fuICkc4fgi5x-J1_w&oe=69DC6398&_nc_sid=b41fef",
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
        "strong_id__": "1029649300",
        "pk": 1029649300,
        "pk_id": "1029649300",
        "id": "1029649300",
        "username": "natgeoanimals",
        "full_name": "National Geographic Animals",
        "is_private": false,
        "is_verified": true,
        "profile_pic_id": "3865698702530758137_1029649300",
        "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=ic5ODsLE2O8Q7kNvwEGHxhQ&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af0zjQ2IMfdgEAsHbfwXbsu041FKMX_zAEkmqvpLIF7R5Q&oe=69DC588C&_nc_sid=b41fef",
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
  },
  {
    "pk": "3870670793969876810",
    "id": "3870670793969876810_787132",
    "code": "DW3YpRVDb9K",
    "taken_at": "2026-04-08T10:00:01Z",
    "taken_at_ts": 1775642401,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFvP__q3WGKmfy05ow_404oJlTQ_FrtOjwYMFG8V4fev4ocmUT7mIsLNB-Xs7Yxse8&_nc_ohc=XbeNvhLXv28Q7kNvwHHKU1J&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3leXgZ8wptuDekiNCR5Y7VlJfCnga7n3VBpJ7-HY2NVg&oe=69DC51E9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 104,
    "comments_disabled": false,
    "like_count": 39843,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870670683399590370",
        "id": "3870670683399590370_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwFY29_b&_nc_oc=AdrLP4iKrJAF4r4yHOPW2QS1OsZssr1HUAnM2asLpzfsyR3OvQVEsWda4EpFY6EYRM4&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0I5xXw2u5VNmlQqDlqA3cOMyDBIR0eY8DYPkrVIgDU5A&oe=69DC4AFB",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              56778,
              113556,
              170335
            ],
            "height": 959,
            "scans_profile": "e35",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwFY29_b&_nc_oc=AdrLP4iKrJAF4r4yHOPW2QS1OsZssr1HUAnM2asLpzfsyR3OvQVEsWda4EpFY6EYRM4&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0I5xXw2u5VNmlQqDlqA3cOMyDBIR0eY8DYPkrVIgDU5A&oe=69DC4AFB",
            "width": 1439,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              27979,
              55958,
              83938
            ],
            "height": 500,
            "scans_profile": "e35",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwFY29_b&_nc_oc=AdrLP4iKrJAF4r4yHOPW2QS1OsZssr1HUAnM2asLpzfsyR3OvQVEsWda4EpFY6EYRM4&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0WE3TL7im8cl9HJnN_Y9ad1uE9DNvUFeBJ7Mu8mvoWHQ&oe=69DC4AFB",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      },
      {
        "pk": "3870670679968669302",
        "id": "3870670679968669302_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwE6AjPP&_nc_oc=AdrZTKvS4qQG97HfE5JypO50eJMxEvd8S6mlLrnKTeOAKI-8i2fDFT14XkmL39aNzyw&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af3uDvQSJ-4KeApw8ZFqeZgytkXxgQF0-MNuWg3g1maOIw&oe=69DC54D1",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              40239,
              80479,
              120719
            ],
            "height": 959,
            "scans_profile": "e35",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwE6AjPP&_nc_oc=AdrZTKvS4qQG97HfE5JypO50eJMxEvd8S6mlLrnKTeOAKI-8i2fDFT14XkmL39aNzyw&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af3uDvQSJ-4KeApw8ZFqeZgytkXxgQF0-MNuWg3g1maOIw&oe=69DC54D1",
            "width": 1439,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              19829,
              39659,
              59488
            ],
            "height": 500,
            "scans_profile": "e35",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwE6AjPP&_nc_oc=AdrZTKvS4qQG97HfE5JypO50eJMxEvd8S6mlLrnKTeOAKI-8i2fDFT14XkmL39aNzyw&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af130d7qt7WerL1bYYg80mmJAnX-uJfW25yiPsz-DPV4RA&oe=69DC54D1",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      },
      {
        "pk": "3870670694816531730",
        "id": "3870670694816531730_787132",
        "video_url": null,
        "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwEyuUgs&_nc_oc=AdrVcMo3rsbUsb1KSM-7BO1yCpcEK4rJ_RHN4YUyb7X8nrIFDM97x59D-HLBVaEAv4g&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0b8xHNmkhWrmi1MRbUDUuxRD_kO_TUrXyP2EEbDFv4ag&oe=69DC46CA",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              51971,
              103943,
              155915
            ],
            "height": 1080,
            "scans_profile": "e35",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwEyuUgs&_nc_oc=AdrVcMo3rsbUsb1KSM-7BO1yCpcEK4rJ_RHN4YUyb7X8nrIFDM97x59D-HLBVaEAv4g&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0b8xHNmkhWrmi1MRbUDUuxRD_kO_TUrXyP2EEbDFv4ag&oe=69DC46CA",
            "width": 1440,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              25599,
              51198,
              76797
            ],
            "height": 563,
            "scans_profile": "e35",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwEyuUgs&_nc_oc=AdrVcMo3rsbUsb1KSM-7BO1yCpcEK4rJ_RHN4YUyb7X8nrIFDM97x59D-HLBVaEAv4g&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0FNIUphNhjutzBXWQfeu8J-u8Rgy2a5m5VKzSA8vc1Mg&oe=69DC46CA",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870670793969876810_787132",
        "commerciality_status": "not_commercial",
        "taken_at": 1775642401
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          56778,
          113556,
          170335
        ],
        "height": 959,
        "scans_profile": "e35",
        "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwFY29_b&_nc_oc=AdrLP4iKrJAF4r4yHOPW2QS1OsZssr1HUAnM2asLpzfsyR3OvQVEsWda4EpFY6EYRM4&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0I5xXw2u5VNmlQqDlqA3cOMyDBIR0eY8DYPkrVIgDU5A&oe=69DC4AFB",
        "width": 1439,
        "is_spatial_image": false
      },
      {
        "estimated_scans_sizes": [
          27979,
          55958,
          83938
        ],
        "height": 500,
        "scans_profile": "e35",
        "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwFY29_b&_nc_oc=AdrLP4iKrJAF4r4yHOPW2QS1OsZssr1HUAnM2asLpzfsyR3OvQVEsWda4EpFY6EYRM4&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=RUfsCcEoSHwTKZ_ln_eGkQ&_nc_ss=7a3ba&oh=00_Af0WE3TL7im8cl9HJnN_Y9ad1uE9DNvUFeBJ7Mu8mvoWHQ&oe=69DC4AFB",
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

### GET /v1/user/search/followers

Search users by followers. Returns matching User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `query` | string | Yes | Query |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/search/followers?user_id=787132&query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_search_followers_v1(user_id="787132", query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/search/followers",
        headers=headers,
        params={"user_id": "787132", "query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/search/followers?user_id=787132&query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "69025436922",
    "id": "69025436922",
    "username": "pedroqduarte",
    "full_name": "Pedro Duarte",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.2885-19/491416168_662266566416516_4619764470022606481_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MjAuYzIifQ&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gF4GyeYnTVQ2YKG2CZ-mLkOHDpzf-cCMvIlpGPHsS12CsGSoJ8pGFbBcDFGIgvEA1o&_nc_ohc=J452D13OposQ7kNvwFBmS6U&_nc_gid=8AjY95ivEK0UMcFe1oCl_A&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GGhqSh2EGHDzU1oCAJEOqxVPsxxAbkULAAAB1501500j-ccb7-5&oh=00_Af2rBckat1U03LmLggFy8Neu2JXpyEZhcTKcDHtdwpxMhw&oe=69DC5FDF&_nc_sid=6ff7c8",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "43374964307",
    "id": "43374964307",
    "username": "postedbynj",
    "full_name": "",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/658260017_18063616745444308_1491397800595950837_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gF4GyeYnTVQ2YKG2CZ-mLkOHDpzf-cCMvIlpGPHsS12CsGSoJ8pGFbBcDFGIgvEA1o&_nc_ohc=Qs_lKy2sErgQ7kNvwEMh0Qy&_nc_gid=8AjY95ivEK0UMcFe1oCl_A&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GDFAPCfUk3iDwyxAAPUMUttlgrIUbmNDAQAB1501500j-ccb7-5&oh=00_Af27qnlCmg_bv3p2mjU5O2JLuQVu5eKSpPai4mbaMuETNQ&oe=69DC35EE&_nc_sid=6ff7c8",
    "is_private": false,
    "is_verified": false
  },
  {
    "pk": "35814620919",
    "id": "35814620919",
    "username": "praguosphere",
    "full_name": "PRAGUOSPHERE",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/660140245_18074573600196920_3208973545650305425_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gF4GyeYnTVQ2YKG2CZ-mLkOHDpzf-cCMvIlpGPHsS12CsGSoJ8pGFbBcDFGIgvEA1o&_nc_ohc=N0ogvpr6pBAQ7kNvwFg4vXu&_nc_gid=8AjY95ivEK0UMcFe1oCl_A&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GNXwWCc4CeiaujZAAJG5HBpwkIgsbmNDAQAB1501500j-ccb7-5&oh=00_Af2tjaDNrtClQBYh1Mx5QFNq83RcmbPeibzpt8E_7wBtBw&oe=69DC549C&_nc_sid=6ff7c8",
    "is_private": false,
    "is_verified": false
  }
]
```

</details>

---

### GET /v1/user/search/following

Search users by following users. Returns matching User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `query` | string | Yes | Query |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/search/following?user_id=787132&query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_search_following_v1(user_id="787132", query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/search/following",
        headers=headers,
        params={"user_id": "787132", "query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/search/following?user_id=787132&query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "23947096",
    "id": "23947096",
    "username": "natgeotravel",
    "full_name": "National Geographic Travel",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFqPkcPNucfxgL0R81kNyjRgT43BEFBjspsSOgXtSln73N4MKZqhYIBEMQuXAGrTDo&_nc_ohc=t-DCVZxwtX4Q7kNvwHArQzp&_nc_gid=0qnTeGc0RcUW5ugjP4eHCA&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af33aJLqVpbUErzspVeUqOFzoiUZJ4Mvteasww1W4VoKWg&oe=69DC6746&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "1029649300",
    "id": "1029649300",
    "username": "natgeoanimals",
    "full_name": "National Geographic Animals",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFqPkcPNucfxgL0R81kNyjRgT43BEFBjspsSOgXtSln73N4MKZqhYIBEMQuXAGrTDo&_nc_ohc=ic5ODsLE2O8Q7kNvwEppRvt&_nc_gid=0qnTeGc0RcUW5ugjP4eHCA&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af06Fz27CksQ5ngDdCjr3f7Xab8ob9T_3BH6_ZPlyAPzog&oe=69DC588C&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "414805671",
    "id": "414805671",
    "username": "natgeoscience",
    "full_name": "National Geographic Science",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/658043965_18575534785021672_4145157128631909093_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFqPkcPNucfxgL0R81kNyjRgT43BEFBjspsSOgXtSln73N4MKZqhYIBEMQuXAGrTDo&_nc_ohc=ocufCJtUTR4Q7kNvwHCAiZ1&_nc_gid=0qnTeGc0RcUW5ugjP4eHCA&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GD30OCfoxl_4Wf5BAOV6SE5yjoY5bmNDAQAB1501500j-ccb7-5&oh=00_Af2SKF_AstIWpJtgHbs_vGaKmxk4YZidAFZ7O_P24l7nHg&oe=69DC3785&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": true
  }
]
```

</details>

---

### GET /v1/user/tag/medias

Prefer to use /v2/user/tag/medias

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/tag/medias?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/tag/medias",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/tag/medias?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/user/tag/medias/chunk

Get usertag medias

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/tag/medias/chunk?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_tag_medias_chunk_v1(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/tag/medias/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/tag/medias/chunk?user_id=787132",
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
      "pk": "1929261108986102451",
      "id": "1929261108986102451_429173",
      "code": "BrGHMHIF8Kz",
      "taken_at": "2018-12-07T18:04:27Z",
      "taken_at_ts": 1544205867,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwE3BwDT&_nc_oc=AdpS5LyvNOpvB-zDLyLJlRJFDkqXygvQ4bvaX1CX7rXetEMKIML_Uu2li5lAJvAB4_I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af2oFnCeYM-n2J52qUDCBCvpSC9h83LfXlpdXuAvBkJKbA&oe=69DC6562",
      "location": {
        "pk": 250376789,
        "name": "Vardzia, Aspindzis Raioni, Georgia",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 43.2575,
        "lat": 41.3753,
        "external_id": "109068119127535",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "429173",
        "id": "429173",
        "username": "hynecheck",
        "full_name": "Hynek Hampl",
        "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/427378186_275046522125863_1224244213859159903_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43ODUuYzIifQ&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=Bb5J40vuSOQQ7kNvwE04Rfv&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GApGeRknfj9CJ-oAAF8PZ02gY-0QbkULAAAB1501500j-ccb7-5&oh=00_Af0Zgpd7f1HjGlJRIoLJQafraQSajGNKtmRIEPWJagWdWw&oe=69DC51BA&_nc_sid=a8b8e2",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 579,
      "comments_disabled": false,
      "like_count": 14016,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Vardzia is a cave monastery site located in southern Georgia. It is excavated from the slopes of the Erusheti Mountain on the left side of the Kura River. Oh Georgia, I miss you when I look at these images 😭 #georgia #exploregeorgia #MavicPro\n.\n.\n.\n.\n.\n#mymavic #awesome_earthpix #collectivelycreate #exploretocreate #livefolk #beautifuldestinations #iglifecz #folkcreative #exklusive_shot #AGameOfTones #igerscz #discoverglobe #QueekyGrams #ourplanetdaily #adventureculture #welivetoexplore #stayandwander #dnescestujem #droneofficial #droneoftheday #dronesdaily #dji #fromwhereidrone #earthofficial #natgeo #MavicPro @beautifuldestinations @roamtheplanet @earthofficial @earthpix @folkmagazine @liveoutdoor.s @awesomeglobe @awesome.earth @djiglobal @fromwhereidrone @dronestagr.am @droneoftheday @droneofficial @earthstoke @livefolk @global_hotshotz @vzcomood @artofvisuals @majestic_earth_ @folkvibe @welivetoexplore @lastingvisuals @mountainsphoto @theglobewanderer @tentree @awesome.earth @awesomeglobe @ourplanetdaily",
      "accessibility_caption": null,
      "usertags": [
        {
          "user": {
            "pk": "1709655155",
            "id": "1709655155",
            "username": "fromwhereidrone",
            "full_name": "From Where I Drone®",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/11426732_990789794299104_1839082617_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=Nk9rpOO4FmUQ7kNvwFU21zS&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GKxbrgDgfLw5HoUDAHksnm0AAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af2hZBx3Jh0URPcuwkJvI3IPV5pUAVupHEPcARfpAKe9Sg&oe=69DC3E73&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": false
          },
          "x": 0.9639999866000001,
          "y": 0.0160000008
        },
        {
          "user": {
            "pk": "195270438",
            "id": "195270438",
            "username": "wonderful_places",
            "full_name": "Wonderful Places",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/487340431_1510016599961079_422634517629355178_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=seU08ayHeVsQ7kNvwFDraN4&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GI85DB33rQsjWl0FAKrEHcXaf90FbkULAAAB1501500j-ccb7-5&oh=00_Af33iJy05Zrp7OwSaSAaqMkPdqQ3PP0H2XDBZURWlf03UQ&oe=69DC556A&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.8700000048000001,
          "y": 0.0496000014
        },
        {
          "user": {
            "pk": "2280748136",
            "id": "2280748136",
            "username": "droneofficial",
            "full_name": "droneofficial™",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/468337925_1583355895611127_2678160184603292032_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=1sUi-nQ8MMwQ7kNvwHFdzoy&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GAVF6hv3-rXFDaAFAICx35Z-vColbkULAAAB1501500j-ccb7-5&oh=00_Af1oZTOVaJmaakO26w-NVpE-lXjvJoFtNmAwNKJLgqBKxw&oe=69DC34E0&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": false
          },
          "x": 0.9319999814000001,
          "y": 0.0912000015
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
            50179,
            100358,
            150537
          ],
          "height": 1334,
          "scans_profile": "e35",
          "url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwE3BwDT&_nc_oc=AdpS5LyvNOpvB-zDLyLJlRJFDkqXygvQ4bvaX1CX7rXetEMKIML_Uu2li5lAJvAB4_I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af2oFnCeYM-n2J52qUDCBCvpSC9h83LfXlpdXuAvBkJKbA&oe=69DC6562",
          "width": 1080,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            33759,
            67518,
            101277
          ],
          "height": 926,
          "scans_profile": "e35",
          "url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwE3BwDT&_nc_oc=AdpS5LyvNOpvB-zDLyLJlRJFDkqXygvQ4bvaX1CX7rXetEMKIML_Uu2li5lAJvAB4_I&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af3j2pQygqraqrKqrPwdLx-SFIpmohfMWLOPARmwj2KeBw&oe=69DC6562",
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
      "pk": "1929229904589027835",
      "id": "1929229904589027835_276524869",
      "code": "BrGAGBxFvn7",
      "taken_at": "2018-12-07T17:02:28Z",
      "taken_at_ts": 1544202148,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwE_OMWV&_nc_oc=Adrn78vAI3s3aongkWKz1XTPOmIWvLOZowoKTspTma2gymZqoRR21ooYMbteiKX3Njs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af0z1NJSjjXqKoVyatJo2j-8rUM0ZBGvpI_FvX7HMFmOUw&oe=69DC4804",
      "location": {
        "pk": 1141278516000361,
        "name": "Tàu Cát Bà Xanh",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "Số 235 , đường Cái Bèo ",
        "city": "",
        "zip": null,
        "lng": 107.05010223359,
        "lat": 20.724692987102,
        "external_id": "1141278516000361",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "276524869",
        "id": "276524869",
        "username": "samuellemieux",
        "full_name": "Samuel Lemieux",
        "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/460602681_1286701775682716_7443510089900581929_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NTguYzIifQ&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=Enb1_W-dnWUQ7kNvwEPZtEw&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GDk9dBucfEWaP5IEAClkj0b9qExnbkULAAAB1501500j-ccb7-5&oh=00_Af3YGsHxQPHuR2YtJ-T412zdiwAHnti9NAkJDCGZCRh2fQ&oe=69DC36EC&_nc_sid=a8b8e2",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 182,
      "comments_disabled": false,
      "like_count": 6172,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "No helmet needed once your on Cát Bà Island.\n.\nCát Bà Island || Vietnam\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nShot on EOS T3i and SIGMA 85mm F1.4 EX DG HSM\nISO 100 | f/1.4 | 1/2000\n——\n#vietnam #vietnamese #vietnamesefood #vietnamflashback #vietnamesegirl #vietnamtravel #vietnamtrip #vietnamesehair #vietnamwar #vietnamesecuisine #vietnamflashbacks #vietnamesecoffee #vietnamfood #Canon #canonphotography #canonphoto #canon6d #canoneos #canonusa #canon70d #canon5dmarkiii #canon5d #canonaustralia #canonphotos #canon7d #canon60d #canon700d #canon5dmarkiv #canonphotographer #canoncanada",
      "accessibility_caption": null,
      "usertags": [
        {
          "user": {
            "pk": "1029649300",
            "id": "1029649300",
            "username": "natgeoanimals",
            "full_name": "National Geographic Animals",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=ic5ODsLE2O8Q7kNvwEc_tV0&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2USGHb8vBg3n7CZuDTf6jujp83YVyxPvAH63vAONf6SA&oe=69DC588C&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.5,
          "y": 0.5
        },
        {
          "user": {
            "pk": "1315608830",
            "id": "1315608830",
            "username": "canonusa",
            "full_name": "Canon USA",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-19/525764789_18523595374024831_4665287119118685063_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NjcuYzIifQ&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=tshhWSqzMN4Q7kNvwFvZP2b&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GLWIVh9-WDuiHM9BAIdTRsbqbb5AbmNDAQAB1501500j-ccb7-5&oh=00_Af1z5dWOAOmwS-R4ZhByZlHi1wTMei97yrhvPe3CYb_RMg&oe=69DC41A3&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.5,
          "y": 0.5
        },
        {
          "user": {
            "pk": "1364955209",
            "id": "1364955209",
            "username": "travelawesome",
            "full_name": "TRAVEL AWESOME",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/10175116_700926226628139_537225696_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=ErU9paF0HF0Q7kNvwE5mhsW&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GIxCmwArfsAafX0CAOBpBSAAAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af0qEGt9RXmgId3MUo68t5sXTCAkxj7GwPrpJusAtnMdBw&oe=69DC3FE3&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": false
          },
          "x": 0.5,
          "y": 0.5
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
            16232,
            32464,
            48696
          ],
          "height": 720,
          "scans_profile": "e35",
          "url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwE_OMWV&_nc_oc=Adrn78vAI3s3aongkWKz1XTPOmIWvLOZowoKTspTma2gymZqoRR21ooYMbteiKX3Njs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af0z1NJSjjXqKoVyatJo2j-8rUM0ZBGvpI_FvX7HMFmOUw&oe=69DC4804",
          "width": 1080,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            10923,
            21846,
            32769
          ],
          "height": 500,
          "scans_profile": "e35",
          "url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwE_OMWV&_nc_oc=Adrn78vAI3s3aongkWKz1XTPOmIWvLOZowoKTspTma2gymZqoRR21ooYMbteiKX3Njs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af2czjeV49MrkdWU1zzDNSltp9S7nzKnSHhGGQufBQUX6A&oe=69DC4804",
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
      "pk": "1929198769279088926",
      "id": "1929198769279088926_1423130965",
      "code": "BrF5A8wADke",
      "taken_at": "2018-12-07T16:00:36Z",
      "taken_at_ts": 1544198436,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwHz-fqv&_nc_oc=AdpJ_EtCFmhtnQWUa9VK8n6z-LPmrSdXxYK-srX5KAIwuzIh0DOnHCV46olEu1y4w4w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af3OOS9GuPR-jS_LqphBjiSYq4rWEW3PMQPtg0FggDFXyQ&oe=69DC6737",
      "location": {
        "pk": 109714185714936,
        "name": "Florida",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": -81.631666666667,
        "lat": 28.133333333333,
        "external_id": "109714185714936",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "1423130965",
        "id": "1423130965",
        "username": "canusatouristik",
        "full_name": "CANUSA TOURISTIK 🇺🇸 & 🇨🇦",
        "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/205154326_1843163085845566_6652282020977594618_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDAwLmMyIn0&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=4Co_t95in6EQ7kNvwGm4joF&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GBZoOgw_tP7YWIwGAPpQFrZAp1FcbkULAAAB1501500j-ccb7-5&oh=00_Af05SM7SrLyj66gh93MC9LFiJiRlU9GYQ16cqlEhImbnAg&oe=69DC5283&_nc_sid=a8b8e2",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 204,
      "comments_disabled": false,
      "like_count": 5581,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "☀️Warme Sonnenstrahlen, herrliche Seeluft und weicher Sandstrand - erlebt den ewigen Sommer in Florida😍 Die rund 700 Kilometer lange Landzunge zwischen dem Atlantik und dem Golf von Mexiko wird auch Sunshine State genannt und wird seinem Namen auf jeden Fall gerecht - rund 300 Sonnentage im Jahr kann man in dem US-Bundeststaat genießen.🏝#mycanusa #sunshinestate #visitflorida #florida #exploremore #visittheusa",
      "accessibility_caption": null,
      "usertags": [
        {
          "user": {
            "pk": "20388776",
            "id": "20388776",
            "username": "visittheusa",
            "full_name": "Visit The USA",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/491438798_18500574025036777_282017071777073097_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=iCn6e-hArvwQ7kNvwHD5sTt&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GM7CSh3pM_eOLLpBAMlH3lcI7ekDbvEnAQAB1501500j-ccb7-5&oh=00_Af3GMFIK3J0lyQ8hlqtJMS7JyjiAhJMWQ5mo8qUQ25cmHQ&oe=69DC5871&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.4499999881,
          "y": 0.5911949873
        },
        {
          "user": {
            "pk": "28867825",
            "id": "28867825",
            "username": "visitflorida",
            "full_name": "VISITFLORIDA",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-19/539584343_18524625733003826_8708481332788290688_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43OTYuYzIifQ&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=jHwtv1i8lr8Q7kNvwGty5xn&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GFdnKSAyqmmIDNBBAIBk9-Whvdp4bmNDAQAB1501500j-ccb7-5&oh=00_Af3tW7lvVO2OUk4sn7xKt-Hr9rB-ybc6cSmhc68hqpOD2Q&oe=69DC31A7&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.7916666865,
          "y": 0.6509433985
        },
        {
          "user": {
            "pk": "57636",
            "id": "57636",
            "username": "lonelyplanet",
            "full_name": "Lonely Planet",
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/264061680_892373304802999_2303500327805762813_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zNjAuYzIifQ&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFBjGzdiqoySXMo8Plg6dVGJ6HOSlJnai11etwix0jENHhhnl_v98qpT1bkF-t_Zpg&_nc_ohc=EUO-NceyQRAQ7kNvwFxGt49&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GPBCvQ_3-tbZmysDAP282-pXrfcfbkULAAAB1501500j-ccb7-5&oh=00_Af2MMRe5mTex7KLEOk9AC_6NpKvedOnPfkE8GkdNEo5G3g&oe=69DC48AB&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.5124999881,
          "y": 0.267295599
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
            25149,
            50299,
            75448
          ],
          "height": 716,
          "scans_profile": "e35",
          "url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwHz-fqv&_nc_oc=AdpJ_EtCFmhtnQWUa9VK8n6z-LPmrSdXxYK-srX5KAIwuzIh0DOnHCV46olEu1y4w4w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af3OOS9GuPR-jS_LqphBjiSYq4rWEW3PMQPtg0FggDFXyQ&oe=69DC6737",
          "width": 1080,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            16919,
            33839,
            50759
          ],
          "height": 497,
          "scans_profile": "e35",
          "url": "https://scontent-ber1-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwHz-fqv&_nc_oc=AdpJ_EtCFmhtnQWUa9VK8n6z-LPmrSdXxYK-srX5KAIwuzIh0DOnHCV46olEu1y4w4w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_gid=xIZlu95bkVZ3dgdZ-Cq-Ow&_nc_ss=7a3ba&oh=00_Af0TnOKYGmkxvgbsAoYl8kSwyYnUzoUkAnjnKFsqbv0-gg&oe=69DC6737",
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
  "1926933891264902156"
]
```

</details>

---

### GET /v1/user/videos

Get user videos

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/videos?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/videos",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/videos?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/user/videos/chunk

Get part of user videos with cursor (default 50 media per request)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/videos/chunk?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/videos/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/videos/chunk?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/user/web_profile_info

WARNING: Deprecated. Instagram returns ~90% false UserNotFound since Feb 2, 2026. Use /gql/user/web_profile_info instead (accepts numeric user ID, much more reliable).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/user/web_profile_info?username=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/user/web_profile_info",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/user/web_profile_info?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-user){ target=_blank }
