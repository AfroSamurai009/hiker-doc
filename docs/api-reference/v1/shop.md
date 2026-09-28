# Shop Endpoints

Instagram Shop: seller info, storefront collections and products.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/v1/shop/about`](#get-v1shopabout) | [`/v1/shop/products/by_collection/chunk`](#get-v1shopproductsby_collectionchunk) | [`/v1/shop/storefront`](#get-v1shopstorefront)

---

### GET /v1/shop/about

Get "About this shop": seller name, address, contacts, privacy policy

`user_id` is the pk of the account that owns the shop; a merchant id
(`17841...`) is accepted too.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/shop/about?user_id=254591602"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/shop/about",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "254591602"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/shop/about?user_id=254591602",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v1/shop/products/by_collection/chunk

Get a chunk of products of a shop collection

`encoded_collection_id` comes from `collections[]` of
`/v1/shop/storefront`. The Instagram pagination payload is ~10 KB, too
long for a query string, so it is kept server-side and the client gets an
opaque 64-char `cursor` that lives 24 hours.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `encoded_collection_id` | string | Yes | Encoded Collection Id |
| `cursor` | string | No | Use value of the second element of the previous response. The cursor is valid for 24 hours. |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/shop/products/by_collection/chunk?encoded_collection_id=all_products:630954291743565:254591602"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/shop/products/by_collection/chunk",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"encoded_collection_id": "all_products:630954291743565:254591602"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/shop/products/by_collection/chunk?encoded_collection_id=all_products:630954291743565:254591602",
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
      "product_id": "28385557674430352",
      "merchant_id": "17841401908063977",
      "merchant_pk": 254591602,
      "merchant_username": "buffbunny_collection",
      "title": "Iconic Mesh Jersey - Rose Water",
      "price": "$42.00",
      "full_price": "$42.00",
      "price_amount": 42.0,
      "full_price_amount": 42.0,
      "image_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "image_id": "1729339085371026",
      "image_width": 776,
      "image_height": 1035,
      "external_url": "https://www.buffbunny.com/products/iconic-mesh-jersey-rose-water?utm_content=Facebook_UA&utm_source=facebook&variant=51523080192132",
      "checkout_style": "offsite_link"
    },
    {
      "product_id": "28221474770806382",
      "merchant_id": "17841401908063977",
      "merchant_pk": 254591602,
      "merchant_username": "buffbunny_collection",
      "title": "Iconic Mesh Jersey - Mystique",
      "price": "$42.00",
      "full_price": "$42.00",
      "price_amount": 42.0,
      "full_price_amount": 42.0,
      "image_url": "https://scontent-sjc3-1.cdninstagram.com/...",
      "image_id": "1564928251419714",
      "image_width": 1535,
      "image_height": 2048,
      "external_url": "https://www.buffbunny.com/products/iconic-mesh-jersey-mystique?utm_content=Facebook_UA&utm_source=facebook&variant=51523091595396",
      "checkout_style": "offsite_link"
    },
    {
      "product_id": "28773514292336848",
      "merchant_id": "17841401908063977",
      "merchant_pk": 254591602,
      "merchant_username": "buffbunny_collection",
      "title": "Iconic Mesh Jersey - Stardust",
      "price": "$42.00",
      "full_price": "$42.00",
      "price_amount": 42.0,
      "full_price_amount": 42.0,
      "image_url": "https://scontent-sjc6-1.cdninstagram.com/...",
      "image_id": "1844207433609416",
      "image_width": 849,
      "image_height": 1131,
      "external_url": "https://www.buffbunny.com/products/iconic-mesh-jersey-stardust?utm_content=Facebook_UA&utm_source=facebook&variant=51523090743428",
      "checkout_style": "offsite_link"
    }
  ],
  "d28b40d255063c1f6cee1432766aa45f17a481956602ef41039efe87f22be18e"
]
```

</details>

---

### GET /v1/shop/storefront

Get shop storefront: merchant ids, collections and first-screen products

A shop exists when `/v2/user/by/username` returns
`seller_shoppable_feed_type == "mini_shop_wave_2"`; an account without a
shop answers 404 `ShopNotFound`. Use `encoded_collection_id` from
`collections[]` to page through products. A storefront made of curated
collections only can return an empty `products[]` — that is not an error.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v1/shop/storefront?user_id=254591602"
    ```

=== "Python (requests)"

    ```python
    import requests

    response = requests.get(
        "https://api.hikerapi.com/v1/shop/storefront",
        headers={"x-access-key": "YOUR_TOKEN"},
        params={"user_id": "254591602"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v1/shop/storefront?user_id=254591602",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "merchant_id": "17841401908063977",
  "merchant_pk": 254591602,
  "merchant_username": "buffbunny_collection",
  "collections": [
    {
      "encoded_collection_id": "pivot_collection:630954291743565:254591602",
      "collection_type": "pivot_collection",
      "collection_page_id": null,
      "name": null
    },
    {
      "encoded_collection_id": "all_products:630954291743565:254591602",
      "collection_type": "all_products",
      "collection_page_id": null,
      "name": null
    }
  ],
  "products": [
    {
      "product_id": "27863177590027404",
      "merchant_id": "17841401908063977",
      "merchant_pk": 254591602,
      "merchant_username": "buffbunny_collection",
      "title": "Iconic Mesh Jersey - Mystique",
      "price": "$42.00",
      "full_price": "$42.00",
      "price_amount": 42.0,
      "full_price_amount": 42.0,
      "image_url": "https://scontent-det1-1.cdninstagram.com/...",
      "image_id": "1065532902965989",
      "image_width": 793,
      "image_height": 1079,
      "external_url": "https://www.buffbunny.com/products/iconic-mesh-jersey-mystique?utm_content=Facebook_UA&utm_source=facebook&variant=51523091660932",
      "checkout_style": "offsite_link"
    },
    {
      "product_id": "27708949332115929",
      "merchant_id": "17841401908063977",
      "merchant_pk": 254591602,
      "merchant_username": "buffbunny_collection",
      "title": "Iconic Mesh Jersey - Gamma Green",
      "price": "$42.00",
      "full_price": "$42.00",
      "price_amount": 42.0,
      "full_price_amount": 42.0,
      "image_url": "https://scontent-det1-1.cdninstagram.com/...",
      "image_id": "1709654460147034",
      "image_width": 880,
      "image_height": 1174,
      "external_url": "https://www.buffbunny.com/products/iconic-mesh-jersey-gamma-green?utm_content=Facebook_UA&utm_source=facebook&variant=51523089236100",
      "checkout_style": "offsite_link"
    },
    {
      "product_id": "28227056516986943",
      "merchant_id": "17841401908063977",
      "merchant_pk": 254591602,
      "merchant_username": "buffbunny_collection",
      "title": "Strong Sports Bra - Mystique",
      "price": "$44.00",
      "full_price": "$44.00",
      "price_amount": 44.0,
      "full_price_amount": 44.0,
      "image_url": "https://scontent-det1-1.cdninstagram.com/...",
      "image_id": "1773111823814983",
      "image_width": 694,
      "image_height": 925,
      "external_url": "https://www.buffbunny.com/products/strong-seamless-sports-bra-mystique?utm_content=Facebook_UA&utm_source=facebook&variant=51520529039492",
      "checkout_style": "offsite_link"
    }
  ]
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v1-shop){ target=_blank }
