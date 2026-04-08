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
        "strong_id__": "4290885509",
        "id": "4290885509",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841404245296360",
        "full_name": "Teresa Wrigley",
        "has_anonymous_profile_picture": false,
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
        "pk": "4290885509",
        "profile_pic_id": "3758391744724372864_4290885509",
        "profile_pic_url": "https://scontent-mxp2-1.cdninstagram.com/v/t51.82787-19/573215496_18412239754141510_3751195623028207489_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mxp2-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHISV3BtGlqyoBQdU_WOPlaLICnjLPPHQkiDXsnoQaSQ5JrD9zxg0DedpL62x5bMRc&_nc_ohc=UPa13xRcc7sQ7kNvwHtZyC8&_nc_gid=2xE-XkAcBdTOsPpnbcU19Q&edm=AIfao94BAAAA&ccb=7-5&ig_cache_key=GAiTKiJGnxCi1WlBAIGvmGGL7A40bmNDAQAB1501500j-ccb7-5&oh=00_Af1EZQ4QwmTCrhz_rEXYuB-0mJDfDPsKobSCo1Azq711mg&oe=69DC24E4&_nc_sid=9f8d40",
        "reel_auto_archive": null,
        "username": "tajw60",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "37070197889",
        "id": "37070197889",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841437136683774",
        "full_name": "Soumi Biswas",
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
        "pk": "37070197889",
        "profile_pic_id": "3866974006172385404_37070197889",
        "profile_pic_url": "https://scontent-mxp2-1.cdninstagram.com/v/t51.82787-19/658839282_18075290666237890_8598075638626610861_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mxp2-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHISV3BtGlqyoBQdU_WOPlaLICnjLPPHQkiDXsnoQaSQ5JrD9zxg0DedpL62x5bMRc&_nc_ohc=vyNeWBiMp6oQ7kNvwEEW2tB&_nc_gid=2xE-XkAcBdTOsPpnbcU19Q&edm=AIfao94BAAAA&ccb=7-5&ig_cache_key=GPIWRSfCf1_PYTdAAK1uRyA9gFJ3bmNDAQAB1501500j-ccb7-5&oh=00_Af17NNwQBEckHhqr6p4XEAPpHR5k7-5CQn2gSwc3e1bnRg&oe=69DC33AB&_nc_sid=9f8d40",
        "reel_auto_archive": null,
        "username": "soumiforyou",
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
    "users": [
      {
        "__typename": "XDTUserDict",
        "strong_id__": "14331657700",
        "id": "14331657700",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841414211021457",
        "full_name": "ナショナルジオグラフィック日本版",
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
          "outgoing_request": false,
          "is_viewer_unconnected": false,
          "reachability_status": 0
        },
        "pk": "14331657700",
        "profile_pic_id": "2073867961613189688_14331657700",
        "profile_pic_url": "https://scontent-sof1-1.cdninstagram.com/v/t51.2885-19/65160972_483182759115510_2590728031043584000_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MDAuZXhwZXJpbWVudGFsIn0&_nc_ht=scontent-sof1-1.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gHKeXz1w_yQTStnJf9E8fjENbDzKBnOvnweklraghubzJ1xcV892yRn8jN8iF1fzjk&_nc_ohc=7ujGFVqjyKQQ7kNvwHjqIvv&_nc_gid=Sq-jHfgMFoFVlXK5hIbEeg&edm=AFFDd_gBAAAA&ccb=7-5&ig_cache_key=GAxH4gP2_rfAc7cBAAAAAABrHfQjbkULAAAB1501500j-ccb7-5&oh=00_Af3LkNy4H4uQAitb7UZLaP0VaOgXHtP3qjMrubbLJu_lQQ&oe=69DC21ED&_nc_sid=421beb",
        "reel_auto_archive": null,
        "username": "natgeomagjp",
        "all_media_count": null
      },
      {
        "__typename": "XDTUserDict",
        "strong_id__": "8958735",
        "id": "8958735",
        "is_fulfilled__(name:\"XDTUserDict\")": true,
        "allowed_commenter_type": null,
        "fbid_v2": "17841401882050139",
        "full_name": "Christie Hemm Klok",
        "has_anonymous_profile_picture": false,
        "interop_messaging_user_fbid": null,
        "is_private": false,
        "is_verified": true,
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
          "outgoing_request": false,
          "is_viewer_unconnected": true,
          "reachability_status": 6
        },
        "pk": "8958735",
        "profile_pic_id": "3354861487016662033_8958735",
        "profile_pic_url": "https://scontent-sof1-1.cdninstagram.com/v/t51.2885-19/439586899_1933783770387040_7648789920126959876_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmV4cGVyaW1lbnRhbCJ9&_nc_ht=scontent-sof1-1.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gHKeXz1w_yQTStnJf9E8fjENbDzKBnOvnweklraghubzJ1xcV892yRn8jN8iF1fzjk&_nc_ohc=78gK351qr6gQ7kNvwEU-fma&_nc_gid=Sq-jHfgMFoFVlXK5hIbEeg&edm=AFFDd_gBAAAA&ccb=7-5&ig_cache_key=GFOQMxpg0rQexN4GAASBwUbo9SVqbkULAAAB1501500j-ccb7-5&oh=00_Af1tryU3k8NWNPtd87idl-csND8w1v1TC629ESSfwb-AMQ&oe=69DC42DC&_nc_sid=421beb",
        "reel_auto_archive": null,
        "username": "christiehemmklok",
        "all_media_count": null
      }
    ],
    "next_max_id": "25",
    "has_more": true
  },
  "next_page_id": "25"
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
      "profile_pic_url": "https://scontent-ord5-2.cdninstagram.com/v/t51.82787-19/637874143_18000571244899335_4344695742994650168_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gG9QCwvhVh26kckIFwTSRLiUmfJopOI4-TA5ALfes_nZDQkstGHbnKCCbAyOwgSUSU&_nc_ohc=dBFMb_fAhlIQ7kNvwFnGP94&_nc_gid=eJvFKzSF9_L5LPOt01Jy7w&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af19jEYnzHDTU5XMQUZGrF0vKWH3vmRSvNA6miZRMARC3Q&oe=69DC290A&_nc_sid=10d13b",
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
      "profile_pic_url": "https://instagram.fpen1-2.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fpen1-2.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHcG0n5PLP8GHojYbqWb0T_tDuf38acbzmu1A4059yJukLuGm6fXG6agl4-xNcdQd-G8Erl06WbcJ3zu-bkp4A9&_nc_ohc=a8xHEXzvkAIQ7kNvwFSMO5n&_nc_gid=tSCm3hRwIpJs5HnQLVO9DA&edm=AOmzUmYBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af3ETY6P2ZCknr1O5mJdIGIEuRi7MEXpwFcGesyR4RLgCA&oe=69DC366A&_nc_sid=13eb94",
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
        "profile_pic_url": "https://scontent-sof1-2.cdninstagram.com/v/t51.82787-19/637874143_18000571244899335_4344695742994650168_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sof1-2.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gEGh608KSdrU_Q9oVz6bu7xY2tG3lvdMbMAIADQH4EEs5XHW8Xdnr_BN9a7idchOig&_nc_ohc=dBFMb_fAhlIQ7kNvwEl24Md&_nc_gid=jV2EN2MRyvl7AR7QOmlhpw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2dvqirRc7bxpry0Fsp4D811ET95myxwpicTm8atV-Y6A&oe=69DC290A&_nc_sid=10d13b",
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
        "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-jpg_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4yMjQuYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFj3eiiw0Qq5D9ZDbVBInsEDSwNgyKY7rWnkcCKeTXayUDnBbV5ursgbsYJMWAAzkndMrVeRDZ9is0HUWmwFXzW&_nc_ohc=a8xHEXzvkAIQ7kNvwEqDuO_&edm=AAAAAAABAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af07_ec1YkTh-NL4Ca5yOvRAqMSODoAYj67iIJjEH4MOgA&oe=69DC366A&_nc_sid=328259",
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
    }
  ],
  "{\"server_cursor\": \"QVFETXVzcUQ1UUprVWtrRmFBN2dUMVF5TTJma1RKai1SeWZQT2hCNTJ3UFo3bVB6WldPc1ZBRUFTM2VrYkwyU2Y4NElwaEtZTHZuRTRkRHhaUndSczBBUg==\", \"is_server_cursor_inverse\": true}"
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
    "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/657368100_18524206573079242_7484305376738684507_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHALGbjlDVs-of5-I6eB6k8GP4XjMn-9xyp5iAuTG69M6Evm_6Twt4R_Lbs1CSN0wc&_nc_ohc=vI3vQUoB9qcQ7kNvwFB1IZl&_nc_gid=11f34fVgfoH4O5HVVzGYcA&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2o9WY7tMz3Ifpy0j0Nj4F73Tnhr0ZO_tL3OiAUNsU3WQ&oe=69DC244C&_nc_sid=10d13b",
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
    "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/521543842_18519945877043019_5787012878919658365_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHALGbjlDVs-of5-I6eB6k8GP4XjMn-9xyp5iAuTG69M6Evm_6Twt4R_Lbs1CSN0wc&_nc_ohc=Na0h44VZnZwQ7kNvwFwSOsX&_nc_gid=11f34fVgfoH4O5HVVzGYcA&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af1pIJdpsDuXfxqP4IwDaroNM7kC1LEQRurTtD88HnjN2Q&oe=69DC4AE7&_nc_sid=10d13b",
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
      "request_start_time_ms": 1775657814757,
      "time_at_flush_ms": 1775657814804
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
                "rank_token": "1775658012829|3f90486f5d3220b86c46ec96d5e11a3362da3aad66f025cd573346c5dd2178a2",
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
                    "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFOl6UMAaW5QlRq3kSI0QlH9A8BCTKXj11xirHgQHUYi05TBzYnrBiON3S-1fHwxjA&_nc_ohc=XbeNvhLXv28Q7kNvwGgydmN&_nc_gid=kGed8qhU9z7WpTXheCsFAg&edm=ADuq63kBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af17GmBE8v3VHzUx44F4bdYgrxI8xLflkpjnLGbJe6MdiQ&oe=69DC51E9&_nc_sid=cebafd"
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
                    "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/659308674_18586177681011097_7504785013676369025_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFOl6UMAaW5QlRq3kSI0QlH9A8BCTKXj11xirHgQHUYi05TBzYnrBiON3S-1fHwxjA&_nc_ohc=t-DCVZxwtX4Q7kNvwG0dpPb&_nc_gid=kGed8qhU9z7WpTXheCsFAg&edm=ADuq63kBAAAA&ccb=7-5&ig_cache_key=GIJATCeZsWi2BwhCAIHk2jc1WiZobmNDAQAB1501500j-ccb7-5&oh=00_Af2LGVCG2XkjwumFnVItfkF5sS-fI4iFvPr_ajI-S6Jk8w&oe=69DC2F06&_nc_sid=cebafd"
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
              "edges"
            ]
          },
          {
            "label": "TopSerpAccountsHCMFragment__force_flush",
            "path": [
              "1$xdt_fbsearch__top_serp_graphql(after:$after,first:null,request_data:{\"is_discovery_grid_enabled\":$is_discovery_grid_enabled,\"is_pagination_request\":$is_pagination_request,\"journey_session_id\":$journey_session_id,\"post_id\":$post_id,\"query\":$query,\"requested_unit_types\":$requested_unit_types,\"search_session_id\":$search_session_id,\"serp_origination_context\":$serp_origination_context,\"serp_session_id\":$serp_session_id,\"turn_id\":$turn_id})",
              "edges"
            ]
          }
        ],
        "server_metadata": {
  // ... truncated
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
                      "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwFsL3s3&_nc_oc=Adq-2MHYLca1okEwC2TCbxys2mOkRgF6MLqV5K3vdRMH4_HqYSjTWi9U6iUH-rnLYrg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=8gXgERWEndUk7P14CvgK_g&_nc_ss=7a3ba&oh=00_Af2DssDb7Iowd_FYrr4fLDKe7cZrBdhLCGoKXVIaWahfBA&oe=69DC32B4",
                      "width": 640
                    },
                    "igtv_first_frame": {
                      "width": 640,
                      "height": 1136,
                      "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwFsL3s3&_nc_oc=Adq-2MHYLca1okEwC2TCbxys2mOkRgF6MLqV5K3vdRMH4_HqYSjTWi9U6iUH-rnLYrg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=8gXgERWEndUk7P14CvgK_g&_nc_ss=7a3ba&oh=00_Af2DssDb7Iowd_FYrr4fLDKe7cZrBdhLCGoKXVIaWahfBA&oe=69DC32B4",
                      "scans_profile": "e15"
                    },
                    "smart_frame": null
                  },
                  "candidates": [
                    {
                      "height": 1333,
                      "scans_profile": "e35",
                      "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwHINpie&_nc_oc=Adqke4LvaeUrfw6iyeHaFR97r3RCBr60tmH2Rkx69xJTmHWtcQEOgU2XpNbQrIKQ-P8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=8gXgERWEndUk7P14CvgK_g&_nc_ss=7a3ba&oh=00_Af0K-FI_J9oF-9gPcQFXyTbKcTNgdtUUZgISVA-Q-oo8PA&oe=69DC46E1",
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
                        "https://scontent-sea1-1.cdninstagram.com/v/t51.71878-15/661377490_4446710915609804_6368747692439450584_n.jpg?_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFCiMxVi0B0ZyJCsW_tmjUMMdKy0yYcLa2CQUZIcWZvC0rujpatZurh_ICTrSXH9U0&_nc_ohc=8YQN_m5Qfl0Q7kNvwEADPc3&_nc_gid=8gXgERWEndUk7P14CvgK_g&edm=AL8dhF4BAAAA&ccb=7-5&oh=00_Af1wauGDH7VQn-smJDs9JaXrr_JRU1s8STgvhHPhOVVZqg&oe=69DC46C6&_nc_sid=dc74e4"
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
                "original_height": 1280,
                "original_width": 720,
                "pk": "3870025531093850440",
                "play_count": 2548031,
                "product_type": "clips",
                "video_versions": [
                  {
                    "height": 1280,
  // ... truncated
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
      "pk": "36138315528",
      "id": "36138315528",
      "username": "jellyfish.8114682",
      "full_name": "",
      "profile_pic_url": "https://instagram.fcgk33-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-webp&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fcgk33-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gFa4KBfPZoJ36TxWMWQ9Np01_BCCg7WSof4JtjtfqRyPiH4GI8tl7pJo15vTPXlX4Lee5CkpzkzyS7_KMEYPU2L&_nc_ohc=a8xHEXzvkAIQ7kNvwH3MKLR&_nc_gid=qoc8uRnC8lZJ7Piu1LfBaA&edm=ALlQn9MBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af2AvGkJY1aCW9KZDjxey_rUxrKTgkamxbR18ns5-nPHDw&oe=69DC366A&_nc_sid=e7f676",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 36138315528,
        "expiring_at": 1775744174,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 36138315528,
          "profile_pic_url": "https://instagram.fcgk33-1.fna.fbcdn.net/v/t51.2885-19/573323465_1219825463302212_7278921664109726296_n.png?stp=dst-webp&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=instagram.fcgk33-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gFa4KBfPZoJ36TxWMWQ9Np01_BCCg7WSof4JtjtfqRyPiH4GI8tl7pJo15vTPXlX4Lee5CkpzkzyS7_KMEYPU2L&_nc_ohc=a8xHEXzvkAIQ7kNvwH3MKLR&_nc_gid=qoc8uRnC8lZJ7Piu1LfBaA&edm=ALlQn9MBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.3-ccb7-5&oh=00_Af2AvGkJY1aCW9KZDjxey_rUxrKTgkamxbR18ns5-nPHDw&oe=69DC366A&_nc_sid=e7f676",
          "username": "jellyfish.8114682"
        }
      }
    },
    {
      "pk": "38839641163",
      "id": "38839641163",
      "username": "planet_964",
      "full_name": "Planet 964",
      "profile_pic_url": "https://scontent-syd2-1.cdninstagram.com/v/t51.82787-19/661591116_18074441222289164_6717437846402522080_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MTAuYzIifQ&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHFHUHM54lFsTCUHQoll2GlDkKqgo8MdtVfWrLbBgNtAtHCzgfGfCgDdDlkS1snsvw&_nc_ohc=TVqghbp143oQ7kNvwFJeFH4&_nc_gid=XQ4qCDvail7lPX2We_DGpQ&edm=AOG-cTkBAAAA&ccb=7-5&ig_cache_key=GEwUbycMd5HImzZAAOBblnshIjldbmNDAQAB1501500j-ccb7-5&oh=00_Af00zba-RKvhOrrfUMP32w3AWpBajSUve_IN1P1n43Xpew&oe=69DC4E55&_nc_sid=17ea04",
      "is_private": false,
      "is_verified": false,
      "reel": {
        "id": 38839641163,
        "expiring_at": 1775744174,
        "has_pride_media": false,
        "latest_reel_media": 0,
        "owner": {
          "id": 38839641163,
          "profile_pic_url": "https://scontent-syd2-1.cdninstagram.com/v/t51.82787-19/661591116_18074441222289164_6717437846402522080_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MTAuYzIifQ&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHFHUHM54lFsTCUHQoll2GlDkKqgo8MdtVfWrLbBgNtAtHCzgfGfCgDdDlkS1snsvw&_nc_ohc=TVqghbp143oQ7kNvwFJeFH4&_nc_gid=XQ4qCDvail7lPX2We_DGpQ&edm=AOG-cTkBAAAA&ccb=7-5&ig_cache_key=GEwUbycMd5HImzZAAOBblnshIjldbmNDAQAB1501500j-ccb7-5&oh=00_Af00zba-RKvhOrrfUMP32w3AWpBajSUve_IN1P1n43Xpew&oe=69DC4E55&_nc_sid=17ea04",
          "username": "planet_964"
        }
      }
    }
  ],
  "QVFBMTU5N0cwSTIxcWVLcVhlTXFnUlRIM2c4VWV4NXd1R1JQRFJoS0pYSzNPOXJiSGpwQ3IwTnRRVHFpdkdHUXFRelAzeGRzVnpSS29tazhhdkFNVUtLXw=="
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
      "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/659123606_17925610677266662_299620373829898330_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFM40aGYtKomAoAAn0saOIz9CcuV2FQJX1o8f1iRBDQIX7Egos2PspgKlrvRWnQWVM&_nc_ohc=1GP4i4FmPtQQ7kNvwGwC1EZ&_nc_gid=1iDxyCuDFENzAyypLarA1w&edm=ANg5bX4BAAAA&ccb=7-5&oh=00_Af2rVF2DE8V8D-8ETDpp2QYrOrADRlNG-4ZzsxEbzDtQ9w&oe=69DC5134&_nc_sid=0055be",
      "is_private": false,
      "is_verified": false
    },
    {
      "pk": "20650647",
      "id": "20650647",
      "username": "russwest44",
      "full_name": "Russell Westbrook",
      "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/309889627_1524999051276415_7968180555528416495_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45MjMuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFM40aGYtKomAoAAn0saOIz9CcuV2FQJX1o8f1iRBDQIX7Egos2PspgKlrvRWnQWVM&_nc_ohc=7iK5Ff6oxt0Q7kNvwFVK8FN&_nc_gid=1iDxyCuDFENzAyypLarA1w&edm=ANg5bX4BAAAA&ccb=7-5&oh=00_Af2XmjKKkLkqedJjJpLZc51HBVDE7QIaGPWFnjqSjBiIXA&oe=69DC45F1&_nc_sid=0055be",
      "is_private": false,
      "is_verified": true
    }
  ],
  "QVFBY1BVV2Vad2hpQ1A4NmhLOUhhaDJ1cDBYT1FJT3U3N3lDM3JPSTZfZDZiVmpNellZYnhuTF9VQk1oUU1SWXB0Vm1HWlA4MC10dnB5SThvbzlWeVlrYw=="
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
                      "url": "https://scontent-arn2-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwGyy6Mu&_nc_oc=AdplFk89551ZUrkJ5R91FtgX0pV-snfiwp9s4pKk-KslsB2Ns7VVWwhIU_cgpJK_Tac&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_gid=grAuCFcr7Zficm9rkJU6Vw&_nc_ss=7a3ba&oh=00_Af2eUjfh_fpNRmwn8feIfwXMW4aVDLQoFb7RBdB6Jgungw&oe=69DC2DB1",
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
                      "url": "https://scontent-arn2-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwE_ZAZW&_nc_oc=AdoKzK9ptv5_YVGwVWJ75H-um0fL_-YPUkGpLr2w9nqE50_pCT-YBAh1vFNxhuKMy-s&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_gid=grAuCFcr7Zficm9rkJU6Vw&_nc_ss=7a3ba&oh=00_Af18vr_eRCXKUj8idxwwpGpIVJPuiQabgY00ZcLKr3ShKQ&oe=69DC51CA",
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
          "request_start_time_ms": 1775657770955,
          "time_at_flush_ms": 1775657771253
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
        "profile_grid_items_cursor": "QVFCZ2hUQWFfR1hhZk95TnZBUEdISEZoLUxaX0lMTkxuYkZyMzk0Q1lmUEJTUUpucW5lZDlsUU1DS3lMSnFaVGM1bVYwNk1kRkgxVUNka1dQSk9rQy03Uw==",
        "profile_grid_items": [
          {
            "__typename": "XDTProfileGridItemDict",
            "strong_id__": null,
            "is_fulfilled__(name:\"XDTProfileGridItemDict\")": true,
  // ... truncated
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
    "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.2885-19/476007829_1163063532177165_1226079916897236515_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFk2k1cck07sGNKZxrjgiXOXTD_dMF3lPwcGWalj93oNPIQCBSmj-dF_-bn7hgtKac&_nc_ohc=CoEZxRj_enMQ7kNvwHuwhy-&_nc_gid=FgFl9IoVr88rfmKnp5JZcA&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af18s-BFHMseMeSiDE-NrbuzjiYSsT4QTu7DI9w4vjPWHQ&oe=69DC3DAE&_nc_sid=94fea1",
    "is_private": false,
    "is_verified": true
  },
  {
    "pk": "11830955",
    "id": "11830955",
    "username": "taylorswift",
    "full_name": "Taylor Swift",
    "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/626626039_18625087675054956_4249858978563573242_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFk2k1cck07sGNKZxrjgiXOXTD_dMF3lPwcGWalj93oNPIQCBSmj-dF_-bn7hgtKac&_nc_ohc=lWhS5q1zaL4Q7kNvwHyBVeK&_nc_gid=FgFl9IoVr88rfmKnp5JZcA&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af1X1C4ZOIkInZk4Fo5etUVmz4HbXqK-nkcqP7aa38qS1w&oe=69DC1F3A&_nc_sid=94fea1",
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
                    "url": "https://scontent-mad1-1.cdninstagram.com/v/t51.71878-15/658993118_1501376918245324_1176804504778663620_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vcf2Ah6wBGoQ7kNvwEAbVxk&_nc_oc=Ado-ITKVnZIkmrsp3o3-4jwkML_wdCaEyex_PYu7XQ1o2r04__PY4zRREqv2JufQ3kU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_gid=GGouKZ2SrqGcT7zndOaA4Q&_nc_ss=7a3ba&oh=00_Af33YVBqAkqXbAei2GG6tSxcxo_1uDEXSY9Pn1L9Eh-nkw&oe=69DC336F",
                    "width": 640
                  },
                  "igtv_first_frame": {
                    "height": 1136,
                    "scans_profile": "e15",
                    "url": "https://scontent-mad1-1.cdninstagram.com/v/t51.71878-15/658993118_1501376918245324_1176804504778663620_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=101&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=vcf2Ah6wBGoQ7kNvwEAbVxk&_nc_oc=Ado-ITKVnZIkmrsp3o3-4jwkML_wdCaEyex_PYu7XQ1o2r04__PY4zRREqv2JufQ3kU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_gid=GGouKZ2SrqGcT7zndOaA4Q&_nc_ss=7a3ba&oh=00_Af33YVBqAkqXbAei2GG6tSxcxo_1uDEXSY9Pn1L9Eh-nkw&oe=69DC336F",
                    "width": 640
                  },
                  "smart_frame": null
                },
                "candidates": [
                  {
                    "estimated_scans_sizes": [
                      22800,
                      45600
                    ],
                    "height": 1333,
                    "scans_profile": "e35",
                    "url": "https://scontent-mad1-1.cdninstagram.com/v/t51.82787-15/659582635_18583331794043047_3383163414177246697_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=Mzg3MDEzMDE0MjkxNjI4MjM5MjE4NTgzMzMxNzkxMDQzMDQ3.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=hMjOf9gwscIQ7kNvwFWoEPN&_nc_oc=AdqbuUnppycHOIKmDhPTUbyRJ99lUR6yuJ8U_6MEaGTaJiTsRxnoorHe9jFX7pOtj14&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-mad1-1.cdninstagram.com&_nc_gid=GGouKZ2SrqGcT7zndOaA4Q&_nc_ss=7a3ba&oh=00_Af2GkTFY-2kpBAYt7uUxqdoWfSqeJHg0hFv5BxycO3iSig&oe=69DC1D2D",
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
  // ... truncated
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
      "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPOTM2NjE5NzQzMzkyNDU5AAGniykGEqFJMTXqUJorfSHq-tpYcsHb9hbJraBkRznfC1OpYAYp-KXwJEleW68_aem_R3HJcTKDqTknuv5sEGIuiw&e=AT7ylqtHrwGfcA9IU7ob1mAlSA4crhTWY_AAB39TUEoJAUGdw1ecAvFVZmCnu555-LCPvGFXJK8V6wkb3z8hOdrsFOcGPbCKNinNQoLLU-PdxLTzIblVnDvr37cH55nasQeyCu3QnvPp",
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
  "profile_pic_url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_cat=1&ccb=7-5&_nc_sid=f7ccc5&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwEbFGE1&_nc_oc=Adre4YKtub8JtomlLRvrPjXxafN1nSSI6wTi5hX40AwT-GAYFsTukZVZ6YWN4vMwEdE&_nc_zt=24&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_gid=mRsq_BQuz3tyvOjWOWDU2A&_nc_ss=7a3a8&oh=00_Af0AxZpjg-rGioiLOjbzpUAm_1iXjuok_2g1z3IYZGQHoA&oe=69DC51E9",
  "hd_profile_pic_url_info": {
    "url": "https://scontent-scl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?_nc_cat=1&ccb=7-5&_nc_sid=bf7eb4&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLnd3dy4xMDgwLkMzIn0%3D&_nc_ohc=ajSLGo90eDAQ7kNvwEbFGE1&_nc_oc=Adre4YKtub8JtomlLRvrPjXxafN1nSSI6wTi5hX40AwT-GAYFsTukZVZ6YWN4vMwEdE&_nc_zt=24&_nc_ht=scontent-scl3-1.cdninstagram.com&_nc_gid=mRsq_BQuz3tyvOjWOWDU2A&_nc_ss=7a3a8&oh=00_Af25IwkLoXBvBSkRsG3l5hencfwNOhzffPjhlK01--lHkQ&oe=69DC51E9"
  },
  "is_unpublished": false,
  "latest_reel_media": 1775583063,
  "has_profile_pic": null,
  "profile_pic_genai_tool_info": null,
  "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
  "full_name": "National Geographic",
  "is_verified": true,
  "show_account_transparency_details": true,
  "account_type": 2,
  "follower_count": 274984408,
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
  // ... truncated
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-gql){ target=_blank }
