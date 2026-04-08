# Location Endpoints

Get location info and media by location ID.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/location/by/id`](#get-v1locationbyid) | [`/v1/location/guides`](#get-v1locationguides) | [`/v1/location/medias/recent`](#get-v1locationmediasrecent) | [`/v1/location/medias/recent/chunk`](#get-v1locationmediasrecentchunk) | [`/v1/location/medias/top`](#get-v1locationmediastop) | [`/v1/location/medias/top/chunk`](#get-v1locationmediastopchunk) | [`/v1/location/search`](#get-v1locationsearch)

---

### GET /v1/location/by/id

Get location object by id. Returns a Location object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/by/id?id=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_by_id_v1(id="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/by/id",
        headers=headers,
        params={"id": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/by/id?id=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "pk": 213131048,
  "name": "Berlin, Germany",
  "phone": "",
  "website": "https://www.berlin.de/",
  "category": "Region",
  "hours": {
    "status": "",
    "current_status": "",
    "hours_today": "",
    "schedule": [],
    "is_open": false
  },
  "address": "",
  "city": "",
  "zip": "",
  "lng": null,
  "lat": null,
  "external_id": "111175118906315",
  "external_id_source": null
}
```

</details>

---

### GET /v1/location/guides

Get location guides. Returns location guide data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/guides?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_guides_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/guides",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/guides?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/location/medias/recent

Get location recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/recent?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_recent_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/recent",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/recent?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870820823258908956",
    "id": "3870820823258908956_76902937953",
    "code": "DW36we_iEkc",
    "taken_at": "2026-04-08T14:17:33Z",
    "taken_at_ts": 1775657853,
    "media_type": 2,
    "product_type": "clips",
    "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661578946_17876219574561954_7451617886524604299_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDgyMDgyMzI1ODkwODk1NjE3ODc2MjE5NTY4NTYxOTU0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIyNjh4NDAzMi5zZHIuQzMifQ%3D%3D&_nc_ohc=Ox1ygxfteusQ7kNvwGIM-8a&_nc_oc=AdqkvYnLvmOrX-nHpih8O8Tm6NY5anMBo9gQRpuEVeejvZ5xgR-u643QDd98z4ShxR8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&oh=00_Af3-H9LaOCkAPxIC1sMVwZXrZZfeI7ASQoZE6xZySGkHBw&oe=69DC2AFC",
    "location": {
      "pk": 213131048,
      "name": "Berlin, Germany",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "",
      "city": "",
      "zip": null,
      "lng": 13.401251,
      "lat": 52.518391,
      "external_id": "111175118906315",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "76902937953",
      "id": "76902937953",
      "username": "bocado.berlin",
      "full_name": "BOCADO Berlin",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658045171_17874004323561954_4837055008297918770_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44NTUuYzEifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gExvAHvk5K4uYlM41E8Ft1wqfb6wzPsR0_k1ZFnfvuVzxbdwGFKeAG7TStS9pMT9wU&_nc_ohc=nen4APJ7mY0Q7kNvwGN9Ce7&_nc_gid=h9sYNygiEtUZBvWbxira1A&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GPP4OCficWvuT4A-ADIhn-jmqyBDbmNDAQAB1501500j-ccb7-5&oh=00_Af2sxDC8k9_iMaQSA66UrK3oSR-iDzjyuk6CRAEy1XWspQ&oe=69DC4343&_nc_sid=99328a",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 0,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "#restaurant #bocado #tapas #cocktails #berlin",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFKH-zZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2J_dF5LXNe0s9PyNzgE8ikjBwXqy_bxDewoxzHmO2TNQ&oe=69D84485",
    "view_count": 0,
    "video_duration": 11.654000282287598,
    "title": "",
    "resources": [],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          18172,
          36344
        ],
        "height": 1333,
        "scans_profile": "e35",
        "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/661578946_17876219574561954_7451617886524604299_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg3MDgyMDgyMzI1ODkwODk1NjE3ODc2MjE5NTY4NTYxOTU0.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjIyNjh4NDAzMi5zZHIuQzMifQ%3D%3D&_nc_ohc=Ox1ygxfteusQ7kNvwGIM-8a&_nc_oc=AdqkvYnLvmOrX-nHpih8O8Tm6NY5anMBo9gQRpuEVeejvZ5xgR-u643QDd98z4ShxR8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&oh=00_Af3-H9LaOCkAPxIC1sMVwZXrZZfeI7ASQoZE6xZySGkHBw&oe=69DC2AFC",
        "width": 750,
        "is_spatial_image": false
      }
    ],
    "video_versions": [
      {
        "bandwidth": 1289954,
        "height": 1280,
        "id": "1712432703502038v",
        "type": 101,
        "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFKH-zZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2J_dF5LXNe0s9PyNzgE8ikjBwXqy_bxDewoxzHmO2TNQ&oe=69D84485",
        "url_expiration_timestamp_us": null,
        "width": 720,
        "fallback": null
      },
      {
        "bandwidth": 1289954,
        "height": 1280,
        "id": "1712432703502038v",
        "type": 102,
        "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQMF38d94-X0Q_OmLNo6V4eP04iWzHY7WZq-ExZ0zXnlXKXvKfWl1S7QAlCx96YAfOiDinZw9LyOhu8-s-Nda3j--2acYo8zjZLH2ik.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=RuvfyKeoOqoQ7kNvwFKH-zZ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc4NzYyMTk0NzI1NjE5NTQsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=933e720c30195def&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84NjQyREE2MjcyQjY1NDI2QkFGMTk1Q0EwMTQwMDBBOV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E1NEI5RUJCMTk0OUEwQjE1MkZEQ0JGMzZENTZDRUE0X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbEnLb59ZTBPxUCKAJDMywXQCdEGJN0vGoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=h9sYNygiEtUZBvWbxira1A&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2J_dF5LXNe0s9PyNzgE8ikjBwXqy_bxDewoxzHmO2TNQ&oe=69D84485",
        "url_expiration_timestamp_us": null,
  // ... truncated
```

</details>

---

### GET /v1/location/medias/recent/chunk

Get location chunk of recent medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/recent/chunk?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_recent_chunk_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/recent/chunk",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/recent/chunk?location_pk=213131048",
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
      "pk": "3870820134504117611",
      "id": "3870820134504117611_7556662934",
      "code": "DW36mdijDVr",
      "taken_at": "2026-04-08T14:17:50Z",
      "taken_at_ts": 1775657870,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661225089_1448822322898568_5834653775145915082_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=Mzg3MDgyMDEzNDUwNDExNzYxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=meZzUfZ4sgQQ7kNvwHCQbQG&_nc_oc=Adqx9Gu6VmDRJgF-f1sv6aZKRtPRi6h2dyVpVxXzfC-7Q-1d1wgUQ4YK8Vn5PQDZkUc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&oh=00_Af0UATAXI4d48ZtnFjKXmmAX8OOc2_gKmu6n62zPz95IjA&oe=69DC2177",
      "location": {
        "pk": 213131048,
        "name": "Berlin, Germany",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "",
        "zip": null,
        "lng": 13.401251,
        "lat": 52.518391,
        "external_id": "111175118906315",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "7556662934",
        "id": "7556662934",
        "username": "sofia_deol",
        "full_name": "Sofia de Oliveira🦋| NPC Bikini",
        "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/489045697_516419634670208_8361051641537387041_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDEyLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFnOOW94S78cIE8EXJgDwdDEFoscmb5-sBJLaMACCCSXigV-cN0GuL81ha--C8P0Jo&_nc_ohc=P8cs1coqh-4Q7kNvwFQCejt&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GME_Jh2AKuFQrtUBACFaiFIrbAh0bkULAAAB1501500j-ccb7-5&oh=00_Af3nH5fNRVdyoPUPLe4cfcHAGj-_lmISxA_5si75xNKI-A&oe=69DC287E&_nc_sid=99328a",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 0,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Be honest… is this “too much”? 👀\n.\n.\n.\n#gymgirl #stronggirl #selfconfidence #fitnessreel #gymmotivation",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPSLxUdVHCpDSUBUOPmG6gAzNxj1sPH2x1-Vurx7OilISocDthudy2lfqkS8gzYlsQsIJCySs-LIiv1tTtZuGPRwwMkgeGer1ArgQA.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=EQKsO4OWTkEQ7kNvwEmksB0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMjk0MTM5NDUyNTQ5MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=f09d518ab84d6f95&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNzQzODAwOEQzNDQ2MTM5OEY2M0JGQTg3RUE4RkE4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzVENDVBRjYwNDU1MjdFOEYzRDZBMjA5M0M5MEFFNUFCX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaukK_yp6CPQRUCKAJDMywXQBbul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2aAZ9KYdZqGtgzG6y2M4Kv__t_L9SEmA7eRygRvWugtA&oe=69D85BD1",
      "view_count": 0,
      "video_duration": 5.757999897003174,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            4950,
            9900
          ],
          "height": 1136,
          "scans_profile": "e15",
          "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661225089_1448822322898568_5834653775145915082_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=108&ig_cache_key=Mzg3MDgyMDEzNDUwNDExNzYxMQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=meZzUfZ4sgQQ7kNvwHCQbQG&_nc_oc=Adqx9Gu6VmDRJgF-f1sv6aZKRtPRi6h2dyVpVxXzfC-7Q-1d1wgUQ4YK8Vn5PQDZkUc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&oh=00_Af0UATAXI4d48ZtnFjKXmmAX8OOc2_gKmu6n62zPz95IjA&oe=69DC2177",
          "width": 640,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 1112289,
          "height": 1280,
          "id": "820219617212334v",
          "type": 101,
          "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPSLxUdVHCpDSUBUOPmG6gAzNxj1sPH2x1-Vurx7OilISocDthudy2lfqkS8gzYlsQsIJCySs-LIiv1tTtZuGPRwwMkgeGer1ArgQA.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=EQKsO4OWTkEQ7kNvwEmksB0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMjk0MTM5NDUyNTQ5MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=f09d518ab84d6f95&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNzQzODAwOEQzNDQ2MTM5OEY2M0JGQTg3RUE4RkE4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzVENDVBRjYwNDU1MjdFOEYzRDZBMjA5M0M5MEFFNUFCX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaukK_yp6CPQRUCKAJDMywXQBbul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2aAZ9KYdZqGtgzG6y2M4Kv__t_L9SEmA7eRygRvWugtA&oe=69D85BD1",
          "url_expiration_timestamp_us": null,
          "width": 720,
          "fallback": null
        },
        {
          "bandwidth": 1112289,
          "height": 1280,
          "id": "820219617212334v",
          "type": 102,
          "url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m86/AQPSLxUdVHCpDSUBUOPmG6gAzNxj1sPH2x1-Vurx7OilISocDthudy2lfqkS8gzYlsQsIJCySs-LIiv1tTtZuGPRwwMkgeGer1ArgQA.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=EQKsO4OWTkEQ7kNvwEmksB0&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTgzMjk0MTM5NDUyNTQ5MzUsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=f09d518ab84d6f95&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8wNzQzODAwOEQzNDQ2MTM5OEY2M0JGQTg3RUE4RkE4Ml92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzVENDVBRjYwNDU1MjdFOEYzRDZBMjA5M0M5MEFFNUFCX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaukK_yp6CPQRUCKAJDMywXQBbul41P3zsYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=MFiF5E2gde8WhyuCfQ7Uug&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2aAZ9KYdZqGtgzG6y2M4Kv__t_L9SEmA7eRygRvWugtA&oe=69D85BD1",
  // ... truncated
```

</details>

---

### GET /v1/location/medias/top

Get location top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/top?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_top_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/top",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/top?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "3870812423301488664",
    "id": "3870812423301488664_3028562913",
    "code": "DW342P7DeAY",
    "taken_at": "2026-04-08T14:00:20Z",
    "taken_at_ts": 1775656820,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": {
      "pk": 1029352986,
      "name": "Studio2 & Media Library for Dance and Theatre",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "Mariannenplatz 2",
      "city": "",
      "zip": null,
      "lng": 13.42446,
      "lat": 52.5038399,
      "external_id": "412463942289587",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "3028562913",
      "id": "3028562913",
      "username": "lebesheva_maria",
      "full_name": "Мария Лебешева",
      "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/v/t51.2885-19/424576707_1115460392965599_9214457040827163117_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-sin2-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEg40lDKj0H-MW_139g3qD_YXdTxIS4Rv8jX0E6HikXpoJhzt8VXXfcPBkWIGoC3AE&_nc_ohc=Z1v9c_XktXgQ7kNvwHv93Ba&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GMOGThnf1XtcgfYDAO2hmbzbU_B-bkULAAAB1501500j-ccb7-5&oh=00_Af0C3FwwC6f_zv2-KqjViLNpMpj60YLtO7D6YDbF7jNpGw&oe=69DC3C84&_nc_sid=99328a",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 1,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Танцевальная лаборатория Запределье, 2026",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870811310191911595",
        "id": "3870811310191911595_3028562913",
        "video_url": null,
        "thumbnail_url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0WkTAyXdtyOV07emBlwDwyBquXvLc69Sd74mO6rlhprw&oe=69DC5100",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              13647,
              27294
            ],
            "height": 1799,
            "scans_profile": "e35",
            "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af0WkTAyXdtyOV07emBlwDwyBquXvLc69Sd74mO6rlhprw&oe=69DC5100",
            "width": 1440,
            "is_spatial_image": false
          },
          {
            "estimated_scans_sizes": [
              6718,
              13437
            ],
            "height": 937,
            "scans_profile": "e35",
            "url": "https://scontent-sin2-1.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_p750x750_sh2.08_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwGx9vFZ&_nc_oc=Adr0PMAAPG-ngOdN-5eoXzBmWdFJlykJZ9r-FHcKKRK0sbjno1cpyV7y4ZqS_D9n5Ys&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin2-1.cdninstagram.com&_nc_gid=_6N0KdeJ6s107cZ9Brfn5w&_nc_ss=7a3ba&oh=00_Af2bUVXdz3m3dsP3aS6cgDYxvGBt6h8Ru67TcsPA5aVHcQ&oe=69DC5100",
            "width": 750,
            "is_spatial_image": false
          }
        ],
  // ... truncated
```

</details>

---

### GET /v1/location/medias/top/chunk

Get location chunk of top medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `location_pk` | integer | Yes | Location Pk |
| `max_id` | string | No | Max Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/medias/top/chunk?location_pk=213131048"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_top_chunk_v1(location_pk="213131048")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/top/chunk",
        headers=headers,
        params={"location_pk": "213131048"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/top/chunk?location_pk=213131048",
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
      "pk": "3870812423301488664",
      "id": "3870812423301488664_3028562913",
      "code": "DW342P7DeAY",
      "taken_at": "2026-04-08T14:00:20Z",
      "taken_at_ts": 1775656820,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": {
        "pk": 1029352986,
        "name": "Studio2 & Media Library for Dance and Theatre",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "Mariannenplatz 2",
        "city": "",
        "zip": null,
        "lng": 13.42446,
        "lat": 52.5038399,
        "external_id": "412463942289587",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "3028562913",
        "id": "3028562913",
        "username": "lebesheva_maria",
        "full_name": "Мария Лебешева",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/424576707_1115460392965599_9214457040827163117_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zMjAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gE_iIhELGkMHRrqCOxJ4HnWzllW-rhWuZF0plYZdPKIx0Dbs8Hh2K14ppP3tCxThK0&_nc_ohc=Z1v9c_XktXgQ7kNvwGVZCFS&_nc_gid=YN-agi0EhJb6182K1_sHFA&edm=AKmAybEBAAAA&ccb=7-5&ig_cache_key=GMOGThnf1XtcgfYDAO2hmbzbU_B-bkULAAAB1501500j-ccb7-5&oh=00_Af2UQEAkTwC6a0E91grDt62T2Go4zYp9Qc7B3G1Ty1nRpA&oe=69DC3C84&_nc_sid=99328a",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 1,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Танцевальная лаборатория Запределье, 2026",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870811310191911595",
          "id": "3870811310191911595_3028562913",
          "video_url": null,
          "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af1mTY-42vLB9XfJsUk2cimKZjb_NO7xeS6B669VGoO45g&oe=69DC5100",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                13647,
                27294
              ],
              "height": 1799,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af1mTY-42vLB9XfJsUk2cimKZjb_NO7xeS6B669VGoO45g&oe=69DC5100",
              "width": 1440,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                6718,
                13437
              ],
              "height": 937,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658869238_18463180051098914_5108602989405484146_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=100&ig_cache_key=Mzg3MDgxMTMxMDE5MTkxMTU5NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTc5OS5zZHIuQzMifQ%3D%3D&_nc_ohc=QpGY74SNvuwQ7kNvwEPz01p&_nc_oc=Adrn5dPL74tJ23XSP4W_hHOR8TK09oywpdG9adU88SNZ9hBHykKZZJNz8ERM3RgFQFc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=YN-agi0EhJb6182K1_sHFA&_nc_ss=7a3ba&oh=00_Af0UNUqSbqhIFVv8xJ0AK3rtWZYBaz2RP7Q-SHSn9i3c6A&oe=69DC5100",
              "width": 750,
              "is_spatial_image": false
            }
  // ... truncated
```

</details>

---

### GET /v1/location/search

Get locations using lat and long

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `lat` | number | Yes | Lat |
| `lng` | number | Yes | Lng |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/location/search?lat=40.7128&lng=-74.006"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_search_v1(lat=40.7128, lng=-74.006)
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v1/location/search",
        headers=headers,
        params={"lat": 40.7128, "lng": -74.006},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/search?lat=40.7128&lng=-74.006",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": null,
    "name": "Central Park",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "<0.1mi",
    "city": null,
    "zip": null,
    "lng": -74.0059728,
    "lat": 40.7127753,
    "external_id": "2233371183358453",
    "external_id_source": "facebook_places"
  },
  {
    "pk": null,
    "name": "München, Germany",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "<0.1mi",
    "city": null,
    "zip": null,
    "lng": -74.0059728,
    "lat": 40.7127753,
    "external_id": "436749889689403",
    "external_id_source": "facebook_places"
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-locations){ target=_blank }
