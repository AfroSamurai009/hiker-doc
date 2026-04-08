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
  "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwDcIE2z_RBh7yGRBOAiKq4yN-YnTJGMP_KjzLVrIxjjG36RjTnbeWKcWsxnkWoBQ&_nc_ohc=XbeNvhLXv28Q7kNvwEWC7Pp&_nc_gid=ZkuzixIpoHSHf736EJFgjQ&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1RTorOfbN24WrHPxKOHooqvT_3K1OHFzL-to6Ugme4Hw&oe=69DC19A9&_nc_sid=6c5dea",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274984400,
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
  "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGeef3ucxVuFD9E-CssGPMjRS4Ap1YsdYKAeMZfZ4L2xwJ6I2qrjqBOpPe0oZEqV3U&_nc_ohc=XbeNvhLXv28Q7kNvwGaUhgD&_nc_gid=l_7W6UzCo-tTf29BjlIIRw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1r45IIRqM04aC7WztcVlUIb_BzBgODLkLjX58W4MBtVQ&oe=69DC19A9&_nc_sid=164c1d",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274984400,
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
  "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGCjBGKh_8plpX1tr5aPP88H5oBtG883BL_KHlo2wlgTl41JoMj8kCEoIORe8TKU9s&_nc_ohc=XbeNvhLXv28Q7kNvwHzd1Ep&_nc_gid=7sN5bbnSrBO0rOccwzZxJw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2S_kwTA08UCnqZT70BdDuJB5RP3OFW43YybGrgiv8TIw&oe=69DC19A9&_nc_sid=164c1d",
  "profile_pic_url_hd": null,
  "is_verified": true,
  "media_count": 31529,
  "follower_count": 274984400,
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
    "thumbnail_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwG-zYeV&_nc_oc=AdomvQs38NBSbin_qbz68xTRgonzGPHSEoXNCckJuvpGkMUUmO53RK2CFrFxI96A4Qc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&oh=00_Af094IDPoZOcr2lAGtLG0XRB9PfbOHfHcxq1Vt4i5QRnAw&oe=69DC46E1",
    "location": null,
    "user": {
      "pk": "1029649300",
      "id": "1029649300",
      "username": "natgeoanimals",
      "full_name": "National Geographic Animals",
      "profile_pic_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH3VEjDry6Vs-kfMyuQVEKf7Eg6ikiXZfz50lnFLHgBAstlQPq4Y8QbjVoe7wfCOBQ&_nc_ohc=ic5ODsLE2O8Q7kNvwEhz33t&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2Zmlu_nVomttjtSmE6YF6nOyAv-xd1AvfyY2Xc_r9F9A&oe=69DC204C&_nc_sid=c024bc",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 479,
    "comments_disabled": false,
    "like_count": 49174,
    "play_count": 2547585,
    "has_liked": false,
    "caption_text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwGZCrH1&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2IJkW8m-zBb6qeim6oy20qL_1jeSZbYoLpzkoLm-3FDg&oe=69D853EC",
    "view_count": 0,
    "video_duration": 60.736000061035156,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          18248,
          36496
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwG-zYeV&_nc_oc=AdomvQs38NBSbin_qbz68xTRgonzGPHSEoXNCckJuvpGkMUUmO53RK2CFrFxI96A4Qc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&oh=00_Af094IDPoZOcr2lAGtLG0XRB9PfbOHfHcxq1Vt4i5QRnAw&oe=69DC46E1",
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
        "url": "https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwGZCrH1&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2IJkW8m-zBb6qeim6oy20qL_1jeSZbYoLpzkoLm-3FDg&oe=69D853EC",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1579353,
        "height": 1280,
        "id": "4284559321859069v",
        "type": 102,
        "url": "https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwGZCrH1&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2IJkW8m-zBb6qeim6oy20qL_1jeSZbYoLpzkoLm-3FDg&oe=69D853EC",
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
  // ... truncated
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
      "thumbnail_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwEFfsDj&_nc_oc=AdrqoHznIVapSmGehf18hVzomITNwIhY2oPlO_9ZqI2pXYodKJA7oUQlCE8sRPNoNrw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_ss=7a3ba&oh=00_Af2yOFQoJxU_WW2UWMNrKc8J2OG6aiqCRHhH7dUgzDVLTg&oe=69DC46E1",
      "location": null,
      "user": {
        "pk": "1029649300",
        "id": "1029649300",
        "username": "natgeoanimals",
        "full_name": "National Geographic Animals",
        "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE6Q53GCzhClpeVlrU_K0GnWUhB5lFAOJSF6U63yAXaSVc_pzwChRQQAmHBA5Mjh78&_nc_ohc=ic5ODsLE2O8Q7kNvwE2sdLw&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af0x-0gboxvCIxunGFWBdPqmAFAK0Ce4BGTmzW9sjZifLw&oe=69DC204C&_nc_sid=c024bc",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 479,
      "comments_disabled": false,
      "like_count": 49169,
      "play_count": 2547585,
      "has_liked": false,
      "caption_text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwFCcxGV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2p6ohNM7AUJGxCy5pw0y126CHLDxo9o9CYg-2_viwI-A&oe=69D853EC",
      "view_count": 0,
      "video_duration": 60.736000061035156,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            18248,
            36496
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwEFfsDj&_nc_oc=AdrqoHznIVapSmGehf18hVzomITNwIhY2oPlO_9ZqI2pXYodKJA7oUQlCE8sRPNoNrw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_ss=7a3ba&oh=00_Af2yOFQoJxU_WW2UWMNrKc8J2OG6aiqCRHhH7dUgzDVLTg&oe=69DC46E1",
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
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwFCcxGV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2p6ohNM7AUJGxCy5pw0y126CHLDxo9o9CYg-2_viwI-A&oe=69D853EC",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1579353,
          "height": 1280,
          "id": "4284559321859069v",
          "type": 102,
          "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwFCcxGV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2p6ohNM7AUJGxCy5pw0y126CHLDxo9o9CYg-2_viwI-A&oe=69D853EC",
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
  // ... truncated
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
    "pk": "63912641487",
    "id": "63912641487",
    "username": "mbxs.07",
    "full_name": "mbx",
    "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658385983_17946450099129488_8532192189292977490_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gE9hvDo-tSQu3a2FPD3XeefgFRIb4UCytEM_9tJTWY9i2BtXegwfsJD0J_nRV3aPXE&_nc_ohc=q5v27yTsgyAQ7kNvwFA0Yxb&_nc_gid=Qe4v3hNZXrnyLBM4MOix6A&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GD8sPieQTCOHM8I-AFKdKzaXb2h2bmNDAQAB1501500j-ccb7-5&oh=00_Af2PyQzn6iCkBVwoSTRTYrJkI_nMCQp3yNfvXczZ6DBLqA&oe=69DC2B5D&_nc_sid=6ff7c8",
    "is_private": false,
    "is_verified": false
  },
  {
    "pk": "4290885509",
    "id": "4290885509",
    "username": "tajw60",
    "full_name": "Teresa Wrigley",
    "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-19/573215496_18412239754141510_3751195623028207489_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gE9hvDo-tSQu3a2FPD3XeefgFRIb4UCytEM_9tJTWY9i2BtXegwfsJD0J_nRV3aPXE&_nc_ohc=UPa13xRcc7sQ7kNvwG-9Cfv&_nc_gid=Qe4v3hNZXrnyLBM4MOix6A&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GAiTKiJGnxCi1WlBAIGvmGGL7A40bmNDAQAB1501500j-ccb7-5&oh=00_Af1o0dEgymnVKEU1NUXHfh-Gml2LabIJPnOAv90obp0rjw&oe=69DC24E4&_nc_sid=6ff7c8",
    "is_private": true,
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
      "pk": "63912641487",
      "id": "63912641487",
      "username": "mbxs.07",
      "full_name": "mbx",
      "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658385983_17946450099129488_8532192189292977490_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gGazp3mBvoZfbQvM2Q5_Q9EKagtRn1dFFAzRXW-ZaUjKcyXFlJ4X_aB39fq6iMOyv0&_nc_ohc=q5v27yTsgyAQ7kNvwFA0Yxb&_nc_gid=klPFFcy5gfHFKniOHuzboA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GD8sPieQTCOHM8I-AFKdKzaXb2h2bmNDAQAB1501500j-ccb7-5&oh=00_Af1BI_WkJKbeLRzVQuD5lfsfiuZodm2LeUHV2IsYd3F3zQ&oe=69DC2B5D&_nc_sid=6ff7c8",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "4290885509",
      "id": "4290885509",
      "username": "tajw60",
      "full_name": "Teresa Wrigley",
      "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-19/573215496_18412239754141510_3751195623028207489_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gGazp3mBvoZfbQvM2Q5_Q9EKagtRn1dFFAzRXW-ZaUjKcyXFlJ4X_aB39fq6iMOyv0&_nc_ohc=UPa13xRcc7sQ7kNvwG-9Cfv&_nc_gid=klPFFcy5gfHFKniOHuzboA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GAiTKiJGnxCi1WlBAIGvmGGL7A40bmNDAQAB1501500j-ccb7-5&oh=00_Af3Ftgbf5iQADdwPTg0n2QLSbBFvaUdR6ck9URoHLhXE_A&oe=69DC24E4&_nc_sid=6ff7c8",
      "is_private": true,
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
    "pk": "361314460",
    "id": "361314460",
    "username": "shonephoto",
    "full_name": "Robbie Shone",
    "profile_pic_url": "https://scontent-sin2-1.cdninstagram.com/v/t51.2885-19/354370994_1405493676903026_8480872527503633727_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gEjKYUW8VYHBbMWrnlrt-bJW2dBapnS_kez2Fdb7esO29DhdmmM21vZYfKQNDdB7i8&_nc_ohc=13iZrYuK4cAQ7kNvwEcQswG&_nc_gid=tz-rfe9691Rcshis4VGLFg&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GLJFHxVyilj-Sf4EAD8tOVOhHLJ1bkULAAAB1501500j-ccb7-5&oh=00_Af19FMWERMl3MWRGxWCew4ltXiBlbtvsSQ49yzDkSjx7bw&oe=69DC3473&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": false
  },
  {
    "pk": "24570749",
    "id": "24570749",
    "username": "amytoensing",
    "full_name": "Amy Toensing",
    "profile_pic_url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-19/524724246_18527088106058750_6092484181596815389_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gEjKYUW8VYHBbMWrnlrt-bJW2dBapnS_kez2Fdb7esO29DhdmmM21vZYfKQNDdB7i8&_nc_ohc=oBgaaK26TbwQ7kNvwEIsogT&_nc_gid=tz-rfe9691Rcshis4VGLFg&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GBaoRh-_s0jZSdJBAB3Aw3MV2oxUbmNDAQAB1501500j-ccb7-5&oh=00_Af07HosLk5ATwYl1HdHKhJUQoisiBCnkzSXD5eFv2hD06w&oe=69DC2E2C&_nc_sid=ce9561",
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
      "pk": "14331657700",
      "id": "14331657700",
      "username": "natgeomagjp",
      "full_name": "ナショナルジオグラフィック日本版",
      "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/v/t51.2885-19/65160972_483182759115510_2590728031043584000_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MDAuYzIifQ&_nc_ht=scontent-sin2-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gG1IonPs3Ug9vjVEa_CcwAByDnupJjx-X1g039lDbDaGRQCDrJBlUkqmUQ9096MgKQ&_nc_ohc=7ujGFVqjyKQQ7kNvwHsfzr9&_nc_gid=Cdb3I6fDf0ZswzPJJhENyg&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GAxH4gP2_rfAc7cBAAAAAABrHfQjbkULAAAB1501500j-ccb7-5&oh=00_Af3amvKnxA4zlB1mek0zcZwUxCB6rikdq2u0_DZ6d3xOHQ&oe=69DC21ED&_nc_sid=ce9561",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "8958735",
      "id": "8958735",
      "username": "christiehemmklok",
      "full_name": "Christie Hemm Klok",
      "profile_pic_url": "https://scontent-sin11-1.cdninstagram.com/v/t51.2885-19/439586899_1933783770387040_7648789920126959876_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sin11-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gG1IonPs3Ug9vjVEa_CcwAByDnupJjx-X1g039lDbDaGRQCDrJBlUkqmUQ9096MgKQ&_nc_ohc=78gK351qr6gQ7kNvwGj86Km&_nc_gid=Cdb3I6fDf0ZswzPJJhENyg&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GFOQMxpg0rQexN4GAASBwUbo9SVqbkULAAAB1501500j-ccb7-5&oh=00_Af3SFq7pnAYZ7w1rQTn_q6AuL8MKJl1E13SNm0xAyVtkpA&oe=69DC42DC&_nc_sid=ce9561",
      "is_private": false,
      "is_verified": true
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
    "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwH4PITn&_nc_oc=Adqyoq6kwCfX-m7IqPTbQttt70XnhGFdeRlmsDNiGBhXkw02d4OE_j7Ov0XDHy1-nm4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_ss=7a3ba&oh=00_Af15YJdXdSLItZMGoRXs9j_w_NA3RTEjt5zpmTzIc7lJcQ&oe=69DC2DB1",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHL1lTdiNjY4kTrhoDkC8-PJSK_2evPUSd62XjjV7A_3js9WGl3IjZWqxx6HMyo6Ww&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1terAkUEAjzt9o-htbk2jZeRImjLKt3-pbKFAOnahLMA&oe=69DC19A9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 236,
    "comments_disabled": false,
    "like_count": 35785,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwF69nzI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2USQqmRYPhHxx7U3S01oTYXXXSB2m2m1J39bWuFOk9_Q&oe=69D84A2E",
    "view_count": 0,
    "video_duration": 60.10100173950195,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          24827,
          49654
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwH4PITn&_nc_oc=Adqyoq6kwCfX-m7IqPTbQttt70XnhGFdeRlmsDNiGBhXkw02d4OE_j7Ov0XDHy1-nm4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_ss=7a3ba&oh=00_Af15YJdXdSLItZMGoRXs9j_w_NA3RTEjt5zpmTzIc7lJcQ&oe=69DC2DB1",
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
        "url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwF69nzI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2USQqmRYPhHxx7U3S01oTYXXXSB2m2m1J39bWuFOk9_Q&oe=69D84A2E",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 102,
        "url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwF69nzI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2USQqmRYPhHxx7U3S01oTYXXXSB2m2m1J39bWuFOk9_Q&oe=69D84A2E",
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
  // ... truncated
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
      "thumbnail_url": "https://scontent-atl3-3.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwGZR-On&_nc_oc=Adq-rSlOVoEaYpiGqfh0cBRzKpQs9yHWf3u2DVsKDRw3Oj5NCv9j3S1403S9qMpytXY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_ss=7a3ba&oh=00_Af3gzQklQiRm_tFjS-bOWXStcs_3WMYz6cJIhaAdLtgFlA&oe=69DC2DB1",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGBK8z3L9lqy4DWvML--BpgVJy36lGCiwBUPBGQ6-Nh99kvvNoUUoGhXCiDz34DBIk&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af21UlzcJbkuel7b_lAq1YhzxqFGUgdRksXzbmWZaD1Wdg&oe=69DC19A9&_nc_sid=b41fef",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 236,
      "comments_disabled": false,
      "like_count": 35785,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwEBY26L&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsIndhdGNoX3RpbWVfcyI6NjE5MzIzOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3hpAO6EJt_JctH9DZukF7sXHh83B5kdPxUDJbPkZ0GZw&oe=69D84A2E",
      "view_count": 0,
      "video_duration": 60.10100173950195,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            24827,
            49654
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-atl3-3.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwGZR-On&_nc_oc=Adq-rSlOVoEaYpiGqfh0cBRzKpQs9yHWf3u2DVsKDRw3Oj5NCv9j3S1403S9qMpytXY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_ss=7a3ba&oh=00_Af3gzQklQiRm_tFjS-bOWXStcs_3WMYz6cJIhaAdLtgFlA&oe=69DC2DB1",
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
          "url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwEBY26L&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsIndhdGNoX3RpbWVfcyI6NjE5MzIzOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3hpAO6EJt_JctH9DZukF7sXHh83B5kdPxUDJbPkZ0GZw&oe=69D84A2E",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1568436,
          "height": 1280,
          "id": "1258679306414510v",
          "type": 102,
          "url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwEBY26L&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsIndhdGNoX3RpbWVfcyI6NjE5MzIzOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3hpAO6EJt_JctH9DZukF7sXHh83B5kdPxUDJbPkZ0GZw&oe=69D84A2E",
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
  // ... truncated
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
    "thumbnail_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwGmNHxt&_nc_oc=Adpj3EmeY7IwO7YUL6BXd1j7O_6IsKj8kPTS7Gao3aayJhwyNkWNAUTE78rPoTw9Hdo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_ss=7a3ba&oh=00_Af3O9KiIb_9lZXCeDrzP9-pfaw-HLOjgVF_OVoi3mQI6xw&oe=69DC2DB1",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHLerj-sL0LCtDjad8eAFqTo4hxLTnY7Mr86bhrtVsVr5uOmioN2de1CHC0PZpT-ao&_nc_ohc=XbeNvhLXv28Q7kNvwFjjZcH&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0gwvqUwb8v6dFl4bqCTT0PonGIU-Y5yudCqf5xizPuag&oe=69DC19A9&_nc_sid=b41fef",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 236,
    "comments_disabled": false,
    "like_count": 35785,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwGqqotN&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3h936nmuAnjJnV-nF-25RVklRCdUIrN7Mzhqn9K7ToYQ&oe=69D84A2E",
    "view_count": 0,
    "video_duration": 60.10100173950195,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          24827,
          49654
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwGmNHxt&_nc_oc=Adpj3EmeY7IwO7YUL6BXd1j7O_6IsKj8kPTS7Gao3aayJhwyNkWNAUTE78rPoTw9Hdo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_ss=7a3ba&oh=00_Af3O9KiIb_9lZXCeDrzP9-pfaw-HLOjgVF_OVoi3mQI6xw&oe=69DC2DB1",
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
        "url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwGqqotN&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3h936nmuAnjJnV-nF-25RVklRCdUIrN7Mzhqn9K7ToYQ&oe=69D84A2E",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1568436,
        "height": 1280,
        "id": "1258679306414510v",
        "type": 102,
        "url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwGqqotN&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3h936nmuAnjJnV-nF-25RVklRCdUIrN7Mzhqn9K7ToYQ&oe=69D84A2E",
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
  // ... truncated
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
    "pk": "4290885509",
    "id": "4290885509",
    "username": "tajw60",
    "full_name": "Teresa Wrigley",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/573215496_18412239754141510_3751195623028207489_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHjBDhHNM3lI6mh3iFQDO6wM5GzKlz3k9Ded9ebN-DFn8jKCI2UU8EUBqUTBDIT5aY&_nc_ohc=UPa13xRcc7sQ7kNvwFkUsIb&_nc_gid=dKyJdoaJ9opv1maC3ZpkHA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GAiTKiJGnxCi1WlBAIGvmGGL7A40bmNDAQAB1501500j-ccb7-5&oh=00_Af0fUVbWZpf2XpyX7OVLlgDmbX8yqTkBT74v2BsPTvYB5w&oe=69DC24E4&_nc_sid=6ff7c8",
    "is_private": true,
    "is_verified": false
  },
  {
    "pk": "63912641487",
    "id": "63912641487",
    "username": "mbxs.07",
    "full_name": "mbx",
    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/658385983_17946450099129488_8532192189292977490_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHjBDhHNM3lI6mh3iFQDO6wM5GzKlz3k9Ded9ebN-DFn8jKCI2UU8EUBqUTBDIT5aY&_nc_ohc=q5v27yTsgyAQ7kNvwFxuvII&_nc_gid=dKyJdoaJ9opv1maC3ZpkHA&edm=APQMUHMBAAAA&ccb=7-5&ig_cache_key=GD8sPieQTCOHM8I-AFKdKzaXb2h2bmNDAQAB1501500j-ccb7-5&oh=00_Af0MwYPNrs09ZGsBnNWxyeBtwLiSmZrmB-2ZDLbQ2iaHZg&oe=69DC2B5D&_nc_sid=6ff7c8",
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
    "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFNrTvFsQMabviDE-wdIY3pvVKwMzVmWGym4KkpOx7JEvRd1zbtuJ6X-RJQkTrE4kY&_nc_ohc=t-DCVZxwtX4Q7kNvwFFNUip&_nc_gid=0xik6A6vqClgUOUk5HX0BA&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af0kmsrHKrgYjc2FMP3leAUJ-dw4hY7FUJN0n_1eUHh-cQ&oe=69DC2F06&_nc_sid=ce9561",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "1029649300",
    "id": "1029649300",
    "username": "natgeoanimals",
    "full_name": "National Geographic Animals",
    "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFNrTvFsQMabviDE-wdIY3pvVKwMzVmWGym4KkpOx7JEvRd1zbtuJ6X-RJQkTrE4kY&_nc_ohc=ic5ODsLE2O8Q7kNvwFi9kYX&_nc_gid=0xik6A6vqClgUOUk5HX0BA&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af1qr3xH_0BZmuY6teQhR1b-TnY2qmdw2EfEHSmuLE4m9w&oe=69DC204C&_nc_sid=ce9561",
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
      "thumbnail_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwEurejE&_nc_oc=AdpPgjNXYzBWJCcS4sOFRy4-6XfNZa5vGRAZaWR9S-gZOhcmF9weAwnTRZL9Ch7Da7g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&_nc_ss=7a3ba&oh=00_Af1y7C0CTEGxtZz7jq-RcF2SKKp2QVla_PR5PArBYK691Q&oe=69DC2D22",
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
        "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/427378186_275046522125863_1224244213859159903_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43ODUuYzIifQ&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFRn8MxvRnbdO41DfdbIW9co0OX3Sj9pLsqeVmVuOiPaDtW39qObUSTibEGMqwBS88&_nc_ohc=Bb5J40vuSOQQ7kNvwHLrqUA&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GApGeRknfj9CJ-oAAF8PZ02gY-0QbkULAAAB1501500j-ccb7-5&oh=00_Af1Wx5bsMNnN_dH2A8HV1Vq64vEESu_K8BLBb5BIIKKSBw&oe=69DC197A&_nc_sid=a8b8e2",
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
            "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/11426732_990789794299104_1839082617_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFRn8MxvRnbdO41DfdbIW9co0OX3Sj9pLsqeVmVuOiPaDtW39qObUSTibEGMqwBS88&_nc_ohc=Nk9rpOO4FmUQ7kNvwGz4YCk&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GKxbrgDgfLw5HoUDAHksnm0AAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af0gZXQBuZ0yJn-CGoymTp42Mglsmt_CCBEqF_FtagC5yQ&oe=69DC3E73&_nc_sid=a8b8e2",
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
            "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/487340431_1510016599961079_422634517629355178_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFRn8MxvRnbdO41DfdbIW9co0OX3Sj9pLsqeVmVuOiPaDtW39qObUSTibEGMqwBS88&_nc_ohc=seU08ayHeVsQ7kNvwFX5otx&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GI85DB33rQsjWl0FAKrEHcXaf90FbkULAAAB1501500j-ccb7-5&oh=00_Af104MTKSEok2Be_2lopgFSf0tIokqX28n4jXvL136AUeQ&oe=69DC1D2A&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "x": 0.8700000048000001,
          "y": 0.0496000014
        }
      ],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [],
      "image_versions": [
  // ... truncated
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
