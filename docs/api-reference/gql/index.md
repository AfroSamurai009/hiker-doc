# GraphQL API

Instagram GraphQL endpoints with cursor-based pagination.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/g2/user/followers`](#get-g2userfollowers) | [`/g2/user/following`](#get-g2userfollowing) | [`/gql/comment/likers`](#get-gqlcommentlikers) | [`/gql/comment/likers/chunk`](#get-gqlcommentlikerschunk) | [`/gql/comments`](#get-gqlcomments) | [`/gql/comments/chunk`](#get-gqlcommentschunk) | [`/gql/comments/threaded`](#get-gqlcommentsthreaded) | [`/gql/comments/threaded/chunk`](#get-gqlcommentsthreadedchunk) | [`/gql/media/likers`](#get-gqlmedialikers) | [`/gql/media/usertags`](#get-gqlmediausertags) | [`/gql/topsearch`](#get-gqltopsearch) | [`/gql/user/by/id`](#get-gqluserbyid) | [`/gql/user/by/username`](#get-gqluserbyusername) | [`/gql/user/clips`](#get-gqluserclips) | [`/gql/user/followers`](#get-gqluserfollowers) | [`/gql/user/followers/chunk`](#get-gqluserfollowerschunk) | [`/gql/user/following`](#get-gqluserfollowing) | [`/gql/user/following/chunk`](#get-gqluserfollowingchunk) | [`/gql/user/medias`](#get-gqlusermedias) | [`/gql/user/related/profiles`](#get-gqluserrelatedprofiles) | [`/gql/user/reposts`](#get-gqluserreposts) | [`/gql/user/web_profile_info`](#get-gqluserweb_profile_info)

---

### GET /g2/user/followers

Get part (one page) of followers users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `page_id` | string | No | Page Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/g2/user/followers?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/g2/user/followers",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/g2/user/followers?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "users": [
      {
        "__typename": "XDTUserDict",
        "strong_id__": "41668656782",
        "id": "41668656782",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841441543478582",
        "full_name": "emiliana ᡣ𐭩",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": false,
        "is_verified": false,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "friendship_status": {
          "following": false,
          "incoming_request": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "outgoing_request": false
        },
        "pk": "41668656782",
        "profile_pic_id": "3870865179543084090_41668656782",
        "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/660830868_18068601482384783_221122897203355395_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gFY34bOOKGuHAG4qZEz1r1CzHB9zgugpKtl3kyVUaY_svPa-2T3IM4ORQPKGZ2i5d4&_nc_ohc=d_02GQQswNAQ7kNvwGlc5up&_nc_gid=G30jeY0bPX-cpvbS-dfpzw&edm=AIfao94BAAAA&ccb=7-5&ig_cache_key=GJR6YyePFfIcTDFAAAPfgnsalhEDbmNDAQAB1501500j-ccb7-5&oh=00_Af13VwImJS8zuzJ7j-OPYokJiE_8Jno47kDaWn9n73ORuQ&oe=69DC4D93&_nc_sid=9f8d40",
        "reel_auto_archive": null,
        "username": "emiliareview",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "37859019705",
        "id": "37859019705",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841437791172377",
        "full_name": "",
        "has_anonymous_profile_picture": true,
        "interop_messaging_user_fbid": null,
        "is_private": true,
        "is_verified": false,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "friendship_status": {
          "following": false,
          "incoming_request": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": true,
          "is_restricted": false,
          "outgoing_request": false
        },
        "pk": "37859019705",
        "profile_pic_id": null,
        "profile_pic_url": "https://instagram.fcgh4-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-webp&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fcgh4-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gEJNT3WvGxdWga5SDOtLp3-p4VYxKf8m6HHqUauvN6R12w4n6Yp0-ppNWn6sEfJHmPKds_VPoX6pYTVboek-7Kg&_nc_ohc=a8xHEXzvkAIQ7kNvwHSCLCj&_nc_gid=uL7I90kgHailxyhgP_l1Bg&edm=AFs-eF8BAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af1nW7VRurfmqbWoU_3oXfckopMKud9x21dgxZr5drNrdA&oe=69DC366A&_nc_sid=72eed0",
        "reel_auto_archive": null,
        "username": "catsnake206",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "39102974861",
        "id": "39102974861",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841439085857871",
        "full_name": "Anthony",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": false,
        "is_verified": false,
        "1llatest_reel_media": 0,
        "liked_clips_count": null,
        "account_badges": [],
        "social_context": null,
        "friendship_status": {
          "following": false,
          "incoming_request": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "outgoing_request": false
        },
        "pk": "39102974861",
        "profile_pic_id": "3870863838152879125_39102974861",
        "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/659192141_18075463877302862_5791951774016899382_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42MDQuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gFY34bOOKGuHAG4qZEz1r1CzHB9zgugpKtl3kyVUaY_svPa-2T3IM4ORQPKGZ2i5d4&_nc_ohc=RtByDxFG4sQQ7kNvwHMkQtm&_nc_gid=G30jeY0bPX-cpvbS-dfpzw&edm=AIfao94BAAAA&ccb=7-5&ig_cache_key=GE15SidOmo7jiTdAADaJeI5zJWFQbmNDAQAB1501500j-ccb7-5&oh=00_Af2YCcCnaOZC6Aml9ql_UkDuqb7SEP4NOtNFo0TT6r0RZA&oe=69DC4F9B&_nc_sid=9f8d40",
        "reel_auto_archive": null,
        "username": "templar.sarahpg",
        "all_media_count": null
      }
    ],
    "next_max_id": null,
    "should_limit_list_of_followers": true
  },
  "next_page_id": null
}
```

</details>

---

### GET /g2/user/following

Get part (one page) of following users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `page_id` | string | No | Page Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/g2/user/following?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/g2/user/following",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/g2/user/following?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "users": [],
    "next_max_id": null,
    "has_more": false
  },
  "next_page_id": null
}
```

</details>

---

### GET /gql/comment/likers

Get likers on a comment

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comment/likers?media_id=3776832898280228145"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/comment/likers",
        headers=headers,
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/comment/likers?media_id=3776832898280228145",
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

### GET /gql/comment/likers/chunk

Get likers on a comment

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `comment_id` | string | No | Comment Id |
| `media_id` | string | No | Media Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comment/likers/chunk?comment_id=17901801633335930&media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.comment_likers_chunk_gql(comment_id="17901801633335930", media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/comment/likers/chunk",
        headers=headers,
        params={"comment_id": "17901801633335930", "media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/comment/likers/chunk?comment_id=17901801633335930&media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /gql/comments

Get comments on a media

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `sort_order` | string | No | Sort Order |
| `amount` | integer | No | Amount |
| `max_requests` | integer | No | Max Requests |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comments?media_id=3776832898280228145"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/comments",
        headers=headers,
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/comments?media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "17988842789786755",
    "user": {
      "is_verified": false,
      "id": "57093755334",
      "pk": "57093755334",
      "username": "imsoumya_12",
      "is_unpublished": null,
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/637874143_18000571244899335_4344695742994650168_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gG0ISsEMg07jXtltCFAWQiuE2W_3-zSM7JnM1hQboVS1yDTEUSN7rN06E89jvgTO1U&_nc_ohc=dBFMb_fAhlIQ7kNvwE-Wc1F&_nc_gid=YW-8_1bJgh-eorNvcnriDw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af0aABVTShc1M-md2x7Ug6-NpdoWyWdUw7VMT78rfSurAg&oe=69DC614A&_nc_sid=10d13b",
      "fbid_v2": "17841456980046719"
    },
    "is_covered": false,
    "child_comment_count": 0,
    "restricted_status": null,
    "parent_comment_id": null,
    "has_translation": null,
    "has_liked_comment": false,
    "text": "I want to build a house there ☺️",
    "created_at": 1774293705,
    "comment_like_count": 0,
    "giphy_media_info": null,
    "__typename": "XDTCommentDict"
  },
  {
    "pk": "18129360946549093",
    "user": {
      "is_verified": false,
      "id": "77976112959",
      "pk": "77976112959",
      "username": "lenoid62",
      "is_unpublished": null,
      "profile_pic_url": "https://instagram.fbth12-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fbth12-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gFhFctNC8ZR1_vQZQ2R1sKIqEy3wLEZlFtr7yDr63JD5gLETYI1q3yte4vhUOXm4L0&_nc_ohc=a8xHEXzvkAIQ7kNvwGeH_3k&_nc_gid=GNxzej--P3-Ja_3IIQW0Ug&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af0s-EJvSrms-wy0e3iobgXjYk2s-Fl23rRmJtpVE1fyBA&oe=69DC366A&_nc_sid=847350",
      "fbid_v2": "17841477788797014"
    },
    "is_covered": false,
    "child_comment_count": 0,
    "restricted_status": null,
    "parent_comment_id": null,
    "has_translation": null,
    "has_liked_comment": false,
    "text": "What a rainforest that's all I do this rain",
    "created_at": 1773230981,
    "comment_like_count": 0,
    "giphy_media_info": null,
    "__typename": "XDTCommentDict"
  },
  {
    "pk": "18111056248578971",
    "user": {
      "is_verified": false,
      "id": "1336487531",
      "pk": "1336487531",
      "username": "uemaaru",
      "is_unpublished": null,
      "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.2885-19/424452175_219315124592338_4571001550298011010_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gG0ISsEMg07jXtltCFAWQiuE2W_3-zSM7JnM1hQboVS1yDTEUSN7rN06E89jvgTO1U&_nc_ohc=d3KBcGCYEUkQ7kNvwHIxyh-&_nc_gid=YW-8_1bJgh-eorNvcnriDw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2HPRK4zAuzicWyD9wRtLfLMo49ZbHHAx1Ewjddr5_g4w&oe=69DC45A9&_nc_sid=10d13b",
      "fbid_v2": "17841401185950882"
    },
    "is_covered": false,
    "child_comment_count": 0,
    "restricted_status": null,
    "parent_comment_id": null,
    "has_translation": null,
    "has_liked_comment": false,
    "text": "心地いい👂🏼",
    "created_at": 1770335847,
    "comment_like_count": 0,
    "giphy_media_info": null,
    "__typename": "XDTCommentDict"
  }
]
```

</details>

---

### GET /gql/comments/chunk

Get comments on a media. Returns Comment objects with cursor.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `sort_order` | string | No | Sort Order |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comments/chunk?media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.comments_chunk_gql(media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/comments/chunk",
        headers=headers,
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/comments/chunk?media_id=3776832898280228145",
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
      "pk": "17988842789786755",
      "user": {
        "is_verified": false,
        "id": "57093755334",
        "pk": "57093755334",
        "username": "imsoumya_12",
        "is_unpublished": null,
        "profile_pic_url": "https://scontent-waw2-2.cdninstagram.com/v/t51.82787-19/637874143_18000571244899335_4344695742994650168_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gH9sxr9Ticf8peMmdJEiNxkkZ04cH4keigqPnqnKEiATGvvpf-qb_c-oABORi4Jsr0&_nc_ohc=dBFMb_fAhlIQ7kNvwGc65GU&_nc_gid=Z-Q4bKmbOmewsN1S_cPSFQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af0kUtLXZ4FW9qubiaatfnYRQOiuLFGXMd5YuJMpAjZgWQ&oe=69DC614A&_nc_sid=10d13b",
        "fbid_v2": "17841456980046719"
      },
      "is_covered": false,
      "child_comment_count": 0,
      "restricted_status": null,
      "parent_comment_id": null,
      "has_translation": null,
      "has_liked_comment": false,
      "text": "I want to build a house there ☺️",
      "created_at": 1774293705,
      "comment_like_count": 0,
      "giphy_media_info": null,
      "__typename": "XDTCommentDict"
    },
    {
      "pk": "18129360946549093",
      "user": {
        "is_verified": false,
        "id": "77976112959",
        "pk": "77976112959",
        "username": "lenoid62",
        "is_unpublished": null,
        "profile_pic_url": "https://instagram.fbel1-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fbel1-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gGzSLAhAIZWFQ-GYgY-IZVgz7InCdNHyxuPVRpnFz29-uVfIxsfGMgxoNJdwjyCwYrUyrSM6MjM4HZfPCREHvBg&_nc_ohc=a8xHEXzvkAIQ7kNvwEiCdzN&_nc_gid=ywp3jDjci9QDbUm5SvmTYw&edm=ALlQn9MBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af3zwEO3e_eVLnGSZXMPYzAtigu6VzNz8Cs5GukOKDn_nw&oe=69DC366A&_nc_sid=e7f676",
        "fbid_v2": "17841477788797014"
      },
      "is_covered": false,
      "child_comment_count": 0,
      "restricted_status": null,
      "parent_comment_id": null,
      "has_translation": null,
      "has_liked_comment": false,
      "text": "What a rainforest that's all I do this rain",
      "created_at": 1773230981,
      "comment_like_count": 0,
      "giphy_media_info": null,
      "__typename": "XDTCommentDict"
    },
    {
      "pk": "18111056248578971",
      "user": {
        "is_verified": false,
        "id": "1336487531",
        "pk": "1336487531",
        "username": "uemaaru",
        "is_unpublished": null,
        "profile_pic_url": "https://scontent-waw2-1.cdninstagram.com/v/t51.2885-19/424452175_219315124592338_4571001550298011010_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gH9sxr9Ticf8peMmdJEiNxkkZ04cH4keigqPnqnKEiATGvvpf-qb_c-oABORi4Jsr0&_nc_ohc=d3KBcGCYEUkQ7kNvwFCWuqW&_nc_gid=Z-Q4bKmbOmewsN1S_cPSFQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af1uT2b7p6qSY_aDKwazGprq7kOvTT0hNs_1Ff9lWAvoGQ&oe=69DC45A9&_nc_sid=10d13b",
        "fbid_v2": "17841401185950882"
      },
      "is_covered": false,
      "child_comment_count": 0,
      "restricted_status": null,
      "parent_comment_id": null,
      "has_translation": null,
      "has_liked_comment": false,
      "text": "心地いい👂🏼",
      "created_at": 1770335847,
      "comment_like_count": 0,
      "giphy_media_info": null,
      "__typename": "XDTCommentDict"
    }
  ],
  "{\"server_cursor\": \"QVFDWnh5ZHEwZk44eDBzeWZCS3VIdFZZUnBkbGJKZHhxb3VreXB2NkJvWjV3SW95a2lPVGlkeDRyNHU2MWR2dkRCZktZS3NVZnh4WVhiZS0yc3B6R25vdg==\", \"is_server_cursor_inverse\": true}"
]
```

</details>

---

### GET /gql/comments/threaded

Get threaded comments for comment

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `comment_id` | string | Yes | Comment Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comments/threaded?media_id=3776832898280228145&comment_id=17901801633335930"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/comments/threaded",
        headers=headers,
        params={"media_id": "3776832898280228145", "comment_id": "17901801633335930"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/comments/threaded?media_id=3776832898280228145&comment_id=17901801633335930",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /gql/comments/threaded/chunk

Get threaded comments for comment

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |
| `comment_id` | string | Yes | Comment Id |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/comments/threaded/chunk?media_id=3776832898280228145&comment_id=17901801633335930"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.comments_threaded_chunk_gql(media_id="3776832898280228145", comment_id="17901801633335930")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/comments/threaded/chunk",
        headers=headers,
        params={"media_id": "3776832898280228145", "comment_id": "17901801633335930"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/comments/threaded/chunk?media_id=3776832898280228145&comment_id=17901801633335930",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /gql/media/likers

Get likers on a media (paging is unavailable on this endpoint). Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_id` | string | Yes | Media Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/media/likers?media_id=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_likers_gql(media_id="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/media/likers",
        headers=headers,
        params={"media_id": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/media/likers?media_id=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "2228799241",
    "__typename": "XDTUserDict",
    "username": "miftasya._",
    "full_name": "Mifta D. Syafira",
    "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/657368100_18524206573079242_7484305376738684507_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHq7A6nklCPJ6BcF361Yrhkfxdy8dwuhK4Wk26E8jdNBi4GkH7YQIkb6qOcPfOufPY&_nc_ohc=vI3vQUoB9qcQ7kNvwG4jFNO&_nc_gid=t9dNII7N4uLPyiSlu7XtZA&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af1SFY-UjviH99ncABoB1PcelerIzyqJMkZlWTV83zRw_w&oe=69DC5C8C&_nc_sid=10d13b",
    "is_verified": false,
    "social_context": null,
    "friendship_status": {
      "blocking": false,
      "is_feed_favorite": false,
      "following": false,
      "is_muting_reel": false,
      "muting": false,
      "outgoing_request": false,
      "followed_by": false,
      "incoming_request": false,
      "is_restricted": false,
      "is_bestie": false
    },
    "supervision_info": null,
    "id": "2228799241"
  },
  {
    "pk": "277099018",
    "__typename": "XDTUserDict",
    "username": "nikki_says_meow",
    "full_name": "Nikki Gosal",
    "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.82787-19/521543842_18519945877043019_5787012878919658365_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHq7A6nklCPJ6BcF361Yrhkfxdy8dwuhK4Wk26E8jdNBi4GkH7YQIkb6qOcPfOufPY&_nc_ohc=Na0h44VZnZwQ7kNvwE--Aq6&_nc_gid=t9dNII7N4uLPyiSlu7XtZA&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2xXwClm6gWHePnfJCmRLNeEZTlW9ZiMV7Sc1srpJQDmA&oe=69DC4AE7&_nc_sid=10d13b",
    "is_verified": false,
    "social_context": null,
    "friendship_status": {
      "blocking": false,
      "is_feed_favorite": false,
      "following": false,
      "is_muting_reel": false,
      "muting": false,
      "outgoing_request": false,
      "followed_by": false,
      "incoming_request": false,
      "is_restricted": false,
      "is_bestie": false
    },
    "supervision_info": null,
    "id": "277099018"
  },
  {
    "pk": "3992818700",
    "__typename": "XDTUserDict",
    "username": "linethquirurgica",
    "full_name": "Lineth García González",
    "profile_pic_url": "https://scontent-vie1-1.cdninstagram.com/v/t51.2885-19/157549418_882220615673899_6557157409243783974_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43NjAuYzIifQ&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHq7A6nklCPJ6BcF361Yrhkfxdy8dwuhK4Wk26E8jdNBi4GkH7YQIkb6qOcPfOufPY&_nc_ohc=WWtMoKftwLgQ7kNvwF7aYi2&_nc_gid=t9dNII7N4uLPyiSlu7XtZA&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2GBMJd14769ONwagwG55_3MpAZHF0RWHOEVpZLWtAs9g&oe=69DC3DF9&_nc_sid=10d13b",
    "is_verified": false,
    "social_context": null,
    "friendship_status": {
      "blocking": false,
      "is_feed_favorite": false,
      "following": false,
      "is_muting_reel": false,
      "muting": false,
      "outgoing_request": false,
      "followed_by": false,
      "incoming_request": false,
      "is_restricted": false,
      "is_bestie": false
    },
    "supervision_info": null,
    "id": "3992818700"
  }
]
```

</details>

---

### GET /gql/media/usertags

Returns users tagged in the video. You can pass up to 10 media ids

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `media_ids` | array | No | Media Ids |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/media/usertags?media_ids=3776832898280228145"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.media_usertags_gql(media_ids="3776832898280228145")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/media/usertags",
        headers=headers,
        params={"media_ids": "3776832898280228145"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/media/usertags?media_ids=3776832898280228145",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "data": {
    "__typename": "Query",
    "strong_id__": null,
    "1$multifetch__XDTMediaDict(ids:$media_ids)": [
      {
        "node": {
          "__typename": "XDTMediaDict",
          "strong_id__": "3776832898280228145_787132",
          "id": "3776832898280228145_787132",
          "usertags": null,
          "clips_metadata": {
            "template_info": null
          }
        }
      }
    ]
  },
  "extensions": {
    "is_final": true,
    "server_metadata": {
      "request_start_time_ms": 1775663970464,
      "time_at_flush_ms": 1775663970506
    }
  },
  "status": "ok"
}
```

</details>

---

### GET /gql/topsearch

Search top content by keyword (GraphQL TopSerpQuery)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query |
| `end_cursor` | string | No | End Cursor |
| `flat` | boolean | No | Flatten nested response into simple items list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/topsearch?query=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.topsearch_gql(query="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/topsearch",
        headers=headers,
        params={"query": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/topsearch?query=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "data": {
        "__typename": "Query",
        "strong_id__": null,
        "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})": {
          "edges": [
            {
              "__typename": "XDTTopSerpGraphQLConnectionEdge",
              "strong_id__": null,
              "node": {
                "__typename": "XDTTopSerpHeaderUnit",
                "strong_id__": null,
                "is_fulfilled__(name:\"XDTTopSerpUnitInterface\")": true,
                "unit_type": "HEADER",
                "is_fulfilled__(name:\"XDTTopSerpHeaderUnit\")": true,
                "header": "Accounts"
              },
              "cursor": null
            },
            {
              "__typename": "XDTTopSerpGraphQLConnectionEdge",
              "strong_id__": null,
              "node": {
                "__typename": "XDTTopSerpAccountsHCMUnit",
                "strong_id__": null,
                "is_fulfilled__(name:\"XDTTopSerpUnitInterface\")": true,
                "unit_type": "ACCOUNTS_HCM",
                "is_fulfilled__(name:\"XDTTopSerpAccountsHCMUnit\")": true,
                "rank_token": "1775664150729|3373edf051e1b236a0546340d0b3674ada55c34cd96fcc913517331f9b462af1",
                "items": [
                  {
                    "__typename": "XDTUserDict",
                    "strong_id__": "787132",
                    "id": "787132",
                    "is_fulfilled__(name:\"XDTUserDict\")": true,
                    "fbid_v2": "17841400573960012",
                    "username": "natgeo",
                    "full_name": "National Geographic",
                    "profile_pic_id": "3865702555259028436_787132",
                    "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE63O2yHvnsxSK5AmNEEku4z1aiUJSDCSCgdYJ3hE9BIoXn0F2ZxAPjQ-A75cg0BPw&_nc_ohc=XbeNvhLXv28Q7kNvwHywUHy&_nc_gid=bO8DwAhwAuglGlGOn_TBwg&edm=ADuq63kBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af05WmF4p3KawAqa5sZBWd2Ia__fdasUEipx5l6Bc_7mVw&oe=69DC51E9&_nc_sid=cebafd"
                  },
                  {
                    "__typename": "XDTUserDict",
                    "strong_id__": "23947096",
                    "id": "23947096",
                    "is_fulfilled__(name:\"XDTUserDict\")": true,
                    "fbid_v2": "17841400332880374",
                    "username": "natgeotravel",
                    "full_name": "National Geographic Travel",
                    "profile_pic_id": "3865702501739707616_23947096",
                    "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE63O2yHvnsxSK5AmNEEku4z1aiUJSDCSCgdYJ3hE9BIoXn0F2ZxAPjQ-A75cg0BPw&_nc_ohc=t-DCVZxwtX4Q7kNvwE_tgwh&_nc_gid=bO8DwAhwAuglGlGOn_TBwg&edm=ADuq63kBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af0lPDiZuMNfvlhRJI2FzEJoc291JpI2JBvGWxE8aCvOAg&oe=69DC6746&_nc_sid=cebafd"
                  }
                ]
              },
              "cursor": null
            }
          ]
        }
      },
      "extensions": {
        "is_final": false,
        "fulfilled_payloads": [
          {
            "label": "TopSerpHeaderFragment__force_flush",
            "path": [
              "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
              "edges",
              0
            ]
          },
          {
            "label": "TopSerpAccountsHCMFragment__force_flush",
            "path": [
              "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
              "edges",
              1
            ]
          }
        ],
        "server_metadata": {
          "request_start_time_ms": 1775664150310,
          "time_at_flush_ms": 1775664151432
        }
      },
      "status": "ok"
    },
    {
      "errors": [
        {
          "message": "execution error",
          "path": [
            "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
            "edges",
            1
          ],
          "severity": "ERROR"
        },
        {
          "message": "execution error",
          "path": [
            "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
            "edges",
            1
          ],
          "severity": "ERROR"
        },
        {
          "message": "execution error",
          "path": [
            "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
            "edges",
            1
          ],
          "severity": "ERROR"
        }
      ],
      "path": [
        "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
        "edges",
        1
      ],
      "label": "UserSearchEntryDeferredFragment",
      "data": {
        "__typename": "XDTUserDict",
        "strong_id__": "787132",
        "id": "787132",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "is_verified": true,
        "search_subtitle": null,
        "live_broadcast_id": null,
        "account_badges": [],
        "ai_agent_owner_username": null,
        "can_coauthor_posts": true,
        "can_coauthor_posts_with_music": true,
        "extra_display_name": null,
        "fbid_v2": "17841400573960012",
        "friendship_status": {
          "blocking": false,
          "followed_by": false,
          "following": false,
          "incoming_request": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "outgoing_request": false
        },
        "full_name": "National Geographic",
        "has_anonymous_profile_picture": false,
        "has_onboarded_to_text_post_app": null,
        "is_ai_user": null,
        "is_mentionable": true,
        "is_private": false,
        "is_ring_creator": false,
        "is_taggable": true,
        "is_verified_search_boosted": false,
        "1llatest_reel_media": 1775659002,
        "live_broadcast_visibility": null,
        "profile_pic_id": "3865702555259028436_787132",
        "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE63O2yHvnsxSK5AmNEEku4z1aiUJSDCSCgdYJ3hE9BIoXn0F2ZxAPjQ-A75cg0BPw&_nc_ohc=XbeNvhLXv28Q7kNvwHywUHy&_nc_gid=bO8DwAhwAuglGlGOn_TBwg&edm=ADuq63kBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af05WmF4p3KawAqa5sZBWd2Ia__fdasUEipx5l6Bc_7mVw&oe=69DC51E9&_nc_sid=cebafd",
        "search_serp_type": 3,
        "search_social_context": "274M followers",
        "search_social_context_facepiles": null,
        "search_social_context_snippet_type": "typeahead_follow_count",
        "shopping_search_subtitle": null,
        "should_show_category": true,
        "show_ig_app_switcher_badge": true,
        "search_secondary_subtitle": null,
        "show_ring_award": false,
        "show_text_post_app_badge": true,
        "social_context": "274M followers",
        "third_party_downloads_enabled": 2,
        "unseen_count": 0,
        "username": "natgeo"
      },
      "extensions": {
        "is_final": false
      }
    },
    {
      "errors": [
        {
          "message": "execution error",
          "path": [
            "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
            "edges",
            1
          ],
          "severity": "ERROR"
        },
        {
          "message": "execution error",
          "path": [
            "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
            "edges",
            1
          ],
          "severity": "ERROR"
        },
        {
          "message": "execution error",
          "path": [
            "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
            "edges",
            1
          ],
          "severity": "ERROR"
        }
      ],
      "path": [
        "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
        "edges",
        1
      ],
      "label": "UserSearchEntryDeferredFragment",
      "data": {
        "__typename": "XDTUserDict",
        "strong_id__": "23947096",
        "id": "23947096",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "is_verified": true,
        "search_subtitle": null,
        "live_broadcast_id": null,
        "account_badges": [],
        "ai_agent_owner_username": null,
        "can_coauthor_posts": true,
        "can_coauthor_posts_with_music": true,
        "extra_display_name": null,
        "fbid_v2": "17841400332880374",
        "friendship_status": {
          "blocking": false,
          "followed_by": false,
          "following": false,
          "incoming_request": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
          "outgoing_request": false
        },
        "full_name": "National Geographic Travel",
        "has_anonymous_profile_picture": false,
        "has_onboarded_to_text_post_app": null,
        "is_ai_user": null,
        "is_mentionable": true,
        "is_private": false,
        "is_ring_creator": false,
        "is_taggable": true,
        "is_verified_search_boosted": false,
        "1llatest_reel_media": 1775582271,
        "live_broadcast_visibility": null,
        "profile_pic_id": "3865702501739707616_23947096",
        "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE63O2yHvnsxSK5AmNEEku4z1aiUJSDCSCgdYJ3hE9BIoXn0F2ZxAPjQ-A75cg0BPw&_nc_ohc=t-DCVZxwtX4Q7kNvwE_tgwh&_nc_gid=bO8DwAhwAuglGlGOn_TBwg&edm=ADuq63kBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af0lPDiZuMNfvlhRJI2FzEJoc291JpI2JBvGWxE8aCvOAg&oe=69DC6746&_nc_sid=cebafd",
        "search_serp_type": 3,
        "search_social_context": "45.5M followers",
        "search_social_context_facepiles": null,
        "search_social_context_snippet_type": "typeahead_follow_count",
        "shopping_search_subtitle": null,
        "should_show_category": true,
        "show_ig_app_switcher_badge": null,
        "search_secondary_subtitle": null,
        "show_ring_award": false,
        "show_text_post_app_badge": false,
        "social_context": "45.5M followers",
        "third_party_downloads_enabled": 2,
        "unseen_count": 0,
        "username": "natgeotravel"
      },
      "extensions": {
        "is_final": false
      }
    }
  ]
}
```

</details>

---

### GET /gql/user/by/id

Get user object by id. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/by/id?id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/by/id",
        headers=headers,
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/by/id?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /gql/user/by/username

Get user object by username. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/by/username?username=natgeo"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/by/username",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /gql/user/clips

Get user clips. Returns a list of Media objects (Reels).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `max_id` | string | No | Max Id |
| `sort_by_views` | boolean | No | Sort By Views |
| `flat` | boolean | No | Flatten nested media objects into a single list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/clips?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_clips_gql(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/clips",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/clips?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "data": {
        "__typename": "Query",
        "strong_id__": null,
        "1$xdt_user_clips_graphql(data:$data)": {
          "is_fulfilled__(name:\"XDTGraphqlUserClipsResponse\")": true,
          "first_seen_media_id": null,
          "just_watched_context": null,
          "items": [
            {
              "media": {
                "__typename": "XDTMediaDict",
                "strong_id__": "3870025531093850440_1029649300",
                "id": "3870025531093850440_1029649300",
                "is_fulfilled__(name:\"XDTMediaDict\")": true,
                "clips_tab_pinned_user_ids": [],
                "clips_trial": null,
                "enable_media_notes_production": true,
                "inventory_source": null,
                "media_notes": {
                  "items": []
                },
                "floating_context_items": [],
                "media_overlay_info": null,
                "wearable_attribution_info": null,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwEmECzg&_nc_oc=AdokzfCkogyY8j2epV-cNfnzRpPq7WzY6Qsz16M4HPp04MM5Sil4h8q2PJV-zq_lRIY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2mhNXJdznrnhhTpTDuzLRVWEyvW0JYYsy6XSgZ0LDRtA&oe=69DC32B4",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "width": 640,
                      "height": 1136,
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwEmECzg&_nc_oc=AdokzfCkogyY8j2epV-cNfnzRpPq7WzY6Qsz16M4HPp04MM5Sil4h8q2PJV-zq_lRIY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2mhNXJdznrnhhTpTDuzLRVWEyvW0JYYsy6XSgZ0LDRtA&oe=69DC32B4",
                      "scans_profile": "e15"
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwFIH6Uh&_nc_oc=AdoKhZBJt2rIgvN5poxFXlCaCI8OpKe8P6dozc8iWJ_H1dVX_WftFJXBHtbxdxXIzNo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2VvO3aWd2-3XJtsADaCdSkMg2ynlkPgOvJ0R_-zGjvCg&oe=69DC46E1",
                      "width": 750
                    }
                  ],
                  "smart_thumbnail_enabled": null,
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "1fvideo_length": 60.727,
                      "thumbnail_width": 100,
                      "thumbnail_height": 176,
                      "1fthumbnail_duration": 0.578352380952381,
                      "sprite_urls": [
                        "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/661377490_4446710915609804_6368747692439450584_n.jpg?_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHNreaOpnkZRpaxsBjCnIw6B_vjUdqSJQmOO9BFCkTeTf1BuvDrjWrrm8YtvsWvdgY&_nc_ohc=8YQN_m5Qfl0Q7kNvwHvvuAi&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&edm=AL8dhF4BAAAA&ccb=7-5&oh=00_Af0ympUUQ19X5NbQ4SLi0O4UtMYX5ymQnGZCfscrUWlXFg&oe=69DC46C6&_nc_sid=dc74e4"
                      ],
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "max_thumbnails_per_sprite": 105,
                      "sprite_width": 1500,
                      "sprite_height": 1232,
                      "rendered_width": 96,
                      "file_size_kb": 271
                    }
                  }
                },
                "media_type": 2,
                "original_height": 1920,
                "original_width": 1080,
                "pk": "3870025531093850440",
                "play_count": 2594494,
                "product_type": "clips",
                "video_versions": [
                  {
                    "height": 1280,
                    "id": "4284559321859069v",
                    "type": 101,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwEyjJf8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2O28Hy9elGVr78KAqEhYiW5u3mmQF0jCa-HxIBltwDXQ&oe=69D853EC",
                    "width": 720
                  },
                  {
                    "height": 1280,
                    "id": "4284559321859069v",
                    "type": 102,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwEyjJf8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2O28Hy9elGVr78KAqEhYiW5u3mmQF0jCa-HxIBltwDXQ&oe=69D853EC",
                    "width": 720
                  },
                  {
                    "height": 1280,
                    "id": "4284559321859069v",
                    "type": 103,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwEyjJf8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2O28Hy9elGVr78KAqEhYiW5u3mmQF0jCa-HxIBltwDXQ&oe=69D853EC",
                    "width": 720
                  }
                ],
                "1fvideo_duration": 60.736000061035156,
                "meta_ai_content_deep_dive_prompt_v2": null,
                "meta_ai_contextual_voice_data": null,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "mv_link": null,
                "shimmed_mv_link": null
              }
            },
            {
              "media": {
                "__typename": "XDTMediaDict",
                "strong_id__": "3869494020385423326_787132",
                "id": "3869494020385423326_787132",
                "is_fulfilled__(name:\"XDTMediaDict\")": true,
                "clips_tab_pinned_user_ids": [],
                "clips_trial": null,
                "enable_media_notes_production": true,
                "inventory_source": null,
                "media_notes": {
                  "items": []
                },
                "floating_context_items": [],
                "media_overlay_info": null,
                "wearable_attribution_info": null,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/660753805_3353876781448969_8134495688569455809_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=JQlfi0W3VikQ7kNvwHPN-EE&_nc_oc=AdodGyvpBFU9IyHG45nSQ-0daz_pHjlibSNU7n-lRe4-0Fh74MKu2165YUGeQNiE-1M&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af09vTRdhv5yMt8V3UBJYPOJZ4N2hAn_hQipGa121XOYvQ&oe=69DC690C",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "width": 640,
                      "height": 1136,
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/660753805_3353876781448969_8134495688569455809_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=JQlfi0W3VikQ7kNvwHPN-EE&_nc_oc=AdodGyvpBFU9IyHG45nSQ-0daz_pHjlibSNU7n-lRe4-0Fh74MKu2165YUGeQNiE-1M&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af09vTRdhv5yMt8V3UBJYPOJZ4N2hAn_hQipGa121XOYvQ&oe=69DC690C",
                      "scans_profile": "e15"
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwHXCalP&_nc_oc=AdpbwOiDd2vFDfJ67mYkjdPOt2jK-mqNBozu-Tgqm5ryS-HwQbu9XIXR3F89txNxM9U&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af37Sf2dukNgo7FatsrHDr1Y3W-ByE11WNOwWf0orwahaQ&oe=69DC6315",
                      "width": 750
                    }
                  ],
                  "smart_thumbnail_enabled": null,
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "1fvideo_length": 55.43,
                      "thumbnail_width": 100,
                      "thumbnail_height": 176,
                      "1fthumbnail_duration": 0.5279047619047619,
                      "sprite_urls": [
                        "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/660026027_948875084508987_6617144121092333726_n.jpg?_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHNreaOpnkZRpaxsBjCnIw6B_vjUdqSJQmOO9BFCkTeTf1BuvDrjWrrm8YtvsWvdgY&_nc_ohc=a82HNH3lYl8Q7kNvwHEEA7Y&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&edm=AL8dhF4BAAAA&ccb=7-5&oh=00_Af1l6WQ5o2MkegHqL6yFZ3ay1i7vtMvxtvdltWdBP9fscA&oe=69DC36E4&_nc_sid=dc74e4"
                      ],
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "max_thumbnails_per_sprite": 105,
                      "sprite_width": 1500,
                      "sprite_height": 1232,
                      "rendered_width": 96,
                      "file_size_kb": 276
                    }
                  }
                },
                "media_type": 2,
                "original_height": 1920,
                "original_width": 1080,
                "pk": "3869494020385423326",
                "play_count": 1489070,
                "product_type": "clips",
                "video_versions": [
                  {
                    "height": 1280,
                    "id": "2358585431274531v",
                    "type": 101,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwGlTIAa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1yvS9mpEWB3riJT_GhXtHmBWM6soPw4W_p3mozkb86EQ&oe=69D86DB8",
                    "width": 720
                  },
                  {
                    "height": 1280,
                    "id": "2358585431274531v",
                    "type": 102,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwGlTIAa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1yvS9mpEWB3riJT_GhXtHmBWM6soPw4W_p3mozkb86EQ&oe=69D86DB8",
                    "width": 720
                  },
                  {
                    "height": 1280,
                    "id": "2358585431274531v",
                    "type": 103,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwGlTIAa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1yvS9mpEWB3riJT_GhXtHmBWM6soPw4W_p3mozkb86EQ&oe=69D86DB8",
                    "width": 720
                  }
                ],
                "1fvideo_duration": 55.44499969482422,
                "meta_ai_content_deep_dive_prompt_v2": null,
                "meta_ai_contextual_voice_data": null,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "mv_link": null,
                "shimmed_mv_link": null
              }
            },
            {
              "media": {
                "__typename": "XDTMediaDict",
                "strong_id__": "3868170261056492782_787132",
                "id": "3868170261056492782_787132",
                "is_fulfilled__(name:\"XDTMediaDict\")": true,
                "clips_tab_pinned_user_ids": [],
                "clips_trial": null,
                "enable_media_notes_production": true,
                "inventory_source": null,
                "media_notes": {
                  "items": []
                },
                "floating_context_items": [],
                "media_overlay_info": null,
                "wearable_attribution_info": null,
                "image_versions2": {
                  "additional_candidates": {
                    "first_frame": {
                      "height": 1136,
                      "scans_profile": "e15",
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/657963327_1140027124922753_6637085815743529745_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bkThNCUVUwUQ7kNvwGI2lul&_nc_oc=AdoNOK5j6_Uwz2tJ1831dnpTADs1a_wu7N9msn4dEEK4CndslivNAG9O6NbJJl2r1SE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2pb9I5WAcEoUPlY8ajAgJR71dnAEgPrKR-5bvQIrs5DA&oe=69DC345D",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "width": 640,
                      "height": 1136,
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/657963327_1140027124922753_6637085815743529745_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bkThNCUVUwUQ7kNvwGI2lul&_nc_oc=AdoNOK5j6_Uwz2tJ1831dnpTADs1a_wu7N9msn4dEEK4CndslivNAG9O6NbJJl2r1SE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2pb9I5WAcEoUPlY8ajAgJR71dnAEgPrKR-5bvQIrs5DA&oe=69DC345D",
                      "scans_profile": "e15"
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwF6tXet&_nc_oc=Adpt8RgFOqKiPR639g1yrdG-fjYFk8MBdFyhfitO8kW309UseUoT8ETlq8pa_UtNARs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af1wDLVYGUiBDV6CZ2Nywk8JsSRor5CB8OSRFgUB0m1rDQ&oe=69DC4951",
                      "width": 750
                    }
                  ],
                  "smart_thumbnail_enabled": null,
                  "scrubber_spritesheet_info_candidates": {
                    "default": {
                      "1fvideo_length": 47.881,
                      "thumbnail_width": 100,
                      "thumbnail_height": 176,
                      "1fthumbnail_duration": 0.4560095238095238,
                      "sprite_urls": [
                        "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/661407041_2382063302308753_1177647765954686603_n.jpg?_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gHNreaOpnkZRpaxsBjCnIw6B_vjUdqSJQmOO9BFCkTeTf1BuvDrjWrrm8YtvsWvdgY&_nc_ohc=n5iQezOC2T8Q7kNvwEJMdXQ&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&edm=AL8dhF4BAAAA&ccb=7-5&oh=00_Af0I6RB5MH2H2QTJOJHZHtd4s15fbuMZbOIoK3uJt_C4mA&oe=69DC5D1E&_nc_sid=dc74e4"
                      ],
                      "thumbnails_per_row": 15,
                      "total_thumbnail_num_per_sprite": 105,
                      "max_thumbnails_per_sprite": 105,
                      "sprite_width": 1500,
                      "sprite_height": 1232,
                      "rendered_width": 96,
                      "file_size_kb": 274
                    }
                  }
                },
                "media_type": 2,
                "original_height": 1920,
                "original_width": 1080,
                "pk": "3868170261056492782",
                "play_count": 1304842,
                "product_type": "clips",
                "video_versions": [
                  {
                    "height": 1280,
                    "id": "799234956583164v",
                    "type": 101,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwGEWBFt&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2gQuDW1fcpuZ0YuUMceTQfwaJ4FoMGyd2epVt8bUGm0g&oe=69D87233",
                    "width": 720
                  },
                  {
                    "height": 1280,
                    "id": "799234956583164v",
                    "type": 102,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwGEWBFt&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2gQuDW1fcpuZ0YuUMceTQfwaJ4FoMGyd2epVt8bUGm0g&oe=69D87233",
                    "width": 720
                  },
                  {
                    "height": 1280,
                    "id": "799234956583164v",
                    "type": 103,
                    "url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwGEWBFt&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2gQuDW1fcpuZ0YuUMceTQfwaJ4FoMGyd2epVt8bUGm0g&oe=69D87233",
                    "width": 720
                  }
                ],
                "1fvideo_duration": 47.893001556396484,
                "meta_ai_content_deep_dive_prompt_v2": null,
                "meta_ai_contextual_voice_data": null,
                "crosspost_metadata": {
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  }
                },
                "mv_link": null,
                "shimmed_mv_link": null
              }
            }
          ]
        }
      },
      "extensions": {
        "is_final": false,
        "server_metadata": {
          "request_start_time_ms": 1775663939687,
          "time_at_flush_ms": 1775663939965
        }
      },
      "status": "ok"
    },
    {
      "path": [
        "1$xdt_user_clips_graphql(data:$data)"
      ],
      "label": "ClipsProfilePagingInfo__force_flush",
      "data": {
        "is_fulfilled__(name:\"XDTGraphqlUserClipsResponse\")": true,
        "paging_info": {
          "max_id": "QVFDd1lvX0ZEZVpUX3k0QjFETG1rWjRleUtTcVhTczRuMmJ2N214TE5KSkJmRmRvSnNwVkppVE5VT1pxV2lvcEg3dm5YRnpHXzB6SURabUVQTEdMTkZMSw==",
          "more_available": true
        }
      },
      "extensions": {
        "is_final": false
      }
    },
    {
      "path": [
        "1$xdt_user_clips_graphql(data:$data)",
        "items",
        0
      ],
      "label": "ClipsViewerGraphQLFragment",
      "data": {
        "__typename": "XDTMediaDict",
        "strong_id__": "3870025531093850440_1029649300",
        "id": "3870025531093850440_1029649300",
        "is_fulfilled__(name:\"XDTMediaDict\")": true,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "wearable_attribution_info": null,
        "are_remixes_crosspostable": true,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "creator_viewer_insights": null,
        "attribution": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_by_sponsor": null,
        "boosted_post_id": null,
        "boosted_status": null,
        "branded_content_ads_boost_post_tokens": null,
        "can_see_insights_as_brand": false,
        "can_view_more_preview_comments": false,
        "can_viewer_reshare": true,
        "can_viewer_save": true,
        "caption": {
          "__typename": "XDTCommentDict",
          "strong_id__": "18064245098343903",
          "pk": "18064245098343903",
          "bit_flags": 0,
          "content_type": "comment",
          "1lcreated_at": 1775566807,
          "1lcreated_at_utc": 1775566807,
          "did_report_as_spam": false,
          "fb_mentioned_users": null,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": "3870025531093850440",
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
          "text_translation": null,
          "type": 1,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "1029649300",
            "id": "1029649300",
            "is_fulfilled__(name:\"XDTUserDict\")": true,
            "pk": "1029649300",
            "username": "natgeoanimals",
            "full_name": "National Geographic Animals",
            "is_private": false,
            "1fcoeff_weight": null,
            "social_context": null,
            "is_active": null,
            "is_verified": true,
            "profile_pic_id": "3865698702530758137_1029649300",
            "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGWZJnBqxzAw-VoEwc-r8vEw26LLeMwQilK1IsA8cD2n8OApSoH9exdMRVEOK-X1AI&_nc_ohc=ic5ODsLE2O8Q7kNvwFqd1oM&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&edm=AL8dhF4BAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af3gTZzkBgFDaWSLGqD1FrLDeGWvHgU8ZcoUOYzBzKlCzg&oe=69DC588C&_nc_sid=dc74e4",
            "has_onboarded_to_text_post_app": null,
            "follower_count": 15107708,
            "fbid_v2": "17841400519016088"
          },
          "user_id": "1029649300"
        },
        "caption_is_edited": false,
        "client_cache_key": "Mzg3MDAyNTUzMTA5Mzg1MDQ0MA==.3",
        "clips_attribution_info": null,
        "clips_metadata": {
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
          "branded_content_tag_info": {
            "can_add_tag": false
          },
          "clips_creation_entry_point": "",
          "content_appreciation_info": null,
          "contextual_highlight_info": null,
          "disable_use_in_clips_client_cache": false,
          "is_fan_club_promo_video": false,
          "is_public_chat_welcome_video": false,
          "is_shared_to_fb": false,
          "mashup_info": {
            "can_toggle_mashups_allowed": false,
            "has_been_mashed_up": false,
            "has_nonmimicable_additional_audio": false,
            "is_creator_requesting_mashup": false,
            "is_light_weight_check": true,
            "is_pivot_page_available": false,
            "mashup_type": null,
            "mashups_allowed": false,
            "non_privacy_filtered_mashups_media_count": 0,
            "original_media": null
          },
          "merchandising_pill_info": null,
          "music_canonical_id": "18548020762066838",
          "music_info": null,
          "originality_info": null,
          "original_sound_info": {
            "allow_creator_to_rename": true,
            "audio_asset_id": "26338877092460506",
            "audio_filter_infos": null,
            "audio_parts": [],
            "audio_parts_by_filter": [],
            "can_remix_be_shared_to_fb": true,
            "consumption_info": {
              "is_bookmarked": false,
              "is_trending_in_clips": false,
              "should_mute_audio_reason": ""
            },
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663940\" FBManifestIdentifier=\"Fojts50NKRbMrPbB5Z2pBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1498046678354726a\" bandwidth=\"66810\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66810\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m78/AQOElke-XjvO2ixFipAMNby9AqC5CZmOcY8PcbQDmAwEGdrdvbD58TPi5A5RKS7WbXpTrVlZQip3DhNxjBI2vRela2S063MA11oc5y0.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=XLhOSrzrzoUQ7kNvwH4dC1t&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1Et_ld4MXyvc6N8LIgFWuUPpzvcqRGn6YvtCFp3U_BcA&amp;oe=69D8589E</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "duration_in_ms": 60727,
            "hide_remixing": false,
            "ig_artist": {
              "__typename": "XDTUserDict",
              "strong_id__": "1029649300",
              "id": "1029649300",
              "full_name": "National Geographic Animals",
              "has_onboarded_to_text_post_app": null,
              "is_private": false,
              "is_verified": true,
              "pk": "1029649300",
              "profile_pic_id": "3865698702530758137_1029649300",
              "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGWZJnBqxzAw-VoEwc-r8vEw26LLeMwQilK1IsA8cD2n8OApSoH9exdMRVEOK-X1AI&_nc_ohc=ic5ODsLE2O8Q7kNvwFqd1oM&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&edm=AL8dhF4BAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af3gTZzkBgFDaWSLGqD1FrLDeGWvHgU8ZcoUOYzBzKlCzg&oe=69DC588C&_nc_sid=dc74e4",
              "username": "natgeoanimals"
            },
            "is_audio_automatically_attributed": false,
            "is_explicit": false,
            "is_original_audio_download_eligible": false,
            "is_reuse_disabled": false,
            "is_xpost_from_fb": false,
            "original_audio_subtype": "default",
            "original_audio_title": "Original audio",
            "original_media_id": "3870025531093850440",
            "progressive_download_url": "https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m69/AQPYF2mAhRbYzYMrI560MWB9XBJqAACyr7szcVbj1WFwaneaOm5BlFHWUM37z1AaOh6Oyo4BIq6T2yeHyTeibfXn.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_ohc=wTkgipWqtN0Q7kNvwHjN4Uu&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2h6f7vjgBbRgYQlWn66LVb5JFC2WMZQfMuX5kz1yMSkg&oe=69DC5663",
            "should_mute_audio": false,
            "time_created": 1775566809,
            "trend_rank": null
          },
          "professional_clips_upsell_type": 0,
          "reusable_text_attribute_string": null,
          "shopping_info": null,
          "show_achievements": false,
          "show_tips": null,
          "template_info": null
        },
        "clips_tab_pinned_user_ids": [],
        "clips_trial": null,
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [
          {
            "__typename": "XDTUserDict",
            "strong_id__": "787132",
            "id": "787132",
            "full_name": "National Geographic",
            "has_onboarded_to_text_post_app": null,
            "is_private": false,
            "is_verified": true,
            "pk": "787132",
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGWZJnBqxzAw-VoEwc-r8vEw26LLeMwQilK1IsA8cD2n8OApSoH9exdMRVEOK-X1AI&_nc_ohc=XbeNvhLXv28Q7kNvwFh10Oy&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&edm=AL8dhF4BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3poq7B2wD4bOxDOgxllOJwxraGHA2XYs_e1oaLFAjQTg&oe=69DC51E9&_nc_sid=dc74e4",
            "username": "natgeo"
          }
        ],
        "code": "DW1F7dciplI",
        "comment_count": 493,
        "comment_inform_treatment": {
          "should_have_inform_treatment": false,
          "text": ""
        },
        "comment_likes_enabled": true,
        "comment_threading_enabled": true,
        "commenting_disabled_for_viewer": null,
        "comments_disabled": null,
        "commerciality_status": "not_commercial",
        "creative_config": null,
        "deleted_reason": 0,
        "1ldevice_timestamp": 177556301582,
        "dominant_color": null,
        "enable_media_notes_production": true,
        "inventory_source": null,
        "media_notes": {
          "items": []
        },
        "enable_waist": true,
        "explore_hide_comments": null,
        "facepile_top_likers": null,
        "fb_like_count": null,
        "fb_play_count": null,
        "filter_type": 0,
        "fundraiser_tag": {
          "beneficiary_name": null,
          "beneficiary_username": null,
          "can_viewer_donate": null,
          "can_viewer_remove_fundraiser_tag": null,
          "contextual_title_str": null,
          "formatted_amount_raised": null,
          "formatted_fundraiser_progress_info_text": null,
          "formatted_goal_amount": null,
          "fundraiser_id": null,
          "fundraiser_owner_username": null,
          "fundraiser_title": null,
          "fundraiser_type": null,
          "is_media_owner_fundraiser_owner": null,
          "progress_str": null,
          "show_fundraiser_owner_attribution": null,
          "thumbnail_display_url": null
        },
        "has_audio": true,
        "has_delayed_metadata": false,
        "has_hidden_comments": null,
        "has_liked": false,
        "has_more_comments": true,
        "has_reshares": null,
        "has_shared_to_fb": 0,
        "has_viewer_saved": null,
        "has_views_fetching": true,
        "hide_view_all_comment_entrypoint": true,
        "ig_media_sharing_disabled": false,
        "igtv_exists_in_viewer_series": null,
        "igtv_series_info": null,
        "igtv_shopping_info": null,
        "image_versions2": {
          "additional_candidates": {
            "first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwEmECzg&_nc_oc=AdokzfCkogyY8j2epV-cNfnzRpPq7WzY6Qsz16M4HPp04MM5Sil4h8q2PJV-zq_lRIY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2mhNXJdznrnhhTpTDuzLRVWEyvW0JYYsy6XSgZ0LDRtA&oe=69DC32B4",
              "width": 640
            },
            "igtv_first_frame": {
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwEmECzg&_nc_oc=AdokzfCkogyY8j2epV-cNfnzRpPq7WzY6Qsz16M4HPp04MM5Sil4h8q2PJV-zq_lRIY&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2mhNXJdznrnhhTpTDuzLRVWEyvW0JYYsy6XSgZ0LDRtA&oe=69DC32B4",
              "width": 640
            }
          },
          "candidates": [
            {
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwFIH6Uh&_nc_oc=AdoKhZBJt2rIgvN5poxFXlCaCI8OpKe8P6dozc8iWJ_H1dVX_WftFJXBHtbxdxXIzNo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&_nc_ss=7a3ba&oh=00_Af2VvO3aWd2-3XJtsADaCdSkMg2ynlkPgOvJ0R_-zGjvCg&oe=69DC46E1",
              "width": 750
            }
          ],
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "file_size_kb": 271,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_width": 1500,
              "1fthumbnail_duration": 0.578352381,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "1fvideo_length": 60.727
            }
          },
          "smart_thumbnail_enabled": null
        },
        "integrity_review_decision": "pending",
        "invited_coauthor_producers": [],
        "is_artist_pick": false,
        "is_comments_gif_composer_enabled": false,
        "is_currently_promoting_by_sponsor": null,
        "is_dash_eligible": 1,
        "is_fb_only": null,
        "is_in_profile_grid": false,
        "is_internal_only": null,
        "is_organic_product_tagging_eligible": true,
        "is_paid_partnership": false,
        "is_post_live": null,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_shared_from_basel": null,
        "is_third_party_downloads_eligible": false,
        "is_unified_video": false,
        "is_visual_reply_commenter_notice_enabled": true,
        "1flat": null,
        "like_and_view_counts_disabled": false,
        "share_count_disabled": false,
        "like_count": 50461,
        "1flng": null,
        "location": null,
        "logging_info_token": null,
        "mashup_info": null,
        "max_num_visible_preview_comments": 2,
        "media_appreciation_settings": null,
        "media_cropping_info": null,
        "media_notice": null,
        "media_overlay_info": null,
        "media_type": 2,
        "media_attributions_data": [],
        "music_metadata": null,
        "nearly_complete_copyright_match": null,
        "next_max_id": null,
        "number_of_qualities": 8,
        "organic_cta_info": null,
        "organic_cta_type": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiM2NlZWJiNmMyY2JiNDMxZDliYzA0MzA1NWU4MTBiNjUzODcwMDI1NTMxMDkzODUwNDQwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkzOTk4MXwzODcwMDI1NTMxMDkzODUwNDQwfDM4ODMwOTQ1NjIxfDVlOTAwMmVlOWJhOWUzMWM0ZGY1ZWZmMzMzZTU5ZDc4YzkzNGU5NjJmYjM4MDgyYTRmODY0Mzk5MDQ5YmMzMDgifSwic2lnbmF0dXJlIjoiIn0=",
        "original_height": 1920,
        "original_media_has_visual_reply_media": false,
        "original_width": 1080,
        "photo_of_you": false,
        "play_count": 2594494,
        "preview": null,
        "product_tags": null,
        "profile_grid_control_enabled": false,
        "reshare_count": 11453,
        "senders": [],
        "sharing_friction_info": {
          "should_have_sharing_friction": false
        },
        "shop_routing_user_id": null,
        "should_request_ads": false,
        "floating_context_items": [],
        "social_context": [],
        "sponsor_tags": null,
        "story_notify_me_stickers": null,
        "story_polls": null,
        "story_prompts": null,
        "story_sliders": null,
        "subscribe_cta_visible": false,
        "subscription_media_visibility": null,
        "1ltaken_at": 1775566804,
        "thumbnails": null,
        "title": null,
        "upcoming_event": null,
        "user": {
          "__typename": "XDTUserDict",
          "strong_id__": "1029649300",
          "id": "1029649300",
          "is_fulfilled__(name:\"XDTUserDict\")": true,
          "pk": "1029649300",
          "username": "natgeoanimals",
          "full_name": "National Geographic Animals",
          "is_private": false,
          "1fcoeff_weight": null,
          "social_context": null,
          "is_active": null,
          "is_verified": true,
          "profile_pic_id": "3865698702530758137_1029649300",
          "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGWZJnBqxzAw-VoEwc-r8vEw26LLeMwQilK1IsA8cD2n8OApSoH9exdMRVEOK-X1AI&_nc_ohc=ic5ODsLE2O8Q7kNvwFqd1oM&_nc_gid=7kIe2z2Kx_C021HqNx39yQ&edm=AL8dhF4BAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af3gTZzkBgFDaWSLGqD1FrLDeGWvHgU8ZcoUOYzBzKlCzg&oe=69DC588C&_nc_sid=dc74e4",
          "has_onboarded_to_text_post_app": null,
          "follower_count": 15107708,
          "fbid_v2": "17841400519016088"
        },
        "usertags": null,
        "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663939\" FBManifestIdentifier=\"Fobts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxs71ud+73IoDiqC0wu3LjwPImKTi/7u7BL6Zk9OwssAE/t+w5JmOxQSSmNLH6cjSBerci73BkuQFmJ6qw8jLyAaQj4fa8c2pB8T5kOjGrLcHhqCP7Nm3vAeqnN3Z9IWhDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.1\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"868003729587559v\" bandwidth=\"178266\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1353206\" FBPlaybackResolutionMos=\"0:100,360:56.7,480:54.4,720:53.2,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.1,720:83.8,1080:76.2\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQOsCsgfDrcn7Gsyqj04T425mPWmeq8-MeX07h5wqKf_ykgUXeoigrvG2JQeRp4Wd_MdM-ZLa9ORl60gPpY3e_JZiFGCQ5EL6KkXMnk.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=Uh48tAtlw1sQ7kNvwHFw7CH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTc4MjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3C7Llm3mNofEdifdzWoNxigmi6nvlL_u6wDE3R483fLQ&amp;oe=69DC51D7</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10892\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-78531\" FBFirstSegmentRange=\"1014-106281\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106282-221200\" FBPrefetchSegmentRange=\"1014-106281\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2092036534705762v\" bandwidth=\"240856\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1828322\" FBPlaybackResolutionMos=\"0:100,360:63.6,480:60.6,720:58.1,1080:58.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95,480:93.1,720:88.4,1080:81.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQPRuSajZ_hFnjDpVSn1TY6XCtP7Zo9QzDsXmaKDU4mXL33dQv9cZzKhXl7Y_oeRcW9BNsObRl_FpdyfkSlu8ArGYU5-l43-uxy7_sg.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=-0z8YeyvyDgQ7kNvwGO5DmJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjQwODU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2BQpzEQ9Xn1AcBk5fA6iLASP822bUgvkMpqbQJHUi9Sg&amp;oe=69DC6448</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-12646\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-105375\" FBFirstSegmentRange=\"1014-143432\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"143433-293318\" FBPrefetchSegmentRange=\"1014-143432\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1267502918297183v\" bandwidth=\"326220\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2476312\" FBPlaybackResolutionMos=\"0:100,360:69,480:66,720:63.5,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.4,480:95.3,720:93.4,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBZheSdr-Op1k9B7pYwuciRaL5RCC2XcBVLkVwDPXAKrAhlrALgBooKgZk6nCMZz5AvNoGknQE18-kCW9-RNH_qVgCyawe5etIWbE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=4ClMe01ofx0Q7kNvwFtPK3q&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzI2MjIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0PRgccBXxLscFzlu1E7KYiNqf9QmHScMbCzkm4F5imaA&amp;oe=69DC57D8</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-15483\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-142126\" FBFirstSegmentRange=\"1014-195190\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"195191-393663\" FBPrefetchSegmentRange=\"1014-195190\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1277876490344447v\" bandwidth=\"409602\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3109259\" FBPlaybackResolutionMos=\"0:100,360:73,480:69.8,720:67,1080:65.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.7,720:95.4,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxkQrl5cFyNncjOUGRq3XWMGmEnR7xzXjtdkfQlw0oreW4eSXmKA9eBGchHF9ByGL1ldZ-V_-LDFLMXxx4oytbIqVxuBwnRf-_tR0.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=5YrnOUUJMr4Q7kNvwFsB4PV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDA5NjAyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af15gFnL1InRd2z4pCmW3wxF-Rli3NaelCXwPwJ4LExy5w&amp;oe=69DC3457</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16985\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-176185\" FBFirstSegmentRange=\"1014-244141\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"244142-487399\" FBPrefetchSegmentRange=\"1014-244141\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1848477759129484v\" bandwidth=\"540603\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4103680\" FBPlaybackResolutionMos=\"0:100,360:77,480:74,720:70.7,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.24,480:98,720:97.4,1080:93.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQP2bW0aIfz99a4ARx2Q2fPwwUvSZlmUT1jxqzlfSPxqDy_XKQdY1A9deJRHs78I9y2z_ngWT2zfhDIKZ8-XZxBrQWFF9SDm2muWNnE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=M35pMpEQ64sQ7kNvwFs-8__&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NTQwNjAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2U5mVO-PmDo9dwOSqkm2y5UnIYI0EZuYSrGXB_BbQ9PQ&amp;oe=69DC4906</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-18644\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-229855\" FBFirstSegmentRange=\"1014-321368\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"321369-630140\" FBPrefetchSegmentRange=\"1014-321368\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1588945909073417v\" bandwidth=\"681362\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"5172172\" FBPlaybackResolutionMos=\"0:100,360:80.4,480:76.6,720:73.2,1080:70.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.62,480:98.37,720:98.59,1080:95.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQPuKZF2qKICjs08-k_G1H8gucF1aCSpWB6stiwUGXWNvKfX5Hm_pNaY4z6GYTR0ZmsxXCYFw3SGDP8cejuR9yWwzxdzv-J159SieXo.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=jd4D7ZlmtxMQ7kNvwEiuTY_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjgxMzYyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af12PmXStC6iL1Ct4D7TxCPLTvVDgDmhYplFuh168VqCDw&amp;oe=69DC4007</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-20592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-288895\" FBFirstSegmentRange=\"1014-405533\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"405534-781198\" FBPrefetchSegmentRange=\"1014-405533\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2061822901412808v\" bandwidth=\"912497\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6926702\" FBPlaybackResolutionMos=\"0:100,360:83.9,480:79.9,720:75.7,1080:72.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.077,480:98.93,720:99.306,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQOjiwsO48rCaOF6m6s4bgg66iRhLGj5CKjR4DDmQ8T9kE2SvEWALkKtR50Wk2wGAMLc1Ws3pNhZSA9Y-QIiggu_wdfx_Bl0gwfgXDQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=fEsXwzzt-3AQ7kNvwExym3Q&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6OTEyNDk3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1JkxZRdD2Sw54H5roJDDNHKYZ-p8H2Q_zXHuPbktoLuQ&amp;oe=69DC387A</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-23580\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-385865\" FBFirstSegmentRange=\"1014-544870\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"544871-1019514\" FBPrefetchSegmentRange=\"1014-544870\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1627595234965301v\" bandwidth=\"1235000\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"9374797\" FBPlaybackResolutionMos=\"0:100,360:86.4,480:82.8,720:77.8,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.386,480:99.342,720:99.569,1080:99.632\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQM_p3Fq6rDYprSjJ8-MUlNGuff4JfkbCcT-LYH34W9o85XM1tWSkDeCFiP_sdVayBjAG_vXE0vYkHj0noxXvuN1eESyaLJtPOQ3Rmg.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=YK0MlTWtfdIQ7kNvwHiXObC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTIzNTAwMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3Z0fRw0YHh1x3ORiZqjBEWTe7OKRw0gWbWnP-DIbi5dg&amp;oe=69DC4156</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-32211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-518374\" FBFirstSegmentRange=\"1014-739833\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"739834-1405190\" FBPrefetchSegmentRange=\"1014-739833\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4294793980782357a\" bandwidth=\"46380\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46380\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"353137\" FBPaqMos=\"87.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9GI-VauacxM2tCfwmiCOijhyH33zBWrM0Dr4JwD6i2FjABcTvvBGOXIydEyGVXVx6wkUjNuDAtapI93ufxCNL1tRZuAP-HRtBv50.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=Uo8ixeKIRUsQ7kNvwFFxItE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjUxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3P1vbiYfWlpPFTpIeQSpQPRlX4qvtFq30XpyiFz_wjWQ&amp;oe=69DC60EA</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2136\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-14938\" FBFirstSegmentRange=\"1025-28400\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28401-56361\" FBPrefetchSegmentRange=\"1025-28400\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1256673039910436a\" bandwidth=\"74812\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74812\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"568992\" FBPaqMos=\"89.65\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQPA0IU4X5qD93OmmaSc1st7oueEaOmYwYCBhH3T3wOKN7WutkRMOZ1TDwC1ugFmlc5yKEeuM_xeo_vD4IzH2AbUDhA7xa2uuL_kti8.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=H10A9jvUydQQ7kNvwFFo9T1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NDk0NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af17AQAin4AJMkxL714xUI9TtCq_8nH8ap5CKEivWvXh_A&amp;oe=69DC6622</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21486\" FBFirstSegmentRange=\"1026-43481\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"43482-90615\" FBPrefetchSegmentRange=\"1026-43481\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"878713468520453a\" bandwidth=\"108352\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108352\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"823623\" FBPaqMos=\"83.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQOhb37d5jmr5MvSl8eT28PWBputzk-lecQ-RBUBedLEv96EozZbcoK_AR-dP3eFTj3ZDuOnoWe6DiibSbh3Vjc_rcGupQpI3Z2uCnA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=qIB9a-mC_CIQ7kNvwHabEpC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDg0ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3f09JPPBlnNj-s8PJR7fbV5BzKSlRhlKt_1GE_Vy6hdw&amp;oe=69DC55C7</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2395\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-30757\" FBFirstSegmentRange=\"1021-62738\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62739-132935\" FBPrefetchSegmentRange=\"1021-62738\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2103223183861763a\" bandwidth=\"143947\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"143947\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1093864\" FBPaqMos=\"87.00\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-xxb1-1.cdninstagram.com/o1/v/t2/f2/m367/AQOgH1TOj2U7Ucn9wQoBfkebTHLZ9A_EoIFXsEJ2CkC1MsQUoWoasexRt0uwJQMyHQr8MmjxA15OisXxvCobhDmp05SCyaFAKp2_vFI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-xxb1-1.cdninstagram.com&amp;_nc_ohc=Kg8UNuEeTkcQ7kNvwFf9lMf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxNDQwODEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=7kIe2z2Kx_C021HqNx39yQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3tFlS4aBWwBRBIdCEdgI2BnmbHnN15EpelGOXec9ETDg&amp;oe=69DC5327</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-45040\" FBFirstSegmentRange=\"1021-86500\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"86501-176000\" FBPrefetchSegmentRange=\"1021-86500\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "1fvideo_subtitles_confidence": null,
        "video_subtitles_enabled": null,
        "video_subtitles_status": null,
        "video_subtitles_uri": null,
        "video_subtitles_locale": null,
        "byoa_langs": null,
        "translated_video_subtitles": null,
        "video_sticker_locales": [],
        "sticker_translations_enabled": null,
        "clips_karaoke_caption": null,
        "clips_captions": null,
        "clips_captions_translations_urls": null,
        "clips_text": null,
        "view_count": null,
        "view_state_item_type": 128,
        "visual_comment_reply_sticker_info": null,
        "visual_replies_info": null,
        "xpost_deny_reason": null,
        "top_likers": []
      },
      "extensions": {
        "is_final": false
      }
    }
  ]
}
```

</details>

---

### GET /gql/user/followers

⚠️ Billing: 2 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/followers?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/followers",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/followers?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /gql/user/followers/chunk

⚠️ Billing: 2 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `force` | boolean | No | Skip account privacy check |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/followers/chunk?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_followers_chunk_gql(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/followers/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/followers/chunk?user_id=787132",
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
      "pk": "38603263886",
      "id": "38603263886",
      "username": "anilpatidar79113",
      "full_name": "",
      "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/660803108_18074699612287887_7133173336373565105_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NjAuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGQ1QWo_K1ytibpXSdxr2QfSXkN3Kyc1e-ljtHyWlo7FTBBsHe7dnxQFJ7TQ8km4e4&_nc_ohc=1umQirS--7AQ7kNvwHBwS0P&_nc_gid=JWCphkbhrKnYeM_tt3vSzg&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af0dPJGAMp0ZN0CEhLfI84w-nMCCrg_VOEuo9dvOd6b01w&oe=69DC59B3&_nc_sid=17ea04",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 38603263886,
        "expiring_at": 1775750336,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 38603263886,
          "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/660803108_18074699612287887_7133173336373565105_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NjAuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gGQ1QWo_K1ytibpXSdxr2QfSXkN3Kyc1e-ljtHyWlo7FTBBsHe7dnxQFJ7TQ8km4e4&_nc_ohc=1umQirS--7AQ7kNvwHBwS0P&_nc_gid=JWCphkbhrKnYeM_tt3vSzg&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af0dPJGAMp0ZN0CEhLfI84w-nMCCrg_VOEuo9dvOd6b01w&oe=69DC59B3&_nc_sid=17ea04",
          "username": "anilpatidar79113"
        }
      }
    },
    {
      "pk": "37856792876",
      "id": "37856792876",
      "username": "hisliburclar",
      "full_name": "",
      "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/662814813_18075676073256877_3334239291894936166_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGQ1QWo_K1ytibpXSdxr2QfSXkN3Kyc1e-ljtHyWlo7FTBBsHe7dnxQFJ7TQ8km4e4&_nc_ohc=Yxsd-DI8KeoQ7kNvwESUNc7&_nc_gid=JWCphkbhrKnYeM_tt3vSzg&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af0fnElbv4_G4zAYbMpacGNPtxxJw87ie5CMBsn3rOpO0A&oe=69DC60BE&_nc_sid=17ea04",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 37856792876,
        "expiring_at": 1775750336,
        "has_pride_media": false,
        "latest_reel_media": 1775662069,
        "owner": {
          "id": 37856792876,
          "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/662814813_18075676073256877_3334239291894936166_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gGQ1QWo_K1ytibpXSdxr2QfSXkN3Kyc1e-ljtHyWlo7FTBBsHe7dnxQFJ7TQ8km4e4&_nc_ohc=Yxsd-DI8KeoQ7kNvwESUNc7&_nc_gid=JWCphkbhrKnYeM_tt3vSzg&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af0fnElbv4_G4zAYbMpacGNPtxxJw87ie5CMBsn3rOpO0A&oe=69DC60BE&_nc_sid=17ea04",
          "username": "hisliburclar"
        }
      }
    },
    {
      "pk": "38352482095",
      "id": "38352482095",
      "username": "builderacademye",
      "full_name": "",
      "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/663236559_18075610952274096_6872836836684532981_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MTIuYzIifQ&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gGQ1QWo_K1ytibpXSdxr2QfSXkN3Kyc1e-ljtHyWlo7FTBBsHe7dnxQFJ7TQ8km4e4&_nc_ohc=V5Q4zNL0FbMQ7kNvwHDVC-o&_nc_gid=JWCphkbhrKnYeM_tt3vSzg&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af1sQrC4UBU0nOu9Gu_lyzYQqnKdt-ThIWOU1RS0calFOQ&oe=69DC4827&_nc_sid=17ea04",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 38352482095,
        "expiring_at": 1775750336,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 38352482095,
          "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/663236559_18075610952274096_6872836836684532981_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MTIuYzIifQ&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gGQ1QWo_K1ytibpXSdxr2QfSXkN3Kyc1e-ljtHyWlo7FTBBsHe7dnxQFJ7TQ8km4e4&_nc_ohc=V5Q4zNL0FbMQ7kNvwHDVC-o&_nc_gid=JWCphkbhrKnYeM_tt3vSzg&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af1sQrC4UBU0nOu9Gu_lyzYQqnKdt-ThIWOU1RS0calFOQ&oe=69DC4827&_nc_sid=17ea04",
          "username": "builderacademye"
        }
      }
    }
  ],
  "QVFDa05zOFp4a0tobzZVX1lrT1M0Z0lTcWtETnlEZWEtNkNWLWUwZUk3NGlWZ3RjTUd0S3JhR3B4Q09vS1E5ODF1REdLT0tZcy03RDNqdllMT1cyYVljNg=="
]
```

</details>

---

### GET /gql/user/following

⚠️ Billing: 2 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/following?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/following",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/following?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /gql/user/following/chunk

⚠️ Billing: 2 requests per call. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `force` | boolean | No | Skip account privacy check |
| `end_cursor` | string | No | End Cursor |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/following/chunk?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_following_chunk_gql(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/following/chunk",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/following/chunk?user_id=787132",
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
      "pk": "68012770661",
      "id": "68012770661",
      "username": "natgeofamily",
      "full_name": "National Geographic Family",
      "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/659123606_17925610677266662_299620373829898330_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHH953J3BugLUfZ9oUsMTYOxTw6XqGIBeInasbRnBTvLGxq81-pHK-1MgA5LhYugfY&_nc_ohc=1GP4i4FmPtQQ7kNvwHumtgo&_nc_gid=v5vcF24Pdotvd4v0UOX8Mg&edm=ANg5bX4BAAAA&ccb=7-5&oh=00_Af25S7fyMJKb2S6ALVgHbjdAE1J5Pwwwi_nLnB3wy8FNKw&oe=69DC5134&_nc_sid=0055be",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "20650647",
      "id": "20650647",
      "username": "russwest44",
      "full_name": "Russell Westbrook",
      "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.2885-19/309889627_1524999051276415_7968180555528416495_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MjMuYzIifQ&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHH953J3BugLUfZ9oUsMTYOxTw6XqGIBeInasbRnBTvLGxq81-pHK-1MgA5LhYugfY&_nc_ohc=7iK5Ff6oxt0Q7kNvwHBIQKR&_nc_gid=v5vcF24Pdotvd4v0UOX8Mg&edm=ANg5bX4BAAAA&ccb=7-5&oh=00_Af0PcLaeQVEEriddmIR61iMc6LraHMltRMsFpcnfhF01tQ&oe=69DC45F1&_nc_sid=0055be",
      "is_private": false,
      "is_verified": true
    },
    {
      "pk": "3956077735",
      "id": "3956077735",
      "username": "borgeousland",
      "full_name": "Børge Ousland",
      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.2885-19/18809286_1322467697802145_5393617671164002304_a.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gHH953J3BugLUfZ9oUsMTYOxTw6XqGIBeInasbRnBTvLGxq81-pHK-1MgA5LhYugfY&_nc_ohc=fiCJeO8zB6AQ7kNvwEUZCim&_nc_gid=v5vcF24Pdotvd4v0UOX8Mg&edm=ANg5bX4BAAAA&ccb=7-5&oh=00_Af1YWlc6k1N8lPJAwQ9-pfiYjgwNV6E03vBzVSC0Zxrnxg&oe=69DC4DB7&_nc_sid=0055be",
      "is_private": false,
      "is_verified": true
    }
  ],
  "QVFEelN2d1Ezd0tqVF9UcjlPa29yVlg5aTNlNFR0YjRDc3AwMTd6cXkwaWxWRjJFSk03MWF2UDRHaE1NelpEcDhsR0RfdllCSkVOT00xcGdKWlJkVFlPVw=="
]
```

</details>

---

### GET /gql/user/medias

Get user medias. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `profile_grid_items_cursor` | string | No | Profile Grid Items Cursor |
| `flat` | boolean | No | Flatten nested media objects into a single list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/medias?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_medias_gql(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/medias",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/medias?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "stream_rows": [
    {
      "data": {
        "__typename": "Query",
        "strong_id__": null,
        "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)": {
          "is_fulfilled__(name:\"XDTProfileFeedDict\")": true,
          "__typename": "XDTProfileFeedDict",
          "strong_id__": null,
          "is_fulfilled__(name:\"XDTHintableResponse\")": true,
          "client_hints": {
            "is_fulfilled__(name:\"XDTClientHints\")": true,
            "version": 4,
            "media": [
              {
                "is_fulfilled__(name:\"XDTMediaHint\")": true,
                "resources": [
                  {
                    "is_fulfilled__(name:\"XDTMediaResourceHint\")": true,
                    "image": {
                      "is_fulfilled__(name:\"XDTImageCandidate\")": true,
                      "width": 750,
                      "height": 1333,
                      "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwH4PITn&_nc_oc=Adqyoq6kwCfX-m7IqPTbQttt70XnhGFdeRlmsDNiGBhXkw02d4OE_j7Ov0XDHy1-nm4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af0jyAc1nHvg6-8lZ1_4XKE5cAHZbT0ehcH91rNPWw68Zg&oe=69DC65F1",
                      "scans_profile": "e35"
                    }
                  }
                ]
              },
              {
                "is_fulfilled__(name:\"XDTMediaHint\")": true,
                "resources": [
                  {
                    "is_fulfilled__(name:\"XDTMediaResourceHint\")": true,
                    "image": {
                      "is_fulfilled__(name:\"XDTImageCandidate\")": true,
                      "width": 750,
                      "height": 1333,
                      "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwHcIZWZ&_nc_oc=Ado83B0s5jz8dfuXJcC2_3LwTE9PL6gbnbNffbCb9Fqedq4mnY6cjZuyYpF2INOhly4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af3tIuqnHHcDXSpR8Se9VgrYCPfIN5tCDCv2przUJVP7qw&oe=69DC51CA",
                      "scans_profile": "e35"
                    }
                  }
                ]
              },
              {
                "is_fulfilled__(name:\"XDTMediaHint\")": true,
                "resources": [
                  {
                    "is_fulfilled__(name:\"XDTMediaResourceHint\")": true,
                    "image": {
                      "is_fulfilled__(name:\"XDTImageCandidate\")": true,
                      "width": 750,
                      "height": 500,
                      "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGUjnbD&_nc_oc=AdqD0Jkuffm92QoPIi11YVqryF1qygm1046jKXofnjGH-T1LjQQt-XeE7cstjwFtHC8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af3uLIQczjbO-UFERnTAQVz895UxhhlY__0ndO35DxVGgQ&oe=69DC4AFB",
                      "scans_profile": "e35"
                    }
                  }
                ]
              }
            ]
          }
        }
      },
      "extensions": {
        "is_final": false,
        "fulfilled_payloads": [
          {
            "label": "ClientHintsResponse__force_flush",
            "path": [
              "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)"
            ]
          }
        ],
        "server_metadata": {
          "request_start_time_ms": 1775663933890,
          "time_at_flush_ms": 1775663934189
        }
      },
      "status": "ok"
    },
    {
      "path": [
        "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)"
      ],
      "label": "ProfileTimelineFragment__force_flush",
      "data": {
        "is_fulfilled__(name:\"XDTProfileFeedDict\")": true,
        "pinned_profile_grid_items_ids": "",
        "profile_grid_items_cursor": "QVFCc01Pc2VEN2JZeGpldkswVzUtQkN6Q0lfLWJzczlUUFNQUy1FQU5jZkg4SnQ5S1dxcGtld1NHR1kycFRaSkJQQmJvYlRZcmE3UGdjLWhwTWhBZ0RFNA==",
        "profile_grid_items": [
          {
            "__typename": "XDTProfileGridItemDict",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTProfileGridItemDict\")": true,
            "highlight": null,
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3865659729796199935_787132",
              "id": "3865659729796199935_787132",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "carousel_media_count": null,
              "carousel_media": null,
              "content_views_count": null,
              "enable_waist": true,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/658030605_1256609569870746_7397274986069476460_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bCRwORgGzQAQ7kNvwF5RZh1&_nc_oc=AdquSNjPPpT8z4ajVY0YD9A3h2HbI0Nc171eOzH4Lih5y8lQQ69D8ewnFPPP4iLNoVU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af0NoUxms6Uzb730xi-L2Pf1AB40iHIfVnXwQvSgezxQRQ&oe=69DC528D",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/658030605_1256609569870746_7397274986069476460_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bCRwORgGzQAQ7kNvwF5RZh1&_nc_oc=AdquSNjPPpT8z4ajVY0YD9A3h2HbI0Nc171eOzH4Lih5y8lQQ69D8ewnFPPP4iLNoVU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af0NoUxms6Uzb730xi-L2Pf1AB40iHIfVnXwQvSgezxQRQ&oe=69DC528D",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      24827,
                      49654,
                      74482
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwH4PITn&_nc_oc=Adqyoq6kwCfX-m7IqPTbQttt70XnhGFdeRlmsDNiGBhXkw02d4OE_j7Ov0XDHy1-nm4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af0jyAc1nHvg6-8lZ1_4XKE5cAHZbT0ehcH91rNPWw68Zg&oe=69DC65F1",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 264,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.5723904762,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 60.101
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "media_cropping_info": null,
              "media_type": 2,
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3865659729796199935",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "product_type": "clips",
              "timeline_pinned_user_ids": [
                "787132"
              ],
              "open_carousel_submission_state": null,
              "all_previous_submitters": null,
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "787132",
                "id": "787132",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_referral_eligible": null,
                  "is_fan_club_gifting_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400573960012",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false,
                  "outgoing_request": false
                },
                "full_name": "National Geographic",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "113671860027320",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "787132",
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3o0KjoP-7UWnzrMeJDVV0v3ZEKbTFP5kr_yRiq32FxOw&oe=69DC51E9&_nc_sid=21e75c",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeo"
              },
              "1ltaken_at": 1775048403
            }
          },
          {
            "__typename": "XDTProfileGridItemDict",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTProfileGridItemDict\")": true,
            "highlight": null,
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3844732796656436386_787132",
              "id": "3844732796656436386_787132",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "carousel_media_count": null,
              "carousel_media": null,
              "content_views_count": null,
              "enable_waist": true,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/641943524_1845518526116919_3841198709316411912_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Y4swoqOyiUUQ7kNvwGO7f2W&_nc_oc=Adp59oRdnFp_1xJkfXQkQErDxvM9Gr3YXsfu9hh_ghM5T1HN2EB6o6Fsi-mUkkOksYk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af27t6bHcmFx_Kuy0vADj-Z4yO3somgvCDVWz4FhEwwpMw&oe=69DC47BC",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.71878-15/641943524_1845518526116919_3841198709316411912_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Y4swoqOyiUUQ7kNvwGO7f2W&_nc_oc=Adp59oRdnFp_1xJkfXQkQErDxvM9Gr3YXsfu9hh_ghM5T1HN2EB6o6Fsi-mUkkOksYk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af27t6bHcmFx_Kuy0vADj-Z4yO3somgvCDVWz4FhEwwpMw&oe=69DC47BC",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      48270,
                      96540,
                      144811
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwHcIZWZ&_nc_oc=Ado83B0s5jz8dfuXJcC2_3LwTE9PL6gbnbNffbCb9Fqedq4mnY6cjZuyYpF2INOhly4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af3tIuqnHHcDXSpR8Se9VgrYCPfIN5tCDCv2przUJVP7qw&oe=69DC51CA",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 313,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.5721333333,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 60.074
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "media_cropping_info": null,
              "media_type": 2,
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3844732796656436386",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "product_type": "clips",
              "timeline_pinned_user_ids": [
                "787132"
              ],
              "open_carousel_submission_state": null,
              "all_previous_submitters": null,
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "787132",
                "id": "787132",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_referral_eligible": null,
                  "is_fan_club_gifting_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400573960012",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false,
                  "outgoing_request": false
                },
                "full_name": "National Geographic",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "113671860027320",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "787132",
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3o0KjoP-7UWnzrMeJDVV0v3ZEKbTFP5kr_yRiq32FxOw&oe=69DC51E9&_nc_sid=21e75c",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeo"
              },
              "1ltaken_at": 1772550004
            }
          },
          {
            "__typename": "XDTProfileGridItemDict",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTProfileGridItemDict\")": true,
            "highlight": null,
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3870670793969876810_787132",
              "id": "3870670793969876810_787132",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "carousel_media_count": 10,
              "carousel_media": [
                {
                  "__typename": "XDTMediaDict",
                  "strong_id__": "3870670683399590370_787132",
                  "id": "3870670683399590370_787132",
                  "carousel_parent_id": "3870670793969876810_787132",
                  "image_versions2": {
                    "candidates": [
                      {
                        "width": 1439,
                        "height": 959,
                        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGUjnbD&_nc_oc=AdqD0Jkuffm92QoPIi11YVqryF1qygm1046jKXofnjGH-T1LjQQt-XeE7cstjwFtHC8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af0YaelxPjI6RvoykTe0zPU9eGTmmbCtQqvLzMrkzMLZVw&oe=69DC4AFB",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          56778,
                          113556,
                          170335
                        ]
                      },
                      {
                        "width": 750,
                        "height": 500,
                        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGUjnbD&_nc_oc=AdqD0Jkuffm92QoPIi11YVqryF1qygm1046jKXofnjGH-T1LjQQt-XeE7cstjwFtHC8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af3uLIQczjbO-UFERnTAQVz895UxhhlY__0ndO35DxVGgQ&oe=69DC4AFB",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          27979,
                          55958,
                          83938
                        ]
                      }
                    ],
                    "smart_thumbnail_enabled": null
                  },
                  "is_dash_eligible": null,
                  "media_type": 1,
                  "original_width": 1439,
                  "original_height": 959,
                  "pk": "3870670683399590370"
                },
                {
                  "__typename": "XDTMediaDict",
                  "strong_id__": "3870670679968669302_787132",
                  "id": "3870670679968669302_787132",
                  "carousel_parent_id": "3870670793969876810_787132",
                  "image_versions2": {
                    "candidates": [
                      {
                        "width": 1439,
                        "height": 959,
                        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHWGpJH&_nc_oc=Adq4MS62q4RaW17FSt3lxgcVsGYCVdE03LiBi8fdGFCEhbKN9bap20SIGeNKRRIo2_Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af3qZ0CDa0sTxEb7jopla-bR6rRkpcFJV_PnTI9ycxBQ2A&oe=69DC54D1",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          40239,
                          80479,
                          120719
                        ]
                      },
                      {
                        "width": 750,
                        "height": 500,
                        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHWGpJH&_nc_oc=Adq4MS62q4RaW17FSt3lxgcVsGYCVdE03LiBi8fdGFCEhbKN9bap20SIGeNKRRIo2_Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af34ff6At7KuCNPqV1LiLQhxVvLAVV8IymipYhU10kAhJQ&oe=69DC54D1",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          19829,
                          39659,
                          59488
                        ]
                      }
                    ],
                    "smart_thumbnail_enabled": null
                  },
                  "is_dash_eligible": null,
                  "media_type": 1,
                  "original_width": 1439,
                  "original_height": 959,
                  "pk": "3870670679968669302"
                },
                {
                  "__typename": "XDTMediaDict",
                  "strong_id__": "3870670694816531730_787132",
                  "id": "3870670694816531730_787132",
                  "carousel_parent_id": "3870670793969876810_787132",
                  "image_versions2": {
                    "candidates": [
                      {
                        "width": 1440,
                        "height": 1080,
                        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwHvwsLS&_nc_oc=AdrY5ze1hAp8ujyPcxQk1Xym-cAhzynWqgTPakLWauW0sXHvQvl06iDjAzC14WgkOX0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af34hKF34rZXnNrShDTzvTe8JeOOu8AHgnJ9rLYgdBGjUg&oe=69DC46CA",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          51971,
                          103943,
                          155915
                        ]
                      },
                      {
                        "width": 750,
                        "height": 563,
                        "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwHvwsLS&_nc_oc=AdrY5ze1hAp8ujyPcxQk1Xym-cAhzynWqgTPakLWauW0sXHvQvl06iDjAzC14WgkOX0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af1q3RBxG8zdyVeP0DRNhFunmSzFGX0bfNjVE7jkrsWccA&oe=69DC46CA",
                        "scans_profile": "e35",
                        "estimated_scans_sizes": [
                          25599,
                          51198,
                          76797
                        ]
                      }
                    ],
                    "smart_thumbnail_enabled": null
                  },
                  "is_dash_eligible": null,
                  "media_type": 1,
                  "original_width": 1440,
                  "original_height": 1080,
                  "pk": "3870670694816531730"
                }
              ],
              "content_views_count": null,
              "enable_waist": true,
              "image_versions2": {
                "additional_candidates": null,
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      56778,
                      113556,
                      170335
                    ],
                    "height": 959,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGUjnbD&_nc_oc=AdqD0Jkuffm92QoPIi11YVqryF1qygm1046jKXofnjGH-T1LjQQt-XeE7cstjwFtHC8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af0YaelxPjI6RvoykTe0zPU9eGTmmbCtQqvLzMrkzMLZVw&oe=69DC4AFB",
                    "width": 1439
                  },
                  {
                    "estimated_scans_sizes": [
                      27979,
                      55958,
                      83938
                    ],
                    "height": 500,
                    "scans_profile": "e35",
                    "url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwGUjnbD&_nc_oc=AdqD0Jkuffm92QoPIi11YVqryF1qygm1046jKXofnjGH-T1LjQQt-XeE7cstjwFtHC8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_ss=7a3ba&oh=00_Af3uLIQczjbO-UFERnTAQVz895UxhhlY__0ndO35DxVGgQ&oe=69DC4AFB",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": null,
                "smart_thumbnail_enabled": null
              },
              "media_cropping_info": null,
              "media_type": 8,
              "original_height": 959,
              "original_width": 1439,
              "pk": "3870670793969876810",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "product_type": "carousel_container",
              "timeline_pinned_user_ids": [],
              "open_carousel_submission_state": "closed",
              "all_previous_submitters": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "787132",
                "id": "787132",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_referral_eligible": null,
                  "is_fan_club_gifting_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400573960012",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false,
                  "outgoing_request": false
                },
                "full_name": "National Geographic",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "113671860027320",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "787132",
                "profile_pic_id": "3865702555259028436_787132",
                "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3o0KjoP-7UWnzrMeJDVV0v3ZEKbTFP5kr_yRiq32FxOw&oe=69DC51E9&_nc_sid=21e75c",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeo"
              },
              "1ltaken_at": 1775642401
            }
          }
        ],
        "more_available": true,
        "next_max_id": "3868170261056492782",
        "num_results": 12,
        "user": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "full_name": "National Geographic",
          "has_onboarded_to_text_post_app": null,
          "is_cannes": false,
          "is_private": false,
          "is_verified": true,
          "pk": "787132",
          "profile_grid_display_type": "default",
          "profile_overlay_info": {
            "bloks_payload": null,
            "overlay_format": "NONE"
          },
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3o0KjoP-7UWnzrMeJDVV0v3ZEKbTFP5kr_yRiq32FxOw&oe=69DC51E9&_nc_sid=21e75c",
          "username": "natgeo",
          "user_activation_info": {
            "activation_type": null
          }
        },
        "auto_load_more_enabled": true
      },
      "extensions": {
        "is_final": false
      }
    },
    {
      "path": [
        "1$xdt_api__v1__profile_timeline(_request_data:{\"count\":$count,\"exclude_comment\":$exclude_comment,\"fetch_all_highlights\":$fetch_all_highlights,\"fetch_media_for_highlights\":$include_associated_highlights,\"fetch_profile_grid_items\":$fetch_profile_grid_items,\"is_pull_to_refresh\":$is_pull_to_refresh,\"max_id\":$max_id,\"pinned_profile_grid_items_ids\":$pinned_profile_grid_items_ids,\"profile_grid_items_cursor\":$profile_grid_items_cursor},user_id:$user_id)",
        "profile_grid_items",
        11
      ],
      "label": "ProfileTimelineMediaItemDeferredFields",
      "data": {
        "__typename": "XDTMediaDict",
        "strong_id__": "3868170261056492782_787132",
        "id": "3868170261056492782_787132",
        "is_fulfilled__(name:\"XDTMediaDict\")": true,
        "linked_media_data": null,
        "channel_tag_data": null,
        "organic_cta_type": null,
        "organic_cta_info": null,
        "story_prompts": null,
        "carousel_media_pending_post_count": null,
        "main_feed_carousel_starting_media_id": null,
        "1ftallest_media_aspect_ratio": null,
        "open_to_public_submission_description_text": null,
        "is_dismiss_pending_media_banner": null,
        "save_count": null,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYjBlOGRkZTk5OTViNDM1MDhkOGJiYWM0MDQ4OGU5ZDUzODY4MTcwMjYxMDU2NDkyNzgyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkzNDUxMnwzODY4MTcwMjYxMDU2NDkyNzgyfDM4NTg3OTYxMTA0fDRmYzU0NTlmM2U0ZDVlMjk3NDBmNDc1NjgzOWRkNWQzMjAxY2EzOWE3YzUwMjE1NTgxNWEzNWQ4ZGJkOTk1YzMifSwic2lnbmF0dXJlIjoiIn0=",
        "wearable_attribution_info": null,
        "accessibility_caption": null,
        "are_remixes_crosspostable": true,
        "crosspost": null,
        "crosspost_metadata": {
          "fb_crosspost_deeplink_profile_id": null,
          "fb_crosspost_fbid": null,
          "is_feedback_aggregated": null,
          "th_unified_feedback_row_tap_target_url": null,
          "unified_feedback_enabled": null,
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "attribution_content_url": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_post_id": null,
        "boosted_status": null,
        "original_media_has_visual_reply_media": false,
        "like_and_view_counts_disabled": false,
        "share_count_disabled": false,
        "code": "DWugFulAJTu",
        "coauthor_producer_can_see_organic_insights": false,
        "coauthor_producers": [
          {
            "__typename": "XDTUserDict",
            "strong_id__": "271370325",
            "id": "271370325",
            "full_name": "christine wilkinson, phd",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3245086179333885169_271370325",
            "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/404288054_706561544741164_8609495828476348252_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44ODguYzIifQ&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=9NDLLLLwDV8Q7kNvwEDYOue&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GDbyGBgs4eItnYICAFxHikfXEnt3bkULAAAB1501500j-ccb7-5&oh=00_Af3ukxjK13rG_leSqNw6diGcujgn7toAa-P--IooQowq3A&oe=69DC57AB&_nc_sid=21e75c",
            "username": "christine_eleanor",
            "user_activation_info": {
              "activation_type": null
            }
          }
        ],
        "invited_coauthor_producers": [],
        "caption": {
          "__typename": "XDTCommentDict",
          "strong_id__": "18083194658064008",
          "pk": "18083194658064008",
          "bit_flags": 0,
          "content_type": "comment",
          "1lcreated_at": 1775404813,
          "1lcreated_at_utc": 1775404813,
          "did_report_as_spam": false,
          "fb_mentioned_users": null,
          "has_translation": null,
          "is_covered": false,
          "is_ranked_comment": false,
          "media_id": "3868170261056492782",
          "private_reply_status": 0,
          "share_enabled": false,
          "status": "Active",
          "text": "Spotted hyenas are a powerful example of the resilience and strength found in nature. For wildlife ecologist, conservation scientist, and National Geographic Explorer Dr. Christine Wilkinson (@christine_eleanor), these reminders are what wonder is all about. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
          "text_translation": null,
          "type": 1,
          "user": {
            "__typename": "XDTUserDict",
            "strong_id__": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "1fcoeff_weight": null,
            "social_context": null,
            "is_active": null,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3o0KjoP-7UWnzrMeJDVV0v3ZEKbTFP5kr_yRiq32FxOw&oe=69DC51E9&_nc_sid=21e75c",
            "has_onboarded_to_text_post_app": null,
            "follower_count": 274984770,
            "fbid_v2": "17841400573960012"
          }
        },
        "caption_add_on": null,
        "caption_is_edited": false,
        "carousel_last_edited_at": null,
        "creator_viewer_insights": null,
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "can_modify_carousel": null,
        "can_viewer_save": true,
        "can_viewer_reshare": true,
        "has_liked": false,
        "top_likers": [],
        "facepile_top_likers": null,
        "floating_context_items": [],
        "social_context": [],
        "is_comments_gif_composer_enabled": false,
        "is_currently_promoting_by_sponsor": null,
        "is_auto_created": null,
        "is_cutout_sticker_allowed": false,
        "is_eligible_for_media_note_recs_nux": null,
        "is_reuse_allowed": false,
        "is_post_live_clips_media": false,
        "is_quiet_post": false,
        "is_shared_from_basel": null,
        "media_attributions_data": [],
        "igbio_product": null,
        "location": null,
        "play_count": 1304849,
        "like_count": 7479,
        "client_cache_key": "Mzg2ODE3MDI2MTA1NjQ5Mjc4Mg==.3",
        "filter_type": 0,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "subscribe_cta_visible": false,
        "video_subtitles_locale": null,
        "translated_video_subtitles": null,
        "byoa_langs": null,
        "video_sticker_locales": [],
        "sticker_translations_enabled": null,
        "clips_karaoke_caption": null,
        "clips_captions": null,
        "clips_captions_translations_urls": null,
        "clips_text": null,
        "should_request_ads": false,
        "is_paid_partnership": false,
        "sponsor_tags": null,
        "is_visual_reply_commenter_notice_enabled": true,
        "clips_tab_pinned_user_ids": [],
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "owner": {
          "__typename": "XDTUserDict",
          "strong_id__": "787132",
          "id": "787132",
          "can_see_quiet_post_attribution": true,
          "fbid_v2": "17841400573960012",
          "feed_post_reshare_disabled": false,
          "friendship_status": {
            "following": false,
            "is_bestie": false,
            "is_feed_favorite": false,
            "is_restricted": false
          },
          "full_name": "National Geographic",
          "has_anonymous_profile_picture": false,
          "is_favorite": false,
          "is_private": false,
          "is_unpublished": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3o0KjoP-7UWnzrMeJDVV0v3ZEKbTFP5kr_yRiq32FxOw&oe=69DC51E9&_nc_sid=21e75c",
          "show_account_transparency_details": true,
          "transparency_product_enabled": false,
          "username": "natgeo"
        },
        "fundraiser_tag": {
          "beneficiary_username": null,
          "beneficiary_name": null,
          "can_viewer_donate": null,
          "contextual_title_str": null,
          "formatted_amount_raised": null,
          "formatted_fundraiser_progress_info_text": null,
          "formatted_goal_amount": null,
          "fundraiser_id": null,
          "fundraiser_title": null,
          "fundraiser_type": null,
          "has_standalone_fundraiser": false,
          "progress_str": null,
          "thumbnail_display_url": null,
          "is_media_owner_fundraiser_owner": null,
          "fundraiser_owner_username": null,
          "show_fundraiser_owner_attribution": null,
          "can_viewer_remove_fundraiser_tag": null
        },
        "comment_likes_enabled": true,
        "comments_disabled": null,
        "comment_threading_enabled": true,
        "clips_metadata": {
          "originality_info": null,
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
          "branded_content_tag_info": {
            "can_add_tag": false
          },
          "clips_creation_entry_point": "",
          "content_appreciation_info": null,
          "contextual_highlight_info": null,
          "disable_use_in_clips_client_cache": false,
          "is_fan_club_promo_video": false,
          "is_public_chat_welcome_video": false,
          "is_shared_to_fb": false,
          "mashup_info": {
            "can_toggle_mashups_allowed": false,
            "has_been_mashed_up": false,
            "has_nonmimicable_additional_audio": false,
            "is_creator_requesting_mashup": false,
            "is_light_weight_check": true,
            "is_pivot_page_available": false,
            "mashup_type": null,
            "mashups_allowed": false,
            "non_privacy_filtered_mashups_media_count": 0,
            "original_media": null
          },
          "merchandising_pill_info": null,
          "music_canonical_id": "18439666597118965",
          "music_info": null,
          "original_sound_info": {
            "allow_creator_to_rename": true,
            "audio_asset_id": "26074550038833869",
            "audio_parts": [],
            "audio_parts_by_filter": [],
            "can_remix_be_shared_to_fb": true,
            "can_remix_be_shared_to_fb_expansion": true,
            "consumption_info": {
              "is_bookmarked": false,
              "is_trending_in_clips": false,
              "should_mute_audio_reason": ""
            },
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBManifestTimestamp=\"1775663934\" FBManifestIdentifier=\"Fvzss50NKRa4sr3lnNynAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"931771249568924a\" bandwidth=\"66894\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66894\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m78/AQObEBSySE0AGNBbG4lxf162Q155i5gTcG0OizHqB4rRxcGyySZDjummT0z9r1wsiCbVlaRrtWqIqFWzQVPE7UxmQ1lTMC4PQzMnv0M.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=8_2Uu26HoJkQ7kNvwEKxPmB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo2NzA4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af1NGKF507lC4QipIzkghEMXjLJazcBbg6r4fbrh41sf0g&amp;oe=69D86E19</BaseURL><SegmentBase indexRange=\"824-1143\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
            "duration_in_ms": 47881,
            "hide_remixing": false,
            "ig_artist": {
              "__typename": "XDTUserDict",
              "strong_id__": "787132",
              "id": "787132",
              "full_name": "National Geographic",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3865702555259028436_787132",
              "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGJE1xHQXT31z9xYS570DWQE5STmS6h2pl0y2vP5wcH3YhnThnStV7fYUw-Qjr-p6Y&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&edm=AHBgTAQBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3o0KjoP-7UWnzrMeJDVV0v3ZEKbTFP5kr_yRiq32FxOw&oe=69DC51E9&_nc_sid=21e75c",
              "username": "natgeo"
            },
            "is_audio_automatically_attributed": false,
            "is_eligible_for_audio_effects": true,
            "is_explicit": false,
            "is_original_audio_download_eligible": false,
            "oa_owner_is_music_artist": false,
            "is_reuse_disabled": false,
            "is_xpost_from_fb": false,
            "original_audio_subtype": "default",
            "original_audio_title": "Original audio",
            "original_media_id": "3868170261056492782",
            "progressive_download_url": "https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m69/AQNsTvlWrX5b5jAnAagr-VEkXvHgjuh1R7UtSI3qunavCZFTpObST3AI8L-cDc_wZTw8bAKRL2XuixVvoM6ISAHt.mp4?strext=1&_nc_cat=100&_nc_sid=8bf8fe&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_ohc=TbFtdnyPN3QQ7kNvwG1Z2hH&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0PEh0i-wxos7PrV2U_P7SbueosiA_P_flzB5n_j7FOZQ&oe=69DC4132",
            "should_mute_audio": false,
            "time_created": 1775404814,
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "professional_clips_upsell_type": 0,
          "show_achievements": false
        },
        "creative_config": null,
        "max_num_visible_preview_comments": 2,
        "has_more_comments": true,
        "has_tagged_users": true,
        "fb_user_tags": {
          "in": []
        },
        "has_reshares": null,
        "preview": null,
        "product_collection_tag": null,
        "product_suggestions": null,
        "product_tags": null,
        "photo_of_you": false,
        "is_organic_product_tagging_eligible": true,
        "media_notice": null,
        "media_overlay_info": null,
        "boost_upsell_banner_payload": null,
        "is_fb_only": null,
        "is_artist_pick": false,
        "can_see_insights_as_brand": false,
        "comment_count": 78,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "can_view_more_preview_comments": false,
        "hide_view_all_comment_entrypoint": true,
        "inline_composer_display_condition": null,
        "1finline_composer_imp_trigger_time": null,
        "is_third_party_downloads_eligible": false,
        "ig_media_sharing_disabled": false,
        "has_viewer_saved": null,
        "carousel_media": null,
        "number_of_qualities": 8,
        "is_dash_eligible": 1,
        "upcoming_event": null,
        "usertags": null,
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBDeliveryExperimentName=\"ig4a_stall_profile_tuning_v2\" FBDeliveryExperimentGroup=\"test_1_6\" FBManifestTimestamp=\"1775663934\" FBManifestIdentifier=\"Fvzss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxqbV6aDR+bYDqvaKk6SpqgT+7OaL4NTBBNj9mrKQtbMFjO6L353LugW8goKl5dy6BYLQssb/qogGmPbggPvSlAbwr/bX4oT0BoSVlbCehoIHqrXuq+uJnQfYts6QtoSsWxwYHWlnNGFfdmlkZW9fcW9lX3N0YWxsX3Byb2ZpbGVzGBxpZzRhX3N0YWxsX3Byb2ZpbGVfdHVuaW5nX3YyGAh0ZXN0XzFfNgASGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyIsGRgFbGlnaHQAFgYUABIUAgA=\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1536512375144606v\" bandwidth=\"125041\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"748393\" FBPlaybackResolutionMos=\"0:100,360:68.6,480:63.5,720:57.2,1080:52.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.7,480:90.2,720:86.7,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOC-37dngJq90Dyy1_JazUnnPGdWCHskETHnxkRIIJCSOlZF1fVQ-6mAFGNhj2z93WeeIs714OUklQmfut9nIzTnVBICEHS1YfCoAw.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=e25xSTehHgsQ7kNvwGcAIzW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTI1MDQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af38iXjYo4_yHdcB6BxdFdZu4pWIsKXazktDauZFg3vVHg&amp;oe=69DC5053</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-11379\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-53195\" FBFirstSegmentRange=\"978-73681\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"73682-177801\" FBPrefetchSegmentRange=\"978-73681\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1707180720280577v\" bandwidth=\"268984\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1609913\" FBPlaybackResolutionMos=\"0:100,360:82.1,480:77.4,720:72,1080:65\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:96,720:94.9,1080:90.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOoI_Qc5Hb567q3s03DZ7hurU3EPc934bMb3FmMMVaHXDUYxsb4QiUQt8F8TcKitfPDLHzHey1wENKGp-vSnIF1hHoyzJ4LrrK2kjM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=ajpqDB5imFoQ7kNvwE5qdN5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MjY4OTg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af37xCB3bGTQLIRm04qUun8NAll5DusT2fGMSSIctL47RQ&amp;oe=69DC64EB</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-19527\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-105884\" FBFirstSegmentRange=\"978-157985\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"157986-375189\" FBPrefetchSegmentRange=\"978-157985\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1944018522917880v\" bandwidth=\"368764\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2207110\" FBPlaybackResolutionMos=\"0:100,360:85.9,480:81.7,720:75.8,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.04,480:97.6,720:97.2,1080:93.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQM3ITI-kIVflLXqBQCMcqSKriqhB8j74oqGUj6f3pYWDnqOC18MUJJNe0oZbKf0kPXddx31PP3oAzTIyNssN5V0g7YFH89E5A-Ij6s.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=Mwx1ng6pC6sQ7kNvwHaRHzt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MzY4NzY0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af37vJ845-B5Jlms6XFwOuGJmTSSuwhIUNzjl-AdI2rwuQ&amp;oe=69DC662F</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-24075\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-141715\" FBFirstSegmentRange=\"978-216596\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"216597-512096\" FBPrefetchSegmentRange=\"978-216596\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1218968110062997v\" bandwidth=\"442503\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2648452\" FBPlaybackResolutionMos=\"0:100,360:87.7,480:83.8,720:77.5,1080:70.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.61,480:98.35,720:98.31,1080:95.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQOYTMwguxNmYzts7ztqP3uq8QYqnySSAGvKGU84jFkz30lRwgwLYRu68NUaE4CuVcCCkccg0gJEpbQIdwnc6OfTFFkYbjN5LqbfVG4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=KFTAZdhAk40Q7kNvwFO10nW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NDQyNTAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af2apsmm91nERV-hv2dZEnS--fBGYUCVG7CX9-OFx44rmQ&amp;oe=69DC56A1</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-27189\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-169993\" FBFirstSegmentRange=\"978-261689\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"261690-617097\" FBPrefetchSegmentRange=\"978-261689\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1734255584222604v\" bandwidth=\"593051\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3549501\" FBPlaybackResolutionMos=\"0:100,360:89.9,480:86.3,720:80.5,1080:72.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99,480:98.97,720:99.193,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9lx9WGs0aObQ1f5j5Tn6y1xVQXR-Dwub7W_SxmroZb4LDoDVxPW13tmY1vHIkgBkSqIxvS44m4qTOlQHuogzz-fjvXsOFNStGw5o.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=IG_0Np9TPzEQ7kNvwE53Ce5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NTkzMDUxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af1rq3ftHPCmIld3eoiBlPZ0YjCyCDtWg3VbK7Sd777rUQ&amp;oe=69DC5BBE</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-32309\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-227501\" FBFirstSegmentRange=\"978-353323\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"353324-811886\" FBPrefetchSegmentRange=\"978-353323\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1974830039737666v\" bandwidth=\"808049\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4836297\" FBPlaybackResolutionMos=\"0:100,360:91.5,480:88.1,720:82.7,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.177,480:99.289,720:99.419,1080:98.77\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQNxzz3B_d6VnnNmwILSsdhY1b8WYAyEq1nGyoBddc0-zErqxX-3eoxHWRJoRjzW8rt7CPCOSi7aXg9mJJvD7MDk23Y4mXgSrDlMMp0.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=1oWA7fT-WaIQ7kNvwFsPU5V&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6ODA4MDQ5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af1PMtVT99pwrVy8UNquY6hc7LB2CMui6gNBZlCy_BC2Vg&amp;oe=69DC3E3B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-37690\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-306742\" FBFirstSegmentRange=\"978-478293\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"478294-1073273\" FBPrefetchSegmentRange=\"978-478293\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2034265537498453v\" bandwidth=\"1150676\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6886972\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:89.4,720:84.3,1080:75.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.316,480:99.475,720:99.604,1080:99.184\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQO8nzMmBULFzOq0Uc221nMlzpRXdUpXzRan5dqj-VDzxkIrtzc1nz0dI1BX50zPIMwgzzgD9a0zuNNVJoHjAR_qboR3srHbCUwAf98.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=AJfwxCErVuwQ7kNvwFqvH5U&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTE1MDY3NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af3DNLHqIcYW2S8Gl30SRDhRZFt5V_ymVlyS67cY8N6zow&amp;oe=69DC467B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-42521\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-414721\" FBFirstSegmentRange=\"978-651076\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"651077-1467135\" FBPrefetchSegmentRange=\"978-651076\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"965261856159059v\" bandwidth=\"1802418\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"10787749\" FBPlaybackResolutionMos=\"0:100,360:93.6,480:91,720:86.4,1080:81.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.439,480:99.57,720:99.699,1080:99.627\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNl6wEb07Ks3JIhuPO2wCPZMvypoiru-vDavX2ZbnVx8EmjXzlq5vNBYsVwM0MoQtRL7pguuPZmXv_tnRPUIgRfIL00yZnEyV3zjZQ.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=WeUmuiwzlkoQ7kNvwGtswPs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTgwMjQxOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af3LVK-mZbNJn89wwX6iVrpnNdG9coyzCcPiVAaGE_9SCQ&amp;oe=69DC591C</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-62167\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-590586\" FBFirstSegmentRange=\"978-956290\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"956291-2465586\" FBPrefetchSegmentRange=\"978-956290\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"25711055888567724a\" bandwidth=\"43137\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"43137\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"259233\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPwGwzN_jZWTG5g53W6HPaq6prVW3aFxZFUMoApdF5Bb07alTzINwfJIHhTt2__EB0B73uktjzHCPmfysFRIfXNu5jyUMQk7HQ2MAA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=D8aq4uZD0HoQ7kNvwGF-2kn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo0MzMwMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af0mMlv1dgNKr_SLHFlX7zLz_A1PCTz309KKHPv7sUXWfg&amp;oe=69DC3521</BaseURL><SegmentBase indexRange=\"837-988\" timescale=\"48000\" FBMinimumPrefetchRange=\"989-2211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"989-15011\" FBFirstSegmentRange=\"989-27427\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27428-53863\" FBPrefetchSegmentRange=\"989-27427\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1520437802786668a\" bandwidth=\"71500\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71500\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"429033\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m367/AQM1qgyiYipO3nTb3Q4w_ENJZ3IxJuj0VPo2tuNaBczlM_oHVqwMkDYBW3T0y1773ATnvblNT7r_xf3TsujSnPIypzOSKbCvToAOuws.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-1.cdninstagram.com&amp;_nc_ohc=hwhUj3NemRQQ7kNvwHmj2y1&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo3MTY2NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af3ubfODdB-Wk51vqd4bhP_hw3VosR1sz347CiftMI2uDw&amp;oe=69DC4C06</BaseURL><SegmentBase indexRange=\"838-989\" timescale=\"48000\" FBMinimumPrefetchRange=\"990-2669\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"990-24617\" FBFirstSegmentRange=\"990-45672\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"45673-89246\" FBPrefetchSegmentRange=\"990-45672\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1270292424743743a\" bandwidth=\"104937\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"104937\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"629205\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOSZPTrQoZvEzpNyz3hhbxCnafm4XAlkTPd_h7zn5N1n6R0Ga6E8UgDUI08GX-XKGcGJAxmhV-HhXGeeaJ0XyTdLAqhdbtcuwmB8ms.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-2.cdninstagram.com&amp;_nc_ohc=L_y6Qh90gVgQ7kNvwHKrFaL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMDUxMDEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af3AZnQuh5uJmO_If5w2lHp_XBQmeBkMzD-Hf9RqnPs9hw&amp;oe=69DC5BBA</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2362\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-35155\" FBFirstSegmentRange=\"985-65716\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"65717-128980\" FBPrefetchSegmentRange=\"985-65716\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1536210714590086a\" bandwidth=\"136838\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"136838\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"820186\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lga3-3.cdninstagram.com/o1/v/t2/f2/m367/AQO7KXm8TEDvhztA9v_PIl-O0CaShP5_2iBO4ggZMBeDRGTOTXVI3umPjYEK9ju_ZrOe1b_AWcnu75HARzg6Y6KbrJQ7pMmp_w0mKfU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lga3-3.cdninstagram.com&amp;_nc_ohc=itqu0TbKGQYQ7kNvwFA0dfS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMzcwMDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=DuSWxqWaAFeLwH_ucY59vA&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af2OseoS08Xz03O5RRDHDPwfRbBGsEzfeTYl27T2wPgk0w&amp;oe=69DC4117</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2442\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-44989\" FBFirstSegmentRange=\"985-85365\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85366-166815\" FBPrefetchSegmentRange=\"985-85365\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "video_versions": [
          {
            "url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwE9iPx_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0TaBk-8h62o54mXDAW41OMR6wIHawWURRTWwXvhsSn3w&oe=69D87233",
            "type": 101,
            "width": 720,
            "height": 1280
          },
          {
            "url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwE9iPx_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0TaBk-8h62o54mXDAW41OMR6wIHawWURRTWwXvhsSn3w&oe=69D87233",
            "type": 102,
            "width": 720,
            "height": 1280
          },
          {
            "url": "https://scontent-lga3-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwE9iPx_&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=DuSWxqWaAFeLwH_ucY59vA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0TaBk-8h62o54mXDAW41OMR6wIHawWURRTWwXvhsSn3w&oe=69D87233",
            "type": 103,
            "width": 720,
            "height": 1280
          }
        ],
        "1fvideo_duration": 47.8930015564,
        "1fvideo_subtitles_confidence": null,
        "video_subtitles_enabled": null,
        "video_subtitles_status": null,
        "video_subtitles_uri": null,
        "visibility": null,
        "view_count": null,
        "visual_comment_reply_sticker_info": null,
        "visual_replies_info": null,
        "xpost_deny_reason": null,
        "xpost_deny_reason_enum": null,
        "threads_xpost_deny_reason": null,
        "has_audio": true,
        "has_delayed_metadata": false,
        "has_hidden_comments": null,
        "reshare_count": 153,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_post_live": null,
        "deleted_reason": 0,
        "has_shared_to_fb": 0,
        "dominant_color": null,
        "music_metadata": null,
        "fb_comment_count": null,
        "fb_like_count": null,
        "fb_play_count": null,
        "ig_play_count": 1304849,
        "autodub_status": null,
        "mashup_info": null,
        "enable_media_notes_production": true,
        "media_repost_count": 91,
        "media_reposter_bottomsheet_enabled": false,
        "media_notes": {
          "items": []
        },
        "clips_attribution_info": null,
        "mv_link": null,
        "shimmed_mv_link": null
      },
      "extensions": {
        "is_final": false
      }
    }
  ]
}
```

</details>

---

### GET /gql/user/related/profiles

Get related profiles by user id

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/related/profiles?id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/related/profiles",
        headers=headers,
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/related/profiles?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
[
  {
    "pk": "247944034",
    "id": "247944034",
    "username": "beyonce",
    "full_name": "Beyoncé",
    "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.2885-19/476007829_1163063532177165_1226079916897236515_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF0BgoIV24CvyBJEXBtD3qf7aUm4hbCim3VP4sQqCd1sGF75yaKpAeYlvQhJXmnJwQ&_nc_ohc=CoEZxRj_enMQ7kNvwGd0V3x&_nc_gid=F5ibgO50K9Ep7HGkUaauuQ&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af2jo4zSx2L2rUIYkF6MU7QZhF_kSrgx7Jfj_u3rMPMIhA&oe=69DC3DAE&_nc_sid=94fea1",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "11830955",
    "id": "11830955",
    "username": "taylorswift",
    "full_name": "Taylor Swift",
    "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/626626039_18625087675054956_4249858978563573242_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF0BgoIV24CvyBJEXBtD3qf7aUm4hbCim3VP4sQqCd1sGF75yaKpAeYlvQhJXmnJwQ&_nc_ohc=lWhS5q1zaL4Q7kNvwE7mv99&_nc_gid=F5ibgO50K9Ep7HGkUaauuQ&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af2lwxJboiOJuYaRnx4eNOZ0ASuUEkwM27X6UeDTmLlS4Q&oe=69DC577A&_nc_sid=94fea1",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "561009264",
    "id": "561009264",
    "username": "discovery",
    "full_name": "Discovery",
    "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.2885-19/496344929_18509875681049265_1952047293875638812_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF0BgoIV24CvyBJEXBtD3qf7aUm4hbCim3VP4sQqCd1sGF75yaKpAeYlvQhJXmnJwQ&_nc_ohc=e10HFbdTyOcQ7kNvwHh7Wa1&_nc_gid=F5ibgO50K9Ep7HGkUaauuQ&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af0ecnKU3UqdCVO5rpaj1uskUONgWXe1N1Jlaws9mlbw1g&oe=69DC584D&_nc_sid=94fea1",
    "is_private": false,
    "is_verified": true
  }
]
```

</details>

---

### GET /gql/user/reposts

Get user media reposts

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `repost_next_max_id` | string | No | Repost Next Max Id |
| `flat` | boolean | No | Flatten nested response into simple items list |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/reposts?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_reposts_gql(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/reposts",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/reposts?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "data": {
    "__typename": "Query",
    "strong_id__": null,
    "1$fetch__XDTUserDict(id:$id)": {
      "__typename": "XDTUserDict",
      "strong_id__": "787132",
      "id": "787132",
      "username": "natgeo",
      "1$user_reposts_timeline(max_id:$max_id)": {
        "is_fulfilled__(name:\"XDTProfileFeedDict\")": true,
        "repost_grid_items": [
          {
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3870130142916282392_18091046",
              "id": "3870130142916282392_18091046",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "all_previous_submitters": null,
              "carousel_media": null,
              "carousel_media_count": null,
              "carousel_media_pending_post_count": null,
              "channel_tag_data": null,
              "content_views_count": null,
              "enable_media_notes_production": true,
              "enable_waist": true,
              "facepile_top_likers": null,
              "gen_ai_detection_method": {
                "detection_method": "NONE"
              },
              "has_delayed_metadata": false,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax7-1.cdninstagram.com/v/t51.71878-15/658993118_1501376918245324_1176804504778663620_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vcf2Ah6wBGoQ7kNvwGcx3Ol&_nc_oc=AdqFSl3zHIFmEp_0L67UyxjEPR-kvSJzgvFuSm_4C6PJ67LUiNk4Z0CxbOjiyMaiMLw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af2RC35qOtZm2RUdNOV7ajddyW-N2bK4RtfBKa9iTU5mKQ&oe=69DC336F",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax7-1.cdninstagram.com/v/t51.71878-15/658993118_1501376918245324_1176804504778663620_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vcf2Ah6wBGoQ7kNvwGcx3Ol&_nc_oc=AdqFSl3zHIFmEp_0L67UyxjEPR-kvSJzgvFuSm_4C6PJ67LUiNk4Z0CxbOjiyMaiMLw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af2RC35qOtZm2RUdNOV7ajddyW-N2bK4RtfBKa9iTU5mKQ&oe=69DC336F",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      22800,
                      45600,
                      68400
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/659582635_18583331794043047_3383163414177246697_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=Mzg3MDEzMDE0MjkxNjI4MjM5MjE4NTgzMzMxNzkxMDQzMDQ3.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hMjOf9gwscIQ7kNvwFrWVhi&_nc_oc=AdoAtgfrCNS3a2co0wnNLu5BaYsPlUpbtv0SdlYpbXHQS6Y0k7iu1BLpv6PwOA1L76E&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af0EeSis2kESGtfDM-dUpSBlbMRuwhMnK6YB7IPHWBnkYg&oe=69DC556D",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 368,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.4081809523809524,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 42.859
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "is_dismiss_pending_media_banner": null,
              "main_feed_carousel_starting_media_id": null,
              "media_cropping_info": null,
              "media_notes": {
                "is_fulfilled__(name:\"XDTMediaNotesResponse\")": true,
                "items": [
                  {
                    "audience": 7,
                    "1lcreated_at": 1775577889,
                    "has_translation": false,
                    "id": "17948733029984622",
                    "note_response_info": null,
                    "note_style": 13,
                    "reactions": [],
                    "text": "",
                    "user": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "787132",
                      "id": "787132",
                      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=XbeNvhLXv28Q7kNvwEyTvya&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3r23_FsnaV-pg8vreXK0O9xTHKfuPYXAbMgILhndg3gg&oe=69DC51E9&_nc_sid=f514b5",
                      "username": "natgeo"
                    },
                    "user_id": "787132"
                  }
                ]
              },
              "media_repost_count": 32,
              "media_reposter_bottomsheet_enabled": false,
              "media_type": 2,
              "open_carousel_submission_state": null,
              "open_to_public_submission_description_text": null,
              "organic_cta_info": null,
              "organic_cta_type": null,
              "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODQ0MjM0NTU5MDJjNGM1NmE0ZWNjY2E5Y2QzM2Y4YWUzODcwMTMwMTQyOTE2MjgyMzkyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkzODAyNHwzODcwMTMwMTQyOTE2MjgyMzkyfDM4ODQyNzE4NzYzfGYzNTVkNWRiOTg1YmM2ZDRjYWNkYjhlNTMyNjRmNjhmZTcxZGFlNTE4Nzg5OWY2ZDk2ZmRmNzdhZWE2ZTJmNzMifSwic2lnbmF0dXJlIjoiIn0=",
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3870130142916282392",
              "product_type": "clips",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "save_count": null,
              "story_prompts": null,
              "1ltaken_at": 1775577621,
              "1ftallest_media_aspect_ratio": null,
              "timeline_pinned_user_ids": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_gifting_eligible": null,
                  "is_fan_club_referral_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false,
                  "is_viewer_unconnected": false,
                  "outgoing_request": false
                },
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "105432187515418",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "wearable_attribution_info": null,
              "accessibility_caption": null,
              "are_remixes_crosspostable": true,
              "attribution_content_url": null,
              "audience": null,
              "autodub_status": null,
              "boost_unavailable_identifier": null,
              "boost_unavailable_reason": null,
              "boost_upsell_banner_payload": null,
              "boosted_post_id": null,
              "boosted_status": null,
              "byoa_langs": null,
              "can_modify_carousel": null,
              "can_see_insights_as_brand": false,
              "can_view_more_preview_comments": false,
              "can_viewer_reshare": true,
              "can_viewer_save": true,
              "caption": {
                "__typename": "XDTCommentDict",
                "strong_id__": "17948732129984622",
                "pk": "17948732129984622",
                "bit_flags": 0,
                "content_type": "comment",
                "1lcreated_at": 1775577607,
                "1lcreated_at_utc": 1775577607,
                "did_report_as_spam": false,
                "has_translation": null,
                "is_covered": false,
                "is_ranked_comment": false,
                "media_id": "3870130142916282392",
                "private_reply_status": 0,
                "share_enabled": false,
                "status": "Active",
                "text": "Moments of wonder don't just come from nature—but from those who understand it masterfully too. That was conservationist and National Geographic Explorer @drsteveboyes' experience when searching for Angola's mythical \"ghost elephants\" with Xui, a San master tracker. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection and stream #GhostElephants on @DisneyPlus.",
                "type": 1,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "18091046",
                  "id": "18091046",
                  "1fcoeff_weight": null,
                  "fbid_v2": "17841401291380282",
                  "follower_count": 7301247,
                  "full_name": "National Geographic TV",
                  "has_onboarded_to_text_post_app": null,
                  "is_active": null,
                  "is_private": false,
                  "is_verified": true,
                  "pk": "18091046",
                  "profile_pic_id": "3865691934048399589_18091046",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                  "social_context": null,
                  "username": "natgeotv"
                }
              },
              "caption_add_on": null,
              "caption_is_edited": false,
              "carousel_last_edited_at": null,
              "client_cache_key": "Mzg3MDEzMDE0MjkxNjI4MjM5Mg==.3",
              "clips_attribution_info": null,
              "clips_karaoke_caption": null,
              "clips_captions": null,
              "clips_captions_translations_urls": null,
              "clips_metadata": {
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
                  "best_audio_cluster_id": "3897912897183605"
                },
                "audio_type": "original_sounds",
                "branded_content_tag_info": {
                  "can_add_tag": false
                },
                "clips_creation_entry_point": "",
                "content_appreciation_info": null,
                "contextual_highlight_info": null,
                "disable_use_in_clips_client_cache": false,
                "is_fan_club_promo_video": false,
                "is_public_chat_welcome_video": false,
                "is_shared_to_fb": false,
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_pivot_page_available": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "original_media": null
                },
                "merchandising_pill_info": null,
                "music_canonical_id": "18465450868099684",
                "music_info": null,
                "original_sound_info": {
                  "allow_creator_to_rename": true,
                  "audio_asset_id": "26325524987109477",
                  "audio_parts": [],
                  "audio_parts_by_filter": [],
                  "can_remix_be_shared_to_fb": true,
                  "can_remix_be_shared_to_fb_expansion": true,
                  "consumption_info": {
                    "is_bookmarked": false,
                    "is_trending_in_clips": false,
                    "should_mute_audio_reason": ""
                  },
                  "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT42.858665S\" FBManifestTimestamp=\"1775663938\" FBManifestIdentifier=\"FoTts50NKRaU8a/g8IbMBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT42.858665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1574618863631434a\" bandwidth=\"66331\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66331\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m78/AQOY5EGkoTBlLE1xh96dNgdWb1hLDnasjXImlcAczMGf9ccHVQerw2uLLOCBFI0HWu_2cKC2bpoloHn0IMPKnz6dpumou2-txXI1guw.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=6oMp0TM4ghcQ7kNvwEJJBv-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NzI5OTU1MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQyLCJiaXRyYXRlIjo2NjUzOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2-jpzrqbJ7HyEgZAdtv-QzaYwvOq219dUKogJw1ObIQg&amp;oe=69D8657A</BaseURL><SegmentBase indexRange=\"824-1119\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                  "duration_in_ms": 42859,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  },
                  "hide_remixing": false,
                  "ig_artist": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "18091046",
                    "id": "18091046",
                    "full_name": "National Geographic TV",
                    "is_private": false,
                    "is_verified": true,
                    "pk": "18091046",
                    "profile_pic_id": "3865691934048399589_18091046",
                    "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                    "username": "natgeotv"
                  },
                  "is_audio_automatically_attributed": false,
                  "is_eligible_for_audio_effects": true,
                  "is_explicit": false,
                  "is_original_audio_download_eligible": false,
                  "is_reuse_disabled": false,
                  "is_xpost_from_fb": false,
                  "oa_owner_is_music_artist": false,
                  "original_audio_subtype": "default",
                  "original_audio_title": "Original audio",
                  "original_media_id": "3870130142916282392",
                  "progressive_download_url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m69/AQM7ThcTIHPLAyeogCCOufQf3LVIp4H7hAm9NO8-Ggpf7f_9eHEowjA-rzNJ55UxkRqIjC9_SHQSFWCG_H-WTIcg.mp4?strext=1&_nc_cat=102&_nc_sid=8bf8fe&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=DS5DXaoFRxQQ7kNvwEK5y1E&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTc3Mjk5NTUxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af2sd1H404XQNcINU0e55DwWvkR3aC5wqoeWe4F3BtB3UA&oe=69DC67DC",
                  "should_mute_audio": false,
                  "time_created": 1775577610
                },
                "professional_clips_upsell_type": 0,
                "show_achievements": false
              },
              "clips_tab_pinned_user_ids": [],
              "clips_text": null,
              "coauthor_producer_can_see_organic_insights": false,
              "coauthor_producers": [
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "1260571151",
                  "id": "1260571151",
                  "full_name": "Steve Boyes",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "1260571151",
                  "profile_pic_id": "3019168329369961544_1260571151",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.2885-19/326167817_224566586583857_8010457387470001872_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=Tozf6TL7um4Q7kNvwEz7Adi&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GAntcBMxK5-7PcwAANCWjXyN3CpvbkULAAAB1501500j-ccb7-5&oh=00_Af1ixCmgqaGdYGf9dHjrvNy-qfB6rGBkTel1VsWlNRkCMA&oe=69DC5A68&_nc_sid=f514b5",
                  "username": "drsteveboyes"
                },
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "15473083628",
                  "id": "15473083628",
                  "full_name": "Nat Geo Documentary Films",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "15473083628",
                  "profile_pic_id": "3865721697802787660_15473083628",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658349376_18136815370515629_4670085031459966438_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MzEuYzIifQ&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=fMHK5S3K2SIQ7kNvwGZNSAK&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GECdPSetNIRlVm9AAOZNCsuXec9AbmNDAQAB1501500j-ccb7-5&oh=00_Af0fi76nHoKh3gwgamlu75huEqlvi154z64LJmCC6il1FA&oe=69DC50CE&_nc_sid=f514b5",
                  "username": "natgeodocs"
                }
              ],
              "code": "DW1dtwzDogY",
              "comment_count": 26,
              "comment_inform_treatment": {
                "action_type": null,
                "should_have_inform_treatment": false,
                "text": "",
                "url": null
              },
              "comment_likes_enabled": true,
              "comment_threading_enabled": true,
              "comments_disabled": null,
              "community_notes_info": {
                "enable_submission_friction": false,
                "has_viewer_submitted_note": false,
                "note_submission_disabled": false
              },
              "creative_config": null,
              "creator_viewer_insights": null,
              "crosspost": null,
              "crosspost_metadata": {
                "fb_crosspost_deeplink_profile_id": null,
                "fb_crosspost_fbid": null,
                "fb_downstream_use_xpost_metadata": {
                  "downstream_use_xpost_deny_reason": "NONE"
                },
                "is_feedback_aggregated": null,
                "th_unified_feedback_row_tap_target_url": null,
                "unified_feedback_enabled": null
              },
              "deleted_reason": 0,
              "dominant_color": null,
              "fb_comment_count": null,
              "fb_like_count": null,
              "fb_play_count": null,
              "filter_type": 0,
              "fundraiser_tag": {
                "beneficiary_name": null,
                "beneficiary_username": null,
                "can_viewer_donate": null,
                "can_viewer_remove_fundraiser_tag": null,
                "contextual_title_str": null,
                "formatted_amount_raised": null,
                "formatted_fundraiser_progress_info_text": null,
                "formatted_goal_amount": null,
                "fundraiser_id": null,
                "fundraiser_owner_username": null,
                "fundraiser_title": null,
                "fundraiser_type": null,
                "has_standalone_fundraiser": false,
                "is_media_owner_fundraiser_owner": null,
                "progress_str": null,
                "show_fundraiser_owner_attribution": null,
                "thumbnail_display_url": null
              },
              "has_audio": true,
              "has_hidden_comments": null,
              "has_liked": false,
              "has_more_comments": true,
              "has_reshares": null,
              "has_shared_to_fb": 0,
              "has_tagged_users": true,
              "has_viewer_saved": null,
              "hide_view_all_comment_entrypoint": true,
              "ig_media_sharing_disabled": false,
              "ig_play_count": 90594,
              "igbio_product": null,
              "inline_composer_display_condition": null,
              "1finline_composer_imp_trigger_time": null,
              "invited_coauthor_producers": [],
              "is_artist_pick": false,
              "is_auto_created": null,
              "is_comments_gif_composer_enabled": false,
              "is_currently_promoting_by_sponsor": null,
              "is_cutout_sticker_allowed": false,
              "is_dash_eligible": 1,
              "is_eligible_for_media_note_recs_nux": null,
              "is_fb_only": null,
              "is_in_profile_grid": false,
              "is_organic_product_tagging_eligible": true,
              "is_paid_partnership": false,
              "is_post_live": null,
              "is_post_live_clips_media": false,
              "is_quiet_post": false,
              "is_reshare_of_text_post_app_media_in_ig": false,
              "is_reuse_allowed": false,
              "is_shared_from_basel": null,
              "is_third_party_downloads_eligible": false,
              "is_visual_reply_commenter_notice_enabled": true,
              "like_and_view_counts_disabled": false,
              "like_count": 2446,
              "media_attributions_data": [],
              "location": null,
              "mashup_info": null,
              "max_num_visible_preview_comments": 2,
              "media_notice": null,
              "media_overlay_info": null,
              "music_metadata": null,
              "mv_link": null,
              "number_of_qualities": 8,
              "original_media_has_visual_reply_media": false,
              "owner": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "can_see_quiet_post_attribution": true,
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false
                },
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                "show_account_transparency_details": true,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "photo_of_you": false,
              "play_count": 90594,
              "preview": null,
              "product_collection_tag": null,
              "product_suggestions": null,
              "product_tags": null,
              "profile_grid_control_enabled": false,
              "reshare_count": 34,
              "share_count_disabled": false,
              "shimmed_mv_link": null,
              "should_request_ads": false,
              "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
              "social_context": [],
              "sticker_translations_enabled": null,
              "subscribe_cta_visible": false,
              "threads_xpost_deny_reason": null,
              "top_likers": [],
              "translated_video_subtitles": null,
              "upcoming_event": null,
              "usertags": null,
              "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
              "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT42.858665S\" FBManifestTimestamp=\"1775663938\" FBManifestIdentifier=\"FoTts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxuyAiO+R/f8C8tj75LGNngOuj/P7ycWqA9y7m8fe/KwD5vWV5eHXuwTGz/aeiPL9BOywuuiw8pkFhMm9muiUwwXYiYTB8eLRBdSw47qv6eEF8Kiugbjw9wX8/5f2u++DBiIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT42.858665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:77\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1402737425044451v\" bandwidth=\"317233\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1698787\" FBPlaybackResolutionMos=\"0:100,360:52.9,480:50.6,720:49.5,1080:50.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.9,480:85.3,720:80.7,1080:74.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQOGdNMWQBbGmop1wTfnJNcZrJjM-RZbo04RUpMidgrN7cCbTnBCBHG_sTTUwPhgq_lmerbiNscjCZfwTBM5vu7m4LrCagTFDWnY8Kg.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=2KFG_M66ls0Q7kNvwEPwkq8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6MzE3MjMzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3eeOwNyqjIG9s8nNAm9yO3K2Ox0mw6XmJ85D69-EJnfw&amp;oe=69DC40A0</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-49799\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-208542\" FBFirstSegmentRange=\"966-247509\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"247510-385329\" FBPrefetchSegmentRange=\"966-247509\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1587194629227116v\" bandwidth=\"468790\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2510372\" FBPlaybackResolutionMos=\"0:100,360:61.2,480:58.4,720:56.6,1080:56.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93,480:90.5,720:87,1080:80.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO4fAW6jsZktyhka_x4pqni2fSrM4WZ19ZfiwYMF0k15twnvPLVRK9YYkKKO2DC-nbX6M9Hldrt1o19vu2KnCzpqzb4BXcnhATnovM.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=ZxminLYGL5oQ7kNvwHsKn7v&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6NDY4NzkwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1GnIkJIsZGV_8vHz-unA7whXLXjxQFiooTBjg6pILArA&amp;oe=69DC34CE</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-59518\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-306781\" FBFirstSegmentRange=\"966-366475\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"366476-574112\" FBPrefetchSegmentRange=\"966-366475\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1464315522010166v\" bandwidth=\"605475\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3242319\" FBPlaybackResolutionMos=\"0:100,360:66.8,480:63.9,720:61.7,1080:60.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.4,480:93.6,720:91,1080:85.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNWIUlZ5RtWpksPYsme1w4ak26oqIsg1GEGTwAlkAAlSxkj1-ktCuYBgg9rhan_9IXHf3Nj9mWtFB_V-e4_rqjniSaUJ7B0hhUjveQ.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=fFEHyaEwOnYQ7kNvwFsy5Or&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6NjA1NDc1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3eSRZZMLE1_cQpo57h1nIbnzHHiicD6RIOxd4AvJDWVg&amp;oe=69DC31F9</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-64014\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-393243\" FBFirstSegmentRange=\"966-473018\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"473019-755190\" FBPrefetchSegmentRange=\"966-473018\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"937979245650903v\" bandwidth=\"795535\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"4260093\" FBPlaybackResolutionMos=\"0:100,360:72.3,480:69.5,720:66.8,1080:65.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.2,480:95.9,720:94.2,1080:89.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNfpBkN9CMvULQ6EVpudcT7DCS93b9UEarcbi6zbBRlocsJkVf_qtbW7xltNftr405n9BmfMK-m2kkFHHFFTtv28DYXCIPuct6mc8A.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=0qmKrnv_avsQ7kNvwEDhdEH&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6Nzk1NTM1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0EOB6RnCWsX-nAHYQ-m9030F7tNx1dyTz52rZsglx-4w&amp;oe=69DC618D</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-71155\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-511036\" FBFirstSegmentRange=\"966-619914\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"619915-1008569\" FBPrefetchSegmentRange=\"966-619914\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1670990313933368v\" bandwidth=\"991575\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"5309887\" FBPlaybackResolutionMos=\"0:100,360:75.6,480:73,720:70.2,1080:68.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.37,480:97.5,720:96.4,1080:92.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNvrK_9fibpJgyvh89Dp38zU-EX6F1OBen1OqZQTfSBy4vb9d7DLwLgIbZYLSRFmvsjhBnbh1MMiSJuXg60UvzunK89GyPA20T64Wo.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=fTTFZybJn4cQ7kNvwHx8aSS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6OTkxNTc1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3a_fNKJiZekum1R6bUtKf8Vdud4WTEIdaAoFqUqD7ySQ&amp;oe=69DC6999</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-79638\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-630699\" FBFirstSegmentRange=\"966-772409\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"772410-1269563\" FBPrefetchSegmentRange=\"966-772409\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1257150052744563v\" bandwidth=\"1267193\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"6785822\" FBPlaybackResolutionMos=\"0:100,360:79.3,480:76.4,720:73.7,1080:71.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.74,480:98.52,720:98.04,1080:94.7\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQOLGRWnhGyS5IkKESXH89_Ug_7md5_cqy_9A9z6dlC2Kpsj_RtUDRn4SscduxVpCPazuT6dqTAfp2vSXDZUYbUCDNNshGcWmp4_H-w.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=PSGXAhOAe_UQ7kNvwHDJXmn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6MTI2NzE5MywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1QftZXzk5C680f-z0rc5pPaEGcT6TuidkRW4Eaj_SxDA&amp;oe=69DC3C1E</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-92424\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-802161\" FBFirstSegmentRange=\"966-989081\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"989082-1629784\" FBPrefetchSegmentRange=\"966-989081\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1555067025470018v\" bandwidth=\"1672429\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"8955859\" FBPlaybackResolutionMos=\"0:100,360:83,480:79.9,720:76.5,1080:74\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.013,480:98.89,720:99.147,1080:96.7\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQPg1g1MXZMLyyGFJFNSIySweoI-n2OlhPwI4oZFM_v7tbsb8L33TtMCjElVzofpghBJlMpHNYJcoUvcNL6NUkK-e1fhspWCYJtYPgM.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=99MslkQfSCEQ7kNvwHmqoHY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6MTY3MjQyOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1dQnZ5Ijpi3v4WfcXVjnd7l8GfERttAXr8tmARTu-70g&amp;oe=69DC31E2</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-110324\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-1046676\" FBFirstSegmentRange=\"966-1290961\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1290962-2118706\" FBPrefetchSegmentRange=\"966-1290961\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"943324948295406v\" bandwidth=\"2560779\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"13712974\" FBPlaybackResolutionMos=\"0:100,360:87.4,480:84.9,720:81.3,1080:78.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.53,480:99.437,720:99.815,1080:99.657\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"12800/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMRGet-uKox1F9avdpzFcZPrKgfU90BikWDY2JGa9dix2Yxb8ZD4MegqQFm2IHpLcJSDNSpSYuIOd8aTiNFQH3opu7naa2XG5s4BZM.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=UVQsU-BuARYQ7kNvwH7pQ_L&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzcyOTk1NTEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0MiwiYml0cmF0ZSI6MjU2MDc3OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0CBthnqmx3XyVx1Mt0ZAnz8RMYinOyOkMwBmQZSNw0XQ&amp;oe=69DC5FCC</BaseURL><SegmentBase indexRange=\"826-965\" timescale=\"12800\" FBMinimumPrefetchRange=\"966-161757\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-1582988\" FBFirstSegmentRange=\"966-1991125\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1991126-3183998\" FBPrefetchSegmentRange=\"966-1991125\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"910625648637497a\" bandwidth=\"44024\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"44024\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"236823\" FBPaqMos=\"86.79\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQOYPACVfJrNpgB2CHkJlpxU9SoRgyZXw7LJt4DaqRb9rbbcvEreNTDlSboLL5LOOQ8qiemQ2DAKr9Oj3Sq3fA0Y2f77mIoZ_VKENRM.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=7XXcIcFCuVMQ7kNvwHfTPJj&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NzI5OTU1MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQyLCJiaXRyYXRlIjo0NDIwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0yc8w5PhGbYwd93voTnA0EYku_hbX8poVocmXeZ0rBNg&amp;oe=69DC4749</BaseURL><SegmentBase indexRange=\"837-976\" timescale=\"48000\" FBMinimumPrefetchRange=\"977-2032\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"977-14945\" FBFirstSegmentRange=\"977-28158\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28159-53909\" FBPrefetchSegmentRange=\"977-28158\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"844375788683318a\" bandwidth=\"78182\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"78182\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"419825\" FBPaqMos=\"86.55\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQM57z8XbJqNo9ZgfTzdo8RXGSAVf10kszRSDZHjUYelpGZFCSDZQ-4-_C3Raim4MelGPftniraV-4mzuXvBJO_O7gRk8ZEz_L_pU0U.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=7eUw8Lxl874Q7kNvwH1fmHp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NzI5OTU1MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQyLCJiaXRyYXRlIjo3ODM2NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1NIDONp0ChB5U5sNGA5UG4XuDQQgCfygZDFQjAey3gzw&amp;oe=69DC3AFB</BaseURL><SegmentBase indexRange=\"838-977\" timescale=\"48000\" FBMinimumPrefetchRange=\"978-2432\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-25109\" FBFirstSegmentRange=\"978-48974\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48975-94972\" FBPrefetchSegmentRange=\"978-48974\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1622490395470890a\" bandwidth=\"129661\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"129661\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"695607\" FBPaqMos=\"81.90\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMgkH6oPiXKQhz97dWWUkmSYmJpIfgGCK0wE1-dwUiRlQR7jPOlAUoQf77VpjCTkc3rghjBQGAVStffH8lAmTIv0CfvlIRYogowaRk.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=EJwhY-iMFskQ7kNvwHr39Q4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NzI5OTU1MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQyLCJiaXRyYXRlIjoxMjk4NDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2-N34RXqORn4njKHmNiHMoyGesd_N35HyfV2UHt9N28Q&amp;oe=69DC49F1</BaseURL><SegmentBase indexRange=\"833-972\" timescale=\"48000\" FBMinimumPrefetchRange=\"973-2301\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"973-41383\" FBFirstSegmentRange=\"973-84037\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"84038-159264\" FBPrefetchSegmentRange=\"973-84037\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1697361938284542a\" bandwidth=\"153164\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"153164\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"821523\" FBPaqMos=\"86.61\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPTlczgtPvR4taTmErIA0S7hcHV7bkj7vWg5tlEKumG9r4vmHP8EsaRoo81Gp-8qF2Kb4XN3LVyt3ZblTCPL2oraqW7yPlLRhnkoKE.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=K563mHQDc2sQ7kNvwEYvYkA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NzI5OTU1MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQyLCJiaXRyYXRlIjoxNTMzNDUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af20fKKp0lcl6tmt7FAOmA9XgLpnYd2yA3GfRYBbt_emMg&amp;oe=69DC45D9</BaseURL><SegmentBase indexRange=\"833-972\" timescale=\"48000\" FBMinimumPrefetchRange=\"973-2334\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"973-49615\" FBFirstSegmentRange=\"973-100520\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"100521-187345\" FBPrefetchSegmentRange=\"973-100520\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
              "1fvideo_duration": 42.858001708984375,
              "video_sticker_locales": [],
              "1fvideo_subtitles_confidence": null,
              "video_subtitles_enabled": null,
              "video_subtitles_locale": null,
              "video_subtitles_status": null,
              "video_subtitles_uri": null,
              "video_versions": [
                {
                  "height": 1280,
                  "id": "1291971733040522v",
                  "type": 101,
                  "url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQMDIiqH3xH4xZTXH1Cw9wtSUqWYARnbbHL-Q6QYhtDXcvddEN8pF1-ghYiBkwE7oskeyjNBYvSE3WVkPScCBVVxzTc5eiWY31CEetU.mp4?_nc_cat=107&_nc_sid=5e9851&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=hj-AFdWZE6UQ7kNvwGMHOt4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTc3Mjk5NTUxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=4fb413a7db533f85&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNjQyQkYxNzQwMjI2NDRFNDY5QUZCMjE2OTA5RDU5M192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzFGNDQ5NjM2ODg0OEU1RDZENjY1MTVCQkExMzg5REI5X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbaqJKvup3mPxUCKAJDMywXQEVrhR64UewYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2gEMYiQnhgTNQF-lMmxi4WzDfg8B0oDmxolQQL1_Zn6g&oe=69D85488",
                  "width": 720
                },
                {
                  "height": 1280,
                  "id": "1291971733040522v",
                  "type": 102,
                  "url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQMDIiqH3xH4xZTXH1Cw9wtSUqWYARnbbHL-Q6QYhtDXcvddEN8pF1-ghYiBkwE7oskeyjNBYvSE3WVkPScCBVVxzTc5eiWY31CEetU.mp4?_nc_cat=107&_nc_sid=5e9851&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=hj-AFdWZE6UQ7kNvwGMHOt4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTc3Mjk5NTUxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=4fb413a7db533f85&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNjQyQkYxNzQwMjI2NDRFNDY5QUZCMjE2OTA5RDU5M192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzFGNDQ5NjM2ODg0OEU1RDZENjY1MTVCQkExMzg5REI5X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbaqJKvup3mPxUCKAJDMywXQEVrhR64UewYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2gEMYiQnhgTNQF-lMmxi4WzDfg8B0oDmxolQQL1_Zn6g&oe=69D85488",
                  "width": 720
                },
                {
                  "height": 1280,
                  "id": "1291971733040522v",
                  "type": 103,
                  "url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQMDIiqH3xH4xZTXH1Cw9wtSUqWYARnbbHL-Q6QYhtDXcvddEN8pF1-ghYiBkwE7oskeyjNBYvSE3WVkPScCBVVxzTc5eiWY31CEetU.mp4?_nc_cat=107&_nc_sid=5e9851&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=hj-AFdWZE6UQ7kNvwGMHOt4&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTc3Mjk5NTUxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=4fb413a7db533f85&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNjQyQkYxNzQwMjI2NDRFNDY5QUZCMjE2OTA5RDU5M192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzFGNDQ5NjM2ODg0OEU1RDZENjY1MTVCQkExMzg5REI5X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbaqJKvup3mPxUCKAJDMywXQEVrhR64UewYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2gEMYiQnhgTNQF-lMmxi4WzDfg8B0oDmxolQQL1_Zn6g&oe=69D85488",
                  "width": 720
                }
              ],
              "view_count": null,
              "visibility": null,
              "visual_comment_reply_sticker_info": null,
              "visual_replies_info": null,
              "xpost_deny_reason": null,
              "xpost_deny_reason_enum": null,
              "floating_context_items": []
            }
          },
          {
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3869523223822719896_18091046",
              "id": "3869523223822719896_18091046",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "all_previous_submitters": null,
              "carousel_media": null,
              "carousel_media_count": null,
              "carousel_media_pending_post_count": null,
              "channel_tag_data": null,
              "content_views_count": null,
              "enable_media_notes_production": true,
              "enable_waist": true,
              "facepile_top_likers": null,
              "gen_ai_detection_method": {
                "detection_method": "NONE"
              },
              "has_delayed_metadata": false,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.71878-15/660135795_881793001577644_7641417558792209876_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=QghCk19eFR0Q7kNvwFXFkfL&_nc_oc=AdpIR7Igk9BG4ZrBOAoWg-LZxGoAUO3YQKu3IJjuJFpJv4v-XU_VPf9l2mr5NJGV-ac&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af1QpX5U4a_Tpd6-pKn2oXI_ZFjaUG_REHx2-TGxUaI6_Q&oe=69DC5813",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.71878-15/660135795_881793001577644_7641417558792209876_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=QghCk19eFR0Q7kNvwFXFkfL&_nc_oc=AdpIR7Igk9BG4ZrBOAoWg-LZxGoAUO3YQKu3IJjuJFpJv4v-XU_VPf9l2mr5NJGV-ac&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af1QpX5U4a_Tpd6-pKn2oXI_ZFjaUG_REHx2-TGxUaI6_Q&oe=69DC5813",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      18719,
                      37438,
                      56158
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-15/659641699_18583155493043047_3634661845755302072_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=105&ig_cache_key=Mzg2OTUyMzIyMzgyMjcxOTg5NjE4NTgzMTU1NDkwMDQzMDQ3.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=vCUNXTn5kcAQ7kNvwGJqg68&_nc_oc=AdqQn1v4X6VTPvcU0RLl3_FDIh7Hg7eJB0TMbRM93ewx0NMJbzIDya6aab5Dk--wIU0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af3tzdrRt-68YFAUZLlFFWJz7nwE12fbHR2zG_JAkGqF0A&oe=69DC61F1",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 315,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.7265142857142858,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 76.284
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "is_dismiss_pending_media_banner": null,
              "main_feed_carousel_starting_media_id": null,
              "media_cropping_info": null,
              "media_notes": {
                "is_fulfilled__(name:\"XDTMediaNotesResponse\")": true,
                "items": [
                  {
                    "audience": 7,
                    "1lcreated_at": 1775510140,
                    "has_translation": false,
                    "id": "17924460174101740",
                    "note_response_info": null,
                    "note_style": 13,
                    "reactions": [],
                    "text": "",
                    "user": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "787132",
                      "id": "787132",
                      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=XbeNvhLXv28Q7kNvwEyTvya&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3r23_FsnaV-pg8vreXK0O9xTHKfuPYXAbMgILhndg3gg&oe=69DC51E9&_nc_sid=f514b5",
                      "username": "natgeo"
                    },
                    "user_id": "787132"
                  }
                ]
              },
              "media_repost_count": 203,
              "media_reposter_bottomsheet_enabled": false,
              "media_type": 2,
              "open_carousel_submission_state": null,
              "open_to_public_submission_description_text": null,
              "organic_cta_info": null,
              "organic_cta_type": null,
              "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODQ0MjM0NTU5MDJjNGM1NmE0ZWNjY2E5Y2QzM2Y4YWUzODY5NTIzMjIzODIyNzE5ODk2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkzODA0M3wzODY5NTIzMjIzODIyNzE5ODk2fDM4ODQyNzE4NzYzfDVkNWZjM2VkOTA0YmEyOWRjMTk4ZDUwMGE3ZjVmNGJkOWQyMDMxYzllNjZiMmE1YjEwMDUxN2U0OTE5ZTUxYTIifSwic2lnbmF0dXJlIjoiIn0=",
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3869523223822719896",
              "product_type": "clips",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "save_count": null,
              "story_prompts": null,
              "1ltaken_at": 1775509220,
              "1ftallest_media_aspect_ratio": null,
              "timeline_pinned_user_ids": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_gifting_eligible": null,
                  "is_fan_club_referral_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false,
                  "is_viewer_unconnected": false,
                  "outgoing_request": false
                },
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "105432187515418",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 2,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "wearable_attribution_info": null,
              "accessibility_caption": null,
              "are_remixes_crosspostable": true,
              "attribution_content_url": null,
              "audience": null,
              "autodub_status": null,
              "boost_unavailable_identifier": null,
              "boost_unavailable_reason": null,
              "boost_upsell_banner_payload": null,
              "boosted_post_id": null,
              "boosted_status": null,
              "byoa_langs": null,
              "can_modify_carousel": null,
              "can_see_insights_as_brand": false,
              "can_view_more_preview_comments": false,
              "can_viewer_reshare": true,
              "can_viewer_save": true,
              "caption": {
                "__typename": "XDTCommentDict",
                "strong_id__": "17924459310101740",
                "pk": "17924459310101740",
                "bit_flags": 0,
                "content_type": "comment",
                "1lcreated_at": 1775509207,
                "1lcreated_at_utc": 1775509207,
                "did_report_as_spam": false,
                "has_translation": null,
                "is_covered": false,
                "is_ranked_comment": false,
                "media_id": "3869523223822719896",
                "private_reply_status": 0,
                "share_enabled": false,
                "status": "Active",
                "text": "Nat Geo Explorer-at-Large @jamescameronofficial and entomologist @drsammygrams may use different tools when it comes to telling stories, but they're both devoted to sharing the wonders of the natural world. Even down to the lives of the tiniest bees.\n\nNarrated by @bertiegregory, #SecretsOfTheBees is now streaming on @DisneyPlus and @hulu.",
                "type": 1,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "18091046",
                  "id": "18091046",
                  "1fcoeff_weight": null,
                  "fbid_v2": "17841401291380282",
                  "follower_count": 7301247,
                  "full_name": "National Geographic TV",
                  "has_onboarded_to_text_post_app": null,
                  "is_active": null,
                  "is_private": false,
                  "is_verified": true,
                  "pk": "18091046",
                  "profile_pic_id": "3865691934048399589_18091046",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                  "social_context": null,
                  "username": "natgeotv"
                }
              },
              "caption_add_on": null,
              "caption_is_edited": false,
              "carousel_last_edited_at": null,
              "client_cache_key": "Mzg2OTUyMzIyMzgyMjcxOTg5Ng==.3",
              "clips_attribution_info": null,
              "clips_karaoke_caption": null,
              "clips_captions": null,
              "clips_captions_translations_urls": null,
              "clips_metadata": {
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
                  "best_audio_cluster_id": "1618270416151995"
                },
                "audio_type": "original_sounds",
                "branded_content_tag_info": {
                  "can_add_tag": false
                },
                "clips_creation_entry_point": "",
                "content_appreciation_info": null,
                "contextual_highlight_info": null,
                "disable_use_in_clips_client_cache": false,
                "is_fan_club_promo_video": false,
                "is_public_chat_welcome_video": false,
                "is_shared_to_fb": false,
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_pivot_page_available": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "original_media": null
                },
                "merchandising_pill_info": null,
                "music_canonical_id": "18462154606102637",
                "music_info": null,
                "original_sound_info": {
                  "allow_creator_to_rename": true,
                  "audio_asset_id": "26678087618482030",
                  "audio_parts": [],
                  "audio_parts_by_filter": [],
                  "can_remix_be_shared_to_fb": true,
                  "can_remix_be_shared_to_fb_expansion": true,
                  "consumption_info": {
                    "is_bookmarked": false,
                    "is_trending_in_clips": false,
                    "should_mute_audio_reason": ""
                  },
                  "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT76.288002S\" FBManifestTimestamp=\"1775663938\" FBManifestIdentifier=\"FoTts50NKRbcu/fUjrjIAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT76.288002S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1003718645313262a\" bandwidth=\"66343\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66343\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m78/AQNk0bpw5VHFq16iAvmlMuFt6o2gCwtx9lSwOflKYPWEwV6OnsRCCUE-aUAwgAw2et5ShFEACUVvLCHuwr_xVlwdNP7KvbrnGiUk0tA.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=hmaWTsrNlhAQ7kNvwEFOZcW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NTUwMDI0MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc2LCJiaXRyYXRlIjo2NjQ4MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2ihEXTIcT1eWlYQdFtO_KultRrLIgp-pQ0PQCeTDiNWw&amp;oe=69D85FFC</BaseURL><SegmentBase indexRange=\"824-1323\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                  "duration_in_ms": 76284,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  },
                  "hide_remixing": false,
                  "ig_artist": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "18091046",
                    "id": "18091046",
                    "full_name": "National Geographic TV",
                    "is_private": false,
                    "is_verified": true,
                    "pk": "18091046",
                    "profile_pic_id": "3865691934048399589_18091046",
                    "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                    "username": "natgeotv"
                  },
                  "is_audio_automatically_attributed": false,
                  "is_eligible_for_audio_effects": true,
                  "is_explicit": false,
                  "is_original_audio_download_eligible": false,
                  "is_reuse_disabled": false,
                  "is_xpost_from_fb": false,
                  "oa_owner_is_music_artist": false,
                  "original_audio_subtype": "default",
                  "original_audio_title": "Original audio",
                  "original_media_id": "3869523223822719896",
                  "progressive_download_url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQOkbu5ehDmiyK2zxaI1XGAJQz8t3eHWY18fEzQirKHDAgoopdTqM2icJkMREVSNJLUL9AE05vIuzC088yDimxpC.mp4?_nc_cat=104&_nc_sid=8bf8fe&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=i8DVGeDP6_UQ7kNvwFL4Dr5&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTc1NTAwMjQxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af09OCTmchsns9g6FaoiNWBTpDFnTHMNrRiUKgQKmpJLuw&oe=69D83EE2",
                  "should_mute_audio": false,
                  "time_created": 1775509210
                },
                "professional_clips_upsell_type": 0,
                "show_achievements": false
              },
              "clips_tab_pinned_user_ids": [],
              "clips_text": null,
              "coauthor_producer_can_see_organic_insights": false,
              "coauthor_producers": [
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "10506924608",
                  "id": "10506924608",
                  "full_name": "James Cameron",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "10506924608",
                  "profile_pic_id": "1964371814524155358_10506924608",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=TYSekVkP8Y0Q7kNvwHqZRC3&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af2cwAkda8coeKXkzynw_dQZYixoRYe92B4SWk562HpXEw&oe=69DC6398&_nc_sid=f514b5",
                  "username": "jamescameronofficial"
                },
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "191074609",
                  "id": "191074609",
                  "full_name": "Hulu",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "191074609",
                  "profile_pic_id": "3756416250542097738_191074609",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/574400438_18538966897034610_4563057389814688225_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDc5LmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=MW84984-PUoQ7kNvwHG302U&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GLanPCJyhWaYF91BAOEpoBmFPFM-bmNDAQAB1501500j-ccb7-5&oh=00_Af3aqtznIhgr3GFIoBkE9rSYshfD9vJucrpPF6FdASgdRg&oe=69DC3924&_nc_sid=f514b5",
                  "username": "hulu"
                },
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "1628164961",
                  "id": "1628164961",
                  "full_name": "Samuel Ramsey",
                  "is_private": false,
                  "is_verified": false,
                  "pk": "1628164961",
                  "profile_pic_id": "2453903210149049965_1628164961",
                  "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.2885-19/128358315_385513056207772_7365182308375630471_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=SmRMTB50BroQ7kNvwHY1rQQ&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GKuXpgecg8VAn14BAIeSuHxJYjZmbkULAAAB1501500j-ccb7-5&oh=00_Af3Zl9Zl8pdYa2Kc-UZQDxA3qUDcj8WMYj8gYYBwVGF3fw&oe=69DC399C&_nc_sid=f514b5",
                  "username": "drsammygrams"
                }
              ],
              "code": "DWzTt7WE9uY",
              "comment_count": 169,
              "comment_inform_treatment": {
                "action_type": null,
                "should_have_inform_treatment": false,
                "text": "",
                "url": null
              },
              "comment_likes_enabled": true,
              "comment_threading_enabled": true,
              "comments_disabled": null,
              "community_notes_info": {
                "enable_submission_friction": false,
                "has_viewer_submitted_note": false,
                "note_submission_disabled": false
              },
              "creative_config": null,
              "creator_viewer_insights": null,
              "crosspost": null,
              "crosspost_metadata": {
                "fb_crosspost_deeplink_profile_id": null,
                "fb_crosspost_fbid": null,
                "fb_downstream_use_xpost_metadata": {
                  "downstream_use_xpost_deny_reason": "NONE"
                },
                "is_feedback_aggregated": null,
                "th_unified_feedback_row_tap_target_url": null,
                "unified_feedback_enabled": null
              },
              "deleted_reason": 0,
              "dominant_color": null,
              "fb_comment_count": null,
              "fb_like_count": null,
              "fb_play_count": null,
              "filter_type": 0,
              "fundraiser_tag": {
                "beneficiary_name": null,
                "beneficiary_username": null,
                "can_viewer_donate": null,
                "can_viewer_remove_fundraiser_tag": null,
                "contextual_title_str": null,
                "formatted_amount_raised": null,
                "formatted_fundraiser_progress_info_text": null,
                "formatted_goal_amount": null,
                "fundraiser_id": null,
                "fundraiser_owner_username": null,
                "fundraiser_title": null,
                "fundraiser_type": null,
                "has_standalone_fundraiser": false,
                "is_media_owner_fundraiser_owner": null,
                "progress_str": null,
                "show_fundraiser_owner_attribution": null,
                "thumbnail_display_url": null
              },
              "has_audio": true,
              "has_hidden_comments": null,
              "has_liked": false,
              "has_more_comments": true,
              "has_reshares": null,
              "has_shared_to_fb": 0,
              "has_tagged_users": true,
              "has_viewer_saved": null,
              "hide_view_all_comment_entrypoint": true,
              "ig_media_sharing_disabled": false,
              "ig_play_count": 418720,
              "igbio_product": null,
              "inline_composer_display_condition": null,
              "1finline_composer_imp_trigger_time": null,
              "invited_coauthor_producers": [],
              "is_artist_pick": false,
              "is_auto_created": null,
              "is_comments_gif_composer_enabled": false,
              "is_currently_promoting_by_sponsor": null,
              "is_cutout_sticker_allowed": false,
              "is_dash_eligible": 1,
              "is_eligible_for_media_note_recs_nux": null,
              "is_fb_only": null,
              "is_in_profile_grid": false,
              "is_organic_product_tagging_eligible": true,
              "is_paid_partnership": false,
              "is_post_live": null,
              "is_post_live_clips_media": false,
              "is_quiet_post": false,
              "is_reshare_of_text_post_app_media_in_ig": false,
              "is_reuse_allowed": false,
              "is_shared_from_basel": null,
              "is_third_party_downloads_eligible": false,
              "is_visual_reply_commenter_notice_enabled": true,
              "like_and_view_counts_disabled": false,
              "like_count": 5292,
              "media_attributions_data": [],
              "location": null,
              "mashup_info": null,
              "max_num_visible_preview_comments": 2,
              "media_notice": null,
              "media_overlay_info": null,
              "music_metadata": null,
              "mv_link": null,
              "number_of_qualities": 8,
              "original_media_has_visual_reply_media": false,
              "owner": {
                "__typename": "XDTUserDict",
                "strong_id__": "18091046",
                "id": "18091046",
                "can_see_quiet_post_attribution": true,
                "fbid_v2": "17841401291380282",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false
                },
                "full_name": "National Geographic TV",
                "has_anonymous_profile_picture": false,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "pk": "18091046",
                "profile_pic_id": "3865691934048399589_18091046",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                "show_account_transparency_details": true,
                "transparency_product_enabled": false,
                "username": "natgeotv"
              },
              "photo_of_you": false,
              "play_count": 418720,
              "preview": null,
              "product_collection_tag": null,
              "product_suggestions": null,
              "product_tags": null,
              "profile_grid_control_enabled": false,
              "reshare_count": 387,
              "share_count_disabled": false,
              "shimmed_mv_link": null,
              "should_request_ads": false,
              "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
              "social_context": [],
              "sticker_translations_enabled": null,
              "subscribe_cta_visible": false,
              "threads_xpost_deny_reason": null,
              "top_likers": [],
              "translated_video_subtitles": null,
              "upcoming_event": null,
              "usertags": null,
              "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
              "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT76.288002S\" FBManifestTimestamp=\"1775663938\" FBManifestIdentifier=\"FoTts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxqrAoZ2Ct/8CkML3joXRpQO23qnK3Mq6A6jGr4zUjsoE1orpn7Oh2gXO/IDizOmmBvbV2NezpsIGwqz18Yurzwa2/OD+vfr4Boqp+fiKiJoImIa95NHT1AjK8sCetNuYXiIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT76.288002S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"843171098800149v\" bandwidth=\"194840\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1857913\" FBPlaybackResolutionMos=\"0:100,360:66.6,480:63.3,720:61,1080:60.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:90.7,480:88.1,720:85.4,1080:80.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQPz-TYWZKhHKujnhjjzqs3F-7bBwrokJSTdTHWdUvxLHt9xgra4KSeolUMkQg3KnBYM86blYjQetg5XU8yNWSe6yHD1AuHaD1JNS1A.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=KYIF9jrq7zsQ7kNvwGp-wLs&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6MTk0ODQwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0xFvnE65Nrr4skhA1jIyHF9j6VAOp3WocENe0zoOuvog&amp;oe=69DC41AE</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-8871\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-42458\" FBFirstSegmentRange=\"1050-60638\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"60639-177174\" FBPrefetchSegmentRange=\"1050-60638\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1774226933554983v\" bandwidth=\"288859\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2754444\" FBPlaybackResolutionMos=\"0:100,360:71.7,480:68.5,720:65.6,1080:64.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:92.4,720:90.7,1080:85.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNeg91O530AzDjAwJkTj8rHJ-B_bFsbbmCVSt-2TOpPCxKXiaadGBqvsQi5VbxFIZY_EPydB9GCPD36nWxIFhCNGPmoS8Jma7KAutM.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=W9ejiNGJ60wQ7kNvwG3FCd3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6Mjg4ODU5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af185Tlyjq8by2hiDASiu078Plw4o5UigorMgBOEbtEvYw&amp;oe=69DC68E4</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-11439\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-60366\" FBFirstSegmentRange=\"1050-88853\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"88854-263434\" FBPrefetchSegmentRange=\"1050-88853\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1954836915167003v\" bandwidth=\"379504\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3618797\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:72.1,720:69,1080:67.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.9,480:94.6,720:93.4,1080:89.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMnFy1CMCq3yMGXIBCjXvL-RcMTCbkIyAgssp1k9dBixt2KTlMFvlE-ctDTMIyRYUXojdkPXIsvCBHF6vPg9jhwccpKGfED9JE-_JA.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=4t60Gv6Z0TEQ7kNvwFD4ebS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6Mzc5NTA0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2zn7xFISMRkmUi8JsbKRDj7dwX6dWXoclbnPxWm_h_SQ&amp;oe=69DC3994</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-13125\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-76931\" FBFirstSegmentRange=\"1050-116843\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"116844-350099\" FBPrefetchSegmentRange=\"1050-116843\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1288879433183636v\" bandwidth=\"506391\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"4828739\" FBPlaybackResolutionMos=\"0:100,360:78.4,480:75.2,720:72.1,1080:70.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.3,480:96.4,720:95.9,1080:92.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO_srPxb90oq5TachuG1QD6miSUp80tdIIosgBVV-TRJG7Lyb2qKhvqHL-n-0W5Nvanb9JLaTLxYzMYw4w-dxtK3YDEdqBbdR50pMI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=prsCcFta-OQQ7kNvwHobnWx&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6NTA2MzkxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1iL7su4UsdmgFVuNrPYYYHFiZgMDLEWD8s2FLycvQ6Fg&amp;oe=69DC4F37</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-15569\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-99355\" FBFirstSegmentRange=\"1050-157088\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"157089-474711\" FBPrefetchSegmentRange=\"1050-157088\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"927181046739080v\" bandwidth=\"670810\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"6396570\" FBPlaybackResolutionMos=\"0:100,360:81.7,480:77.7,720:74.6,1080:72.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.34,480:97.9,720:98,1080:94.7\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNu6JFcYyeTDfLZWZ9b--qBw42uhyLWG1ENylqyRxZxqsumIW_hhDRx1_UcuES8nDmuEj7_4ydp5CLTF7R_RjXIkRFDvuoyfXs7dzs.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=NfxeLQAC1HAQ7kNvwGgPgXq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6NjcwODEwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0BR8kfENOz04HXbIlFOfDkNX3_sHVQvce-6sOmjIj_DA&amp;oe=69DC5D63</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-17827\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-125568\" FBFirstSegmentRange=\"1050-208293\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"208294-642014\" FBPrefetchSegmentRange=\"1050-208293\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"26512994748341413v\" bandwidth=\"849067\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"8096351\" FBPlaybackResolutionMos=\"0:100,360:84,480:80.3,720:76.5,1080:74.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.84,480:98.66,720:99.026,1080:96.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQNS08UMbPPI3VnRD50HtYNtBrJ08P6O2ZQ_TQKpwFIjn1RbPsHdLkB80bxbpGQEqOgHxoSIRtINpWAfV56nYnkzh8lEXyrUHUy3HEs.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=2BOQ6DBwy9gQ7kNvwHhvq2U&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6ODQ5MDY3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af116rsF1vZ7VMCFPFU1pTegsFqomCKm0zWlPu0tiG2aQw&amp;oe=69DC362E</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-20313\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-156153\" FBFirstSegmentRange=\"1050-270641\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"270642-841596\" FBPrefetchSegmentRange=\"1050-270641\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1605860790706859v\" bandwidth=\"1086881\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"10364044\" FBPlaybackResolutionMos=\"0:100,360:86,480:82.6,720:78.5,1080:76\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.291,480:99.264,720:99.432,1080:98.15\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPJLNTdolrdK3V4UbY_3H7NpRRZ7-R2_gA9J0E31i1K35ZlGRDogFbZ1dRnig0GfS3JNMxL3cmWLbDvaJ2gPDCkS-TuQvZ6417sYa4.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=zY5pF3-KlkkQ7kNvwEb0WFy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6MTA4Njg4MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2veoPRWRBt32zHmRidhO2H5mhilFhkFfKdNbUdVdskLw&amp;oe=69DC68FB</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-22244\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-192422\" FBFirstSegmentRange=\"1050-348090\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"348091-1107483\" FBPrefetchSegmentRange=\"1050-348090\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2437954673287564v\" bandwidth=\"1544580\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"14728468\" FBPlaybackResolutionMos=\"0:100,360:88.3,480:85.5,720:81.8,1080:79.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.585,480:99.539,720:99.645,1080:99.681\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNs8YDzDDIYArK1ShOXSpzZ81XY37nrUfHFN3nioxnDpBAt0mN6x-pIru-ZXJFvszz1gkIGJurxF961rhl-0HcrcQdobnfYvgK4xds.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=EKEiJjP3uAcQ7kNvwGwWO7A&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NzU1MDAyNDEwNTMyNSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo3NiwiYml0cmF0ZSI6MTU0NDU4MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1uHMhTlNJkInQB7Cs9PR0YI_FnEIRVn086AfHPB6QIJg&amp;oe=69DC566B</BaseURL><SegmentBase indexRange=\"826-1049\" timescale=\"11988\" FBMinimumPrefetchRange=\"1050-30754\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1050-281784\" FBFirstSegmentRange=\"1050-518655\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"518656-1635542\" FBPrefetchSegmentRange=\"1050-518655\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1863313027672865a\" bandwidth=\"44032\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"44032\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"420947\" FBPaqMos=\"88.18\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOM3zAhoWEpu4rPedsdZYuDvx3aBV5PBLSm_9qzON3XRZKnZIlR6-VlEXOEhXOrnl8ykwd2LJkabveFI3W_k8xIuzlKMX53NukEev8.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=-xHYKx1e5H0Q7kNvwEyc5Xy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NTUwMDI0MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc2LCJiaXRyYXRlIjo0NDE0MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af11xH8nneWXeOjIs7mFRD3HZt9dglHqg48Zsmm83DHMkA&amp;oe=69DC4E11</BaseURL><SegmentBase indexRange=\"837-1060\" timescale=\"48000\" FBMinimumPrefetchRange=\"1061-2206\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1061-14556\" FBFirstSegmentRange=\"1061-26776\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"26777-53114\" FBPrefetchSegmentRange=\"1061-26776\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"973252015241115a\" bandwidth=\"70275\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"70275\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"671198\" FBPaqMos=\"88.64\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQNvuusLeQUSFLhw-x24E0VB3s-W9xsgwRGbFe0DRAseUlyTjzaao2MFMlkccXfLlkVT_BkoWaxOiNIRpbd7OfgsB_jgGSacQOIG05I.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=sj4x-t3_08sQ7kNvwE3199Z&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NTUwMDI0MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc2LCJiaXRyYXRlIjo3MDM4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0hIFPRW_TFEUxPCDDxQMnu3iuN9zeI-mx5KSPTVO9WQw&amp;oe=69DC66F4</BaseURL><SegmentBase indexRange=\"838-1061\" timescale=\"48000\" FBMinimumPrefetchRange=\"1062-2651\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1062-22598\" FBFirstSegmentRange=\"1062-41838\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"41839-84327\" FBPrefetchSegmentRange=\"1062-41838\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1834645167215995a\" bandwidth=\"103344\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"103344\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"986545\" FBPaqMos=\"82.39\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNTmzKmFZTFuyz-drkxDzXMkdD1MYwpPDgjQskB_durKBSP10aorzVqTIqYzZmOvgoTpg0kpspz-cUf52yV7y5e5kTntGE7ldKRAGk.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=j8JgmoKLJyAQ7kNvwGqYP3r&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NTUwMDI0MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc2LCJiaXRyYXRlIjoxMDM0NTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1PWUdzCKzQPoc5i4hnJORsc1LhwSRZir_PL9uCYdAmhQ&amp;oe=69DC5AD9</BaseURL><SegmentBase indexRange=\"833-1056\" timescale=\"48000\" FBMinimumPrefetchRange=\"1057-2494\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1057-33411\" FBFirstSegmentRange=\"1057-64110\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"64111-125417\" FBPrefetchSegmentRange=\"1057-64110\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2309113326283333a\" bandwidth=\"135087\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"135087\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1289245\" FBPaqMos=\"87.55\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPtp9Aus6HHAi4WAi_gY5jGUloCGw0Hlin654XaDay86BNkpmagVrbFUi-Phhb_lwb3Q5NpYyCsphga3vJyE_r6QEKDgHR4fVqKKvQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=koPGFXYnEToQ7kNvwF9fPkY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU3NTUwMDI0MTA1MzI1LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjc2LCJiaXRyYXRlIjoxMzUxOTcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2YYwSw0O8d7JC8dh7ErO6MBgVqp8NDttNQ4bC58wbOqg&amp;oe=69DC533A</BaseURL><SegmentBase indexRange=\"833-1056\" timescale=\"48000\" FBMinimumPrefetchRange=\"1057-2569\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1057-41439\" FBFirstSegmentRange=\"1057-80423\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"80424-162500\" FBPrefetchSegmentRange=\"1057-80423\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
              "1fvideo_duration": 76.28800201416016,
              "video_sticker_locales": [],
              "1fvideo_subtitles_confidence": null,
              "video_subtitles_enabled": null,
              "video_subtitles_locale": null,
              "video_subtitles_status": null,
              "video_subtitles_uri": null,
              "video_versions": [
                {
                  "height": 1280,
                  "id": "1317080756953513v",
                  "type": 101,
                  "url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQM-2HjWZuu7UNZN2-6YG4zRTwFn45lUxExvmiYPffq4VYirDis8znaROaIeZhf7vAf3MqKgaQyo8ZKmSp8ktGJ1nRHfAhgb4sTYPqU.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=cYcD7x2y1ekQ7kNvwECV2YY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTc1NTAwMjQxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=c7c51fdc0abd749c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84RTRDQjYxRjRDOTA0M0ZFNjQzNDFCQTdDMkI1OTI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0ZCNDc4MkQ5RjAwQzQwRjU3QkU3MDQ0MDU3NjQ2Nzk4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACba9cjj_ZLmPxUCKAJDMywXQFMSLQ5WBBkYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1C3YGGtFIsJxPlUUeNSMpdenkbueLhKnAwW8ihvXLe5w&oe=69D8557B",
                  "width": 720
                },
                {
                  "height": 1280,
                  "id": "1317080756953513v",
                  "type": 102,
                  "url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQM-2HjWZuu7UNZN2-6YG4zRTwFn45lUxExvmiYPffq4VYirDis8znaROaIeZhf7vAf3MqKgaQyo8ZKmSp8ktGJ1nRHfAhgb4sTYPqU.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=cYcD7x2y1ekQ7kNvwECV2YY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTc1NTAwMjQxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=c7c51fdc0abd749c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84RTRDQjYxRjRDOTA0M0ZFNjQzNDFCQTdDMkI1OTI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0ZCNDc4MkQ5RjAwQzQwRjU3QkU3MDQ0MDU3NjQ2Nzk4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACba9cjj_ZLmPxUCKAJDMywXQFMSLQ5WBBkYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1C3YGGtFIsJxPlUUeNSMpdenkbueLhKnAwW8ihvXLe5w&oe=69D8557B",
                  "width": 720
                },
                {
                  "height": 1280,
                  "id": "1317080756953513v",
                  "type": 103,
                  "url": "https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m86/AQM-2HjWZuu7UNZN2-6YG4zRTwFn45lUxExvmiYPffq4VYirDis8znaROaIeZhf7vAf3MqKgaQyo8ZKmSp8ktGJ1nRHfAhgb4sTYPqU.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_ohc=cYcD7x2y1ekQ7kNvwECV2YY&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTc1NTAwMjQxMDUzMjUsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=c7c51fdc0abd749c&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84RTRDQjYxRjRDOTA0M0ZFNjQzNDFCQTdDMkI1OTI4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0ZCNDc4MkQ5RjAwQzQwRjU3QkU3MDQ0MDU3NjQ2Nzk4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACba9cjj_ZLmPxUCKAJDMywXQFMSLQ5WBBkYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1C3YGGtFIsJxPlUUeNSMpdenkbueLhKnAwW8ihvXLe5w&oe=69D8557B",
                  "width": 720
                }
              ],
              "view_count": null,
              "visibility": null,
              "visual_comment_reply_sticker_info": null,
              "visual_replies_info": null,
              "xpost_deny_reason": null,
              "xpost_deny_reason_enum": null,
              "floating_context_items": []
            }
          },
          {
            "item_type": "media",
            "media": {
              "__typename": "XDTMediaDict",
              "strong_id__": "3868158180002863232_1029649300",
              "id": "3868158180002863232_1029649300",
              "is_fulfilled__(name:\"XDTMediaDict\")": true,
              "all_previous_submitters": null,
              "carousel_media": null,
              "carousel_media_count": null,
              "carousel_media_pending_post_count": null,
              "channel_tag_data": null,
              "content_views_count": null,
              "enable_media_notes_production": true,
              "enable_waist": true,
              "facepile_top_likers": null,
              "gen_ai_detection_method": {
                "detection_method": "NONE"
              },
              "has_delayed_metadata": false,
              "image_versions2": {
                "additional_candidates": {
                  "first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax3-2.cdninstagram.com/v/t51.71878-15/660296520_2570709223323021_5390155659312245773_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=103&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=XVzfHkwUZxAQ7kNvwFXHAwB&_nc_oc=AdquVXqDc8Xos-7MIeCD5miJooAGcmHtu_uZmeql7WoQg3mjNCfAY1UrbHKr1lkZQ_E&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af1nmwu5VEvwDktd6nsxGzIioZQTwsHAvH6BFYL1pRcVxQ&oe=69DC4348",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-lax3-2.cdninstagram.com/v/t51.71878-15/660296520_2570709223323021_5390155659312245773_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=103&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=XVzfHkwUZxAQ7kNvwFXHAwB&_nc_oc=AdquVXqDc8Xos-7MIeCD5miJooAGcmHtu_uZmeql7WoQg3mjNCfAY1UrbHKr1lkZQ_E&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af1nmwu5VEvwDktd6nsxGzIioZQTwsHAvH6BFYL1pRcVxQ&oe=69DC4348",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      14818,
                      29636,
                      44455
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/658976282_18586339588017301_888182851993674748_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=Mzg2ODE1ODE4MDAwMjg2MzIzMjE4NTg2MzM5NTg1MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=P86qpUBWrFEQ7kNvwEjNO3S&_nc_oc=Adr6dUUcG9lXoK_HlwTD12Fz4AeoPeEAtJTZ0BdoK6S6gMOgrjwz3dzI84ptXY6I0Xk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&oh=00_Af0s5CJl7dOykyJEb9NGeHvMQfy3tru427hc4mr_h1omfg&oe=69DC4CF7",
                    "width": 750
                  }
                ],
                "scrubber_spritesheet_info_candidates": {
                  "default": {
                    "file_size_kb": 388,
                    "max_thumbnails_per_sprite": 105,
                    "rendered_width": 96,
                    "sprite_height": 1232,
                    "sprite_width": 1500,
                    "1fthumbnail_duration": 0.3741809523809524,
                    "thumbnail_height": 176,
                    "thumbnail_width": 100,
                    "thumbnails_per_row": 15,
                    "total_thumbnail_num_per_sprite": 105,
                    "1fvideo_length": 39.289
                  }
                },
                "smart_thumbnail_enabled": null
              },
              "is_dismiss_pending_media_banner": null,
              "main_feed_carousel_starting_media_id": null,
              "media_cropping_info": null,
              "media_notes": {
                "is_fulfilled__(name:\"XDTMediaNotesResponse\")": true,
                "items": [
                  {
                    "audience": 7,
                    "1lcreated_at": 1775408480,
                    "has_translation": false,
                    "id": "18313925050257625",
                    "note_response_info": null,
                    "note_style": 13,
                    "reactions": [],
                    "text": "",
                    "user": {
                      "__typename": "XDTUserDict",
                      "strong_id__": "787132",
                      "id": "787132",
                      "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=XbeNvhLXv28Q7kNvwEyTvya&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3r23_FsnaV-pg8vreXK0O9xTHKfuPYXAbMgILhndg3gg&oe=69DC51E9&_nc_sid=f514b5",
                      "username": "natgeo"
                    },
                    "user_id": "787132"
                  }
                ]
              },
              "media_repost_count": 396,
              "media_reposter_bottomsheet_enabled": false,
              "media_type": 2,
              "open_carousel_submission_state": null,
              "open_to_public_submission_description_text": null,
              "organic_cta_info": null,
              "organic_cta_type": null,
              "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODQ0MjM0NTU5MDJjNGM1NmE0ZWNjY2E5Y2QzM2Y4YWUzODY4MTU4MTgwMDAyODYzMjMyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkzODA0M3wzODY4MTU4MTgwMDAyODYzMjMyfDM4ODQyNzE4NzYzfGMyMTBjNWY4OWM2NzY5NmRiMmMyYzE5ZTdhYTk4NGViNmZlYWIxMmNhMDMwNWZmZDg3MzFlY2IwOGM5NTEwODYifSwic2lnbmF0dXJlIjoiIn0=",
              "original_height": 1920,
              "original_width": 1080,
              "pk": "3868158180002863232",
              "product_type": "clips",
              "profile_grid_thumbnail_fitting_style": "UNSET",
              "save_count": null,
              "story_prompts": null,
              "1ltaken_at": 1775408402,
              "1ftallest_media_aspect_ratio": null,
              "timeline_pinned_user_ids": [],
              "user": {
                "__typename": "XDTUserDict",
                "strong_id__": "1029649300",
                "id": "1029649300",
                "account_type": 2,
                "all_media_count": null,
                "allowed_commenter_type": null,
                "can_boost_post": null,
                "can_see_organic_insights": null,
                "fan_club_info": {
                  "autosave_to_exclusive_highlight": null,
                  "connected_member_count": null,
                  "fan_club_id": null,
                  "fan_club_name": null,
                  "fan_consideration_page_revamp_eligiblity": null,
                  "has_enough_subscribers_for_ssc": null,
                  "is_fan_club_gifting_eligible": null,
                  "is_fan_club_referral_eligible": null,
                  "subscriber_count": null
                },
                "fbid_v2": "17841400519016088",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false,
                  "is_viewer_unconnected": false,
                  "outgoing_request": false
                },
                "full_name": "National Geographic Animals",
                "has_anonymous_profile_picture": false,
                "has_onboarded_to_text_post_app": null,
                "interop_messaging_user_fbid": "122600375795297",
                "is_active_on_text_post_app": true,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "liked_clips_count": null,
                "pk": "1029649300",
                "profile_pic_id": "3865698702530758137_1029649300",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=ic5ODsLE2O8Q7kNvwEdS3_S&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2F8WAQTcDlxiU_RlSQNKfNAJrKfg2tBjV1TGu1LcIE9Q&oe=69DC588C&_nc_sid=f514b5",
                "reel_auto_archive": null,
                "show_account_transparency_details": true,
                "show_insights_terms": null,
                "third_party_downloads_enabled": 1,
                "transparency_product_enabled": false,
                "username": "natgeoanimals"
              },
              "wearable_attribution_info": null,
              "accessibility_caption": null,
              "are_remixes_crosspostable": true,
              "attribution_content_url": null,
              "audience": null,
              "autodub_status": null,
              "boost_unavailable_identifier": null,
              "boost_unavailable_reason": null,
              "boost_upsell_banner_payload": null,
              "boosted_post_id": null,
              "boosted_status": null,
              "byoa_langs": null,
              "can_modify_carousel": null,
              "can_see_insights_as_brand": false,
              "can_view_more_preview_comments": false,
              "can_viewer_reshare": true,
              "can_viewer_save": true,
              "caption": {
                "__typename": "XDTCommentDict",
                "strong_id__": "18313924753257625",
                "pk": "18313924753257625",
                "bit_flags": 0,
                "content_type": "comment",
                "1lcreated_at": 1775408404,
                "1lcreated_at_utc": 1775408404,
                "did_report_as_spam": false,
                "has_translation": null,
                "is_covered": false,
                "is_ranked_comment": false,
                "media_id": "3868158180002863232",
                "private_reply_status": 0,
                "share_enabled": false,
                "status": "Active",
                "text": "Mothers will do anything to protect their young—even if it takes a little magic. By transporting sticks to an empty snail shell, this mom creates a hidden sanctuary, perfectly camouflaged to protect her cherished egg 🐝\n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
                "type": 1,
                "user": {
                  "__typename": "XDTUserDict",
                  "strong_id__": "1029649300",
                  "id": "1029649300",
                  "1fcoeff_weight": null,
                  "fbid_v2": "17841400519016088",
                  "follower_count": 15107687,
                  "full_name": "National Geographic Animals",
                  "has_onboarded_to_text_post_app": null,
                  "is_active": null,
                  "is_private": false,
                  "is_verified": true,
                  "pk": "1029649300",
                  "profile_pic_id": "3865698702530758137_1029649300",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=ic5ODsLE2O8Q7kNvwEdS3_S&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2F8WAQTcDlxiU_RlSQNKfNAJrKfg2tBjV1TGu1LcIE9Q&oe=69DC588C&_nc_sid=f514b5",
                  "social_context": null,
                  "username": "natgeoanimals"
                }
              },
              "caption_add_on": null,
              "caption_is_edited": false,
              "carousel_last_edited_at": null,
              "client_cache_key": "Mzg2ODE1ODE4MDAwMjg2MzIzMg==.3",
              "clips_attribution_info": null,
              "clips_karaoke_caption": null,
              "clips_captions": null,
              "clips_captions_translations_urls": null,
              "clips_metadata": {
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
                  "best_audio_cluster_id": "4302986679964253"
                },
                "audio_type": "original_sounds",
                "branded_content_tag_info": {
                  "can_add_tag": false
                },
                "clips_creation_entry_point": "",
                "content_appreciation_info": null,
                "contextual_highlight_info": null,
                "disable_use_in_clips_client_cache": false,
                "is_fan_club_promo_video": false,
                "is_public_chat_welcome_video": false,
                "is_shared_to_fb": false,
                "mashup_info": {
                  "can_toggle_mashups_allowed": false,
                  "has_been_mashed_up": false,
                  "has_nonmimicable_additional_audio": false,
                  "is_creator_requesting_mashup": false,
                  "is_light_weight_check": true,
                  "is_pivot_page_available": false,
                  "mashup_type": null,
                  "mashups_allowed": false,
                  "non_privacy_filtered_mashups_media_count": 0,
                  "original_media": null
                },
                "merchandising_pill_info": null,
                "music_canonical_id": "18577514941003946",
                "music_info": null,
                "original_sound_info": {
                  "allow_creator_to_rename": true,
                  "audio_asset_id": "26489030390784128",
                  "audio_parts": [],
                  "audio_parts_by_filter": [],
                  "can_remix_be_shared_to_fb": true,
                  "can_remix_be_shared_to_fb_expansion": true,
                  "consumption_info": {
                    "is_bookmarked": false,
                    "is_trending_in_clips": false,
                    "should_mute_audio_reason": ""
                  },
                  "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT39.296001S\" FBManifestTimestamp=\"1775663938\" FBManifestIdentifier=\"FoTts50NKRa455zeu57dBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT39.296001S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1612407460043228a\" bandwidth=\"66791\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66791\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m78/AQOtQYZds7o2tfj3Hp-tPbgkvNeOPSh7Dw2uwV7_MdhdFyvbc9023uPnZ49BKuqBZHQzslY14p11BQgH_FHqPiokE7HujG2otvbSPP0.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=HO-L93nMEAAQ7kNvwHX_cHE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0NTA1MjkxMTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM5LCJiaXRyYXRlIjo2NzAxMywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2_IBmO5D6eKxm8taF7DEQ07ggqc4ZMwSG2O7_WCKt_dQ&amp;oe=69D84CBC</BaseURL><SegmentBase indexRange=\"824-1095\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
                  "duration_in_ms": 39289,
                  "fb_downstream_use_xpost_metadata": {
                    "downstream_use_xpost_deny_reason": "NONE"
                  },
                  "hide_remixing": false,
                  "ig_artist": {
                    "__typename": "XDTUserDict",
                    "strong_id__": "1029649300",
                    "id": "1029649300",
                    "full_name": "National Geographic Animals",
                    "is_private": false,
                    "is_verified": true,
                    "pk": "1029649300",
                    "profile_pic_id": "3865698702530758137_1029649300",
                    "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=ic5ODsLE2O8Q7kNvwEdS3_S&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2F8WAQTcDlxiU_RlSQNKfNAJrKfg2tBjV1TGu1LcIE9Q&oe=69DC588C&_nc_sid=f514b5",
                    "username": "natgeoanimals"
                  },
                  "is_audio_automatically_attributed": false,
                  "is_eligible_for_audio_effects": true,
                  "is_explicit": false,
                  "is_original_audio_download_eligible": false,
                  "is_reuse_disabled": false,
                  "is_xpost_from_fb": false,
                  "oa_owner_is_music_artist": false,
                  "original_audio_subtype": "default",
                  "original_audio_title": "Original audio",
                  "original_media_id": "3868158180002863232",
                  "progressive_download_url": "https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQNFCwipYmnFikVRAdUSdNmrbr5W13cEhC355x3lpq1Fao8r_Bl6UtG-MJ4Kqcu5at1xXk6FPfGDBvNUdVcey1yR5w.mp4?_nc_cat=111&_nc_sid=8bf8fe&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_ohc=PHwzdNO7KjIQ7kNvwGUzgtQ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQ1MDUyOTExMTY2NDksImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af0xuFvGAoLGMME1ow6lfQx_zhBrypHB2nOs92lRd1OYPg&oe=69D86554",
                  "should_mute_audio": false,
                  "time_created": 1775408405
                },
                "professional_clips_upsell_type": 0,
                "show_achievements": false
              },
              "clips_tab_pinned_user_ids": [],
              "clips_text": null,
              "coauthor_producer_can_see_organic_insights": false,
              "coauthor_producers": [
                {
                  "__typename": "XDTUserDict",
                  "strong_id__": "18091046",
                  "id": "18091046",
                  "full_name": "National Geographic TV",
                  "is_private": false,
                  "is_verified": true,
                  "pk": "18091046",
                  "profile_pic_id": "3865691934048399589_18091046",
                  "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=zov5ST0QeW4Q7kNvwEirFGr&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af0ShrG6JmMlsQXUcRN_JwsKA_OpSq8-_We7rhOGDoi-6w&oe=69DC4D93&_nc_sid=f514b5",
                  "username": "natgeotv"
                }
              ],
              "code": "DWudV7OF5iA",
              "comment_count": 86,
              "comment_inform_treatment": {
                "action_type": null,
                "should_have_inform_treatment": false,
                "text": "",
                "url": null
              },
              "comment_likes_enabled": true,
              "comment_threading_enabled": true,
              "comments_disabled": null,
              "community_notes_info": {
                "enable_submission_friction": false,
                "has_viewer_submitted_note": false,
                "note_submission_disabled": false
              },
              "creative_config": null,
              "creator_viewer_insights": null,
              "crosspost": null,
              "crosspost_metadata": {
                "fb_crosspost_deeplink_profile_id": null,
                "fb_crosspost_fbid": null,
                "fb_downstream_use_xpost_metadata": {
                  "downstream_use_xpost_deny_reason": "NONE"
                },
                "is_feedback_aggregated": null,
                "th_unified_feedback_row_tap_target_url": null,
                "unified_feedback_enabled": null
              },
              "deleted_reason": 0,
              "dominant_color": null,
              "fb_comment_count": null,
              "fb_like_count": null,
              "fb_play_count": null,
              "filter_type": 0,
              "fundraiser_tag": {
                "beneficiary_name": null,
                "beneficiary_username": null,
                "can_viewer_donate": null,
                "can_viewer_remove_fundraiser_tag": null,
                "contextual_title_str": null,
                "formatted_amount_raised": null,
                "formatted_fundraiser_progress_info_text": null,
                "formatted_goal_amount": null,
                "fundraiser_id": null,
                "fundraiser_owner_username": null,
                "fundraiser_title": null,
                "fundraiser_type": null,
                "has_standalone_fundraiser": false,
                "is_media_owner_fundraiser_owner": null,
                "progress_str": null,
                "show_fundraiser_owner_attribution": null,
                "thumbnail_display_url": null
              },
              "has_audio": true,
              "has_hidden_comments": null,
              "has_liked": false,
              "has_more_comments": true,
              "has_reshares": null,
              "has_shared_to_fb": 0,
              "has_tagged_users": true,
              "has_viewer_saved": null,
              "hide_view_all_comment_entrypoint": true,
              "ig_media_sharing_disabled": false,
              "ig_play_count": 483070,
              "igbio_product": null,
              "inline_composer_display_condition": null,
              "1finline_composer_imp_trigger_time": null,
              "invited_coauthor_producers": [],
              "is_artist_pick": false,
              "is_auto_created": null,
              "is_comments_gif_composer_enabled": false,
              "is_currently_promoting_by_sponsor": null,
              "is_cutout_sticker_allowed": false,
              "is_dash_eligible": 1,
              "is_eligible_for_media_note_recs_nux": null,
              "is_fb_only": null,
              "is_in_profile_grid": false,
              "is_organic_product_tagging_eligible": true,
              "is_paid_partnership": false,
              "is_post_live": null,
              "is_post_live_clips_media": false,
              "is_quiet_post": false,
              "is_reshare_of_text_post_app_media_in_ig": false,
              "is_reuse_allowed": false,
              "is_shared_from_basel": null,
              "is_third_party_downloads_eligible": false,
              "is_visual_reply_commenter_notice_enabled": true,
              "like_and_view_counts_disabled": false,
              "like_count": 15733,
              "media_attributions_data": [],
              "location": null,
              "mashup_info": null,
              "max_num_visible_preview_comments": 2,
              "media_notice": null,
              "media_overlay_info": null,
              "music_metadata": null,
              "mv_link": null,
              "number_of_qualities": 8,
              "original_media_has_visual_reply_media": false,
              "owner": {
                "__typename": "XDTUserDict",
                "strong_id__": "1029649300",
                "id": "1029649300",
                "can_see_quiet_post_attribution": true,
                "fbid_v2": "17841400519016088",
                "feed_post_reshare_disabled": false,
                "friendship_status": {
                  "following": false,
                  "is_bestie": false,
                  "is_feed_favorite": false,
                  "is_restricted": false
                },
                "full_name": "National Geographic Animals",
                "has_anonymous_profile_picture": false,
                "is_favorite": false,
                "is_private": false,
                "is_unpublished": false,
                "is_verified": true,
                "pk": "1029649300",
                "profile_pic_id": "3865698702530758137_1029649300",
                "profile_pic_url": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHHEE9FrWHiHqYey__USKxBHsDJJ0pQM6DzK2mdxhgVcY-i9mbf46GEkKSo19SAbSA&_nc_ohc=ic5ODsLE2O8Q7kNvwEdS3_S&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&edm=APTNdPIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2F8WAQTcDlxiU_RlSQNKfNAJrKfg2tBjV1TGu1LcIE9Q&oe=69DC588C&_nc_sid=f514b5",
                "show_account_transparency_details": true,
                "transparency_product_enabled": false,
                "username": "natgeoanimals"
              },
              "photo_of_you": false,
              "play_count": 483070,
              "preview": null,
              "product_collection_tag": null,
              "product_suggestions": null,
              "product_tags": null,
              "profile_grid_control_enabled": false,
              "reshare_count": 1594,
              "share_count_disabled": false,
              "shimmed_mv_link": null,
              "should_request_ads": false,
              "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
              "social_context": [],
              "sticker_translations_enabled": null,
              "subscribe_cta_visible": false,
              "threads_xpost_deny_reason": null,
              "top_likers": [],
              "translated_video_subtitles": null,
              "upcoming_event": null,
              "usertags": null,
              "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
              "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT39.296001S\" FBManifestTimestamp=\"1775663938\" FBManifestIdentifier=\"FoTts50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxq6zxOHopqYD7Of4pqrSswOyjOT/8e/RA+K55tjk5rcE+rWN1o6gzATsme2KjezhBLq++4bQ9YkF8PPghd6H1QWew8KisIDqBfyk35+k3vgFqq3KhqqhgQeE2JKLho3ECCIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWBhQAEhQCAA==\"><Period id=\"0\" duration=\"PT39.296001S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:73.4\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1640477827289295v\" bandwidth=\"238071\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1169209\" FBPlaybackResolutionMos=\"0:100,360:54.7,480:52.3,720:51.8,1080:54.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.2,480:87.7,720:80.5,1080:73.2\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMYdlIOYRopJLGZB-8XT4OjQ3Gaux-SvqereEm9Crse4mxeOJ2phlHhDAiTD1Zomd45W7UzZO-VFahw1QrZlOSbyHvIDU9vGpH1xRQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=-cUkpJ-s4qAQ7kNvwHJJjSB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6MjM4MDcxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3CEwwGeGC-46IL6o5oQskcTdYmu8etCqqyzaHetUMlhA&amp;oe=69DC5FF2</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-10825\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-49830\" FBFirstSegmentRange=\"954-88393\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"88394-202077\" FBPrefetchSegmentRange=\"954-88393\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1341062344713846v\" bandwidth=\"320138\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1572253\" FBPlaybackResolutionMos=\"0:100,360:61.8,480:58.7,720:57.2,1080:59\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95,480:92.5,720:86.4,1080:79.3\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMRoYOtMdxVo9r1zZraz8nxDab92GomNB2k7FAduIbuVuheFZsTcxyJ58CoHOeEnW4LP0VZe4ngyulOaR36Ug9eybnL6pJf3p72vGA.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=Mn_kSLjTQ-UQ7kNvwElF1wc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6MzIwMTM4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0992Ruo5tvQBoVeFGiUgKjEUq_qlAGQqTvP7qecBLjGg&amp;oe=69DC4DF8</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-13162\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-64210\" FBFirstSegmentRange=\"954-115380\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"115381-276570\" FBPrefetchSegmentRange=\"954-115380\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1024468079903513v\" bandwidth=\"424936\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2086934\" FBPlaybackResolutionMos=\"0:100,360:68,480:64.9,720:62.9,1080:63.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95.3,720:91.8,1080:86.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMdr-8P-cynkYdYOIyhnu7Sx_LezM9Dtps__pB2a99G5kJbW7AMG5onnQ5v7XhZiLOJfrHdc2CWTLGH1ERq6Jo_4K0nSuzcFIqFNUw.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=4G083QPDsOIQ7kNvwGM3_UZ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6NDI0OTM2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1YLosRqNgRHaWe_X-N3G6aTn9eUDASzmAhaZsDkJ91NQ&amp;oe=69DC6304</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-16307\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-82272\" FBFirstSegmentRange=\"954-150854\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"150855-377259\" FBPrefetchSegmentRange=\"954-150854\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1594424741862648v\" bandwidth=\"531798\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2611748\" FBPlaybackResolutionMos=\"0:100,360:72.5,480:69.4,720:67,1080:66.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.7,720:94.6,1080:89.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPwgoCrByIIKcPIrRVkE20G8-SnJw7bnBCaivi1kgUTQKmIiEn6vz9WT4PXBFmeEyIStMeVbXmCAfWwZ24vcinmw9Ck3soc_LsNCXg.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=aXvwm64aRFQQ7kNvwH7dNSO&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6NTMxNzk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3DOAli4FJ3BwIlOHuF7NwjQnSeMH3vY0tIuuVfv2tIWw&amp;oe=69DC5723</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-19170\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-100098\" FBFirstSegmentRange=\"954-185417\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"185418-474658\" FBPrefetchSegmentRange=\"954-185417\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"957989543418358v\" bandwidth=\"703094\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3453011\" FBPlaybackResolutionMos=\"0:100,360:76.9,480:74.1,720:71.4,1080:70.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.57,480:97.8,720:96.4,1080:93.1\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMq3iEVymMiO1HTqoqMZfy1PrEBju-1-a9iUKQGNk_-Ewuu3UOovnAXVyx0BsCN2hfwKULKUBWYtVO2pSRGLDB9OEZIa_j_1VlkPis.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=KfiJLu3-79EQ7kNvwGvn9_F&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6NzAzMDk0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1AXhg--mtp2TUKA_BJ7UtHOOt1IaGgD7oOtl5C1RjXhA&amp;oe=69DC572F</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-22636\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-126587\" FBFirstSegmentRange=\"954-239272\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"239273-631870\" FBPrefetchSegmentRange=\"954-239272\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"928654709787863v\" bandwidth=\"885647\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4349558\" FBPlaybackResolutionMos=\"0:100,360:81,480:77.3,720:74.7,1080:73.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.01,480:98.68,720:97.5,1080:95.3\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPK_n0X3lwhqcbxSI-wCWLG1s8py4m-FxpaSUYd5RASdEqLxG3YbarGpbkW1JQCRJGT_AI_p2qH7BQ3TirJ9QS77qpeIel0L-hLt60.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=jsAf3kSHXjAQ7kNvwF4vtY-&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6ODg1NjQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2-ZJ3OHxlHqyj7nR1_SfXxYj6dVVsgyEp7aSL1aArijw&amp;oe=69DC46D9</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-26336\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-155059\" FBFirstSegmentRange=\"954-296585\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"296586-804115\" FBPrefetchSegmentRange=\"954-296585\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1248612047441521v\" bandwidth=\"1187459\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"5831807\" FBPlaybackResolutionMos=\"0:100,360:85.3,480:81.9,720:78.1,1080:76.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.194,480:98.94,720:98.43,1080:97.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m367/AQPASPymy5mKQ0tYKoOVl3mQos_aYNjUXjIEg1H7bSOq_JoN0kgPYNShxryCm84HvdjjOBKkBuwrpeGwV6kCD7Xy3i6K0UR0P_kq-LI.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax7-1.cdninstagram.com&amp;_nc_ohc=W26rHquAvrQQ7kNvwGNYkeQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6MTE4NzQ1OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1tQ55vhxsrHaOCfcRj_dVu1sEVc5FCYEAF6veLKlfmCw&amp;oe=69DC3702</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-31170\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-200734\" FBFirstSegmentRange=\"954-389084\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"389085-1093446\" FBPrefetchSegmentRange=\"954-389084\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2401557550355970v\" bandwidth=\"1669406\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"8198724\" FBPlaybackResolutionMos=\"0:100,360:88.5,480:85.6,720:82,1080:80.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.331,480:99.129,720:98.71,1080:98.29\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMEZgJYhw85Gx27HWFWNFyG12sN8ribE3ND3VBjs-eResuNQqEcnl-VkzFoGx1wnEUwCcWonFrWToozdvxbTqsgGk1Q7h8ngFvzjpA.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=YgqBpR6IB-0Q7kNvwGOhgi6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDUwNTI5MTExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjozOSwiYml0cmF0ZSI6MTY2OTQwNiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1X8duxt41Kb0lZDRjbMqkIVoeEt9qMeQPZC6DN4zo3Jg&amp;oe=69DC5BF0</BaseURL><SegmentBase indexRange=\"826-953\" timescale=\"11988\" FBMinimumPrefetchRange=\"954-41706\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"954-279953\" FBFirstSegmentRange=\"954-545127\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"545128-1546559\" FBPrefetchSegmentRange=\"954-545127\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1293577399414141a\" bandwidth=\"47184\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"47184\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"232728\" FBPaqMos=\"87.10\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMSaknBTB6TWJeYMHopbnIpzMtayEsrXRyWMucvtUT8zbB6IMHAU3I186DfxYC6lx_QOnxkSPQhE9tGY9mNXXpbs8RFV78_bnlLIHU.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=idAXc0A04DkQ7kNvwFy8grY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0NTA1MjkxMTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM5LCJiaXRyYXRlIjo0NzM3OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1JP73GHlEaTYqzX5iiYkcOGIO_TCSWYtXx7Xbvj-djzw&amp;oe=69DC3A9C</BaseURL><SegmentBase indexRange=\"837-964\" timescale=\"48000\" FBMinimumPrefetchRange=\"965-1996\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"965-15374\" FBFirstSegmentRange=\"965-29923\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"29924-59459\" FBPrefetchSegmentRange=\"965-29923\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1973096439958357a\" bandwidth=\"71615\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71615\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"352738\" FBPaqMos=\"90.18\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMgvI35iHYp9GXqUXcnvJ0LVYzFm_eRUzOLM5xGbTXPf69JyJeC0a8Nh24Tn255KE3gz3kezSm05Iz5TNAXdoyCJrnv1PJTR8WFYEo.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-2.cdninstagram.com&amp;_nc_ohc=IeYo5jtZojoQ7kNvwHr4quX&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0NTA1MjkxMTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM5LCJiaXRyYXRlIjo3MTgxMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2-xnof9p6pbxHYZK2527Gz6cBIQOv4ZRAVlvBf9qh7hg&amp;oe=69DC5D7B</BaseURL><SegmentBase indexRange=\"838-965\" timescale=\"48000\" FBMinimumPrefetchRange=\"966-2402\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"966-24075\" FBFirstSegmentRange=\"966-46798\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"46799-90733\" FBPrefetchSegmentRange=\"966-46798\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1429186882269085a\" bandwidth=\"104262\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"104262\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"513094\" FBPaqMos=\"79.75\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOzNcRo2qH01sKJrRGdvVrFZOBCHvxjPgomyBWYemHkW7p9uhDCbNhYMjzdscm4txHXmd2OZjkM74HC8QbdoP9EtqNZ6v9gvyHGYPc.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=CivA6GqQnCcQ7kNvwFdtBak&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0NTA1MjkxMTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM5LCJiaXRyYXRlIjoxMDQ0NTcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1On5HNH9OmXt5DNaH2xOyi-PSNbiLX3hz8VDZHQLcGUA&amp;oe=69DC52AB</BaseURL><SegmentBase indexRange=\"833-960\" timescale=\"48000\" FBMinimumPrefetchRange=\"961-2270\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-34047\" FBFirstSegmentRange=\"961-68001\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"68002-132847\" FBPrefetchSegmentRange=\"961-68001\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1672877447047486a\" bandwidth=\"139525\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"139525\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"686305\" FBPaqMos=\"84.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOvkt-Uaivfwc-kUWQMhkQ7CXomohoYg2vwE770zn0irEMxAyk150si2_EgW8s-v7LgQPK7KXQSkUoqoUm7PMlXJ3dBknm2qUqsRDQ.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-lax3-1.cdninstagram.com&amp;_nc_ohc=UTBb5_vnbHAQ7kNvwEEiwDE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0NTA1MjkxMTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjM5LCJiaXRyYXRlIjoxMzk3MjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3oSnAlfdqa-gIYFhWk8AwFeMPz4o-d-YC0LFP5XqHKCg&amp;oe=69DC6803</BaseURL><SegmentBase indexRange=\"833-960\" timescale=\"48000\" FBMinimumPrefetchRange=\"961-2287\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"961-47794\" FBFirstSegmentRange=\"961-92541\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"92542-180101\" FBPrefetchSegmentRange=\"961-92541\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
              "1fvideo_duration": 39.29600143432617,
              "video_sticker_locales": [],
              "1fvideo_subtitles_confidence": null,
              "video_subtitles_enabled": null,
              "video_subtitles_locale": null,
              "video_subtitles_status": null,
              "video_subtitles_uri": null,
              "video_versions": [
                {
                  "height": 1280,
                  "id": "920722424142526v",
                  "type": 101,
                  "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQO1zmqaB6XKqAI5VKWg2QWL_pnUhtp2ls5xJWFUNDOgAr5GzOPAMd4ahd2QmG0Ezy_LkepUd1vE9b0ZJTujt0NGVQWp_NELmqNQmzM.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=MhVKSGH97-UQ7kNvwHzW9YR&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ1MDUyOTExMTY2NDksImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=897bc3105a63c3c0&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GOTRBNjI4NzVGREM4RDM1MjBGNkNDRUM4NUQ2QzlBNF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U0NEREMDA5RDEwRDY2QTM0QTczQjlFQzAwNkZCODlFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSwfXf4OHkPxUCKAJDMywXQEOk_fO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1x5mw1ZPbqxMMpCyTP524ztCb6UXaaQ-ybs419_vNoMw&oe=69D858D9",
                  "width": 720
                },
                {
                  "height": 1280,
                  "id": "920722424142526v",
                  "type": 102,
                  "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQO1zmqaB6XKqAI5VKWg2QWL_pnUhtp2ls5xJWFUNDOgAr5GzOPAMd4ahd2QmG0Ezy_LkepUd1vE9b0ZJTujt0NGVQWp_NELmqNQmzM.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=MhVKSGH97-UQ7kNvwHzW9YR&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ1MDUyOTExMTY2NDksImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=897bc3105a63c3c0&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GOTRBNjI4NzVGREM4RDM1MjBGNkNDRUM4NUQ2QzlBNF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U0NEREMDA5RDEwRDY2QTM0QTczQjlFQzAwNkZCODlFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSwfXf4OHkPxUCKAJDMywXQEOk_fO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1x5mw1ZPbqxMMpCyTP524ztCb6UXaaQ-ybs419_vNoMw&oe=69D858D9",
                  "width": 720
                },
                {
                  "height": 1280,
                  "id": "920722424142526v",
                  "type": 103,
                  "url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQO1zmqaB6XKqAI5VKWg2QWL_pnUhtp2ls5xJWFUNDOgAr5GzOPAMd4ahd2QmG0Ezy_LkepUd1vE9b0ZJTujt0NGVQWp_NELmqNQmzM.mp4?_nc_cat=108&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=MhVKSGH97-UQ7kNvwHzW9YR&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ1MDUyOTExMTY2NDksImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=897bc3105a63c3c0&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GOTRBNjI4NzVGREM4RDM1MjBGNkNDRUM4NUQ2QzlBNF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0U0NEREMDA5RDEwRDY2QTM0QTczQjlFQzAwNkZCODlFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSwfXf4OHkPxUCKAJDMywXQEOk_fO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=5CnQ53P3uCZYCY7b5DBQEA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1x5mw1ZPbqxMMpCyTP524ztCb6UXaaQ-ybs419_vNoMw&oe=69D858D9",
                  "width": 720
                }
              ],
              "view_count": null,
              "visibility": null,
              "visual_comment_reply_sticker_info": null,
              "visual_replies_info": null,
              "xpost_deny_reason": null,
              "xpost_deny_reason_enum": null,
              "floating_context_items": []
            }
          }
        ],
        "repost_next_max_id": "QVFBOWZ5NGFqUHRDdk1jc0ZXSTBKbzE0YnpFdjVkMmdkM3R2bnZQRlFBWUlWZm1RWmhkZzNrRUJDQ3pyZGNwd3lETkFRaElnMVFqblhfRzF1OU5HNVF2SQ==",
        "repost_more_available": true
      }
    }
  },
  "extensions": {
    "is_final": true,
    "fulfilled_payloads": [
      {
        "label": "DeferrableSharedMedia",
        "path": [
          "1$fetch__XDTUserDict(id:$id)",
          "1$user_reposts_timeline(max_id:$max_id)",
          "repost_grid_items"
        ]
      },
      {
        "label": "DeferrableSharedMedia",
        "path": [
          "1$fetch__XDTUserDict(id:$id)",
          "1$user_reposts_timeline(max_id:$max_id)",
          "repost_grid_items"
        ]
      },
      {
        "label": "DeferrableSharedMedia",
        "path": [
          "1$fetch__XDTUserDict(id:$id)",
          "1$user_reposts_timeline(max_id:$max_id)",
          "repost_grid_items"
        ]
      }
    ],
    "server_metadata": {
      "request_start_time_ms": 1775663937455,
      "time_at_flush_ms": 1775663938570
    }
  },
  "status": "ok"
}
```

</details>

---

### GET /gql/user/web_profile_info

Get user profile info by user id (GraphQL web_profile_info)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/gql/user/web_profile_info?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_web_profile_info_gql(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/gql/user/web_profile_info",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/gql/user/web_profile_info?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "friendship_status": {
    "following": false,
    "blocking": false,
    "is_feed_favorite": false,
    "outgoing_request": false,
    "followed_by": false,
    "incoming_request": false,
    "is_restricted": false,
    "is_bestie": false,
    "muting": false,
    "is_muting_reel": false
  },
  "gating": null,
  "fbid_v2": "17841400573960012",
  "is_memorialized": false,
  "is_private": false,
  "has_story_archive": null,
  "is_coppa_enforced": false,
  "supervision_info": null,
  "is_regulated_c18": false,
  "regulated_news_in_locations": null,
  "bio_links": [
    {
      "image_url": "",
      "is_pinned": false,
      "link_type": "external",
      "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPOTM2NjE5NzQzMzkyNDU5AAGnIeDI4ZFCOrA4uKCKX6tF3TTYnnAI7a1PmakeAPRsB3XC_RJxEmeO73K1Aic_aem_0AvqmIKZ6U_CXAKCOoXUcg&e=AT7LtSS3WGey1sU47pRgHhcg9seeUul0bh6Uptl0MqT6fR3Dg04elSzjydX53qkpICU4CB75TVAgfdmLvKPejkiKuRUNrTzaY1fQx4lj4effVvpILmdfvrSNVpYez8vNQu6-zFZlQYz2",
      "media_accent_color_hex": "",
      "media_type": "none",
      "title": "",
      "url": "http://visitstore.bio/natgeo",
      "creation_source": "NONE"
    }
  ],
  "linked_fb_info": null,
  "text_post_app_badge_label": "natgeo",
  "show_text_post_app_badge": true,
  "username": "natgeo",
  "pk": "787132",
  "live_broadcast_visibility": null,
  "live_broadcast_id": null,
  "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_cat=1&ccb=7-5&_nc_sid=f7ccc5&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwGwXgyU&_nc_oc=Adqm-sRgNOPeSIwqV4OkBYYtp4x64TpsVez4SebxkOkL6jxDNtvl9CsEYwZp8ZocOoI&_nc_zt=24&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_gid=fimGcT5oS1GSyXxb7jLF8A&_nc_ss=7a3a8&oh=00_Af0N0ctG77XzafBtBZhtRBhfjvX1qeYHL1-PXnXqaHUkQA&oe=69DC51E9",
  "hd_profile_pic_url_info": {
    "url": "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?_nc_cat=1&ccb=7-5&_nc_sid=bf7eb4&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwGwXgyU&_nc_oc=Adqm-sRgNOPeSIwqV4OkBYYtp4x64TpsVez4SebxkOkL6jxDNtvl9CsEYwZp8ZocOoI&_nc_zt=24&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_gid=fimGcT5oS1GSyXxb7jLF8A&_nc_ss=7a3a8&oh=00_Af0r-X8a5ROPzCf_Mpw957V_15Ada-QAINDV1PwloU2zwQ&oe=69DC51E9"
  },
  "is_unpublished": false,
  "latest_reel_media": 1775659002,
  "has_profile_pic": null,
  "profile_pic_genai_tool_info": null,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "full_name": "National Geographic",
  "is_verified": true,
  "show_account_transparency_details": true,
  "account_type": 2,
  "follower_count": 274988518,
  "mutual_followers_count": 0,
  "profile_context_links_with_user_ids": [],
  "profile_context_facepile_users": [],
  "address_street": "",
  "city_name": "",
  "is_business": true,
  "zip": "",
  "biography_with_entities": {
    "entities": []
  },
  "category": "",
  "should_show_category": false,
  "is_ring_creator": false,
  "show_ring_award": false,
  "ring_creator_metadata": {
    "profile_background_color": null
  },
  "account_badges": [],
  "ai_agent_type": null,
  "external_lynx_url": null,
  "external_url": null,
  "pronouns": [],
  "transparency_label": null,
  "transparency_product": null,
  "hide_creator_marketplace_badge": false,
  "id": "787132",
  "has_chaining": true,
  "remove_message_entrypoint": false,
  "is_embeds_disabled": false,
  "is_cannes": false,
  "is_professional_account": null,
  "following_count": 193,
  "media_count": 31529,
  "total_clips_count": 1,
  "latest_besties_reel_media": null,
  "reel_media_seen_timestamp": null
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-gql){ target=_blank }
