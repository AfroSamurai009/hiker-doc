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
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775657717\" FBManifestIdentifier=\"FuqLs50NKRbMrPbB5Z2pBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1498046678354726a\" bandwidth=\"66810\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66810\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m78/AQOElke-XjvO2ixFipAMNby9AqC5CZmOcY8PcbQDmAwEGdrdvbD58TPi5A5RKS7WbXpTrVlZQip3DhNxjBI2vRela2S063MA11oc5y0.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=XLhOSrzrzoUQ7kNvwHYSJuH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2CAv-qJq9cSzCsvzyIqvmJRASE1ZgxIjS7mXwwDjK77g&amp;oe=69D8589E</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "progressive_download_url": "https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m69/AQPYF2mAhRbYzYMrI560MWB9XBJqAACyr7szcVbj1WFwaneaOm5BlFHWUM37z1AaOh6Oyo4BIq6T2yeHyTeibfXn.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_ohc=wTkgipWqtN0Q7kNvwHzuDan&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2EI9FikHb35qeVUX5NPStJAd3AB0Xbc90T0Jd3EIbW2g&oe=69DC1E23",
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
          "profile_pic_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH3VEjDry6Vs-kfMyuQVEKf7Eg6ikiXZfz50lnFLHgBAstlQPq4Y8QbjVoe7wfCOBQ&_nc_ohc=ic5ODsLE2O8Q7kNvwEhz33t&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2Zmlu_nVomttjtSmE6YF6nOyAv-xd1AvfyY2Xc_r9F9A&oe=69DC204C&_nc_sid=c024bc"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775657718\" FBManifestIdentifier=\"FuyLs50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZtpKal9ScgMkCzo2Dq7qi/wKKoLTC7cuPA/ams5yMlrEDyJik4v+7uwSkqoqBzomOBe6JqLSYw8wGuNTorbLX6AaGoI/s2be8B67e29mIlNEHqpzd2fSFoQ8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2AhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.1\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"952556667169211v\" bandwidth=\"124017\" codecs=\"vp09.00.30.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"941404\" FBPlaybackResolutionMos=\"0:100,360:41.6,480:39.2,720:38.5,1080:40.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:77,480:71.2,720:63,1080:54.5\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN-3fTGmvhHM7Q1y_FOG9xoedvPlxkGouNg1lFuA5_xgsQghUOtSFTS9vKLfO0D_L1GacDWvy5ce_R_nyJ1EFvz2nLYwpilZbxOCxI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=9VOyAIJ6L3sQ7kNvwEiAtVp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTI0MDE3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af32a8GVkM2PMnbtYZtqxkt__Z1hkjQ9gEPo3KH3IeMjaQ&amp;oe=69DC4B7B</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-7405\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-55624\" FBFirstSegmentRange=\"1006-74648\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"74649-143790\" FBPrefetchSegmentRange=\"1006-74648\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"842817852171111v\" bandwidth=\"175646\" codecs=\"vp09.00.30.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1333319\" FBPlaybackResolutionMos=\"0:100,360:51.2,480:47.7,720:45.5,1080:46.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:84.1,480:79,720:71,1080:62\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNpqtjx8cAdYzcQjWE6DlkGJaexf-bSQlGWJO9YaMvAQ4vdy8ite1nByg8Pjyu05bLRur7bHiQMuO2PYNDsIzQGbAz2r5wY3L4lcCk.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=s9UVBq06zuwQ7kNvwGQ32aA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTc1NjQ2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1EJs8ZKqyZfkg3Sm0nGTnYCV3skYtHJwnqK-sOKlsPnw&amp;oe=69DC3749</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-8918\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-77986\" FBFirstSegmentRange=\"1006-108408\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"108409-203782\" FBPrefetchSegmentRange=\"1006-108408\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"2148790485874583v\" bandwidth=\"244057\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"1852621\" FBPlaybackResolutionMos=\"0:100,360:58.2,480:55.1,720:52.8,1080:52.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.4,480:85.6,720:79.6,1080:71.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNxC9rSaw6H7px3dJvPKJ020vH5eUaC9l9yHN2ErdJ66xFoeS-_TvsKoXf_rbhgDwu2C_MKWjFrdoyyTClnbC9EL_2nqlAPJ6MZ4xw.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=0JP9Fuy6RNsQ7kNvwFlUok0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjQ0MDU3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af33QEP_FAgmC9NiKfwe2v5MbME5eP5qjHx_rLxIc058EQ&amp;oe=69DC2C53</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-10941\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-105644\" FBFirstSegmentRange=\"1006-148737\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"148738-280929\" FBPrefetchSegmentRange=\"1006-148737\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1857129955000951v\" bandwidth=\"345605\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2623466\" FBPlaybackResolutionMos=\"0:100,360:67.1,480:63.4,720:60.3,1080:59.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93,480:90,720:85,1080:77.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNav0tPtmTT37aB9fmHzEtiGJapNzrZhtnoWk0KO2LFUUewLn1Tll5uif2fIYVwbK940FTea_dYflbheFFvVJ_bphKAB10ex6BrGsY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=cKumA8YfUaAQ7kNvwFvfCfi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzQ1NjA1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0IvX-jPFLh8vTrHelnYEfbQX7UhnwFtP_ULuaaJIxIKA&amp;oe=69DC47E8</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-13673\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-151725\" FBFirstSegmentRange=\"1006-207400\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"207401-392549\" FBPrefetchSegmentRange=\"1006-207400\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"723482497443465v\" bandwidth=\"482609\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3663455\" FBPlaybackResolutionMos=\"0:100,360:73.7,480:70.1,720:66.6,1080:64.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:94.2,720:90.2,1080:83.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNPQgAn7a4JAzryeXYRe4NrWCHXJIS7SKTMjR4k5LsAnUu9HfBLRldM6k9vApxUwodfgoYcRKyfYapFedH2kTQgzSk4khJ4tMj7GZs.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=MtHqQI2HEs8Q7kNvwHgK3v4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDgyNjA5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3v-Js2MmZn6AMPCsRk0Oo-ySOlUZErBzz3Ur54hofkkw&amp;oe=69DC4DA0</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-16842\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-209852\" FBFirstSegmentRange=\"1006-293485\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"293486-548674\" FBPrefetchSegmentRange=\"1006-293485\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1438326298069650v\" bandwidth=\"631853\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"4796349\" FBPlaybackResolutionMos=\"0:100,360:77.4,480:74.3,720:70.7,1080:68.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.4,480:96.1,720:93.3,1080:87.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOO2Y8UwiIp2Iy2afTi4liyqQhm7RVOq45AF-KZs6nAUTfOyk5K1mWfb-BAKVnV2ngIAoBlT1DaQI5eY7EiSiFx8GanfbhRAv83jmo.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=O7wzvRQMxggQ7kNvwHBBvpA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjMxODUzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1vAuX_4q-R8IBpaG-NgP0YZCr5niJo_fLnJQszqY9XYg&amp;oe=69DC28FA</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-20006\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-269774\" FBFirstSegmentRange=\"1006-379627\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"379628-704580\" FBPrefetchSegmentRange=\"1006-379627\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1919049686390044v\" bandwidth=\"843182\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"6400537\" FBPlaybackResolutionMos=\"0:100,360:82,480:77.8,720:74.3,1080:71.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.31,480:97.6,720:95.7,1080:90.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOgYlNMirFA1-g5Ud5JWUZYDq9jXLOSRoXoIYVAEJ8oeiPw5sYT74UlROegghgFCRXwytRinQ3rFg69shxZeV8cEJSf3UeIgMURtyA.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-2.cdninstagram.com&amp;_nc_ohc=qYFvQ1RhaPsQ7kNvwFLsxcb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6ODQzMTgyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2-GqUT9I6azSr1LjZQC5kuVwsFwlcVolsJdhLcYbZoMw&amp;oe=69DC3758</BaseURL><SegmentBase indexRange=\"818-1005\" timescale=\"11988\" FBMinimumPrefetchRange=\"1006-23752\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1006-354646\" FBFirstSegmentRange=\"1006-506815\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"506816-930985\" FBPrefetchSegmentRange=\"1006-506815\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4294793980782357a\" bandwidth=\"46380\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46380\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"353137\" FBPaqMos=\"87.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m367/AQN9GI-VauacxM2tCfwmiCOijhyH33zBWrM0Dr4JwD6i2FjABcTvvBGOXIydEyGVXVx6wkUjNuDAtapI93ufxCNL1tRZuAP-HRtBv50.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-2.cdninstagram.com&amp;_nc_ohc=Uo8ixeKIRUsQ7kNvwFGert2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjUxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1I1TTkijBnf1dlHu_Xn2GKDO9hw-Q8ny5ujWt-U_sLRw&amp;oe=69DC28AA</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2136\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-14938\" FBFirstSegmentRange=\"1025-28400\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28401-56361\" FBPrefetchSegmentRange=\"1025-28400\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1256673039910436a\" bandwidth=\"74812\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74812\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"568992\" FBPaqMos=\"89.65\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPA0IU4X5qD93OmmaSc1st7oueEaOmYwYCBhH3T3wOKN7WutkRMOZ1TDwC1ugFmlc5yKEeuM_xeo_vD4IzH2AbUDhA7xa2uuL_kti8.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=H10A9jvUydQQ7kNvwG3t5Hr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NDk0NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3UOsSTyjk_b00jdbtC2sGKTqxddUAC8j6cLummoeU93w&amp;oe=69DC2DE2</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21486\" FBFirstSegmentRange=\"1026-43481\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"43482-90615\" FBPrefetchSegmentRange=\"1026-43481\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"878713468520453a\" bandwidth=\"108352\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108352\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"823623\" FBPaqMos=\"83.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOhb37d5jmr5MvSl8eT28PWBputzk-lecQ-RBUBedLEv96EozZbcoK_AR-dP3eFTj3ZDuOnoWe6DiibSbh3Vjc_rcGupQpI3Z2uCnA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-2.cdninstagram.com&amp;_nc_ohc=qIB9a-mC_CIQ7kNvwHSO51P&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDg0ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1fNBW8WAz25ihUCzsRzlb1_sKWBZPfXbkJIsZNQou4Ag&amp;oe=69DC1D87</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2395\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-30757\" FBFirstSegmentRange=\"1021-62738\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62739-132935\" FBPrefetchSegmentRange=\"1021-62738\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2103223183861763a\" bandwidth=\"143947\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"143947\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1093864\" FBPaqMos=\"87.00\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOgH1TOj2U7Ucn9wQoBfkebTHLZ9A_EoIFXsEJ2CkC1MsQUoWoasexRt0uwJQMyHQr8MmjxA15OisXxvCobhDmp05SCyaFAKp2_vFI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=X7gcVcXpzlUQ7kNvwGW_1ND&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxNDQwODEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3BTFt73mES9vIyj7-q5ydfabR9MsC046vJYb6sBurRRQ&amp;oe=69DC1AE7</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-45040\" FBFirstSegmentRange=\"1021-86500\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"86501-176000\" FBPrefetchSegmentRange=\"1021-86500\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "profile_pic_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH3VEjDry6Vs-kfMyuQVEKf7Eg6ikiXZfz50lnFLHgBAstlQPq4Y8QbjVoe7wfCOBQ&_nc_ohc=XbeNvhLXv28Q7kNvwH-D1Zg&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af25zkoQ3pjAyxRNfF2yvmFtsyo2VSey9aX_QUsSqaCZVA&oe=69DC19A9&_nc_sid=c024bc",
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
    "thumbnail_url": "https://scontent-fra3-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwEfjijv&_nc_oc=AdrgiwWRbzB7GoNf7Y8Mk1QpSRMZJj7Ska4gRQ6KnsseD_pbM_Uk7MjYVr89mIa03SM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&oh=00_Af11hgDValc7Y1WU1wVjyjRQHGghfoNF0P-FpkqTSaBFZQ&oe=69DC2AD5",
    "location": null,
    "user": {
      "pk": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "profile_pic_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH3VEjDry6Vs-kfMyuQVEKf7Eg6ikiXZfz50lnFLHgBAstlQPq4Y8QbjVoe7wfCOBQ&_nc_ohc=XbeNvhLXv28Q7kNvwH-D1Zg&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af25zkoQ3pjAyxRNfF2yvmFtsyo2VSey9aX_QUsSqaCZVA&oe=69DC19A9&_nc_sid=c024bc",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": true
    },
    "comment_count": 65,
    "comments_disabled": false,
    "like_count": 11040,
    "play_count": 1479128,
    "has_liked": false,
    "caption_text": "In Hoppers, Piper Curda’s character Mabel explored her sense of wonder for the natural world with the help of hopping technology. For now, we still have to do it the old-fashioned way.\n\nSee Disney and Pixar’s new movie Hoppers, now playing, only in theaters, and step into wonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwG5_NYm&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0JL_0hYt4Tiki8dCyC4aIeYWyetG0lo62nnEOoEtwmYA&oe=69D83578",
    "view_count": 0,
    "video_duration": 55.44499969482422,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          13479,
          26958
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-fra3-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwEfjijv&_nc_oc=AdrgiwWRbzB7GoNf7Y8Mk1QpSRMZJj7Ska4gRQ6KnsseD_pbM_Uk7MjYVr89mIa03SM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&oh=00_Af11hgDValc7Y1WU1wVjyjRQHGghfoNF0P-FpkqTSaBFZQ&oe=69DC2AD5",
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
        "url": "https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwG5_NYm&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0JL_0hYt4Tiki8dCyC4aIeYWyetG0lo62nnEOoEtwmYA&oe=69D83578",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1113315,
        "height": 1280,
        "id": "2358585431274531v",
        "type": 102,
        "url": "https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwG5_NYm&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0JL_0hYt4Tiki8dCyC4aIeYWyetG0lo62nnEOoEtwmYA&oe=69D83578",
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
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775657717\" FBManifestIdentifier=\"FuqLs50NKRbEl5Tt0tWmAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"929459223037410a\" bandwidth=\"60820\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"60820\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m78/AQN38tw9LWdIk_CWlJ0ze2Ayn07LgXtA4TMaLXc-6SODK58HBqKnlOKk8_LTSIHFsE3VGUlntYj8FPrehpb5VftWJE3s0U_LvQcQ0p4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=ZHLfVpYSwAwQ7kNvwFM1M-b&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo2MDk5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3X2L0jZ9oGt2U3wv8iVM3vrrvauE4CkGVVLCSdVdEM0g&amp;oe=69D82D73</BaseURL><SegmentBase indexRange=\"824-1191\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "progressive_download_url": "https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m69/AQPKBMTmsUUaSlY28FrQeX4c4T6dijF6gtmaEyTFBN6pFY5bZ5DsQbcUjfr7pEffSR4eVHh1ugsHyMjH1cbkv8Kz.mp4?strext=1&_nc_cat=106&_nc_sid=8bf8fe&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_ohc=VR1-k3frXTsQ7kNvwEK8gz9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af1qphGoZ6u0vDNhR8WCBkDyu-lM4b2MTy61cilN5h5sUA&oe=69DC1B8C",
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
          "profile_pic_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH3VEjDry6Vs-kfMyuQVEKf7Eg6ikiXZfz50lnFLHgBAstlQPq4Y8QbjVoe7wfCOBQ&_nc_ohc=XbeNvhLXv28Q7kNvwH-D1Zg&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af25zkoQ3pjAyxRNfF2yvmFtsyo2VSey9aX_QUsSqaCZVA&oe=69DC19A9&_nc_sid=c024bc"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775657718\" FBManifestIdentifier=\"FuyLs50NGBJyMmV2ZXZwOS1yMWdlbjJ2cDkZtoj2oazpzr0DnNudguLFwQT+z4jepP/TBNKk6/a745sF9KKOwMXurwWOksKj1eLJBdiWy9Tktd4FoKjfhfOcigbMs+Gn19XjBv7DsKjI9JIH7t/Ex5qIsg8iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2AhQAEhQCAA==\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:73.2\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"4332216817063927v\" bandwidth=\"135432\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q20\" FBContentLength=\"938388\" FBPlaybackResolutionMos=\"0:100,360:70.1,480:68.3,720:67.3,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.2,480:85.1,720:79.9,1080:73\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMUj7FletR5pa9_gRk6esncr9u2X9X0DLMPwgU8Mt8NKWIr_hCvVm47nUlFkimq0Yh1Y71qtO5LZGNBirPyCWfl83mCgqffj2XNH-Q.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=jg4TE1tURH0Q7kNvwFKJGVC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTM1NDMyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1YBmRJpywpfagN5HivnjhaSMW8Pxik09MIqXZ-aBNBtw&amp;oe=69DC3AD8</BaseURL><SegmentBase indexRange=\"818-993\" timescale=\"11988\" FBMinimumPrefetchRange=\"994-9666\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"994-34682\" FBFirstSegmentRange=\"994-54971\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"54972-110869\" FBPrefetchSegmentRange=\"994-54971\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1569598654137479v\" bandwidth=\"192552\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q30\" FBContentLength=\"1334158\" FBPlaybackResolutionMos=\"0:100,360:75.5,480:73.7,720:72.3,1080:72.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:91.7,480:89.4,720:85.4,1080:79.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNwhzIsjziDypkGd209ABI9Zh5yaN2ssH9BzVuFVIaab3_jTAyAnfKGuTxjkLfcN0lpqV4TXvbgBnJdtIBfOpDC8os4TCdgPsj0St8.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=X9gmwhGOdqoQ7kNvwE1Rg6m&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTkyNTUyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0lvk9Z6xxK2iXrKDFurgLnkyhv3Em_NxyERvREMGSbuw&amp;oe=69DC3B44</BaseURL><SegmentBase indexRange=\"818-993\" timescale=\"11988\" FBMinimumPrefetchRange=\"994-12112\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"994-46376\" FBFirstSegmentRange=\"994-74483\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"74484-151052\" FBPrefetchSegmentRange=\"994-74483\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"2011909826416895v\" bandwidth=\"262304\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q40\" FBContentLength=\"1817457\" FBPlaybackResolutionMos=\"0:100,360:79.4,480:77.2,720:75.7,1080:75\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.1,480:92.5,720:89.5,1080:83.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMVJHqNcEBCmuVdlnwiqqQnE3mscwiFEhRgkn6dTzIRkxjj8djOl4cUAMuJ3WIFW07FfUWGGE9cGwUDlx5lH_OIuQ1EYPTpYKEUW-I.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=VB0WV_HG1skQ7kNvwFBfy9f&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MjYyMzA0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af399NLolS9WKQ_uCZz8MLwZyhCihKQWvqP9kmQtmoL-wg&amp;oe=69DC3ABD</BaseURL><SegmentBase indexRange=\"818-993\" timescale=\"11988\" FBMinimumPrefetchRange=\"994-14910\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"994-59785\" FBFirstSegmentRange=\"994-97132\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"97133-197464\" FBPrefetchSegmentRange=\"994-97132\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1711336570219024v\" bandwidth=\"369200\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q50\" FBContentLength=\"2558120\" FBPlaybackResolutionMos=\"0:100,360:84.1,480:81.8,720:79.6,1080:78\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:95,720:92.9,1080:87.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPlrTo1JA4OAn5JGqJ1E1rjgpRH0AZXj_9_YTU0tbjcIz8qZIxn6M9RAJ5aIPZb9eaFvo1YgPlZZvTd15rTk7OwrjIoLE3iJaUItNs.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=viEtkRX1puMQ7kNvwHFADcD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MzY5MjAwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3dR0r36i0DRr_LE2A2OA_tyeGWx3CuIL46PcCY1zq8fw&amp;oe=69DC384A</BaseURL><SegmentBase indexRange=\"818-993\" timescale=\"11988\" FBMinimumPrefetchRange=\"994-18793\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"994-81906\" FBFirstSegmentRange=\"994-134073\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"134074-274625\" FBPrefetchSegmentRange=\"994-134073\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1908025170078950v\" bandwidth=\"460451\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q60\" FBContentLength=\"3190377\" FBPlaybackResolutionMos=\"0:100,360:86.4,480:84.3,720:82.1,1080:80.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:96.2,720:94.6,1080:89.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOQEJou-EcgBUqrwBbayXiAq_9-rmCWxcQOAA7Tx-3Ju_iIBquOoByc6enCgO9-cLQUa9pc7KGnngbsGjuznn3iuxLvSKsGtA7a3Ew.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=97bS97Gi6OAQ7kNvwEP4CzC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NDYwNDUxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2DwV6DyEDuyPifXd8obOp8Rlv7n6eCmhyaH0SohLRomg&amp;oe=69DC45C1</BaseURL><SegmentBase indexRange=\"818-993\" timescale=\"11988\" FBMinimumPrefetchRange=\"994-22108\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"994-101606\" FBFirstSegmentRange=\"994-167449\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"167450-344984\" FBPrefetchSegmentRange=\"994-167449\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1468457361959209v\" bandwidth=\"629599\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q70\" FBContentLength=\"4362369\" FBPlaybackResolutionMos=\"0:100,360:88.7,480:86.8,720:84.7,1080:82.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:97.3,720:96.2,1080:91.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPO9WbGAJmfbtEV--xAaPcYCUdG7_FFX5i5IGhOUF1ziAzo2xeeZr0ZFbcvxVew8PcHrEzFxigx4kYkzT6KWJ5iBJRD_UlCB_05cq8.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=Up7lBtAaFwEQ7kNvwEibf34&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NjI5NTk5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0CZ8LUyR9P9GCDkXdJsqKYQsIV8IvF_qmtUFPDF0sMmg&amp;oe=69DC2E70</BaseURL><SegmentBase indexRange=\"818-993\" timescale=\"11988\" FBMinimumPrefetchRange=\"994-26997\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"994-134574\" FBFirstSegmentRange=\"994-224524\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"224525-464948\" FBPrefetchSegmentRange=\"994-224524\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1310605610914815v\" bandwidth=\"819532\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2evevp9-r1gen2vp9_q80\" FBContentLength=\"5678377\" FBPlaybackResolutionMos=\"0:100,360:90.3,480:88.4,720:86.4,1080:84.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98,480:97.7,720:97,1080:92.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-fra5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPk4Pmbdr_0BF4QR6jzFxuH9KzXuxEmWNP5Y9BoSpb86VsE3EKg4SowPLwteR5HYjoUXxv6SpTabXtg55GXwtoWUr2bRKFhhy8TOhs.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-1.cdninstagram.com&amp;_nc_ohc=eAFIR8mj3rQQ7kNvwGWHb6k&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJldmV2cDktcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6ODE5NTMyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af08a1DfJlwZI45eaHwj3RjqK6qposaO7JyuU2Ccu0eq-g&amp;oe=69DC2D4F</BaseURL><SegmentBase indexRange=\"818-993\" timescale=\"11988\" FBMinimumPrefetchRange=\"994-32832\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"994-172205\" FBFirstSegmentRange=\"994-290523\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"290524-602901\" FBPrefetchSegmentRange=\"994-290523\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1615007113110956a\" bandwidth=\"45829\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45829\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"318635\" FBPaqMos=\"90.73\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOq8zAQzpeRCoSQuovKRKQeNbycFlDBjsuggCgJzVUNsydkP6wpqSMV87VACc6egwIxdyoZ9qyuATjsxvSkWgWUtLCaKeDUW5vI2l0.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=n8c3OFNcOe4Q7kNvwGWHqbW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo0NTk3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1ws7HaaAXXTJ65qCcDmiSdVSTd_JTVUfGcRS24mGppLg&amp;oe=69DC2330</BaseURL><SegmentBase indexRange=\"837-1012\" timescale=\"48000\" FBMinimumPrefetchRange=\"1013-2182\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1013-15598\" FBFirstSegmentRange=\"1013-28913\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28914-57244\" FBPrefetchSegmentRange=\"1013-28913\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1270034985105102a\" bandwidth=\"72011\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"72011\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"500096\" FBPaqMos=\"90.72\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNETgTPe23OWiy-KGFj4O0xaNmi9xW8k8We4jlz_Lesh43O4RfyZWEg4kgQ77avCmAh4dhCO9ERkZrtXpEBa1nLDn-iaNXSGANeubo.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra5-2.cdninstagram.com&amp;_nc_ohc=wOOs-JEmecsQ7kNvwEz5dK6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo3MjE1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1JFM9tY_R4_Mj2b825KicDWl2rU3XLWWcyTdnNGCjQAg&amp;oe=69DC26BF</BaseURL><SegmentBase indexRange=\"838-1013\" timescale=\"48000\" FBMinimumPrefetchRange=\"1014-2538\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-26077\" FBFirstSegmentRange=\"1014-48598\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48599-97300\" FBPrefetchSegmentRange=\"1014-48598\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"979919517793668a\" bandwidth=\"103761\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"103761\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"720138\" FBPaqMos=\"88.08\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNOpf9BEo2_A4jYtakOEtpNQQZDYD9C0aIFAN-Q6y8Ina7CtFSkF_92RvlAvk1DGfzRoyEa6eCluUBrw77Kir2QY9JUObENLk8IZsE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-1.cdninstagram.com&amp;_nc_ohc=sGdWzzK2ve0Q7kNvwHxRaAI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMDM5MDYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0o4EzsxX8eSbTt4SYqh4SubkCsXPzk4WCpSAaHaVFqJw&amp;oe=69DC1E0E</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2467\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-36815\" FBFirstSegmentRange=\"1009-70144\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"70145-139522\" FBPrefetchSegmentRange=\"1009-70144\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1512628090423482a\" bandwidth=\"134031\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"134031\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"929932\" FBPaqMos=\"90.49\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-fra3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMDkCHmLVEnsU6T5_aC7ZlGvMakuRW1O3OnJZfxZuCHE1fs0cf1weWXn_tPspjek6E1p7CHcVLpGZLRSFGGTuIaxYNUE1SlwG3YTc4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-fra3-2.cdninstagram.com&amp;_nc_ohc=sKJdfZK9eLkQ7kNvwH2Oc_J&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMzQxNzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=0GCuxrh7S2PLSinUodoPjQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Ofwf8twDEhRCppAzO92vKp4Bgfb5mLT6lr9AKvEAo_w&amp;oe=69DC19C9</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2532\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-44659\" FBFirstSegmentRange=\"1009-85613\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85614-170092\" FBPrefetchSegmentRange=\"1009-85613\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "profile_pic_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/543579175_18522017512026754_6429363176312325029_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzQuYzIifQ&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH3VEjDry6Vs-kfMyuQVEKf7Eg6ikiXZfz50lnFLHgBAstlQPq4Y8QbjVoe7wfCOBQ&_nc_ohc=v0quYpmBS-oQ7kNvwHElxpW&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GCdcZiCC8lNCrc1BAKXDEqC_rzlZbmNDAQAB1501500j-ccb7-5&oh=00_Af0W60qV8jf0vKZHBCAhzj12w6frYIBE-Lfda6858HZHuQ&oe=69DC4FB3&_nc_sid=c024bc",
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
        "profile_pic_url": "https://scontent-fra5-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-fra5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gH3VEjDry6Vs-kfMyuQVEKf7Eg6ikiXZfz50lnFLHgBAstlQPq4Y8QbjVoe7wfCOBQ&_nc_ohc=zov5ST0QeW4Q7kNvwG2YIE4&_nc_gid=0GCuxrh7S2PLSinUodoPjQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0lSLbXM_GWucnf5RwRNx_OXQWK8Q8pD90V5fV9K1PMAQ&oe=69DC4D93&_nc_sid=c024bc",
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
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775657700\" FBManifestIdentifier=\"FsiLs50NKRbMrPbB5Z2pBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1498046678354726a\" bandwidth=\"66810\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66810\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m78/AQOElke-XjvO2ixFipAMNby9AqC5CZmOcY8PcbQDmAwEGdrdvbD58TPi5A5RKS7WbXpTrVlZQip3DhNxjBI2vRela2S063MA11oc5y0.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=XLhOSrzrzoUQ7kNvwGBZLzR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2OWkKnFn7ElYGTQ1JwpVw43eSV-zj_i3KsdI8bAJlW_Q&amp;oe=69D8589E</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQPYF2mAhRbYzYMrI560MWB9XBJqAACyr7szcVbj1WFwaneaOm5BlFHWUM37z1AaOh6Oyo4BIq6T2yeHyTeibfXn.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=wTkgipWqtN0Q7kNvwGEmyBd&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af36vVKM_hP02NXApd6vBX7wvj8kLVv_acM6H6zh9EW0rQ&oe=69DC1E23",
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
            "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE6Q53GCzhClpeVlrU_K0GnWUhB5lFAOJSF6U63yAXaSVc_pzwChRQQAmHBA5Mjh78&_nc_ohc=ic5ODsLE2O8Q7kNvwE2sdLw&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af0x-0gboxvCIxunGFWBdPqmAFAK0Ce4BGTmzW9sjZifLw&oe=69DC204C&_nc_sid=c024bc"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775657701\" FBManifestIdentifier=\"FsqLs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxs71ud+73IoDiqC0wu3LjwPImKTi/7u7BL6Zk9OwssAE/t+w5JmOxQSSmNLH6cjSBerci73BkuQFmJ6qw8jLyAaQj4fa8c2pB8T5kOjGrLcHhqCP7Nm3vAeqnN3Z9IWhDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.1\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"868003729587559v\" bandwidth=\"178266\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1353206\" FBPlaybackResolutionMos=\"0:100,360:56.7,480:54.4,720:53.2,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.1,720:83.8,1080:76.2\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOsCsgfDrcn7Gsyqj04T425mPWmeq8-MeX07h5wqKf_ykgUXeoigrvG2JQeRp4Wd_MdM-ZLa9ORl60gPpY3e_JZiFGCQ5EL6KkXMnk.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Uh48tAtlw1sQ7kNvwHJtfae&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTc4MjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2_x5EOlnp4ZP3uGOAWn3YX5nOUuS-EgpJllbki0HkjVw&amp;oe=69DC1997</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10892\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-78531\" FBFirstSegmentRange=\"1014-106281\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106282-221200\" FBPrefetchSegmentRange=\"1014-106281\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2092036534705762v\" bandwidth=\"240856\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1828322\" FBPlaybackResolutionMos=\"0:100,360:63.6,480:60.6,720:58.1,1080:58.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95,480:93.1,720:88.4,1080:81.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPRuSajZ_hFnjDpVSn1TY6XCtP7Zo9QzDsXmaKDU4mXL33dQv9cZzKhXl7Y_oeRcW9BNsObRl_FpdyfkSlu8ArGYU5-l43-uxy7_sg.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=-0z8YeyvyDgQ7kNvwHPjZr1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjQwODU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3-_S5aZ0D50s6IdocEcoyECdaVxL969rdHqmSGk_p5vg&amp;oe=69DC2C08</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-12646\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-105375\" FBFirstSegmentRange=\"1014-143432\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"143433-293318\" FBPrefetchSegmentRange=\"1014-143432\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1267502918297183v\" bandwidth=\"326220\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2476312\" FBPlaybackResolutionMos=\"0:100,360:69,480:66,720:63.5,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.4,480:95.3,720:93.4,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBZheSdr-Op1k9B7pYwuciRaL5RCC2XcBVLkVwDPXAKrAhlrALgBooKgZk6nCMZz5AvNoGknQE18-kCW9-RNH_qVgCyawe5etIWbE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=4ClMe01ofx0Q7kNvwErjZeR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzI2MjIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3jdTArW3ZgayrZA1rwBfkTk7uNFVGirnaQYZFVv7zGQw&amp;oe=69DC1F98</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-15483\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-142126\" FBFirstSegmentRange=\"1014-195190\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"195191-393663\" FBPrefetchSegmentRange=\"1014-195190\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1277876490344447v\" bandwidth=\"409602\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3109259\" FBPlaybackResolutionMos=\"0:100,360:73,480:69.8,720:67,1080:65.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.7,720:95.4,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw5-3.cdninstagram.com/o1/v/t2/f2/m367/AQPxkQrl5cFyNncjOUGRq3XWMGmEnR7xzXjtdkfQlw0oreW4eSXmKA9eBGchHF9ByGL1ldZ-V_-LDFLMXxx4oytbIqVxuBwnRf-_tR0.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;_nc_ohc=5YrnOUUJMr4Q7kNvwETcKvs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDA5NjAyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3W-F1K3FfUMCLwizPwRrQITce81fWUR5p3_-R1BhKCIg&amp;oe=69DC3457</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16985\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-176185\" FBFirstSegmentRange=\"1014-244141\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"244142-487399\" FBPrefetchSegmentRange=\"1014-244141\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1848477759129484v\" bandwidth=\"540603\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4103680\" FBPlaybackResolutionMos=\"0:100,360:77,480:74,720:70.7,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.24,480:98,720:97.4,1080:93.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP2bW0aIfz99a4ARx2Q2fPwwUvSZlmUT1jxqzlfSPxqDy_XKQdY1A9deJRHs78I9y2z_ngWT2zfhDIKZ8-XZxBrQWFF9SDm2muWNnE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=M35pMpEQ64sQ7kNvwGozJDC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NTQwNjAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2JYHE9XRoXE1i3m_qiTrYloO5QPKiivN6ZFtEhSTmr4Q&amp;oe=69DC4906</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-18644\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-229855\" FBFirstSegmentRange=\"1014-321368\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"321369-630140\" FBPrefetchSegmentRange=\"1014-321368\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1588945909073417v\" bandwidth=\"681362\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"5172172\" FBPlaybackResolutionMos=\"0:100,360:80.4,480:76.6,720:73.2,1080:70.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.62,480:98.37,720:98.59,1080:95.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-3.cdninstagram.com/o1/v/t2/f2/m367/AQPuKZF2qKICjs08-k_G1H8gucF1aCSpWB6stiwUGXWNvKfX5Hm_pNaY4z6GYTR0ZmsxXCYFw3SGDP8cejuR9yWwzxdzv-J159SieXo.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;_nc_ohc=jd4D7ZlmtxMQ7kNvwFbdKxB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjgxMzYyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af23WrD8jq1jpn4mfaiznqo80J8H2WKt0Zb_HCpzwlt5Lg&amp;oe=69DC4007</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-20592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-288895\" FBFirstSegmentRange=\"1014-405533\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"405534-781198\" FBPrefetchSegmentRange=\"1014-405533\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2061822901412808v\" bandwidth=\"912497\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6926702\" FBPlaybackResolutionMos=\"0:100,360:83.9,480:79.9,720:75.7,1080:72.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.077,480:98.93,720:99.306,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOjiwsO48rCaOF6m6s4bgg66iRhLGj5CKjR4DDmQ8T9kE2SvEWALkKtR50Wk2wGAMLc1Ws3pNhZSA9Y-QIiggu_wdfx_Bl0gwfgXDQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=fEsXwzzt-3AQ7kNvwFIhL0G&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6OTEyNDk3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ICHQG9JrKXOmhJgjSOBb-viv8Hu2XLQqA40R_Pbokxw&amp;oe=69DC387A</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-23580\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-385865\" FBFirstSegmentRange=\"1014-544870\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"544871-1019514\" FBPrefetchSegmentRange=\"1014-544870\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1627595234965301v\" bandwidth=\"1235000\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"9374797\" FBPlaybackResolutionMos=\"0:100,360:86.4,480:82.8,720:77.8,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.386,480:99.342,720:99.569,1080:99.632\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-3.cdninstagram.com/o1/v/t2/f2/m367/AQM_p3Fq6rDYprSjJ8-MUlNGuff4JfkbCcT-LYH34W9o85XM1tWSkDeCFiP_sdVayBjAG_vXE0vYkHj0noxXvuN1eESyaLJtPOQ3Rmg.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;_nc_ohc=YK0MlTWtfdIQ7kNvwGzoLTt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTIzNTAwMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af13seZ_5yqSmBlBAPUKovlTQUXCa7PlR4EWCu5gDkPF5A&amp;oe=69DC4156</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-32211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-518374\" FBFirstSegmentRange=\"1014-739833\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"739834-1405190\" FBPrefetchSegmentRange=\"1014-739833\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4294793980782357a\" bandwidth=\"46380\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46380\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"353137\" FBPaqMos=\"87.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9GI-VauacxM2tCfwmiCOijhyH33zBWrM0Dr4JwD6i2FjABcTvvBGOXIydEyGVXVx6wkUjNuDAtapI93ufxCNL1tRZuAP-HRtBv50.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=Uo8ixeKIRUsQ7kNvwGH7M28&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjUxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2L1EDC_iTHZXNwLOpsR8CsdEc0uzGcs70twzI6XqS84A&amp;oe=69DC28AA</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2136\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-14938\" FBFirstSegmentRange=\"1025-28400\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28401-56361\" FBPrefetchSegmentRange=\"1025-28400\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1256673039910436a\" bandwidth=\"74812\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74812\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"568992\" FBPaqMos=\"89.65\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-3.cdninstagram.com/o1/v/t2/f2/m367/AQPA0IU4X5qD93OmmaSc1st7oueEaOmYwYCBhH3T3wOKN7WutkRMOZ1TDwC1ugFmlc5yKEeuM_xeo_vD4IzH2AbUDhA7xa2uuL_kti8.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-3.cdninstagram.com&amp;_nc_ohc=H10A9jvUydQQ7kNvwFc9CWg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NDk0NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ITq8Zmzb5y9Z6jDcGM-nBimR1RC2J5k5cNdzSFMkgDg&amp;oe=69DC2DE2</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21486\" FBFirstSegmentRange=\"1026-43481\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"43482-90615\" FBPrefetchSegmentRange=\"1026-43481\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"878713468520453a\" bandwidth=\"108352\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108352\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"823623\" FBPaqMos=\"83.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOhb37d5jmr5MvSl8eT28PWBputzk-lecQ-RBUBedLEv96EozZbcoK_AR-dP3eFTj3ZDuOnoWe6DiibSbh3Vjc_rcGupQpI3Z2uCnA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=qIB9a-mC_CIQ7kNvwGL-vTp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDg0ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ZTg8iTUxuUM5Li99LLtAL7gC2Wf05JYoVT3ecVd3Vwg&amp;oe=69DC1D87</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2395\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-30757\" FBFirstSegmentRange=\"1021-62738\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62739-132935\" FBPrefetchSegmentRange=\"1021-62738\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2103223183861763a\" bandwidth=\"143947\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"143947\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1093864\" FBPaqMos=\"87.00\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOgH1TOj2U7Ucn9wQoBfkebTHLZ9A_EoIFXsEJ2CkC1MsQUoWoasexRt0uwJQMyHQr8MmjxA15OisXxvCobhDmp05SCyaFAKp2_vFI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=X7gcVcXpzlUQ7kNvwENgb4o&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxNDQwODEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2phQFWbDo3nELhGiSs-WLzG2HNXjrw99jHPw42csB8bA&amp;oe=69DC1AE7</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-45040\" FBFirstSegmentRange=\"1021-86500\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"86501-176000\" FBPrefetchSegmentRange=\"1021-86500\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE6Q53GCzhClpeVlrU_K0GnWUhB5lFAOJSF6U63yAXaSVc_pzwChRQQAmHBA5Mjh78&_nc_ohc=XbeNvhLXv28Q7kNvwH38lmO&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af19Keuv6yoiCoFZQdKMYeXFXuKDT2UJ7MIi974grxbiBw&oe=69DC19A9&_nc_sid=c024bc",
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
      "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwHdNHS6&_nc_oc=AdqeODVALpXv69i55DnnhHCmX8ppYX_wsHJFHuv_NcJ6956WbUCt-ZGRXdejW0fbFyI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_ss=7a3ba&oh=00_Af3DDUIiSgd8QN7ZVwwMh1T_IxHP-CJDSjGKnm3av-UtWQ&oe=69DC2AD5",
      "location": null,
      "user": {
        "pk": "787132",
        "id": "787132",
        "username": "natgeo",
        "full_name": "National Geographic",
        "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE6Q53GCzhClpeVlrU_K0GnWUhB5lFAOJSF6U63yAXaSVc_pzwChRQQAmHBA5Mjh78&_nc_ohc=XbeNvhLXv28Q7kNvwH38lmO&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af19Keuv6yoiCoFZQdKMYeXFXuKDT2UJ7MIi974grxbiBw&oe=69DC19A9&_nc_sid=c024bc",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": true
      },
      "comment_count": 65,
      "comments_disabled": false,
      "like_count": 11040,
      "play_count": 1479078,
      "has_liked": false,
      "caption_text": "In Hoppers, Piper Curda’s character Mabel explored her sense of wonder for the natural world with the help of hopping technology. For now, we still have to do it the old-fashioned way.\n\nSee Disney and Pixar’s new movie Hoppers, now playing, only in theaters, and step into wonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwE4rQwU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2GVu_ZFg_C_ec-hcuD1UfYeWZlJmXHnVYaKvQRb4sS-A&oe=69D83578",
      "view_count": 0,
      "video_duration": 55.44499969482422,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            13479,
            26958
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwHdNHS6&_nc_oc=AdqeODVALpXv69i55DnnhHCmX8ppYX_wsHJFHuv_NcJ6956WbUCt-ZGRXdejW0fbFyI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_ss=7a3ba&oh=00_Af3DDUIiSgd8QN7ZVwwMh1T_IxHP-CJDSjGKnm3av-UtWQ&oe=69DC2AD5",
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
          "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwE4rQwU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2GVu_ZFg_C_ec-hcuD1UfYeWZlJmXHnVYaKvQRb4sS-A&oe=69D83578",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1113315,
          "height": 1280,
          "id": "2358585431274531v",
          "type": 102,
          "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwE4rQwU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2GVu_ZFg_C_ec-hcuD1UfYeWZlJmXHnVYaKvQRb4sS-A&oe=69D83578",
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
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775657700\" FBManifestIdentifier=\"FsiLs50NKRbEl5Tt0tWmAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"929459223037410a\" bandwidth=\"60820\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"60820\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQN38tw9LWdIk_CWlJ0ze2Ayn07LgXtA4TMaLXc-6SODK58HBqKnlOKk8_LTSIHFsE3VGUlntYj8FPrehpb5VftWJE3s0U_LvQcQ0p4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=ZHLfVpYSwAwQ7kNvwGVz1Mc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo2MDk5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0Xo3R7fOpTUTLqH046CHrecjWtS70Xdhuog5z6ZE3ATg&amp;oe=69D82D73</BaseURL><SegmentBase indexRange=\"824-1191\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKBMTmsUUaSlY28FrQeX4c4T6dijF6gtmaEyTFBN6pFY5bZ5DsQbcUjfr7pEffSR4eVHh1ugsHyMjH1cbkv8Kz.mp4?strext=1&_nc_cat=106&_nc_sid=8bf8fe&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=VR1-k3frXTsQ7kNvwGtag1V&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0PgqiHqtGYe_6rFR1xGTDI1xKn_wyzHpfTsNdBqQ00Rg&oe=69DC1B8C",
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
            "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE6Q53GCzhClpeVlrU_K0GnWUhB5lFAOJSF6U63yAXaSVc_pzwChRQQAmHBA5Mjh78&_nc_ohc=XbeNvhLXv28Q7kNvwH38lmO&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af19Keuv6yoiCoFZQdKMYeXFXuKDT2UJ7MIi974grxbiBw&oe=69DC19A9&_nc_sid=c024bc"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775657701\" FBManifestIdentifier=\"FsqLs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxtbm7f2IgpUD7OHlgsygpwOI9qGs6c69A4K35IPMyMEDsI3CoKTHvgSc252C4sXBBPyF6YussKgF9KKOwMXurwXYlsvU5LXeBdjS1K7XuegF6PTG0/GH9wW+g9vN5+3SByIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:73.2\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"890639983950251v\" bandwidth=\"148183\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1026735\" FBPlaybackResolutionMos=\"0:100,360:77,480:75.4,720:74.2,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:93.1,720:92.5,1080:88.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxVTdb31AW_INujP1IDvNHV263--MPtveeFNN3GUuUVYCWKFeS7YZ9ZN2G12w1BpIi_FdawNocSzgpCnZ_RmsvfPjiy1uTBHb9oZw.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=Azv6S-cYlSkQ7kNvwEGWStv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTQ4MTgzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3tDJ3H0KIZBJyiEj68iZRSiGD-22l96cY05dUTyvhbQw&amp;oe=69DC300E</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-11627\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-38956\" FBFirstSegmentRange=\"1002-59102\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"59103-123876\" FBPrefetchSegmentRange=\"1002-59102\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1496166365471102v\" bandwidth=\"217161\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1504667\" FBPlaybackResolutionMos=\"0:100,360:81.6,480:79.3,720:77.4,1080:76.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:95.5,720:95.4,1080:91.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0yhiq2c2nWFCoYYsXHyN0n4pQ1H3Bf1PillRJPvA7F7s4T2vZEWWlnN1ab7wlhBx2qkPUdSqWmZq9YiCbgQr1iy6TnVK92GJFM7E.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=-GnWOEbhFFMQ7kNvwFnPI1y&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MjE3MTYxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0GRibawPA066aDVekfCsvBCFvs2axzoXeMX66eBk_ESA&amp;oe=69DC271A</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-15046\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-52809\" FBFirstSegmentRange=\"1002-81554\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"81555-172554\" FBPrefetchSegmentRange=\"1002-81554\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1637064280544428v\" bandwidth=\"297468\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2061099\" FBPlaybackResolutionMos=\"0:100,360:85.4,480:83.2,720:81,1080:79.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.5,480:97.1,720:97.8,1080:94\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNmpoeNdw7yb2DNMihh-Q2G15Y477O-Sk1OLg5Yvc1SF5s2DvEEWcyZxNMIPHB9gTiEJuesLauW023efqZ9CuKWYNgVahVJF3UIkRc.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=DWIM7dIPpcYQ7kNvwEtIf4t&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mjk3NDY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2BqlcNcqMAxETe_z-lKCc3V_g0a99k0ZBCYjvbGPSmog&amp;oe=69DC3FEE</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-18788\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-68106\" FBFirstSegmentRange=\"1002-106801\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106802-227120\" FBPrefetchSegmentRange=\"1002-106801\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"930746796390518v\" bandwidth=\"386132\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2675439\" FBPlaybackResolutionMos=\"0:100,360:87.4,480:85.4,720:83.2,1080:81\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.11,480:98,720:98.9,1080:95.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOqmazZV0GgC-FMAgX5Uo4Hzr4dpsUwPLWUSkWVzIH2EIopdalxgjleoQbUfcUfP1apdP-4Gsa_iSGhTS3l313F1z6FbA8TyS6K2AY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=XpZ2XTBJDXAQ7kNvwFIWvtX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mzg2MTMyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Z25sgA_hi-pJvPIaiKlxr45B3QX32FLJgt9jVRsnREg&amp;oe=69DC26CC</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-22235\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-83355\" FBFirstSegmentRange=\"1002-132950\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"132951-285253\" FBPrefetchSegmentRange=\"1002-132950\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1263463985333080v\" bandwidth=\"479911\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3325212\" FBPlaybackResolutionMos=\"0:100,360:88.9,480:86.9,720:84.7,1080:82.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.46,480:98.4,720:99.414,1080:96.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN5Sl_4u8bg21xVtk-cIUfm9Z6DIbmrVvFA9a9N55F9NWJNHo03righvcgXtgSk_3JVH4wvKy4OTeNsgcwEtoacof_IARGxdKkAT-A.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=P7dFgXaWfIwQ7kNvwG5RvD3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NDc5OTExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af03MBgONggljQb9_9OSh_POrbDmk6ouuDa0oRU00mjGsg&amp;oe=69DC25A8</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-26049\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-100642\" FBFirstSegmentRange=\"1002-162120\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"162121-346006\" FBPrefetchSegmentRange=\"1002-162120\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1669194164264244v\" bandwidth=\"600336\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4159614\" FBPlaybackResolutionMos=\"0:100,360:90.2,480:88.2,720:86,1080:83.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.75,480:98.79,720:99.619,1080:97.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOkSM-p5C4-U6nKoTCQGR9QEo9t8_5IVg-ngkZWi13nRqVLUyRlAs1Es-YozyB9s8bjtNsK18hWCL1Of88sI3ZDe_gO2S45lP4yjWI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=8zqHITencNwQ7kNvwHHuJX7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NjAwMzM2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af13ERRKhV4QgKXsf9WM_JTkvcjJ60gsf5trC2qoNY0jcQ&amp;oe=69DC3AC3</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-30771\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-121891\" FBFirstSegmentRange=\"1002-198284\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"198285-422683\" FBPrefetchSegmentRange=\"1002-198284\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"988608596839873v\" bandwidth=\"797098\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"5522936\" FBPlaybackResolutionMos=\"0:100,360:91.3,480:89.4,720:87.2,1080:84.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.026,480:99.172,720:99.732,1080:97.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMf3Rx8OOzEgPrCPNBR-0Nt-fwNaR6LdwmdWPUwzv4ulTwm_6h2bijtJ5Bjd87z0Jr-dXFj9FkGKtlRGWG6WeJW59Fiu3efb5LsrRI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=B11mdo9l0D0Q7kNvwGBr2B_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Nzk3MDk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1HfxKqsS83OAkdpz-kY3MhBiEJuD3YEN58qwihEB9pLA&amp;oe=69DC4992</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-37057\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-156105\" FBFirstSegmentRange=\"1002-256214\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"256215-544176\" FBPrefetchSegmentRange=\"1002-256214\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2152531255582943v\" bandwidth=\"1154217\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"7997347\" FBPlaybackResolutionMos=\"0:100,360:92.4,480:90.7,720:88.4,1080:87\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.557,480:99.564,720:99.814,1080:99.824\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNSJdZpIRgVNqEBZdYq3cRarDru00HEWTghNg_iisXPQJn1ZojfEEAKYKMxJ1XCUfUglkRb6_gx6l6OzyKpZWsTXEQRU05M7RCeihQ.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=K8EwAJQ3wUIQ7kNvwFpG8Zd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTE1NDIxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0okTeiWfLECurq-o_Z4s1fBamiZGq9jUPTQdzaIeFxHg&amp;oe=69DC40FD</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-50470\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-211892\" FBFirstSegmentRange=\"1002-345895\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"345896-752596\" FBPrefetchSegmentRange=\"1002-345895\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1615007113110956a\" bandwidth=\"45829\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45829\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"318635\" FBPaqMos=\"90.73\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOq8zAQzpeRCoSQuovKRKQeNbycFlDBjsuggCgJzVUNsydkP6wpqSMV87VACc6egwIxdyoZ9qyuATjsxvSkWgWUtLCaKeDUW5vI2l0.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=n8c3OFNcOe4Q7kNvwFUWaqf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo0NTk3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ZNmdlnhiLyb9ZDL8J1BKTwV7pbtxw8uG2vmq30K1TjA&amp;oe=69DC2330</BaseURL><SegmentBase indexRange=\"837-1012\" timescale=\"48000\" FBMinimumPrefetchRange=\"1013-2182\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1013-15598\" FBFirstSegmentRange=\"1013-28913\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28914-57244\" FBPrefetchSegmentRange=\"1013-28913\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1270034985105102a\" bandwidth=\"72011\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"72011\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"500096\" FBPaqMos=\"90.72\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNETgTPe23OWiy-KGFj4O0xaNmi9xW8k8We4jlz_Lesh43O4RfyZWEg4kgQ77avCmAh4dhCO9ERkZrtXpEBa1nLDn-iaNXSGANeubo.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=wOOs-JEmecsQ7kNvwG2kjw-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo3MjE1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1lxJyANYDwBywArdlmqwW6k2z9z5j9y51SO5votRiLZg&amp;oe=69DC26BF</BaseURL><SegmentBase indexRange=\"838-1013\" timescale=\"48000\" FBMinimumPrefetchRange=\"1014-2538\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-26077\" FBFirstSegmentRange=\"1014-48598\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48599-97300\" FBPrefetchSegmentRange=\"1014-48598\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"979919517793668a\" bandwidth=\"103761\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"103761\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"720138\" FBPaqMos=\"88.08\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNOpf9BEo2_A4jYtakOEtpNQQZDYD9C0aIFAN-Q6y8Ina7CtFSkF_92RvlAvk1DGfzRoyEa6eCluUBrw77Kir2QY9JUObENLk8IZsE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=sGdWzzK2ve0Q7kNvwFe1yzN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMDM5MDYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0pPDORuGbMSXkg-CVrwzANzTsJo5wpSicxBS17563PfQ&amp;oe=69DC1E0E</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2467\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-36815\" FBFirstSegmentRange=\"1009-70144\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"70145-139522\" FBPrefetchSegmentRange=\"1009-70144\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1512628090423482a\" bandwidth=\"134031\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"134031\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"929932\" FBPaqMos=\"90.49\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMDkCHmLVEnsU6T5_aC7ZlGvMakuRW1O3OnJZfxZuCHE1fs0cf1weWXn_tPspjek6E1p7CHcVLpGZLRSFGGTuIaxYNUE1SlwG3YTc4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=sKJdfZK9eLkQ7kNvwEE2qtl&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMzQxNzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=qKesjlqkxd5lN7tdefVRRQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1-17PjRUxkUXm4g0Vqno0jg5pvM_NRuVMytSP4TXwa0g&amp;oe=69DC19C9</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2532\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-44659\" FBFirstSegmentRange=\"1009-85613\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85614-170092\" FBPrefetchSegmentRange=\"1009-85613\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/543579175_18522017512026754_6429363176312325029_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzQuYzIifQ&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE6Q53GCzhClpeVlrU_K0GnWUhB5lFAOJSF6U63yAXaSVc_pzwChRQQAmHBA5Mjh78&_nc_ohc=v0quYpmBS-oQ7kNvwFqc6fN&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GCdcZiCC8lNCrc1BAKXDEqC_rzlZbmNDAQAB1501500j-ccb7-5&oh=00_Af0NVoEqBGUyaEX0UfA9xUC8WYZHwHrdNgb9ycv1zXm_Eg&oe=69DC4FB3&_nc_sid=c024bc",
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
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gE6Q53GCzhClpeVlrU_K0GnWUhB5lFAOJSF6U63yAXaSVc_pzwChRQQAmHBA5Mjh78&_nc_ohc=zov5ST0QeW4Q7kNvwFjSS9n&_nc_gid=qKesjlqkxd5lN7tdefVRRQ&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af3HMLR7dqHFQbUdtmh-X1I1XRGhrkTTKCl43RjFutCWCw&oe=69DC4D93&_nc_sid=c024bc",
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
  "QVFEa091SHFSRDZRd3ptdVExTHpTdEZ1VWlJd1VrWkZQRGRkYmRFNGJGZlZnRUJFcUlrYzIySjJxSXBneGtRSm9UbkI2N0c3b0xYRmQ3S2hud0ZEeWpHVQ=="
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
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.02S\" FBManifestTimestamp=\"1775657728\" FBManifestIdentifier=\"FoCMs50NKRbkmJfH7/yMBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.02S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwFzs5Ra&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njc5NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3HPwJfsOrfYxk7ftV90DV0o-Vm_Fm4A2SJqkeagJLoTw&amp;oe=69D83B87</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "progressive_download_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m86/AQM3BWmWT9DCIR_4a6ETqY74iK_vSJ0mGCY5KURpD0ZI6aeamU2Fve1dXA5lCRBiztE1g_SEXMn_Iq_pDtwv8Zw.mp4?_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=3yv_Gp1gyOgQ7kNvwFh3ZFS&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2bQPLwM59Ea7pc2-p0eu0AQ3xjTzzyXOl41xd0NwOglw&oe=69D8476D",
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
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHL1lTdiNjY4kTrhoDkC8-PJSK_2evPUSd62XjjV7A_3js9WGl3IjZWqxx6HMyo6Ww&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1terAkUEAjzt9o-htbk2jZeRImjLKt3-pbKFAOnahLMA&oe=69DC19A9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.101768S\" FBDeliveryExperimentName=\"ig4a_stall_profile_tuning_v2\" FBDeliveryExperimentGroup=\"test_1_6\" FBManifestTimestamp=\"1775657728\" FBManifestIdentifier=\"FoCMs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxraJxpnwkvECjNnxgZuPjwT4stmliZm5BLzN2fTZweUFmpjfwsvS2Ab2jc22sdnYBuSVwq6x85UHzIqHl+PItgfq7MGKwvrFB9bylbjgtpcL0pa399PQmQyK78y/iIvqDxwYHWlnNGFfdmlkZW9fcW9lX3N0YWxsX3Byb2ZpbGVzGBxpZzRhX3N0YWxsX3Byb2ZpbGVfdHVuaW5nX3YyGAh0ZXN0XzFfNgASGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyIsGRgFbGlnaHQAFg4UABIUAgA=\"><Period id=\"0\" duration=\"PT60.101768S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"811763878117979v\" bandwidth=\"262728\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1973809\" FBPlaybackResolutionMos=\"0:100,360:62.9,480:58.1,720:53.3,1080:50.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.8,720:86.4,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP4s_c0uSAuy00HwODOQxGqL_KE1A5w9lnFiX0JfdCCMJTPukZiwIvC7uddABS-MUJBTNgcjIqVwxgJQEL9EM2gpulN4btvCIHeIYE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=-PmLEytgxDcQ7kNvwFJpfbh&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjYyNzI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0OC8F-gvKsbpOi1MONCiVYCirbSK1OqrcIbwjI-9gx1g&amp;oe=69DC2C4E</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-6086\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-129562\" FBFirstSegmentRange=\"1014-166973\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"166974-328722\" FBPrefetchSegmentRange=\"1014-166973\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1159146579572294v\" bandwidth=\"377484\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2835938\" FBPlaybackResolutionMos=\"0:100,360:68.5,480:63.8,720:58.3,1080:55.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.8,480:92.9,720:90.7,1080:85.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMeaQpVDw5N0MxBLbLlLw4lSRHBoeCxqRWEdQxK9-uXl9boeDW4fLNwvdk093JFHDC5HeJYG-12qm4BaWfLYFo8emoy6rS4rnz8i4c.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=Lw0vzjNBHBgQ7kNvwHQbYmv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6Mzc3NDg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3ISrnUBVIGLjLlW4ljpjxEFZYHttyBA_8TJRJKWKp9xA&amp;oe=69DC2EDB</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-7174\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-184877\" FBFirstSegmentRange=\"1014-237575\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"237576-461968\" FBPrefetchSegmentRange=\"1014-237575\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2124162255043381v\" bandwidth=\"485928\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3650647\" FBPlaybackResolutionMos=\"0:100,360:71.5,480:67,720:61.5,1080:57.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:94.7,720:92.9,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOz6ELjZ949BogdJm_QNe1EGQjv1zTfVS_ZRTHhaA80l6nyo0X-36y79QprnZ4mpheYpPgrlqKovz2Z7nwAtkupZFh-qPPgSofw_SI.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=RIdyZ7swaFgQ7kNvwEL1EOs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDg1OTI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af34U9o2RUrtgrAk3ZFOFDTcCXnsUFPF7XUleVlf6xx-aw&amp;oe=69DC2D2D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8131\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-237174\" FBFirstSegmentRange=\"1014-303731\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"303732-578455\" FBPrefetchSegmentRange=\"1014-303731\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1251674976627900v\" bandwidth=\"619033\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"4650624\" FBPlaybackResolutionMos=\"0:100,360:74,480:69.7,720:64.2,1080:60.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95.9,720:94.7,1080:90.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNqHjWw34JU1zEWGF9C1h7VwlLIrqdJWbZ4OklUXgX1JUvMWrcXQ-RHcIlLZ5-leK-3oztau40NjRSFd8sWnMMpU8GdkzR1wupOZ10.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=pcYzS9tQp0IQ7kNvwFXIf7R&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjE5MDMzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2R-zAcKSF6Fm1sIdAmhg89RvAOGnkDpJnBfyNXL3NDcA&amp;oe=69DC29CC</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8867\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-298106\" FBFirstSegmentRange=\"1014-381215\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"381216-715818\" FBPrefetchSegmentRange=\"1014-381215\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2090322355085990v\" bandwidth=\"859541\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"6457494\" FBPlaybackResolutionMos=\"0:100,360:76.8,480:72.8,720:67.2,1080:63\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.8,720:96.6,1080:93.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOiOZhsUH6TLkrnE9FwF7XkrsQrJbO4ranASPXWOp_kfZQnOZspqXMH9zwqL2A5ODtpWwSfSYjqVdnN5JwtnoKgDmzpRneeR6UjSf0.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=rP_jkdcldEoQ7kNvwEFEkHy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6ODU5NTQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3FCE88fiZx8C7EedUhdtaeCzKc1GT3i41tWWgIx-Jseg&amp;oe=69DC51BD</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10444\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-407931\" FBFirstSegmentRange=\"1014-520416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"520417-950605\" FBPrefetchSegmentRange=\"1014-520416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1630604991607646v\" bandwidth=\"1133257\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"8513850\" FBPlaybackResolutionMos=\"0:100,360:79.2,480:74.9,720:69.3,1080:64.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.07,480:97.5,720:97.6,1080:94.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQP6A5LFkcBJyvdNdliF_xHUaxD51PWWWorNb6dDtDzQ7XD8gAviBfoW1AVfcumwubAQFQ032SHQZ6jcxptLJTaTYNl8toVCs_2M5DY.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=MiND23-EIg0Q7kNvwH8D37Q&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTEzMzI1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3CuwxzzQnweI7ZlUM8Y6M01DO17rLY_ucy8r-I7jcKbg&amp;oe=69DC478B</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-11592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-528888\" FBFirstSegmentRange=\"1014-673311\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"673312-1205023\" FBPrefetchSegmentRange=\"1014-673311\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4455411234741189v\" bandwidth=\"1595477\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"11986380\" FBPlaybackResolutionMos=\"0:100,360:81.7,480:76.7,720:71.1,1080:66.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.55,480:98.2,720:98.36,1080:96.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO_EY8JAwoG2qGh3eNttzDv3bWaZbosyVqFsbHFSUR4ZIUqvEF3dIs_iUyiWHHffWx17NcAJslxKGK2F9yc3KKxTtB-3yov2ohU284.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=IcB0Uykb9IYQ7kNvwEr8XLz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTU5NTQ3NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2jqnrMzvg6vzY7aYqEFm-JCJHoorvZSLxxHs8rV_m06w&amp;oe=69DC368D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-13404\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-713619\" FBFirstSegmentRange=\"1014-916365\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"916366-1632404\" FBPrefetchSegmentRange=\"1014-916365\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1883899549033339v\" bandwidth=\"2141971\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"16092034\" FBPlaybackResolutionMos=\"0:100,360:84.6,480:79.8,720:74.1,1080:69.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.68,480:98.58,720:98.79,1080:98.46\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMAha-Ay45jS94TL8ynk5QQMBTTvF50BcTEUfE52AZhmIWcW5z7BSGD7RuWJzR1UJ1XHTtxnis--HnzX7LnQt9XFRHTMhfDthD67SM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=teHbZCY8fNsQ7kNvwFKqesR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjE0MTk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3GOa4Wnd9fnpcWrZNxzqsLgVgfZBOcMdjkUFGSyd9VxQ&amp;oe=69DC4BD5</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-962472\" FBFirstSegmentRange=\"1014-1247892\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1247893-2246471\" FBPrefetchSegmentRange=\"1014-1247892\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2018486635742578a\" bandwidth=\"46242\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46242\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"347952\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN6d2WH86jHFShcbXf9sjQbZkQC0xUp0rW7EDnG4Bq4tXew6Pz2MHtHSrpUQKKBEGJCn216bnzZ43Z6y4oPrg8CshaIRDStXBf_2m8.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=p_6H5YxvVOsQ7kNvwGC4RUg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjM3OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1aQ2jGjuFH0z7O90PlJZ7kQOSotjesJxygi7z-JZMBOQ&amp;oe=69DC4148</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2090\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-13193\" FBFirstSegmentRange=\"1025-25675\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"25676-52073\" FBPrefetchSegmentRange=\"1025-25675\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"3434060956755369a\" bandwidth=\"76016\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"76016\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"571334\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPiBT48Or08Wq2GueJ_a1ZGlP5QobL4jCYts8LWjbigiJaGQYlGIGdimLvTRUGI0Qy06ehqd8LGIkG1qUx2Q1PSVeSpBpibYNGQTcw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=jks4A86ZRgcQ7kNvwGnz6S2&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NjE1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2LKNAhE9wt5Pb_EZD4o2kzu08TzRML8BZlk5w6Ra0Psw&amp;oe=69DC2C65</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2475\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21765\" FBFirstSegmentRange=\"1026-40537\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"40538-84371\" FBPrefetchSegmentRange=\"1026-40537\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1883782792341005a\" bandwidth=\"105481\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"105481\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"792391\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNe18lXJWbOpFruCxw7tvHWDJwvLtPJ4A3aWliKSnQwQggwuFpt247QNTOPKpxOYARAZ0l711AUP70HG4efjUphK33t2U_SaotfKeo.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=4RJy2Aqlc90Q7kNvwFCt4iP&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDU2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3gEdb2bgEddcOhDt8JMJW0uYm4g7HIUkJRl21RX8BBkA&amp;oe=69DC4B9E</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2371\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-29113\" FBFirstSegmentRange=\"1021-57428\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"57429-121150\" FBPrefetchSegmentRange=\"1021-57428\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"3147742935432363a\" bandwidth=\"137156\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137156\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1030031\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQP_rTgUjxqk_-kh-SP-bwQXBAWsh2FhnEOAntOUAYLiE6AGbZrgLCCQ311RK6AMTE9vBeDWK_JptQx8gsbsogY_ivE-bvNPRZah-eI.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=0oFa_fCas-kQ7kNvwG-P0qq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMzcyOTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0j4th7RaVdOFZUHXG69jErGjdvllSZHSiO7Tek1m9Klg&amp;oe=69DC45AD</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2418\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-35310\" FBFirstSegmentRange=\"1021-75028\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"75029-156364\" FBPrefetchSegmentRange=\"1021-75028\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHL1lTdiNjY4kTrhoDkC8-PJSK_2evPUSd62XjjV7A_3js9WGl3IjZWqxx6HMyo6Ww&_nc_ohc=zov5ST0QeW4Q7kNvwHd9Pty&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af152SNFJN4OZQ8WwHV2ICaiIGoTuolXnMwwzXRb65Z_tg&oe=69DC4D93&_nc_sid=b41fef",
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
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/656558113_18577653481026735_1735858011052165396_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHL1lTdiNjY4kTrhoDkC8-PJSK_2evPUSd62XjjV7A_3js9WGl3IjZWqxx6HMyo6Ww&_nc_ohc=HX8JmLcZS9cQ7kNvwFpU63f&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCFIIievNH8ERwBCABTJRwGqARcYbmNDAQAB1501500j-ccb7-5&oh=00_Af0I029nwnUaWKz8C_ZNN9fT_N63o8ACixul7fKlTktKVQ&oe=69DC2203&_nc_sid=b41fef",
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
    "thumbnail_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwHcIZWZ&_nc_oc=Ado83B0s5jz8dfuXJcC2_3LwTE9PL6gbnbNffbCb9Fqedq4mnY6cjZuyYpF2INOhly4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_ss=7a3ba&oh=00_Af3h2HpPowet5yGLo_tAr12y6JsHSL6XG3Oj_TEeeAZPyg&oe=69DC198A",
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
    "comment_count": 612,
    "comments_disabled": false,
    "like_count": 66049,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwGJs1C8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3TzTrIn9KaOG0Oy4USfwWK9omriIH9Aaf0vFlk9ZlBiQ&oe=69D848EB",
    "view_count": 0,
    "video_duration": 60.07400131225586,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          48270,
          96540
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwHcIZWZ&_nc_oc=Ado83B0s5jz8dfuXJcC2_3LwTE9PL6gbnbNffbCb9Fqedq4mnY6cjZuyYpF2INOhly4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_ss=7a3ba&oh=00_Af3h2HpPowet5yGLo_tAr12y6JsHSL6XG3Oj_TEeeAZPyg&oe=69DC198A",
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
        "url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwGJs1C8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3TzTrIn9KaOG0Oy4USfwWK9omriIH9Aaf0vFlk9ZlBiQ&oe=69D848EB",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 102,
        "url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwGJs1C8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3TzTrIn9KaOG0Oy4USfwWK9omriIH9Aaf0vFlk9ZlBiQ&oe=69D848EB",
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
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775657728\" FBManifestIdentifier=\"FoCMs50NKRb65a+KkPmzCSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwHqA7mP&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af0tKXI7crizVAYZrWL01_MrU8IROdgZ3JCYzORCmsgbLw&amp;oe=69D82A43</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "progressive_download_url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOu1cJkIUYpfLz5hsq6b4bAI93Dsnj-0FVN5QJfDUtHrdxoyYljTBeDYR-FHSZ5LvVWtD_zp4sNL8fsO46SW16u.mp4?_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=zRv5taEP1NwQ7kNvwFVb3f2&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1VNJsBCPQzxYh_XvJi_bLnByWteOng7xj9mAi4Tdar0w&oe=69D8409F",
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
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHL1lTdiNjY4kTrhoDkC8-PJSK_2evPUSd62XjjV7A_3js9WGl3IjZWqxx6HMyo6Ww&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1terAkUEAjzt9o-htbk2jZeRImjLKt3-pbKFAOnahLMA&oe=69DC19A9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBDeliveryExperimentName=\"ig4a_stall_profile_tuning_v2\" FBDeliveryExperimentGroup=\"test_1_6\" FBManifestTimestamp=\"1775657728\" FBManifestIdentifier=\"FoCMs50NGBVyMmF2MS1yMWdlbjJ2cDktc3ItbTMZts6vz+q68+cCloW29/706gKYpt6Nmb6WA8Cev8TGuqUDgOfs4t/R/wTkw82K6pLOBYjXqZnZwrkG+IDMucqplQewy4njp6j3B5C3mdTG0uwK0uKu+83j7g0cGB1pZzRhX3ZpZGVvX3FvZV9zdGFsbF9wcm9maWxlcxgcaWc0YV9zdGFsbF9wcm9maWxlX3R1bmluZ192MhgIdGVzdF8xXzYAEhgmZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlMTIzNF9pYnJfYXVkaW8iLBkYBWxpZ2h0ABZGFAASFAIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"926794690062240v\" bandwidth=\"347369\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q20\" FBContentLength=\"2607838\" FBPlaybackResolutionMos=\"0:100,360:71.1,480:69.2,720:68.3,1080:68,1440:69.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.1,480:92.1,720:89.9,1080:85.1,1440:81.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNX0WhGmAzCdZo6iXFxtohCQDAo6IkYWLLT-QexjwjCbNEO2J16rjugGx2qdpnVGYHrJyuW1juWbUYIZE-KKFzvjvEBxsTS9niZlpg.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=xY_c8h1oTdoQ7kNvwFlafD0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjM0NzM2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3OS09doN2i2ONmiRhA0GmcmS6g4RKL33oyYcS-oLJu-Q&amp;oe=69DC4190</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-16849\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-97894\" FBFirstSegmentRange=\"992-160729\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"160730-335227\" FBPrefetchSegmentRange=\"992-160729\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1579222173331698v\" bandwidth=\"473605\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q30\" FBContentLength=\"3555543\" FBPlaybackResolutionMos=\"0:100,360:75.6,480:73.7,720:72.5,1080:71.3,1440:72.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:95,720:93.5,1080:88.8,1440:85.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOn17sJvqdiMhkoGoFmRR5GvuvNKCHSPfM25qx56-aT4OI4BuqqNzI8j7dH7jh2N2_dbfIUJaoxqkpbbodQJRvwsNOMax8gwV-YhWA.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=7pNo1CqmBMEQ7kNvwEWuXap&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjQ3MzYwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af23V8hGU9BwggzZFYwKxj46jrc_i0fdNG6CSQ9G5WlGPQ&amp;oe=69DC230B</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-19527\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-133927\" FBFirstSegmentRange=\"992-218133\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"218134-452895\" FBPrefetchSegmentRange=\"992-218133\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"3902778526521513v\" bandwidth=\"625656\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q40\" FBContentLength=\"4697049\" FBPlaybackResolutionMos=\"0:100,360:79.3,480:77.1,720:75.6,1080:73.9,1440:74.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.8,720:96,1080:91.6,1440:88.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOOU8oXTyCVpU-lmAAc3_fl6kDSbhxCpH4efAxDxNoneEnKetCjQjLZ9KHtN3CUSDuJPZtsvli_XDHmo8b1ASvErktcaYsoq1DK9KE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=A-cC6Mz09_0Q7kNvwFJst_T&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjYyNTY1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2v04TjMMwsHsagEXEVCopxNcstDeGR4UTJiQ5DohanvQ&amp;oe=69DC5066</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-22504\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-177689\" FBFirstSegmentRange=\"992-286646\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"286647-593012\" FBPrefetchSegmentRange=\"992-286646\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"3053662511508936v\" bandwidth=\"787710\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q50\" FBContentLength=\"5913657\" FBPlaybackResolutionMos=\"0:100,360:82.5,480:80,720:77.8,1080:75.8,1440:76\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.4,480:97.9,720:97.7,1080:93.8,1440:90.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQN79BZn0MCXHe4haCJV-DuRXKj6NUoZ7pm6VPQmqmy_GFCaYVAYmItyNqQYpOuq9jfXPxjVgV8waXDdPAyxlBNzpNlPmbFohIPFsEI.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=fsdF06ZdvtUQ7kNvwGZ0IdD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjc4NzcxMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3akdk-OWvJU5-7zxjGZEiKUsty47XhGV8M9cFqttxbNQ&amp;oe=69DC2FC1</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-25197\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-226185\" FBFirstSegmentRange=\"992-362247\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"362248-746579\" FBPrefetchSegmentRange=\"992-362247\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1406580284037568v\" bandwidth=\"1057308\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q60\" FBContentLength=\"7937634\" FBPlaybackResolutionMos=\"0:100,360:85.7,480:83.5,720:81.2,1080:77.8,1440:77.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.99,480:98.81,720:98.9,1080:96.4,1440:93.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPq9PBIrgCuw9czWULqIBNha5wIpimHyrnCPVuWOOYRLDS8EKKjne3_MAfCbpBUOfGsYNFTaoHLSsXNkDEAQBJLmxIulSE1TMAGnIg.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=UjuToJF2I9EQ7kNvwE9zcHM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjEwNTczMDgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2tof7bqBzTzAojcIaMisntp2cbSX_nEXA2Q0Si-klbWQ&amp;oe=69DC24F7</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-31163\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-312092\" FBFirstSegmentRange=\"992-493774\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"493775-1013854\" FBPrefetchSegmentRange=\"992-493774\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"893871963490700v\" bandwidth=\"1533975\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q70\" FBContentLength=\"11516167\" FBPlaybackResolutionMos=\"0:100,360:88.7,480:86.7,720:84.6,1080:80.9,1440:80.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.448,480:99.335,720:99.445,1080:98.49,1440:97\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMPETj8IpBiBkhacc3ka9xGGJY_Vhp_M65AbG8Lk30ZXwyPpsIJM1_dVRTCPZv8czkiBDcl9SgWUVn1gJ2r-FfblyChLlitxKrm-tM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=215mmyF_ZIIQ7kNvwGxe_FQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjE1MzM5NzUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0qN7_I0cplToNq2HdJwRdtJ02mvftVy5OO7a2b75NdPA&amp;oe=69DC42DF</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-39114\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-464852\" FBFirstSegmentRange=\"992-726697\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"726698-1500620\" FBPrefetchSegmentRange=\"992-726697\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"2017218692481084v\" bandwidth=\"2125286\" codecs=\"av01.0.08M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q80\" FBContentLength=\"15955370\" FBPlaybackResolutionMos=\"0:100,360:91.1,480:89.3,720:87.2,1080:85.7,1440:85\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.582,480:99.57,720:99.638,1080:99.543,1440:99.51\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPEq_fDYGM2ttktK9udbibTCz-aRwlCIgvxHxpDEhZ884BMwI1n2xS39QmwK4IEFNtqeQTjfVamkDY2mGr_g5VbMRAqF4G7H1jid8w.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=U6M1ngXlgTYQ7kNvwHxE--G&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjIxMjUyODYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0kVBvfIp6VD6XIlXc7Bu70uMqZMIBs_EwWZ87efaMPxg&amp;oe=69DC2267</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-54263\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-660245\" FBFirstSegmentRange=\"992-1035883\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"1035884-2133073\" FBPrefetchSegmentRange=\"992-1035883\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"791432930126823a\" bandwidth=\"47670\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"47670\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"358991\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQN3B75EZEr34ogr7GF1-T8vsbRKZ0Hzt6I6En8nSV9eT5yH8hS7FboShpOBcVDzR296sMqT1lRDQP7tvvVfVk_vfTYGsEUEbJ9ofr4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=ay4usgmqp8AQ7kNvwELqXS7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDc4MDUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3v0Kqcwhi8aTV72H7gSzeNPH0zqoVBikGDjBJwM1ZWWg&amp;oe=69DC47B5</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-1967\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-15154\" FBFirstSegmentRange=\"1025-29469\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"29470-59290\" FBPrefetchSegmentRange=\"1025-29469\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2232701137531608a\" bandwidth=\"78366\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"78366\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"589501\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQO_Kfz1SxVxfEtHysoYJq5EongdyvUBq28ntHTV81-Un7YiMtp5CGbiplQDZWPM7nySIjiDaI9682e_NoHPy7_xcMYwRpUfO3LIB2o.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=ytygejStfkIQ7kNvwGDA9cd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6Nzg1MDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0qb9H0nQRiDa2R7DSOh_-VyQ7htz6mRRPzP2iKuTx1Ug&amp;oe=69DC1EA7</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2440\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-24395\" FBFirstSegmentRange=\"1026-48164\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48165-95228\" FBPrefetchSegmentRange=\"1026-48164\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"798056319992139a\" bandwidth=\"130531\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"130531\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"981215\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMgwgSgO9Smp8fdwbQvnvHmK_0Xf5Jgb72LxKi21knzAy6E1NLnuOLJwxaVciThtRnzxMh6ORF8Z1IBJOLR96LzoKp0gxsKe_nG4q0.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=LKSgGeO3P60Q7kNvwG6c4kz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTMwNjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1lir5GdHcyd-bxJeGuoAuZuVGs1riuCBvOeyMLg-TpNw&amp;oe=69DC293D</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2334\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-37007\" FBFirstSegmentRange=\"1021-75805\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"75806-158864\" FBPrefetchSegmentRange=\"1021-75805\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1815340029130180a\" bandwidth=\"160079\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"160079\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1203103\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQM9jm9NeAu3kk1yLA4gL6O-f_KeHsx_JlKCAde_LcpIlfHLA-CDepjFEe_rO2ZLJ3VHegu6kP5A_uQF4PN8szOxKe0RvAJQKK5d5C4.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=I5_xZd0KA_oQ7kNvwG8C-Ar&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTYwMjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3eStdOvL6gncbH8pFlLun1ShCAZgNNlau_RlJuMAUVkw&amp;oe=69DC1F1A</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2350\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-46420\" FBFirstSegmentRange=\"1021-94312\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"94313-194524\" FBPrefetchSegmentRange=\"1021-94312\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gHL1lTdiNjY4kTrhoDkC8-PJSK_2evPUSd62XjjV7A_3js9WGl3IjZWqxx6HMyo6Ww&_nc_ohc=TYSekVkP8Y0Q7kNvwFAm-sZ&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af3_gwzT9QN6pWlNpU1dSgl-QV8adpBvPbGGaTSINyRDpQ&oe=69DC2B58&_nc_sid=b41fef",
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
        "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHL1lTdiNjY4kTrhoDkC8-PJSK_2evPUSd62XjjV7A_3js9WGl3IjZWqxx6HMyo6Ww&_nc_ohc=ic5ODsLE2O8Q7kNvwFxafQC&_nc_gid=Q4NjZOdMW6QB9iUHHz2w6w&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2_AEOitGeJIQiUUXG0pIwJ9xRrNilnIIAR3oUzrREJpQ&oe=69DC204C&_nc_sid=b41fef",
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
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.02S\" FBManifestTimestamp=\"1775657695\" FBManifestIdentifier=\"Fr6Ls50NKRbkmJfH7/yMBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.02S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwE6FHLH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njc5NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af26mxww05cpjnldeMrh5jpsaT1_RiUxXspQ_GifFlHqTQ&amp;oe=69D83B87</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "progressive_download_url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQM3BWmWT9DCIR_4a6ETqY74iK_vSJ0mGCY5KURpD0ZI6aeamU2Fve1dXA5lCRBiztE1g_SEXMn_Iq_pDtwv8Zw.mp4?_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=3yv_Gp1gyOgQ7kNvwGHWWcl&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0Xzu-e0EJdaMyPqo48pyxqiQ87L8KTvV0B-Hi_Rw1XsQ&oe=69D8476D",
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
            "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGBK8z3L9lqy4DWvML--BpgVJy36lGCiwBUPBGQ6-Nh99kvvNoUUoGhXCiDz34DBIk&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af21UlzcJbkuel7b_lAq1YhzxqFGUgdRksXzbmWZaD1Wdg&oe=69DC19A9&_nc_sid=b41fef"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.101768S\" FBManifestTimestamp=\"1775657695\" FBManifestIdentifier=\"Fr6Ls50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtraJxpnwkvECjNnxgZuPjwT4stmliZm5BLzN2fTZweUFmpjfwsvS2Ab2jc22sdnYBuSVwq6x85UHzIqHl+PItgfq7MGKwvrFB9KWt/fT0JkMiu/Mv4iL6g8iGCJkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGVfaWJyX2F1ZGlvIiwZGAVsaWdodAAWDhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.101768S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"811763878117979v\" bandwidth=\"262728\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1973809\" FBPlaybackResolutionMos=\"0:100,360:62.9,480:58.1,720:53.3,1080:50.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.8,720:86.4,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP4s_c0uSAuy00HwODOQxGqL_KE1A5w9lnFiX0JfdCCMJTPukZiwIvC7uddABS-MUJBTNgcjIqVwxgJQEL9EM2gpulN4btvCIHeIYE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=-PmLEytgxDcQ7kNvwFqiBwe&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjoyNjI3MjgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3aoEK2h5QHTc8l4NCbyEJj5d2Oy1TxcT_9Xu3S2gnW6g&amp;oe=69DC2C4E</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-6086\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-129562\" FBFirstSegmentRange=\"1014-166973\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"166974-328722\" FBPrefetchSegmentRange=\"1014-166973\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1159146579572294v\" bandwidth=\"377484\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2835938\" FBPlaybackResolutionMos=\"0:100,360:68.5,480:63.8,720:58.3,1080:55.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.8,480:92.9,720:90.7,1080:85.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMeaQpVDw5N0MxBLbLlLw4lSRHBoeCxqRWEdQxK9-uXl9boeDW4fLNwvdk093JFHDC5HeJYG-12qm4BaWfLYFo8emoy6rS4rnz8i4c.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=Lw0vzjNBHBgQ7kNvwFQ-3k1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjozNzc0ODQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Dn1kO9lUg9q8JdQ2xgKhUrj3wGyVx0cIzpFLGvXgPOg&amp;oe=69DC2EDB</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-7174\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-184877\" FBFirstSegmentRange=\"1014-237575\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"237576-461968\" FBPrefetchSegmentRange=\"1014-237575\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2124162255043381v\" bandwidth=\"485928\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3650647\" FBPlaybackResolutionMos=\"0:100,360:71.5,480:67,720:61.5,1080:57.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:94.7,720:92.9,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOz6ELjZ949BogdJm_QNe1EGQjv1zTfVS_ZRTHhaA80l6nyo0X-36y79QprnZ4mpheYpPgrlqKovz2Z7nwAtkupZFh-qPPgSofw_SI.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=RIdyZ7swaFgQ7kNvwGNUvU7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjo0ODU5MjgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Su3ns55ayK89pYfvIvRB34aYzVBaH4x1ruGoPqs5pOA&amp;oe=69DC2D2D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8131\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-237174\" FBFirstSegmentRange=\"1014-303731\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"303732-578455\" FBPrefetchSegmentRange=\"1014-303731\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1251674976627900v\" bandwidth=\"619033\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"4650624\" FBPlaybackResolutionMos=\"0:100,360:74,480:69.7,720:64.2,1080:60.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95.9,720:94.7,1080:90.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNqHjWw34JU1zEWGF9C1h7VwlLIrqdJWbZ4OklUXgX1JUvMWrcXQ-RHcIlLZ5-leK-3oztau40NjRSFd8sWnMMpU8GdkzR1wupOZ10.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=pcYzS9tQp0IQ7kNvwEszMoJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjo2MTkwMzMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af20sz2onxzmM8vi2oOvyypDdF2Mrz3TDiN5_HHtqEgtjQ&amp;oe=69DC29CC</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8867\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-298106\" FBFirstSegmentRange=\"1014-381215\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"381216-715818\" FBPrefetchSegmentRange=\"1014-381215\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2090322355085990v\" bandwidth=\"859541\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"6457494\" FBPlaybackResolutionMos=\"0:100,360:76.8,480:72.8,720:67.2,1080:63\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.8,720:96.6,1080:93.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOiOZhsUH6TLkrnE9FwF7XkrsQrJbO4ranASPXWOp_kfZQnOZspqXMH9zwqL2A5ODtpWwSfSYjqVdnN5JwtnoKgDmzpRneeR6UjSf0.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=rP_jkdcldEoQ7kNvwHI63QF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjo4NTk1NDEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af29CalXPFITkH09MXHTyeDpubTG1nVI6wlAx6282IbsdQ&amp;oe=69DC197D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10444\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-407931\" FBFirstSegmentRange=\"1014-520416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"520417-950605\" FBPrefetchSegmentRange=\"1014-520416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1630604991607646v\" bandwidth=\"1133257\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"8513850\" FBPlaybackResolutionMos=\"0:100,360:79.2,480:74.9,720:69.3,1080:64.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.07,480:97.5,720:97.6,1080:94.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP6A5LFkcBJyvdNdliF_xHUaxD51PWWWorNb6dDtDzQ7XD8gAviBfoW1AVfcumwubAQFQ032SHQZ6jcxptLJTaTYNl8toVCs_2M5DY.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=MiND23-EIg0Q7kNvwHHB5kp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjoxMTMzMjU3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1mD28mB2lDY903llqTju-frjB6jQrG_po68HxKUeODtA&amp;oe=69DC478B</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-11592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-528888\" FBFirstSegmentRange=\"1014-673311\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"673312-1205023\" FBPrefetchSegmentRange=\"1014-673311\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4455411234741189v\" bandwidth=\"1595477\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"11986380\" FBPlaybackResolutionMos=\"0:100,360:81.7,480:76.7,720:71.1,1080:66.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.55,480:98.2,720:98.36,1080:96.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQO_EY8JAwoG2qGh3eNttzDv3bWaZbosyVqFsbHFSUR4ZIUqvEF3dIs_iUyiWHHffWx17NcAJslxKGK2F9yc3KKxTtB-3yov2ohU284.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=IcB0Uykb9IYQ7kNvwF_YL1v&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjoxNTk1NDc3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0msJJmYpzJwqBlfYCFFPb0yaoupHhhrFMcglDOuNQsFg&amp;oe=69DC368D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-13404\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-713619\" FBFirstSegmentRange=\"1014-916365\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"916366-1632404\" FBPrefetchSegmentRange=\"1014-916365\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1883899549033339v\" bandwidth=\"2141971\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"16092034\" FBPlaybackResolutionMos=\"0:100,360:84.6,480:79.8,720:74.1,1080:69.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.68,480:98.58,720:98.79,1080:98.46\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMAha-Ay45jS94TL8ynk5QQMBTTvF50BcTEUfE52AZhmIWcW5z7BSGD7RuWJzR1UJ1XHTtxnis--HnzX7LnQt9XFRHTMhfDthD67SM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=teHbZCY8fNsQ7kNvwEt5Cp5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwid2F0Y2hfdGltZV9zIjo2MTkzMjM5LCJiaXRyYXRlIjoyMTQxOTcxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0iH_HenMwvpgmIS7sU8T6gSV3r2cbS0uUYptddz94Zaw&amp;oe=69DC4BD5</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-962472\" FBFirstSegmentRange=\"1014-1247892\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1247893-2246471\" FBPrefetchSegmentRange=\"1014-1247892\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2018486635742578a\" bandwidth=\"46242\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46242\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"347952\" FBPaqMos=\"87.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN6d2WH86jHFShcbXf9sjQbZkQC0xUp0rW7EDnG4Bq4tXew6Pz2MHtHSrpUQKKBEGJCn216bnzZ43Z6y4oPrg8CshaIRDStXBf_2m8.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=p_6H5YxvVOsQ7kNvwHViz6E&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ3YXRjaF90aW1lX3MiOjYxOTMyMzksImJpdHJhdGUiOjQ2Mzc4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3OpXUnRPLMVAx0-LoeBthYAk9pFBUGYaGTQ8D9VvF0gw&amp;oe=69DC4148</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2090\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-13193\" FBFirstSegmentRange=\"1025-25675\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"25676-52073\" FBPrefetchSegmentRange=\"1025-25675\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"3434060956755369a\" bandwidth=\"76016\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"76016\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"571334\" FBPaqMos=\"88.88\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPiBT48Or08Wq2GueJ_a1ZGlP5QobL4jCYts8LWjbigiJaGQYlGIGdimLvTRUGI0Qy06ehqd8LGIkG1qUx2Q1PSVeSpBpibYNGQTcw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=jks4A86ZRgcQ7kNvwFTvgb7&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ3YXRjaF90aW1lX3MiOjYxOTMyMzksImJpdHJhdGUiOjc2MTUyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af27SD8LI_oM6GI2caGixBGZsGImx8lZcEEVpMLPseOO-g&amp;oe=69DC2C65</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2475\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21765\" FBFirstSegmentRange=\"1026-40537\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"40538-84371\" FBPrefetchSegmentRange=\"1026-40537\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1883782792341005a\" bandwidth=\"105481\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"105481\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"792391\" FBPaqMos=\"90.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNe18lXJWbOpFruCxw7tvHWDJwvLtPJ4A3aWliKSnQwQggwuFpt247QNTOPKpxOYARAZ0l711AUP70HG4efjUphK33t2U_SaotfKeo.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=4RJy2Aqlc90Q7kNvwFWLO7c&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ3YXRjaF90aW1lX3MiOjYxOTMyMzksImJpdHJhdGUiOjEwNTYxNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Nkhg5BXnXfOwfxJoSU4g9LkdWf7_JqjU1M-0VwNtEEw&amp;oe=69DC4B9E</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2371\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-29113\" FBFirstSegmentRange=\"1021-57428\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"57429-121150\" FBPrefetchSegmentRange=\"1021-57428\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "profile_pic_url": "https://scontent-atl3-3.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGBK8z3L9lqy4DWvML--BpgVJy36lGCiwBUPBGQ6-Nh99kvvNoUUoGhXCiDz34DBIk&_nc_ohc=zov5ST0QeW4Q7kNvwFDQilc&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af3qtCheJPtS1ft2f69LwKxHodWkmq9kDoa3W-2XtLiMhg&oe=69DC4D93&_nc_sid=b41fef",
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
          "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/656558113_18577653481026735_1735858011052165396_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGBK8z3L9lqy4DWvML--BpgVJy36lGCiwBUPBGQ6-Nh99kvvNoUUoGhXCiDz34DBIk&_nc_ohc=HX8JmLcZS9cQ7kNvwHGCczV&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCFIIievNH8ERwBCABTJRwGqARcYbmNDAQAB1501500j-ccb7-5&oh=00_Af1svRoyLk5nKXgxBrGJnhktxp2kzTJLmSxGMGVO_jS8bQ&oe=69DC2203&_nc_sid=b41fef",
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
      "thumbnail_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwGI6aTh&_nc_oc=Ado6tNAdarXUnmbkKJrfMxwyAyYa1N8cHf5Tmvjid9CI6-pFlsnveuXFOY8VRmljJvM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_ss=7a3ba&oh=00_Af3IuU6T9UDYJ8yQziuaGt-aCpJTNTiK831XLgY-ulkT6A&oe=69DC198A",
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
      "comment_count": 612,
      "comments_disabled": false,
      "like_count": 66049,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwG0Py-L&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0UWWsJjMnHOEA3iVDvf4TaJpDnUr1slNa_jmLH7cZbyA&oe=69D848EB",
      "view_count": 0,
      "video_duration": 60.07400131225586,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            48270,
            96540
          ],
          "height": 1333,
          "scans_profile": "e35",
          "url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwGI6aTh&_nc_oc=Ado6tNAdarXUnmbkKJrfMxwyAyYa1N8cHf5Tmvjid9CI6-pFlsnveuXFOY8VRmljJvM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_ss=7a3ba&oh=00_Af3IuU6T9UDYJ8yQziuaGt-aCpJTNTiK831XLgY-ulkT6A&oe=69DC198A",
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
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwG0Py-L&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0UWWsJjMnHOEA3iVDvf4TaJpDnUr1slNa_jmLH7cZbyA&oe=69D848EB",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1607971,
          "height": 1280,
          "id": "1791310395606912v",
          "type": 102,
          "url": "https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-atl3-3.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwG0Py-L&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0UWWsJjMnHOEA3iVDvf4TaJpDnUr1slNa_jmLH7cZbyA&oe=69D848EB",
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
          "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775657695\" FBManifestIdentifier=\"Fr6Ls50NKRb65a+KkPmzCSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwElpF4O&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af3JSBgiRrciFBjNkMGM6MKNEbSe1ajKOvQo_7_kKlAtoA&amp;oe=69D82A43</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "progressive_download_url": "https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOu1cJkIUYpfLz5hsq6b4bAI93Dsnj-0FVN5QJfDUtHrdxoyYljTBeDYR-FHSZ5LvVWtD_zp4sNL8fsO46SW16u.mp4?_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_ohc=zRv5taEP1NwQ7kNvwHddwAi&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af27YZYEyPyr0KAWOLQEFM4BidkBU-7DslNAYph16ApOLA&oe=69D8409F",
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
            "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGBK8z3L9lqy4DWvML--BpgVJy36lGCiwBUPBGQ6-Nh99kvvNoUUoGhXCiDz34DBIk&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af21UlzcJbkuel7b_lAq1YhzxqFGUgdRksXzbmWZaD1Wdg&oe=69DC19A9&_nc_sid=b41fef"
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
      "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775657695\" FBManifestIdentifier=\"Fr6Ls50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZtsrw04uR18sCzq/P6rrz5wKWhbb3/vTqApzdk6Xv+K0Dxuuo6Jq8ugT8qtjBxZO8BPCKjMvPhZIFpOKYvtG6+gX63pmOjZvKB7DLieOnqPcHmM/m7e6J4AgiGCJkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGVfaWJyX2F1ZGlvIiwZGAVsaWdodAAWRhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"2463075544126412v\" bandwidth=\"98700\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"740997\" FBPlaybackResolutionMos=\"0:100,360:50.2,480:49.8,720:51.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:81.5,480:77.8,720:73.9\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"180p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN6gnjrJFUMe_iGtOvfrqX-ViXeTzDW06a8ZdP0G5_Gx_dvGUuV3s7kx7JrfCFrda2CxFXZ6sTEMINz9N4GQyWc-9y8VorP1D_Ee0k.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=RHBElRovWxkQ7kNvwHiqQw0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjk4NzAwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af24470nwCe_8rrFTWV7fNqo6WTgyyQgC5w1qafyFmL__w&amp;oe=69DC25AE</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-7270\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-28690\" FBFirstSegmentRange=\"980-49398\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"49399-101383\" FBPrefetchSegmentRange=\"980-49398\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1254477646863075v\" bandwidth=\"176081\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1321931\" FBPlaybackResolutionMos=\"0:100,360:62.5,480:60.9,720:60.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.8,480:85.7,720:82.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN7n_YNp3qL55PMFiO6M15eGByiDtuBGAFjiKnAKuKmq4fXiV7IZmLSN8vMH1T2puOJNFv6gP4XVwkuRBT2Rd7WctV-aY8rbmndTS4.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=4ZkjxCW9XWcQ7kNvwE7vEnL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjE3NjA4MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3b8gc5H01rS8l9E2SwA1GwAz3tAk9JCafsnXFLin7quQ&amp;oe=69DC1E6F</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-9944\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-48419\" FBFirstSegmentRange=\"980-82940\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"82941-173125\" FBPrefetchSegmentRange=\"980-82940\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"729373640129573v\" bandwidth=\"258449\" codecs=\"av01.0.04M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"1940313\" FBPlaybackResolutionMos=\"0:100,360:69.7,480:67.7,720:66.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93,480:90.7,720:87.6\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQMhm1VlTw-q6tAq3_VO-Qo-fDUI9RXAvPLk2xGou9A_bfVEma7sr79YSfBbbLhK40Rf3afD_XhVyic_lfwkSfSvK1cAcS8wiZvQguA.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=YvrF_i_JpQYQ7kNvwHpfHnu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjI1ODQ0OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3eQ0v8vXZKKB2F7yEUBPaUAwufaa4Yofn4J8ID7Qgrmg&amp;oe=69DC4AA8</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-12377\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-69827\" FBFirstSegmentRange=\"980-119483\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"119484-251945\" FBPrefetchSegmentRange=\"980-119483\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1447053883441848v\" bandwidth=\"328968\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2469731\" FBPlaybackResolutionMos=\"0:100,360:73.2,480:71.3,720:70.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.7,480:93.8,720:94.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOe9JmOLc4VPurI_zKmN5jUq_fVlQkrD3tKqiS7IRBvjQ1UeCfKZ4BUTvjteK9aLUqFzlTXoTiGWl7VBJQzR2iyRFw4glqSoJUYiJo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=O5BWtjCgbTQQ7kNvwFU_VZk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjMyODk2OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0G95aUDcqb1dMpJ8PZrps8QHG5UMrTTnprQiCBEoGoDQ&amp;oe=69DC243D</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-15335\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-89831\" FBFirstSegmentRange=\"980-153560\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"153561-322157\" FBPrefetchSegmentRange=\"980-153560\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"945457498060622v\" bandwidth=\"440030\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3303531\" FBPlaybackResolutionMos=\"0:100,360:76.9,480:75,720:73.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.5,480:96.3,720:97\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNa7jLvsTsvGVFnYqKEuaLMpI0cPcOsESv0wTgc3jBiwRxUYyA-ZTCjk4d6K_d8mFWJE76422NZ8XtDLARcMK6Vu7MO-5UM1Jpuabc.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=0UcOq0L5pNIQ7kNvwGrapEi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjQ0MDAzMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0KX-7TnKs_qdZnErMpXZ15NdUlR_SND0o7Yzj4pPhClw&amp;oe=69DC486C</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-17666\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-119383\" FBFirstSegmentRange=\"980-202463\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"202464-425415\" FBPrefetchSegmentRange=\"980-202463\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"2133518174074813v\" bandwidth=\"580481\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4357970\" FBPlaybackResolutionMos=\"0:100,360:80.8,480:78.1,720:76.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.42,480:97.7,720:98.56\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-atl3-3.cdninstagram.com/o1/v/t2/f2/m367/AQO_yWtm76q-jxAze9o6xAXSXgCc_-JyJ2tJ4sF-hnCYl1moO89-0wfdtrgX-xEsKi12CQxrTikr3HcweR1HhPnRjK7L5d8fF75gqlQ.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-3.cdninstagram.com&amp;_nc_ohc=99PGv7ufZDUQ7kNvwHWYvnR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjU4MDQ4MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0iDXIePHFJX5I7fCMw4bIC8tQMdBgtHK6sCMMTzpadKA&amp;oe=69DC2419</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-20222\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-157716\" FBFirstSegmentRange=\"980-267379\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"267380-559841\" FBPrefetchSegmentRange=\"980-267379\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1676663089993874v\" bandwidth=\"826892\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6207903\" FBPlaybackResolutionMos=\"0:100,360:84.7,480:82.1,720:79.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.126,480:98.91,720:99.278\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMcjd-0rTUZKI9UPMmQinD-viIkaAxNBU8iwyMRuyN4tVm3yz9jlKpPlnfheI2UxC8Bc3mapLuQa5d6P9WeFX3fhh-oe4qCXjD2CUA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=UDiHLJgBy6UQ7kNvwFZ6hQF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjgyNjg5MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2VSqRwCn0enDqEnSHK893h94JJvd-UcZITYJimi9hJRg&amp;oe=69DC4199</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-24579\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-226730\" FBFirstSegmentRange=\"980-380753\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"380754-795640\" FBPrefetchSegmentRange=\"980-380753\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1258177049594558v\" bandwidth=\"1186844\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"8910246\" FBPlaybackResolutionMos=\"0:100,360:87.7,480:85.3,720:82.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.492,480:99.445,720:99.682\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNwKtuW_7agA5xTUpu6GXYYZFNNw6bTUUpb3S8tc_fMkyVMSJBlPCngUnIZQFstd4NMV-vi6Fot5Fyg69j0j5TEkYn8hBIYfDg5gGk.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=VGpyByHEQ48Q7kNvwEM3krD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjExODY4NDQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3lROt_NziJ-RTSawfgOdZ0fzqk8HtA-St1APO9kcgt0w&amp;oe=69DC26F2</BaseURL><SegmentBase indexRange=\"804-979\" timescale=\"11988\" FBMinimumPrefetchRange=\"980-31258\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"980-332570\" FBFirstSegmentRange=\"980-552600\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"552601-1149437\" FBPrefetchSegmentRange=\"980-552600\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-803\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"791432930126823a\" bandwidth=\"47670\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"47670\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"358991\" FBPaqMos=\"89.30\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQN3B75EZEr34ogr7GF1-T8vsbRKZ0Hzt6I6En8nSV9eT5yH8hS7FboShpOBcVDzR296sMqT1lRDQP7tvvVfVk_vfTYGsEUEbJ9ofr4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=ay4usgmqp8AQ7kNvwHbb8jg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDc4MDUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0cByuvG8E9RhTqm5RYCcXIe0Y5YSjqysZU83dJl78TUg&amp;oe=69DC47B5</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-1967\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-15154\" FBFirstSegmentRange=\"1025-29469\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"29470-59290\" FBPrefetchSegmentRange=\"1025-29469\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2232701137531608a\" bandwidth=\"78366\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"78366\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"589501\" FBPaqMos=\"90.30\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO_Kfz1SxVxfEtHysoYJq5EongdyvUBq28ntHTV81-Un7YiMtp5CGbiplQDZWPM7nySIjiDaI9682e_NoHPy7_xcMYwRpUfO3LIB2o.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-1.cdninstagram.com&amp;_nc_ohc=ytygejStfkIQ7kNvwFogzlo&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6Nzg1MDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Pvqob8TjKbfEAolCNa0Ki9ekDF59D8UQfF7LJ7-PH5g&amp;oe=69DC1EA7</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2440\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-24395\" FBFirstSegmentRange=\"1026-48164\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48165-95228\" FBPrefetchSegmentRange=\"1026-48164\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"798056319992139a\" bandwidth=\"130531\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"130531\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"981215\" FBPaqMos=\"92.51\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-atl3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMgwgSgO9Smp8fdwbQvnvHmK_0Xf5Jgb72LxKi21knzAy6E1NLnuOLJwxaVciThtRnzxMh6ORF8Z1IBJOLR96LzoKp0gxsKe_nG4q0.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-atl3-2.cdninstagram.com&amp;_nc_ohc=LKSgGeO3P60Q7kNvwG_qbny&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTMwNjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Wgy2pP27auEJbSPT7d8TD3bLzP0zqeZcE8ARn1xluYQ&amp;oe=69DC293D</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2334\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-37007\" FBFirstSegmentRange=\"1021-75805\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"75806-158864\" FBPrefetchSegmentRange=\"1021-75805\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
          "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gGBK8z3L9lqy4DWvML--BpgVJy36lGCiwBUPBGQ6-Nh99kvvNoUUoGhXCiDz34DBIk&_nc_ohc=TYSekVkP8Y0Q7kNvwEbAoNx&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af3gK-XTqskRz2QB4WjPeel7b7Wrwo2sHPCtZt0LwZHUXA&oe=69DC2B58&_nc_sid=b41fef",
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
          "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGBK8z3L9lqy4DWvML--BpgVJy36lGCiwBUPBGQ6-Nh99kvvNoUUoGhXCiDz34DBIk&_nc_ohc=ic5ODsLE2O8Q7kNvwE58ntK&_nc_gid=n8SRL0kHPWx6Suv1Gzwa9g&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af27qEJSkQgeflZxus_6nCWYxXk5-CtcjtDWPaN5n10mMw&oe=69DC204C&_nc_sid=b41fef",
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
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.02S\" FBManifestTimestamp=\"1775657698\" FBManifestIdentifier=\"FsSLs50NKRbkmJfH7/yMBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.02S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwHAdjJV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njc5NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1NzjoKFKf8PZF2e29px00kaO2sZeRfMMPveYpVCaJymg&amp;oe=69D83B87</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "progressive_download_url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM3BWmWT9DCIR_4a6ETqY74iK_vSJ0mGCY5KURpD0ZI6aeamU2Fve1dXA5lCRBiztE1g_SEXMn_Iq_pDtwv8Zw.mp4?_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=3yv_Gp1gyOgQ7kNvwFWn59Z&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2QMrIL1Kga89HTr0gh5r5wVAQpko-N9oJHTJaJgzAq-A&oe=69D8476D",
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
          "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHLerj-sL0LCtDjad8eAFqTo4hxLTnY7Mr86bhrtVsVr5uOmioN2de1CHC0PZpT-ao&_nc_ohc=XbeNvhLXv28Q7kNvwFjjZcH&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0gwvqUwb8v6dFl4bqCTT0PonGIU-Y5yudCqf5xizPuag&oe=69DC19A9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.101768S\" FBManifestTimestamp=\"1775657698\" FBManifestIdentifier=\"FsSLs50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxraJxpnwkvECjNnxgZuPjwT4stmliZm5BLzN2fTZweUFmpjfwsvS2Ab2jc22sdnYBuSVwq6x85UHzIqHl+PItgfq7MGKwvrFB9bylbjgtpcL0pa399PQmQyK78y/iIvqDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGA5tb2RlcmF0ZV9oZWF2eRkYB2FuZHJvaWQAFg4UABIUAgA=\"><Period id=\"0\" duration=\"PT60.101768S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.7\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"811763878117979v\" bandwidth=\"262728\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1973809\" FBPlaybackResolutionMos=\"0:100,360:62.9,480:58.1,720:53.3,1080:50.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.8,720:86.4,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP4s_c0uSAuy00HwODOQxGqL_KE1A5w9lnFiX0JfdCCMJTPukZiwIvC7uddABS-MUJBTNgcjIqVwxgJQEL9EM2gpulN4btvCIHeIYE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=-PmLEytgxDcQ7kNvwFCK2dd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjYyNzI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3dGfcxhMTNUk3hOcryIwFRsk_hqGm50urGBDxr38S3vA&amp;oe=69DC2C4E</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-6086\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-129562\" FBFirstSegmentRange=\"1014-166973\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"166974-328722\" FBPrefetchSegmentRange=\"1014-166973\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1159146579572294v\" bandwidth=\"377484\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2835938\" FBPlaybackResolutionMos=\"0:100,360:68.5,480:63.8,720:58.3,1080:55.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.8,480:92.9,720:90.7,1080:85.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMeaQpVDw5N0MxBLbLlLw4lSRHBoeCxqRWEdQxK9-uXl9boeDW4fLNwvdk093JFHDC5HeJYG-12qm4BaWfLYFo8emoy6rS4rnz8i4c.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=Lw0vzjNBHBgQ7kNvwGnT6Uj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6Mzc3NDg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af01sYuinDn8XX51MaYrZU4IIDZqUgVtRAGB_MBOG5hxzA&amp;oe=69DC2EDB</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-7174\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-184877\" FBFirstSegmentRange=\"1014-237575\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"237576-461968\" FBPrefetchSegmentRange=\"1014-237575\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2124162255043381v\" bandwidth=\"485928\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3650647\" FBPlaybackResolutionMos=\"0:100,360:71.5,480:67,720:61.5,1080:57.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:94.7,720:92.9,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOz6ELjZ949BogdJm_QNe1EGQjv1zTfVS_ZRTHhaA80l6nyo0X-36y79QprnZ4mpheYpPgrlqKovz2Z7nwAtkupZFh-qPPgSofw_SI.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=RIdyZ7swaFgQ7kNvwEdoDHR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDg1OTI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3tpLdb4I_4aiBxXQaEpjLE578awiZD6NDTr5Y5aaFQOQ&amp;oe=69DC2D2D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8131\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-237174\" FBFirstSegmentRange=\"1014-303731\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"303732-578455\" FBPrefetchSegmentRange=\"1014-303731\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1251674976627900v\" bandwidth=\"619033\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"4650624\" FBPlaybackResolutionMos=\"0:100,360:74,480:69.7,720:64.2,1080:60.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95.9,720:94.7,1080:90.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNqHjWw34JU1zEWGF9C1h7VwlLIrqdJWbZ4OklUXgX1JUvMWrcXQ-RHcIlLZ5-leK-3oztau40NjRSFd8sWnMMpU8GdkzR1wupOZ10.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=pcYzS9tQp0IQ7kNvwF7OGEJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjE5MDMzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3iA1D_kmknZsZxyD1_3NRe9rxhCJP9F0fKxOYt-qQXLQ&amp;oe=69DC29CC</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8867\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-298106\" FBFirstSegmentRange=\"1014-381215\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"381216-715818\" FBPrefetchSegmentRange=\"1014-381215\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2090322355085990v\" bandwidth=\"859541\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"6457494\" FBPlaybackResolutionMos=\"0:100,360:76.8,480:72.8,720:67.2,1080:63\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.8,720:96.6,1080:93.2\" FBAbrPolicyTags=\"avoid_on_cellular\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOiOZhsUH6TLkrnE9FwF7XkrsQrJbO4ranASPXWOp_kfZQnOZspqXMH9zwqL2A5ODtpWwSfSYjqVdnN5JwtnoKgDmzpRneeR6UjSf0.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=rP_jkdcldEoQ7kNvwHtluSQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6ODU5NTQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3j74kEp0E4TLTEaDJ-Ltcyar7dezslJOO4zNSNjKne1A&amp;oe=69DC197D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10444\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-407931\" FBFirstSegmentRange=\"1014-520416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"520417-950605\" FBPrefetchSegmentRange=\"1014-520416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1630604991607646v\" bandwidth=\"1133257\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"8513850\" FBPlaybackResolutionMos=\"0:100,360:79.2,480:74.9,720:69.3,1080:64.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.07,480:97.5,720:97.6,1080:94.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6A5LFkcBJyvdNdliF_xHUaxD51PWWWorNb6dDtDzQ7XD8gAviBfoW1AVfcumwubAQFQ032SHQZ6jcxptLJTaTYNl8toVCs_2M5DY.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=MiND23-EIg0Q7kNvwHugNts&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTEzMzI1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0-q2Wp89tqHEY5xcVjZX11PYzp7C5ee8jCNH2V6Gs0zA&amp;oe=69DC478B</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-11592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-528888\" FBFirstSegmentRange=\"1014-673311\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"673312-1205023\" FBPrefetchSegmentRange=\"1014-673311\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4455411234741189v\" bandwidth=\"1595477\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"11986380\" FBPlaybackResolutionMos=\"0:100,360:81.7,480:76.7,720:71.1,1080:66.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.55,480:98.2,720:98.36,1080:96.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO_EY8JAwoG2qGh3eNttzDv3bWaZbosyVqFsbHFSUR4ZIUqvEF3dIs_iUyiWHHffWx17NcAJslxKGK2F9yc3KKxTtB-3yov2ohU284.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=IcB0Uykb9IYQ7kNvwF4k1iE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTU5NTQ3NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1MlAsNhwLDJ7EaL19CQbTNlpL9X9a41iAm1ZmyynbKaA&amp;oe=69DC368D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-13404\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-713619\" FBFirstSegmentRange=\"1014-916365\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"916366-1632404\" FBPrefetchSegmentRange=\"1014-916365\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1883899549033339v\" bandwidth=\"2141971\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"16092034\" FBPlaybackResolutionMos=\"0:100,360:84.6,480:79.8,720:74.1,1080:69.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.68,480:98.58,720:98.79,1080:98.46\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMAha-Ay45jS94TL8ynk5QQMBTTvF50BcTEUfE52AZhmIWcW5z7BSGD7RuWJzR1UJ1XHTtxnis--HnzX7LnQt9XFRHTMhfDthD67SM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=teHbZCY8fNsQ7kNvwGrl3WI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjE0MTk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1pqKV1qY9JHx7SlzqszthWj7v75urOy9hIOVwnQ1MI3A&amp;oe=69DC4BD5</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-962472\" FBFirstSegmentRange=\"1014-1247892\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1247893-2246471\" FBPrefetchSegmentRange=\"1014-1247892\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2018486635742578a\" bandwidth=\"46242\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46242\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"347952\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN6d2WH86jHFShcbXf9sjQbZkQC0xUp0rW7EDnG4Bq4tXew6Pz2MHtHSrpUQKKBEGJCn216bnzZ43Z6y4oPrg8CshaIRDStXBf_2m8.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=p_6H5YxvVOsQ7kNvwFWGwGn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjM3OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1amGOKgPC7HAda30nwTSGzkCNr_eO--obUzKkEforUMg&amp;oe=69DC4148</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2090\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-13193\" FBFirstSegmentRange=\"1025-25675\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"25676-52073\" FBPrefetchSegmentRange=\"1025-25675\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"3434060956755369a\" bandwidth=\"76016\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"76016\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"571334\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPiBT48Or08Wq2GueJ_a1ZGlP5QobL4jCYts8LWjbigiJaGQYlGIGdimLvTRUGI0Qy06ehqd8LGIkG1qUx2Q1PSVeSpBpibYNGQTcw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=jks4A86ZRgcQ7kNvwFzbSTC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NjE1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2BVLLT8cKk4QeeeBTBhv6G_MqXqpKQvT6YU3izZrw9ZQ&amp;oe=69DC2C65</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2475\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21765\" FBFirstSegmentRange=\"1026-40537\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"40538-84371\" FBPrefetchSegmentRange=\"1026-40537\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1883782792341005a\" bandwidth=\"105481\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"105481\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"792391\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNe18lXJWbOpFruCxw7tvHWDJwvLtPJ4A3aWliKSnQwQggwuFpt247QNTOPKpxOYARAZ0l711AUP70HG4efjUphK33t2U_SaotfKeo.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=4RJy2Aqlc90Q7kNvwFCw_Nu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDU2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3seDYM8vzB0QuwQakSB79R-zHb6TWb1ay-WcRu_9j__g&amp;oe=69DC4B9E</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2371\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-29113\" FBFirstSegmentRange=\"1021-57428\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"57429-121150\" FBPrefetchSegmentRange=\"1021-57428\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"3147742935432363a\" bandwidth=\"137156\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137156\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1030031\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQP_rTgUjxqk_-kh-SP-bwQXBAWsh2FhnEOAntOUAYLiE6AGbZrgLCCQ311RK6AMTE9vBeDWK_JptQx8gsbsogY_ivE-bvNPRZah-eI.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=0oFa_fCas-kQ7kNvwFCmDmt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMzcyOTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1V_5Kk9awpIg6rVIY4LWi1heXRiJZqyXa036AvKqhz0A&amp;oe=69DC45AD</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2418\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-35310\" FBFirstSegmentRange=\"1021-75028\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"75029-156364\" FBPrefetchSegmentRange=\"1021-75028\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHLerj-sL0LCtDjad8eAFqTo4hxLTnY7Mr86bhrtVsVr5uOmioN2de1CHC0PZpT-ao&_nc_ohc=zov5ST0QeW4Q7kNvwHorov_&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af3s4_ansyK_0LfcTiSye_VMK8nZ44hDjRyi3vHvY1xJWQ&oe=69DC4D93&_nc_sid=b41fef",
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
        "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/656558113_18577653481026735_1735858011052165396_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHLerj-sL0LCtDjad8eAFqTo4hxLTnY7Mr86bhrtVsVr5uOmioN2de1CHC0PZpT-ao&_nc_ohc=HX8JmLcZS9cQ7kNvwFrZZbY&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCFIIievNH8ERwBCABTJRwGqARcYbmNDAQAB1501500j-ccb7-5&oh=00_Af25fKQB46t_9aaEEKO5T0DzUn_tKvg_FxJzhwqIW9jaDQ&oe=69DC2203&_nc_sid=b41fef",
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
    "thumbnail_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwF7jaKE&_nc_oc=AdqbH2e6kShgTGnU5sxZ9HpdUErTjX3QXpo6OXibEH_5_g4YVTdtC7qif9J9f58sbnM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_ss=7a3ba&oh=00_Af0B7hjLCjCtkb7xWaXfz8uSw0RsKdAWGBUepQL6_06k1g&oe=69DC198A",
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
    "comment_count": 612,
    "comments_disabled": false,
    "like_count": 66049,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwEGhXcT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3JPSuKPRZ1pu0qhBHCxISl7CAFK8d3Y4XxTCoS4XG1Ig&oe=69D848EB",
    "view_count": 0,
    "video_duration": 60.07400131225586,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          48270,
          96540
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwF7jaKE&_nc_oc=AdqbH2e6kShgTGnU5sxZ9HpdUErTjX3QXpo6OXibEH_5_g4YVTdtC7qif9J9f58sbnM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_ss=7a3ba&oh=00_Af0B7hjLCjCtkb7xWaXfz8uSw0RsKdAWGBUepQL6_06k1g&oe=69DC198A",
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
        "url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwEGhXcT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3JPSuKPRZ1pu0qhBHCxISl7CAFK8d3Y4XxTCoS4XG1Ig&oe=69D848EB",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1607971,
        "height": 1280,
        "id": "1791310395606912v",
        "type": 102,
        "url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwEGhXcT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3JPSuKPRZ1pu0qhBHCxISl7CAFK8d3Y4XxTCoS4XG1Ig&oe=69D848EB",
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
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775657698\" FBManifestIdentifier=\"FsSLs50NKRb65a+KkPmzCSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwHuwMAJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2_-uA4ZKzUgnkU-RYNlzSTvAPmbBeis23rR-924vzLpg&amp;oe=69D82A43</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "progressive_download_url": "https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOu1cJkIUYpfLz5hsq6b4bAI93Dsnj-0FVN5QJfDUtHrdxoyYljTBeDYR-FHSZ5LvVWtD_zp4sNL8fsO46SW16u.mp4?_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_ohc=zRv5taEP1NwQ7kNvwELNLBR&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1Qj20Qr5_-XhKalfUI-uwQvgDuyVNc6K9eZ7_gK8IgFg&oe=69D8409F",
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
          "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHLerj-sL0LCtDjad8eAFqTo4hxLTnY7Mr86bhrtVsVr5uOmioN2de1CHC0PZpT-ao&_nc_ohc=XbeNvhLXv28Q7kNvwFjjZcH&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0gwvqUwb8v6dFl4bqCTT0PonGIU-Y5yudCqf5xizPuag&oe=69DC19A9&_nc_sid=b41fef"
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
    "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775657698\" FBManifestIdentifier=\"FsSLs50NGBVyMmF2MS1yMWdlbjJ2cDktc3ItbTMZts6vz+q68+cCloW29/706gKYpt6Nmb6WA8Cev8TGuqUDgOfs4t/R/wTkw82K6pLOBYjXqZnZwrkG+IDMucqplQewy4njp6j3B5C3mdTG0uwK0uKu+83j7g0iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyIsGRgObW9kZXJhdGVfaGVhdnkZGAdhbmRyb2lkABZGFAASFAIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.7\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"926794690062240v\" bandwidth=\"347369\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q20\" FBContentLength=\"2607838\" FBPlaybackResolutionMos=\"0:100,360:71.1,480:69.2,720:68.3,1080:68,1440:69.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.1,480:92.1,720:89.9,1080:85.1,1440:81.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNX0WhGmAzCdZo6iXFxtohCQDAo6IkYWLLT-QexjwjCbNEO2J16rjugGx2qdpnVGYHrJyuW1juWbUYIZE-KKFzvjvEBxsTS9niZlpg.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=xY_c8h1oTdoQ7kNvwH2SB5X&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjM0NzM2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3mjIAnXHHDtIxNjB9i3t87c569vGreDX5Q9uUkJdaVsg&amp;oe=69DC4190</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-16849\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-97894\" FBFirstSegmentRange=\"992-160729\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"160730-335227\" FBPrefetchSegmentRange=\"992-160729\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1579222173331698v\" bandwidth=\"473605\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q30\" FBContentLength=\"3555543\" FBPlaybackResolutionMos=\"0:100,360:75.6,480:73.7,720:72.5,1080:71.3,1440:72.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:95,720:93.5,1080:88.8,1440:85.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOn17sJvqdiMhkoGoFmRR5GvuvNKCHSPfM25qx56-aT4OI4BuqqNzI8j7dH7jh2N2_dbfIUJaoxqkpbbodQJRvwsNOMax8gwV-YhWA.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=7pNo1CqmBMEQ7kNvwF-HRD4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjQ3MzYwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af05cxRqORrJvScOkKqf54XoXRs8oqhHCFii9Bl5QDIBbQ&amp;oe=69DC230B</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-19527\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-133927\" FBFirstSegmentRange=\"992-218133\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"218134-452895\" FBPrefetchSegmentRange=\"992-218133\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"3902778526521513v\" bandwidth=\"625656\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q40\" FBContentLength=\"4697049\" FBPlaybackResolutionMos=\"0:100,360:79.3,480:77.1,720:75.6,1080:73.9,1440:74.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.8,720:96,1080:91.6,1440:88.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOOU8oXTyCVpU-lmAAc3_fl6kDSbhxCpH4efAxDxNoneEnKetCjQjLZ9KHtN3CUSDuJPZtsvli_XDHmo8b1ASvErktcaYsoq1DK9KE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=A-cC6Mz09_0Q7kNvwHh4qNW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjYyNTY1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1VfHanisFt2u_Db3Yb_gF5mdbULMc0L3__KqX6R73t1g&amp;oe=69DC5066</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-22504\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-177689\" FBFirstSegmentRange=\"992-286646\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"286647-593012\" FBPrefetchSegmentRange=\"992-286646\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"3053662511508936v\" bandwidth=\"787710\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q50\" FBContentLength=\"5913657\" FBPlaybackResolutionMos=\"0:100,360:82.5,480:80,720:77.8,1080:75.8,1440:76\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.4,480:97.9,720:97.7,1080:93.8,1440:90.9\" FBAbrPolicyTags=\"avoid_on_cellular\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN79BZn0MCXHe4haCJV-DuRXKj6NUoZ7pm6VPQmqmy_GFCaYVAYmItyNqQYpOuq9jfXPxjVgV8waXDdPAyxlBNzpNlPmbFohIPFsEI.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=fsdF06ZdvtUQ7kNvwGaY54K&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjc4NzcxMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1mhJKjmWTyB8wIGRVJWyzIumqqxIOh6szBtlwd6_Yb5w&amp;oe=69DC2FC1</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-25197\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-226185\" FBFirstSegmentRange=\"992-362247\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"362248-746579\" FBPrefetchSegmentRange=\"992-362247\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1406580284037568v\" bandwidth=\"1057308\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q60\" FBContentLength=\"7937634\" FBPlaybackResolutionMos=\"0:100,360:85.7,480:83.5,720:81.2,1080:77.8,1440:77.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.99,480:98.81,720:98.9,1080:96.4,1440:93.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPq9PBIrgCuw9czWULqIBNha5wIpimHyrnCPVuWOOYRLDS8EKKjne3_MAfCbpBUOfGsYNFTaoHLSsXNkDEAQBJLmxIulSE1TMAGnIg.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=UjuToJF2I9EQ7kNvwHax4_J&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjEwNTczMDgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0V5iRiW51he8-nNtTQ21uNSEzwZIPNzAWJ9PJ5-EVXjQ&amp;oe=69DC24F7</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-31163\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-312092\" FBFirstSegmentRange=\"992-493774\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"493775-1013854\" FBPrefetchSegmentRange=\"992-493774\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"893871963490700v\" bandwidth=\"1533975\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q70\" FBContentLength=\"11516167\" FBPlaybackResolutionMos=\"0:100,360:88.7,480:86.7,720:84.6,1080:80.9,1440:80.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.448,480:99.335,720:99.445,1080:98.49,1440:97\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMPETj8IpBiBkhacc3ka9xGGJY_Vhp_M65AbG8Lk30ZXwyPpsIJM1_dVRTCPZv8czkiBDcl9SgWUVn1gJ2r-FfblyChLlitxKrm-tM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=215mmyF_ZIIQ7kNvwHd1Fb1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjE1MzM5NzUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3v0d-43EaZR2I7HbL54QOGpiTBNvrjrQeA3EytTwAfpQ&amp;oe=69DC42DF</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-39114\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-464852\" FBFirstSegmentRange=\"992-726697\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"726698-1500620\" FBPrefetchSegmentRange=\"992-726697\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"2017218692481084v\" bandwidth=\"2125286\" codecs=\"av01.0.08M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q80\" FBContentLength=\"15955370\" FBPlaybackResolutionMos=\"0:100,360:91.1,480:89.3,720:87.2,1080:85.7,1440:85\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.582,480:99.57,720:99.638,1080:99.543,1440:99.51\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPEq_fDYGM2ttktK9udbibTCz-aRwlCIgvxHxpDEhZ884BMwI1n2xS39QmwK4IEFNtqeQTjfVamkDY2mGr_g5VbMRAqF4G7H1jid8w.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=U6M1ngXlgTYQ7kNvwFgCQn5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM1LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjIxMjUyODYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af07ZrGBaS0Z3lELJk_Q8lesQnVaF0DcDbYxRZNtO8h70g&amp;oe=69DC2267</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-54263\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-660245\" FBFirstSegmentRange=\"992-1035883\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"1035884-2133073\" FBPrefetchSegmentRange=\"992-1035883\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"791432930126823a\" bandwidth=\"47670\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"47670\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"358991\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN3B75EZEr34ogr7GF1-T8vsbRKZ0Hzt6I6En8nSV9eT5yH8hS7FboShpOBcVDzR296sMqT1lRDQP7tvvVfVk_vfTYGsEUEbJ9ofr4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=ay4usgmqp8AQ7kNvwHrIDbs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDc4MDUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0rsKYjMPk0pskrw2uP6Bss05AEYYQM1YLFoTCPr_9ByA&amp;oe=69DC47B5</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-1967\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-15154\" FBFirstSegmentRange=\"1025-29469\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"29470-59290\" FBPrefetchSegmentRange=\"1025-29469\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2232701137531608a\" bandwidth=\"78366\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"78366\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"589501\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO_Kfz1SxVxfEtHysoYJq5EongdyvUBq28ntHTV81-Un7YiMtp5CGbiplQDZWPM7nySIjiDaI9682e_NoHPy7_xcMYwRpUfO3LIB2o.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=ytygejStfkIQ7kNvwHT_In_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6Nzg1MDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2zu8Af-HKFfcT-eQsAUqHABVmKVsv3Fc99Bu3J30PY9g&amp;oe=69DC1EA7</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2440\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-24395\" FBFirstSegmentRange=\"1026-48164\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48165-95228\" FBPrefetchSegmentRange=\"1026-48164\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"798056319992139a\" bandwidth=\"130531\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"130531\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"981215\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMgwgSgO9Smp8fdwbQvnvHmK_0Xf5Jgb72LxKi21knzAy6E1NLnuOLJwxaVciThtRnzxMh6ORF8Z1IBJOLR96LzoKp0gxsKe_nG4q0.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=LKSgGeO3P60Q7kNvwFS-Ny9&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTMwNjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2wRa_Of4l95qFLiN-ZaMIZGN61FufMysd1pHu_MKI_dg&amp;oe=69DC293D</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2334\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-37007\" FBFirstSegmentRange=\"1021-75805\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"75806-158864\" FBPrefetchSegmentRange=\"1021-75805\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1815340029130180a\" bandwidth=\"160079\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"160079\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1203103\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-scl3-1.cdninstagram.com/o1/v/t2/f2/m367/AQM9jm9NeAu3kk1yLA4gL6O-f_KeHsx_JlKCAde_LcpIlfHLA-CDepjFEe_rO2ZLJ3VHegu6kP5A_uQF4PN8szOxKe0RvAJQKK5d5C4.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-scl3-1.cdninstagram.com&amp;_nc_ohc=I5_xZd0KA_oQ7kNvwE5i1od&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzUsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTYwMjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2IC9F_y_ptsZ09_aooruwEV1gzAktUlGa8nDxtd7XiZg&amp;oe=69DC1F1A</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2350\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-46420\" FBFirstSegmentRange=\"1021-94312\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"94313-194524\" FBPrefetchSegmentRange=\"1021-94312\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
        "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gHLerj-sL0LCtDjad8eAFqTo4hxLTnY7Mr86bhrtVsVr5uOmioN2de1CHC0PZpT-ao&_nc_ohc=TYSekVkP8Y0Q7kNvwEkgFbp&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af1UsXnvFcCqH-XsBhoAPtLUoCqtey3x64K8X6KjPJhPdA&oe=69DC2B58&_nc_sid=b41fef",
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
        "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHLerj-sL0LCtDjad8eAFqTo4hxLTnY7Mr86bhrtVsVr5uOmioN2de1CHC0PZpT-ao&_nc_ohc=ic5ODsLE2O8Q7kNvwG0YkeK&_nc_gid=EJJPqdqev9dY2Bon-fBJsQ&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af3p7tPyOEQuMXF-3f1CuwAG4XKYtgIat-EmCtHueN4HUw&oe=69DC204C&_nc_sid=b41fef",
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
        {
          "estimated_scans_sizes": [
            50179,
            100358
          ],
          "height": 1334,
          "scans_profile": "e35",
          "url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwEurejE&_nc_oc=AdpPgjNXYzBWJCcS4sOFRy4-6XfNZa5vGRAZaWR9S-gZOhcmF9weAwnTRZL9Ch7Da7g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&_nc_ss=7a3ba&oh=00_Af1y7C0CTEGxtZz7jq-RcF2SKKp2QVla_PR5PArBYK691Q&oe=69DC2D22",
          "width": 1080,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            33759,
            67518
          ],
          "height": 926,
          "scans_profile": "e35",
          "url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwEurejE&_nc_oc=AdpPgjNXYzBWJCcS4sOFRy4-6XfNZa5vGRAZaWR9S-gZOhcmF9weAwnTRZL9Ch7Da7g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&_nc_ss=7a3ba&oh=00_Af3UscYMFuALW9E_lcIWLd_P514XPdG7ci9EUC5_Bsh-4g&oe=69DC2D22",
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
      "thumbnail_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFfdVRU&_nc_oc=Adpz4RwKlocR9Su3dBxZ-9OHIXzrIatW7TYYrjAEXPoCqZMWv_Gagu6x5ovZ7TSndA8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&_nc_ss=7a3ba&oh=00_Af1o-TZUs78Bxx2E4xCKjiijTXDw_m3GsIb3J1q0-aPWtg&oe=69DC4804",
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
        "profile_pic_url": "https://scontent-waw2-1.cdninstagram.com/v/t51.2885-19/460602681_1286701775682716_7443510089900581929_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NTguYzIifQ&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFRn8MxvRnbdO41DfdbIW9co0OX3Sj9pLsqeVmVuOiPaDtW39qObUSTibEGMqwBS88&_nc_ohc=Enb1_W-dnWUQ7kNvwHj1j8N&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GDk9dBucfEWaP5IEAClkj0b9qExnbkULAAAB1501500j-ccb7-5&oh=00_Af3fDVc1Hw73q8vEwfLdy3LMLe_OlL-5tpBqpw0lXfC5Eg&oe=69DC36EC&_nc_sid=a8b8e2",
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
            "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFRn8MxvRnbdO41DfdbIW9co0OX3Sj9pLsqeVmVuOiPaDtW39qObUSTibEGMqwBS88&_nc_ohc=ic5ODsLE2O8Q7kNvwEw466q&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af06O9ekSLDmsr3mP4FvRYCkLL4bxYiGWvxd67nCYtKZyA&oe=69DC204C&_nc_sid=a8b8e2",
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
            "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/525764789_18523595374024831_4665287119118685063_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NjcuYzIifQ&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFRn8MxvRnbdO41DfdbIW9co0OX3Sj9pLsqeVmVuOiPaDtW39qObUSTibEGMqwBS88&_nc_ohc=tshhWSqzMN4Q7kNvwGgbV6B&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GLWIVh9-WDuiHM9BAIdTRsbqbb5AbmNDAQAB1501500j-ccb7-5&oh=00_Af3-bTazv79zJRcRheGSn2bb396jdUBvfojIzmPyxnFFBg&oe=69DC41A3&_nc_sid=a8b8e2",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
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
            32464
          ],
          "height": 720,
          "scans_profile": "e35",
          "url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFfdVRU&_nc_oc=Adpz4RwKlocR9Su3dBxZ-9OHIXzrIatW7TYYrjAEXPoCqZMWv_Gagu6x5ovZ7TSndA8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&_nc_ss=7a3ba&oh=00_Af1o-TZUs78Bxx2E4xCKjiijTXDw_m3GsIb3J1q0-aPWtg&oe=69DC4804",
          "width": 1080,
          "is_spatial_image": false
        },
        {
          "estimated_scans_sizes": [
            10923,
            21846
          ],
          "height": 500,
          "scans_profile": "e35",
          "url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFfdVRU&_nc_oc=Adpz4RwKlocR9Su3dBxZ-9OHIXzrIatW7TYYrjAEXPoCqZMWv_Gagu6x5ovZ7TSndA8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_gid=useMRF2pN1Xa5i1s2ih6qQ&_nc_ss=7a3ba&oh=00_Af3qw8XHpObQBLu9pOiS9XI4GPfqGIrhNozWb-xBJVxW2g&oe=69DC4804",
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
