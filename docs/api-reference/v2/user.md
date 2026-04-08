# User Endpoints

Enhanced user data with pagination via page_id.

!!! info "Authentication & errors"
    All endpoints require `x-access-key` header. See [Authentication](../../getting-started/authentication.md). Error responses: [Response Codes](../response-codes.md).

**Endpoints:** [`/a2/user`](#get-a2user) | [`/v2/user/by/id`](#get-v2userbyid) | [`/v2/user/by/username`](#get-v2userbyusername) | [`/v2/user/clips`](#get-v2userclips) | [`/v2/user/explore/businesses/by/id`](#get-v2userexplorebusinessesbyid) | [`/v2/user/followers`](#get-v2userfollowers) | [`/v2/user/following`](#get-v2userfollowing) | [`/v2/user/highlights`](#get-v2userhighlights) | [`/v2/user/highlights/by/username`](#get-v2userhighlightsbyusername) | [`/v2/user/medias`](#get-v2usermedias) | [`/v2/user/stories`](#get-v2userstories) | [`/v2/user/stories/by/username`](#get-v2userstoriesbyusername) | [`/v2/user/suggested/profiles`](#get-v2usersuggestedprofiles) | [`/v2/user/tag/medias`](#get-v2usertagmedias) | [`/v2/user/videos`](#get-v2uservideos) | [`/v2/userstream/by/id`](#get-v2userstreambyid) | [`/v2/userstream/by/username`](#get-v2userstreambyusername)

---

### GET /a2/user

Get user object

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/a2/user?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_a2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/a2/user",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/a2/user?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "graphql": {
    "user": {
      "id": "787132",
      "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
      "full_name": "National Geographic",
      "edge_followed_by": {
        "count": 274984404
      },
      "edge_follow": {
        "count": 193
      },
      "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG1gKsAIlT6rUCkIVLJa3Hcp0CNlmoCZH1gzkWdWyV-hgOwWo3mZHf3VqBmkhZWOvo&_nc_ohc=XbeNvhLXv28Q7kNvwH5l3lh&_nc_gid=QUFQzDV_eE6bQjCOAsIDdg&edm=AKralEIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0o33nMFJ2exefQ2eXf96uRQM2t7c1kJfNt_AbCA3cjwg&oe=69DC19A9&_nc_sid=2fe71f",
      "profile_pic_url_hd": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s640x640_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG1gKsAIlT6rUCkIVLJa3Hcp0CNlmoCZH1gzkWdWyV-hgOwWo3mZHf3VqBmkhZWOvo&_nc_ohc=XbeNvhLXv28Q7kNvwH5l3lh&_nc_gid=QUFQzDV_eE6bQjCOAsIDdg&edm=AKralEIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB6406400j-ccb7-5&oh=00_Af3D5ei8a-8XCoQLDSWJ0GirwKsYDWIEkDnXz1zvvZSm0Q&oe=69DC19A9&_nc_sid=2fe71f",
      "edge_owner_to_timeline_media": {
        "count": 31529,
        "edges": [
          {
            "node": {
              "id": "3865659729796199935",
              "shortcode": "DWllQsJCPX_",
              "display_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwFFPzW-&_nc_oc=Adp7nBwfi2NidLsGeswUBizeYSxrZtBF2tMYz0aZedkkkUJAto4QqdXzvlYIDFr4qn4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=mSLf2NU0PdP6f90G87Tohg&_nc_ss=7a3ba&oh=00_Af0X8cALN-hT0uy2v5gC92o9cjCSYHb6zP92jLxrNCzfVw&oe=69DC2DB1",
              "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwFFPzW-&_nc_oc=Adp7nBwfi2NidLsGeswUBizeYSxrZtBF2tMYz0aZedkkkUJAto4QqdXzvlYIDFr4qn4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=mSLf2NU0PdP6f90G87Tohg&_nc_ss=7a3ba&oh=00_Af0X8cALN-hT0uy2v5gC92o9cjCSYHb6zP92jLxrNCzfVw&oe=69DC2DB1",
              "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwGJZwbe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=mSLf2NU0PdP6f90G87Tohg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2B8X7DYxMfe7Rb9xNeBmS3cjpdEOY7dJaM1YRIFS7Usg&oe=69D84A2E",
              "__typename": "GraphVideo",
              "product_type": "clips",
              "title": "",
              "video_duration": 60.10100173950195,
              "video_view_count": 0,
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {
                      "text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder"
                    }
                  }
                ]
              },
              "edge_media_to_comment": {
                "count": 236
              },
              "edge_liked_by": {
                "count": 35785
              },
              "edge_media_preview_like": {
                "count": 35785
              }
            }
          },
          {
            "node": {
              "id": "3844732796656436386",
              "shortcode": "DVbPBu5AESi",
              "display_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwFdJ3Ca&_nc_oc=Adq9wnqVXQim_eHH63aOEqybqTyHrN1hpL09Ga0BAv0qdb6K9iOHSFMNs73kZl5tLLo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=mSLf2NU0PdP6f90G87Tohg&_nc_ss=7a3ba&oh=00_Af3qrfQc85fTLvnHF3oDsVPa_NDHVJ6vB606TSV4b_weEA&oe=69DC51CA",
              "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwFdJ3Ca&_nc_oc=Adq9wnqVXQim_eHH63aOEqybqTyHrN1hpL09Ga0BAv0qdb6K9iOHSFMNs73kZl5tLLo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=mSLf2NU0PdP6f90G87Tohg&_nc_ss=7a3ba&oh=00_Af3qrfQc85fTLvnHF3oDsVPa_NDHVJ6vB606TSV4b_weEA&oe=69DC51CA",
              "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwHV24vR&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=mSLf2NU0PdP6f90G87Tohg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1j2GeTl46HO4WWMmkOcwaEsV74W-KRwkQ3O7HiqR6VdQ&oe=69D848EB",
              "__typename": "GraphVideo",
              "product_type": "clips",
              "title": "",
              "video_duration": 60.07400131225586,
              "video_view_count": 0,
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {
                      "text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu."
                    }
                  }
                ]
              },
              "edge_media_to_comment": {
                "count": 612
              },
              "edge_liked_by": {
                "count": 66049
              },
              "edge_media_preview_like": {
                "count": 66049
              }
            }
  // ... truncated
```

</details>

---

### GET /v2/user/by/id

Get user object by id. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/by/id?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_id_v2(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/by/id",
        headers=headers,
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/by/id?id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "user": {
    "strong_id__": "787132",
    "pk": 787132,
    "id": "787132",
    "full_name": "National Geographic",
    "username": "natgeo",
    "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
    "profile_pic_url": "https://instagram.frix7-1.fna.fbcdn.net/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.frix7-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gHIcLkT8Wpd-Vp_Z-zLRIiEnySlma-H9ygE8UVgfh0qdusbtfd-ZZm3zlqdbAlhxwY&_nc_ohc=XbeNvhLXv28Q7kNvwFGCUxf&_nc_gid=KyuBCu9XGLeBBbpvwEN26A&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2wMpzDdOyKvaB4UTOz6hp5BYdUYNywfFSWu-IQgzR0YA&oe=69DC19A9&_nc_sid=6c5dea",
    "is_opal_enabled": false,
    "eligible_for_text_app_activation_badge": false,
    "highlights_tray_type": "DEFAULT",
    "account_type": 2,
    "bio_links": [
      {
        "link_id": 17954981494900183,
        "url": "http://visitstore.bio/natgeo",
        "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnkYfXPXp8KLj_NDnCXh-QDcDMkU61wl3dom0ImedbP9LYe2cAhka5_NszuTY_aem_XNk_LDbtmspMxjUHOQ3pnQ&e=AT6rhDn9jrrd6o0SGGqhB172IR5PVH-zKGqlb21yf-wy2VurXO2lbaZAKUlfJu_dX0ZDNZyLdClXbWH3Qr3mxu35o8Izb1sfATNep-BShA",
        "link_type": "external",
        "title": "",
        "media_type": "none",
        "image_url": "",
        "icon_url": "",
        "media_accent_color_hex": "",
        "is_pinned": false,
        "is_verified": false,
        "open_external_url_with_in_app_browser": true,
        "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnkYfXPXp8KLj_NDnCXh-QDcDMkU61wl3dom0ImedbP9LYe2cAhka5_NszuTY_aem_XNk_LDbtmspMxjUHOQ3pnQ",
        "creation_source": "NONE"
      }
    ],
    "is_call_to_action_enabled": false,
    "is_business": true,
    "biography_with_entities": {
      "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
      "entities": []
    },
    "show_shoppable_feed": false,
    "seller_shoppable_feed_type": "none",
    "is_profile_picture_expansion_enabled": true,
    "show_schools_badge": null,
    "text_post_app_badge_label": "natgeo",
    "text_post_new_post_count": 5,
    "text_post_app_joiner_number": 672534,
    "text_post_app_joiner_number_label": "672,534",
    "recon_features": {
      "enable_recon_cta": true
    },
    "media_count": 31529,
    "trial_clips_rate_limiting": {
      "warning_title": "You can share one more trial reel",
      "at_limit_title": "You've reached the limit",
      "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
      "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
      "count": 20
    },
    "is_prime_onboarding_account": false,
    "is_onboarding_account": false,
    "show_ring_award": false,
    "ring_creator_metadata": {},
    "is_verified": true,
    "is_ring_creator": false,
    "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
    "is_private": false,
    "following_count": 193,
    "follower_count": 274984404,
    "fbid_v2": 17841400573960012,
    "pk_id": "787132",
    "feed_post_reshare_disabled": false,
    "has_ever_selected_topics": false,
    "has_nme_badge": false,
    "third_party_downloads_enabled": 2,
    "show_fb_link_on_profile": false,
    "show_fb_page_link_on_profile": false,
    "can_hide_category": true,
    "can_hide_public_contacts": true,
    "primary_profile_link_type": 0,
    "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
    "current_catalog_id": null,
    "mini_shop_seller_onboarding_status": null,
  // ... truncated
```

</details>

---

### GET /v2/user/by/username

Get user object by username. Returns a User object.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_by_username_v2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/by/username",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "user": {
    "strong_id__": "787132",
    "pk": 787132,
    "id": "787132",
    "full_name": "National Geographic",
    "username": "natgeo",
    "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
    "profile_pic_url": "https://scontent-lga3-2.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-2.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEXREqYBZrfY4kTR2VLgQ2n_5bGqozRA2MRkzj_tb9Gft5d5XzWTtXNGxuUx3UnsdY&_nc_ohc=XbeNvhLXv28Q7kNvwFHmgPT&_nc_gid=XczVM2HQTGy4tRMtDt1hkA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3Yy_BSHurR0OTbDadha6Q69mlC1xsJTPAT2ILTER3uFA&oe=69DC19A9&_nc_sid=164c1d",
    "is_opal_enabled": false,
    "eligible_for_text_app_activation_badge": false,
    "highlights_tray_type": "DEFAULT",
    "account_type": 2,
    "bio_links": [
      {
        "link_id": 17954981494900183,
        "url": "http://visitstore.bio/natgeo",
        "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGniNsrN7Ql-skX4m6AlJA6feY0y6bgLi9311B3PtBLpxkv6DBFut-HqlfA9Yw_aem_NyCDViq0OTf5RefU0XBbsw&e=AT5-4ysKPgc8HXkS1cO5XRY43JdnvwMmWlM35HWwFADEoGCiHhVMzcHuA78Xb5FhGGXhdJowFY9GU3ClKtiw04Lhx_1jwlqd8WvPU1IXSA",
        "link_type": "external",
        "title": "",
        "media_type": "none",
        "image_url": "",
        "icon_url": "",
        "media_accent_color_hex": "",
        "is_pinned": false,
        "is_verified": false,
        "open_external_url_with_in_app_browser": true,
        "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGniNsrN7Ql-skX4m6AlJA6feY0y6bgLi9311B3PtBLpxkv6DBFut-HqlfA9Yw_aem_NyCDViq0OTf5RefU0XBbsw",
        "creation_source": "NONE"
      }
    ],
    "is_call_to_action_enabled": false,
    "is_business": true,
    "biography_with_entities": {
      "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
      "entities": []
    },
    "show_shoppable_feed": false,
    "seller_shoppable_feed_type": "none",
    "is_profile_picture_expansion_enabled": true,
    "show_schools_badge": null,
    "text_post_app_badge_label": "natgeo",
    "text_post_new_post_count": 5,
    "text_post_app_joiner_number": 672534,
    "text_post_app_joiner_number_label": "672,534",
    "recon_features": {
      "enable_recon_cta": true
    },
    "media_count": 31529,
    "trial_clips_rate_limiting": {
      "warning_title": "You can share one more trial reel",
      "at_limit_title": "You've reached the limit",
      "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
      "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
      "count": 20
    },
    "is_prime_onboarding_account": false,
    "is_onboarding_account": false,
    "show_ring_award": false,
    "ring_creator_metadata": {},
    "is_verified": true,
    "is_ring_creator": false,
    "is_private": false,
    "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
    "following_count": 193,
    "follower_count": 274984403,
    "fbid_v2": 17841400573960012,
    "pk_id": "787132",
    "feed_post_reshare_disabled": false,
    "has_ever_selected_topics": false,
    "has_nme_badge": false,
    "third_party_downloads_enabled": 2,
    "show_fb_link_on_profile": false,
    "show_fb_page_link_on_profile": false,
    "can_hide_category": true,
    "can_hide_public_contacts": true,
    "primary_profile_link_type": 0,
    "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
    "current_catalog_id": null,
    "mini_shop_seller_onboarding_status": null,
  // ... truncated
```

</details>

---

### GET /v2/user/clips

Get user clips. Returns a list of Media objects (Reels).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/clips?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_clips_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/clips",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/clips?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "items": [
      {
        "media": {
          "strong_id__": "3870025531093850440_1029649300",
          "id": "3870025531093850440_1029649300",
          "disable_caption_and_comment": false,
          "fbid": 18064241420343903,
          "deleted_reason": 0,
          "client_cache_key": "Mzg3MDAyNTUzMTA5Mzg1MDQ0MA==.3",
          "integrity_review_decision": "pending",
          "pk": "3870025531093850440",
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
                  4454,
                  8908
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwFsMjFy&_nc_oc=AdovCKrvoGthY-lYLHaR7Di4g04JTGydGa3kHaOq584fPkTvzSeg-FGRr4Pf4iUswPk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_gid=z1jggVzEMNLoxtKvYerNcQ&_nc_ss=7a3ba&oh=00_Af3Iv3Fc7c_CPmybdjTkqgTpPZikTw9oy5nazkjEXUPOFg&oe=69DC32B4",
                "width": 640,
                "is_spatial_image": false
              },
              "igtv_first_frame": {
                "estimated_scans_sizes": [
                  4454,
                  8908
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwFsMjFy&_nc_oc=AdovCKrvoGthY-lYLHaR7Di4g04JTGydGa3kHaOq584fPkTvzSeg-FGRr4Pf4iUswPk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_gid=z1jggVzEMNLoxtKvYerNcQ&_nc_ss=7a3ba&oh=00_Af3Iv3Fc7c_CPmybdjTkqgTpPZikTw9oy5nazkjEXUPOFg&oe=69DC32B4",
                "width": 640,
                "is_spatial_image": false
              },
              "smart_frame": null
            },
            "candidates": [
              {
                "estimated_scans_sizes": [
                  18248,
                  36496
                ],
                "height": 1333,
                "scans_profile": "e35",
                "url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwEBd8S8&_nc_oc=AdoOaq6iFYrSX5WUbqNzJTDEZwrkRf47zFKjPOi7D058nvlD1F9WCJFFisyllTt8kWs&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_gid=z1jggVzEMNLoxtKvYerNcQ&_nc_ss=7a3ba&oh=00_Af1jtG1qtcv_sXTmJqNbIZUKS41G6hiaCUEPMDAggikcsw&oe=69DC46E1",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 271,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_urls": [
                  "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/661377490_4446710915609804_6368747692439450584_n.jpg?_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gH47fU_9bj2T2Pf4sFG9R-k4ymlpKxoLrO2MU4fRZcSOtRsd41Sv5nmYLdGs5MgEcc&_nc_ohc=8YQN_m5Qfl0Q7kNvwETAK3Z&_nc_gid=z1jggVzEMNLoxtKvYerNcQ&edm=ACHbZRIBAAAA&ccb=7-5&oh=00_Af2ZSVhDaKbiYWLvFnv8fyiSz_qmJV52w2LMvCdzZmT_bQ&oe=69DC46C6&_nc_sid=c024bc"
                ],
                "sprite_width": 1500,
                "thumbnail_duration": 0.578352380952381,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
  // ... truncated
```

</details>

---

### GET /v2/user/explore/businesses/by/id

Get list of recommended accounts for business category of the user by his id. Returns recommended accounts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/explore/businesses/by/id?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_explore_businesses_by_id_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/explore/businesses/by/id",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/explore/businesses/by/id?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "category_id": 0,
  "items": [
    {
      "user": {
        "strong_id__": "5445218106",
        "pk": 5445218106,
        "pk_id": "5445218106",
        "fbid_v2": 17841405343200652,
        "third_party_downloads_enabled": 1,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "id": "5445218106",
        "profile_pic_id": "1511834005069211669_5445218106",
        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.2885-19/36979478_1108966052592442_2446283676674162688_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xODEuYzIifQ&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gEuh6_TnLLMMJAAWFaR2ol1_Ab1vMPVuWtvXfaqVvMOPyqVtUBrLsMK8bCyL1qnX2Q&_nc_ohc=6FpOoF1f938Q7kNvwGlPq6t&_nc_gid=50rsMaiAvn6n0Bs-Qy_dEw&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=GBZDNAI6_6FHmfADAAAAAAAL8vIhbkULAAAB1501500j-ccb7-5&oh=00_Af1RpyN_Vqa5wNFHGmxCYxuzmk8Zmv1MYj9sLS2nBDu3TQ&oe=69DC2B57&_nc_sid=3e1f4f",
        "is_verified": false,
        "username": "the_scientist_magazine",
        "full_name": "The Scientist Magazine",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "latest_reel_media": 1775657053,
        "account_badges": [],
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
        },
        "should_show_category": true,
        "category_id": "2233",
        "is_category_tappable": true,
        "should_show_public_contacts": true,
        "category": "Media/news company"
      },
      "media_previews": [
        {
          "media_id": 3865741383072792696,
          "media_fbid": 18074569283561933,
          "thumbnail_url": "https://scontent-iad6-1.cdninstagram.com/v/t39.30808-6/658827819_1372199101613834_6861606413018434238_n.jpg?stp=c0.205.1638.1638a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gEuh6_TnLLMMJAAWFaR2ol1_Ab1vMPVuWtvXfaqVvMOPyqVtUBrLsMK8bCyL1qnX2Q&_nc_ohc=DUn9KPp4r1QQ7kNvwGPY4GD&_nc_gid=50rsMaiAvn6n0Bs-Qy_dEw&edm=ALPbrGYAAAAA&ccb=7-5&ig_cache_key=Mzg2NTc0MTM4MzA3Mjc5MjY5Ng%3D%3D.3.c-ccb7-5&oh=00_Af21QIYrtzV5JWUdgXcigdZqmz6OR85btIpygfw9RyQXuQ&oe=69DC3607&_nc_sid=3e1f4f"
        },
        {
          "media_id": 3844028826083372791,
          "media_fbid": 17955279509935029,
          "thumbnail_url": "https://scontent-iad3-1.cdninstagram.com/v/t39.30808-6/645739337_1347153844118360_5210304906653608462_n.jpg?stp=c0.205.1638.1638a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gEuh6_TnLLMMJAAWFaR2ol1_Ab1vMPVuWtvXfaqVvMOPyqVtUBrLsMK8bCyL1qnX2Q&_nc_ohc=fg5hVq6PNTQQ7kNvwGclDUy&_nc_gid=50rsMaiAvn6n0Bs-Qy_dEw&edm=ALPbrGYAAAAA&ccb=7-5&ig_cache_key=Mzg0NDAyODgyNjA4MzM3Mjc5MQ%3D%3D.3.c-ccb7-5&oh=00_Af2KBH7YmhTQK5Q2chtiKM2ICv9abpl6HIjDZRS0YcYi8Q&oe=69DC3ED3&_nc_sid=3e1f4f"
        }
      ]
    },
    {
      "user": {
        "strong_id__": "41706552435",
        "pk": 41706552435,
        "pk_id": "41706552435",
        "fbid_v2": 17841441533073319,
        "third_party_downloads_enabled": 1,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "id": "41706552435",
        "profile_pic_id": "3515614788425463673_41706552435",
        "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/469203603_607657381816727_6317965279284024222_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MTIuYzIifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gEuh6_TnLLMMJAAWFaR2ol1_Ab1vMPVuWtvXfaqVvMOPyqVtUBrLsMK8bCyL1qnX2Q&_nc_ohc=gMsqSllxmw4Q7kNvwHmZ54L&_nc_gid=50rsMaiAvn6n0Bs-Qy_dEw&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=GJN69xuXaWNCqSgCAJ7T_Y7y661XbkULAAAB1501500j-ccb7-5&oh=00_Af1PnMupCPOhnBx-qpW_GOJlVPANlEzgA4xqgkgM9c6xtg&oe=69DC34CC&_nc_sid=3e1f4f",
        "is_verified": false,
        "username": "sciencex.physorg",
        "full_name": "Science X / Phys.org",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "latest_reel_media": 1775653633,
        "account_badges": [],
        "friendship_status": {
          "following": false,
          "is_bestie": false,
          "is_feed_favorite": false,
          "is_private": false,
          "is_restricted": false,
  // ... truncated
```

</details>

---

### GET /v2/user/followers

Get part (one page) of followers users with cursor. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/followers?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_followers_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/followers",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/followers?user_id=787132",
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
        "pk": "8997860794",
        "id": "8997860794",
        "username": "edochieuchendu",
        "full_name": "edochieuchendu",
        "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/660543945_18341635714300795_5491368841241892774_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43MjAuYzIifQ&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gF98cLC1ese7nlfKsryFhJkddX7XCqmrw6wwbR_f9XY3BI6y9CxLFLstqygOXM-kFM&_nc_ohc=93GRH3J01l0Q7kNvwECTcne&_nc_gid=B3N5-bbrcnmmemTbPLvOTw&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af10hA5YfI80S1tqmtW9TUHqcw8UPTw6jI9xOn2lzhH0LA&oe=69DC36C0&_nc_sid=17ea04",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false,
        "account_badges": null,
        "fbid_v2": null,
        "has_anonymous_profile_picture": null,
        "latest_reel_media": 1775656753,
        "pk_id": null,
        "profile_pic_id": null,
        "strong_id__": null,
        "third_party_downloads_enabled": null,
        "reel": {
          "id": "8997860794",
          "expiring_at": 1775744143,
          "has_pride_media": false,
          "latest_reel_media": 1775656753,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "8997860794",
            "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/660543945_18341635714300795_5491368841241892774_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43MjAuYzIifQ&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gF98cLC1ese7nlfKsryFhJkddX7XCqmrw6wwbR_f9XY3BI6y9CxLFLstqygOXM-kFM&_nc_ohc=93GRH3J01l0Q7kNvwECTcne&_nc_gid=B3N5-bbrcnmmemTbPLvOTw&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af10hA5YfI80S1tqmtW9TUHqcw8UPTw6jI9xOn2lzhH0LA&oe=69DC36C0&_nc_sid=17ea04",
            "username": "edochieuchendu"
          }
        },
        "followed_by_viewer": false,
        "follows_viewer": false,
        "requested_by_viewer": false
      },
      {
        "pk": "5774696840",
        "id": "5774696840",
        "username": "viktoriablayer",
        "full_name": "Blayer Viktória",
        "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.2885-19/20225271_254144308419459_4537409713003823104_a.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gF98cLC1ese7nlfKsryFhJkddX7XCqmrw6wwbR_f9XY3BI6y9CxLFLstqygOXM-kFM&_nc_ohc=oXMQpf7sFCwQ7kNvwHn2exC&_nc_gid=B3N5-bbrcnmmemTbPLvOTw&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af1xs_hLaHoUvz9lux4vxkAMpL7DPaixmpH8bPt6474Jyw&oe=69DC3CB5&_nc_sid=17ea04",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false,
        "account_badges": null,
        "fbid_v2": null,
        "has_anonymous_profile_picture": null,
        "latest_reel_media": 0,
        "pk_id": null,
        "profile_pic_id": null,
        "strong_id__": null,
        "third_party_downloads_enabled": null,
        "reel": {
          "id": "5774696840",
          "expiring_at": 1775744143,
          "has_pride_media": false,
          "latest_reel_media": 0,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "5774696840",
            "profile_pic_url": "https://scontent-sjc3-1.cdninstagram.com/v/t51.2885-19/20225271_254144308419459_4537409713003823104_a.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gF98cLC1ese7nlfKsryFhJkddX7XCqmrw6wwbR_f9XY3BI6y9CxLFLstqygOXM-kFM&_nc_ohc=oXMQpf7sFCwQ7kNvwHn2exC&_nc_gid=B3N5-bbrcnmmemTbPLvOTw&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af1xs_hLaHoUvz9lux4vxkAMpL7DPaixmpH8bPt6474Jyw&oe=69DC3CB5&_nc_sid=17ea04",
            "username": "viktoriablayer"
          }
        },
        "followed_by_viewer": false,
        "follows_viewer": false,
        "requested_by_viewer": false
      }
    ],
    "big_list": null,
    "page_size": null,
    "next_max_id": null,
    "has_more": null,
    "should_limit_list_of_followers": null,
    "use_clickable_see_more": null,
    "show_spam_follow_request_tab": null,
    "status": null
  // ... truncated
```

</details>

---

### GET /v2/user/following

Get part (one page) of following users. Returns a list of User objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/following?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_following_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/following",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/following?user_id=787132",
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
        "strong_id__": "14331657700",
        "pk": "14331657700",
        "pk_id": "14331657700",
        "id": "14331657700",
        "fbid_v2": 17841414211021457,
        "third_party_downloads_enabled": 1,
        "profile_pic_id": "2073867961613189688_14331657700",
        "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/v/t51.2885-19/65160972_483182759115510_2590728031043584000_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MDAuYzIifQ&_nc_ht=scontent-sin2-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gHRrEOVVIvAUgroT2lycY_glipEWvA7O3oF4_ITDwYuqwBEuHCCT9L5AqtmRdby9j4&_nc_ohc=7ujGFVqjyKQQ7kNvwHsfzr9&_nc_gid=Gqnsq-r1Q3Z6GMJRU9jrXw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GAxH4gP2_rfAc7cBAAAAAABrHfQjbkULAAAB1501500j-ccb7-5&oh=00_Af02LSE7Fd9Sr-qvMC-rXgPnVTY5OjkPcMNrEVOkTrbu-Q&oe=69DC21ED&_nc_sid=ce9561",
        "is_verified": false,
        "username": "natgeomagjp",
        "full_name": "ナショナルジオグラフィック日本版",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "account_badges": [],
        "latest_reel_media": 0,
        "is_favorite": false
      },
      {
        "strong_id__": "12802178",
        "pk": "12802178",
        "pk_id": "12802178",
        "id": "12802178",
        "fbid_v2": 17841400065340200,
        "third_party_downloads_enabled": 1,
        "profile_pic_id": "3274170007750843044_12802178",
        "profile_pic_url": "https://scontent-sin2-2.cdninstagram.com/v/t51.2885-19/416867607_774634348037538_4645960129122799142_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sin2-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gHRrEOVVIvAUgroT2lycY_glipEWvA7O3oF4_ITDwYuqwBEuHCCT9L5AqtmRdby9j4&_nc_ohc=9cpBf5YDNfEQ7kNvwFMbIGY&_nc_gid=Gqnsq-r1Q3Z6GMJRU9jrXw&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GBfl2BiiRSWdhsACACYO-kAfxHlAbkULAAAB1501500j-ccb7-5&oh=00_Af3XWof9NB390XfruFU36vx9qInQ5xVyu761B7GcoepaEQ&oe=69DC38FB&_nc_sid=ce9561",
        "is_verified": true,
        "username": "stephaniemeiling",
        "full_name": "Stephanie Mei-Ling",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "account_badges": [],
        "latest_reel_media": 0,
        "is_favorite": false
      }
    ],
    "big_list": true,
    "page_size": 25,
    "next_max_id": "25",
    "has_more": true,
    "should_limit_list_of_followers": false,
    "use_clickable_see_more": false,
    "follow_ranking_token": "cfcbfec691db4f3fb21c5e47683d0fdf|35144191759|osr",
    "status": "ok"
  },
  "next_page_id": "25"
}
```

</details>

---

### GET /v2/user/highlights

⚠️ Billing: 2 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/highlights?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/highlights",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/highlights?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "tray": [
      {
        "strong_id__": "highlight:17983616051768088",
        "id": "highlight:17983616051768088",
        "reel_type": "highlight_reel",
        "title": "Gift Guide",
        "created_at": 1764846391,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": null,
          "media_id": null,
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gG5Mt-f1kTAGK9TmMTX_9bDXFwXXf43H8M3nzF2LRPNobP6NEDdSFS3EHv6ULJuo5E&_nc_ohc=y1uvOTY1dWMQ7kNvwFH3a5M&_nc_gid=SUfOQEG3YZNIFFFTRJGdUg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af05Hg9-LwfNTWg9eKwIJbFtrGAqYnlvnBZ3Pb0RD0Vpkg&oe=69DC397C&_nc_sid=847350",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1766243006,
        "seen_ranked_position": -1766243006,
        "media_count": 12,
        "updated_timestamp": 1766243006,
        "latest_reel_media": 1766242839,
        "seen": null,
        "can_reply": false,
        "can_react_with_avatar": false,
        "contains_stitched_media_blocked_by_rm": false,
        "user": {
          "strong_id__": "787132",
          "pk": "787132",
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gG5Mt-f1kTAGK9TmMTX_9bDXFwXXf43H8M3nzF2LRPNobP6NEDdSFS3EHv6ULJuo5E&_nc_ohc=XbeNvhLXv28Q7kNvwH38lmO&_nc_gid=SUfOQEG3YZNIFFFTRJGdUg&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2b8elgFUqtARqfiJPt1jy7XvH6e7nEqBF6cEFaHz_ubg&oe=69DC19A9&_nc_sid=847350",
          "account_badges": [],
          "interop_messaging_user_fbid": 113671860027320,
          "is_creator_agent_enabled": false
        },
        "pk": "17983616051768088",
        "items": []
      },
      {
        "strong_id__": "highlight:18018069326790931",
        "id": "highlight:18018069326790931",
        "reel_type": "highlight_reel",
        "title": "BOTW 2026",
        "created_at": 1761052067,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": null,
          "media_id": null,
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gG5Mt-f1kTAGK9TmMTX_9bDXFwXXf43H8M3nzF2LRPNobP6NEDdSFS3EHv6ULJuo5E&_nc_ohc=KnNItKNMJcAQ7kNvwExIaSG&_nc_gid=SUfOQEG3YZNIFFFTRJGdUg&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af1On6FpPbVhcpy7_KD4wZ01Q5KJG8wFV3eIlD3XNKz5iw&oe=69DC19F3&_nc_sid=847350",
            "width": 150
          },
  // ... truncated
```

</details>

---

### GET /v2/user/highlights/by/username

⚠️ Billing: 3 requests per call. Returns a list of Highlight objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `amount` | integer | No | Amount |
| `force` | boolean | No | Skip account privacy check |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/highlights/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_highlights_by_username_v2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/highlights/by/username",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/highlights/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "tray": [
      {
        "strong_id__": "highlight:17983616051768088",
        "id": "highlight:17983616051768088",
        "reel_type": "highlight_reel",
        "title": "Gift Guide",
        "created_at": 1764846391,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": null,
          "media_id": null,
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gF_AmxVeYteyRhf6g0ANviRwW1XOrVW71vlBwkfnF1EEdkzVN0AdquzQW-hQQ9VmdE&_nc_ohc=y1uvOTY1dWMQ7kNvwG4wjJq&_nc_gid=MjAjAUTGYjk57I-jcZ-NCQ&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af2grHh6RQDlHt5T3bphzkwMYVMvMdDGXDBtBqaXZcTalQ&oe=69DC397C&_nc_sid=847350",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1766243006,
        "seen_ranked_position": -1766243006,
        "media_count": 12,
        "updated_timestamp": 1766243006,
        "latest_reel_media": 1766242839,
        "seen": null,
        "can_reply": false,
        "can_react_with_avatar": false,
        "contains_stitched_media_blocked_by_rm": false,
        "user": {
          "strong_id__": "787132",
          "pk": "787132",
          "pk_id": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "is_private": false,
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF_AmxVeYteyRhf6g0ANviRwW1XOrVW71vlBwkfnF1EEdkzVN0AdquzQW-hQQ9VmdE&_nc_ohc=XbeNvhLXv28Q7kNvwFICEUk&_nc_gid=MjAjAUTGYjk57I-jcZ-NCQ&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af06QwYO4hJMPOqGeXcRBg1GQuGsximubW1oQ6WjdFoR_g&oe=69DC19A9&_nc_sid=847350",
          "account_badges": [],
          "interop_messaging_user_fbid": 113671860027320,
          "is_creator_agent_enabled": false
        },
        "pk": "17983616051768088",
        "items": []
      },
      {
        "strong_id__": "highlight:18018069326790931",
        "id": "highlight:18018069326790931",
        "reel_type": "highlight_reel",
        "title": "BOTW 2026",
        "created_at": 1761052067,
        "is_pinned_highlight": false,
        "prefetch_count": 0,
        "highlight_reel_type": "DEFAULT",
        "is_converted_to_clips": false,
        "is_nux": false,
        "can_gif_quick_reply": true,
        "can_reshare": true,
        "is_archived": false,
        "cover_media": {
          "crop_rect": null,
          "media_id": null,
          "upload_id": null,
          "cropped_image_version": {
            "height": 150,
            "scans_profile": "",
            "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gF_AmxVeYteyRhf6g0ANviRwW1XOrVW71vlBwkfnF1EEdkzVN0AdquzQW-hQQ9VmdE&_nc_ohc=KnNItKNMJcAQ7kNvwFs4_NF&_nc_gid=MjAjAUTGYjk57I-jcZ-NCQ&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af0aJ5janqj-tK_9G3jzKW3GnIsFS3vAg7kBWtlC3DPDZQ&oe=69DC19F3&_nc_sid=847350",
            "width": 150
          },
  // ... truncated
```

</details>

---

### GET /v2/user/medias

Get user medias. Results chunk. Returns a list of Media objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/medias?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/medias",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/medias?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "profile_grid_items": null,
    "profile_grid_items_cursor": null,
    "pinned_profile_grid_items_ids": null,
    "special_empty_state": null,
    "num_results": 12,
    "more_available": true,
    "items": [
      {
        "strong_id__": "3865659729796199935_787132",
        "id": "3865659729796199935_787132",
        "caption_is_edited": false,
        "device_timestamp": 177504257174,
        "filter_type": 0,
        "is_post_live_clips_media": false,
        "disable_caption_and_comment": false,
        "like_and_view_counts_disabled": false,
        "fbid": 18174874810398454,
        "deleted_reason": 0,
        "client_cache_key": "Mzg2NTY1OTcyOTc5NjE5OTkzNQ==.3",
        "integrity_review_decision": "pending",
        "pk": "3865659729796199935",
        "is_affiliate_commission_eligible": false,
        "has_delayed_metadata": false,
        "mezql_token": "",
        "should_request_ads": false,
        "has_privately_liked": false,
        "is_quiet_post": false,
        "profile_grid_thumbnail_fitting_style": "UNSET",
        "collaborator_edit_eligibility": false,
        "share_count_disabled": false,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "has_shared_to_fb": 0,
        "is_visual_reply_commenter_notice_enabled": true,
        "translated_langs_for_autodub": [],
        "subtype_name_for_REST__": "XDTClipsMedia",
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_third_party_downloads_eligible": false,
        "code": "DWllQsJCPX_",
        "enable_media_notes_production": true,
        "has_views_fetching": true,
        "original_media_has_visual_reply_media": false,
        "report_info": {
          "has_viewer_submitted_report": false
        },
        "image_versions2": {
          "additional_candidates": {
            "first_frame": {
              "estimated_scans_sizes": [
                2644,
                5288
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.71878-15/658030605_1256609569870746_7397274986069476460_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bCRwORgGzQAQ7kNvwFS8m3e&_nc_oc=AdqfqlLRGICPAojMIc59C_Ejki5zHdJnlCur-NjGrJiIdHC13PbweeEeEBsTR24t28o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=2BlZSoyeDReLEUotd6D8pw&_nc_ss=7a3ba&oh=00_Af3FpqBhM5kvNo8e8gRl1CklbfLt1gQvlNW0Qee7hyDfuw&oe=69DC1A4D",
              "width": 640,
              "is_spatial_image": false
            },
            "igtv_first_frame": {
              "estimated_scans_sizes": [
                2644,
                5288
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sea1-1.cdninstagram.com/v/t51.71878-15/658030605_1256609569870746_7397274986069476460_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bCRwORgGzQAQ7kNvwFS8m3e&_nc_oc=AdqfqlLRGICPAojMIc59C_Ejki5zHdJnlCur-NjGrJiIdHC13PbweeEeEBsTR24t28o&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_gid=2BlZSoyeDReLEUotd6D8pw&_nc_ss=7a3ba&oh=00_Af3FpqBhM5kvNo8e8gRl1CklbfLt1gQvlNW0Qee7hyDfuw&oe=69DC1A4D",
              "width": 640,
              "is_spatial_image": false
            },
            "smart_frame": null
          },
          "candidates": [
            {
  // ... truncated
```

</details>

---

### GET /v2/user/stories

⚠️ Billing: 2 requests per call. Returns a list of Story objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `force` | boolean | No | Skip account privacy check |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/stories?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_stories_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/stories",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/stories?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "broadcast": null,
  "reel": {
    "id": 787132,
    "strong_id__": "787132",
    "latest_reel_media": 1775583063,
    "seen": 0,
    "can_reply": false,
    "can_gif_quick_reply": true,
    "can_reshare": true,
    "reel_type": "user_reel",
    "ad_expiry_timestamp_in_millis": null,
    "is_cta_sticker_available": null,
    "should_treat_link_sticker_as_cta": null,
    "pool_refresh_ttl_in_sec": null,
    "can_react_with_avatar": false,
    "prefetch_count": 0,
    "expiring_at": 1775669463,
    "user": {
      "strong_id__": "787132",
      "pk": 787132,
      "pk_id": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF91VAoJxVRRHt_wP2d1tbeUasRm6Xz0gGNZmW4THczxPDkYH9lBzO-ND4UnmPHVaU&_nc_ohc=XbeNvhLXv28Q7kNvwEHq1Il&_nc_gid=umd_QuXCYCPeMlNFE9KNcA&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1yjxemIsO47ZX88rgU5HqEEv3UCou_n78oozm0KpRLFw&oe=69DC19A9&_nc_sid=6d62aa",
      "interop_messaging_user_fbid": 113671860027320,
      "is_creator_agent_enabled": false,
      "transparency_product_enabled": false,
      "is_screenshot_blocking_enabled": false,
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
    "items": [
      {
        "strong_id__": "3870193736105885141_787132",
        "id": "3870193736105885141_787132",
        "expiring_at": 1775669463,
        "pk": 3870193736105885141,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18133922983469531,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDE5MzczNjEwNTg4NTE0MQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-dfw5-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF91VAoJxVRRHt_wP2d1tbeUasRm6Xz0gGNZmW4THczxPDkYH9lBzO-ND4UnmPHVaU&_nc_ohc=XbeNvhLXv28Q7kNvwEHq1Il&_nc_gid=umd_QuXCYCPeMlNFE9KNcA&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1yjxemIsO47ZX88rgU5HqEEv3UCou_n78oozm0KpRLFw&oe=69DC19A9&_nc_sid=6d62aa",
  // ... truncated
```

</details>

---

### GET /v2/user/stories/by/username

⚠️ Billing: 3 requests per call. Returns a list of Story objects.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |
| `force` | boolean | No | Skip account privacy check |
| `safe_int` | boolean | No | Convert all big integers to strings |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/stories/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_stories_by_username_v2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/stories/by/username",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/stories/by/username?username=natgeo",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "broadcast": null,
  "reel": {
    "id": 787132,
    "strong_id__": "787132",
    "latest_reel_media": 1775583063,
    "seen": 0,
    "can_reply": false,
    "can_gif_quick_reply": true,
    "can_reshare": true,
    "reel_type": "user_reel",
    "ad_expiry_timestamp_in_millis": null,
    "is_cta_sticker_available": null,
    "should_treat_link_sticker_as_cta": null,
    "pool_refresh_ttl_in_sec": null,
    "can_react_with_avatar": false,
    "prefetch_count": 0,
    "expiring_at": 1775669463,
    "user": {
      "strong_id__": "787132",
      "pk": 787132,
      "pk_id": "787132",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "is_private": false,
      "is_ring_creator": false,
      "show_ring_award": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF0NiG8LrWXi52kCTssDPQ3Gx7e6aDnR7CkaKH2CkQ-Lwz7GRJOimPIFlkfJs9PYPo&_nc_ohc=XbeNvhLXv28Q7kNvwG3oDx_&_nc_gid=jGuhbzRVnhLm13L6EnG3GQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af27W2qoU5MaxIKCwsgd27CJ92bNtKo4dhQDBN9jAbE14A&oe=69DC19A9&_nc_sid=6d62aa",
      "interop_messaging_user_fbid": 113671860027320,
      "is_creator_agent_enabled": false,
      "transparency_product_enabled": false,
      "is_screenshot_blocking_enabled": false,
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
    "items": [
      {
        "strong_id__": "3870193736105885141_787132",
        "id": "3870193736105885141_787132",
        "expiring_at": 1775669463,
        "pk": 3870193736105885141,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18133922983469531,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDE5MzczNjEwNTg4NTE0MQ==.3",
        "has_privately_liked": false,
        "user": {
          "strong_id__": "787132",
          "id": "787132",
          "pk": 787132,
          "fbid_v2": 17841400573960012,
          "pk_id": "787132",
          "eligible_for_text_app_activation_badge": false,
          "account_type": 2,
          "is_private": false,
          "account_badges": [],
          "full_name": "National Geographic",
          "is_verified": true,
          "profile_pic_id": "3865702555259028436_787132",
          "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gF0NiG8LrWXi52kCTssDPQ3Gx7e6aDnR7CkaKH2CkQ-Lwz7GRJOimPIFlkfJs9PYPo&_nc_ohc=XbeNvhLXv28Q7kNvwG3oDx_&_nc_gid=jGuhbzRVnhLm13L6EnG3GQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af27W2qoU5MaxIKCwsgd27CJ92bNtKo4dhQDBN9jAbE14A&oe=69DC19A9&_nc_sid=6d62aa",
  // ... truncated
```

</details>

---

### GET /v2/user/suggested/profiles

Fetch suggested users details by target_id.

expand_suggestion=True for more detailed response

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User Id |
| `expand_suggestion` | boolean | No | Expand Suggestion |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/suggested/profiles?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_suggested_profiles_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/suggested/profiles",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/suggested/profiles?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "users": [
    {
      "strong_id__": "247944034",
      "pk": 247944034,
      "pk_id": "247944034",
      "id": "247944034",
      "username": "beyonce",
      "full_name": "Beyoncé",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3558910092344959196_247944034",
      "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.2885-19/476007829_1163063532177165_1226079916897236515_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEAbgw-a6QU8F3felfXpPVm1knG2Gh40utOm64ItYcZAmpM8JTQMh2RFC63S7B8hnM&_nc_ohc=CoEZxRj_enMQ7kNvwHuwhy-&_nc_gid=68x_G3kHITvJqsLnRmBG2Q&edm=AIzrcHcBAAAA&ccb=7-5&ig_cache_key=GJVNXxwNx6-UzCEEACN25jgw6QMRbkULAAAB3203200j-ccb7-5&oh=00_Af1gwaRzZf3pGeth93A1aOXb1y-6WSFggdElELmvVclMVQ&oe=69DC3DAE&_nc_sid=e9f0d8",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "Beyoncé",
      "social_context": "Beyoncé"
    },
    {
      "strong_id__": "11830955",
      "pk": 11830955,
      "pk_id": "11830955",
      "id": "11830955",
      "username": "taylorswift",
      "full_name": "Taylor Swift",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3825454373149795026_11830955",
      "profile_pic_url": "https://scontent-ord5-3.cdninstagram.com/v/t51.82787-19/626626039_18625087675054956_4249858978563573242_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ord5-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEAbgw-a6QU8F3felfXpPVm1knG2Gh40utOm64ItYcZAmpM8JTQMh2RFC63S7B8hnM&_nc_ohc=lWhS5q1zaL4Q7kNvwHyBVeK&_nc_gid=68x_G3kHITvJqsLnRmBG2Q&edm=AIzrcHcBAAAA&ccb=7-5&ig_cache_key=GPeNWSVsO8gmaytCAPpFyWo5iPo6bmNDAQAB3203200j-ccb7-5&oh=00_Af1_btbqs6fd1efmas0tzn6R1i_e3j7o-Evu5om4Yv7M5w&oe=69DC1F3A&_nc_sid=e9f0d8",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "Taylor Swift",
      "social_context": "Taylor Swift"
    }
  ],
  "is_backup": false,
  "is_recommend_account": false,
  "chaining_upsell_cards": [],
  "follow_ranking_token": "b39dafd8534f4783927de6b8d9fb9d93|38340771762|chaining",
  "status": "ok"
}
```

</details>

---

### GET /v2/user/tag/medias

Get usertag medias

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/tag/medias?user_id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.user_tag_medias_v2(user_id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/tag/medias",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/tag/medias?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

<details>
<summary>Example response</summary>

```json
{
  "response": {
    "num_results": 21,
    "more_available": true,
    "items": [
      {
        "strong_id__": "1929261108986102451_429173",
        "id": "1929261108986102451_429173",
        "fbid": 18006729904037433,
        "deleted_reason": 0,
        "client_cache_key": "MTkyOTI2MTEwODk4NjEwMjQ1MQ==.3",
        "integrity_review_decision": "approved",
        "pk": "1929261108986102451",
        "has_delayed_metadata": false,
        "mezql_token": "",
        "should_request_ads": false,
        "has_privately_liked": false,
        "is_quiet_post": false,
        "collaborator_edit_eligibility": false,
        "share_count_disabled": false,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_visual_reply_commenter_notice_enabled": true,
        "subtype_name_for_REST__": "XDTFeedMedia",
        "has_views_fetching_on_search_grid": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                50179,
                100358
              ],
              "height": 1334,
              "scans_profile": "e35",
              "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwHbdBld&_nc_oc=Adozu9YrkZP4Alpv0cq9_E9U12Lk7h4Y_wx_7mF1HpLXTokHdQMnkVwtZdgik2e05-c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=CglUWvnrmM8A_j4aaA9O1g&_nc_ss=7a3ba&oh=00_Af1NEtuVfCtKeqj7oprLfmgj5pQ0wLRXFHtUSpFFK9Ikuw&oe=69DC2D22",
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
              "url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwHbdBld&_nc_oc=Adozu9YrkZP4Alpv0cq9_E9U12Lk7h4Y_wx_7mF1HpLXTokHdQMnkVwtZdgik2e05-c&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=CglUWvnrmM8A_j4aaA9O1g&_nc_ss=7a3ba&oh=00_Af2p_hDkSc2zoUiaR52QCfL0vM--xGOfM0iUxszlLtAvvg&oe=69DC2D22",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 1,
        "original_width": 1080,
        "original_height": 1334,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMWM5ZDBjNWE3OTlmNDRmZjkwZWYyZWViYjJkZjdjMzIxOTI5MjYxMTA4OTg2MTAyNDUxIiwic2VydmVyX3Rva2VuIjoiMTc3NTY1Nzc0NTU4N3wxOTI5MjYxMTA4OTg2MTAyNDUxfDI5NzcwMDI1OTExfDgxNmQ0N2M2YTM2NzYzNTk0ZjRhNDBlNzlhMTRlNzE0YWU3NTFiMzVlZWNkZGQ1NjYxMDc5MGFhOTRkM2IwYjQifSwic2lnbmF0dXJlIjoiIn0=",
        "music_metadata": {
          "audio_type": null,
          "music_canonical_id": "0",
          "pinned_media_ids": null,
          "music_info": null,
          "original_sound_info": null
        },
        "clips_tab_pinned_user_ids": [],
        "is_open_to_public_submission": false,
        "is_social_ufi_disabled": false,
        "timeline_pinned_user_ids": [],
        "taken_at": 1544205867,
        "usertags": [
          {
            "user": {
              "pk": "1709655155",
              "id": "1709655155",
              "username": "fromwhereidrone",
              "full_name": "From Where I Drone®",
              "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.2885-19/11426732_990789794299104_1839082617_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFV1PWMBBmhw_dgZCa3ovOs1gbFQ2qOYWHLtEHLBie3shj1H84AoRz_-tANV5yciEM&_nc_ohc=Nk9rpOO4FmUQ7kNvwFHyQbf&_nc_gid=CglUWvnrmM8A_j4aaA9O1g&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GKxbrgDgfLw5HoUDAHksnm0AAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af3kmYZBZ0J2k8FTO6nu-YF962HlS5wsNQGZz09V7bY8Iw&oe=69DC3E73&_nc_sid=a8b8e2",
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": false
            },
            "x": 0.9639999866000001,
            "y": 0.0160000008
  // ... truncated
```

</details>

---

### GET /v2/user/videos

Get part of user videos with cursor (default 50 media per request)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | No | Id of user account |
| `page_id` | string | No | Use value of field `next_page_id` from response for getting next page |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/user/videos?user_id=787132"
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/user/videos",
        headers=headers,
        params={"user_id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/user/videos?user_id=787132",
      { headers: { "x-access-key": "YOUR_TOKEN" } }
    );
    const data = await response.json();
    ```

---

### GET /v2/userstream/by/id

Get userstream (info) by id. Returns user stream data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Id |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/userstream/by/id?id=787132"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.userstream_by_id_v2(id="787132")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/userstream/by/id",
        headers=headers,
        params={"id": "787132"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/userstream/by/id?id=787132",
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
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "id": "787132",
        "full_name": "National Geographic",
        "username": "natgeo",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHM4ROtobMi0hk9eGv3l4kquEvdKI9zbzVwmKQ9sb2aVniexlNj1qpiLV4tswHzl3Y&_nc_ohc=XbeNvhLXv28Q7kNvwH5l3lh&_nc_gid=U_X9QNT-fOeGgpk1YgTB_A&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af24SzAlMbSTel4wZqQY5Tg8XzNUulxNrjY5158_94sShQ&oe=69DC19A9&_nc_sid=6c5dea"
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "pk": 787132,
        "is_opal_enabled": false,
        "eligible_for_text_app_activation_badge": false,
        "highlights_tray_type": "DEFAULT",
        "account_type": 2,
        "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHM4ROtobMi0hk9eGv3l4kquEvdKI9zbzVwmKQ9sb2aVniexlNj1qpiLV4tswHzl3Y&_nc_ohc=XbeNvhLXv28Q7kNvwH5l3lh&_nc_gid=U_X9QNT-fOeGgpk1YgTB_A&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af24SzAlMbSTel4wZqQY5Tg8XzNUulxNrjY5158_94sShQ&oe=69DC19A9&_nc_sid=6c5dea",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn-ksESaaA1QoKVKHdpPrqGFIMZ5D5QovYuGBKY9Rwd3u07O4auIKc0VHRemc_aem_fFk8pPe9PfvdfEkW2IQugA&e=AT51vx8RiY9bbfCPKj2wdyXM3fvLt_xD7aWjevW7_fNljFO87r-iEk5nG46JYPfEMVpz3Xy4jjJHboVM6w9IwWedCQjD3DQczSZ0vnU7-Q",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "creation_source": "NONE"
          }
        ],
        "is_call_to_action_enabled": false,
        "is_business": true,
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "is_profile_picture_expansion_enabled": true,
        "show_schools_badge": null,
        "text_post_app_badge_label": "natgeo",
        "text_post_new_post_count": 5,
        "text_post_app_joiner_number": 672534,
        "text_post_app_joiner_number_label": "672,534",
        "recon_features": {
          "enable_recon_cta": true
        },
        "media_count": 31529,
        "trial_clips_rate_limiting": {
          "warning_title": "You can share one more trial reel",
          "at_limit_title": "You've reached the limit",
          "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
          "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
          "count": 20
        },
        "is_prime_onboarding_account": false,
        "is_onboarding_account": false,
        "show_ring_award": false,
        "ring_creator_metadata": {},
        "is_verified": true,
        "is_ring_creator": false,
        "is_private": false,
        "username": "natgeo",
        "full_name": "National Geographic",
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "following_count": 193,
        "follower_count": 274984404
      },
      "status": "ok"
    }
  // ... truncated
```

</details>

---

### GET /v2/userstream/by/username

Get userstream (info) by username. Returns user stream data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `username` | string | Yes | Username |

=== "curl"

    ```bash
    curl -H "x-access-key: YOUR_TOKEN" \
      "https://api.hikerapi.com/v2/userstream/by/username?username=natgeo"
    ```

=== "Python"

    ```python
    from hikerapi import Client

    cl = Client(token="YOUR_TOKEN")
    result = cl.userstream_by_username_v2(username="natgeo")
    ```

=== "Python (requests)"

    ```python
    import requests

    headers = {"x-access-key": "YOUR_TOKEN"}
    response = requests.get(
        "https://api.hikerapi.com/v2/userstream/by/username",
        headers=headers,
        params={"username": "natgeo"},
    )
    print(response.json())
    ```

=== "JavaScript"

    ```javascript
    const response = await fetch(
      "https://api.hikerapi.com/v2/userstream/by/username?username=natgeo",
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
      "user": {
        "strong_id__": "787132",
        "pk": 787132,
        "id": "787132",
        "full_name": "National Geographic",
        "username": "natgeo",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "profile_pic_url": "https://scontent-den2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-den2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHFnKfRMU3_hQxwEyJN1Qu66EXmpJ2FyVEUbqZydSNGlU10A9CtGFo5aiM9NJy_IXQ&_nc_ohc=XbeNvhLXv28Q7kNvwGKeTsx&_nc_gid=_GCAKPbQ_805pzu1rUYdtA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3wB3buKb7-2ovX5eDyUhu4Wakqh9F1uiTxnSsheqJH6g&oe=69DC19A9&_nc_sid=164c1d"
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "pk": 787132,
        "is_opal_enabled": false,
        "eligible_for_text_app_activation_badge": false,
        "highlights_tray_type": "DEFAULT",
        "account_type": 2,
        "profile_pic_url": "https://scontent-den2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-den2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHFnKfRMU3_hQxwEyJN1Qu66EXmpJ2FyVEUbqZydSNGlU10A9CtGFo5aiM9NJy_IXQ&_nc_ohc=XbeNvhLXv28Q7kNvwGKeTsx&_nc_gid=_GCAKPbQ_805pzu1rUYdtA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3wB3buKb7-2ovX5eDyUhu4Wakqh9F1uiTxnSsheqJH6g&oe=69DC19A9&_nc_sid=164c1d",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnKtvHB2qwuv9AHF8aBB_8DRsDWdEFQ0NBLffSCmhNw5JXrQGVKn0uU-eSyxo_aem_jHN93FiBE_niacPLcjvPVA&e=AT65Gk9GZ0fQtKBBNfQy8jZqXkvpV67LNaDuDabGBJScljbY1w2kF-3zdy5IojKVYT2DyTjQwRe2DCY0MQmB5aq6bnv7RB5vXJgCTH-jZQ",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnKtvHB2qwuv9AHF8aBB_8DRsDWdEFQ0NBLffSCmhNw5JXrQGVKn0uU-eSyxo_aem_jHN93FiBE_niacPLcjvPVA",
            "creation_source": "NONE"
          }
        ],
        "is_call_to_action_enabled": false,
        "is_business": true,
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "show_shoppable_feed": false,
        "seller_shoppable_feed_type": "none",
        "is_profile_picture_expansion_enabled": true,
        "show_schools_badge": null,
        "text_post_app_badge_label": "natgeo",
        "text_post_new_post_count": 5,
        "text_post_app_joiner_number": 672534,
        "text_post_app_joiner_number_label": "672,534",
        "recon_features": {
          "enable_recon_cta": true
        },
        "media_count": 31529,
        "trial_clips_rate_limiting": {
          "warning_title": "You can share one more trial reel",
          "at_limit_title": "You've reached the limit",
          "warning_body": "You've almost reached the limit. Once you share this trial reel, you'll need to wait up to 24 hours to start using trial reels again.",
          "at_limit_body": "You've shared the maximum number of trial reels allowed within 24 hours. You can share this reel to everyone now as a regular reel or wait up to 24 hours to share it as a trial reel.",
          "count": 20
        },
        "is_prime_onboarding_account": false,
        "is_onboarding_account": false,
        "show_ring_award": false,
        "ring_creator_metadata": {},
        "is_verified": true,
        "is_ring_creator": false,
        "is_private": false,
        "username": "natgeo",
        "full_name": "National Geographic",
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "following_count": 193,
        "follower_count": 274984404
  // ... truncated
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-user){ target=_blank }
