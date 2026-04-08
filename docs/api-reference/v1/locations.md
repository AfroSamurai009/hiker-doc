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

    response = requests.get(
        "https://api.hikerapi.com/v1/location/by/id",
        headers={"x-access-key": "YOUR_TOKEN"},
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

    response = requests.get(
        "https://api.hikerapi.com/v1/location/guides",
        headers={"x-access-key": "YOUR_TOKEN"},
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

    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/recent",
        headers={"x-access-key": "YOUR_TOKEN"},
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
    "pk": "3870915854612290399",
    "id": "3870915854612290399_615150761",
    "code": "DW4QXX1l9tf",
    "taken_at": "2026-04-08T17:25:51Z",
    "taken_at_ts": 1775669151,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-sea1-1.cdninstagram.com/...",
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
      "pk": "615150761",
      "id": "615150761",
      "username": "bom_dia_oficial",
      "full_name": "BOM DIA",
      "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 0,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "🗞️ Leia mais em bomdia.eu\n\n#comunidades #alemanha #berlim #embaixadadeportugal #apoiosocial #adidasocial #portugalpositivo #portuguesesnaalemanha",
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
          26834,
          53669,
          80504
        ],
        "height": 1350,
        "scans_profile": "e35",
        "url": "https://scontent-sea1-1.cdninstagram.com/...",
        "width": 1080,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870915779155762893",
    "id": "3870915779155762893_42402701875",
    "code": "DW4QWRkCJ7N",
    "taken_at": "2026-04-08T17:25:46Z",
    "taken_at_ts": 1775669146,
    "media_type": 1,
    "product_type": "feed",
    "thumbnail_url": "https://scontent-sea5-1.cdninstagram.com/...",
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
      "pk": "42402701875",
      "id": "42402701875",
      "username": "svitlanaliveberlin2026",
      "full_name": "Світлана життя в Німеччині | Документи та страхування",
      "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 0,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "1 травня | Берлін\nPREMIUM BOAT PARTY ✨\n\nУявіть:\nсонячний день, легкий вітер, яхта, музика, красиві люди та атмосфера справжнього відпочинку…\n\nМи запрошуємо вас на незабутню прогулянку преміальною яхтою\nодним із найкрасивіших маршрутів — від Kladow у напрямку Потсдама 🌊\n\n⸻\n\n🕛 Початок: 12:00\n⏳ Тривалість: 6 годин\n💶 Вартість: 75€\n\n⸻\n\nУ програмі:\n\n🎤 Жива музика (співачка + ведуча)\n🎷 Саксофоніст\n🎧 DJ\n📸 Фотограф і фотозона\n🥂 Welcome drink\n🍴 Легкі закуски від UBB Community\n\n➕ Додатково на борту:\n🔥 Барбекю\n🍸 Бар з напоями\n\n⸻\n\n✨ Dress Code: Elegant\nНам важливо зберегти атмосферу — красиву, легку та по-справжньому особливу\n\n⸻\n\nЦе не просто прогулянка\nЦе подія, яка залишиться у пам’яті\n\nДень, у якому поєднуються музика, місце та люди\n\n⸻\n\n📞 Продаж квитків за телефоном:\n+49 30 306 430 11\n+49 176 429 471 91\n\nКількість місць обмежена",
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
          34673,
          69347,
          104021
        ],
        "height": 1920,
        "scans_profile": "e35",
        "url": "https://scontent-sea5-1.cdninstagram.com/...",
        "width": 1439,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870915786663899914",
    "id": "3870915786663899914_4908794799",
    "code": "DW4QWYjjbMK",
    "taken_at": "2026-04-08T17:25:42Z",
    "taken_at_ts": 1775669142,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
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
      "pk": "4908794799",
      "id": "4908794799",
      "username": "stoica.eugenia",
      "full_name": "Stoica Eugenia",
      "profile_pic_url": "https://scontent-sea1-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 0,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870915716056988499",
        "id": "3870915716056988499_4908794799",
        "video_url": null,
        "thumbnail_url": "https://scontent-sea1-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              26232,
              52464,
              78697
            ],
            "height": 1917,
            "scans_profile": "e35",
            "url": "https://scontent-sea1-1.cdninstagram.com/...",
            "width": 1440,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870915786663899914_4908794799",
        "commerciality_status": "not_commercial",
        "taken_at": 1775669141
      },
      {
        "pk": "3870915717533400351",
        "id": "3870915717533400351_4908794799",
        "video_url": null,
        "thumbnail_url": "https://scontent-sea1-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              21995,
              43990,
              65986
            ],
            "height": 1917,
            "scans_profile": "e35",
            "url": "https://scontent-sea1-1.cdninstagram.com/...",
            "width": 1440,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870915786663899914_4908794799",
        "commerciality_status": "not_commercial",
        "taken_at": 1775669141
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          26232,
          52464,
          78697
        ],
        "height": 1917,
        "scans_profile": "e35",
        "url": "https://scontent-sea1-1.cdninstagram.com/...",
        "width": 1440,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  }
]
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
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_recent_chunk_v1(location_pk="213131048")
    # Next page: cl.location_medias_recent_chunk_v1(location_pk="213131048", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/recent/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"location_pk": "213131048"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/recent/chunk?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870914238210689846",
      "id": "3870914238210689846_3658495812",
      "code": "DW4P_2cjMs2",
      "taken_at": "2026-04-08T17:26:08Z",
      "taken_at_ts": 1775669168,
      "media_type": 2,
      "product_type": "clips",
      "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/...",
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
        "pk": "3658495812",
        "id": "3658495812",
        "username": "laurahanns",
        "full_name": "Laura",
        "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 0,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "🤠",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": "https://scontent-lax3-1.cdninstagram.com/...",
      "view_count": 0,
      "video_duration": 3.434999942779541,
      "title": "",
      "resources": [],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            10051,
            20103,
            30155
          ],
          "height": 900,
          "scans_profile": "e15",
          "url": "https://scontent-lax3-1.cdninstagram.com/...",
          "width": 508,
          "is_spatial_image": false
        }
      ],
      "video_versions": [
        {
          "bandwidth": 991751,
          "height": 1024,
          "id": "1278343891048193v",
          "type": 101,
          "url": "https://scontent-lax3-1.cdninstagram.com/...",
          "url_expiration_timestamp_us": null,
          "width": 576,
          "fallback": null
        }
      ],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870915939369375340",
      "id": "3870915939369375340_1263197878",
      "code": "DW4QYmxglZs",
      "taken_at": "2026-04-08T17:26:05Z",
      "taken_at_ts": 1775669165,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/...",
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
        "pk": "1263197878",
        "id": "1263197878",
        "username": "edwin.koeselitz",
        "full_name": "Edwin.köselitz",
        "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 0,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "More than a brick. - no.3 from the series \"berliner Einzelgänger\" \n.\n.\n.\n.\n.\n#streetphotography #berlín #streetsofgermany #street_photography #streetphotographyinternational",
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
            8601,
            17203,
            25804
          ],
          "height": 1440,
          "scans_profile": null,
          "url": "https://scontent-lax3-1.cdninstagram.com/...",
          "width": 1080,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870915901881106787",
      "id": "3870915901881106787_7791670114",
      "code": "DW4QYD3CMFj",
      "taken_at": "2026-04-08T17:26:03Z",
      "taken_at_ts": 1775669163,
      "media_type": 1,
      "product_type": "feed",
      "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/...",
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
        "pk": "7791670114",
        "id": "7791670114",
        "username": "almanca.ogrenmitkubra",
        "full_name": "Almanca🇩🇪Türkçe🇹🇷",
        "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 0,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "",
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
            13132,
            26265,
            39398
          ],
          "height": 1327,
          "scans_profile": "e35",
          "url": "https://scontent-lax3-2.cdninstagram.com/...",
          "width": 1323,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WzEsWzM4NzA5MTE1NzkxMDU4NDg2MjldLCJRVkZCUXpFelZubElNamc0UjA1bVVFTXpNbEJwTFd0WFZGWlVWRGhUVGpFeWVuTmZhRFZIZDJOSFJIZzJkMWxuYzJkZmJsOUlVV2QwTUY4MGNIUnBlVkkxWVVsdVZISTJkbVZvTkZsQmJVeGpTMDR0Tlc1WVZBPT0iXQ=="
]
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

    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/top",
        headers={"x-access-key": "YOUR_TOKEN"},
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
    "pk": "3870914042428987856",
    "id": "3870914042428987856_2108273813",
    "code": "DW4P9AHDRnQ",
    "taken_at": "2026-04-08T17:22:14Z",
    "taken_at_ts": 1775668934,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": {
      "pk": 105061,
      "name": "Berliner Dom",
      "phone": "",
      "website": "",
      "category": "",
      "hours": {},
      "address": "Am Lustgarten ",
      "city": "",
      "zip": null,
      "lng": 13.401190816472,
      "lat": 52.518973442797,
      "external_id": "112795185449050",
      "external_id_source": "facebook_places"
    },
    "user": {
      "pk": "2108273813",
      "id": "2108273813",
      "username": "ju.evelina",
      "full_name": "Эвелина Штейн",
      "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 0,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "💛🌼🌻🔆🏛️🍯",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870913757669297027",
        "id": "3870913757669297027_2108273813",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              56846,
              113693,
              170540
            ],
            "height": 1920,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "width": 1440,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870914042428987856_2108273813",
        "commerciality_status": "not_commercial",
        "taken_at": 1775668933
      },
      {
        "pk": "3870913761276457166",
        "id": "3870913761276457166_2108273813",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              40968,
              81937,
              122905
            ],
            "height": 1920,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "width": 1440,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870914042428987856_2108273813",
        "commerciality_status": "not_commercial",
        "taken_at": 1775668933
      },
      {
        "pk": "3870913763415552805",
        "id": "3870913763415552805_2108273813",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              48880,
              97761,
              146642
            ],
            "height": 1560,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "width": 1170,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870914042428987856_2108273813",
        "commerciality_status": "not_commercial",
        "taken_at": 1775668933
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          56846,
          113693,
          170540
        ],
        "height": 1920,
        "scans_profile": "e35",
        "url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "width": 1440,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870895297681775751",
    "id": "3870895297681775751_388090000",
    "code": "DW4LsOtDVyH",
    "taken_at": "2026-04-08T16:45:00Z",
    "taken_at_ts": 1775666700,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
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
      "pk": "388090000",
      "id": "388090000",
      "username": "rotholz",
      "full_name": "ROTHOLZ ®",
      "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 3,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "Made in a small studio in Italy, our seasonal bandanas come in a lightweight organic cotton fabric with a soft, flowing feel.",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870894992101602814",
        "id": "3870894992101602814_388090000",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              20490,
              40980,
              61470
            ],
            "height": 1473,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "width": 1179,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870895297681775751_388090000",
        "commerciality_status": "not_commercial",
        "taken_at": 1775666699
      },
      {
        "pk": "3870894994760743494",
        "id": "3870894994760743494_388090000",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              16911,
              33823,
              50734
            ],
            "height": 1473,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "width": 1179,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870895297681775751_388090000",
        "commerciality_status": "not_commercial",
        "taken_at": 1775666699
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          20490,
          40980,
          61470
        ],
        "height": 1473,
        "scans_profile": "e35",
        "url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "width": 1179,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  },
  {
    "pk": "3870892662081778265",
    "id": "3870892662081778265_1720226721",
    "code": "DW4LF4HDPJZ",
    "taken_at": "2026-04-08T16:39:45Z",
    "taken_at_ts": 1775666385,
    "media_type": 8,
    "product_type": "carousel_container",
    "thumbnail_url": null,
    "location": null,
    "user": {
      "pk": "1720226721",
      "id": "1720226721",
      "username": "foxat61",
      "full_name": "Alexandra Schofield",
      "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/...",
      "profile_pic_url_hd": null,
      "is_private": false,
      "is_verified": false
    },
    "comment_count": 0,
    "comments_disabled": false,
    "like_count": 1,
    "play_count": 0,
    "has_liked": false,
    "caption_text": "View from the loo! \nOverlooking Tiergarten and specifically the gorillas and monkeys at Berlin Zoo, top spot for sunshiney beers rounding off a day of facts, shopping and beer!",
    "accessibility_caption": null,
    "usertags": [],
    "sponsor_tags": [],
    "video_url": null,
    "view_count": 0,
    "video_duration": 0.0,
    "title": "",
    "resources": [
      {
        "pk": "3870892648223751332",
        "id": "3870892648223751332_1720226721",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              6116,
              12232,
              18349
            ],
            "height": 900,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-2.cdninstagram.com/...",
            "width": 720,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870892662081778265_1720226721",
        "commerciality_status": "not_commercial",
        "taken_at": 1775666385
      },
      {
        "pk": "3870892648785811168",
        "id": "3870892648785811168_1720226721",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              7502,
              15005,
              22508
            ],
            "height": 900,
            "scans_profile": "e35",
            "url": "https://scontent-dfw6-1.cdninstagram.com/...",
            "width": 720,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870892662081778265_1720226721",
        "commerciality_status": "not_commercial",
        "taken_at": 1775666385
      },
      {
        "pk": "3870892648844521199",
        "id": "3870892648844521199_1720226721",
        "video_url": null,
        "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/...",
        "media_type": 1,
        "product_type": "carousel_item",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              62069,
              124138,
              186207
            ],
            "height": 1920,
            "scans_profile": "e35",
            "url": "https://scontent-dfw5-1.cdninstagram.com/...",
            "width": 1536,
            "is_spatial_image": false
          }
        ],
        "video_versions": [],
        "preview": null,
        "carousel_parent_id": "3870892662081778265_1720226721",
        "commerciality_status": "not_commercial",
        "taken_at": 1775666385
      }
    ],
    "image_versions": [
      {
        "estimated_scans_sizes": [
          6116,
          12232,
          18349
        ],
        "height": 900,
        "scans_profile": "e35",
        "url": "https://scontent-dfw5-2.cdninstagram.com/...",
        "width": 720,
        "is_spatial_image": false
      }
    ],
    "video_versions": [],
    "like_and_view_counts_disabled": false,
    "coauthor_producers": [],
    "is_paid_partnership": false
  }
]
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
    # Next page: add &max_id=... from previous response
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.location_medias_top_chunk_v1(location_pk="213131048")
    # Next page: cl.location_medias_top_chunk_v1(location_pk="213131048", max_id="...")
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/location/medias/top/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"location_pk": "213131048"},
    )
    # Next page: add "max_id": "..." to params
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/location/medias/top/chunk?location_pk=213131048",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    // Next page: add &max_id=... to URL
    ```

<details>
<summary>Example response</summary>

```json
[
  [
    {
      "pk": "3870892662081778265",
      "id": "3870892662081778265_1720226721",
      "code": "DW4LF4HDPJZ",
      "taken_at": "2026-04-08T16:39:45Z",
      "taken_at_ts": 1775666385,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": null,
      "user": {
        "pk": "1720226721",
        "id": "1720226721",
        "username": "foxat61",
        "full_name": "Alexandra Schofield",
        "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 1,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "View from the loo! \nOverlooking Tiergarten and specifically the gorillas and monkeys at Berlin Zoo, top spot for sunshiney beers rounding off a day of facts, shopping and beer!",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870892648223751332",
          "id": "3870892648223751332_1720226721",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                6116,
                12232,
                18349
              ],
              "height": 900,
              "scans_profile": "e35",
              "url": "https://scontent-lax3-1.cdninstagram.com/...",
              "width": 720,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870892662081778265_1720226721",
          "commerciality_status": "not_commercial",
          "taken_at": 1775666385
        },
        {
          "pk": "3870892648785811168",
          "id": "3870892648785811168_1720226721",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                7502,
                15005,
                22508
              ],
              "height": 900,
              "scans_profile": "e35",
              "url": "https://scontent-lax3-2.cdninstagram.com/...",
              "width": 720,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870892662081778265_1720226721",
          "commerciality_status": "not_commercial",
          "taken_at": 1775666385
        },
        {
          "pk": "3870892648844521199",
          "id": "3870892648844521199_1720226721",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax7-1.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                62069,
                124138,
                186207
              ],
              "height": 1920,
              "scans_profile": "e35",
              "url": "https://scontent-lax7-1.cdninstagram.com/...",
              "width": 1536,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870892662081778265_1720226721",
          "commerciality_status": "not_commercial",
          "taken_at": 1775666385
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            6116,
            12232,
            18349
          ],
          "height": 900,
          "scans_profile": "e35",
          "url": "https://scontent-lax3-1.cdninstagram.com/...",
          "width": 720,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870895297681775751",
      "id": "3870895297681775751_388090000",
      "code": "DW4LsOtDVyH",
      "taken_at": "2026-04-08T16:45:00Z",
      "taken_at_ts": 1775666700,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
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
        "pk": "388090000",
        "id": "388090000",
        "username": "rotholz",
        "full_name": "ROTHOLZ ®",
        "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 3,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "Made in a small studio in Italy, our seasonal bandanas come in a lightweight organic cotton fabric with a soft, flowing feel.",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870894992101602814",
          "id": "3870894992101602814_388090000",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                20490,
                40980,
                61470
              ],
              "height": 1473,
              "scans_profile": "e35",
              "url": "https://scontent-lax3-2.cdninstagram.com/...",
              "width": 1179,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870895297681775751_388090000",
          "commerciality_status": "not_commercial",
          "taken_at": 1775666699
        },
        {
          "pk": "3870894994760743494",
          "id": "3870894994760743494_388090000",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax7-1.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                16911,
                33823,
                50734
              ],
              "height": 1473,
              "scans_profile": "e35",
              "url": "https://scontent-lax7-1.cdninstagram.com/...",
              "width": 1179,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870895297681775751_388090000",
          "commerciality_status": "not_commercial",
          "taken_at": 1775666699
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            20490,
            40980,
            61470
          ],
          "height": 1473,
          "scans_profile": "e35",
          "url": "https://scontent-lax3-2.cdninstagram.com/...",
          "width": 1179,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    },
    {
      "pk": "3870909232719607210",
      "id": "3870909232719607210_1698482298",
      "code": "DW4O3AuCDWq",
      "taken_at": "2026-04-08T17:12:41Z",
      "taken_at_ts": 1775668361,
      "media_type": 8,
      "product_type": "carousel_container",
      "thumbnail_url": null,
      "location": {
        "pk": 803948879707908,
        "name": "Berlin, Deutschland",
        "phone": "",
        "website": "",
        "category": "",
        "hours": {},
        "address": "",
        "city": "Berlin, Germany",
        "zip": null,
        "lng": 13.34153048,
        "lat": 52.50025492,
        "external_id": "803948879707908",
        "external_id_source": "facebook_places"
      },
      "user": {
        "pk": "1698482298",
        "id": "1698482298",
        "username": "ksifilinos",
        "full_name": "Xifilinos Travel",
        "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/...",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false
      },
      "comment_count": 0,
      "comments_disabled": false,
      "like_count": 0,
      "play_count": 0,
      "has_liked": false,
      "caption_text": "",
      "accessibility_caption": null,
      "usertags": [],
      "sponsor_tags": [],
      "video_url": null,
      "view_count": 0,
      "video_duration": 0.0,
      "title": "",
      "resources": [
        {
          "pk": "3870908984903396307",
          "id": "3870908984903396307_1698482298",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                18728,
                37456,
                56184
              ],
              "height": 1920,
              "scans_profile": "e35",
              "url": "https://scontent-lax3-2.cdninstagram.com/...",
              "width": 1440,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870909232719607210_1698482298",
          "commerciality_status": "not_commercial",
          "taken_at": 1775668358
        },
        {
          "pk": "3870908990414686785",
          "id": "3870908990414686785_1698482298",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                25689,
                51378,
                77067
              ],
              "height": 1080,
              "scans_profile": "e35",
              "url": "https://scontent-lax3-1.cdninstagram.com/...",
              "width": 1440,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870909232719607210_1698482298",
          "commerciality_status": "not_commercial",
          "taken_at": 1775668358
        },
        {
          "pk": "3870908998719376543",
          "id": "3870908998719376543_1698482298",
          "video_url": null,
          "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/...",
          "media_type": 1,
          "product_type": "carousel_item",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                21743,
                43487,
                65231
              ],
              "height": 1920,
              "scans_profile": "e35",
              "url": "https://scontent-lax3-2.cdninstagram.com/...",
              "width": 1440,
              "is_spatial_image": false
            }
          ],
          "video_versions": [],
          "preview": null,
          "carousel_parent_id": "3870909232719607210_1698482298",
          "commerciality_status": "not_commercial",
          "taken_at": 1775668358
        }
      ],
      "image_versions": [
        {
          "estimated_scans_sizes": [
            18728,
            37456,
            56184
          ],
          "height": 1920,
          "scans_profile": "e35",
          "url": "https://scontent-lax3-2.cdninstagram.com/...",
          "width": 1440,
          "is_spatial_image": false
        }
      ],
      "video_versions": [],
      "like_and_view_counts_disabled": false,
      "coauthor_producers": [],
      "is_paid_partnership": false
    }
  ],
  "WzEsWzM4NzA4NDA4MjE5ODU4NDIwMjJdLCJmNWM2NjhiMmUzMzA0NzMxOGFmYWNjNTk2ZjQxMGY0YyJd"
]
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

    response = requests.get(
        "https://api.hikerapi.com/v1/location/search",
        headers={"x-access-key": "YOUR_TOKEN"},
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
  },
  {
    "pk": null,
    "name": "Downtown New York",
    "phone": "",
    "website": "",
    "category": "",
    "hours": {},
    "address": "<0.1mi",
    "city": null,
    "zip": null,
    "lng": -74.0059728,
    "lat": 40.7127753,
    "external_id": "385666572019058",
    "external_id_source": "facebook_places"
  }
]
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-locations){ target=_blank }
