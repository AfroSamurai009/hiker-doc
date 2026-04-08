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
        "count": 274988519
      },
      "edge_follow": {
        "count": 193
      },
      "profile_pic_url": "https://scontent-mxp1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mxp1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEEX0tGLO9Bz_w00ltZuUhdnyDjUVkBtN4f5h5NqQZDIKsPFVdZbWm97fEPmHX8RPw&_nc_ohc=XbeNvhLXv28Q7kNvwFNVXRo&_nc_gid=LLYKg659-tMBDlvTVz8cAw&edm=AKralEIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af35Z8L18ze4XmyenqgmfAXKceVSXXBRC5OCMdwuRgRbKQ&oe=69DC51E9&_nc_sid=2fe71f",
      "profile_pic_url_hd": "https://scontent-mxp1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s640x640_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-mxp1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEEX0tGLO9Bz_w00ltZuUhdnyDjUVkBtN4f5h5NqQZDIKsPFVdZbWm97fEPmHX8RPw&_nc_ohc=XbeNvhLXv28Q7kNvwFNVXRo&_nc_gid=LLYKg659-tMBDlvTVz8cAw&edm=AKralEIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB6406400j-ccb7-5&oh=00_Af3JIDkpGHmLnh3Tq_DyJzHcTVWI32gUBPzt5mnCaQgPHQ&oe=69DC51E9&_nc_sid=2fe71f",
      "edge_owner_to_timeline_media": {
        "count": 31529,
        "edges": [
          {
            "node": {
              "id": "3865659729796199935",
              "shortcode": "DWllQsJCPX_",
              "display_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwEp0241&_nc_oc=AdovkTgm6WAVEMVch5zmy0Cv2M4CPWcTE1hq2mWHyIaf_YK3zJUccVWhem60kyVL10U&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af1K8ookp7Gccuqn2lNOKoCZpjIN4cRU8893winJqh_kRA&oe=69DC65F1",
              "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwEp0241&_nc_oc=AdovkTgm6WAVEMVch5zmy0Cv2M4CPWcTE1hq2mWHyIaf_YK3zJUccVWhem60kyVL10U&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af1K8ookp7Gccuqn2lNOKoCZpjIN4cRU8893winJqh_kRA&oe=69DC65F1",
              "video_url": "https://scontent-lax7-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwFCQn07&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3m8UGfL7a0-qsPd8HsGXmVvX9qK3SZ7VCRTWwhSyQQIw&oe=69D84A2E",
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
                "count": 35859
              },
              "edge_media_preview_like": {
                "count": 35859
              }
            }
          },
          {
            "node": {
              "id": "3844732796656436386",
              "shortcode": "DVbPBu5AESi",
              "display_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwEOC7ON&_nc_oc=AdrGAm-1OPPZKPC05ltmEcbcpjQrQ9ZuVr80UperREXfLKeY-sZWW04NiqfSPkkXoxM&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af0k7bc8PAKyjcwmgKu_-VahuEojA6lQ8LqOzmxFp_Oybg&oe=69DC51CA",
              "thumbnail_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwEOC7ON&_nc_oc=AdrGAm-1OPPZKPC05ltmEcbcpjQrQ9ZuVr80UperREXfLKeY-sZWW04NiqfSPkkXoxM&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af0k7bc8PAKyjcwmgKu_-VahuEojA6lQ8LqOzmxFp_Oybg&oe=69DC51CA",
              "video_url": "https://scontent-lax3-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwH_cHm9&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0-Zkg78w-QyAClkKy_vVwcolDjownn024HZ5WjsNSckA&oe=69D848EB",
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
                "count": 614
              },
              "edge_liked_by": {
                "count": 66069
              },
              "edge_media_preview_like": {
                "count": 66069
              }
            }
          },
          {
            "node": {
              "id": "3870670793969876810",
              "shortcode": "DW3YpRVDb9K",
              "display_url": null,
              "thumbnail_url": null,
              "video_url": null,
              "__typename": "GraphSidecar",
              "product_type": "carousel_container",
              "title": "",
              "video_duration": 0.0,
              "video_view_count": 0,
              "edge_media_to_caption": {
                "edges": [
                  {
                    "node": {
                      "text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World"
                    }
                  }
                ]
              },
              "edge_media_to_comment": {
                "count": 104
              },
              "edge_liked_by": {
                "count": 39891
              },
              "edge_media_preview_like": {
                "count": 39891
              },
              "edge_sidecar_to_children": {
                "edges": [
                  {
                    "node": {
                      "__typename": "GraphImage",
                      "id": "3870670683399590370",
                      "shortcode": "DW3YnqWjRHi",
                      "display_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwFY29_b&_nc_oc=AdrLP4iKrJAF4r4yHOPW2QS1OsZssr1HUAnM2asLpzfsyR3OvQVEsWda4EpFY6EYRM4&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af1U1OYBg1pNFTZYviDCNX9IkF-bnC2FVqODJZZquY_6EQ&oe=69DC4AFB",
                      "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwFY29_b&_nc_oc=AdrLP4iKrJAF4r4yHOPW2QS1OsZssr1HUAnM2asLpzfsyR3OvQVEsWda4EpFY6EYRM4&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af1U1OYBg1pNFTZYviDCNX9IkF-bnC2FVqODJZZquY_6EQ&oe=69DC4AFB",
                      "video_url": null
                    }
                  },
                  {
                    "node": {
                      "__typename": "GraphImage",
                      "id": "3870670679968669302",
                      "shortcode": "DW3YnnKDV52",
                      "display_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwE6AjPP&_nc_oc=AdrZTKvS4qQG97HfE5JypO50eJMxEvd8S6mlLrnKTeOAKI-8i2fDFT14XkmL39aNzyw&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af0vKLuXY7mk9B8ftz1UU7yOA0xHNq4QNoa5uF7gtu-KkA&oe=69DC54D1",
                      "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwE6AjPP&_nc_oc=AdrZTKvS4qQG97HfE5JypO50eJMxEvd8S6mlLrnKTeOAKI-8i2fDFT14XkmL39aNzyw&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af0vKLuXY7mk9B8ftz1UU7yOA0xHNq4QNoa5uF7gtu-KkA&oe=69DC54D1",
                      "video_url": null
                    }
                  },
                  {
                    "node": {
                      "__typename": "GraphImage",
                      "id": "3870670694816531730",
                      "shortcode": "DW3Yn0_DcUS",
                      "display_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwEyuUgs&_nc_oc=AdrVcMo3rsbUsb1KSM-7BO1yCpcEK4rJ_RHN4YUyb7X8nrIFDM97x59D-HLBVaEAv4g&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af3cmKZSBYTRgeGVQX7UvMiqZLSyOb0-ctwKbJVdf0wZDw&oe=69DC46CA",
                      "thumbnail_url": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwEyuUgs&_nc_oc=AdrVcMo3rsbUsb1KSM-7BO1yCpcEK4rJ_RHN4YUyb7X8nrIFDM97x59D-HLBVaEAv4g&_nc_ad=z-m&_nc_cid=1155&_nc_zt=23&se=8&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=TeIUa_FlnA_LUX81GJdNbA&_nc_ss=7a3ba&oh=00_Af3cmKZSBYTRgeGVQX7UvMiqZLSyOb0-ctwKbJVdf0wZDw&oe=69DC46CA",
                      "video_url": null
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  }
}
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
    "profile_pic_url": "https://scontent-syd2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGzlJyWJV4bAUtAwK0D5Tv_Nvk67T4B_EFw1omN4VbyZ2JgXZJsbn9fiZQNaKAUvmM&_nc_ohc=XbeNvhLXv28Q7kNvwGNs_F-&_nc_gid=M5GuUGUJIzi4E9_Ghimo6g&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0P6tEBb3mm35WhlQIshe7j7_LgZkaxIW5vMC15VmnOxw&oe=69DC51E9&_nc_sid=6c5dea",
    "is_opal_enabled": false,
    "eligible_for_text_app_activation_badge": false,
    "highlights_tray_type": "DEFAULT",
    "account_type": 2,
    "bio_links": [
      {
        "link_id": 17954981494900183,
        "url": "http://visitstore.bio/natgeo",
        "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnjCt3QsV2yYf27bG10MurjkrXUrmFt14AQ_yXjjp2_wckw6vF5gAa3wEMCRY_aem_ikA8GU6dKBBDFHsnw9nQ7A&e=AT6W6kMB_QGf0mXNZ2_a8jYi9_jq29Rn3tdRIEsApbfyreXBXYJ8py2cDHaKzPDdev6ReS7aB-P39ocHE79yD2A8ey7lnNiwtxVIHCLWLg",
        "link_type": "external",
        "title": "",
        "media_type": "none",
        "image_url": "",
        "icon_url": "",
        "media_accent_color_hex": "",
        "is_pinned": false,
        "is_verified": false,
        "open_external_url_with_in_app_browser": true,
        "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnjCt3QsV2yYf27bG10MurjkrXUrmFt14AQ_yXjjp2_wckw6vF5gAa3wEMCRY_aem_ikA8GU6dKBBDFHsnw9nQ7A",
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
    "follower_count": 274988518,
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
    "ads_incentive_expiration_date": null,
    "ads_page_id": null,
    "ads_page_name": null,
    "account_category": "",
    "can_add_fb_group_link_on_profile": false,
    "can_use_affiliate_partnership_messaging_as_creator": false,
    "can_use_affiliate_partnership_messaging_as_brand": false,
    "has_gen_ai_personas_for_profile_banner": false,
    "has_guides": false,
    "highlight_reshare_disabled": false,
    "include_direct_blacklist_status": true,
    "is_direct_roll_call_enabled": true,
    "is_eligible_for_meta_verified_links_in_reels": false,
    "is_eligible_for_post_boost_mv_upsell": false,
    "is_meta_verified_related_accounts_display_enabled": false,
    "is_new_to_instagram": false,
    "is_profile_broadcast_sharing_enabled": true,
    "is_secondary_account_creation": false,
    "profile_type": 0,
    "is_coppa_enforced": false,
    "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
    "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
    "is_bestie": false,
    "latest_reel_media": 1775659002,
    "latest_besties_reel_media": 0,
    "account_badges": [],
    "has_highlight_reels": true,
    "is_creator_agent_enabled": false,
    "interop_messaging_user_fbid": 113671860027320,
    "profile_pic_id": "3865702555259028436_787132",
    "has_anonymous_profile_picture": false,
    "fan_club_info": {
      "autosave_to_exclusive_highlight": null,
      "connected_member_count": null,
      "fan_club_id": null,
      "fan_club_name": null,
      "has_created_ssc": null,
      "has_enough_subscribers_for_ssc": null,
      "is_fan_club_gifting_eligible": null,
      "is_fan_club_referral_eligible": null,
      "is_free_trial_eligible": null,
      "largest_public_bc_id": null,
      "subscriber_count": null,
      "should_show_playlists_in_profile_tab": null,
      "fan_consideration_page_revamp_eligiblity": null
    },
    "hd_profile_pic_url_info": {
      "height": 1080,
      "url": "https://scontent-syd2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE2IdMqzjuL5aXbRMlPWQFAMZ4cMbAQWszud3FUGslyxaT4emkpJjMs1OhlV5ch9EQ&_nc_ohc=XbeNvhLXv28Q7kNvwGNs_F-&_nc_gid=M5GuUGUJIzi4E9_Ghimo6g&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB0j-ccb7-5&oh=00_Af1aB-dfEASh--TxD3Cb_0P37d9-uaTlGmdzgZCSXqTbJA&oe=69DC51E9&_nc_sid=6c5dea",
      "width": 1080
    },
    "hd_profile_pic_versions": [
      {
        "height": 320,
        "url": "https://scontent-syd2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE2IdMqzjuL5aXbRMlPWQFAMZ4cMbAQWszud3FUGslyxaT4emkpJjMs1OhlV5ch9EQ&_nc_ohc=XbeNvhLXv28Q7kNvwGNs_F-&_nc_gid=M5GuUGUJIzi4E9_Ghimo6g&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB3203200j-ccb7-5&oh=00_Af3tULBvBwNckjhS9VfDUeVPa2J1nndqdJVpGOx_Nt-D5g&oe=69DC51E9&_nc_sid=6c5dea",
        "width": 320
      },
      {
        "height": 640,
        "url": "https://scontent-syd2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s640x640_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-syd2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE2IdMqzjuL5aXbRMlPWQFAMZ4cMbAQWszud3FUGslyxaT4emkpJjMs1OhlV5ch9EQ&_nc_ohc=XbeNvhLXv28Q7kNvwGNs_F-&_nc_gid=M5GuUGUJIzi4E9_Ghimo6g&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB6406400j-ccb7-5&oh=00_Af2t56k52G3c6Zk2AgoMIjq9fjoTDrJTX4pkOEiu1oEimQ&oe=69DC51E9&_nc_sid=6c5dea",
        "width": 640
      }
    ],
    "is_active_on_text_post_app": true,
    "is_cannes": false,
    "is_facebook_onboarded_charity": false,
    "is_favorite": false,
    "merchant_checkout_style": "none",
    "show_account_transparency_details": true,
    "transparency_product_enabled": false,
    "text_app_last_visited_time": null,
    "is_eligible_for_slide": false,
    "live_subscription_status": "default",
    "business_contact_method": "UNKNOWN",
    "category_id": "0",
    "city_id": "0",
    "city_name": "",
    "direct_messaging": "UNKNOWN",
    "instagram_location_id": "",
    "page_id": null,
    "public_email": "",
    "public_phone_country_code": "",
    "public_phone_number": "",
    "should_show_category": false,
    "should_show_public_contacts": true,
    "zip": "",
    "contact_phone_number": "",
    "has_music_on_profile": false,
    "has_videos": true,
    "has_views_fetching": true,
    "is_category_tappable": false,
    "is_eligible_for_creator_product_links": false,
    "is_eligible_for_lead_center": true,
    "is_eligible_for_schools_search_upsell": false,
    "is_eligible_for_smb_support_flow": true,
    "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
    "num_of_admined_pages": null,
    "page_name": "National Geographic",
    "professional_conversion_suggested_account_type": 3,
    "profile_context": "",
    "smb_support_partner": null,
    "show_all_highlights_as_selected_in_management_screen": false,
    "trial_clips_enabled": false,
    "enable_add_school_in_edit_profile": false,
    "shopping_post_onboard_nux_type": null,
    "fb_page_call_to_action_id": "",
    "address_street": "",
    "is_profile_audio_call_enabled": false,
    "displayed_action_button_partner": null,
    "smb_delivery_partner": null,
    "smb_support_delivery_partner": null,
    "displayed_action_button_type": null,
    "category": "",
    "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnBN2Mf43qq5VmNNX4o3iE_wnlj6QA6GwFaE7uwuDn2GtczOAOKtL7Wr64TA4_aem_0QC6DQEltE1uABMa3WJx2A&e=AT7NE0mYQA9VDmF308N2DPzf5bCStO4r1o7mAZFVe0MHZ8UgqyP2H4edJgCzhtKY6vj6hDUZUlrlWvy3Qm1EChbKHJBXej4hjE8nG0cR1w",
    "external_url": "http://visitstore.bio/natgeo",
    "active_standalone_fundraisers": {
      "total_count": 0,
      "fundraisers": []
    },
    "additional_business_addresses": [],
    "allow_manage_memorialization": false,
    "auto_expand_chaining": false,
    "avatar_status": {
      "has_avatar": false
    },
    "broadcast_chat_preference_status": {
      "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
      "is_broadcast_chat_creator": true,
      "notification_setting_type": 2
    },
    "can_use_branded_content_discovery_as_brand": false,
    "can_use_branded_content_discovery_as_creator": false,
    "can_use_paid_partnership_messaging_as_creator": false,
    "chaining_upsell_cards": [],
    "charity_profile_fundraiser_info": {
      "pk": 787132,
      "has_active_fundraiser": false,
      "is_facebook_onboarded_charity": false,
      "consumption_sheet_config": {
        "can_viewer_donate": false,
        "currency": null,
        "donation_disabled_message": null,
        "donation_url": null,
        "has_viewer_donated": null,
        "privacy_disclaimer": null,
        "profile_fundraiser_id": null,
        "you_donated_message": null,
        "donation_amount_config": {
          "default_selected_donation_value": null,
          "donation_amount_selector_values": [],
          "maximum_donation_amount": null,
          "minimum_donation_amount": null,
          "prefill_amount": null,
          "user_currency": null
        }
      }
    },
    "creator_shopping_info": {
      "linked_merchant_accounts": []
    },
    "follow_friction_type": 0,
    "has_active_charity_business_profile_fundraiser": false,
    "has_chaining": true,
    "has_collab_collections": false,
    "has_exclusive_feed_content": false,
    "instagram_pk": "787132",
    "is_profile_search_enabled": false,
    "is_eligible_for_meta_verified_links_in_post": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
    "is_eligible_for_meta_verified_multiple_addresses_creation": false,
    "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
    "is_eligible_for_meta_verified_related_accounts": false,
    "meta_verified_related_accounts_count": 0,
    "is_eligible_to_host_profile_reels_ads": false,
    "is_favorite_for_clips": false,
    "is_favorite_for_highlights": false,
    "is_in_canada": false,
    "is_interest_account": true,
    "is_memorialized": false,
    "is_potential_business": false,
    "is_regulated_news_in_viewer_location": false,
    "is_remix_setting_enabled_for_posts": true,
    "is_remix_setting_enabled_for_reels": true,
    "is_regulated_c18": false,
    "profile_overlay_info": {
      "overlay_format": "NONE",
      "bloks_payload": null
    },
    "is_stories_teaser_muted": false,
    "is_supervision_features_enabled": false,
    "is_whatsapp_linked": false,
    "mutual_followers_count": 0,
    "nametag": {
      "available_theme_colors": [
        -1,
        7747834,
        13828293
      ],
      "background_image_url": "",
      "emoji": "😀",
      "emoji_color": 0,
      "gradient": 2,
      "is_background_image_blurred": false,
      "mode": 0,
      "selected_theme_color": -1,
      "selfie_sticker": 0,
      "selfie_url": "",
      "theme_color": {
        "available_theme_colors": [
          {
            "display_label": "Default",
            "int_value": -1
          },
          {
            "display_label": "Purple",
            "int_value": 7747834
          },
          {
            "display_label": "Lavender",
            "int_value": 13828293
          }
        ],
        "selected_theme_color": {
          "display_label": "Default",
          "int_value": -1
        }
      }
    },
    "not_meta_verified_friction_info": {
      "label_friction_content": "Not Meta Verified",
      "is_eligible_for_label_friction": false
    },
    "open_external_url_with_in_app_browser": true,
    "pinned_channels_info": {
      "has_public_channels": false,
      "pinned_channels_list": []
    },
    "profile_context_facepile_users": [],
    "profile_context_links_with_user_ids": [],
    "profile_pic_genai_tool_info": [],
    "pronouns": [],
    "relevant_news_regulation_locations": [],
    "remove_message_entrypoint": false,
    "request_contact_enabled": false,
    "show_blue_badge_on_main_profile": true,
    "show_ig_app_switcher_badge": true,
    "disable_profile_shop_cta": false,
    "show_text_post_app_badge": true,
    "show_text_post_app_switcher_badge": true,
    "spam_follower_setting_enabled": true,
    "total_ar_effects": 0,
    "total_clips_count": 1,
    "upcoming_events": [],
    "whatsapp_number": "",
    "recs_from_friends": {
      "enable_recs_from_friends": false,
      "recs_from_friends_entry_point_type": "banner"
    },
    "adjusted_banners_order": [],
    "has_visible_media_notes": true,
    "is_open_to_collab": false,
    "is_daily_limit_blocking": false,
    "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF0-JYf8If9ScZ1RAKDXkmMONDBhoCxwK2GwtasnMMpN-M",
    "is_oregon_custom_gender_consented": false,
    "profile_reels_sorting_eligibility": "DISABLED",
    "nonpro_can_maybe_see_profile_hypercard": false,
    "should_show_tagged_tab": true,
    "posts_subscription_status": "default",
    "reels_subscription_status": "default",
    "stories_subscription_status": "default",
    "is_profile_wa_calling_enabled": false,
    "wa_calling_option_for_wa_linked": 0,
    "wa_calling_option_for_legacy_num": 0,
    "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
    "has_private_collections": true,
    "is_guardian_r_account_cannes_pair": false,
    "can_see_support_inbox": null,
    "has_fan_club_subscriptions": false,
    "show_wa_link_on_profile": false,
    "meta_verified_benefits_info": {
      "active_meta_verified_benefits": [],
      "is_eligible_for_meta_verified_content_protection": false,
      "is_eligible_for_ig_meta_verified_label": false
    },
    "existing_user_age_collection_enabled": true,
    "has_public_tab_threads": true,
    "is_eligible_for_meta_verified_label": true,
    "is_favorite_for_stories": false,
    "is_parenting_account": false,
    "show_post_insights_entry_point": true,
    "short_drama_creator": null,
    "short_drama_series_playlist_id": null,
    "short_drama_series_episode_count": null,
    "short_drama_series_seed_media_id": null,
    "short_drama_series_title": null,
    "short_drama_role": "NONE",
    "short_drama_series_profiles": [],
    "short_drama_producer_account": null,
    "moonshot_joiner_number": null,
    "is_creator_marketplace_badge_visible": false,
    "creator_marketplace_accounts_reached_metric": null,
    "school_affiliated_account_viewer_status": null,
    "qa_freeform_banner": null,
    "qa_freeform_banner_available_prompts": [
      {
        "prompt": "CURRENT_OBSESSION",
        "display_text": "Current obsession"
      },
      {
        "prompt": "DREAM_DESTINATION",
        "display_text": "Dream destination"
      },
      {
        "prompt": "PLAYING",
        "display_text": "Playing"
      }
    ],
    "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
    "can_message_pinned_carrera_interest_owner": true
  },
  "status": "ok"
}
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
    "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gE11bNUeW9bWv8vWDsskilEtf1Gpla1_NgHsEXuckFfA0tDCG2XNms5oBnhbudm8II&_nc_ohc=XbeNvhLXv28Q7kNvwEzvjdK&_nc_gid=AbCNwiEI4_GZ9faCYdKmIA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af14_t3rtUgiDMsgvxjQkWjtL0QwdSJysiJ0pqDjhusOAg&oe=69DC51E9&_nc_sid=164c1d",
    "is_opal_enabled": false,
    "eligible_for_text_app_activation_badge": false,
    "highlights_tray_type": "DEFAULT",
    "account_type": 2,
    "bio_links": [
      {
        "link_id": 17954981494900183,
        "url": "http://visitstore.bio/natgeo",
        "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn81HlHdmLUK9PTiHGuqVqZTLGziAP6W-iCUpOdtitaSitckeiAS4kX_x1XuA_aem_Q8Mt1-7fXcc91hG42W5vDw&e=AT7MPKfz8nr_v0vP_M5ejizGZBomAqJuxKeeSPu0J-qSNf6ZgZowFchiXgmN4hoDFHNkTqlBsknJh7lx5E_y6MGCuVYz1lkLIInmFR1rpQ",
        "link_type": "external",
        "title": "",
        "media_type": "none",
        "image_url": "",
        "icon_url": "",
        "media_accent_color_hex": "",
        "is_pinned": false,
        "is_verified": false,
        "open_external_url_with_in_app_browser": true,
        "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn81HlHdmLUK9PTiHGuqVqZTLGziAP6W-iCUpOdtitaSitckeiAS4kX_x1XuA_aem_Q8Mt1-7fXcc91hG42W5vDw",
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
    "follower_count": 274984771,
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
    "ads_incentive_expiration_date": null,
    "ads_page_id": null,
    "ads_page_name": null,
    "account_category": "",
    "can_add_fb_group_link_on_profile": false,
    "can_use_affiliate_partnership_messaging_as_creator": false,
    "can_use_affiliate_partnership_messaging_as_brand": false,
    "has_gen_ai_personas_for_profile_banner": false,
    "has_guides": false,
    "highlight_reshare_disabled": false,
    "include_direct_blacklist_status": true,
    "is_direct_roll_call_enabled": true,
    "is_eligible_for_meta_verified_links_in_reels": false,
    "is_eligible_for_post_boost_mv_upsell": false,
    "is_meta_verified_related_accounts_display_enabled": false,
    "is_new_to_instagram": false,
    "is_profile_broadcast_sharing_enabled": true,
    "is_secondary_account_creation": false,
    "profile_type": 0,
    "is_coppa_enforced": false,
    "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
    "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
    "is_bestie": false,
    "latest_reel_media": 1775659002,
    "latest_besties_reel_media": 0,
    "account_badges": [],
    "has_highlight_reels": true,
    "is_creator_agent_enabled": false,
    "interop_messaging_user_fbid": 113671860027320,
    "profile_pic_id": "3865702555259028436_787132",
    "has_anonymous_profile_picture": false,
    "fan_club_info": {
      "autosave_to_exclusive_highlight": null,
      "connected_member_count": null,
      "fan_club_id": null,
      "fan_club_name": null,
      "has_created_ssc": null,
      "has_enough_subscribers_for_ssc": null,
      "is_fan_club_gifting_eligible": null,
      "is_fan_club_referral_eligible": null,
      "is_free_trial_eligible": null,
      "largest_public_bc_id": null,
      "subscriber_count": null,
      "should_show_playlists_in_profile_tab": null,
      "fan_consideration_page_revamp_eligiblity": null
    },
    "hd_profile_pic_url_info": {
      "height": 1080,
      "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFIYS3bHttFcsPgGUekckpR6GvFKj_3IG9fa2JNoFgWpD_vnwhCoix2A8AQWC47VfM&_nc_ohc=XbeNvhLXv28Q7kNvwEzvjdK&_nc_gid=AbCNwiEI4_GZ9faCYdKmIA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB0j-ccb7-5&oh=00_Af2swknmA4jxJqPm89rp6oXztmmIKzGJG4xbL7DtCqc1Ug&oe=69DC51E9&_nc_sid=164c1d",
      "width": 1080
    },
    "hd_profile_pic_versions": [
      {
        "height": 320,
        "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFIYS3bHttFcsPgGUekckpR6GvFKj_3IG9fa2JNoFgWpD_vnwhCoix2A8AQWC47VfM&_nc_ohc=XbeNvhLXv28Q7kNvwEzvjdK&_nc_gid=AbCNwiEI4_GZ9faCYdKmIA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB3203200j-ccb7-5&oh=00_Af2OJTYj-r41FD45XS7eglpZoljTF2Xg419bi03pJ27O2g&oe=69DC51E9&_nc_sid=164c1d",
        "width": 320
      },
      {
        "height": 640,
        "url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s640x640_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFIYS3bHttFcsPgGUekckpR6GvFKj_3IG9fa2JNoFgWpD_vnwhCoix2A8AQWC47VfM&_nc_ohc=XbeNvhLXv28Q7kNvwEzvjdK&_nc_gid=AbCNwiEI4_GZ9faCYdKmIA&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB6406400j-ccb7-5&oh=00_Af30Qg9wQgdMiSqwjZjnxlKvh3LSxfiObBd_irg4jgIcJA&oe=69DC51E9&_nc_sid=164c1d",
        "width": 640
      }
    ],
    "is_active_on_text_post_app": true,
    "is_cannes": false,
    "is_facebook_onboarded_charity": false,
    "is_favorite": false,
    "merchant_checkout_style": "none",
    "show_account_transparency_details": true,
    "transparency_product_enabled": false,
    "text_app_last_visited_time": null,
    "is_eligible_for_slide": false,
    "live_subscription_status": "default",
    "business_contact_method": "UNKNOWN",
    "category_id": "0",
    "city_id": "0",
    "city_name": "",
    "direct_messaging": "UNKNOWN",
    "instagram_location_id": "",
    "page_id": null,
    "public_email": "",
    "public_phone_country_code": "",
    "public_phone_number": "",
    "should_show_category": false,
    "should_show_public_contacts": true,
    "zip": "",
    "contact_phone_number": "",
    "has_music_on_profile": false,
    "has_videos": true,
    "has_views_fetching": true,
    "is_category_tappable": false,
    "is_eligible_for_creator_product_links": false,
    "is_eligible_for_lead_center": true,
    "is_eligible_for_schools_search_upsell": false,
    "is_eligible_for_smb_support_flow": true,
    "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
    "num_of_admined_pages": null,
    "page_name": "National Geographic",
    "professional_conversion_suggested_account_type": 3,
    "profile_context": "",
    "smb_support_partner": null,
    "show_all_highlights_as_selected_in_management_screen": false,
    "trial_clips_enabled": false,
    "enable_add_school_in_edit_profile": false,
    "shopping_post_onboard_nux_type": null,
    "fb_page_call_to_action_id": "",
    "address_street": "",
    "is_profile_audio_call_enabled": false,
    "displayed_action_button_partner": null,
    "smb_delivery_partner": null,
    "smb_support_delivery_partner": null,
    "displayed_action_button_type": null,
    "category": "",
    "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGnmG_5BXr6OSmCcHJNc9ZOMKtiO5q1IMj6_RhDZaCZ16Vyb_4sR-wjvxiUopc_aem_qxAPrwDy-AaBHuNVU8nBEg&e=AT68pEjQdNyl-HB4a9D4t4pKnZYi0FHJ4iebrwKTDBN-hNNKU2dO0qhflnUzS_XSgwqVCm45qgLczh9syc8-VFyJXw3W2QTutxMdVUADQA",
    "external_url": "http://visitstore.bio/natgeo",
    "active_standalone_fundraisers": {
      "total_count": 0,
      "fundraisers": []
    },
    "additional_business_addresses": [],
    "allow_manage_memorialization": false,
    "auto_expand_chaining": false,
    "avatar_status": {
      "has_avatar": false
    },
    "broadcast_chat_preference_status": {
      "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
      "is_broadcast_chat_creator": true,
      "notification_setting_type": 2
    },
    "can_use_branded_content_discovery_as_brand": false,
    "can_use_branded_content_discovery_as_creator": false,
    "can_use_paid_partnership_messaging_as_creator": false,
    "chaining_upsell_cards": [],
    "charity_profile_fundraiser_info": {
      "pk": 787132,
      "has_active_fundraiser": false,
      "is_facebook_onboarded_charity": false,
      "consumption_sheet_config": {
        "can_viewer_donate": false,
        "currency": null,
        "donation_disabled_message": null,
        "donation_url": null,
        "has_viewer_donated": null,
        "privacy_disclaimer": null,
        "profile_fundraiser_id": null,
        "you_donated_message": null,
        "donation_amount_config": {
          "default_selected_donation_value": null,
          "donation_amount_selector_values": [],
          "maximum_donation_amount": null,
          "minimum_donation_amount": null,
          "prefill_amount": null,
          "user_currency": null
        }
      }
    },
    "creator_shopping_info": {
      "linked_merchant_accounts": []
    },
    "follow_friction_type": 0,
    "has_active_charity_business_profile_fundraiser": false,
    "has_chaining": true,
    "has_collab_collections": false,
    "has_exclusive_feed_content": false,
    "instagram_pk": "787132",
    "is_profile_search_enabled": false,
    "is_eligible_for_meta_verified_links_in_post": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet": false,
    "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
    "is_eligible_for_meta_verified_multiple_addresses_creation": false,
    "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
    "is_eligible_for_meta_verified_related_accounts": false,
    "meta_verified_related_accounts_count": 0,
    "is_eligible_to_host_profile_reels_ads": false,
    "is_favorite_for_clips": false,
    "is_favorite_for_highlights": false,
    "is_in_canada": false,
    "is_interest_account": true,
    "is_memorialized": false,
    "is_potential_business": false,
    "is_regulated_news_in_viewer_location": false,
    "is_remix_setting_enabled_for_posts": true,
    "is_remix_setting_enabled_for_reels": true,
    "is_regulated_c18": false,
    "profile_overlay_info": {
      "overlay_format": "NONE",
      "bloks_payload": null
    },
    "is_stories_teaser_muted": false,
    "is_supervision_features_enabled": false,
    "is_whatsapp_linked": false,
    "mutual_followers_count": 0,
    "nametag": {
      "available_theme_colors": [
        -1,
        7747834,
        13828293
      ],
      "background_image_url": "",
      "emoji": "😀",
      "emoji_color": 0,
      "gradient": 2,
      "is_background_image_blurred": false,
      "mode": 0,
      "selected_theme_color": -1,
      "selfie_sticker": 0,
      "selfie_url": "",
      "theme_color": {
        "available_theme_colors": [
          {
            "display_label": "Default",
            "int_value": -1
          },
          {
            "display_label": "Purple",
            "int_value": 7747834
          },
          {
            "display_label": "Lavender",
            "int_value": 13828293
          }
        ],
        "selected_theme_color": {
          "display_label": "Default",
          "int_value": -1
        }
      }
    },
    "not_meta_verified_friction_info": {
      "label_friction_content": "Not Meta Verified",
      "is_eligible_for_label_friction": false
    },
    "open_external_url_with_in_app_browser": true,
    "pinned_channels_info": {
      "has_public_channels": false,
      "pinned_channels_list": []
    },
    "profile_context_facepile_users": [],
    "profile_context_links_with_user_ids": [],
    "profile_pic_genai_tool_info": [],
    "pronouns": [],
    "relevant_news_regulation_locations": [],
    "remove_message_entrypoint": false,
    "request_contact_enabled": false,
    "show_blue_badge_on_main_profile": true,
    "show_ig_app_switcher_badge": true,
    "disable_profile_shop_cta": false,
    "show_text_post_app_badge": true,
    "show_text_post_app_switcher_badge": true,
    "spam_follower_setting_enabled": true,
    "total_ar_effects": 0,
    "total_clips_count": 1,
    "upcoming_events": [],
    "whatsapp_number": "",
    "recs_from_friends": {
      "enable_recs_from_friends": false,
      "recs_from_friends_entry_point_type": "banner"
    },
    "adjusted_banners_order": [],
    "has_visible_media_notes": true,
    "is_open_to_collab": false,
    "is_daily_limit_blocking": false,
    "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF09ILF2JoKWvnWMHw4fVBB2cAgCOEa0z7FVtP2buDgmLk",
    "is_oregon_custom_gender_consented": false,
    "profile_reels_sorting_eligibility": "CHECK_VIEWER_QE",
    "nonpro_can_maybe_see_profile_hypercard": false,
    "should_show_tagged_tab": true,
    "posts_subscription_status": "default",
    "reels_subscription_status": "default",
    "stories_subscription_status": "default",
    "is_profile_wa_calling_enabled": false,
    "wa_calling_option_for_wa_linked": 0,
    "wa_calling_option_for_legacy_num": 0,
    "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
    "has_private_collections": true,
    "is_guardian_r_account_cannes_pair": false,
    "can_see_support_inbox": null,
    "has_fan_club_subscriptions": false,
    "show_wa_link_on_profile": false,
    "meta_verified_benefits_info": {
      "active_meta_verified_benefits": [],
      "is_eligible_for_meta_verified_content_protection": false,
      "is_eligible_for_ig_meta_verified_label": false
    },
    "existing_user_age_collection_enabled": true,
    "has_public_tab_threads": true,
    "is_eligible_for_meta_verified_label": true,
    "is_favorite_for_stories": false,
    "is_parenting_account": false,
    "show_post_insights_entry_point": true,
    "short_drama_creator": null,
    "short_drama_series_playlist_id": null,
    "short_drama_series_episode_count": null,
    "short_drama_series_seed_media_id": null,
    "short_drama_series_title": null,
    "short_drama_role": "NONE",
    "short_drama_series_profiles": [],
    "short_drama_producer_account": null,
    "moonshot_joiner_number": null,
    "is_creator_marketplace_badge_visible": false,
    "creator_marketplace_accounts_reached_metric": null,
    "school_affiliated_account_viewer_status": null,
    "qa_freeform_banner": null,
    "qa_freeform_banner_available_prompts": [
      {
        "prompt": "CURRENT_OBSESSION",
        "display_text": "Current obsession"
      },
      {
        "prompt": "DREAM_DESTINATION",
        "display_text": "Dream destination"
      },
      {
        "prompt": "PLAYING",
        "display_text": "Playing"
      }
    ],
    "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
    "can_message_pinned_carrera_interest_owner": true
  },
  "status": "ok"
}
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
                  8908,
                  13363
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwE5dQqI&_nc_oc=AdoQzOlYsfUHdforfM7VPJvX3EGUg4ZBYI3TP50a3uWUgsLegKHSajH_yctBarkUoW4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af28Cio4tpULKbNIwD-5pvyU6RNkSae_FsQxV_xglfo5_Q&oe=69DC32B4",
                "width": 640,
                "is_spatial_image": false
              },
              "igtv_first_frame": {
                "estimated_scans_sizes": [
                  4454,
                  8908,
                  13363
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/661777154_4383082448594832_9021766415602217145_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=M6kuWOEgfC8Q7kNvwE5dQqI&_nc_oc=AdoQzOlYsfUHdforfM7VPJvX3EGUg4ZBYI3TP50a3uWUgsLegKHSajH_yctBarkUoW4&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af28Cio4tpULKbNIwD-5pvyU6RNkSae_FsQxV_xglfo5_Q&oe=69DC32B4",
                "width": 640,
                "is_spatial_image": false
              },
              "smart_frame": null
            },
            "candidates": [
              {
                "estimated_scans_sizes": [
                  18248,
                  36496,
                  54745
                ],
                "height": 1333,
                "scans_profile": "e35",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwFTYNFh&_nc_oc=Adp5ghrkUYa6j_a33RMue1XbuOd9w4VAdAXJQg1hRKthBy2zCeTgEOVJSpB1MkZUkkA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af2giIzEG-7gGX36ATKJtH6DXiXCc0KzADljBWqlIKTWpg&oe=69DC46E1",
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
                  "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/661377490_4446710915609804_6368747692439450584_n.jpg?_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=8YQN_m5Qfl0Q7kNvwEa5aja&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&oh=00_Af1iE8qv0smxzB5YO3Tbw0BjnzcwtsjPShj9wKb5p5E3Ug&oe=69DC46C6&_nc_sid=c024bc"
                ],
                "sprite_width": 1500,
                "thumbnail_duration": 0.578352380952381,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 60.727
              }
            }
          },
          "media_type": 2,
          "original_width": 1080,
          "original_height": 1920,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMDMxMGExNWM3N2JjNDc0ZDgzYWVjMzcwMTkzZjI3MzAzODcwMDI1NTMxMDkzODUwNDQwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwOTIzOHwzODcwMDI1NTMxMDkzODUwNDQwfDM1MTQ1NDQxMDI1fDNkNzZkNWU2NjAwZGQ5MDUyYzQ1YzJjZGZkZGYxMjViMGIzZGFmMzUzZjkyOTA4YjlhZDc3OTkzNzMxYmI5NTAifSwic2lnbmF0dXJlIjoiIn0=",
          "music_metadata": null,
          "has_tagged_users": true,
          "clips_tab_pinned_user_ids": [],
          "original_lang_for_translations": "en",
          "is_open_to_public_submission": false,
          "is_social_ufi_disabled": false,
          "timeline_pinned_user_ids": [],
          "taken_at": 1775566804,
          "photo_of_you": false,
          "can_see_insights_as_brand": false,
          "fundraiser_tag": {
            "has_standalone_fundraiser": false
          },
          "fb_user_tags": {
            "in": []
          },
          "media_overlay_info": null,
          "is_in_profile_grid": false,
          "profile_grid_control_enabled": false,
          "is_artist_pick": false,
          "media_notes": {
            "items": []
          },
          "product_type": "clips",
          "social_context": [],
          "subscribe_cta_visible": false,
          "creative_config": null,
          "is_cutout_sticker_allowed": false,
          "cutout_sticker_info": [],
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "meta_ai_suggested_prompts": [],
          "gen_ai_chat_with_ai_cta_info": null,
          "can_reply": false,
          "floating_context_items": [],
          "is_eligible_content_for_post_roll_ad": false,
          "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
          "eligible_insights_entrypoints": "NONE",
          "media_attributions_data": [],
          "media_ui_attributions_data": [],
          "media_ui_attributions_data_v2": [],
          "creator_product_link_infos": [],
          "is_eligible_for_poe": false,
          "is_eligible_for_organic_eager_refresh": false,
          "commerce_integrity_review_decision": "",
          "is_reuse_allowed": false,
          "logging_info_token": "GCBkZTFlNTIyYTIxYTE0NTRkOGNhZGU2MDA2MDU5Y2Q2MngDbmhhAA==",
          "boost_unavailable_identifier": null,
          "boost_unavailable_reason": null,
          "boost_unavailable_reason_v2": null,
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
              "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=XbeNvhLXv28Q7kNvwFKx7FQ&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3SqAb7JvL9cxArgf2vmRlvgA9GWggJzlzboQvHgbqoIA&oe=69DC51E9&_nc_sid=c024bc",
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
          "coauthor_producer_can_see_organic_insights": false,
          "invited_coauthor_producers": [],
          "collab_follow_button_info": {
            "show_follow_button": true,
            "is_owner_in_author_exp": true
          },
          "igbio_product": null,
          "is_paid_partnership": false,
          "reshare_count": 11398,
          "ig_media_sharing_disabled": false,
          "media_repost_count": 1195,
          "view_state_item_type": 128,
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
              "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663909\" FBManifestIdentifier=\"Fsrss50NKRbMrPbB5Z2pBSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1498046678354726a\" bandwidth=\"66810\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66810\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m78/AQOElke-XjvO2ixFipAMNby9AqC5CZmOcY8PcbQDmAwEGdrdvbD58TPi5A5RKS7WbXpTrVlZQip3DhNxjBI2vRela2S063MA11oc5y0.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=XLhOSrzrzoUQ7kNvwExqGo_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af2E-y8kYFKzRXe2KvBMFQVfwkKtNEWEk1fqNns2wto_HQ&amp;oe=69D8589E</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
              "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQPYF2mAhRbYzYMrI560MWB9XBJqAACyr7szcVbj1WFwaneaOm5BlFHWUM37z1AaOh6Oyo4BIq6T2yeHyTeibfXn.mp4?strext=1&_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=wTkgipWqtN0Q7kNvwEzrgCz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3cSbScc9phpozLmzGwHg0yE7HxlRev_RdSFfhNl_dQnA&oe=69DC5663",
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
                "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=ic5ODsLE2O8Q7kNvwEaDUHs&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af3uKXeWAadbKSJMT81a2MSwp7lB9fBA6Q1HpFmjnEyT6A&oe=69DC588C&_nc_sid=c024bc"
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
          "like_count": 50458,
          "top_likers": [],
          "hidden_likes_string_variant": -1,
          "caption": {
            "strong_id__": "18064245098343903",
            "bit_flags": 0,
            "created_at": 1775566807,
            "created_at_utc": 1775566807,
            "did_report_as_spam": false,
            "is_ranked_comment": false,
            "pk": "18064245098343903",
            "share_enabled": false,
            "content_type": "comment",
            "media_id": 3870025531093850440,
            "status": "Active",
            "type": 1,
            "user_id": 1029649300,
            "text": "Intruder alert! 🚨 Murder Hornets eat bees and their larvae, but these Asian honey bees aren't going to let their hive be destroyed without a fight. \n\n#SecretsOfTheBees is now streaming on @DisneyPlus and @hulu",
            "user": {
              "strong_id__": "1029649300",
              "pk": 1029649300,
              "pk_id": "1029649300",
              "id": "1029649300",
              "is_unpublished": false,
              "fbid_v2": 17841400519016088,
              "username": "natgeoanimals",
              "full_name": "National Geographic Animals",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3865698702530758137_1029649300",
              "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=ic5ODsLE2O8Q7kNvwEaDUHs&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af3uKXeWAadbKSJMT81a2MSwp7lB9fBA6Q1HpFmjnEyT6A&oe=69DC588C&_nc_sid=c024bc"
            },
            "is_covered": false,
            "private_reply_status": 0
          },
          "comment_count": 493,
          "comment_inform_treatment": {
            "action_type": null,
            "should_have_inform_treatment": false,
            "text": "",
            "url": null
          },
          "is_photo_comments_composer_enabled_for_author": false,
          "hide_view_all_comment_entrypoint": true,
          "locations": [],
          "play_count": 2594257,
          "ig_play_count": 2594257,
          "shop_routing_user_id": null,
          "featured_products": [],
          "are_remixes_crosspostable": true,
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "is_eligible_for_autodub": false,
          "is_eligible_for_autodub_upsell": false,
          "video_sticker_locales": [],
          "has_audio": true,
          "video_duration": 60.736000061035156,
          "is_dash_eligible": 1,
          "video_versions": [
            {
              "bandwidth": 1579353,
              "height": 1280,
              "id": "4284559321859069v",
              "type": 101,
              "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwFuMTpU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Rp0mv-s3s5v2GpU_lJWqYkucgQZ3jUAfoPB3mowMx-Q&oe=69D853EC",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            },
            {
              "bandwidth": 1579353,
              "height": 1280,
              "id": "4284559321859069v",
              "type": 102,
              "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwFuMTpU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Rp0mv-s3s5v2GpU_lJWqYkucgQZ3jUAfoPB3mowMx-Q&oe=69D853EC",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            },
            {
              "bandwidth": 1579353,
              "height": 1280,
              "id": "4284559321859069v",
              "type": 103,
              "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwFuMTpU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Rp0mv-s3s5v2GpU_lJWqYkucgQZ3jUAfoPB3mowMx-Q&oe=69D853EC",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            }
          ],
          "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.736S\" FBManifestTimestamp=\"1775663909\" FBManifestIdentifier=\"Fsrss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxs71ud+73IoDiqC0wu3LjwPImKTi/7u7BL6Zk9OwssAE/t+w5JmOxQSSmNLH6cjSBerci73BkuQFmJ6qw8jLyAaQj4fa8c2pB8T5kOjGrLcHhqCP7Nm3vAeqnN3Z9IWhDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.736S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:75.1\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"868003729587559v\" bandwidth=\"178266\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1353206\" FBPlaybackResolutionMos=\"0:100,360:56.7,480:54.4,720:53.2,1080:54.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.1,720:83.8,1080:76.2\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOsCsgfDrcn7Gsyqj04T425mPWmeq8-MeX07h5wqKf_ykgUXeoigrvG2JQeRp4Wd_MdM-ZLa9ORl60gPpY3e_JZiFGCQ5EL6KkXMnk.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Uh48tAtlw1sQ7kNvwH-IOr5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTc4MjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1fKlt9sjdNHi5B_OanQw1YZAjwBNFULlag2Dja9dvR9g&amp;oe=69DC51D7</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10892\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-78531\" FBFirstSegmentRange=\"1014-106281\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106282-221200\" FBPrefetchSegmentRange=\"1014-106281\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2092036534705762v\" bandwidth=\"240856\" codecs=\"av01.0.04M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1828322\" FBPlaybackResolutionMos=\"0:100,360:63.6,480:60.6,720:58.1,1080:58.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95,480:93.1,720:88.4,1080:81.1\" FBAbrPolicyTags=\"\" width=\"540\" height=\"960\" frameRate=\"11988/500\" FBQualityClass=\"sd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPRuSajZ_hFnjDpVSn1TY6XCtP7Zo9QzDsXmaKDU4mXL33dQv9cZzKhXl7Y_oeRcW9BNsObRl_FpdyfkSlu8ArGYU5-l43-uxy7_sg.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=-0z8YeyvyDgQ7kNvwH8hBhN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjQwODU2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af11tpGFCp66NrGMvdRnCbtEDNIHaw40s0nCOfuhX2JIRw&amp;oe=69DC6448</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-12646\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-105375\" FBFirstSegmentRange=\"1014-143432\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"143433-293318\" FBPrefetchSegmentRange=\"1014-143432\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1267502918297183v\" bandwidth=\"326220\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2476312\" FBPlaybackResolutionMos=\"0:100,360:69,480:66,720:63.5,1080:62.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.4,480:95.3,720:93.4,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBZheSdr-Op1k9B7pYwuciRaL5RCC2XcBVLkVwDPXAKrAhlrALgBooKgZk6nCMZz5AvNoGknQE18-kCW9-RNH_qVgCyawe5etIWbE.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=4ClMe01ofx0Q7kNvwGqPtyl&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MzI2MjIwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af06EvVn2Pa7kEaVpJIafoy0NGwojOoAAVW7HJoXN_sQVQ&amp;oe=69DC57D8</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-15483\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-142126\" FBFirstSegmentRange=\"1014-195190\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"195191-393663\" FBPrefetchSegmentRange=\"1014-195190\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1277876490344447v\" bandwidth=\"409602\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"3109259\" FBPlaybackResolutionMos=\"0:100,360:73,480:69.8,720:67,1080:65.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.7,480:96.7,720:95.4,1080:91.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxkQrl5cFyNncjOUGRq3XWMGmEnR7xzXjtdkfQlw0oreW4eSXmKA9eBGchHF9ByGL1ldZ-V_-LDFLMXxx4oytbIqVxuBwnRf-_tR0.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=5YrnOUUJMr4Q7kNvwES93oQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDA5NjAyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3F1NmtwwFfxUjPD3iHY1vSpkGeD-YWejTvDIQDPBiuqw&amp;oe=69DC3457</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16985\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-176185\" FBFirstSegmentRange=\"1014-244141\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"244142-487399\" FBPrefetchSegmentRange=\"1014-244141\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1848477759129484v\" bandwidth=\"540603\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"4103680\" FBPlaybackResolutionMos=\"0:100,360:77,480:74,720:70.7,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.24,480:98,720:97.4,1080:93.8\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQP2bW0aIfz99a4ARx2Q2fPwwUvSZlmUT1jxqzlfSPxqDy_XKQdY1A9deJRHs78I9y2z_ngWT2zfhDIKZ8-XZxBrQWFF9SDm2muWNnE.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=M35pMpEQ64sQ7kNvwGRgk5z&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NTQwNjAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0K5kRzRVZxp-aSPhatYjbUK2X7lTFKj9dFl_Y6Qw0nZg&amp;oe=69DC4906</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-18644\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-229855\" FBFirstSegmentRange=\"1014-321368\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"321369-630140\" FBPrefetchSegmentRange=\"1014-321368\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1588945909073417v\" bandwidth=\"681362\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"5172172\" FBPlaybackResolutionMos=\"0:100,360:80.4,480:76.6,720:73.2,1080:70.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.62,480:98.37,720:98.59,1080:95.5\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPuKZF2qKICjs08-k_G1H8gucF1aCSpWB6stiwUGXWNvKfX5Hm_pNaY4z6GYTR0ZmsxXCYFw3SGDP8cejuR9yWwzxdzv-J159SieXo.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=jd4D7ZlmtxMQ7kNvwHh-Nyr&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjgxMzYyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2D3z49D5UxqfpR88ZAsqVeF_cp6vTgu7s_vnhei-upEA&amp;oe=69DC4007</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-20592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-288895\" FBFirstSegmentRange=\"1014-405533\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"405534-781198\" FBPrefetchSegmentRange=\"1014-405533\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2061822901412808v\" bandwidth=\"912497\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6926702\" FBPlaybackResolutionMos=\"0:100,360:83.9,480:79.9,720:75.7,1080:72.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.077,480:98.93,720:99.306,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOjiwsO48rCaOF6m6s4bgg66iRhLGj5CKjR4DDmQ8T9kE2SvEWALkKtR50Wk2wGAMLc1Ws3pNhZSA9Y-QIiggu_wdfx_Bl0gwfgXDQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=fEsXwzzt-3AQ7kNvwHg3Ix_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6OTEyNDk3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1ow2v9_44dnBla9qLQZUggIU3_pxZq5y3GdKsP9eeooQ&amp;oe=69DC387A</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-23580\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-385865\" FBFirstSegmentRange=\"1014-544870\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"544871-1019514\" FBPrefetchSegmentRange=\"1014-544870\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1627595234965301v\" bandwidth=\"1235000\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"9374797\" FBPlaybackResolutionMos=\"0:100,360:86.4,480:82.8,720:77.8,1080:75.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.386,480:99.342,720:99.569,1080:99.632\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQM_p3Fq6rDYprSjJ8-MUlNGuff4JfkbCcT-LYH34W9o85XM1tWSkDeCFiP_sdVayBjAG_vXE0vYkHj0noxXvuN1eESyaLJtPOQ3Rmg.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=YK0MlTWtfdIQ7kNvwEYm9pM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTExMTA1NDExNjY0OSwiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTIzNTAwMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1OkoNTgLIGk_4MGkUZsnxUPyYlv8vlWBHpeKpjr9RsNw&amp;oe=69DC4156</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-32211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-518374\" FBFirstSegmentRange=\"1014-739833\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"739834-1405190\" FBPrefetchSegmentRange=\"1014-739833\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"4294793980782357a\" bandwidth=\"46380\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46380\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"353137\" FBPaqMos=\"87.87\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9GI-VauacxM2tCfwmiCOijhyH33zBWrM0Dr4JwD6i2FjABcTvvBGOXIydEyGVXVx6wkUjNuDAtapI93ufxCNL1tRZuAP-HRtBv50.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=Uo8ixeKIRUsQ7kNvwHYMLLq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjUxNCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3a-YQ2bqKWJAOe-LqSVEKYjKYhbeq8nICrINDPKE-Y7A&amp;oe=69DC60EA</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2136\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-14938\" FBFirstSegmentRange=\"1025-28400\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28401-56361\" FBPrefetchSegmentRange=\"1025-28400\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1256673039910436a\" bandwidth=\"74812\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"74812\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"568992\" FBPaqMos=\"89.65\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPA0IU4X5qD93OmmaSc1st7oueEaOmYwYCBhH3T3wOKN7WutkRMOZ1TDwC1ugFmlc5yKEeuM_xeo_vD4IzH2AbUDhA7xa2uuL_kti8.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=H10A9jvUydQQ7kNvwFXkwDt&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NDk0NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0xWmUxbJkKy8IkXkLkZP7hMMY1D7IhRVnMqIOUyMTRpQ&amp;oe=69DC6622</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2385\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21486\" FBFirstSegmentRange=\"1026-43481\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"43482-90615\" FBPrefetchSegmentRange=\"1026-43481\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"878713468520453a\" bandwidth=\"108352\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"108352\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"823623\" FBPaqMos=\"83.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOhb37d5jmr5MvSl8eT28PWBputzk-lecQ-RBUBedLEv96EozZbcoK_AR-dP3eFTj3ZDuOnoWe6DiibSbh3Vjc_rcGupQpI3Z2uCnA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=qIB9a-mC_CIQ7kNvwE5zASn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDg0ODUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1BowUxCyjbl27qzhJ4wDhYsZu2yDFxNURW90jLdPID5g&amp;oe=69DC55C7</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2395\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-30757\" FBFirstSegmentRange=\"1021-62738\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"62739-132935\" FBPrefetchSegmentRange=\"1021-62738\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"2103223183861763a\" bandwidth=\"143947\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"143947\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1093864\" FBPaqMos=\"87.00\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOgH1TOj2U7Ucn9wQoBfkebTHLZ9A_EoIFXsEJ2CkC1MsQUoWoasexRt0uwJQMyHQr8MmjxA15OisXxvCobhDmp05SCyaFAKp2_vFI.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Kg8UNuEeTkcQ7kNvwGYEPeP&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1MTExMDU0MTE2NjQ5LCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxNDQwODEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2mtcaeCp6RCeNkpHv2hYyRgOLzKZ_ptWMctpVl753Hcg&amp;oe=69DC5327</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-45040\" FBFirstSegmentRange=\"1021-86500\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"86501-176000\" FBPrefetchSegmentRange=\"1021-86500\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "number_of_qualities": 8,
          "video_codec": "av01.0.04M.08.0.111.01.01.01.0",
          "sharing_friction_info": {
            "should_have_sharing_friction": false,
            "bloks_app_url": null,
            "sharing_friction_payload": null
          },
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "clips_demotion_control": {
            "title": "Not interested",
            "enable_word_wrapping": true,
            "confirmation_icon": "none",
            "title_style": "normal",
            "confirmation_title": "Post hidden",
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_title_style": "large_left",
            "undo_style": "top_right",
            "confirmation_style": "bottomsheet",
            "followup_options": [
              {
                "text": "Don't suggest posts from natgeoanimals",
                "style": null,
                "id": "dislike_author",
                "data": "author_id:1029649300",
                "show_icon": true,
                "demotion_control": {
                  "confirmation_style": "bottomsheet",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_body": "We won't suggest posts from natgeoanimals.",
                  "undo_style": "inline"
                },
                "subtitle": null
              },
              {
                "text": "Don't suggest posts with certain words",
                "id": "hide_all_specific_words",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              },
              {
                "text": "Manage content preferences",
                "id": "control_center",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              }
            ]
          },
          "user": {
            "pk": "1029649300",
            "id": "1029649300",
            "username": "natgeoanimals",
            "full_name": "National Geographic Animals",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=ic5ODsLE2O8Q7kNvwEaDUHs&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af3uKXeWAadbKSJMT81a2MSwp7lB9fBA6Q1HpFmjnEyT6A&oe=69DC588C&_nc_sid=c024bc",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "community_notes_info": {
            "has_viewer_submitted_note": false,
            "note_submission_disabled": false,
            "enable_submission_friction": false,
            "is_eligible_for_request_a_note": true
          },
          "has_high_risk_gen_ai_inform_treatment": false,
          "caption_is_edited": false,
          "code": "DW1F7dciplI",
          "device_timestamp": 177556301582,
          "enable_media_notes_production": true,
          "filter_type": 0,
          "has_views_fetching": true,
          "is_post_live_clips_media": false,
          "like_and_view_counts_disabled": false,
          "original_media_has_visual_reply_media": false,
          "report_info": {
            "has_viewer_submitted_report": false
          },
          "is_organic_product_tagging_eligible": true,
          "can_viewer_reshare": true,
          "has_shared_to_fb": 0,
          "media_reposter_bottomsheet_enabled": false,
          "has_liked": false,
          "can_viewer_save": true,
          "is_comments_gif_composer_enabled": false,
          "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNO-KoYDS4Nu_FdVXPj1_VyJaxhzdQ2q8qYd4YOl03J5WVULX0xzH2mM7EybSl_N6sihv2sGJ3j6oYO92VMsd_L8YIErLTNevYzy_8.mp4?_nc_cat=111&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=jFVd35lIMfgQ7kNvwFuMTpU&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTUxMTEwNTQxMTY2NDksImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=7950cd8f08efb959&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8xNzQyNUNEMTVEMTgyRUVEMDJDMjBEM0MxN0E1NDBCRF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0JENENBODkwM0VEMkMzNTU3REQ3ODc4RjhGQUEzMEFFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACbSnMSEgoXlPxUCKAJDMywXQE5dDlYEGJMYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3Rp0mv-s3s5v2GpU_lJWqYkucgQZ3jUAfoPB3mowMx-Q&oe=69D853EC",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                18248,
                36496,
                54745
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwFTYNFh&_nc_oc=Adp5ghrkUYa6j_a33RMue1XbuOd9w4VAdAXJQg1hRKthBy2zCeTgEOVJSpB1MkZUkkA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af2giIzEG-7gGX36ATKJtH6DXiXCc0KzADljBWqlIKTWpg&oe=69DC46E1",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "thumbnail_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-15/662535863_18586813237017301_1847857854730647904_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDAyNTUzMTA5Mzg1MDQ0MDE4NTg2ODEzMjM0MDE3MzAx.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=XY6MLl_5VUYQ7kNvwFTYNFh&_nc_oc=Adp5ghrkUYa6j_a33RMue1XbuOd9w4VAdAXJQg1hRKthBy2zCeTgEOVJSpB1MkZUkkA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af2giIzEG-7gGX36ATKJtH6DXiXCc0KzADljBWqlIKTWpg&oe=69DC46E1",
          "location": null,
          "usertags": [],
          "taken_at_ts": 1775566804,
          "sponsor_tags": []
        }
      },
      {
        "media": {
          "strong_id__": "3869494020385423326_787132",
          "id": "3869494020385423326_787132",
          "disable_caption_and_comment": false,
          "fbid": 18312636319285904,
          "deleted_reason": 0,
          "client_cache_key": "Mzg2OTQ5NDAyMDM4NTQyMzMyNg==.3",
          "integrity_review_decision": "pending",
          "pk": "3869494020385423326",
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
                  3860,
                  7721,
                  11582
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/660753805_3353876781448969_8134495688569455809_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=JQlfi0W3VikQ7kNvwGN1EA4&_nc_oc=Adrykiwl8rLe1CVge645sp3aeDHIe6Tkr1OFkW4ixLAoTkn-hGhULKbPAcMKkc6CqJ8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af2CQyCPFnmS2HSD30W3l8U-Vl2KOuC2XTDb7rQQTRSIlQ&oe=69DC690C",
                "width": 640,
                "is_spatial_image": false
              },
              "igtv_first_frame": {
                "estimated_scans_sizes": [
                  3860,
                  7721,
                  11582
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.71878-15/660753805_3353876781448969_8134495688569455809_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=107&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=JQlfi0W3VikQ7kNvwGN1EA4&_nc_oc=Adrykiwl8rLe1CVge645sp3aeDHIe6Tkr1OFkW4ixLAoTkn-hGhULKbPAcMKkc6CqJ8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af2CQyCPFnmS2HSD30W3l8U-Vl2KOuC2XTDb7rQQTRSIlQ&oe=69DC690C",
                "width": 640,
                "is_spatial_image": false
              },
              "smart_frame": null
            },
            "candidates": [
              {
                "estimated_scans_sizes": [
                  13479,
                  26958,
                  40438
                ],
                "height": 1333,
                "scans_profile": "e35",
                "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwETTiLs&_nc_oc=AdrqQN5_AbV9IPYJWNvvUoBJ5Q2IhVY4KwFijAbkf7Vlc9g0bDaqFMo7LJ1FjSwZM4g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af3JP2noFoM_FX8W6vXVLFRV9fss2-KzLQ3sE4rtjAlkqg&oe=69DC6315",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 276,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_urls": [
                  "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/660026027_948875084508987_6617144121092333726_n.jpg?_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=a82HNH3lYl8Q7kNvwHziizS&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&oh=00_Af2iUtSS_N4xts0ebYxhrR9FeOoD1R6o1CPdGja0vatj_w&oe=69DC36E4&_nc_sid=c024bc"
                ],
                "sprite_width": 1500,
                "thumbnail_duration": 0.5279047619047619,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 55.43
              }
            }
          },
          "media_type": 2,
          "original_width": 1080,
          "original_height": 1920,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMDMxMGExNWM3N2JjNDc0ZDgzYWVjMzcwMTkzZjI3MzAzODY5NDk0MDIwMzg1NDIzMzI2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwOTI1NHwzODY5NDk0MDIwMzg1NDIzMzI2fDM1MTQ1NDQxMDI1fDY5MzI5ZWEwZTFjNDhkMGMzZjMwODU1MzFiOTYxNTczMjk5MzljYmQ1OTNlMDg2M2E1NWJlZTZkZDBjODE2ZjkifSwic2lnbmF0dXJlIjoiIn0=",
          "music_metadata": null,
          "has_tagged_users": true,
          "clips_tab_pinned_user_ids": [],
          "original_lang_for_translations": "en",
          "is_open_to_public_submission": false,
          "is_social_ufi_disabled": false,
          "timeline_pinned_user_ids": [],
          "taken_at": 1775502016,
          "photo_of_you": false,
          "can_see_insights_as_brand": false,
          "fundraiser_tag": {
            "has_standalone_fundraiser": false
          },
          "fb_user_tags": {
            "in": []
          },
          "media_overlay_info": null,
          "is_in_profile_grid": false,
          "profile_grid_control_enabled": false,
          "is_artist_pick": false,
          "media_notes": {
            "items": []
          },
          "product_type": "clips",
          "social_context": [],
          "subscribe_cta_visible": false,
          "creative_config": null,
          "is_cutout_sticker_allowed": false,
          "cutout_sticker_info": [],
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "meta_ai_suggested_prompts": [],
          "gen_ai_chat_with_ai_cta_info": null,
          "can_reply": false,
          "floating_context_items": [],
          "is_eligible_content_for_post_roll_ad": false,
          "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
          "eligible_insights_entrypoints": "NONE",
          "media_attributions_data": [],
          "media_ui_attributions_data": [],
          "media_ui_attributions_data_v2": [],
          "creator_product_link_infos": [],
          "is_eligible_for_poe": true,
          "is_eligible_for_organic_eager_refresh": false,
          "commerce_integrity_review_decision": "",
          "is_reuse_allowed": false,
          "logging_info_token": "GCBkZTFlNTIyYTIxYTE0NTRkOGNhZGU2MDA2MDU5Y2Q2MngDbmhhAA==",
          "boost_unavailable_identifier": null,
          "boost_unavailable_reason": null,
          "boost_unavailable_reason_v2": null,
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
              "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/543579175_18522017512026754_6429363176312325029_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NzQuYzIifQ&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=v0quYpmBS-oQ7kNvwGf9B1u&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GCdcZiCC8lNCrc1BAKXDEqC_rzlZbmNDAQAB1501500j-ccb7-5&oh=00_Af3USkSY7qCGln_RaTKUdiGWM9E11bc-0Yq1yCzFT4LTsg&oe=69DC4FB3&_nc_sid=c024bc",
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
              "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=zov5ST0QeW4Q7kNvwHqcAUl&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af1z4CbikOuN2wPzrlNhGwOcDwFpBoE0UHaF-_AB10OFMg&oe=69DC4D93&_nc_sid=c024bc",
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
          "coauthor_producer_can_see_organic_insights": false,
          "invited_coauthor_producers": [],
          "collab_follow_button_info": {
            "show_follow_button": true,
            "is_owner_in_author_exp": true
          },
          "igbio_product": null,
          "is_paid_partnership": false,
          "reshare_count": 470,
          "ig_media_sharing_disabled": false,
          "media_repost_count": 169,
          "view_state_item_type": 128,
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
              "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775663909\" FBManifestIdentifier=\"Fsrss50NKRbEl5Tt0tWmAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"929459223037410a\" bandwidth=\"60820\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"60820\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m78/AQN38tw9LWdIk_CWlJ0ze2Ayn07LgXtA4TMaLXc-6SODK58HBqKnlOKk8_LTSIHFsE3VGUlntYj8FPrehpb5VftWJE3s0U_LvQcQ0p4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=ZHLfVpYSwAwQ7kNvwFz3Tx8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo2MDk5MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af00PmeumdOGk1qnhWupXaS5yZ_Kte8ua3Pxl0Kh5igzYw&amp;oe=69D865B3</BaseURL><SegmentBase indexRange=\"824-1191\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
              "progressive_download_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m69/AQPKBMTmsUUaSlY28FrQeX4c4T6dijF6gtmaEyTFBN6pFY5bZ5DsQbcUjfr7pEffSR4eVHh1ugsHyMjH1cbkv8Kz.mp4?strext=1&_nc_cat=106&_nc_sid=8bf8fe&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=VR1-k3frXTsQ7kNvwHqBLaq&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af25ih1fVM3cD43lkePzYOH3e6tt9lOSsFX_ghsCsNFIrA&oe=69DC53CC",
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
                "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=XbeNvhLXv28Q7kNvwFKx7FQ&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3SqAb7JvL9cxArgf2vmRlvgA9GWggJzlzboQvHgbqoIA&oe=69DC51E9&_nc_sid=c024bc"
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
          "like_count": 11121,
          "top_likers": [],
          "hidden_likes_string_variant": -1,
          "caption": {
            "strong_id__": "18312640027285904",
            "bit_flags": 0,
            "created_at": 1775502018,
            "created_at_utc": 1775502018,
            "did_report_as_spam": false,
            "is_ranked_comment": false,
            "pk": "18312640027285904",
            "share_enabled": false,
            "content_type": "comment",
            "media_id": 3869494020385423326,
            "status": "Active",
            "type": 1,
            "user_id": 787132,
            "text": "In Hoppers, Piper Curda’s character Mabel explored her sense of wonder for the natural world with the help of hopping technology. For now, we still have to do it the old-fashioned way.\n\nSee Disney and Pixar’s new movie Hoppers, now playing, only in theaters, and step into wonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
            "user": {
              "strong_id__": "787132",
              "pk": 787132,
              "pk_id": "787132",
              "id": "787132",
              "is_unpublished": false,
              "fbid_v2": 17841400573960012,
              "username": "natgeo",
              "full_name": "National Geographic",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3865702555259028436_787132",
              "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=XbeNvhLXv28Q7kNvwFKx7FQ&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3SqAb7JvL9cxArgf2vmRlvgA9GWggJzlzboQvHgbqoIA&oe=69DC51E9&_nc_sid=c024bc"
            },
            "is_covered": false,
            "private_reply_status": 0
          },
          "comment_count": 65,
          "comment_inform_treatment": {
            "action_type": null,
            "should_have_inform_treatment": false,
            "text": "",
            "url": null
          },
          "is_photo_comments_composer_enabled_for_author": false,
          "hide_view_all_comment_entrypoint": true,
          "locations": [],
          "play_count": 1489028,
          "ig_play_count": 1489028,
          "shop_routing_user_id": null,
          "featured_products": [],
          "are_remixes_crosspostable": true,
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "is_eligible_for_autodub": false,
          "is_eligible_for_autodub_upsell": false,
          "video_sticker_locales": [],
          "has_audio": true,
          "video_duration": 55.44499969482422,
          "is_dash_eligible": 1,
          "video_versions": [
            {
              "bandwidth": 1113315,
              "height": 1280,
              "id": "2358585431274531v",
              "type": 101,
              "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwGDWUBa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0xrQzCXuOmaF8iiCN8L4hVOkQLmB91iAWc3DQ6V1UQUA&oe=69D86DB8",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            },
            {
              "bandwidth": 1113315,
              "height": 1280,
              "id": "2358585431274531v",
              "type": 102,
              "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwGDWUBa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0xrQzCXuOmaF8iiCN8L4hVOkQLmB91iAWc3DQ6V1UQUA&oe=69D86DB8",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            },
            {
              "bandwidth": 1113315,
              "height": 1280,
              "id": "2358585431274531v",
              "type": 103,
              "url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwGDWUBa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0xrQzCXuOmaF8iiCN8L4hVOkQLmB91iAWc3DQ6V1UQUA&oe=69D86DB8",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            }
          ],
          "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT55.445332S\" FBManifestTimestamp=\"1775663909\" FBManifestIdentifier=\"Fsrss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxtbm7f2IgpUD7OHlgsygpwOI9qGs6c69A4K35IPMyMEDsI3CoKTHvgSc252C4sXBBPyF6YussKgF9KKOwMXurwXYlsvU5LXeBdjS1K7XuegF6PTG0/GH9wW+g9vN5+3SByIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWAhQAEhQCAA==\"><Period id=\"0\" duration=\"PT55.445332S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:73.2\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"890639983950251v\" bandwidth=\"148183\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1026735\" FBPlaybackResolutionMos=\"0:100,360:77,480:75.4,720:74.2,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:93.1,720:92.5,1080:88.1\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQPxVTdb31AW_INujP1IDvNHV263--MPtveeFNN3GUuUVYCWKFeS7YZ9ZN2G12w1BpIi_FdawNocSzgpCnZ_RmsvfPjiy1uTBHb9oZw.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=Azv6S-cYlSkQ7kNvwFUWW1B&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTQ4MTgzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3OD98JrFrzB73psxHu4GT3uRmwuSZnC7i8rNHRiIl2dg&amp;oe=69DC684E</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-11627\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-38956\" FBFirstSegmentRange=\"1002-59102\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"59103-123876\" FBPrefetchSegmentRange=\"1002-59102\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1496166365471102v\" bandwidth=\"217161\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1504667\" FBPlaybackResolutionMos=\"0:100,360:81.6,480:79.3,720:77.4,1080:76.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.2,480:95.5,720:95.4,1080:91.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQP0yhiq2c2nWFCoYYsXHyN0n4pQ1H3Bf1PillRJPvA7F7s4T2vZEWWlnN1ab7wlhBx2qkPUdSqWmZq9YiCbgQr1iy6TnVK92GJFM7E.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=-GnWOEbhFFMQ7kNvwG7e-Wq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MjE3MTYxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2giv7DXcanzacxRxUt0RU5YGvfUdaGfNmB4McNY7i5-A&amp;oe=69DC5F5A</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-15046\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-52809\" FBFirstSegmentRange=\"1002-81554\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"81555-172554\" FBPrefetchSegmentRange=\"1002-81554\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1637064280544428v\" bandwidth=\"297468\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2061099\" FBPlaybackResolutionMos=\"0:100,360:85.4,480:83.2,720:81,1080:79.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.5,480:97.1,720:97.8,1080:94\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNmpoeNdw7yb2DNMihh-Q2G15Y477O-Sk1OLg5Yvc1SF5s2DvEEWcyZxNMIPHB9gTiEJuesLauW023efqZ9CuKWYNgVahVJF3UIkRc.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=DWIM7dIPpcYQ7kNvwEzn_f8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mjk3NDY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1r9roB80CO5jJc_73-QaD24wJcZWOZ8mFgptS92WMz9Q&amp;oe=69DC3FEE</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-18788\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-68106\" FBFirstSegmentRange=\"1002-106801\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"106802-227120\" FBPrefetchSegmentRange=\"1002-106801\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"930746796390518v\" bandwidth=\"386132\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2675439\" FBPlaybackResolutionMos=\"0:100,360:87.4,480:85.4,720:83.2,1080:81\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.11,480:98,720:98.9,1080:95.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOqmazZV0GgC-FMAgX5Uo4Hzr4dpsUwPLWUSkWVzIH2EIopdalxgjleoQbUfcUfP1apdP-4Gsa_iSGhTS3l313F1z6FbA8TyS6K2AY.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=XpZ2XTBJDXAQ7kNvwFGs7Lc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Mzg2MTMyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2Sv0-xGwg5EOwsNOePBVZV5rUtwSWKIU4agxvBXlexvg&amp;oe=69DC5F0C</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-22235\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-83355\" FBFirstSegmentRange=\"1002-132950\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"132951-285253\" FBPrefetchSegmentRange=\"1002-132950\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1263463985333080v\" bandwidth=\"479911\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3325212\" FBPlaybackResolutionMos=\"0:100,360:88.9,480:86.9,720:84.7,1080:82.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.46,480:98.4,720:99.414,1080:96.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN5Sl_4u8bg21xVtk-cIUfm9Z6DIbmrVvFA9a9N55F9NWJNHo03righvcgXtgSk_3JVH4wvKy4OTeNsgcwEtoacof_IARGxdKkAT-A.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=P7dFgXaWfIwQ7kNvwHfUsxV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NDc5OTExLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3RpcL39bcjdD4KbnCcOnQZzL4oBcFFFA_Iz-Ot5Onrnw&amp;oe=69DC5DE8</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-26049\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-100642\" FBFirstSegmentRange=\"1002-162120\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"162121-346006\" FBPrefetchSegmentRange=\"1002-162120\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1669194164264244v\" bandwidth=\"600336\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4159614\" FBPlaybackResolutionMos=\"0:100,360:90.2,480:88.2,720:86,1080:83.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.75,480:98.79,720:99.619,1080:97.2\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOkSM-p5C4-U6nKoTCQGR9QEo9t8_5IVg-ngkZWi13nRqVLUyRlAs1Es-YozyB9s8bjtNsK18hWCL1Of88sI3ZDe_gO2S45lP4yjWI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=8zqHITencNwQ7kNvwE4TBX_&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6NjAwMzM2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0avNlPBzs_KMfxjhEBQXWEUoy6HYLpS19pxWeWjMsY9Q&amp;oe=69DC3AC3</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-30771\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-121891\" FBFirstSegmentRange=\"1002-198284\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"198285-422683\" FBPrefetchSegmentRange=\"1002-198284\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"988608596839873v\" bandwidth=\"797098\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"5522936\" FBPlaybackResolutionMos=\"0:100,360:91.3,480:89.4,720:87.2,1080:84.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.026,480:99.172,720:99.732,1080:97.9\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMf3Rx8OOzEgPrCPNBR-0Nt-fwNaR6LdwmdWPUwzv4ulTwm_6h2bijtJ5Bjd87z0Jr-dXFj9FkGKtlRGWG6WeJW59Fiu3efb5LsrRI.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=B11mdo9l0D0Q7kNvwFKwwVK&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6Nzk3MDk4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3bPDxpeaz2GRJ6AKg2Db5CNu0v9fDYE-NBr6Y3TSlufw&amp;oe=69DC4992</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-37057\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-156105\" FBFirstSegmentRange=\"1002-256214\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"256215-544176\" FBPrefetchSegmentRange=\"1002-256214\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2152531255582943v\" bandwidth=\"1154217\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"7997347\" FBPlaybackResolutionMos=\"0:100,360:92.4,480:90.7,720:88.4,1080:87\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.557,480:99.564,720:99.814,1080:99.824\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQNSJdZpIRgVNqEBZdYq3cRarDru00HEWTghNg_iisXPQJn1ZojfEEAKYKMxJ1XCUfUglkRb6_gx6l6OzyKpZWsTXEQRU05M7RCeihQ.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=K8EwAJQ3wUIQ7kNvwHg9lwv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTQ0NDcyMzExMDYwMywiYXNzZXRfYWdlX2RheXMiOjEsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwiYml0cmF0ZSI6MTE1NDIxNywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1dQA3ZqpSojW49kDWdBOhLS-Y1CQcW1SOS8BsDIUSrtg&amp;oe=69DC40FD</BaseURL><SegmentBase indexRange=\"826-1001\" timescale=\"11988\" FBMinimumPrefetchRange=\"1002-50470\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1002-211892\" FBFirstSegmentRange=\"1002-345895\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"345896-752596\" FBPrefetchSegmentRange=\"1002-345895\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1615007113110956a\" bandwidth=\"45829\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"45829\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"318635\" FBPaqMos=\"90.73\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOq8zAQzpeRCoSQuovKRKQeNbycFlDBjsuggCgJzVUNsydkP6wpqSMV87VACc6egwIxdyoZ9qyuATjsxvSkWgWUtLCaKeDUW5vI2l0.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=n8c3OFNcOe4Q7kNvwGmTz49&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo0NTk3NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af34Mk8nZate6trfa81MS94j3f0vBPB9pEYcUL3Ai3EDdw&amp;oe=69DC5B70</BaseURL><SegmentBase indexRange=\"837-1012\" timescale=\"48000\" FBMinimumPrefetchRange=\"1013-2182\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1013-15598\" FBFirstSegmentRange=\"1013-28913\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"28914-57244\" FBPrefetchSegmentRange=\"1013-28913\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1270034985105102a\" bandwidth=\"72011\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"72011\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"500096\" FBPaqMos=\"90.72\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNETgTPe23OWiy-KGFj4O0xaNmi9xW8k8We4jlz_Lesh43O4RfyZWEg4kgQ77avCmAh4dhCO9ERkZrtXpEBa1nLDn-iaNXSGANeubo.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=wOOs-JEmecsQ7kNvwEir9vS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjo3MjE1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1nJcj8IfnjkwikkJmXFgDg8QRHcqQDXRpAd2jwp9IOdQ&amp;oe=69DC5EFF</BaseURL><SegmentBase indexRange=\"838-1013\" timescale=\"48000\" FBMinimumPrefetchRange=\"1014-2538\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-26077\" FBFirstSegmentRange=\"1014-48598\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48599-97300\" FBPrefetchSegmentRange=\"1014-48598\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"979919517793668a\" bandwidth=\"103761\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"103761\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"720138\" FBPaqMos=\"88.08\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNOpf9BEo2_A4jYtakOEtpNQQZDYD9C0aIFAN-Q6y8Ina7CtFSkF_92RvlAvk1DGfzRoyEa6eCluUBrw77Kir2QY9JUObENLk8IZsE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=sGdWzzK2ve0Q7kNvwEEEE3m&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMDM5MDYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af38dJo8vygbAJzQANGsFFBIKc2L62cSY5gHNn-0w_ANAg&amp;oe=69DC564E</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2467\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-36815\" FBFirstSegmentRange=\"1009-70144\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"70145-139522\" FBPrefetchSegmentRange=\"1009-70144\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1512628090423482a\" bandwidth=\"134031\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"134031\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"929932\" FBPaqMos=\"90.49\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQMDkCHmLVEnsU6T5_aC7ZlGvMakuRW1O3OnJZfxZuCHE1fs0cf1weWXn_tPspjek6E1p7CHcVLpGZLRSFGGTuIaxYNUE1SlwG3YTc4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=sKJdfZK9eLkQ7kNvwHIqDY5&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1NDQ0NzIzMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MSwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjU1LCJiaXRyYXRlIjoxMzQxNzYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af22CvAV_cjzmbEc86CAjxyuMtagfbxin8bqDvTtZ5KtGg&amp;oe=69DC5209</BaseURL><SegmentBase indexRange=\"833-1008\" timescale=\"48000\" FBMinimumPrefetchRange=\"1009-2532\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1009-44659\" FBFirstSegmentRange=\"1009-85613\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85614-170092\" FBPrefetchSegmentRange=\"1009-85613\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "number_of_qualities": 8,
          "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
          "sharing_friction_info": {
            "should_have_sharing_friction": false,
            "bloks_app_url": null,
            "sharing_friction_payload": null
          },
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "clips_demotion_control": {
            "title": "Not interested",
            "enable_word_wrapping": true,
            "confirmation_icon": "none",
            "title_style": "normal",
            "confirmation_title": "Post hidden",
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_title_style": "large_left",
            "undo_style": "top_right",
            "confirmation_style": "bottomsheet",
            "followup_options": [
              {
                "text": "Don't suggest posts from natgeo",
                "style": null,
                "id": "dislike_author",
                "data": "author_id:787132",
                "show_icon": true,
                "demotion_control": {
                  "confirmation_style": "bottomsheet",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_body": "We won't suggest posts from natgeo.",
                  "undo_style": "inline"
                },
                "subtitle": null
              },
              {
                "text": "Don't suggest posts with certain words",
                "id": "hide_all_specific_words",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              },
              {
                "text": "Manage content preferences",
                "id": "control_center",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              }
            ]
          },
          "user": {
            "pk": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=XbeNvhLXv28Q7kNvwFKx7FQ&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3SqAb7JvL9cxArgf2vmRlvgA9GWggJzlzboQvHgbqoIA&oe=69DC51E9&_nc_sid=c024bc",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "community_notes_info": {
            "has_viewer_submitted_note": false,
            "note_submission_disabled": false,
            "enable_submission_friction": false,
            "is_eligible_for_request_a_note": true
          },
          "has_high_risk_gen_ai_inform_treatment": false,
          "caption_is_edited": false,
          "code": "DWzNE9hkj_e",
          "device_timestamp": 1775502016,
          "enable_media_notes_production": true,
          "filter_type": 0,
          "has_views_fetching": true,
          "is_post_live_clips_media": false,
          "like_and_view_counts_disabled": false,
          "original_media_has_visual_reply_media": false,
          "report_info": {
            "has_viewer_submitted_report": false
          },
          "is_organic_product_tagging_eligible": true,
          "can_viewer_reshare": true,
          "has_shared_to_fb": 0,
          "media_reposter_bottomsheet_enabled": false,
          "has_liked": false,
          "can_viewer_save": true,
          "is_comments_gif_composer_enabled": false,
          "video_url": "https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m86/AQMh6i39sODeH8ExuZYvqhJFmZrP6yry-wVkt93t3dpe3sIHrOQF1kp5HdjLiYtlh1PmUOhY0D7UOvvFJzN7l7NdV0zBD3tM8ufCMX4.mp4?_nc_cat=103&_nc_sid=5e9851&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_ohc=Q4Pl4FTVJtUQ7kNvwGDWUBa&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU0NDQ3MjMxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjoxLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NTUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=3321bd2df3496fd7&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84MDQ4OEQ2RjIwRkI2OEY4NDQ4MEQ0N0I1N0YxMENCQ192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzMyNERBMkQ2NDgzODdGNzc2RUMzQ0JFNTc0QkVBQjhFX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWy4qIuJjlPxUCKAJDMywXQEu3Cj1wo9cYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af0xrQzCXuOmaF8iiCN8L4hVOkQLmB91iAWc3DQ6V1UQUA&oe=69D86DB8",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                13479,
                26958,
                40438
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwETTiLs&_nc_oc=AdrqQN5_AbV9IPYJWNvvUoBJ5Q2IhVY4KwFijAbkf7Vlc9g0bDaqFMo7LJ1FjSwZM4g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af3JP2noFoM_FX8W6vXVLFRV9fss2-KzLQ3sE4rtjAlkqg&oe=69DC6315",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/660863216_18647353954019133_4679945327511474927_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=Mzg2OTQ5NDAyMDM4NTQyMzMyNjE4NjQ3MzUzOTQ4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=zg_YhuIpl-YQ7kNvwETTiLs&_nc_oc=AdrqQN5_AbV9IPYJWNvvUoBJ5Q2IhVY4KwFijAbkf7Vlc9g0bDaqFMo7LJ1FjSwZM4g&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af3JP2noFoM_FX8W6vXVLFRV9fss2-KzLQ3sE4rtjAlkqg&oe=69DC6315",
          "location": null,
          "usertags": [],
          "taken_at_ts": 1775502016,
          "sponsor_tags": []
        }
      },
      {
        "media": {
          "strong_id__": "3868170261056492782_787132",
          "id": "3868170261056492782_787132",
          "disable_caption_and_comment": false,
          "fbid": 18083128910064008,
          "deleted_reason": 0,
          "client_cache_key": "Mzg2ODE3MDI2MTA1NjQ5Mjc4Mg==.3",
          "integrity_review_decision": "pending",
          "pk": "3868170261056492782",
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
                  4541,
                  9082,
                  13624
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/657963327_1140027124922753_6637085815743529745_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bkThNCUVUwUQ7kNvwFzDUB-&_nc_oc=AdqJcuNoZS-fsQeiM9DDYoP-623zG2ebE9CYz9i9o9LlNS16_3GScN5bZIp4BWNaLUk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af3qrSOwlh8hA_SKwsKGzbMhukEsmNdCITUyP1VstqH3AQ&oe=69DC345D",
                "width": 640,
                "is_spatial_image": false
              },
              "igtv_first_frame": {
                "estimated_scans_sizes": [
                  4541,
                  9082,
                  13624
                ],
                "height": 1136,
                "scans_profile": "e15",
                "url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.71878-15/657963327_1140027124922753_6637085815743529745_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=109&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bkThNCUVUwUQ7kNvwFzDUB-&_nc_oc=AdqJcuNoZS-fsQeiM9DDYoP-623zG2ebE9CYz9i9o9LlNS16_3GScN5bZIp4BWNaLUk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af3qrSOwlh8hA_SKwsKGzbMhukEsmNdCITUyP1VstqH3AQ&oe=69DC345D",
                "width": 640,
                "is_spatial_image": false
              },
              "smart_frame": null
            },
            "candidates": [
              {
                "estimated_scans_sizes": [
                  18831,
                  37662,
                  56494
                ],
                "height": 1333,
                "scans_profile": "e35",
                "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwGXIey1&_nc_oc=AdozNhlhgalBGZlzsyJ8qmBNXJXdb_8ILp-REdaBbjHEKEV32DSdS2pVtoW2YnhDeGU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af19wLLXNnwWGrwPUZkSx2LsY_GU6EMd2Y_12J7fCfLMTg&oe=69DC4951",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "scrubber_spritesheet_info_candidates": {
              "default": {
                "file_size_kb": 274,
                "max_thumbnails_per_sprite": 105,
                "rendered_width": 96,
                "sprite_height": 1232,
                "sprite_urls": [
                  "https://scontent-dfw6-1.cdninstagram.com/v/t51.71878-15/661407041_2382063302308753_1177647765954686603_n.jpg?_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=n5iQezOC2T8Q7kNvwF0Zd1p&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&oh=00_Af3-kS9rH3wpAEl61naT7J0gawrt8Y06f54rFbsSUh4Awg&oe=69DC5D1E&_nc_sid=c024bc"
                ],
                "sprite_width": 1500,
                "thumbnail_duration": 0.4560095238095238,
                "thumbnail_height": 176,
                "thumbnail_width": 100,
                "thumbnails_per_row": 15,
                "total_thumbnail_num_per_sprite": 105,
                "video_length": 47.881
              }
            }
          },
          "media_type": 2,
          "original_width": 1080,
          "original_height": 1920,
          "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMDMxMGExNWM3N2JjNDc0ZDgzYWVjMzcwMTkzZjI3MzAzODY4MTcwMjYxMDU2NDkyNzgyIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwOTI1NHwzODY4MTcwMjYxMDU2NDkyNzgyfDM1MTQ1NDQxMDI1fGM3MWMzMTY0ZmI5OTdhYTEzYzIxOWI5MjYwYzM3MDU2NGE3NTBiNDU0MGNiODhjYzU0Y2RkMWQzY2IzZGJiNzAifSwic2lnbmF0dXJlIjoiIn0=",
          "music_metadata": null,
          "has_tagged_users": true,
          "clips_tab_pinned_user_ids": [],
          "original_lang_for_translations": "en",
          "is_open_to_public_submission": false,
          "is_social_ufi_disabled": false,
          "timeline_pinned_user_ids": [],
          "taken_at": 1775404810,
          "photo_of_you": false,
          "can_see_insights_as_brand": false,
          "fundraiser_tag": {
            "has_standalone_fundraiser": false
          },
          "fb_user_tags": {
            "in": []
          },
          "media_overlay_info": null,
          "is_in_profile_grid": false,
          "profile_grid_control_enabled": false,
          "is_artist_pick": false,
          "media_notes": {
            "items": []
          },
          "product_type": "clips",
          "social_context": [],
          "subscribe_cta_visible": false,
          "creative_config": null,
          "is_cutout_sticker_allowed": false,
          "cutout_sticker_info": [],
          "is_tagged_media_shared_to_viewer_profile_grid": false,
          "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
          "meta_ai_suggested_prompts": [],
          "gen_ai_chat_with_ai_cta_info": null,
          "can_reply": false,
          "floating_context_items": [],
          "is_eligible_content_for_post_roll_ad": false,
          "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
          "eligible_insights_entrypoints": "NONE",
          "media_attributions_data": [],
          "media_ui_attributions_data": [],
          "media_ui_attributions_data_v2": [],
          "creator_product_link_infos": [],
          "is_eligible_for_poe": true,
          "is_eligible_for_organic_eager_refresh": false,
          "commerce_integrity_review_decision": "",
          "is_reuse_allowed": false,
          "logging_info_token": "GCBkZTFlNTIyYTIxYTE0NTRkOGNhZGU2MDA2MDU5Y2Q2MngDbmhhAA==",
          "boost_unavailable_identifier": null,
          "boost_unavailable_reason": null,
          "boost_unavailable_reason_v2": null,
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
              "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/404288054_706561544741164_8609495828476348252_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44ODguYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=9NDLLLLwDV8Q7kNvwFBO3q8&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GDbyGBgs4eItnYICAFxHikfXEnt3bkULAAAB1501500j-ccb7-5&oh=00_Af3tH1CsEVaWTIUVCxcBmpPwTncZiVTdtdpfGlgj6p6CWw&oe=69DC57AB&_nc_sid=c024bc",
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
          "coauthor_producer_can_see_organic_insights": false,
          "invited_coauthor_producers": [],
          "collab_follow_button_info": {
            "show_follow_button": true,
            "is_owner_in_author_exp": true
          },
          "igbio_product": null,
          "is_paid_partnership": false,
          "reshare_count": 154,
          "ig_media_sharing_disabled": false,
          "media_repost_count": 91,
          "view_state_item_type": 128,
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
              "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBManifestTimestamp=\"1775663909\" FBManifestIdentifier=\"Fsrss50NKRa4sr3lnNynAyIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"931771249568924a\" bandwidth=\"66894\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66894\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m78/AQObEBSySE0AGNBbG4lxf162Q155i5gTcG0OizHqB4rRxcGyySZDjummT0z9r1wsiCbVlaRrtWqIqFWzQVPE7UxmQ1lTMC4PQzMnv0M.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=8_2Uu26HoJkQ7kNvwF6ZqCL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo2NzA4NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af08vXt8RDkWBF4l2_KjsUKNJiaPLI2-6NIo0Q_o7-rZwQ&amp;oe=69D86E19</BaseURL><SegmentBase indexRange=\"824-1143\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
              "progressive_download_url": "https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m69/AQNsTvlWrX5b5jAnAagr-VEkXvHgjuh1R7UtSI3qunavCZFTpObST3AI8L-cDc_wZTw8bAKRL2XuixVvoM6ISAHt.mp4?strext=1&_nc_cat=100&_nc_sid=8bf8fe&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_ohc=TbFtdnyPN3QQ7kNvwHZZfZ7&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&_nc_zt=28&oh=00_Af3XLYYB2hyrM88d6x0Cl5wscMkPbNf7H9h2Ooa8SuyVdQ&oe=69DC4132",
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
                "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=XbeNvhLXv28Q7kNvwFKx7FQ&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3SqAb7JvL9cxArgf2vmRlvgA9GWggJzlzboQvHgbqoIA&oe=69DC51E9&_nc_sid=c024bc"
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
          "like_count": 7479,
          "top_likers": [],
          "hidden_likes_string_variant": -1,
          "caption": {
            "strong_id__": "18083194658064008",
            "bit_flags": 0,
            "created_at": 1775404813,
            "created_at_utc": 1775404813,
            "did_report_as_spam": false,
            "is_ranked_comment": false,
            "pk": "18083194658064008",
            "share_enabled": false,
            "content_type": "comment",
            "media_id": 3868170261056492782,
            "status": "Active",
            "type": 1,
            "user_id": 787132,
            "text": "Spotted hyenas are a powerful example of the resilience and strength found in nature. For wildlife ecologist, conservation scientist, and National Geographic Explorer Dr. Christine Wilkinson (@christine_eleanor), these reminders are what wonder is all about. \n\n#StepIntoWonder with National Geographic’s #EarthMonth collection on @DisneyPlus.",
            "user": {
              "strong_id__": "787132",
              "pk": 787132,
              "pk_id": "787132",
              "id": "787132",
              "is_unpublished": false,
              "fbid_v2": 17841400573960012,
              "username": "natgeo",
              "full_name": "National Geographic",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3865702555259028436_787132",
              "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=XbeNvhLXv28Q7kNvwFKx7FQ&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3SqAb7JvL9cxArgf2vmRlvgA9GWggJzlzboQvHgbqoIA&oe=69DC51E9&_nc_sid=c024bc"
            },
            "is_covered": false,
            "private_reply_status": 0
          },
          "comment_count": 78,
          "comment_inform_treatment": {
            "action_type": null,
            "should_have_inform_treatment": false,
            "text": "",
            "url": null
          },
          "is_photo_comments_composer_enabled_for_author": false,
          "hide_view_all_comment_entrypoint": true,
          "locations": [],
          "play_count": 1304824,
          "ig_play_count": 1304824,
          "shop_routing_user_id": null,
          "featured_products": [],
          "are_remixes_crosspostable": true,
          "crosspost_metadata": {
            "fb_downstream_use_xpost_metadata": {
              "downstream_use_xpost_deny_reason": "NONE"
            }
          },
          "is_eligible_for_autodub": false,
          "is_eligible_for_autodub_upsell": false,
          "video_sticker_locales": [],
          "has_audio": true,
          "video_duration": 47.893001556396484,
          "is_dash_eligible": 1,
          "video_versions": [
            {
              "bandwidth": 1064730,
              "height": 1280,
              "id": "799234956583164v",
              "type": 101,
              "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwFsnMia&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3hwxFeLkPwIonNeThrcS3yosMC-IBTHPxWwsgrIKlOSg&oe=69D87233",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            },
            {
              "bandwidth": 1064730,
              "height": 1280,
              "id": "799234956583164v",
              "type": 102,
              "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwFsnMia&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3hwxFeLkPwIonNeThrcS3yosMC-IBTHPxWwsgrIKlOSg&oe=69D87233",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            },
            {
              "bandwidth": 1064730,
              "height": 1280,
              "id": "799234956583164v",
              "type": 103,
              "url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwFsnMia&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3hwxFeLkPwIonNeThrcS3yosMC-IBTHPxWwsgrIKlOSg&oe=69D87233",
              "url_expiration_timestamp_us": null,
              "width": 720,
              "fallback": null
            }
          ],
          "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT47.893333S\" FBManifestTimestamp=\"1775663909\" FBManifestIdentifier=\"Fsrss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxqbV6aDR+bYDqvaKk6SpqgT+7OaL4NTBBNj9mrKQtbMFjO6L353LugW8goKl5dy6BYLQssb/qogGmPbggPvSlAbwr/bX4oT0BoSVlbCehoIHqrXuq+uJnQfYts6QtoSsWyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWBhQAEhQCAA==\"><Period id=\"0\" duration=\"PT47.893333S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:82.7\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1536512375144606v\" bandwidth=\"125041\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"748393\" FBPlaybackResolutionMos=\"0:100,360:68.6,480:63.5,720:57.2,1080:52.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.7,480:90.2,720:86.7,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOC-37dngJq90Dyy1_JazUnnPGdWCHskETHnxkRIIJCSOlZF1fVQ-6mAFGNhj2z93WeeIs714OUklQmfut9nIzTnVBICEHS1YfCoAw.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=e25xSTehHgsQ7kNvwHXbVjQ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTI1MDQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0bzh7lnh9vActoLyfdN4AHOlSFvVlpnjsNkZa4K0CJIA&amp;oe=69DC5053</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-11379\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-53195\" FBFirstSegmentRange=\"978-73681\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"73682-177801\" FBPrefetchSegmentRange=\"978-73681\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1707180720280577v\" bandwidth=\"268984\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"1609913\" FBPlaybackResolutionMos=\"0:100,360:82.1,480:77.4,720:72,1080:65\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97,480:96,720:94.9,1080:90.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQOoI_Qc5Hb567q3s03DZ7hurU3EPc934bMb3FmMMVaHXDUYxsb4QiUQt8F8TcKitfPDLHzHey1wENKGp-vSnIF1hHoyzJ4LrrK2kjM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=ajpqDB5imFoQ7kNvwGleJCb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MjY4OTg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3PPCyV7XYD-BAqaD_VAOOP5n9IlzrVfu8xAtjX9MOSRg&amp;oe=69DC64EB</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-19527\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-105884\" FBFirstSegmentRange=\"978-157985\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"157986-375189\" FBPrefetchSegmentRange=\"978-157985\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1944018522917880v\" bandwidth=\"368764\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"2207110\" FBPlaybackResolutionMos=\"0:100,360:85.9,480:81.7,720:75.8,1080:68.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.04,480:97.6,720:97.2,1080:93.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQM3ITI-kIVflLXqBQCMcqSKriqhB8j74oqGUj6f3pYWDnqOC18MUJJNe0oZbKf0kPXddx31PP3oAzTIyNssN5V0g7YFH89E5A-Ij6s.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=Mwx1ng6pC6sQ7kNvwG4w0kV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MzY4NzY0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0-anWLv9J_1lffErb4PZ3d-xqZ0KHT-tkz3gpmLzatfg&amp;oe=69DC662F</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-24075\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-141715\" FBFirstSegmentRange=\"978-216596\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"216597-512096\" FBPrefetchSegmentRange=\"978-216596\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1218968110062997v\" bandwidth=\"442503\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"2648452\" FBPlaybackResolutionMos=\"0:100,360:87.7,480:83.8,720:77.5,1080:70.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.61,480:98.35,720:98.31,1080:95.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQOYTMwguxNmYzts7ztqP3uq8QYqnySSAGvKGU84jFkz30lRwgwLYRu68NUaE4CuVcCCkccg0gJEpbQIdwnc6OfTFFkYbjN5LqbfVG4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=KFTAZdhAk40Q7kNvwHJ1lGG&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NDQyNTAzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2hqxjdP1KmJK9iV4a5tHFD2OBrB-Xbgp3EnpCqlrs7hA&amp;oe=69DC56A1</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-27189\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-169993\" FBFirstSegmentRange=\"978-261689\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"261690-617097\" FBPrefetchSegmentRange=\"978-261689\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1734255584222604v\" bandwidth=\"593051\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"3549501\" FBPlaybackResolutionMos=\"0:100,360:89.9,480:86.3,720:80.5,1080:72.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99,480:98.97,720:99.193,1080:97.4\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9lx9WGs0aObQ1f5j5Tn6y1xVQXR-Dwub7W_SxmroZb4LDoDVxPW13tmY1vHIkgBkSqIxvS44m4qTOlQHuogzz-fjvXsOFNStGw5o.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=IG_0Np9TPzEQ7kNvwEdlAqn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6NTkzMDUxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af37J6c8XM0ACacRk5zq0c8ETel4HTYKqa7596fCVlWxuw&amp;oe=69DC5BBE</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-32309\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-227501\" FBFirstSegmentRange=\"978-353323\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"353324-811886\" FBPrefetchSegmentRange=\"978-353323\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1974830039737666v\" bandwidth=\"808049\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"4836297\" FBPlaybackResolutionMos=\"0:100,360:91.5,480:88.1,720:82.7,1080:73.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.177,480:99.289,720:99.419,1080:98.77\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNxzz3B_d6VnnNmwILSsdhY1b8WYAyEq1nGyoBddc0-zErqxX-3eoxHWRJoRjzW8rt7CPCOSi7aXg9mJJvD7MDk23Y4mXgSrDlMMp0.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=1oWA7fT-WaIQ7kNvwFLiXns&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6ODA4MDQ5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2hEnRMJKKMoYrh9MnUa3wcn4GPJKjL4nP4H8V8sUv7XQ&amp;oe=69DC3E3B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-37690\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-306742\" FBFirstSegmentRange=\"978-478293\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"478294-1073273\" FBPrefetchSegmentRange=\"978-478293\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2034265537498453v\" bandwidth=\"1150676\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"6886972\" FBPlaybackResolutionMos=\"0:100,360:92.5,480:89.4,720:84.3,1080:75.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.316,480:99.475,720:99.604,1080:99.184\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO8nzMmBULFzOq0Uc221nMlzpRXdUpXzRan5dqj-VDzxkIrtzc1nz0dI1BX50zPIMwgzzgD9a0zuNNVJoHjAR_qboR3srHbCUwAf98.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=AJfwxCErVuwQ7kNvwGBPFhN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTE1MDY3NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0l9cud8zCmYm9H8_1XpbwHfuHl0k--yJVMf_VyTWjIZA&amp;oe=69DC467B</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-42521\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-414721\" FBFirstSegmentRange=\"978-651076\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"651077-1467135\" FBPrefetchSegmentRange=\"978-651076\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"965261856159059v\" bandwidth=\"1802418\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"10787749\" FBPlaybackResolutionMos=\"0:100,360:93.6,480:91,720:86.4,1080:81.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.439,480:99.57,720:99.699,1080:99.627\" FBAbrPolicyTags=\"avoid_on_cellular,avoid_on_cellular_intentional\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQNl6wEb07Ks3JIhuPO2wCPZMvypoiru-vDavX2ZbnVx8EmjXzlq5vNBYsVwM0MoQtRL7pguuPZmXv_tnRPUIgRfIL00yZnEyV3zjZQ.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=WeUmuiwzlkoQ7kNvwGKe-wJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDk5ODU2NjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjMsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo0NywiYml0cmF0ZSI6MTgwMjQxOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af09QZ82EuPvaAYZtyOt8rZjWHp8i3GD1HDQynk-LZ4ntA&amp;oe=69DC591C</BaseURL><SegmentBase indexRange=\"826-977\" timescale=\"11988\" FBMinimumPrefetchRange=\"978-62167\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"978-590586\" FBFirstSegmentRange=\"978-956290\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"956291-2465586\" FBPrefetchSegmentRange=\"978-956290\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"25711055888567724a\" bandwidth=\"43137\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"43137\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"259233\" FBPaqMos=\"86.23\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-2.cdninstagram.com/o1/v/t2/f2/m367/AQPwGwzN_jZWTG5g53W6HPaq6prVW3aFxZFUMoApdF5Bb07alTzINwfJIHhTt2__EB0B73uktjzHCPmfysFRIfXNu5jyUMQk7HQ2MAA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-2.cdninstagram.com&amp;_nc_ohc=D8aq4uZD0HoQ7kNvwFQ2Ysk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo0MzMwMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3xBGWB3_YyAygfP1JjcXQ3pMe8OBRXRqogQu-h0APYDg&amp;oe=69DC3521</BaseURL><SegmentBase indexRange=\"837-988\" timescale=\"48000\" FBMinimumPrefetchRange=\"989-2211\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"989-15011\" FBFirstSegmentRange=\"989-27427\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"27428-53863\" FBPrefetchSegmentRange=\"989-27427\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1520437802786668a\" bandwidth=\"71500\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71500\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"429033\" FBPaqMos=\"87.36\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m367/AQM1qgyiYipO3nTb3Q4w_ENJZ3IxJuj0VPo2tuNaBczlM_oHVqwMkDYBW3T0y1773ATnvblNT7r_xf3TsujSnPIypzOSKbCvToAOuws.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw5-1.cdninstagram.com&amp;_nc_ohc=hwhUj3NemRQQ7kNvwHGbb3a&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjo3MTY2NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0Iwbf0UXOF7_Crqrtszrd8V679VCgF2EU3n2Zsp65rpA&amp;oe=69DC4C06</BaseURL><SegmentBase indexRange=\"838-989\" timescale=\"48000\" FBMinimumPrefetchRange=\"990-2669\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"990-24617\" FBFirstSegmentRange=\"990-45672\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"45673-89246\" FBPrefetchSegmentRange=\"990-45672\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1270292424743743a\" bandwidth=\"104937\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"104937\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"629205\" FBPaqMos=\"81.20\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOSZPTrQoZvEzpNyz3hhbxCnafm4XAlkTPd_h7zn5N1n6R0Ga6E8UgDUI08GX-XKGcGJAxmhV-HhXGeeaJ0XyTdLAqhdbtcuwmB8ms.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=L_y6Qh90gVgQ7kNvwED03Zv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMDUxMDEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3NmgbsGDFys0o58BG0gRUGqI6EuBI9Dpqq4VcZwo0QFw&amp;oe=69DC5BBA</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2362\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-35155\" FBFirstSegmentRange=\"985-65716\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"65717-128980\" FBPrefetchSegmentRange=\"985-65716\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1536210714590086a\" bandwidth=\"136838\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"136838\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"820186\" FBPaqMos=\"83.96\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-dfw6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO7KXm8TEDvhztA9v_PIl-O0CaShP5_2iBO4ggZMBeDRGTOTXVI3umPjYEK9ju_ZrOe1b_AWcnu75HARzg6Y6KbrJQ7pMmp_w0mKfU.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-dfw6-1.cdninstagram.com&amp;_nc_ohc=itqu0TbKGQYQ7kNvwGRp8d8&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0OTk4NTY2MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjQ3LCJiaXRyYXRlIjoxMzcwMDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=bsyPveyDgwQjdZA5fpcTCw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2PSeoXIg0a24STeKkkP5QBiwRLrW4nG33dwailD7hNrQ&amp;oe=69DC4117</BaseURL><SegmentBase indexRange=\"833-984\" timescale=\"48000\" FBMinimumPrefetchRange=\"985-2442\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"985-44989\" FBFirstSegmentRange=\"985-85365\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"85366-166815\" FBPrefetchSegmentRange=\"985-85365\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
          "number_of_qualities": 8,
          "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
          "sharing_friction_info": {
            "should_have_sharing_friction": false,
            "bloks_app_url": null,
            "sharing_friction_payload": null
          },
          "gen_ai_detection_method": {
            "detection_method": "NONE"
          },
          "clips_demotion_control": {
            "title": "Not interested",
            "enable_word_wrapping": true,
            "confirmation_icon": "none",
            "title_style": "normal",
            "confirmation_title": "Post hidden",
            "confirmation_body": "We'll suggest fewer posts like this.",
            "confirmation_title_style": "large_left",
            "undo_style": "top_right",
            "confirmation_style": "bottomsheet",
            "followup_options": [
              {
                "text": "Don't suggest posts from natgeo",
                "style": null,
                "id": "dislike_author",
                "data": "author_id:787132",
                "show_icon": true,
                "demotion_control": {
                  "confirmation_style": "bottomsheet",
                  "confirmation_icon": "eye-off-pano",
                  "confirmation_body": "We won't suggest posts from natgeo.",
                  "undo_style": "inline"
                },
                "subtitle": null
              },
              {
                "text": "Don't suggest posts with certain words",
                "id": "hide_all_specific_words",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              },
              {
                "text": "Manage content preferences",
                "id": "control_center",
                "show_icon": true,
                "data": null,
                "style": null,
                "demotion_control": null,
                "subtitle": null
              }
            ]
          },
          "user": {
            "pk": "787132",
            "id": "787132",
            "username": "natgeo",
            "full_name": "National Geographic",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFi9SqS7RQ43ukRfet6UYFykOgbgAu8fVVpYoOtn2k7xTfw4TVnToA9NqxJ0PLtBDY&_nc_ohc=XbeNvhLXv28Q7kNvwFKx7FQ&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&edm=ACHbZRIBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3SqAb7JvL9cxArgf2vmRlvgA9GWggJzlzboQvHgbqoIA&oe=69DC51E9&_nc_sid=c024bc",
            "profile_pic_url_hd": null,
            "is_private": false,
            "is_verified": true
          },
          "community_notes_info": {
            "has_viewer_submitted_note": false,
            "note_submission_disabled": false,
            "enable_submission_friction": false,
            "is_eligible_for_request_a_note": true
          },
          "has_high_risk_gen_ai_inform_treatment": false,
          "caption_is_edited": false,
          "code": "DWugFulAJTu",
          "device_timestamp": 1775404810,
          "enable_media_notes_production": true,
          "filter_type": 0,
          "has_views_fetching": true,
          "is_post_live_clips_media": false,
          "like_and_view_counts_disabled": false,
          "original_media_has_visual_reply_media": false,
          "report_info": {
            "has_viewer_submitted_report": false
          },
          "is_organic_product_tagging_eligible": true,
          "can_viewer_reshare": true,
          "has_shared_to_fb": 0,
          "media_reposter_bottomsheet_enabled": false,
          "has_liked": false,
          "can_viewer_save": true,
          "is_comments_gif_composer_enabled": false,
          "video_url": "https://scontent-dfw5-1.cdninstagram.com/o1/v/t2/f2/m86/AQNoP85b9Y7Qc6c-b63EZwTpnP1uf8ccl0FaBOt1H3Fs0E-jbonRo3rUn50qjheMxdd4yR84T985FnZfGlB7PL4CxHkVIfzQrRJ0VW8.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_ohc=ct5wWDuH0u8Q7kNvwFsnMia&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQ5OTg1NjYxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozLCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NDcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5e3b98a1a17d821e&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC84ODRFNUMxRjNFOEJEQjM2RjFGNzcxQkVGODcxRTRBN192aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0I1NDcyODRDMjJFNjkwRDQ4QUQ2MDY1NDdGQThDMUIyX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWls73u_7kPxUCKAJDMywXQEfwxJul41QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3hwxFeLkPwIonNeThrcS3yosMC-IBTHPxWwsgrIKlOSg&oe=69D87233",
          "image_versions": [
            {
              "estimated_scans_sizes": [
                18831,
                37662,
                56494
              ],
              "height": 1333,
              "scans_profile": "e35",
              "url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwGXIey1&_nc_oc=AdozNhlhgalBGZlzsyJ8qmBNXJXdb_8ILp-REdaBbjHEKEV32DSdS2pVtoW2YnhDeGU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af19wLLXNnwWGrwPUZkSx2LsY_GU6EMd2Y_12J7fCfLMTg&oe=69DC4951",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "thumbnail_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.82787-15/658883423_18647058271019133_400055138522681800_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=107&ig_cache_key=Mzg2ODE3MDI2MTA1NjQ5Mjc4MjE4NjQ3MDU4MjY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=krbrEZ7xzDYQ7kNvwGXIey1&_nc_oc=AdozNhlhgalBGZlzsyJ8qmBNXJXdb_8ILp-REdaBbjHEKEV32DSdS2pVtoW2YnhDeGU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_gid=bsyPveyDgwQjdZA5fpcTCw&_nc_ss=7a3ba&oh=00_Af19wLLXNnwWGrwPUZkSx2LsY_GU6EMd2Y_12J7fCfLMTg&oe=69DC4951",
          "location": null,
          "usertags": [],
          "taken_at_ts": 1775404810,
          "sponsor_tags": []
        }
      }
    ],
    "paging_info": {
      "max_id": "QVFCMjU3WDJHZTJMWnBrZVg1Y01tdTRjT1lITnJPS2pzSVpENjNPaHdlVFFDcGt2LTJmWmFWNE1xY0xqcDl3cVl6eDQxQm5TcVNnUUM5b2lQMHY0YzdmTw==",
      "more_available": true
    },
    "status": "ok"
  },
  "next_page_id": "QVFCMjU3WDJHZTJMWnBrZVg1Y01tdTRjT1lITnJPS2pzSVpENjNPaHdlVFFDcGt2LTJmWmFWNE1xY0xqcDl3cVl6eDQxQm5TcVNnUUM5b2lQMHY0YzdmTw=="
}
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
        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.2885-19/36979478_1108966052592442_2446283676674162688_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xODEuYzEifQ&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=6FpOoF1f938Q7kNvwHXtbYt&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=GBZDNAI6_6FHmfADAAAAAAAL8vIhbkULAAAB1501500j-ccb7-5&oh=00_Af1Yragqmc6-wIrn4Vt7iGrfMTOYj6nbQIbIszqdCgoQSg&oe=69DC6397&_nc_sid=3e1f4f",
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
          "thumbnail_url": "https://scontent-iad6-1.cdninstagram.com/v/t39.30808-6/658827819_1372199101613834_6861606413018434238_n.jpg?stp=c0.205.1638.1638a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=DUn9KPp4r1QQ7kNvwHnpFB2&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYAAAAA&ccb=7-5&ig_cache_key=Mzg2NTc0MTM4MzA3Mjc5MjY5Ng%3D%3D.3.c-ccb7-5&oh=00_Af3S3BiD-dgum69-w8zQOxI1oaVIZkb5M2vPEZZSlQ1ddw&oe=69DC3607&_nc_sid=3e1f4f"
        },
        {
          "media_id": 3844028826083372791,
          "media_fbid": 17955279509935029,
          "thumbnail_url": "https://scontent-iad3-1.cdninstagram.com/v/t39.30808-6/645739337_1347153844118360_5210304906653608462_n.jpg?stp=c0.205.1638.1638a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=fg5hVq6PNTQQ7kNvwFFkSjy&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYAAAAA&ccb=7-5&ig_cache_key=Mzg0NDAyODgyNjA4MzM3Mjc5MQ%3D%3D.3.c-ccb7-5&oh=00_Af1xoHR4DQyVxauodUrNVhFV7rIusf_aEtzWhv5I6_g4lg&oe=69DC3ED3&_nc_sid=3e1f4f"
        },
        {
          "media_id": 3823762571422659053,
          "media_fbid": 18164166292407419,
          "thumbnail_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/624072385_18394544134178107_6840591593478423165_n.jpg?stp=c0.135.1080.1080a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=MahlqLr2UVwQ7kNvwHTLU_O&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=MzgyMzc2MjU3MTQyMjY1OTA1Mw%3D%3D.3.c-ccb7-5&oh=00_Af3JdGPHL8cvQvSgRdvMA-VaNE_OTFWjuOu_GQOe6RYqYA&oe=69DC6412&_nc_sid=3e1f4f"
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
        "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/469203603_607657381816727_6317965279284024222_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MTIuYzEifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=gMsqSllxmw4Q7kNvwFoUMc9&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=GJN69xuXaWNCqSgCAJ7T_Y7y661XbkULAAAB1501500j-ccb7-5&oh=00_Af1jONLfmNOcjdUYrOWdwlIsR3bJvys8KU4kcYpSEweo3A&oe=69DC34CC&_nc_sid=3e1f4f",
        "is_verified": false,
        "username": "sciencex.physorg",
        "full_name": "Science X / Phys.org",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "latest_reel_media": 1775660829,
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
        "should_show_public_contacts": false,
        "category": "Media/news company"
      },
      "media_previews": [
        {
          "media_id": 3870815828120322159,
          "media_fbid": 18195445549358591,
          "thumbnail_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/662195230_18080535455384436_8425157386843864810_n.jpg?stp=c0.135.1080.1080a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=363bTgy5hpMQ7kNvwFrbOyR&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=Mzg3MDgxNTgyODEyMDMyMjE1OQ%3D%3D.3.c-ccb7-5&oh=00_Af1sBFKl5E4xWVK_2nia78euZfJKR5Erk5rB5_tXUC-uDA&oe=69DC3C0F&_nc_sid=3e1f4f"
        },
        {
          "media_id": 3870725212590124942,
          "media_fbid": 18078129377179314,
          "thumbnail_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/657248076_18080521988384436_2607751270461745902_n.jpg?stp=c0.135.1080.1080a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=IDFTfas6HlcQ7kNvwFD66XS&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=Mzg3MDcyNTIxMjU5MDEyNDk0Mg%3D%3D.3.c-ccb7-5&oh=00_Af0YFW3YWZC4uKTMZI3QaWSOvQomj7l_N1c7BANl9maJcw&oe=69DC675C&_nc_sid=3e1f4f"
        },
        {
          "media_id": 3870272248125504675,
          "media_fbid": 18006882866891261,
          "thumbnail_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-15/661022992_18080467856384436_2526274961574655859_n.jpg?stp=c0.135.1080.1080a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=M9FJUWaQjEsQ7kNvwFPyowu&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=Mzg3MDI3MjI0ODEyNTUwNDY3NQ%3D%3D.3.c-ccb7-5&oh=00_Af3KKmyBRPg1ufFr9sObLS1obmMvbP4QdPp6ftfZa7PItA&oe=69DC622F&_nc_sid=3e1f4f"
        }
      ]
    },
    {
      "user": {
        "strong_id__": "68012770661",
        "pk": 68012770661,
        "pk_id": "68012770661",
        "fbid_v2": 17841467999841596,
        "third_party_downloads_enabled": 1,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "id": "68012770661",
        "profile_pic_id": "3865708778020840707_68012770661",
        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-19/659123606_17925610677266662_299620373829898330_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=1GP4i4FmPtQQ7kNvwEuZUIz&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=GJZtSSfm6Mx4P68-AFrQmX0kdygEbmNDAQAB1501500j-ccb7-5&oh=00_Af0RC_Ws0jZ-5XBRkMmX4nkwKWxyXcadr3xscGq1-bgtdg&oe=69DC5134&_nc_sid=3e1f4f",
        "is_verified": false,
        "username": "natgeofamily",
        "full_name": "National Geographic Family",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "latest_reel_media": 1775653578,
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
        "category_id": "191684877517919",
        "is_category_tappable": true,
        "should_show_public_contacts": false,
        "category": "Publisher"
      },
      "media_previews": [
        {
          "media_id": 3859246065955483507,
          "media_fbid": 18089268776270434,
          "thumbnail_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/654856323_17924227863266662_3417339785106286434_n.jpg?stp=c0.85.719.719a_dst-jpg_e15_tt6&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=DLhhDXdQeTQQ7kNvwG74dN1&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=Mzg1OTI0NjA2NTk1NTQ4MzUwNw%3D%3D.3.c-ccb7-5&oh=00_Af2KDce6NjtcjUhJcvR8jOAqc5hqtrv-ZHBPMi0vdKd7-A&oe=69DC3BB6&_nc_sid=3e1f4f"
        },
        {
          "media_id": 3870269251261738850,
          "media_fbid": 18091692406918779,
          "thumbnail_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/660615300_17926503360266662_7749496503318016707_n.jpg?stp=c0.420.1080.1080a_dst-jpg_e35_s750x750_sh0.08_tt6&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=zBrXi9H5FngQ7kNvwFaK-sL&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&oh=00_Af1sdbmZe1CGzR07nDsKZJDEee_wTJag6mq5tjGJaRSRbQ&oe=69DC63B3&_nc_sid=3e1f4f"
        },
        {
          "media_id": 3869291641157022329,
          "media_fbid": 17993445389947253,
          "thumbnail_url": "https://scontent-iad3-1.cdninstagram.com/v/t51.82787-15/659425571_17926306896266662_9104587386661003772_n.jpg?stp=c241.0.957.957a_dst-jpg_e15_s750x750_tt6&_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFfMPNNzVtoBTaDQyo7fZHuf3Dvj1dFKhayVN71u-ViZwsNCKKibyl3vcbN_16HEmw&_nc_ohc=AU9A1atADLoQ7kNvwF9zUHG&_nc_gid=W19aVnuubdv1JRXYY_9ZGg&edm=ALPbrGYBAAAA&ccb=7-5&ig_cache_key=Mzg2OTI5MTU5NTcyNDMxNDI3OQ%3D%3D.3.c-ccb7-5&oh=00_Af3ZyuxVLVvmh9Cp4q-Z1N2W-jUFMBaDucuvxeGLRXV10g&oe=69DC6859&_nc_sid=3e1f4f"
        }
      ]
    }
  ],
  "status": "ok"
}
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
        "pk": "41668656782",
        "id": "41668656782",
        "username": "emiliareview",
        "full_name": "emiliana ᡣ𐭩",
        "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/660830868_18068601482384783_221122897203355395_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHWOPOoP2TiruIQ522ZeZ3TFnOSbWkdUC770CinV8vWHxV1sHuD8HaBKmSZkUR9JMI&_nc_ohc=d_02GQQswNAQ7kNvwFPrPxX&_nc_gid=MwvSvojl4Tx6NjsYdU5zSQ&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af3yNFmnn68JcFUuv7Qdv679yYz9prWJku2pOkEU-ZKbvg&oe=69DC4D93&_nc_sid=17ea04",
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
          "id": "41668656782",
          "expiring_at": 1775750312,
          "has_pride_media": false,
          "latest_reel_media": 0,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "41668656782",
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/660830868_18068601482384783_221122897203355395_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHWOPOoP2TiruIQ522ZeZ3TFnOSbWkdUC770CinV8vWHxV1sHuD8HaBKmSZkUR9JMI&_nc_ohc=d_02GQQswNAQ7kNvwFPrPxX&_nc_gid=MwvSvojl4Tx6NjsYdU5zSQ&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af3yNFmnn68JcFUuv7Qdv679yYz9prWJku2pOkEU-ZKbvg&oe=69DC4D93&_nc_sid=17ea04",
            "username": "emiliareview"
          }
        },
        "followed_by_viewer": false,
        "follows_viewer": false,
        "requested_by_viewer": false
      },
      {
        "pk": "38676330571",
        "id": "38676330571",
        "username": "ween_00",
        "full_name": "𝑾𝒆𝒏𝒅𝒚 𝑻𝒂𝒕𝒊𝒂𝒏𝒂.🌹",
        "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/660295830_18098543765290572_2123613911035652493_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gHWOPOoP2TiruIQ522ZeZ3TFnOSbWkdUC770CinV8vWHxV1sHuD8HaBKmSZkUR9JMI&_nc_ohc=zTKlwm_6SGwQ7kNvwHqXKAR&_nc_gid=MwvSvojl4Tx6NjsYdU5zSQ&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af3gpYfCkaRZYkN8CaewmuKbUAe5Ksg07cPeB1vIa6NP6Q&oe=69DC3911&_nc_sid=17ea04",
        "profile_pic_url_hd": null,
        "is_private": true,
        "is_verified": false,
        "account_badges": null,
        "fbid_v2": null,
        "has_anonymous_profile_picture": null,
        "latest_reel_media": null,
        "pk_id": null,
        "profile_pic_id": null,
        "strong_id__": null,
        "third_party_downloads_enabled": null,
        "reel": {
          "id": "38676330571",
          "expiring_at": 1775750312,
          "has_pride_media": false,
          "latest_reel_media": null,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "38676330571",
            "profile_pic_url": "https://scontent-iad6-1.cdninstagram.com/v/t51.82787-19/660295830_18098543765290572_2123613911035652493_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gHWOPOoP2TiruIQ522ZeZ3TFnOSbWkdUC770CinV8vWHxV1sHuD8HaBKmSZkUR9JMI&_nc_ohc=zTKlwm_6SGwQ7kNvwHqXKAR&_nc_gid=MwvSvojl4Tx6NjsYdU5zSQ&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af3gpYfCkaRZYkN8CaewmuKbUAe5Ksg07cPeB1vIa6NP6Q&oe=69DC3911&_nc_sid=17ea04",
            "username": "ween_00"
          }
        },
        "followed_by_viewer": false,
        "follows_viewer": false,
        "requested_by_viewer": false
      },
      {
        "pk": "59169670270",
        "id": "59169670270",
        "username": "chayan__artist",
        "full_name": "chayan",
        "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/660227552_17988001784974271_2182242503266021593_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHWOPOoP2TiruIQ522ZeZ3TFnOSbWkdUC770CinV8vWHxV1sHuD8HaBKmSZkUR9JMI&_nc_ohc=NeXYqjXVmE4Q7kNvwG5iRD6&_nc_gid=MwvSvojl4Tx6NjsYdU5zSQ&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af0lE9Rn73q-k9Dv8es_JJ_XeT3KiO7jwNn-1dEGovNS2A&oe=69DC4B28&_nc_sid=17ea04",
        "profile_pic_url_hd": null,
        "is_private": false,
        "is_verified": false,
        "account_badges": null,
        "fbid_v2": null,
        "has_anonymous_profile_picture": null,
        "latest_reel_media": 1775663779,
        "pk_id": null,
        "profile_pic_id": null,
        "strong_id__": null,
        "third_party_downloads_enabled": null,
        "reel": {
          "id": "59169670270",
          "expiring_at": 1775750312,
          "has_pride_media": false,
          "latest_reel_media": 1775663779,
          "seen": null,
          "owner": {
            "__typename": "GraphUser",
            "id": "59169670270",
            "profile_pic_url": "https://scontent-iad3-2.cdninstagram.com/v/t51.82787-19/660227552_17988001784974271_2182242503266021593_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gHWOPOoP2TiruIQ522ZeZ3TFnOSbWkdUC770CinV8vWHxV1sHuD8HaBKmSZkUR9JMI&_nc_ohc=NeXYqjXVmE4Q7kNvwG5iRD6&_nc_gid=MwvSvojl4Tx6NjsYdU5zSQ&edm=AOG-cTkBAAAA&ccb=7-5&oh=00_Af0lE9Rn73q-k9Dv8es_JJ_XeT3KiO7jwNn-1dEGovNS2A&oe=69DC4B28&_nc_sid=17ea04",
            "username": "chayan__artist"
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
  },
  "next_page_id": "QVFBWU1sQnMzcmNaaVJUN2ZjSkpxM0F5RmtHM1QtbXRTWFVOX1pTaUlXNW1xZFpoU2RfR09RQVEzLXZmOUJoc0lod2Npck5MSGpESUlDeU9YYXdCNEo3aw=="
}
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
        "strong_id__": "8958735",
        "pk": "8958735",
        "pk_id": "8958735",
        "id": "8958735",
        "fbid_v2": 17841401882050139,
        "third_party_downloads_enabled": 2,
        "profile_pic_id": "3354861487016662033_8958735",
        "profile_pic_url": "https://scontent-lhr6-2.cdninstagram.com/v/t51.2885-19/439586899_1933783770387040_7648789920126959876_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lhr6-2.cdninstagram.com&_nc_cat=104&_nc_oc=Q6cZ2gECJGxYR-zCni6pMaqE5GJ3ewjiV5xrKQY8ruyyLnPr17dbfcGJsLFlKpYq5wVsHmI&_nc_ohc=78gK351qr6gQ7kNvwGuh1ts&_nc_gid=spHOy34L-CqBRqkhMUqxrQ&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GFOQMxpg0rQexN4GAASBwUbo9SVqbkULAAAB1501500j-ccb7-5&oh=00_Af042cYc_KFqYwUdLg-ugGbO0PsEB_4pUb7pKUv-OqoKlA&oe=69DC42DC&_nc_sid=ce9561",
        "is_verified": true,
        "username": "christiehemmklok",
        "full_name": "Christie Hemm Klok",
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
        "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/v/t51.2885-19/416867607_774634348037538_4645960129122799142_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lhr8-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gECJGxYR-zCni6pMaqE5GJ3ewjiV5xrKQY8ruyyLnPr17dbfcGJsLFlKpYq5wVsHmI&_nc_ohc=9cpBf5YDNfEQ7kNvwEKTTUj&_nc_gid=spHOy34L-CqBRqkhMUqxrQ&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GBfl2BiiRSWdhsACACYO-kAfxHlAbkULAAAB1501500j-ccb7-5&oh=00_Af0-wkXTy8aTWX93XNfr0gWxt5GMxbR9wgfE7vMuGFumcg&oe=69DC38FB&_nc_sid=ce9561",
        "is_verified": true,
        "username": "stephaniemeiling",
        "full_name": "Stephanie Mei-Ling",
        "is_private": false,
        "has_anonymous_profile_picture": false,
        "account_badges": [],
        "latest_reel_media": 0,
        "is_favorite": false
      },
      {
        "strong_id__": "14331657700",
        "pk": "14331657700",
        "pk_id": "14331657700",
        "id": "14331657700",
        "fbid_v2": 17841414211021457,
        "third_party_downloads_enabled": 1,
        "profile_pic_id": "2073867961613189688_14331657700",
        "profile_pic_url": "https://scontent-lhr8-2.cdninstagram.com/v/t51.2885-19/65160972_483182759115510_2590728031043584000_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby41MDAuYzIifQ&_nc_ht=scontent-lhr8-2.cdninstagram.com&_nc_cat=106&_nc_oc=Q6cZ2gECJGxYR-zCni6pMaqE5GJ3ewjiV5xrKQY8ruyyLnPr17dbfcGJsLFlKpYq5wVsHmI&_nc_ohc=7ujGFVqjyKQQ7kNvwFh_x0A&_nc_gid=spHOy34L-CqBRqkhMUqxrQ&edm=ALB854YBAAAA&ccb=7-5&ig_cache_key=GAxH4gP2_rfAc7cBAAAAAABrHfQjbkULAAAB1501500j-ccb7-5&oh=00_Af3gb3-fdhCI23kzBIr2n4OviCiyVX1sewd-SF7XEegX8g&oe=69DC5A2D&_nc_sid=ce9561",
        "is_verified": false,
        "username": "natgeomagjp",
        "full_name": "ナショナルジオグラフィック日本版",
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
    "follow_ranking_token": "519c7995355e4f31953cb1809bcd5a7e|38834088383|osr",
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
            "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gGF1LlQnSG7ssR3CkoD5-zwxJc56ZKfJwA6Tz7AyM24FG--zsO4rlTvy-ZzqKvVx98&_nc_ohc=y1uvOTY1dWMQ7kNvwEg3yOs&_nc_gid=x_M-3yWkZUIMM3iQvxI0DA&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af2_B80UQHrcOdhmRyRG7b15w4kgq9FM3lE1wf6Ja25lxA&oe=69DC397C&_nc_sid=847350",
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
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGF1LlQnSG7ssR3CkoD5-zwxJc56ZKfJwA6Tz7AyM24FG--zsO4rlTvy-ZzqKvVx98&_nc_ohc=XbeNvhLXv28Q7kNvwHmFjmd&_nc_gid=x_M-3yWkZUIMM3iQvxI0DA&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ZO22RU69iffU67j1H4GKjYC1zLW5ITIbr9lKTDYXAKA&oe=69DC51E9&_nc_sid=847350",
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
            "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gGF1LlQnSG7ssR3CkoD5-zwxJc56ZKfJwA6Tz7AyM24FG--zsO4rlTvy-ZzqKvVx98&_nc_ohc=KnNItKNMJcAQ7kNvwFT56Np&_nc_gid=x_M-3yWkZUIMM3iQvxI0DA&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af0z57bddAb5JkHQFTFJkslzbwFOyq97JHaLm78ENXTwlg&oe=69DC5233&_nc_sid=847350",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1762880767,
        "seen_ranked_position": -1762880767,
        "media_count": 11,
        "updated_timestamp": 1762880767,
        "latest_reel_media": 1762870363,
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
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGF1LlQnSG7ssR3CkoD5-zwxJc56ZKfJwA6Tz7AyM24FG--zsO4rlTvy-ZzqKvVx98&_nc_ohc=XbeNvhLXv28Q7kNvwHmFjmd&_nc_gid=x_M-3yWkZUIMM3iQvxI0DA&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ZO22RU69iffU67j1H4GKjYC1zLW5ITIbr9lKTDYXAKA&oe=69DC51E9&_nc_sid=847350",
          "account_badges": [],
          "interop_messaging_user_fbid": 113671860027320,
          "is_creator_agent_enabled": false
        },
        "pk": "18018069326790931",
        "items": []
      },
      {
        "strong_id__": "highlight:17893209825281221",
        "id": "highlight:17893209825281221",
        "reel_type": "highlight_reel",
        "title": "Limitless",
        "created_at": 1754674432,
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
            "url": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gGF1LlQnSG7ssR3CkoD5-zwxJc56ZKfJwA6Tz7AyM24FG--zsO4rlTvy-ZzqKvVx98&_nc_ohc=-NOYVJuE190Q7kNvwFnR-d9&_nc_gid=x_M-3yWkZUIMM3iQvxI0DA&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af1k5_R0Y3jijFj01yta8MXiJnOLr6Mi7smZ_QMnIkNHbQ&oe=69DC571C&_nc_sid=847350",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1754674495,
        "seen_ranked_position": -1754674495,
        "media_count": 11,
        "updated_timestamp": 1754674495,
        "latest_reel_media": 1752840788,
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
          "profile_pic_url": "https://scontent-sea5-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sea5-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGF1LlQnSG7ssR3CkoD5-zwxJc56ZKfJwA6Tz7AyM24FG--zsO4rlTvy-ZzqKvVx98&_nc_ohc=XbeNvhLXv28Q7kNvwHmFjmd&_nc_gid=x_M-3yWkZUIMM3iQvxI0DA&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2ZO22RU69iffU67j1H4GKjYC1zLW5ITIbr9lKTDYXAKA&oe=69DC51E9&_nc_sid=847350",
          "account_badges": [],
          "interop_messaging_user_fbid": 113671860027320,
          "is_creator_agent_enabled": false
        },
        "pk": "17893209825281221",
        "items": []
      }
    ],
    "last_paginated_highlights_node_edited_at_ts": null,
    "has_fetched_all_remaining_highlights": null,
    "suggested_highlights": {},
    "cursor": null,
    "highlights_tray_type": "DEFAULT",
    "status": "ok"
  },
  "next_page_id": null
}
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
            "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/588606107_1189628196448486_727960022166174119_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHUalXwQ3giN2dX0L_-0yIuz9Kt0MsiiI9PT5YbPLbzZJqjEAM0qXEqHQMDEEAj-t0&_nc_ohc=y1uvOTY1dWMQ7kNvwGLVuhO&_nc_gid=rp2HsQQ6o3PpRPuZmzicMQ&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af1EzUg1rBSv0IjHf6RLhSYcCvVwKbzdGsBUinXznCXC1g&oe=69DC397C&_nc_sid=847350",
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
          "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHUalXwQ3giN2dX0L_-0yIuz9Kt0MsiiI9PT5YbPLbzZJqjEAM0qXEqHQMDEEAj-t0&_nc_ohc=XbeNvhLXv28Q7kNvwHnRixB&_nc_gid=rp2HsQQ6o3PpRPuZmzicMQ&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3mo9N2O4fcffXx-q-2N79VMCiw9-Wkx9iUrrdfeqFLcQ&oe=69DC51E9&_nc_sid=847350",
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
            "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/566565317_698760956040170_6433458010492878047_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gHUalXwQ3giN2dX0L_-0yIuz9Kt0MsiiI9PT5YbPLbzZJqjEAM0qXEqHQMDEEAj-t0&_nc_ohc=KnNItKNMJcAQ7kNvwFTXxDq&_nc_gid=rp2HsQQ6o3PpRPuZmzicMQ&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af2oOBgPvitq3-AfqVRzEPIM8g68wibS8KkaeUzisArqDg&oe=69DC5233&_nc_sid=847350",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1762880767,
        "seen_ranked_position": -1762880767,
        "media_count": 11,
        "updated_timestamp": 1762880767,
        "latest_reel_media": 1762870363,
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
          "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHUalXwQ3giN2dX0L_-0yIuz9Kt0MsiiI9PT5YbPLbzZJqjEAM0qXEqHQMDEEAj-t0&_nc_ohc=XbeNvhLXv28Q7kNvwHnRixB&_nc_gid=rp2HsQQ6o3PpRPuZmzicMQ&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3mo9N2O4fcffXx-q-2N79VMCiw9-Wkx9iUrrdfeqFLcQ&oe=69DC51E9&_nc_sid=847350",
          "account_badges": [],
          "interop_messaging_user_fbid": 113671860027320,
          "is_creator_agent_enabled": false
        },
        "pk": "18018069326790931",
        "items": []
      },
      {
        "strong_id__": "highlight:17893209825281221",
        "id": "highlight:17893209825281221",
        "reel_type": "highlight_reel",
        "title": "Limitless",
        "created_at": 1754674432,
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
            "url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.71878-15/529839968_1442036193794395_3733404095584309526_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHUalXwQ3giN2dX0L_-0yIuz9Kt0MsiiI9PT5YbPLbzZJqjEAM0qXEqHQMDEEAj-t0&_nc_ohc=-NOYVJuE190Q7kNvwEgDatK&_nc_gid=rp2HsQQ6o3PpRPuZmzicMQ&edm=ALbqBD0BAAAA&ccb=7-5&oh=00_Af00cfw6brMyQ66F5NTJgobF5gbi44rGn8gojk7umoCuMQ&oe=69DC571C&_nc_sid=847350",
            "width": 150
          },
          "full_image_version": null
        },
        "ranked_position": -1754674495,
        "seen_ranked_position": -1754674495,
        "media_count": 11,
        "updated_timestamp": 1754674495,
        "latest_reel_media": 1752840788,
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
          "profile_pic_url": "https://scontent-xxb1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxb1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHUalXwQ3giN2dX0L_-0yIuz9Kt0MsiiI9PT5YbPLbzZJqjEAM0qXEqHQMDEEAj-t0&_nc_ohc=XbeNvhLXv28Q7kNvwHnRixB&_nc_gid=rp2HsQQ6o3PpRPuZmzicMQ&edm=ALbqBD0BAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af3mo9N2O4fcffXx-q-2N79VMCiw9-Wkx9iUrrdfeqFLcQ&oe=69DC51E9&_nc_sid=847350",
          "account_badges": [],
          "interop_messaging_user_fbid": 113671860027320,
          "is_creator_agent_enabled": false
        },
        "pk": "17893209825281221",
        "items": []
      }
    ],
    "last_paginated_highlights_node_edited_at_ts": null,
    "has_fetched_all_remaining_highlights": null,
    "suggested_highlights": {},
    "cursor": null,
    "highlights_tray_type": "DEFAULT",
    "status": "ok"
  },
  "next_page_id": null
}
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
                5288,
                7932
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/658030605_1256609569870746_7397274986069476460_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bCRwORgGzQAQ7kNvwHw1hys&_nc_oc=AdokP5aUa5pA8gOOoUbAnfjCQTkBRHgOr32fjraHnngvZ7f83-bBhNkfMfF7S7_0Iw8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af3mRR29bXv8UDaMAdazwGyS4QK6f0a60kjNtBCck4xSCA&oe=69DC528D",
              "width": 640,
              "is_spatial_image": false
            },
            "igtv_first_frame": {
              "estimated_scans_sizes": [
                2644,
                5288,
                7932
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/658030605_1256609569870746_7397274986069476460_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=bCRwORgGzQAQ7kNvwHw1hys&_nc_oc=AdokP5aUa5pA8gOOoUbAnfjCQTkBRHgOr32fjraHnngvZ7f83-bBhNkfMfF7S7_0Iw8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af3mRR29bXv8UDaMAdazwGyS4QK6f0a60kjNtBCck4xSCA&oe=69DC528D",
              "width": 640,
              "is_spatial_image": false
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
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwHU_mM2&_nc_oc=AdquHDQuROTOYtzevl5e_mjLjgkxWoAMGqZ-8b-bLYO_qtd_GVWVEOBPd4QTzH2wOLA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2SwpZI69LGDZ2jVytysVCum8S9gUwqVS0vdZ2mrgjwfg&oe=69DC65F1",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "file_size_kb": 264,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_urls": [
                "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/658824281_1470987474415399_4266216838222781851_n.jpg?_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=j0uLJKlNhxwQ7kNvwGar08q&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&oh=00_Af0IaN29kZ2wayyLXlxmSC2BLjLUH_QsctJ3CZy45AvkvA&oe=69DC350C&_nc_sid=b41fef"
              ],
              "sprite_width": 1500,
              "thumbnail_duration": 0.5723904761904762,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "video_length": 60.101
            }
          }
        },
        "media_type": 2,
        "original_width": 1080,
        "original_height": 1920,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiN2NjOWJmY2I2MjAzNDY4MWJmM2M5YTEwNTViMmNkYzAzODY1NjU5NzI5Nzk2MTk5OTM1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkyNjQ5NXwzODY1NjU5NzI5Nzk2MTk5OTM1fDM3MzYyODg3MTIxfGIyMjE4OGFiOTBlN2I1NDg3YzZiM2Y4YTE5NmUyMGJiOWZlNzM4OGY3MmMwYWRiODNkNDQxZDczMzVjYWY5MDkifSwic2lnbmF0dXJlIjoiIn0=",
        "music_metadata": null,
        "has_tagged_users": true,
        "clips_tab_pinned_user_ids": [],
        "original_lang_for_translations": "en",
        "is_open_to_public_submission": false,
        "is_social_ufi_disabled": false,
        "timeline_pinned_user_ids": [
          787132
        ],
        "taken_at": 1775048403,
        "photo_of_you": false,
        "can_see_insights_as_brand": false,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "fb_user_tags": {
          "in": []
        },
        "media_overlay_info": null,
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "is_artist_pick": false,
        "media_notes": {
          "items": []
        },
        "product_type": "clips",
        "subscribe_cta_visible": false,
        "creative_config": null,
        "is_cutout_sticker_allowed": false,
        "cutout_sticker_info": [],
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "meta_ai_suggested_prompts": [],
        "gen_ai_chat_with_ai_cta_info": null,
        "can_reply": false,
        "floating_context_items": [],
        "is_eligible_content_for_post_roll_ad": false,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "eligible_insights_entrypoints": "NONE",
        "media_attributions_data": [],
        "media_ui_attributions_data": [],
        "media_ui_attributions_data_v2": [],
        "creator_product_link_infos": [],
        "is_eligible_for_poe": true,
        "is_eligible_for_organic_eager_refresh": false,
        "commerce_integrity_review_decision": "",
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
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
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658028372_18581900908043047_3222942396626887724_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=zov5ST0QeW4Q7kNvwHlaZdO&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GFS3OCcnG_DyIwRCACzkfaoIMbosbmNDAQAB1501500j-ccb7-5&oh=00_Af2srnsm0gpZaeQfG3IFMkwpA9l-v3rO58o0gJYWQShyxA&oe=69DC4D93&_nc_sid=b41fef",
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
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/656558113_18577653481026735_1735858011052165396_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby44MDAuYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=HX8JmLcZS9cQ7kNvwEY5q4T&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCFIIievNH8ERwBCABTJRwGqARcYbmNDAQAB1501500j-ccb7-5&oh=00_Af25hA6OqiZi8C1MKzQm-rs_Kw8N4rprjqPJjJCp8faiVQ&oe=69DC5A43&_nc_sid=b41fef",
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
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "collab_follow_button_info": {
          "show_follow_button": true,
          "is_owner_in_author_exp": true
        },
        "igbio_product": null,
        "is_organic_product_tagging_eligible": true,
        "is_paid_partnership": false,
        "reshare_count": 1937,
        "ig_media_sharing_disabled": false,
        "media_reposter_bottomsheet_enabled": false,
        "media_repost_count": 941,
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
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.02S\" FBManifestTimestamp=\"1775663926\" FBManifestIdentifier=\"Fuzss50NKRbkmJfH7/yMBiIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.02S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"1717383415916082a\" bandwidth=\"66633\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66633\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m78/AQP8tU61NyFxmx8kahNzpNBo21Ic0k3EA2wq62BMX6LFNZqlvyo_HZ9uCNMY_ySnjcXlDmMuSA1MAH20tiDo9fIIsQ1FTU7o4CN7myI.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=bvY1V1vszasQ7kNvwGY30Sz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo2Njc5NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af29GZ6JAaxaVOESfws4_bGPiCPcxbJQ0XwsVtn4HPJL4A&amp;oe=69D873C7</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
            "progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQM3BWmWT9DCIR_4a6ETqY74iK_vSJ0mGCY5KURpD0ZI6aeamU2Fve1dXA5lCRBiztE1g_SEXMn_Iq_pDtwv8Zw.mp4?_nc_cat=107&_nc_sid=8bf8fe&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=3yv_Gp1gyOgQ7kNvwH1lg1Y&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af20HeaKDsmOHZgqgOlYbtSTMcKPIMSwIGTxIN4j6dELLQ&oe=69D8476D",
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
              "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef"
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
        "like_count": 35859,
        "has_liked": false,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "can_viewer_save": true,
        "caption": {
          "strong_id__": "18174883744398454",
          "bit_flags": 0,
          "created_at": 1775048407,
          "created_at_utc": 1775048407,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "18174883744398454",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 3865659729796199935,
          "status": "Active",
          "type": 1,
          "user_id": 787132,
          "text": "This Earth Month, step into wonder with National Geographic as we celebrate everything that makes our planet so extraordinary 🌍\n\nStream the National Geographic #EarthMonth collection all April long on @DisneyPlus. #StepIntoWonder",
          "user": {
            "strong_id__": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "id": "787132",
            "is_unpublished": false,
            "fbid_v2": 17841400573960012,
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef"
          },
          "is_covered": false,
          "private_reply_status": 0
        },
        "comment_count": 236,
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
        "is_comments_gif_composer_enabled": false,
        "locations": [],
        "shop_routing_user_id": null,
        "featured_products": [],
        "are_remixes_crosspostable": true,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "is_eligible_for_autodub": false,
        "is_eligible_for_autodub_upsell": false,
        "video_sticker_locales": [],
        "has_audio": true,
        "video_duration": 60.10100173950195,
        "is_dash_eligible": 1,
        "video_versions": [
          {
            "bandwidth": 1568436,
            "height": 1280,
            "id": "1258679306414510v",
            "type": 101,
            "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwF1CBMT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3qV3hgLMcRrpYc27xyOUWrOKLnP3uABOaKcWUVw6YaNw&oe=69D84A2E",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1568436,
            "height": 1280,
            "id": "1258679306414510v",
            "type": 102,
            "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwF1CBMT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3qV3hgLMcRrpYc27xyOUWrOKLnP3uABOaKcWUVw6YaNw&oe=69D84A2E",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1568436,
            "height": 1280,
            "id": "1258679306414510v",
            "type": 103,
            "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwF1CBMT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3qV3hgLMcRrpYc27xyOUWrOKLnP3uABOaKcWUVw6YaNw&oe=69D84A2E",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.101768S\" FBManifestTimestamp=\"1775663926\" FBManifestIdentifier=\"Fuzss50NGBJyMmF2MS1yMWdlbjJ2cDktbTMZxraJxpnwkvECjNnxgZuPjwT4stmliZm5BLzN2fTZweUFmpjfwsvS2Ab2jc22sdnYBuSVwq6x85UHzIqHl+PItgfq7MGKwvrFB9bylbjgtpcL0pa399PQmQyK78y/iIvqDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIjYOFAASFAIA\"><Period id=\"0\" duration=\"PT60.101768S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.7\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"811763878117979v\" bandwidth=\"262728\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q20\" FBContentLength=\"1973809\" FBPlaybackResolutionMos=\"0:100,360:62.9,480:58.1,720:53.3,1080:50.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.3,480:89.8,720:86.4,1080:80.8\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP4s_c0uSAuy00HwODOQxGqL_KE1A5w9lnFiX0JfdCCMJTPukZiwIvC7uddABS-MUJBTNgcjIqVwxgJQEL9EM2gpulN4btvCIHeIYE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=-PmLEytgxDcQ7kNvwFocu0O&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjYyNzI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af35lJuEkaLB8fiIUpyldjhYXCPPBU1EtPI_Y5vXnB-5FQ&amp;oe=69DC648E</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-6086\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-129562\" FBFirstSegmentRange=\"1014-166973\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"166974-328722\" FBPrefetchSegmentRange=\"1014-166973\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1159146579572294v\" bandwidth=\"377484\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q30\" FBContentLength=\"2835938\" FBPlaybackResolutionMos=\"0:100,360:68.5,480:63.8,720:58.3,1080:55.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.8,480:92.9,720:90.7,1080:85.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMeaQpVDw5N0MxBLbLlLw4lSRHBoeCxqRWEdQxK9-uXl9boeDW4fLNwvdk093JFHDC5HeJYG-12qm4BaWfLYFo8emoy6rS4rnz8i4c.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=Lw0vzjNBHBgQ7kNvwG7FPSB&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6Mzc3NDg0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af29WapQBFRzKdhevawk2xzsXEWKMfwlTHhzmHbeypLSJA&amp;oe=69DC671B</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-7174\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-184877\" FBFirstSegmentRange=\"1014-237575\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"237576-461968\" FBPrefetchSegmentRange=\"1014-237575\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2124162255043381v\" bandwidth=\"485928\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q40\" FBContentLength=\"3650647\" FBPlaybackResolutionMos=\"0:100,360:71.5,480:67,720:61.5,1080:57.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:94.7,720:92.9,1080:88.4\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOz6ELjZ949BogdJm_QNe1EGQjv1zTfVS_ZRTHhaA80l6nyo0X-36y79QprnZ4mpheYpPgrlqKovz2Z7nwAtkupZFh-qPPgSofw_SI.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=RIdyZ7swaFgQ7kNvwFwOXR4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDg1OTI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2gwj_A_t83ACLVXD_osseH_xBIGW-dZv7-StuUQH-aCQ&amp;oe=69DC656D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8131\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-237174\" FBFirstSegmentRange=\"1014-303731\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"303732-578455\" FBPrefetchSegmentRange=\"1014-303731\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1251674976627900v\" bandwidth=\"619033\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q50\" FBContentLength=\"4650624\" FBPlaybackResolutionMos=\"0:100,360:74,480:69.7,720:64.2,1080:60.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95.9,720:94.7,1080:90.6\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNqHjWw34JU1zEWGF9C1h7VwlLIrqdJWbZ4OklUXgX1JUvMWrcXQ-RHcIlLZ5-leK-3oztau40NjRSFd8sWnMMpU8GdkzR1wupOZ10.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=pcYzS9tQp0IQ7kNvwHt5JJY&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NjE5MDMzLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3-w7J_QFd_hj9s4aXBDZwaTk6eSsvyQWf-zHyS-tvMog&amp;oe=69DC620C</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-8867\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-298106\" FBFirstSegmentRange=\"1014-381215\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"381216-715818\" FBPrefetchSegmentRange=\"1014-381215\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"2090322355085990v\" bandwidth=\"859541\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q60\" FBContentLength=\"6457494\" FBPlaybackResolutionMos=\"0:100,360:76.8,480:72.8,720:67.2,1080:63\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.8,720:96.6,1080:93.2\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOiOZhsUH6TLkrnE9FwF7XkrsQrJbO4ranASPXWOp_kfZQnOZspqXMH9zwqL2A5ODtpWwSfSYjqVdnN5JwtnoKgDmzpRneeR6UjSf0.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=P_g-CdgV6u4Q7kNvwH2OtBd&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6ODU5NTQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0XjsWo_qRafRGSUPCs_oN_lWwzAcOAEt1GL7IX1Xf5uQ&amp;oe=69DC51BD</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-10444\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-407931\" FBFirstSegmentRange=\"1014-520416\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"520417-950605\" FBPrefetchSegmentRange=\"1014-520416\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1630604991607646v\" bandwidth=\"1133257\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q70\" FBContentLength=\"8513850\" FBPlaybackResolutionMos=\"0:100,360:79.2,480:74.9,720:69.3,1080:64.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.07,480:97.5,720:97.6,1080:94.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP6A5LFkcBJyvdNdliF_xHUaxD51PWWWorNb6dDtDzQ7XD8gAviBfoW1AVfcumwubAQFQ032SHQZ6jcxptLJTaTYNl8toVCs_2M5DY.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=MiND23-EIg0Q7kNvwHnQRt0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTEzMzI1NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2mzBb3cuxmtylbc072r3w2AKkoPfqgkFJIq2ummh_w0Q&amp;oe=69DC478B</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-11592\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-528888\" FBFirstSegmentRange=\"1014-673311\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"673312-1205023\" FBPrefetchSegmentRange=\"1014-673311\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4455411234741189v\" bandwidth=\"1595477\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q80\" FBContentLength=\"11986380\" FBPlaybackResolutionMos=\"0:100,360:81.7,480:76.7,720:71.1,1080:66.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.55,480:98.2,720:98.36,1080:96.3\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQO_EY8JAwoG2qGh3eNttzDv3bWaZbosyVqFsbHFSUR4ZIUqvEF3dIs_iUyiWHHffWx17NcAJslxKGK2F9yc3KKxTtB-3yov2ohU284.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=IcB0Uykb9IYQ7kNvwGZuKBI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTU5NTQ3NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2aiqavcnvgQwciTgNj26sYA4eTD2tDL7sI6MWbN_xgKg&amp;oe=69DC368D</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-13404\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-713619\" FBFirstSegmentRange=\"1014-916365\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"916366-1632404\" FBPrefetchSegmentRange=\"1014-916365\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1883899549033339v\" bandwidth=\"2141971\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-m3_q90\" FBContentLength=\"16092034\" FBPlaybackResolutionMos=\"0:100,360:84.6,480:79.8,720:74.1,1080:69.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.68,480:98.58,720:98.79,1080:98.46\" FBAbrPolicyTags=\"\" width=\"1080\" height=\"1920\" frameRate=\"11988/500\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMAha-Ay45jS94TL8ynk5QQMBTTvF50BcTEUfE52AZhmIWcW5z7BSGD7RuWJzR1UJ1XHTtxnis--HnzX7LnQt9XFRHTMhfDthD67SM.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=teHbZCY8fNsQ7kNvwERwDno&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LW0zX3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NDE3MDk4OTExMDYwMywiYXNzZXRfYWdlX2RheXMiOjcsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MjE0MTk3MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af157w7Zw5_RPtCwZmEPUywODm8urAHegD9pvJP-OoE_Kg&amp;oe=69DC4BD5</BaseURL><SegmentBase indexRange=\"826-1013\" timescale=\"11988\" FBMinimumPrefetchRange=\"1014-16410\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1014-962472\" FBFirstSegmentRange=\"1014-1247892\" FBFirstSegmentDuration=\"5005\" FBSecondSegmentRange=\"1247893-2246471\" FBPrefetchSegmentRange=\"1014-1247892\" FBPrefetchSegmentDuration=\"5005\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"2018486635742578a\" bandwidth=\"46242\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"46242\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"347952\" FBPaqMos=\"87.47\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN6d2WH86jHFShcbXf9sjQbZkQC0xUp0rW7EDnG4Bq4tXew6Pz2MHtHSrpUQKKBEGJCn216bnzZ43Z6y4oPrg8CshaIRDStXBf_2m8.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=p_6H5YxvVOsQ7kNvwGFG9Do&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo0NjM3OCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1jHl1OTjDx_elhnqQesDsFGGB2CMwaUMrJBKkDKr_UhA&amp;oe=69DC4148</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-2090\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-13193\" FBFirstSegmentRange=\"1025-25675\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"25676-52073\" FBPrefetchSegmentRange=\"1025-25675\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"3434060956755369a\" bandwidth=\"76016\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"76016\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"571334\" FBPaqMos=\"88.88\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPiBT48Or08Wq2GueJ_a1ZGlP5QobL4jCYts8LWjbigiJaGQYlGIGdimLvTRUGI0Qy06ehqd8LGIkG1qUx2Q1PSVeSpBpibYNGQTcw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=s1577foHLbUQ7kNvwGbWzQI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjo3NjE1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1B96ZZFoWEi8hIZs4Eezqv3OMe0Qh023Xgmc_mRaqD5A&amp;oe=69DC64A5</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2475\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-21765\" FBFirstSegmentRange=\"1026-40537\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"40538-84371\" FBPrefetchSegmentRange=\"1026-40537\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"1883782792341005a\" bandwidth=\"105481\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"105481\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"792391\" FBPaqMos=\"90.32\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNe18lXJWbOpFruCxw7tvHWDJwvLtPJ4A3aWliKSnQwQggwuFpt247QNTOPKpxOYARAZ0l711AUP70HG4efjUphK33t2U_SaotfKeo.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=4RJy2Aqlc90Q7kNvwGczPja&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMDU2MTYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3QUrQvcFrS5SiLj9JG_q30yOOb3PDVwo-qU_qTLDaJ8A&amp;oe=69DC4B9E</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2371\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-29113\" FBFirstSegmentRange=\"1021-57428\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"57429-121150\" FBPrefetchSegmentRange=\"1021-57428\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"3147742935432363a\" bandwidth=\"137156\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"137156\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1030031\" FBPaqMos=\"91.90\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQP_rTgUjxqk_-kh-SP-bwQXBAWsh2FhnEOAntOUAYLiE6AGbZrgLCCQ311RK6AMTE9vBeDWK_JptQx8gsbsogY_ivE-bvNPRZah-eI.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=0oFa_fCas-kQ7kNvwHKo8Xe&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU0MTcwOTg5MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6NywidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJiaXRyYXRlIjoxMzcyOTEsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af38RUfaS3U6Y5K5ZqylowXtn6lbp22TWxYDIazryW6YTA&amp;oe=69DC45AD</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2418\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-35310\" FBFirstSegmentRange=\"1021-75028\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"75029-156364\" FBPrefetchSegmentRange=\"1021-75028\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "number_of_qualities": 8,
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "sharing_friction_info": {
          "should_have_sharing_friction": false,
          "bloks_app_url": null,
          "sharing_friction_payload": null
        },
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "user": {
          "pk": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "can_viewer_reshare": true,
        "video_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOAmX7PhXTKijCqW6rDeLpSN_wL8whRCnUoNzin8H65dG-21Y0GON3WSDTc2UhMuMeEvV__9iHUf5xoAP9LUd2qYL5gKXBDHPM9dRE.mp4?_nc_cat=105&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=ZO8AcE1k9sEQ7kNvwF1CBMT&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTQxNzA5ODkxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjo3LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=677de3d6a5fdc31d&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC83NjQ5OEI0MzYyOTI4MzNENTY5MjBDODE1RTU3QUNCNl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzdCNEEwMkE2Qzg1NkY3NjNBMUZDOTQxMUFGMUQ4OEFEX2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWldeAps7kPxUCKAJDMywXQE4M7ZFocrAYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af3qV3hgLMcRrpYc27xyOUWrOKLnP3uABOaKcWUVw6YaNw&oe=69D84A2E",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              24827,
              49654,
              74482
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwHU_mM2&_nc_oc=AdquHDQuROTOYtzevl5e_mjLjgkxWoAMGqZ-8b-bLYO_qtd_GVWVEOBPd4QTzH2wOLA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2SwpZI69LGDZ2jVytysVCum8S9gUwqVS0vdZ2mrgjwfg&oe=69DC65F1",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/658912943_18646028512019133_4145673224655235330_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=108&ig_cache_key=Mzg2NTY1OTcyOTc5NjE5OTkzNTE4NjQ2MDI4NTA2MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=RNSEx3XJ91gQ7kNvwHU_mM2&_nc_oc=AdquHDQuROTOYtzevl5e_mjLjgkxWoAMGqZ-8b-bLYO_qtd_GVWVEOBPd4QTzH2wOLA&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2SwpZI69LGDZ2jVytysVCum8S9gUwqVS0vdZ2mrgjwfg&oe=69DC65F1",
        "location": null,
        "usertags": [],
        "taken_at_ts": 1775048403,
        "sponsor_tags": [],
        "play_count": 0
      },
      {
        "strong_id__": "3844732796656436386_787132",
        "id": "3844732796656436386_787132",
        "caption_is_edited": false,
        "device_timestamp": 177254788691,
        "filter_type": 0,
        "is_post_live_clips_media": false,
        "disable_caption_and_comment": false,
        "like_and_view_counts_disabled": false,
        "fbid": 18401136481179230,
        "deleted_reason": 0,
        "client_cache_key": "Mzg0NDczMjc5NjY1NjQzNjM4Ng==.3",
        "integrity_review_decision": "pending",
        "pk": "3844732796656436386",
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
        "code": "DVbPBu5AESi",
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
                5005,
                10010,
                15015
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/641943524_1845518526116919_3841198709316411912_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Y4swoqOyiUUQ7kNvwEMIl_t&_nc_oc=Adrvr96IxfhNlK4d4f03vYSEIwusOFrGBReitw_9xKAyD7pCwUX-DyeRlyIwyFD6x6Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af0jpbyFTjC1K6seHIAkKeB6X0RsXvyT9Y3_bAbja5NOhg&oe=69DC47BC",
              "width": 640,
              "is_spatial_image": false
            },
            "igtv_first_frame": {
              "estimated_scans_sizes": [
                5005,
                10010,
                15015
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/641943524_1845518526116919_3841198709316411912_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=104&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=Y4swoqOyiUUQ7kNvwEMIl_t&_nc_oc=Adrvr96IxfhNlK4d4f03vYSEIwusOFrGBReitw_9xKAyD7pCwUX-DyeRlyIwyFD6x6Q&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af0jpbyFTjC1K6seHIAkKeB6X0RsXvyT9Y3_bAbja5NOhg&oe=69DC47BC",
              "width": 640,
              "is_spatial_image": false
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
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwFRWoKs&_nc_oc=AdrOfys49A73B0sLNIQBRkLgSwMYb7KXAspNceZI2KkxXiB6JifbSb16hTtnngwQ6RM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2cmpD5gzfNZplmGjtGk-jtRYJgyBLauZmaApmX9ZOdfg&oe=69DC51CA",
              "width": 750,
              "is_spatial_image": false
            }
          ],
          "scrubber_spritesheet_info_candidates": {
            "default": {
              "file_size_kb": 313,
              "max_thumbnails_per_sprite": 105,
              "rendered_width": 96,
              "sprite_height": 1232,
              "sprite_urls": [
                "https://scontent-ams2-1.cdninstagram.com/v/t51.71878-15/641022845_1856578795026695_839553732705161755_n.jpg?_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=k1TqxkNwNPkQ7kNvwEiYoiu&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&oh=00_Af0JTz9jv7892nykp3z_ry3u5Ae9vXtT-99Bo8JqqA9mYQ&oe=69DC5630&_nc_sid=b41fef"
              ],
              "sprite_width": 1500,
              "thumbnail_duration": 0.5721333333333333,
              "thumbnail_height": 176,
              "thumbnail_width": 100,
              "thumbnails_per_row": 15,
              "total_thumbnail_num_per_sprite": 105,
              "video_length": 60.074
            }
          }
        },
        "media_type": 2,
        "original_width": 1080,
        "original_height": 1920,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiN2NjOWJmY2I2MjAzNDY4MWJmM2M5YTEwNTViMmNkYzAzODQ0NzMyNzk2NjU2NDM2Mzg2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkyNjQ5N3wzODQ0NzMyNzk2NjU2NDM2Mzg2fDM3MzYyODg3MTIxfDE3MDJlMzU2YjYwOWU4MmU0YTZlNDhiOWRkYzc3YzM0NjI0MGMwMmFjYWQ0ZDYwM2ExNDI2NWY4MWI3OGY5ZmYifSwic2lnbmF0dXJlIjoiIn0=",
        "music_metadata": null,
        "has_tagged_users": true,
        "clips_tab_pinned_user_ids": [],
        "original_lang_for_translations": "en",
        "is_open_to_public_submission": false,
        "is_social_ufi_disabled": false,
        "timeline_pinned_user_ids": [
          787132
        ],
        "taken_at": 1772550004,
        "photo_of_you": false,
        "can_see_insights_as_brand": false,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "fb_user_tags": {
          "in": []
        },
        "media_overlay_info": null,
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "is_artist_pick": false,
        "media_notes": {
          "items": []
        },
        "product_type": "clips",
        "subscribe_cta_visible": false,
        "creative_config": null,
        "is_cutout_sticker_allowed": false,
        "cutout_sticker_info": [],
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "meta_ai_suggested_prompts": [],
        "gen_ai_chat_with_ai_cta_info": null,
        "can_reply": false,
        "floating_context_items": [],
        "is_eligible_content_for_post_roll_ad": false,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "eligible_insights_entrypoints": "NONE",
        "media_attributions_data": [],
        "media_ui_attributions_data": [],
        "media_ui_attributions_data_v2": [],
        "creator_product_link_infos": [],
        "is_eligible_for_poe": true,
        "is_eligible_for_organic_eager_refresh": false,
        "commerce_integrity_review_decision": "",
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
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
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/49530914_2223869040968021_377268303783002112_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby40MDAuYzIifQ&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=105&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=TYSekVkP8Y0Q7kNvwGRGtc6&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GCLI8wJVwTbcmOYHAAAAAACGUzwFbkULAAAB1501500j-ccb7-5&oh=00_Af3EHZEhoZz2L-KSzsShwJgOmy7ehZPKJrNq6Zj4r64x4Q&oe=69DC6398&_nc_sid=b41fef",
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
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=ic5ODsLE2O8Q7kNvwGMKuuw&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af0lx9CnmTifGBjaxvPGW_L3CfipuyD6kzH9JnD4cYC8eA&oe=69DC588C&_nc_sid=b41fef",
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
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "collab_follow_button_info": {
          "show_follow_button": true,
          "is_owner_in_author_exp": true
        },
        "igbio_product": null,
        "is_organic_product_tagging_eligible": true,
        "is_paid_partnership": false,
        "reshare_count": 19214,
        "ig_media_sharing_disabled": false,
        "media_reposter_bottomsheet_enabled": false,
        "media_repost_count": 3368,
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
            "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663926\" FBManifestIdentifier=\"Fuzss50NKRb65a+KkPmzCSIYEGF1ZGlvX2FhY19sbl92YnJkABIA\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\"><Representation id=\"2647505898961277a\" bandwidth=\"71376\" codecs=\"mp4a.40.5\" mimeType=\"audio/mp4\" FBAvgBitrate=\"71376\" audioSamplingRate=\"48000\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m78/AQN3360J8Qjpql7TL3xyh07CzDrDwdbxDjsDn69tBP-4LdVaJRGNou6HZlz1QHelX_R-p5TtkIZC9fYqJoWkXVMh5_um8WC3pcE2Ks4.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=KsVbwQ8QAugQ7kNvwE0w0yR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImRhc2hfbG5faGVhYWNfdmJyM19hdWRpbyIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6MjU2MjgxMDQwNTU4LCJjbGllbnRfbmFtZSI6InVua25vd24iLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NzE1MzksInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a39b&amp;_nc_zt=28&amp;oh=00_Af363kttLgRuAZkL8Aa0iJTaStF-m7H9f4CRLyHO90xnrg&amp;oe=69D86283</BaseURL><SegmentBase indexRange=\"824-1227\" timescale=\"48000\"><Initialization range=\"0-823\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
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
            "progressive_download_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQOu1cJkIUYpfLz5hsq6b4bAI93Dsnj-0FVN5QJfDUtHrdxoyYljTBeDYR-FHSZ5LvVWtD_zp4sNL8fsO46SW16u.mp4?_nc_cat=103&_nc_sid=8bf8fe&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=zRv5taEP1NwQ7kNvwFeONY5&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5WSV9VU0VDQVNFX1BST0RVQ1RfVFlQRS4uQzMuMC5wcm9ncmVzc2l2ZV9hdWRpbyIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af36jkH1X-VPUvXwd_vQfPmdO0sJ6_-5UtbPNGBlerD82A&oe=69D8409F",
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
              "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef"
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
        "like_count": 66069,
        "has_liked": false,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "can_viewer_save": true,
        "caption": {
          "strong_id__": "18401140165179230",
          "bit_flags": 0,
          "created_at": 1772550010,
          "created_at_utc": 1772550010,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "18401140165179230",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 3844732796656436386,
          "status": "Active",
          "type": 1,
          "user_id": 787132,
          "text": "Small in size, but their impact on our planet is huge 🐝 Join @bertiegregory as he explores the weird and wonderful world of bees.\n\n#SecretsOfTheBees premieres Tuesday, March 31 at 8/7c on @natgeotv. Stream on @DisneyPlus and @hulu.",
          "user": {
            "strong_id__": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "id": "787132",
            "is_unpublished": false,
            "fbid_v2": 17841400573960012,
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef"
          },
          "is_covered": false,
          "private_reply_status": 0
        },
        "comment_count": 614,
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
        "is_comments_gif_composer_enabled": false,
        "locations": [],
        "shop_routing_user_id": null,
        "featured_products": [],
        "are_remixes_crosspostable": true,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "is_eligible_for_autodub": false,
        "is_eligible_for_autodub_upsell": false,
        "video_sticker_locales": [],
        "has_audio": true,
        "video_duration": 60.07400131225586,
        "is_dash_eligible": 1,
        "video_versions": [
          {
            "bandwidth": 1607971,
            "height": 1280,
            "id": "1791310395606912v",
            "type": 101,
            "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwHigMxV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2iZ5Uu2BPwRyZqK4_lusl-1-s8c7PQurYgKFzJu5InkQ&oe=69D848EB",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1607971,
            "height": 1280,
            "id": "1791310395606912v",
            "type": 102,
            "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwHigMxV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2iZ5Uu2BPwRyZqK4_lusl-1-s8c7PQurYgKFzJu5InkQ&oe=69D848EB",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1607971,
            "height": 1280,
            "id": "1791310395606912v",
            "type": 103,
            "url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwHigMxV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2iZ5Uu2BPwRyZqK4_lusl-1-s8c7PQurYgKFzJu5InkQ&oe=69D848EB",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT60.074665S\" FBManifestTimestamp=\"1775663926\" FBManifestIdentifier=\"Fuzss50NGBVyMmF2MS1yMWdlbjJ2cDktc3ItbTMZts6vz+q68+cCloW29/706gKYpt6Nmb6WA8Cev8TGuqUDgOfs4t/R/wTkw82K6pLOBYjXqZnZwrkG+IDMucqplQewy4njp6j3B5C3mdTG0uwK0uKu+83j7g0iGCZkYXNoX3VuaWZpZWRfcHJlbWl1bV94aGUxMjM0X2licl9hdWRpbyI2SBQAEhQCAA==\"><Period id=\"0\" duration=\"PT60.074665S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:69.7\" FBCellQualityProfile=\"2\" FBQualityProfile=\"2\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.3; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.4; 100,2,1\"><Representation id=\"926794690062240v\" bandwidth=\"347369\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q20\" FBContentLength=\"2607838\" FBPlaybackResolutionMos=\"0:100,360:71.1,480:69.2,720:68.3,1080:68,1440:69.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.1,480:92.1,720:89.9,1080:85.1,1440:81.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQNX0WhGmAzCdZo6iXFxtohCQDAo6IkYWLLT-QexjwjCbNEO2J16rjugGx2qdpnVGYHrJyuW1juWbUYIZE-KKFzvjvEBxsTS9niZlpg.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=xY_c8h1oTdoQ7kNvwHjGays&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjM0NzM2OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1iuBnpV35YMPWJwiBdfVuJN-wFKPRcSartkIY2HJXsHA&amp;oe=69DC4190</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-16849\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-97894\" FBFirstSegmentRange=\"992-160729\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"160730-335227\" FBPrefetchSegmentRange=\"992-160729\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1579222173331698v\" bandwidth=\"473605\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q30\" FBContentLength=\"3555543\" FBPlaybackResolutionMos=\"0:100,360:75.6,480:73.7,720:72.5,1080:71.3,1440:72.3\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.3,480:95,720:93.5,1080:88.8,1440:85.5\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOn17sJvqdiMhkoGoFmRR5GvuvNKCHSPfM25qx56-aT4OI4BuqqNzI8j7dH7jh2N2_dbfIUJaoxqkpbbodQJRvwsNOMax8gwV-YhWA.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=7pNo1CqmBMEQ7kNvwHq2IIu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjQ3MzYwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3BDDy6YDZsXz4rJCy2Tv9Xj7Iz9FRFpS6DWF697jy5ew&amp;oe=69DC5B4B</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-19527\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-133927\" FBFirstSegmentRange=\"992-218133\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"218134-452895\" FBPrefetchSegmentRange=\"992-218133\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"3902778526521513v\" bandwidth=\"625656\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q40\" FBContentLength=\"4697049\" FBPlaybackResolutionMos=\"0:100,360:79.3,480:77.1,720:75.6,1080:73.9,1440:74.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.6,480:96.8,720:96,1080:91.6,1440:88.7\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQOOU8oXTyCVpU-lmAAc3_fl6kDSbhxCpH4efAxDxNoneEnKetCjQjLZ9KHtN3CUSDuJPZtsvli_XDHmo8b1ASvErktcaYsoq1DK9KE.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=A-cC6Mz09_0Q7kNvwHwf-lp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjYyNTY1NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0vQ3PkIxjoOpmY9aHzRz8Vl5h4LjuFzEp_wZzh3jQ8hA&amp;oe=69DC5066</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-22504\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-177689\" FBFirstSegmentRange=\"992-286646\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"286647-593012\" FBPrefetchSegmentRange=\"992-286646\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"3053662511508936v\" bandwidth=\"787710\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q50\" FBContentLength=\"5913657\" FBPlaybackResolutionMos=\"0:100,360:82.5,480:80,720:77.8,1080:75.8,1440:76\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.4,480:97.9,720:97.7,1080:93.8,1440:90.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN79BZn0MCXHe4haCJV-DuRXKj6NUoZ7pm6VPQmqmy_GFCaYVAYmItyNqQYpOuq9jfXPxjVgV8waXDdPAyxlBNzpNlPmbFohIPFsEI.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=fsdF06ZdvtUQ7kNvwHwvwBo&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjc4NzcxMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0xGq6ke7dDNu_APthMZh_SU9QHp0LmHOfYzeISHArslg&amp;oe=69DC6801</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-25197\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-226185\" FBFirstSegmentRange=\"992-362247\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"362248-746579\" FBPrefetchSegmentRange=\"992-362247\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"1406580284037568v\" bandwidth=\"1057308\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q60\" FBContentLength=\"7937634\" FBPlaybackResolutionMos=\"0:100,360:85.7,480:83.5,720:81.2,1080:77.8,1440:77.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.99,480:98.81,720:98.9,1080:96.4,1440:93.9\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPq9PBIrgCuw9czWULqIBNha5wIpimHyrnCPVuWOOYRLDS8EKKjne3_MAfCbpBUOfGsYNFTaoHLSsXNkDEAQBJLmxIulSE1TMAGnIg.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=UjuToJF2I9EQ7kNvwFSGvtp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjEwNTczMDgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0aaip58G8kfB3TKg44tNQVmh-BqSosilgCAEy8BSPufw&amp;oe=69DC5D37</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-31163\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-312092\" FBFirstSegmentRange=\"992-493774\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"493775-1013854\" FBPrefetchSegmentRange=\"992-493774\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"893871963490700v\" bandwidth=\"1533975\" codecs=\"av01.0.05M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q70\" FBContentLength=\"11516167\" FBPlaybackResolutionMos=\"0:100,360:88.7,480:86.7,720:84.6,1080:80.9,1440:80.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.448,480:99.335,720:99.445,1080:98.49,1440:97\" FBAbrPolicyTags=\"\" width=\"720\" height=\"1280\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMPETj8IpBiBkhacc3ka9xGGJY_Vhp_M65AbG8Lk30ZXwyPpsIJM1_dVRTCPZv8czkiBDcl9SgWUVn1gJ2r-FfblyChLlitxKrm-tM.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=215mmyF_ZIIQ7kNvwHZFwBx&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjE1MzM5NzUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3py7kLU2kfdgKIqON8dixcLq9BG_yEyGT2Mu17_K8-ZA&amp;oe=69DC42DF</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-39114\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-464852\" FBFirstSegmentRange=\"992-726697\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"726698-1500620\" FBPrefetchSegmentRange=\"992-726697\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation><Representation id=\"2017218692481084v\" bandwidth=\"2125286\" codecs=\"av01.0.08M.08\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9-sr-m3_q80\" FBContentLength=\"15955370\" FBPlaybackResolutionMos=\"0:100,360:91.1,480:89.3,720:87.2,1080:85.7,1440:85\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.582,480:99.57,720:99.638,1080:99.543,1440:99.51\" FBAbrPolicyTags=\"\" width=\"1080\" height=\"1920\" frameRate=\"23993/1000\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQPEq_fDYGM2ttktK9udbibTCz-aRwlCIgvxHxpDEhZ884BMwI1n2xS39QmwK4IEFNtqeQTjfVamkDY2mGr_g5VbMRAqF4G7H1jid8w.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=U6M1ngXlgTYQ7kNvwHzFQCg&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5LXNyLW0zX3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk0Njc1OTgyMjExMDYwMywiYXNzZXRfYWdlX2RheXMiOjM2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NjAsImJpdHJhdGUiOjIxMjUyODYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0z-WP7p_gAEFUcBzhiPNhnevkv80Bq2L3d7dobNAyBZA&amp;oe=69DC5AA7</BaseURL><SegmentBase indexRange=\"804-991\" timescale=\"23993\" FBMinimumPrefetchRange=\"992-54263\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"992-660245\" FBFirstSegmentRange=\"992-1035883\" FBFirstSegmentDuration=\"5001\" FBSecondSegmentRange=\"1035884-2133073\" FBPrefetchSegmentRange=\"992-1035883\" FBPrefetchSegmentDuration=\"5001\"><Initialization range=\"0-803\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"791432930126823a\" bandwidth=\"47670\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"47670\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"358991\" FBPaqMos=\"89.30\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQN3B75EZEr34ogr7GF1-T8vsbRKZ0Hzt6I6En8nSV9eT5yH8hS7FboShpOBcVDzR296sMqT1lRDQP7tvvVfVk_vfTYGsEUEbJ9ofr4.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=uKTN0fLYQqMQ7kNvwFdLoLS&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6NDc4MDUsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af100Kv8CDcBv_rU1Gkw6MMH_z4fJtdz5onnTkewKePL-A&amp;oe=69DC47B5</BaseURL><SegmentBase indexRange=\"837-1024\" timescale=\"48000\" FBMinimumPrefetchRange=\"1025-1967\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1025-15154\" FBFirstSegmentRange=\"1025-29469\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"29470-59290\" FBPrefetchSegmentRange=\"1025-29469\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2232701137531608a\" bandwidth=\"78366\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"78366\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"589501\" FBPaqMos=\"90.30\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQO_Kfz1SxVxfEtHysoYJq5EongdyvUBq28ntHTV81-Un7YiMtp5CGbiplQDZWPM7nySIjiDaI9682e_NoHPy7_xcMYwRpUfO3LIB2o.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=ytygejStfkIQ7kNvwGIhcfF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6Nzg1MDIsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2xnCNoXtRNaqv5DfrS8kJsdLkcPsHkdvW3L9FHHhLXJA&amp;oe=69DC56E7</BaseURL><SegmentBase indexRange=\"838-1025\" timescale=\"48000\" FBMinimumPrefetchRange=\"1026-2440\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1026-24395\" FBFirstSegmentRange=\"1026-48164\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"48165-95228\" FBPrefetchSegmentRange=\"1026-48164\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"798056319992139a\" bandwidth=\"130531\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"130531\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"981215\" FBPaqMos=\"92.51\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQMgwgSgO9Smp8fdwbQvnvHmK_0Xf5Jgb72LxKi21knzAy6E1NLnuOLJwxaVciThtRnzxMh6ORF8Z1IBJOLR96LzoKp0gxsKe_nG4q0.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=LKSgGeO3P60Q7kNvwEOPlUp&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTMwNjY2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3I06OTxSd2SC85otuEhcZ8VGS5O0DqlDTTBWSVqhKpDg&amp;oe=69DC617D</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2334\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-37007\" FBFirstSegmentRange=\"1021-75805\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"75806-158864\" FBPrefetchSegmentRange=\"1021-75805\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1815340029130180a\" bandwidth=\"160079\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"160079\" audioSamplingRate=\"48000\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"1203103\" FBPaqMos=\"93.89\" FBAbrPolicyTags=\"\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m367/AQM9jm9NeAu3kk1yLA4gL6O-f_KeHsx_JlKCAde_LcpIlfHLA-CDepjFEe_rO2ZLJ3VHegu6kP5A_uQF4PN8szOxKe0RvAJQKK5d5C4.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-ams2-1.cdninstagram.com&amp;_nc_ohc=I5_xZd0KA_oQ7kNvwGAyU8c&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLmNsaXBzLmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTQ2NzU5ODIyMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MzYsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo2MCwiYml0cmF0ZSI6MTYwMjE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0BQowgdx4nVpm0X3VJXIOYzdHfKkRnOTosYzxaP987cA&amp;oe=69DC575A</BaseURL><SegmentBase indexRange=\"833-1020\" timescale=\"48000\" FBMinimumPrefetchRange=\"1021-2350\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"1021-46420\" FBFirstSegmentRange=\"1021-94312\" FBFirstSegmentDuration=\"4949\" FBSecondSegmentRange=\"94313-194524\" FBPrefetchSegmentRange=\"1021-94312\" FBPrefetchSegmentDuration=\"4949\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "number_of_qualities": 7,
        "video_codec": "av01.0.05M.08",
        "sharing_friction_info": {
          "should_have_sharing_friction": false,
          "bloks_app_url": null,
          "sharing_friction_payload": null
        },
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "user": {
          "pk": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "can_viewer_reshare": true,
        "video_url": "https://scontent-ams2-1.cdninstagram.com/o1/v/t2/f2/m86/AQM8vwq3632EpxT289mrMgjKqJPimP7tCF0_ruWTHaRUi7oU92vxf3rkMhUZjQ-yzxIIQ38fCSKkgc4LtxJFly4Wkegg8H0grrBW3-A.mp4?_nc_cat=110&_nc_sid=5e9851&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_ohc=yD3DtfJ9jaEQ7kNvwHigMxV&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NDY3NTk4MjIxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjozNiwidmlfdXNlY2FzZV9pZCI6MTAwOTksImR1cmF0aW9uX3MiOjYwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&ccb=17-1&vs=d1e23419756dacf9&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9EODRFRENBQzc2Nzg5QkZGNzY4MTkxNDdGRkI2QUFBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyL0E3NDdDN0RBMkM3QkJDNTNDOUM1OTBCQzZBNjgzM0E4X2F1ZGlvX2Rhc2hpbml0Lm1wNBUCAsgBEgAoABgAGwKIB3VzZV9vaWwBMRJwcm9ncmVzc2l2ZV9yZWNpcGUBMRUAACaWvofB9J7hPxUCKAJDMywXQE4HjU_fO2QYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HZeadAQA&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2iZ5Uu2BPwRyZqK4_lusl-1-s8c7PQurYgKFzJu5InkQ&oe=69D848EB",
        "image_versions": [
          {
            "estimated_scans_sizes": [
              48270,
              96540,
              144811
            ],
            "height": 1333,
            "scans_profile": "e35",
            "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwFRWoKs&_nc_oc=AdrOfys49A73B0sLNIQBRkLgSwMYb7KXAspNceZI2KkxXiB6JifbSb16hTtnngwQ6RM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2cmpD5gzfNZplmGjtGk-jtRYJgyBLauZmaApmX9ZOdfg&oe=69DC51CA",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/643602382_18637335874019133_398500559288757580_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=106&ig_cache_key=Mzg0NDczMjc5NjY1NjQzNjM4NjE4NjM3MzM1ODY4MDE5MTMz.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTkyMC5zZHIuQzMifQ%3D%3D&_nc_ohc=Kt3jfB9bFKUQ7kNvwFRWoKs&_nc_oc=AdrOfys49A73B0sLNIQBRkLgSwMYb7KXAspNceZI2KkxXiB6JifbSb16hTtnngwQ6RM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2cmpD5gzfNZplmGjtGk-jtRYJgyBLauZmaApmX9ZOdfg&oe=69DC51CA",
        "location": null,
        "usertags": [],
        "taken_at_ts": 1772550004,
        "sponsor_tags": [],
        "play_count": 0
      },
      {
        "strong_id__": "3870670793969876810_787132",
        "id": "3870670793969876810_787132",
        "caption_is_edited": false,
        "device_timestamp": 1775642401,
        "filter_type": 0,
        "like_and_view_counts_disabled": false,
        "fbid": 17953701309107724,
        "deleted_reason": 0,
        "client_cache_key": "Mzg3MDY3MDc5Mzk2OTg3NjgxMA==.3",
        "integrity_review_decision": "pending",
        "pk": "3870670793969876810",
        "has_delayed_metadata": false,
        "mezql_token": "",
        "should_request_ads": false,
        "has_privately_liked": false,
        "is_quiet_post": false,
        "profile_grid_thumbnail_fitting_style": "UNSET",
        "collaborator_edit_eligibility": false,
        "share_count_disabled": false,
        "has_shared_to_fb": 0,
        "is_visual_reply_commenter_notice_enabled": true,
        "subtype_name_for_REST__": "XDTCarouselContainerMedia",
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "has_views_fetching_on_search_grid": false,
        "code": "DW3YpRVDb9K",
        "enable_media_notes_production": true,
        "has_views_fetching": true,
        "original_media_has_visual_reply_media": false,
        "report_info": {
          "has_viewer_submitted_report": false
        },
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                56778,
                113556,
                170335
              ],
              "height": 959,
              "scans_profile": "e35",
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1cFmE4g8o6wnxAVomalLv5np46QwZHBoWttllW56kT7w&oe=69DC4AFB",
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
              "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af3UxAODqTndzXScaClXGPBvtsojf9-QIGOOVHlpTv6mrg&oe=69DC4AFB",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 8,
        "original_width": 1439,
        "original_height": 959,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiN2NjOWJmY2I2MjAzNDY4MWJmM2M5YTEwNTViMmNkYzAzODcwNjcwNzkzOTY5ODc2ODEwIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkyNjQ5OHwzODcwNjcwNzkzOTY5ODc2ODEwfDM3MzYyODg3MTIxfGEwZTBhODQwYjY5MTBkMTQ1Njc4YjA3YWQ3Y2Y2MGExMTY1NmJhYzI0MzI0NDVlNjY1NTE4ZDA4Y2U1ODM3ZmUifSwic2lnbmF0dXJlIjoiIn0=",
        "music_metadata": {
          "audio_type": null,
          "music_canonical_id": "0",
          "pinned_media_ids": null,
          "music_info": null,
          "original_sound_info": null
        },
        "clips_tab_pinned_user_ids": [],
        "all_previous_submitters": [],
        "is_open_to_public_submission": false,
        "is_social_ufi_disabled": false,
        "timeline_pinned_user_ids": [],
        "taken_at": 1775642401,
        "can_see_insights_as_brand": false,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "fb_user_tags": {
          "in": []
        },
        "media_overlay_info": null,
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "media_notes": {
          "items": []
        },
        "product_type": "carousel_container",
        "subscribe_cta_visible": false,
        "creative_config": null,
        "is_cutout_sticker_allowed": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "meta_ai_suggested_prompts": [],
        "gen_ai_chat_with_ai_cta_info": null,
        "can_reply": false,
        "floating_context_items": [],
        "is_eligible_content_for_post_roll_ad": false,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "eligible_insights_entrypoints": "NONE",
        "media_attributions_data": [],
        "is_eligible_for_poe": true,
        "is_eligible_for_organic_eager_refresh": false,
        "commerce_integrity_review_decision": "",
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "coauthor_producers": [],
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "igbio_product": null,
        "is_organic_product_tagging_eligible": true,
        "is_paid_partnership": false,
        "ig_media_sharing_disabled": false,
        "media_reposter_bottomsheet_enabled": false,
        "media_repost_count": 754,
        "carousel_media_count": 10,
        "carousel_media_pending_post_count": 0,
        "can_modify_carousel": true,
        "carousel_media_ids": [
          3870670683399590370,
          3870670679968669302,
          3870670694816531730
        ],
        "carousel_media": [
          {
            "id": "3870670683399590370_787132",
            "explore_pivot_grid": false,
            "carousel_parent_id": "3870670793969876810_787132",
            "strong_id__": "3870670683399590370_787132",
            "pk": "3870670683399590370",
            "commerciality_status": "not_commercial",
            "product_type": "carousel_item",
            "media_type": 1,
            "caption": null,
            "image_versions2": {
              "candidates": [
                {
                  "estimated_scans_sizes": [
                    56778,
                    113556,
                    170335
                  ],
                  "height": 959,
                  "scans_profile": "e35",
                  "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1cFmE4g8o6wnxAVomalLv5np46QwZHBoWttllW56kT7w&oe=69DC4AFB",
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
                  "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af3UxAODqTndzXScaClXGPBvtsojf9-QIGOOVHlpTv6mrg&oe=69DC4AFB",
                  "width": 750,
                  "is_spatial_image": false
                }
              ]
            },
            "original_width": 1439,
            "original_height": 959,
            "featured_products": [],
            "fb_user_tags": {
              "in": []
            },
            "shop_routing_user_id": null,
            "media_overlay_info": null,
            "creative_config": null,
            "sharing_friction_info": {
              "bloks_app_url": null,
              "should_have_sharing_friction": false,
              "sharing_friction_payload": null
            },
            "taken_at": 1775642401,
            "product_suggestions": [],
            "image_versions": [
              {
                "estimated_scans_sizes": [
                  56778,
                  113556,
                  170335
                ],
                "height": 959,
                "scans_profile": "e35",
                "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1cFmE4g8o6wnxAVomalLv5np46QwZHBoWttllW56kT7w&oe=69DC4AFB",
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
                "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af3UxAODqTndzXScaClXGPBvtsojf9-QIGOOVHlpTv6mrg&oe=69DC4AFB",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1cFmE4g8o6wnxAVomalLv5np46QwZHBoWttllW56kT7w&oe=69DC4AFB"
          },
          {
            "id": "3870670679968669302_787132",
            "explore_pivot_grid": false,
            "carousel_parent_id": "3870670793969876810_787132",
            "strong_id__": "3870670679968669302_787132",
            "pk": "3870670679968669302",
            "commerciality_status": "not_commercial",
            "product_type": "carousel_item",
            "media_type": 1,
            "caption": null,
            "image_versions2": {
              "candidates": [
                {
                  "estimated_scans_sizes": [
                    40239,
                    80479,
                    120719
                  ],
                  "height": 959,
                  "scans_profile": "e35",
                  "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHW4XMR&_nc_oc=Adqp03iy1CWAMRdkatl2HBAFSm9rYclEj4WjQBt3CqK3-4ZFIFTkMZ0y21NxyMVxMAE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1hV59LrJSXeQCaOqyxuR56BAyKNOgVtijgi-sPN7L-OA&oe=69DC54D1",
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
                  "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHW4XMR&_nc_oc=Adqp03iy1CWAMRdkatl2HBAFSm9rYclEj4WjQBt3CqK3-4ZFIFTkMZ0y21NxyMVxMAE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1TwqIeNvXogvZ6CJuC5oDjTsGHcZbG4HkurXwin7Yw7g&oe=69DC54D1",
                  "width": 750,
                  "is_spatial_image": false
                }
              ]
            },
            "original_width": 1439,
            "original_height": 959,
            "featured_products": [],
            "fb_user_tags": {
              "in": []
            },
            "shop_routing_user_id": null,
            "media_overlay_info": null,
            "creative_config": null,
            "sharing_friction_info": {
              "bloks_app_url": null,
              "should_have_sharing_friction": false,
              "sharing_friction_payload": null
            },
            "taken_at": 1775642401,
            "product_suggestions": [],
            "image_versions": [
              {
                "estimated_scans_sizes": [
                  40239,
                  80479,
                  120719
                ],
                "height": 959,
                "scans_profile": "e35",
                "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHW4XMR&_nc_oc=Adqp03iy1CWAMRdkatl2HBAFSm9rYclEj4WjQBt3CqK3-4ZFIFTkMZ0y21NxyMVxMAE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1hV59LrJSXeQCaOqyxuR56BAyKNOgVtijgi-sPN7L-OA&oe=69DC54D1",
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
                "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHW4XMR&_nc_oc=Adqp03iy1CWAMRdkatl2HBAFSm9rYclEj4WjQBt3CqK3-4ZFIFTkMZ0y21NxyMVxMAE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1TwqIeNvXogvZ6CJuC5oDjTsGHcZbG4HkurXwin7Yw7g&oe=69DC54D1",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/662290123_18647813602019133_3044182566003914184_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY3OTk2ODY2OTMwMg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=4IW7I7HiiqsQ7kNvwHW4XMR&_nc_oc=Adqp03iy1CWAMRdkatl2HBAFSm9rYclEj4WjQBt3CqK3-4ZFIFTkMZ0y21NxyMVxMAE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1hV59LrJSXeQCaOqyxuR56BAyKNOgVtijgi-sPN7L-OA&oe=69DC54D1"
          },
          {
            "id": "3870670694816531730_787132",
            "explore_pivot_grid": false,
            "carousel_parent_id": "3870670793969876810_787132",
            "strong_id__": "3870670694816531730_787132",
            "pk": "3870670694816531730",
            "commerciality_status": "not_commercial",
            "product_type": "carousel_item",
            "media_type": 1,
            "caption": null,
            "image_versions2": {
              "candidates": [
                {
                  "estimated_scans_sizes": [
                    51971,
                    103943,
                    155915
                  ],
                  "height": 1080,
                  "scans_profile": "e35",
                  "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwFSOyCz&_nc_oc=AdoNdM4L1RY5aHcfgc9IIA8_5MNU-hmXai3MQkGLEzFwahrXU6hL5UwHeYiTm10w_Nw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2C0SeQPIBGgKDXADeE1kEmJsyMwDeMox0kLRMkf7G4yw&oe=69DC46CA",
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
                  "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwFSOyCz&_nc_oc=AdoNdM4L1RY5aHcfgc9IIA8_5MNU-hmXai3MQkGLEzFwahrXU6hL5UwHeYiTm10w_Nw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af0qd49j9tpegtfS0tOabyB9NicbZ9MVMie4vj3YYohFUA&oe=69DC46CA",
                  "width": 750,
                  "is_spatial_image": false
                }
              ]
            },
            "original_width": 1440,
            "original_height": 1080,
            "featured_products": [],
            "fb_user_tags": {
              "in": []
            },
            "shop_routing_user_id": null,
            "media_overlay_info": null,
            "creative_config": null,
            "sharing_friction_info": {
              "bloks_app_url": null,
              "should_have_sharing_friction": false,
              "sharing_friction_payload": null
            },
            "taken_at": 1775642401,
            "product_suggestions": [],
            "image_versions": [
              {
                "estimated_scans_sizes": [
                  51971,
                  103943,
                  155915
                ],
                "height": 1080,
                "scans_profile": "e35",
                "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwFSOyCz&_nc_oc=AdoNdM4L1RY5aHcfgc9IIA8_5MNU-hmXai3MQkGLEzFwahrXU6hL5UwHeYiTm10w_Nw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2C0SeQPIBGgKDXADeE1kEmJsyMwDeMox0kLRMkf7G4yw&oe=69DC46CA",
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
                "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwFSOyCz&_nc_oc=AdoNdM4L1RY5aHcfgc9IIA8_5MNU-hmXai3MQkGLEzFwahrXU6hL5UwHeYiTm10w_Nw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af0qd49j9tpegtfS0tOabyB9NicbZ9MVMie4vj3YYohFUA&oe=69DC46CA",
                "width": 750,
                "is_spatial_image": false
              }
            ],
            "thumbnail_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/661145289_18647813665019133_5581899396191584665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY5NDgxNjUzMTczMA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0NDB4MTA4MC5zZHIuQzMifQ%3D%3D&_nc_ohc=zctf7nvOgYIQ7kNvwFSOyCz&_nc_oc=AdoNdM4L1RY5aHcfgc9IIA8_5MNU-hmXai3MQkGLEzFwahrXU6hL5UwHeYiTm10w_Nw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af2C0SeQPIBGgKDXADeE1kEmJsyMwDeMox0kLRMkf7G4yw&oe=69DC46CA"
          }
        ],
        "open_carousel_show_follow_button": false,
        "open_carousel_submission_state": "closed",
        "like_count": 39886,
        "has_liked": false,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "can_viewer_save": true,
        "caption": {
          "strong_id__": "17953706634107724",
          "bit_flags": 0,
          "created_at": 1775642405,
          "created_at_utc": 1775642405,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "17953706634107724",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 3870670793969876810,
          "status": "Active",
          "type": 1,
          "user_id": 787132,
          "text": "Whorls, hexagons, and half-moon patterns can be found throughout nature, formed by natural processes such as wind and crashing waves. After spending time along the seashore, photographer and conservationist Jon McCormack discovered that our planet's familiar shapes and designs have guided his work for years. To celebrate this, he set out on a journey to capture nature's intriguing forms at every scale.\n\nSee more of his work and learn about nature's patterns at the link in bio.\n\nPhotographs by @jonmccormackphoto, courtesy of Damiani’s upcoming book Jon McCormack: Patterns - Art of the Natural World",
          "user": {
            "strong_id__": "787132",
            "pk": 787132,
            "pk_id": "787132",
            "id": "787132",
            "is_unpublished": false,
            "fbid_v2": 17841400573960012,
            "username": "natgeo",
            "full_name": "National Geographic",
            "is_private": false,
            "is_verified": true,
            "profile_pic_id": "3865702555259028436_787132",
            "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef"
          },
          "is_covered": false,
          "private_reply_status": 0
        },
        "comment_count": 104,
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
        "is_comments_gif_composer_enabled": false,
        "locations": [],
        "shop_routing_user_id": null,
        "featured_products": [],
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "sharing_friction_info": {
          "should_have_sharing_friction": false,
          "bloks_app_url": null,
          "sharing_friction_payload": null
        },
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "user": {
          "pk": "787132",
          "id": "787132",
          "username": "natgeo",
          "full_name": "National Geographic",
          "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": true
        },
        "can_viewer_reshare": true,
        "image_versions": [
          {
            "estimated_scans_sizes": [
              56778,
              113556,
              170335
            ],
            "height": 959,
            "scans_profile": "e35",
            "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af1cFmE4g8o6wnxAVomalLv5np46QwZHBoWttllW56kT7w&oe=69DC4AFB",
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
            "url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-15/669377477_18647813656019133_6482919518278250270_n.jpg?stp=dst-jpg_e35_s750x750_sh2.08_tt6&_nc_cat=1&ig_cache_key=Mzg3MDY3MDY4MzM5OTU5MDM3MA%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjE0Mzl4OTU5LnNkci5DMyJ9&_nc_ohc=mXOMLuc-TXMQ7kNvwEyNEJv&_nc_oc=Adop8LI0prlPX6K3y_Ooy0ERxvcaW6KkYOdZwZ7yBkO4OqoBw3M-Dn1JBT5-7TX31F0&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&_nc_ss=7a3ba&oh=00_Af3UxAODqTndzXScaClXGPBvtsojf9-QIGOOVHlpTv6mrg&oe=69DC4AFB",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "location": null,
        "usertags": [],
        "taken_at_ts": 1775642401,
        "sponsor_tags": [],
        "play_count": 0
      }
    ],
    "next_max_id": "3868170261056492782_787132",
    "user": {
      "strong_id__": "787132",
      "pk": 787132,
      "pk_id": "787132",
      "profile_grid_display_type": "default",
      "id": "787132",
      "username": "natgeo",
      "full_name": "National Geographic",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3865702555259028436_787132",
      "profile_pic_url": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFQBCOLmRucukIonGouChymboVb6-sAAK0_PM06wdv6M8ld38fg1FDnH8N-C2GcGgM&_nc_ohc=XbeNvhLXv28Q7kNvwGXs_I4&_nc_gid=Z4rMyqoDIFpUSURQVrMYAg&edm=ABmJApABAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0LZGQXuCct7laQJHqAHUAlWYM-qWBoNEx0TS7GpFCEYw&oe=69DC51E9&_nc_sid=b41fef",
      "is_active_on_text_post_app": true
    },
    "auto_load_more_enabled": true,
    "status": "ok"
  },
  "next_page_id": "3868170261056492782_787132"
}
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
    "latest_reel_media": 1775659002,
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
    "expiring_at": 1775745402,
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
      "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=XbeNvhLXv28Q7kNvwHiwpg4&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0eKNY7n-V0g-XQBbq2n67a8etKzcm3Ovh-IySYeE0vbQ&oe=69DC51E9&_nc_sid=6d62aa",
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
        "strong_id__": "3870828041672894129_787132",
        "id": "3870828041672894129_787132",
        "expiring_at": 1775745075,
        "pk": 3870828041672894129,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18311197711278628,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODA0MTY3Mjg5NDEyOQ==.3",
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
          "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=XbeNvhLXv28Q7kNvwHiwpg4&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0eKNY7n-V0g-XQBbq2n67a8etKzcm3Ovh-IySYeE0vbQ&oe=69DC51E9&_nc_sid=6d62aa",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT14.966666S\" FBManifestTimestamp=\"1775663906\" FBManifestIdentifier=\"FsTss50NGA9yMmF2MS1yMWdlbjJ2cDkZxrLYxczFnJ0DhsjEzqvwvAPi8aaX2bzCA5KgnMWa5YIE2qnIh+zZtATk77TF4sGBBZaA74i904kFhpfXovmUkwXQlJnHsO+4BfTFw+jEkPAFyLi74Mu43AnY+NKh+sbtXiIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT14.966666S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:77.2\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"908686982166041v\" bandwidth=\"265179\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"496107\" FBPlaybackResolutionMos=\"0:100,360:55.7,480:53.3,720:52.3,1080:52.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.1,480:85.8,720:79.4,1080:72.8\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPEdLRV8Qg-mV0FjsC2JSFHXcWCWfDdFTOZtWXSsK0AMx2Fp1kUsBh9ALn-nLFdPxJilteoz6yCc2DW2Y7zJC5xW4_Umfk5Y8pxb3g.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=I6XEl-VGPIIQ7kNvwFb595D&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MjY1MTc5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3acXWe4tYaTFc6cWkECV2OovveSQDxLO4UljUA2dXbnQ&amp;oe=69DC6837</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-9169\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-95732\" FBFirstSegmentRange=\"894-136979\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"136980-352813\" FBPrefetchSegmentRange=\"894-136979\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1241792627935853v\" bandwidth=\"369172\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"690661\" FBPlaybackResolutionMos=\"0:100,360:62,480:59.1,720:57.6,1080:57.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:92.2,480:89.4,720:83.5,1080:76.9\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOK4MCv9wTeo4cp3J0NrcXB0pOXxUaLPsQP7Mb_a-sDh3vZsbf6CnbaeM8yftUTdBNUTTiG6W7_9xwNrKMHf4gZ3WS476ggpYFy_Pw.mp4?_nc_cat=101&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=qdIDoY-SWyUQ7kNvwE-iipi&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MzY5MTcyLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3LN-LgPWrEFtTYRel1dXoLic8jkudvV_SHL9I4hiwD2w&amp;oe=69DC38CA</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-10940\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-130000\" FBFirstSegmentRange=\"894-190687\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"190688-492456\" FBPrefetchSegmentRange=\"894-190687\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1132036682385417v\" bandwidth=\"532108\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"995486\" FBPlaybackResolutionMos=\"0:100,360:68.8,480:66,720:64,1080:62.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.3,480:92.3,720:87.4,1080:81.2\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNX0SDcB5CJfFSfbkJhhKtOeRdL39vhAIJWmcLBUR-607ScAwzgyGLesN3cYwYB0dkZP6LD7yZ_bBknYdVqOFBw4XtMeHTENG6bwqA.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=3TObqLwn46EQ7kNvwGgHDZf&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6NTMyMTA4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0XLJUat8lwh7eN5W1tON9uz5G7Qqm31If8fUpXFUk9Tw&amp;oe=69DC3261</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-12940\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-178330\" FBFirstSegmentRange=\"894-269841\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"269842-710966\" FBPrefetchSegmentRange=\"894-269841\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1653949602492794v\" bandwidth=\"677001\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"1266557\" FBPlaybackResolutionMos=\"0:100,360:72.8,480:70.1,720:68.1,1080:66.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.7,480:94.1,720:89.9,1080:84\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOgbA6pnHF3YvHHuG2_E1qGBuyxVjhVdKgLQ_7Wl443FJTW9aD61h22ERw5KaVpShgmGpmQVdnCQVtBV1YG-A8gLEj-TjP_STA8crU.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=4o7ProzvHfAQ7kNvwHcJh32&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6Njc3MDAxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2daVVwr_R6uWRRWw6IKG2yQYNLkFhMXDO8q3PocdDINA&amp;oe=69DC60B6</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-14814\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-221178\" FBFirstSegmentRange=\"894-341699\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"341700-905735\" FBPrefetchSegmentRange=\"894-341699\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1428600218574859v\" bandwidth=\"905429\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"1693908\" FBPlaybackResolutionMos=\"0:100,360:76.6,480:74.2,720:72.1,1080:69.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.7,480:95.6,720:92.1,1080:86.9\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO43VAoDNyEwD0gnD011QIR57OsOQPof_SXTcf3mZ9XfmQGigKoDnXI3NiG89OMic2zPi3K2p3ZbVjkUg24-5CSuRjnNrmc3OffVis.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=p51bWQpFGYAQ7kNvwEofx8U&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6OTA1NDI5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0KYCdcOoKbZbmA2BUZh1zvJAIXxuy6rpVdSJ639eWvQw&amp;oe=69DC3BA3</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-17073\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-290089\" FBFirstSegmentRange=\"894-453533\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"453534-1210424\" FBPrefetchSegmentRange=\"894-453533\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"978296324526595v\" bandwidth=\"1152920\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"2156923\" FBPlaybackResolutionMos=\"0:100,360:79.9,480:76.9,720:74.8,1080:72.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.3,480:96.4,720:93.6,1080:88.9\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOVB5Kc6aM8mu8Li9VLlM9ApD0cjV3M1BRo5Uyii_gm5iuTEqe4IeK_IUV4d9p9NxDS8jZOaZXhLkUL41jv5xR7uyXbgVm3RWDJJ9o.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=SmDCyv_0UxUQ7kNvwG8bTzA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTE1MjkyMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2SxVMAGodhyl_Pq_4416ZeLA3deXqZsiOVVxuMKpY5ag&amp;oe=69DC3D39</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-19379\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-367092\" FBFirstSegmentRange=\"894-577222\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"577223-1543510\" FBPrefetchSegmentRange=\"894-577222\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1449516199503299v\" bandwidth=\"1575510\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"2947518\" FBPlaybackResolutionMos=\"0:100,360:84.2,480:81.2,720:78.3,1080:75.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.9,480:97.3,720:95.1,1080:91.3\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNxPDoQ_wyCxk6lHcIqjp84gnkSj9OCYJGF4C8CSLjVzw2TWrbdhPQA3_PckVqMhls_MihJCV56VwCzpcZM8Z0uuMDDBkEzzUXvVkg.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=FPvv-l2wOG4Q7kNvwHcGB3x&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTU3NTUxMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af06_INk5IPLV6w1PpYAsr7YonehBWYGPpvt-6dV7BN0Ew&amp;oe=69DC4B17</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-22720\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-496903\" FBFirstSegmentRange=\"894-793713\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"793714-2112688\" FBPrefetchSegmentRange=\"894-793713\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1532433668449576v\" bandwidth=\"2186629\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"4090819\" FBPlaybackResolutionMos=\"0:100,360:88.1,480:85.9,720:83.4,1080:81.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.68,480:98.19,720:96.7,1080:95\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN6RmRMHznY-seUMFz-_BsmwLVCxBix3Ul4d8ofRkpkS6Edx8PsotHn-EYb5G-E7V6aCz48kJo4BRGi8BiZmEeekXC-i77ftV7u68Q.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=zt3Z6L8DtZ8Q7kNvwHKctMV&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MjE4NjYyOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0-h52J6BnDQyeCrZ3QHkxZ9OVQsTcav1-eefZlkZdchQ&amp;oe=69DC40DB</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-30581\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-694803\" FBFirstSegmentRange=\"894-1101978\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"1101979-2910294\" FBPrefetchSegmentRange=\"894-1101978\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1410703824428018a\" bandwidth=\"40362\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40362\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"76354\" FBPaqMos=\"82.73\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMxcH2hISXNZ91TkD2keJEeiRTE8E4iFePwl_kPbGGrBcOEZ8g-a3QQapQd_toTe9k5jJTNEwixlc-9I5zexvXJOkY5Fi81c_ixTAw.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=5FO01GOWF0AQ7kNvwEiapxb&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NDQ4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo0MDg1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1RWh8DWU2F_atuEBsweCK0cD4YJfVczieD30ye52Un6w&amp;oe=69DC40D1</BaseURL><SegmentBase indexRange=\"837-916\" timescale=\"44100\" FBMinimumPrefetchRange=\"917-2089\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"917-13996\" FBFirstSegmentRange=\"917-26512\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"26513-52895\" FBPrefetchSegmentRange=\"917-26512\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2736557170060836a\" bandwidth=\"66440\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66440\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"125095\" FBPaqMos=\"87.25\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQP28qPvRVBI5zMazKMQVKgBTg7Vls9diXfzm0pxbtBgNtXvoh3Bi5MdL3CZkQH_6G6-HpJCmOdgCIWnIAdERQLyvKT5xE8LXDKqwA8.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=D7LAIRQr7qQQ7kNvwEbEZfz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NDQ4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo2NjkzMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af03wPFH6kXeyJntgwlXd8KZtKgZ2XJ75fODwbdB7lOOKg&amp;oe=69DC5DCC</BaseURL><SegmentBase indexRange=\"838-917\" timescale=\"44100\" FBMinimumPrefetchRange=\"918-2370\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-20041\" FBFirstSegmentRange=\"918-41531\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"41532-87019\" FBPrefetchSegmentRange=\"918-41531\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"990603226963057a\" bandwidth=\"96134\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"96134\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"180588\" FBPaqMos=\"87.47\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNllB_p_hIiQU0KpnFWbDRq00a9cpozLia1JN0ix0Co_VvEjqzewofMJPLuF1VBW-pDdLOJti3SciepQ3eXrs4ASyHIWZgv8-b4oOk.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=0hhVFKjfdqoQ7kNvwGgBKXc&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NDQ4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo5NjYyMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1vHUZWsNGVU5V07ySMZ5qYZn9VBiZ9INihyFe_fSL-jw&amp;oe=69DC3678</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2424\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-31618\" FBFirstSegmentRange=\"913-61168\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"61169-123895\" FBPrefetchSegmentRange=\"913-61168\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"26699560346345004a\" bandwidth=\"127521\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"127521\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"239252\" FBPaqMos=\"91.40\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrqxnwvvUz2cFOGQqO4eeFerlCA3S0lVY9tkqCmCFI2vcxpuzK5I7Zet748fTdzhQwP4UPs6Np6skG8cOpgBnXBh1ZV2zrfv7pvJY.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=slPnjjf3pdgQ7kNvwFtgaEM&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NDQ4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjoxMjgwMDgsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3R64ZQ0KdZrSoGEgMlwQBEQulG1fqCMCwT9Ya-nuavOw&amp;oe=69DC4F89</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2594\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-42572\" FBFirstSegmentRange=\"913-83723\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"83724-167696\" FBPrefetchSegmentRange=\"913-83723\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "number_of_qualities": 8,
        "video_versions": [
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 101,
            "url": "https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwFbMFq8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2pb-mLyIubm1oevYR1xd43hVMmg7GcEUs_NhyUCz20eg&oe=69D83FDE",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 102,
            "url": "https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwFbMFq8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2pb-mLyIubm1oevYR1xd43hVMmg7GcEUs_NhyUCz20eg&oe=69D83FDE",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 103,
            "url": "https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwFbMFq8&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2pb-mLyIubm1oevYR1xd43hVMmg7GcEUs_NhyUCz20eg&oe=69D83FDE",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 14.965999603271484,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=vY0PvLetHQgQ7kNvwF1moMq&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1usXKurUpjyYwbmgvl16f7fwtO2I7lIsGCG0VkD5GfkA&oe=69DC58F0&_nc_sid=6d62aa",
              "is_unpublished": false,
              "follower_count": 34037452,
              "friendship_status": {
                "following": false
              }
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/662308336_1449496010284799_6982950920110364679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODA0MTY3Mjg5NDEyOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_t3hmPz1AKsQ7kNvwHAq4WW&_nc_oc=Adr7wmncWkRsn2nFk4_x19oHyRQ73Oy-ZoiDr-ogme1pZPQBk_HI-SV7NXmL88djzNQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_ss=7a3ba&oh=00_Af0BxlIl3rB0p6MZrFgG6AgL94t0Wg-SueSQzcqc4c3mpw&oe=69DC3DF4",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/662308336_1449496010284799_6982950920110364679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODA0MTY3Mjg5NDEyOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_t3hmPz1AKsQ7kNvwHAq4WW&_nc_oc=Adr7wmncWkRsn2nFk4_x19oHyRQ73Oy-ZoiDr-ogme1pZPQBk_HI-SV7NXmL88djzNQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_ss=7a3ba&oh=00_Af0BxlIl3rB0p6MZrFgG6AgL94t0Wg-SueSQzcqc4c3mpw&oe=69DC3DF4",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 1080,
        "original_height": 1920,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMWZjMWUwMGRmMTYwNDk3NjhlYjU5ZmQ4ZDc4ZjQ1Y2MzODcwODI4MDQxNjcyODk0MTI5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwNjczMHwzODcwODI4MDQxNjcyODk0MTI5fDM3NjAyMDk3MDE0fDZkODMyNGZmMjY5ZmMxM2Q5NzdmMDgyYWFlMzk4MmM3MzE1MTkyODE0Nzc2ODNjMzA4MTAyNmYxMjQ0MjNkNmQifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658675,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658676503732,
        "code": "DW38ZhqiKax",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "1517189826474103",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=vY0PvLetHQgQ7kNvwF1moMq&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1usXKurUpjyYwbmgvl16f7fwtO2I7lIsGCG0VkD5GfkA&oe=69DC58F0&_nc_sid=6d62aa"
            }
          }
        ]
      },
      {
        "strong_id__": "3870828324352170239_787132",
        "id": "3870828324352170239_787132",
        "expiring_at": 1775745104,
        "pk": 3870828324352170239,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18358102888233883,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODMyNDM1MjE3MDIzOQ==.3",
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
          "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=XbeNvhLXv28Q7kNvwHiwpg4&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0eKNY7n-V0g-XQBbq2n67a8etKzcm3Ovh-IySYeE0vbQ&oe=69DC51E9&_nc_sid=6d62aa",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT14.966666S\" FBManifestTimestamp=\"1775663906\" FBManifestIdentifier=\"FsTss50NGA9yMmF2MS1yMWdlbjJ2cDkZxpz04ayF4M4CxMjkl4jUrwOEsZylg6S2A9K2lOWmsMIEtPe1tee9xwSin+PerfqGBcSVscGDjuQF7oX037Djjgac95bNmbaRBqqJ3MCjmNgGrryHyOndjwz47JfzwaK6DiIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT14.966666S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:79.4\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1882780989096533v\" bandwidth=\"145319\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"271869\" FBPlaybackResolutionMos=\"0:100,360:52,480:49.4,720:47.7,1080:47.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:88.9,480:86.1,720:79.9,1080:73.8\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNWknCI1ypaYG-PXyS_wLsG6LKBhbZLdEGPEOR3_SEHVD3_orSekBEDEWwgZgI15D4OxivyDUDmsDQcFQabSsUBVtvolD1UrT71tnE.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=M0yRHnvtTrAQ7kNvwHdVL-I&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTQ1MzE5LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2e7CXcJQ7P0ZThgN0cQTeeb6jhx-73Q3_HaSjkgDvVfg&amp;oe=69DC4945</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-4354\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-45240\" FBFirstSegmentRange=\"894-56025\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"56026-209121\" FBPrefetchSegmentRange=\"894-56025\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1721343535907191v\" bandwidth=\"319307\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"597371\" FBPlaybackResolutionMos=\"0:100,360:66.9,480:63.7,720:61,1080:59\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.8,480:92.9,720:88.2,1080:82\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPdH_AFP98LkXa2wkHXxcxTJobGMKjWftITKzTvlfP91-ZDY0R7JEzM_9k7zGXQodU8pWozLC4l_64Sakv-Gnv8IOX7cub7HeUGxFk.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=O2DmzM37FAkQ7kNvwFufMQC&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MzE5MzA3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af28hh2T5I6RctH3TrTuS8b0foHjgwgkq9XSEhNKI5xeFA&amp;oe=69DC40DF</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-6202\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-82477\" FBFirstSegmentRange=\"894-106945\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"106946-455109\" FBPrefetchSegmentRange=\"894-106945\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4068785983257404v\" bandwidth=\"452141\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"845881\" FBPlaybackResolutionMos=\"0:100,360:73.1,480:70,720:67.1,1080:64.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.5,480:95.2,720:91.1,1080:85.4\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQO9c2mnXEEvVVX1glHmNMJLj_qfaBuKAxFLTS2mwV7jKynqUv0iwgRU0lJ5WrnMA5ull18DKLblr8zrUqqhYOn-rtkDg3nwn1OnUNw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=COuRQrKjJwUQ7kNvwF5JIrq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6NDUyMTQxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ndSdRXTvoF_u6kBoaOQoEpvu0qiwVq8MAW_S2eB4rUQ&amp;oe=69DC6905</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-7076\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-108062\" FBFirstSegmentRange=\"894-143859\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"143860-640795\" FBPrefetchSegmentRange=\"894-143859\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1727164404915662v\" bandwidth=\"606228\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"1134153\" FBPlaybackResolutionMos=\"0:100,360:76.9,480:74.1,720:71.2,1080:67.9\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.4,480:96.5,720:93.1,1080:87.8\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPW_OJCyqT5z0M_QKclp1LhPFo2Go4ll2epvEaVDWHgRfYi648haV8aHeyWvl9aCFP_4m6l_P1P1_OGCdAC41FgY5ciInpZLtAhpa8.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=nySn0XfBGwYQ7kNvwG2fBfn&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6NjA2MjI4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1g8R3Z_N4GTlVyAr3bqJrJRnPZln0dvdvvPrfjudzpTw&amp;oe=69DC5EBE</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-8079\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-135020\" FBFirstSegmentRange=\"894-185596\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"185597-859203\" FBPrefetchSegmentRange=\"894-185596\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"3412296965615383v\" bandwidth=\"824607\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"1542703\" FBPlaybackResolutionMos=\"0:100,360:81.5,480:77.8,720:75.1,1080:71.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.21,480:97.6,720:95,1080:90.3\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNhIDqgJko3lkkIF6XJjCSOtN-pu4FkyEGNPzkdlrd2AwKKQRv3NyWKimiRXKVDeVQyDFiJJajPp7dcbdwCFFjKa1ZRl6016vRcDbg.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=RhnTkxZoE1IQ7kNvwE_8AwD&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6ODI0NjA3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2nu2JZrQh6CipsnlhPGmg5JsKtkGX9YpMaIYTy8gbMdg&amp;oe=69DC5127</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-9557\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-172334\" FBFirstSegmentRange=\"894-246644\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"246645-1164756\" FBPrefetchSegmentRange=\"894-246644\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1283092410449370v\" bandwidth=\"1119959\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"2095257\" FBPlaybackResolutionMos=\"0:100,360:85.4,480:82.2,720:78.7,1080:74.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.73,480:98.44,720:96.3,1080:92.3\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQO7CZlflLE91FnGaFUJNIkrt-Q-NN094ID5mUak0hZaZ2snDygRsT3whLSCsJvRMkGNPYTS1TTAFLZADHpXVxzFW55D66AK-LgXJaY.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=B2KfqnwTUEIQ7kNvwFBI8wE&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTExOTk1OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3KfABCBGSWxvdlvdnj1Q-pKVtqoXkq0RG-AKnB4q-0MQ&amp;oe=69DC36E0</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-10807\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-221319\" FBFirstSegmentRange=\"894-331040\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"331041-1581215\" FBPrefetchSegmentRange=\"894-331040\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"736123752824078v\" bandwidth=\"1856572\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"3473338\" FBPlaybackResolutionMos=\"0:100,360:90.3,480:87.8,720:85.1,1080:79.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.04,480:98.91,720:97.7,1080:94.5\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMEZiCpPF4aUz4-n6w_k6R_t0gLW2EwY_YdZBYiXbiUt7Rn-sL4a4ebO9jk0uZwSED6lfrkqxLmsqxIRWwZV40A0tw0V_POiwWAJp8.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=vetcFinAcrMQ7kNvwEI8lYW&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTg1NjU3MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2UYYygzlG7urbpJplGBH86f6a1znc8jjFix1xlKU14wg&amp;oe=69DC4E08</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-13102\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-351398\" FBFirstSegmentRange=\"894-569372\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"569373-2634692\" FBPrefetchSegmentRange=\"894-569372\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"949223230837282v\" bandwidth=\"2589184\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"4843932\" FBPlaybackResolutionMos=\"0:100,360:93.2,480:91.5,720:89.4,1080:87.8\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.295,480:99.176,720:98.54,1080:97.6\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPt8nAb0J7vwiIB3nfHOezje4sDxa5zRKuA5LwZjmuE5JpNMuLguNaa4F16q93_34gzoyXZESEzbBmub2rc5lTAjJ9N6-FvZb7eDhs.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=SUa6KCUNCg0Q7kNvwE9JE_n&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MjU4OTE4NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0J87nP5JfpHf3sd5piyfm9sKBj7OUSE_KGHwmFVsJJKA&amp;oe=69DC42FB</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-17236\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-532416\" FBFirstSegmentRange=\"894-845642\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"845643-3635368\" FBPrefetchSegmentRange=\"894-845642\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1627518198490466a\" bandwidth=\"40415\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40415\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"76453\" FBPaqMos=\"77.63\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOw8xb4KIdP1Gz455yZSZ0czsbJmrj6sTVclaJHcXxqhma7TP7e0KJvamRE6uTCP1lKa5dctb4JRTrsuVhzX9JGzBGK6MX8eauR5zQ.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=zPQHb0d_33cQ7kNvwG1NXfz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NjU4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo0MDkwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2eyjT4xFXeRqgfoZngWNQpbSmfRy6TLEEzLr2dDDUzQQ&amp;oe=69DC3607</BaseURL><SegmentBase indexRange=\"837-916\" timescale=\"44100\" FBMinimumPrefetchRange=\"917-2080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"917-13553\" FBFirstSegmentRange=\"917-25411\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"25412-51467\" FBPrefetchSegmentRange=\"917-25411\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1271865281777065a\" bandwidth=\"69062\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"69062\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"129996\" FBPaqMos=\"82.40\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrGDBtMbIemQ_K3v-pMEAE1l0wBAchtWOUJpQj5eWYkcgfQFgvuH88_RzjeQ5zD1qp06OdkC2oPTv8_65UU1HvWwrPvzBP0czhKHM.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=OdRytjrWw5sQ7kNvwEAKdt3&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NjU4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo2OTU1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3dkUDFCwD_4IsCou0Ez0p756DwaOM_uyV16p1JincPGQ&amp;oe=69DC5CB5</BaseURL><SegmentBase indexRange=\"838-917\" timescale=\"44100\" FBMinimumPrefetchRange=\"918-2657\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-23725\" FBFirstSegmentRange=\"918-44783\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"44784-89336\" FBPrefetchSegmentRange=\"918-44783\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"963791102905410a\" bandwidth=\"96207\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"96207\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"180726\" FBPaqMos=\"81.66\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9Jl5dcq9adj_7hJaV25Ki8cWJm9dIRkvSY9ndE4Z33Wnuff2Zt-B4RArU637hAOCr6ahQCbAgELx_aawwqcqMzPmYIk7bwGjoaRw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=uAcuExAmECUQ7kNvwGesVb6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NjU4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo5NjY5NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af21OsG68cEwXubcbDYWWuShLRwkGkzKYZSbvP8LE2uDog&amp;oe=69DC6159</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2475\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-31455\" FBFirstSegmentRange=\"913-59788\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"59789-122039\" FBPrefetchSegmentRange=\"913-59788\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1422671106303953a\" bandwidth=\"131438\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"131438\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"246573\" FBPaqMos=\"88.22\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOZBhzCwpZKChWYvJFkx9fKg-FxfQ5rtMBpHqk2XwyoracwAxZHTYipp89qXJ6L71cDaDUon7YraowFZlMhsyljNKDfdINVsKcvv38.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=fR0AHV-x07IQ7kNvwFuz7i0&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NjU4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjoxMzE5MjYsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0-F1WieMpSgraIVEhaUAKArOCA6Aas1ijvxf5GE1wDUA&amp;oe=69DC662E</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2638\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-41369\" FBFirstSegmentRange=\"913-80242\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"80243-165238\" FBPrefetchSegmentRange=\"913-80242\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "number_of_qualities": 8,
        "video_versions": [
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 101,
            "url": "https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwE9YgeI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af23ti2NV3Vt5toqn-ttOrC9fvdY-z6n32aXNnTPWlujZQ&oe=69D85281",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 102,
            "url": "https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwE9YgeI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af23ti2NV3Vt5toqn-ttOrC9fvdY-z6n32aXNnTPWlujZQ&oe=69D85281",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 103,
            "url": "https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwE9YgeI&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af23ti2NV3Vt5toqn-ttOrC9fvdY-z6n32aXNnTPWlujZQ&oe=69D85281",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 14.965999603271484,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=vY0PvLetHQgQ7kNvwF1moMq&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1usXKurUpjyYwbmgvl16f7fwtO2I7lIsGCG0VkD5GfkA&oe=69DC58F0&_nc_sid=6d62aa",
              "is_unpublished": false,
              "follower_count": 34037452,
              "friendship_status": {
                "following": false
              }
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/657255699_1385632013371495_7666726418949229423_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODMyNDM1MjE3MDIzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m7SPdY3D7l0Q7kNvwF9f5wT&_nc_oc=Adqq7F8t0x8c51LbDDwDeVEjtDRXC8NanHDuguAIowmb1vVK8AkMAQVmLZ9Vm4vYjec&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_ss=7a3ba&oh=00_Af0ZnHpfibXwc7HvXHNCpPCrnEXblEbHEn630noIiNzfiA&oe=69DC54C2",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/657255699_1385632013371495_7666726418949229423_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODMyNDM1MjE3MDIzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m7SPdY3D7l0Q7kNvwF9f5wT&_nc_oc=Adqq7F8t0x8c51LbDDwDeVEjtDRXC8NanHDuguAIowmb1vVK8AkMAQVmLZ9Vm4vYjec&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_ss=7a3ba&oh=00_Af0ZnHpfibXwc7HvXHNCpPCrnEXblEbHEn630noIiNzfiA&oe=69DC54C2",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 1080,
        "original_height": 1920,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMWZjMWUwMGRmMTYwNDk3NjhlYjU5ZmQ4ZDc4ZjQ1Y2MzODcwODI4MzI0MzUyMTcwMjM5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwNjczMHwzODcwODI4MzI0MzUyMTcwMjM5fDM3NjAyMDk3MDE0fDQzYmUxZTM1YjliY2QxNThhN2QwNTJmZDEyMDE1Mzc3OWIzMDg3NzM5ZGZmZTNjOWI4OWRlYWNhMDY2ZGNjMzIifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658704,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658704503734,
        "code": "DW38do7iBj_",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "968400145722533",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=vY0PvLetHQgQ7kNvwF1moMq&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1usXKurUpjyYwbmgvl16f7fwtO2I7lIsGCG0VkD5GfkA&oe=69DC58F0&_nc_sid=6d62aa"
            }
          }
        ]
      },
      {
        "strong_id__": "3870828687528621445_787132",
        "id": "3870828687528621445_787132",
        "expiring_at": 1775745136,
        "pk": 3870828687528621445,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18519178861076290,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODY4NzUyODYyMTQ0NQ==.3",
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
          "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=XbeNvhLXv28Q7kNvwHiwpg4&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af0eKNY7n-V0g-XQBbq2n67a8etKzcm3Ovh-IySYeE0vbQ&oe=69DC51E9&_nc_sid=6d62aa",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT13.733334S\" FBManifestTimestamp=\"1775663906\" FBManifestIdentifier=\"FsTss50NGA9yMmF2MS1yMWdlbjJ2cDkZxuar2ovy/PMC7Mvu8YLuiwOqhsjYh/2QA+CJ8YKs45MD0Oyr4NfmrQPA+83nhuLRBPy/udXj5a0FzKCp/c3k4AW2yKW+hubxBdiK4dTrgMYH6vLgza2nygfQpeaU7tDUDyIYJmRhc2hfdW5pZmllZF9wcmVtaXVtX3hoZTEyMzRfaWJyX2F1ZGlvIiwZGAVsaWdodAAWABQAEhQCAA==\"><Period id=\"0\" duration=\"PT13.733334S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.1\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:MatrixCoefficients\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:ColourPrimaries\" value=\"1\"/><SupplementalProperty schemeIdUri=\"urn:mpeg:mpegB:cicp:TransferCharacteristics\" value=\"1\"/><Representation id=\"1657617728713243v\" bandwidth=\"202630\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q20\" FBContentLength=\"347849\" FBPlaybackResolutionMos=\"0:100,360:59.9,480:57.1,720:55.8,1080:55.7\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.9,480:87,720:82.9,1080:78.1\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"240p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQPrECMfvgDPuYk-kqwzLkJg7IEbR7XW6eBWRaH-ZUbD9prnYyQqPWWBT6P_cIwRi2b2c4xQquRFvM99Iry9I4AnQWOmONGpzZ-5f8Q.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=ztL7V5fumWsQ7kNvwGIsa9o&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EyMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6MjAyNjMwLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af2dUEl1fd8snix0zPJlJ5fIedn7Ex6K9Nt72hHJHSAijw&amp;oe=69DC35B1</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-5181\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-79379\" FBFirstSegmentRange=\"894-103502\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"103503-238273\" FBPrefetchSegmentRange=\"894-103502\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"887913087640176v\" bandwidth=\"292615\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q30\" FBContentLength=\"502323\" FBPlaybackResolutionMos=\"0:100,360:67.2,480:64.2,720:62.3,1080:61.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:93.3,480:91,720:87.1,1080:82.1\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"270p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNXVFl5ZB91TClIlI4hn3e4TUZWrhdE2bCn8ipMe4H18esT2GmV-B4f2mR8dDOnm0cS2oKSCkJdTNqbdNcNkO2paiMtBNVQs8WnxiE.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=kK1LG8LU-gsQ7kNvwGv0Aaq&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3EzMCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6MjkyNjE1LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af0MvfCfDf6osPsmbANAe4ZhReEBv3UsqDdHR-7EhfrUjA&amp;oe=69DC413D</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-6126\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-110253\" FBFirstSegmentRange=\"894-144510\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"144511-334190\" FBPrefetchSegmentRange=\"894-144510\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"870504359383798v\" bandwidth=\"410168\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q40\" FBContentLength=\"704122\" FBPlaybackResolutionMos=\"0:100,360:72.5,480:69.6,720:67.4,1080:65.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.4,480:93.7,720:90.4,1080:85.4\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOR7eQ75CgB0Z_X7VYeY4bu4a43L-J6afuMk7crsWAnafcOSlTaREW5Y8PvG4xeTxQqi64JR70GoCpoQFnF3qMgbjV_Ztiqajk0b1Y.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=9oPzwi5qTwgQ7kNvwHstFhR&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E0MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6NDEwMTY4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af1550e1fAsReGeR5NjAI5fAMWqFao9r_oCJFxrSRWDO0Q&amp;oe=69DC4A53</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-7308\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-148288\" FBFirstSegmentRange=\"894-197792\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"197793-457462\" FBPrefetchSegmentRange=\"894-197792\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"4408231779420520v\" bandwidth=\"557688\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q50\" FBContentLength=\"957366\" FBPlaybackResolutionMos=\"0:100,360:76.8,480:74.1,720:71.8,1080:69.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.9,480:95.6,720:92.9,1080:88.1\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"480p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQN4MZhPSgKct1GPMJNwALlYSnCCvL8ShZSTqdPcotyvufs2tZ9P4dK20PtlgXNaA-x1zFc0OrTeVvi4CWOsb4XulwLdOgakljfEI_A.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=0xEhXfROGDAQ7kNvwFH6UVk&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E1MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6NTU3Njg4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af2YLqfHA0VjfwGUZQJluon0neydrlsxQqkibeS3XrTAew&amp;oe=69DC5185</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-8184\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-192893\" FBFirstSegmentRange=\"894-261338\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"261339-605277\" FBPrefetchSegmentRange=\"894-261338\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"1620209569179686v\" bandwidth=\"756714\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q60\" FBContentLength=\"1299027\" FBPlaybackResolutionMos=\"0:100,360:80.9,480:77.5,720:75.4,1080:72.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.8,480:96.8,720:94.7,1080:90.3\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQOldUf8mrXTFLvdJHCdyuRxszok3dTvWWXmJDE_5_FjwcSy6NAy--g-dvfQiXBHDtsg_oAuNiXZrhYEp1CxJg1fZ-bOPzpuRUovYNI.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=sFjtmcb_dKIQ7kNvwEpKcmy&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E2MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6NzU2NzE0LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3s78iuevNBDOPnLZSufOIQ09jRSmJhyQhofoOR6qRpfQ&amp;oe=69DC4CC1</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-9215\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-252101\" FBFirstSegmentRange=\"894-348825\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"348826-800772\" FBPrefetchSegmentRange=\"894-348825\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"817983244684019v\" bandwidth=\"1033682\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q70\" FBContentLength=\"1774489\" FBPlaybackResolutionMos=\"0:100,360:84.3,480:81.3,720:78.3,1080:75.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.42,480:97.8,720:96.1,1080:92.4\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"640p\"><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQNnTcBITUbYK2AZXW9SsH7pSYffx-Lv6jhU5CPwKk0N88zUv6BwN5cUl7HZ285vdjwpqGtL0rRTCfcwiQEvphhZvz_gEzoTUuYHGzc.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=xYTTbBJxwFEQ7kNvwFC7R2l&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E3MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6MTAzMzY4MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Rve2jjkR8oJukCxizZP7MRFqsMUnAI73UIHVvGeJnuA&amp;oe=69DC4611</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-10457\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-326818\" FBFirstSegmentRange=\"894-463769\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"463770-1067779\" FBPrefetchSegmentRange=\"894-463769\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"881757818257813v\" bandwidth=\"1331794\" codecs=\"av01.0.05M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q80\" FBContentLength=\"2286247\" FBPlaybackResolutionMos=\"0:100,360:86.9,480:84.2,720:81.5,1080:77.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:98.7,480:98.26,720:96.9,1080:93.6\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQMw6DiO_PArO4vRXeL1d-VQex3a4mc5PtAmKlb2aCvDWgd8vO5KimezrIp7u9xuqtKSwspg_6vxZJwvqjjt5aA1uK_C9D7hnGtb60U.mp4?_nc_cat=108&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=Wg5Bo878K_IQ7kNvwHtKNM4&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E4MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6MTMzMTc5NCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af0ZYUACvhI53flxwTPBRzLxp-qTWCGV8lWxBcJ-vWz5fg&amp;oe=69DC3801</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-11589\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-408580\" FBFirstSegmentRange=\"894-589790\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"589791-1350142\" FBPrefetchSegmentRange=\"894-589790\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation><Representation id=\"945145101253416v\" bandwidth=\"1880381\" codecs=\"av01.0.08M.08.0.111.01.01.01.0\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_r2av1-r1gen2vp9_q90\" FBContentLength=\"3227988\" FBPlaybackResolutionMos=\"0:100,360:90.1,480:88,720:85.9,1080:84.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:99.171,480:98.85,720:98.09,1080:96.9\" width=\"1080\" height=\"1920\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"1080p\"><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOdqC63HNKD9RDZxpZdrCVuCwQcIVPP0b30u2_DgSL0unLR6K3GoGaCuFgFYZ0yPDN6e4N5vW_pCW8Ha1kGsMQFEVwFpfgEfyPGCcY.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=aCo1XVa2RJoQ7kNvwGH3-8X&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfcjJhdjEtcjFnZW4ydnA5X3E5MCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6MTg4MDM4MSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af366T5ShmVtfQ1ZJ-lSefkcVElCzcrtDGm_aHcacWus7w&amp;oe=69DC487C</BaseURL><SegmentBase indexRange=\"826-893\" timescale=\"15360\" FBMinimumPrefetchRange=\"894-16043\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"894-587270\" FBFirstSegmentRange=\"894-844575\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"844576-1906521\" FBPrefetchSegmentRange=\"894-844575\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-825\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1508079473995774a\" bandwidth=\"41322\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"41322\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"71780\" FBPaqMos=\"80.37\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBvWzDIb5LTqqPF7OcJqQEUdH2wH-24goKguI3Z79E4jzJ2CzNaVogECA0Vey59AOs4HMbFjQ6o5HpW19a1D0WHb4W8DP3KPHuwos.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=ilIxrYEJjJEQ7kNvwHU72Uu&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ5MDMwMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjEzLCJiaXRyYXRlIjo0MTg0OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2lyRDU08_lVmYy4HX9to-GPoPhPWoKKPja36PBHWulCA&amp;oe=69DC6934</BaseURL><SegmentBase indexRange=\"837-904\" timescale=\"44100\" FBMinimumPrefetchRange=\"905-2078\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"905-12977\" FBFirstSegmentRange=\"905-23904\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"23905-50678\" FBPrefetchSegmentRange=\"905-23904\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2124270915035820a\" bandwidth=\"69374\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"69374\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"119895\" FBPaqMos=\"85.87\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMVFUOJryi5KiqVpJ8Km_Umnvr7v7AOQPPj5J035w5DhUzcmYB4okk8fcJxrudklw1vUAyaiuqkZ1NUPhorQnp_k1Je1QwVp1EvSRU.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=-pxJyFSpiLQQ7kNvwHAf8KA&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ5MDMwMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjEzLCJiaXRyYXRlIjo2OTkwMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1KnZli8jPXFeU9EEhBByqEpYs-BqvEgQnp4oG0b4jn2Q&amp;oe=69DC3D1F</BaseURL><SegmentBase indexRange=\"838-905\" timescale=\"44100\" FBMinimumPrefetchRange=\"906-2582\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-22430\" FBFirstSegmentRange=\"906-42573\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"42574-84991\" FBPrefetchSegmentRange=\"906-42573\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"2133728694115509a\" bandwidth=\"97230\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"97230\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"167669\" FBPaqMos=\"84.36\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMvlhSAgo1bS8WEV2uPNASauhmPHh3w7-BfVeDJBRF0N7YfHwbo8CVtEnnhbZ2rK65uf73_2Ci9fLgmng-47EOaGArql0g38YLfJMU.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc3-1.cdninstagram.com&amp;_nc_ohc=JWkeZTcmU2oQ7kNvwEQxp4V&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ5MDMwMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjEzLCJiaXRyYXRlIjo5Nzc1NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3hnsDUME9kXrUaB5Q4REJ-JShkWT02T1Qy7tejcnKi4g&amp;oe=69DC3982</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2523\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-29290\" FBFirstSegmentRange=\"901-55119\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"55120-117435\" FBPrefetchSegmentRange=\"901-55119\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation><Representation id=\"1305705331670752a\" bandwidth=\"128342\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"128342\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr4_abr_lrac_frag_5_audio\" FBContentLength=\"221032\" FBPaqMos=\"89.43\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-sjc6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNBbvXOjUCz-3aIO5NQH6C4PyQuwVJhgYgSRLruPU9h6UMehdZCCOGLBy0fGOwQ8C15d7eR8Djd8B_3bhgfKpZ1VV-SmjGNcFaxmE4.mp4?_nc_cat=1&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-sjc6-1.cdninstagram.com&amp;_nc_ohc=1SCQx3w338MQ7kNvwFqIo2x&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjRfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ5MDMwMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjEzLCJiaXRyYXRlIjoxMjg4NjcsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&amp;ccb=17-1&amp;_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0HID416GXnD1QIrR4xysxim5pB1q3YKTHduNpw8l96mA&amp;oe=69DC350A</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2656\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-36145\" FBFirstSegmentRange=\"901-67718\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"67719-153320\" FBPrefetchSegmentRange=\"901-67718\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "video_codec": "av01.0.05M.08.0.111.01.01.01.0",
        "number_of_qualities": 8,
        "video_versions": [
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 101,
            "url": "https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwEfABLz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1SHLWOD_ocDqyM4WDzIItUlgHGp_Ta5V4_lrg9EZXL2A&oe=69D85C07",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 102,
            "url": "https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwEfABLz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1SHLWOD_ocDqyM4WDzIItUlgHGp_Ta5V4_lrg9EZXL2A&oe=69D85C07",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 103,
            "url": "https://scontent-sjc3-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwEfABLz&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af1SHLWOD_ocDqyM4WDzIItUlgHGp_Ta5V4_lrg9EZXL2A&oe=69D85C07",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 13.732999801635742,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=vY0PvLetHQgQ7kNvwF1moMq&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1usXKurUpjyYwbmgvl16f7fwtO2I7lIsGCG0VkD5GfkA&oe=69DC58F0&_nc_sid=6d62aa",
              "is_unpublished": false,
              "follower_count": 34037452,
              "friendship_status": {
                "following": false
              }
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/659614888_1512637680515245_5529787493603763341_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODY4NzUyODYyMTQ0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=gitXYB93E4QQ7kNvwEIHHuK&_nc_oc=Adruftkp1ql0glVgij2skraTIFkHQtj4mkMTx27xwtl3Fy7NDxHs1I4MKIvrqKv0CUo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_ss=7a3ba&oh=00_Af1Gsd8vQpKUAk7zrjs6AtKdLDaqbkOe1HfsU7rRLezkqA&oe=69DC69B1",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.71878-15/659614888_1512637680515245_5529787493603763341_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=1&ig_cache_key=Mzg3MDgyODY4NzUyODYyMTQ0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=gitXYB93E4QQ7kNvwEIHHuK&_nc_oc=Adruftkp1ql0glVgij2skraTIFkHQtj4mkMTx27xwtl3Fy7NDxHs1I4MKIvrqKv0CUo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&_nc_ss=7a3ba&oh=00_Af1Gsd8vQpKUAk7zrjs6AtKdLDaqbkOe1HfsU7rRLezkqA&oe=69DC69B1",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 1080,
        "original_height": 1920,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMWZjMWUwMGRmMTYwNDk3NjhlYjU5ZmQ4ZDc4ZjQ1Y2MzODcwODI4Njg3NTI4NjIxNDQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwNjczMHwzODcwODI4Njg3NTI4NjIxNDQ1fDM3NjAyMDk3MDE0fDc0OTczZWQ5MDVkZmEyY2FiOGVmNzZhODBmOGVjNjEyNDZmMmMzZjdkOTU2YWQ0NjRhYjdiOWU5YWVlOWVlMmIifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658736,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658736503736,
        "code": "DW38i7KiPWF",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "983436374123185",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-sjc6-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-sjc6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gEwmLAFYPR4UQi4k0HWpKyPMwrKimMhGGK4AX9guRtt6vQXXrO-U7VEif4x2DClazw&_nc_ohc=vY0PvLetHQgQ7kNvwF1moMq&_nc_gid=YXY6NmwP-jNx4A69gk9vOQ&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af1usXKurUpjyYwbmgvl16f7fwtO2I7lIsGCG0VkD5GfkA&oe=69DC58F0&_nc_sid=6d62aa"
            }
          }
        ]
      }
    ],
    "is_nux": false,
    "has_besties_media": false,
    "media_count": 7,
    "media_ids": [
      3870828041672894129,
      3870828324352170239,
      3870828687528621445
    ],
    "has_fan_club_media": false,
    "show_fan_club_stories_teaser": false,
    "is_cacheable": true,
    "disabled_reply_types": [
      "story_remix_reply",
      "story_selfie_reply",
      "story_voice_reply"
    ],
    "is_archived": false,
    "show_expiration_tray_signal": false
  },
  "unviewable_authors_info": null,
  "status": "ok"
}
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
    "latest_reel_media": 1775659002,
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
    "expiring_at": 1775745402,
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
      "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=XbeNvhLXv28Q7kNvwFSnFJf&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1V1alqw45X3q4yGkFLoin4hdRfwoIxrypHkoKuUtcP1g&oe=69DC51E9&_nc_sid=6d62aa",
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
        "strong_id__": "3870828041672894129_787132",
        "id": "3870828041672894129_787132",
        "expiring_at": 1775745075,
        "pk": 3870828041672894129,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18311197711278628,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODA0MTY3Mjg5NDEyOQ==.3",
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
          "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=XbeNvhLXv28Q7kNvwFSnFJf&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1V1alqw45X3q4yGkFLoin4hdRfwoIxrypHkoKuUtcP1g&oe=69DC51E9&_nc_sid=6d62aa",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT15S\" FBManifestTimestamp=\"1775663908\" FBManifestIdentifier=\"Fsjss50NGBFpZ19kYXNoX2Jhc2ljX3ZwORlm4vGml9m8wgPk77TF4sGBBa67rfLRnZIFuIiswKWwwQfIuLvgy7jcCbqq19+Pu+4KIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT15S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:77.2\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"2114091015832092v\" bandwidth=\"385136\" codecs=\"vp09.00.21.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_360p\" FBContentLength=\"722130\" FBPlaybackResolutionMos=\"0:100,360:74.7,480:68.3,720:59.3,1080:49.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.2,480:83.2,720:74.6,1080:64\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPjaMYVL1MyoLQc8dCDYWBfcOoHDSsDcq6GUbPzDqhDC-MeEddKmukpFcXAMdFEzfKjURm1kHWVHdAETahyJi_0I_jSG9YiKRz_gPgHognI_Q.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=ZtQ4594KFPEQ7kNvwF2VPhF&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMzYwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6Mzg1MTM2LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1JNRPPfSIZA0McsQZNMLJvyB8jOyzXX_Xc-wR8nJijrQ&amp;oe=69DC47E9</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-16845\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-127550\" FBFirstSegmentRange=\"886-183941\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"183942-526325\" FBPrefetchSegmentRange=\"886-183941\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1447466509905623v\" bandwidth=\"1012738\" codecs=\"vp09.00.30.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_540p\" FBContentLength=\"1898884\" FBPlaybackResolutionMos=\"0:100,360:85.6,480:81.8,720:76.2,1080:70.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:95.1,480:93.8,720:90.6,1080:85.1\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMxEX5jmlfXLO2tohFkH7sizhQU88Eiytcyst2Y_i0pPJp8Gt7dwlA_mz40Lm0MxZP9zuv5Gr5A6cblDcUcWlBm1aJGpvCs7MQckOXc4Ay3FA.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=KF0izMsXHcEQ7kNvwEMH4Iv&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNTQwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTAxMjczOCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Evh4aR37BkkpsjXfzRsgGQpAZ1pnLlXufaT084BFOYw&amp;oe=69DC68E8</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-42422\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-337336\" FBFirstSegmentRange=\"886-510753\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"510754-1385248\" FBPrefetchSegmentRange=\"886-510753\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"3057658051095197v\" bandwidth=\"1716360\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_720p\" FBContentLength=\"3218175\" FBPlaybackResolutionMos=\"0:100,360:92.4,480:88.9,720:84.7,1080:77.5\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.2,480:96.2,720:94.8,1080:91.7\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQPJcX_UtZ21hxrF81YFGkpzF9Si_485icrHuF40ZJ2Qg4MTKtIpRfsysuXXHi3P3kDa6GfR5TPEG-_7EhqFu89VR4cmT7wTTLOB9Gxn91cTfQ.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=WiEB38tZ0SwQ7kNvwE8cTNL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNzIwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODQ0ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTcxNjM2MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2k2Rpw_VNvf4nHfmfx20r3Es8taQtNklXlXfu0ERhApw&amp;oe=69DC5725</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-54842\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-560654\" FBFirstSegmentRange=\"886-869089\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"869090-2338683\" FBPrefetchSegmentRange=\"886-869089\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1410703824428018a\" bandwidth=\"40362\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40362\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"76354\" FBPaqMos=\"82.73\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMxcH2hISXNZ91TkD2keJEeiRTE8E4iFePwl_kPbGGrBcOEZ8g-a3QQapQd_toTe9k5jJTNEwixlc-9I5zexvXJOkY5Fi81c_ixTAw.mp4?_nc_cat=104&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=5FO01GOWF0AQ7kNvwGYfDop&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NDQ4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo0MDg1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af18XV41eJ_yllly9sqDA-TMXnVjXhHJ7ZVEGkbU-3hC_w&amp;oe=69DC40D1</BaseURL><SegmentBase indexRange=\"837-916\" timescale=\"44100\" FBMinimumPrefetchRange=\"917-2089\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"917-13996\" FBFirstSegmentRange=\"917-26512\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"26513-52895\" FBPrefetchSegmentRange=\"917-26512\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2736557170060836a\" bandwidth=\"66440\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"66440\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"125095\" FBPaqMos=\"87.25\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQP28qPvRVBI5zMazKMQVKgBTg7Vls9diXfzm0pxbtBgNtXvoh3Bi5MdL3CZkQH_6G6-HpJCmOdgCIWnIAdERQLyvKT5xE8LXDKqwA8.mp4?_nc_cat=103&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=D7LAIRQr7qQQ7kNvwGpHCEJ&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NDQ4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo2NjkzMCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3P7AfC1-Rgn2uCJ2476bVRKyiqm1weRVfk4nRt_yYqDA&amp;oe=69DC5DCC</BaseURL><SegmentBase indexRange=\"838-917\" timescale=\"44100\" FBMinimumPrefetchRange=\"918-2370\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-20041\" FBFirstSegmentRange=\"918-41531\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"41532-87019\" FBPrefetchSegmentRange=\"918-41531\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"990603226963057a\" bandwidth=\"96134\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"96134\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"180588\" FBPaqMos=\"87.47\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQNllB_p_hIiQU0KpnFWbDRq00a9cpozLia1JN0ix0Co_VvEjqzewofMJPLuF1VBW-pDdLOJti3SciepQ3eXrs4ASyHIWZgv8-b4oOk.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=0hhVFKjfdqoQ7kNvwHehf_F&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NDQ4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo5NjYyMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1sADj7_FAkgXZVcZD_wBAOkv223BHd-_axs6pFtucpeQ&amp;oe=69DC3678</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2424\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-31618\" FBFirstSegmentRange=\"913-61168\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"61169-123895\" FBPrefetchSegmentRange=\"913-61168\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "video_codec": "vp09.00.21.08.00.01.01.01.00",
        "number_of_qualities": 3,
        "video_versions": [
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 101,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwFoaKEQ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2sS5fM62K-pSp_o8LlAaNruLUF-RN37v7RVgs4zlcKsA&oe=69D83FDE",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 102,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwFoaKEQ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2sS5fM62K-pSp_o8LlAaNruLUF-RN37v7RVgs4zlcKsA&oe=69D83FDE",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1746448,
            "height": 1280,
            "id": "26262506683371587v",
            "type": 103,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQP_XjnnrU16nGBYHrUVqKYpECTv7-t8PekyZWARS38tlxo4MyCkIRjVkkeshDoTYKafQGo0wp_wyw27L6fYDkfBNRmOkqyILGMTuDA.mp4?_nc_cat=109&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=x6_yZQeOiIsQ7kNvwFoaKEQ&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg0NDgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=64a5ba83eb5b78cb&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzc5NEE3MDU1OENDNTVBMjIzMDkxQUUyNEE0MjA5M0JFX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvNkU0RjYxNEI5Q0JDREFDQThBMjNBQTdFN0NBQzQ0OTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpbAn4b4r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af2sS5fM62K-pSp_o8LlAaNruLUF-RN37v7RVgs4zlcKsA&oe=69D83FDE",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 15.0,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=vY0PvLetHQgQ7kNvwEoq92C&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af08RhGijsLRqWdy9qrrIZBmOf_rb38m9SB9gyfZN889MA&oe=69DC58F0&_nc_sid=6d62aa",
              "is_unpublished": false,
              "follower_count": 34037452,
              "friendship_status": {
                "following": false
              }
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/662308336_1449496010284799_6982950920110364679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgyODA0MTY3Mjg5NDEyOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_t3hmPz1AKsQ7kNvwFJMHKY&_nc_oc=AdoUOKBjrlLJcre8G1BYoDvn2Bvc7jTYygZnR2b-ulrrjdBLUOkz163q38C9qsMfrcc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_ss=7a3ba&oh=00_Af0UPcwarUANo2zrS4owId9o0jB6_kHq8iqoRCUWaVEU_Q&oe=69DC3DF4",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                3902,
                7804,
                11707
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/662308336_1449496010284799_6982950920110364679_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgyODA0MTY3Mjg5NDEyOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=_t3hmPz1AKsQ7kNvwFJMHKY&_nc_oc=AdoUOKBjrlLJcre8G1BYoDvn2Bvc7jTYygZnR2b-ulrrjdBLUOkz163q38C9qsMfrcc&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_ss=7a3ba&oh=00_Af0UPcwarUANo2zrS4owId9o0jB6_kHq8iqoRCUWaVEU_Q&oe=69DC3DF4",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 720,
        "original_height": 1280,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODc5ZWNlY2VmMmM2NGU5NmE0NDM3NTBlNGU2OGNiY2IzODcwODI4MDQxNjcyODk0MTI5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwNzkyMHwzODcwODI4MDQxNjcyODk0MTI5fDMyOTQwMjU0MDYyfDQ0MzQzMDhmODJkN2YxYTNjN2MwZTE1NGM1YzNhMmI4Yzg4N2QwYmE3MTlhZjk2N2ZjNjllMzJhMzAwMjc4NjYifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658675,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658676503732,
        "code": "DW38ZhqiKax",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "1517189826474103",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=vY0PvLetHQgQ7kNvwEoq92C&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af08RhGijsLRqWdy9qrrIZBmOf_rb38m9SB9gyfZN889MA&oe=69DC58F0&_nc_sid=6d62aa"
            }
          }
        ]
      },
      {
        "strong_id__": "3870828324352170239_787132",
        "id": "3870828324352170239_787132",
        "expiring_at": 1775745104,
        "pk": 3870828324352170239,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18358102888233883,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODMyNDM1MjE3MDIzOQ==.3",
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
          "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=XbeNvhLXv28Q7kNvwFSnFJf&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1V1alqw45X3q4yGkFLoin4hdRfwoIxrypHkoKuUtcP1g&oe=69DC51E9&_nc_sid=6d62aa",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT15S\" FBManifestTimestamp=\"1775663908\" FBManifestIdentifier=\"Fsjss50NGBFpZ19kYXNoX2Jhc2ljX3ZwORlmwtPf3fTlsAOEsZylg6S2A/DCuYnf4roEyKuvqZ6UvgTStpTlprDCBMSVscGDjuQFIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT15S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:79.4\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1262587015981796v\" bandwidth=\"282281\" codecs=\"vp09.00.21.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_360p\" FBContentLength=\"529277\" FBPlaybackResolutionMos=\"0:100,360:75.2,480:69.2,720:59.7,1080:50.4\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:89.6,480:84,720:75,1080:65.2\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMSdsyu0IeNqARqDjPvrhKTez-1b7yKpuawGUEpnPMdqTeROsPgFlPBY_5N3xpud19utaJpG9RBKD2bcmNJjMr43dViGIlvKf8j8pHZKmD3Pg.mp4?_nc_cat=111&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=TDIp_OdAjX8Q7kNvwGydPWh&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMzYwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MjgyMjgxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af0dLBBZmuOlEakmVJQeZ_v29rHkoDKSHib-WUIvJ-uMKg&amp;oe=69DC36D9</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-7111\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-66394\" FBFirstSegmentRange=\"886-94381\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"94382-420705\" FBPrefetchSegmentRange=\"886-94381\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1255139643437240v\" bandwidth=\"773961\" codecs=\"vp09.00.30.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_540p\" FBContentLength=\"1451178\" FBPlaybackResolutionMos=\"0:100,360:84.7,480:81.4,720:75.6,1080:70.1\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:94.9,480:93.7,720:90.1,1080:84.8\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNgboSjU0nTZ4vBE2TZigS0tXg3fEqIyrzKI37bsngjV919DAXC7GEpRhHrrcPXBO0QhAMELADLmDunSpw-Kd8VTPpfIbRzMsBu1W-AM6nUhQ.mp4?_nc_cat=109&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=KD66HxtWZKsQ7kNvwHad56S&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNTQwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6NzczOTYxLCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af3kvOxLstTAJ-dG2MuF-xTXy2mjdhncnos8PyRHS5tgkw&amp;oe=69DC619B</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-10919\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-159063\" FBFirstSegmentRange=\"886-245011\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"245012-1109918\" FBPrefetchSegmentRange=\"886-245011\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"951728880743649v\" bandwidth=\"1329697\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_720p\" FBContentLength=\"2493182\" FBPlaybackResolutionMos=\"0:100,360:91,480:87.7,720:83.5,1080:76.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96.8,480:95.8,720:94.4,1080:91\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOnwm-7LKTlK0A55X8lx0FkaBc9ZSonED_wTYB4j__jYXfEgyPhBys3bJlLzsU2siGeFiBus4YT3F9EK4Ve47bIxLu2MmZROawhZfRjwrOFYA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=OCuISed_8UoQ7kNvwEsmAcI&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNzIwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0ODY1ODExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxNCwiYml0cmF0ZSI6MTMyOTY5NywidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_zt=28&amp;_nc_ss=7a3ba&amp;oh=00_Af1faF9gqXpmJvaS0yYig6VZd1rwpCdughnH5igHJ7B0xg&amp;oe=69DC656E</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-14484\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-272456\" FBFirstSegmentRange=\"886-433584\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"433585-1874818\" FBPrefetchSegmentRange=\"886-433584\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1627518198490466a\" bandwidth=\"40415\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"40415\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"76453\" FBPaqMos=\"77.63\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOw8xb4KIdP1Gz455yZSZ0czsbJmrj6sTVclaJHcXxqhma7TP7e0KJvamRE6uTCP1lKa5dctb4JRTrsuVhzX9JGzBGK6MX8eauR5zQ.mp4?_nc_cat=102&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=zPQHb0d_33cQ7kNvwG3vRnL&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NjU4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo0MDkwNSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af3JNzqbvV5yOS8OzJvR8JAOE7IDndza98Xl0lVeVMPruQ&amp;oe=69DC3607</BaseURL><SegmentBase indexRange=\"837-916\" timescale=\"44100\" FBMinimumPrefetchRange=\"917-2080\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"917-13553\" FBFirstSegmentRange=\"917-25411\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"25412-51467\" FBPrefetchSegmentRange=\"917-25411\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"1271865281777065a\" bandwidth=\"69062\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"69062\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"129996\" FBPaqMos=\"82.40\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNrGDBtMbIemQ_K3v-pMEAE1l0wBAchtWOUJpQj5eWYkcgfQFgvuH88_RzjeQ5zD1qp06OdkC2oPTv8_65UU1HvWwrPvzBP0czhKHM.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=OdRytjrWw5sQ7kNvwGUtfYw&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NjU4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo2OTU1MiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1l1_uHENLDj5Fgx03RktowfJsBin00zV_ViQ6NK-9Okg&amp;oe=69DC5CB5</BaseURL><SegmentBase indexRange=\"838-917\" timescale=\"44100\" FBMinimumPrefetchRange=\"918-2657\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"918-23725\" FBFirstSegmentRange=\"918-44783\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"44784-89336\" FBPrefetchSegmentRange=\"918-44783\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"963791102905410a\" bandwidth=\"96207\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"96207\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"180726\" FBPaqMos=\"81.66\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQN9Jl5dcq9adj_7hJaV25Ki8cWJm9dIRkvSY9ndE4Z33Wnuff2Zt-B4RArU637hAOCr6ahQCbAgELx_aawwqcqMzPmYIk7bwGjoaRw.mp4?_nc_cat=100&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=uAcuExAmECUQ7kNvwGiwqUz&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ4NjU4MTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjE0LCJiaXRyYXRlIjo5NjY5NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1Uj8aFaFbC_2f9m-sDRVZHsiJ7KXwHeaD8UrN6gst6cA&amp;oe=69DC6159</BaseURL><SegmentBase indexRange=\"833-912\" timescale=\"44100\" FBMinimumPrefetchRange=\"913-2475\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"913-31455\" FBFirstSegmentRange=\"913-59788\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"59789-122039\" FBPrefetchSegmentRange=\"913-59788\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "video_codec": "vp09.00.21.08.00.01.01.01.00",
        "number_of_qualities": 3,
        "video_versions": [
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 101,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwGDnZLe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af22j8bRkybmd58LqeuXyZex1UEgCeGANXakJAB1CSXRKQ&oe=69D85281",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 102,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwGDnZLe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af22j8bRkybmd58LqeuXyZex1UEgCeGANXakJAB1CSXRKQ&oe=69D85281",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1384222,
            "height": 1280,
            "id": "953910417580528v",
            "type": 103,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQMj0JlR0gs_oCicKscKPDdLsgk_cwKk9XuUACLBjChAweb9GzX-7SPOJ2r0ENzyBiKr5aye-1h4aOviqI-xcsHLYNmXEuapk-6xmDQ.mp4?_nc_cat=100&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=_VmDnWaXI_8Q7kNvwGDnZLe&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDg2NTgxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTQsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=5af62758fdf7c4a2&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzk2NDVBMTdGMDVENkJCMDVEOTNCREE5NzlBODM5NThEX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvRjM0ODUxM0JCQUNEODM1QkZGNDYzODk2Mjk5RkI1QjlfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpaiws75r-U_FQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af22j8bRkybmd58LqeuXyZex1UEgCeGANXakJAB1CSXRKQ&oe=69D85281",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 15.0,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=vY0PvLetHQgQ7kNvwEoq92C&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af08RhGijsLRqWdy9qrrIZBmOf_rb38m9SB9gyfZN889MA&oe=69DC58F0&_nc_sid=6d62aa",
              "is_unpublished": false,
              "follower_count": 34037452,
              "friendship_status": {
                "following": false
              }
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/657255699_1385632013371495_7666726418949229423_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgyODMyNDM1MjE3MDIzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m7SPdY3D7l0Q7kNvwGKfyNu&_nc_oc=AdrkR8AX6upMiAm7c5ygaKCuTyDvadH009Lr0d0fHzotJYgBTmCTrj38NnQ7XmplQvk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_ss=7a3ba&oh=00_Af28qKG7kIzwbsKi7_HKmywA2e3NXlp9xnjkNWF8SRdj0w&oe=69DC54C2",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2437,
                4875,
                7313
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad3-2.cdninstagram.com/v/t51.71878-15/657255699_1385632013371495_7666726418949229423_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=105&ig_cache_key=Mzg3MDgyODMyNDM1MjE3MDIzOQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=m7SPdY3D7l0Q7kNvwGKfyNu&_nc_oc=AdrkR8AX6upMiAm7c5ygaKCuTyDvadH009Lr0d0fHzotJYgBTmCTrj38NnQ7XmplQvk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_ss=7a3ba&oh=00_Af28qKG7kIzwbsKi7_HKmywA2e3NXlp9xnjkNWF8SRdj0w&oe=69DC54C2",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 720,
        "original_height": 1280,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODc5ZWNlY2VmMmM2NGU5NmE0NDM3NTBlNGU2OGNiY2IzODcwODI4MzI0MzUyMTcwMjM5Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwNzkyMHwzODcwODI4MzI0MzUyMTcwMjM5fDMyOTQwMjU0MDYyfDBlNTExOWM5NDY5Y2ZjNTc1Y2ZjNWU1OTMwOTJiNmEwNThkYzY5OTU5Zjc3NjIwZTJjNmIwOTI5NTUxMmU2NjMifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658704,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658704503734,
        "code": "DW38do7iBj_",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "968400145722533",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=vY0PvLetHQgQ7kNvwEoq92C&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af08RhGijsLRqWdy9qrrIZBmOf_rb38m9SB9gyfZN889MA&oe=69DC58F0&_nc_sid=6d62aa"
            }
          }
        ]
      },
      {
        "strong_id__": "3870828687528621445_787132",
        "id": "3870828687528621445_787132",
        "expiring_at": 1775745136,
        "pk": 3870828687528621445,
        "is_visual_reply_commenter_notice_enabled": true,
        "is_reshare_of_text_post_app_media_in_ig": false,
        "is_reel_media": true,
        "fbid": 18519178861076290,
        "mezql_token": "",
        "should_request_ads": false,
        "is_terminal_video_segment": false,
        "integrity_review_decision": "pending",
        "client_cache_key": "Mzg3MDgyODY4NzUyODYyMTQ0NQ==.3",
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
          "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=XbeNvhLXv28Q7kNvwFSnFJf&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1V1alqw45X3q4yGkFLoin4hdRfwoIxrypHkoKuUtcP1g&oe=69DC51E9&_nc_sid=6d62aa",
          "username": "natgeo",
          "user_activation_info": {}
        },
        "shop_routing_user_id": null,
        "subscribe_cta_visible": false,
        "commenting_disabled_for_viewer": true,
        "hide_view_all_comment_entrypoint": false,
        "caption": null,
        "is_dash_eligible": 1,
        "video_dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:mpeg:dash:schema:mpd:2011 DASH-MPD.xsd\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011\" minBufferTime=\"PT2S\" type=\"static\" mediaPresentationDuration=\"PT13.766666S\" FBManifestTimestamp=\"1775663908\" FBManifestIdentifier=\"Fsjss50NGBFpZ19kYXNoX2Jhc2ljX3ZwORlmsM2jz6TgxwT8v7nV4+WtBdaXg7Dxja4G/qqL1pbohAfYiuHU64DGB+ry4M2tp8oHIhgiZGFzaF91bmlmaWVkX3ByZW1pdW1feGhlX2licl9hdWRpbyIsGRgFbGlnaHQAFgAUABIUAgA=\"><Period id=\"0\" duration=\"PT13.766666S\"><AdaptationSet id=\"0\" contentType=\"video\" subsegmentAlignment=\"true\" par=\"9:16\" FBUnifiedUploadResolutionMos=\"360:78.1\" FBCellQualityProfile=\"3\" FBQualityProfile=\"3\" FBCellStallProfile=\"1.8\" FBStallProfile=\"1.8\" FBQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\" FBCellQualityRewardCurve=\"0,1,1.7,d; 80,1.8,1.4; 100,2,1\"><Representation id=\"1790243485279723v\" bandwidth=\"344547\" codecs=\"vp09.00.21.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_360p\" FBContentLength=\"592909\" FBPlaybackResolutionMos=\"0:100,360:76.1,480:69.7,720:60,1080:50.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:90.5,480:84.5,720:75.3,1080:65.4\" width=\"360\" height=\"640\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"360p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQM8luH4j2wToHz7wS2UuzWomYkX_xGnTM6pqLal3cGAV5iN6I-T_mYQ9AtCtrKV7iJUL14jhqzoyPQPAw80cp_3eiZpW-fhFeVGkINR9s2ozQ.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=EFZHFPPvcZMQ7kNvwHeGDWw&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfMzYwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6MzQ0NTQ3LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1MXXr0Z2U-csOY3N3l_JriQ1W-L-aFIrrrK9uiniFybA&amp;oe=69DC3EF5</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-6966\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-101494\" FBFirstSegmentRange=\"886-154709\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"154710-384072\" FBPrefetchSegmentRange=\"886-154709\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1980910679452351v\" bandwidth=\"935188\" codecs=\"vp09.00.30.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_540p\" FBContentLength=\"1609303\" FBPlaybackResolutionMos=\"0:100,360:88.4,480:85.1,720:77.5,1080:71.6\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:96,480:95,720:91.7,1080:86.3\" width=\"540\" height=\"960\" frameRate=\"15360/512\" FBQualityClass=\"sd\" FBQualityLabel=\"540p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQNmwWHejVsXTUj2l7nx-PMgFEUmFYlMjFaBrPkDPe0uQeASRiNhKr39GxNsnxH3Sa7tiuavKjBlRORc7xcq_6pHowEkEr74UtmKxO27XAloYA.mp4?_nc_cat=106&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=AlZYEmi5FY4Q7kNvwHLvWMU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNTQwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6OTM1MTg4LCJ1cmxnZW5fc291cmNlIjoid3d3In0%3D&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af13LPGHgduYPzhvHUe26VSsALs5sJfsNIPX_rGPYG_ayg&amp;oe=69DC569E</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-9841\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-282606\" FBFirstSegmentRange=\"886-425596\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"425597-983340\" FBPrefetchSegmentRange=\"886-425596\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation><Representation id=\"1283684740395864v\" bandwidth=\"1601819\" codecs=\"vp09.00.31.08.00.01.01.01.00\" mimeType=\"video/mp4\" sar=\"1:1\" FBEncodingTag=\"dash_vp9-basic-gen2_720p\" FBContentLength=\"2756464\" FBPlaybackResolutionMos=\"0:100,360:94,480:92.3,720:89.3,1080:80.2\" FBPlaybackResolutionMosConfidenceLevel=\"high\" FBPlaybackResolutionCsvqm=\"0:100,360:97.9,480:97.1,720:96.3,1080:93.1\" width=\"720\" height=\"1280\" frameRate=\"15360/512\" FBQualityClass=\"hd\" FBQualityLabel=\"720p\"><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQOZoC0K6rjCQjmohefRVTN5_dSov0i9slklSBh49Ik3vP91fZ3qLlMgs84SgZ2TsC-jWmWpZG6-ltUT0Mw6jmed8aDBiBi8rv_uBh9NxnHiqg.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=nOn_b3dR5h4Q7kNvwG6GH7E&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfdnA5LWJhc2ljLWdlbjJfNzIwcCIsInZpZGVvX2lkIjpudWxsLCJvaWxfdXJsZ2VuX2FwcF9pZCI6NTY3MDY3MzQzMzUyNDI3LCJjbGllbnRfbmFtZSI6ImlnIiwieHB2X2Fzc2V0X2lkIjoxNzk1NTg0OTAzMDExMDYwMywiYXNzZXRfYWdlX2RheXMiOjAsInZpX3VzZWNhc2VfaWQiOjEwMTAwLCJkdXJhdGlvbl9zIjoxMywiYml0cmF0ZSI6MTYwMTgxOSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0ihrnIlaBgwR0z84_SvyaI3E-sc0Tyez59d0cWEJR_Ag&amp;oe=69DC6151</BaseURL><SegmentBase indexRange=\"818-885\" timescale=\"15360\" FBMinimumPrefetchRange=\"886-13919\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"886-471204\" FBFirstSegmentRange=\"886-718131\" FBFirstSegmentDuration=\"5000\" FBSecondSegmentRange=\"718132-1649615\" FBPrefetchSegmentRange=\"886-718131\" FBPrefetchSegmentDuration=\"5000\"><Initialization range=\"0-817\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet id=\"1\" contentType=\"audio\" subsegmentStartsWithSAP=\"1\" subsegmentAlignment=\"true\" bitstreamSwitching=\"true\"><Representation id=\"1508079473995774a\" bandwidth=\"41322\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"41322\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr1_abr_lrac_frag_5_audio\" FBContentLength=\"71780\" FBPaqMos=\"80.37\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m367/AQPBvWzDIb5LTqqPF7OcJqQEUdH2wH-24goKguI3Z79E4jzJ2CzNaVogECA0Vey59AOs4HMbFjQ6o5HpW19a1D0WHb4W8DP3KPHuwos.mp4?_nc_cat=107&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad6-1.cdninstagram.com&amp;_nc_ohc=ilIxrYEJjJEQ7kNvwF6I_ZU&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjFfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ5MDMwMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjEzLCJiaXRyYXRlIjo0MTg0OSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af2ikkA6ZTYpT_0_1uVDu_bFmbNo7ePFi1GSjFrWekT4bw&amp;oe=69DC6934</BaseURL><SegmentBase indexRange=\"837-904\" timescale=\"44100\" FBMinimumPrefetchRange=\"905-2078\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"905-12977\" FBFirstSegmentRange=\"905-23904\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"23905-50678\" FBPrefetchSegmentRange=\"905-23904\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-836\"/></SegmentBase></Representation><Representation id=\"2124270915035820a\" bandwidth=\"69374\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"69374\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr2_abr_lrac_frag_5_audio\" FBContentLength=\"119895\" FBPaqMos=\"85.87\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-1.cdninstagram.com/o1/v/t2/f2/m367/AQMVFUOJryi5KiqVpJ8Km_Umnvr7v7AOQPPj5J035w5DhUzcmYB4okk8fcJxrudklw1vUAyaiuqkZ1NUPhorQnp_k1Je1QwVp1EvSRU.mp4?_nc_cat=110&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;_nc_ohc=-pxJyFSpiLQQ7kNvwEhmF8J&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjJfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ5MDMwMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjEzLCJiaXRyYXRlIjo2OTkwMSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af1pgLV_EiMiFHxHDcHvzEQ5aG3NyLiHXIhcgkMDwsVL_A&amp;oe=69DC3D1F</BaseURL><SegmentBase indexRange=\"838-905\" timescale=\"44100\" FBMinimumPrefetchRange=\"906-2582\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"906-22430\" FBFirstSegmentRange=\"906-42573\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"42574-84991\" FBPrefetchSegmentRange=\"906-42573\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-837\"/></SegmentBase></Representation><Representation id=\"2133728694115509a\" bandwidth=\"97230\" codecs=\"mp4a.40.42\" mimeType=\"audio/mp4\" FBAvgBitrate=\"97230\" audioSamplingRate=\"44100\" FBEncodingTag=\"dash_audio_xheaac_vbr3_abr_lrac_frag_5_audio\" FBContentLength=\"167669\" FBPaqMos=\"84.36\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-2.cdninstagram.com/o1/v/t2/f2/m367/AQMvlhSAgo1bS8WEV2uPNASauhmPHh3w7-BfVeDJBRF0N7YfHwbo8CVtEnnhbZ2rK65uf73_2Ci9fLgmng-47EOaGArql0g38YLfJMU.mp4?_nc_cat=105&amp;_nc_sid=9ca052&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_ohc=JWkeZTcmU2oQ7kNvwFsvIoN&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImlnLXhwdmRzLnN0b3J5LmMyLUMzLmRhc2hfYXVkaW9feGhlYWFjX3ZicjNfYWJyX2xyYWNfZnJhZ181X2F1ZGlvIiwidmlkZW9faWQiOm51bGwsIm9pbF91cmxnZW5fYXBwX2lkIjo1NjcwNjczNDMzNTI0MjcsImNsaWVudF9uYW1lIjoiaWciLCJ4cHZfYXNzZXRfaWQiOjE3OTU1ODQ5MDMwMTEwNjAzLCJhc3NldF9hZ2VfZGF5cyI6MCwidmlfdXNlY2FzZV9pZCI6MTAxMDAsImR1cmF0aW9uX3MiOjEzLCJiaXRyYXRlIjo5Nzc1NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&amp;ccb=17-1&amp;_nc_gid=hYw4H6QIVXAiRbi75-UwMw&amp;_nc_ss=7a3ba&amp;_nc_zt=28&amp;oh=00_Af0O-UPTu5B2bywQLGLF8AWVW9841uIz59rcWmvhL4qiig&amp;oe=69DC3982</BaseURL><SegmentBase indexRange=\"833-900\" timescale=\"44100\" FBMinimumPrefetchRange=\"901-2523\" FBPartialPrefetchDuration=\"2500\" FBPartialPrefetchRange=\"901-29290\" FBFirstSegmentRange=\"901-55119\" FBFirstSegmentDuration=\"4922\" FBSecondSegmentRange=\"55120-117435\" FBPrefetchSegmentRange=\"901-55119\" FBPrefetchSegmentDuration=\"4922\"><Initialization range=\"0-832\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>\n",
        "video_codec": "vp09.00.21.08.00.01.01.01.00",
        "number_of_qualities": 3,
        "video_versions": [
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 101,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwEseOp3&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af00RpC_hbO1-v4zp9nIQlNIFCrCtilH7EIBJlA_ifhdPg&oe=69D85C07",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 102,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwEseOp3&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af00RpC_hbO1-v4zp9nIQlNIFCrCtilH7EIBJlA_ifhdPg&oe=69D85C07",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          },
          {
            "bandwidth": 1699428,
            "height": 1280,
            "id": "1446825286910099v",
            "type": 103,
            "url": "https://scontent-iad6-1.cdninstagram.com/o1/v/t2/f2/m78/AQMleyUNz2PJjfK-bqpYAq9OVlsR5er_8p7sRIxvUlFBILmIoWytNlx2HIiwOWLSTmS8GSy70uJlSySaVU_R5hgZ1GrtXwCWfa_36s4.mp4?_nc_cat=106&_nc_sid=5e9851&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_ohc=ZPn9alQ7ZfkQ7kNvwEseOp3&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uU1RPUlkuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSIsInhwdl9hc3NldF9pZCI6MTc5NTU4NDkwMzAxMTA2MDMsImFzc2V0X2FnZV9kYXlzIjowLCJ2aV91c2VjYXNlX2lkIjoxMDEwMCwiZHVyYXRpb25fcyI6MTMsInVybGdlbl9zb3VyY2UiOiJ3d3cifQ%3D%3D&ccb=17-1&vs=fdb661439c8db87c&_nc_vs=HBksFQIYUWlnX3hwdl9wbGFjZW1lbnRfcGVybWFuZW50X3YyLzI2NEM5Q0Y0RTYwMEZGMjI5MDk3Q0I2N0FDRDBDNUFGX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhhRaWdfeHB2X3BsYWNlbWVudF9wZXJtYW5lbnRfdjIvMDQ0MzUyQ0JFMDZCNDU5RjJFODgzRDdBN0Y5OEVBQTJfYXVkaW9fZGFzaGluaXQubXA0FQICyAESACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpa2pLH8r-U_FQIoAkMzLBdAK4gxJul41RgSZGFzaF9iYXNlbGluZV8xX3YxEQB16Adl6J0BAA&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_zt=28&_nc_ss=7a3ba&oh=00_Af00RpC_hbO1-v4zp9nIQlNIFCrCtilH7EIBJlA_ifhdPg&oe=69D85C07",
            "url_expiration_timestamp_us": null,
            "width": 720,
            "fallback": null
          }
        ],
        "video_duration": 13.765999794006348,
        "has_audio": true,
        "can_see_insights_as_brand": false,
        "media_type": 2,
        "original_media_type": 2,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "sharing_friction_info": {
          "bloks_app_url": null,
          "should_have_sharing_friction": false,
          "sharing_friction_payload": null
        },
        "has_translation": false,
        "sponsor_tags": [
          {
            "permission": false,
            "sponsor_id": null,
            "username": null,
            "is_pending": false,
            "sponsor": {
              "strong_id__": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=vY0PvLetHQgQ7kNvwEoq92C&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af08RhGijsLRqWdy9qrrIZBmOf_rb38m9SB9gyfZN889MA&oe=69DC58F0&_nc_sid=6d62aa",
              "is_unpublished": false,
              "follower_count": 34037452,
              "friendship_status": {
                "following": false
              }
            }
          }
        ],
        "coauthor_producers": [],
        "media_overlay_info": null,
        "profile_grid_control_enabled": false,
        "image_versions2": {
          "candidates": [
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/659614888_1512637680515245_5529787493603763341_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDgyODY4NzUyODYyMTQ0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=gitXYB93E4QQ7kNvwEPImBN&_nc_oc=AdpPXfHIsxYB7cSEnxvXr-R5fXYF-tlyyMSQivHRRmiTONWtyGohqZEN5Gt4I_NAsGM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_ss=7a3ba&oh=00_Af1VSJgBHwqp_PYROlKYqrK3FgBcJUdAb6i-VprOiXbwuw&oe=69DC69B1",
              "width": 640,
              "is_spatial_image": false
            },
            {
              "estimated_scans_sizes": [
                2419,
                4839,
                7259
              ],
              "height": 1136,
              "scans_profile": "e15",
              "url": "https://scontent-iad6-1.cdninstagram.com/v/t51.71878-15/659614888_1512637680515245_5529787493603763341_n.jpg?stp=dst-jpg_e15_tt6&_nc_cat=102&ig_cache_key=Mzg3MDgyODY4NzUyODYyMTQ0NQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjY0MHgxMTM2LnNkci5DMyJ9&_nc_ohc=gitXYB93E4QQ7kNvwEPImBN&_nc_oc=AdpPXfHIsxYB7cSEnxvXr-R5fXYF-tlyyMSQivHRRmiTONWtyGohqZEN5Gt4I_NAsGM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-iad6-1.cdninstagram.com&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&_nc_ss=7a3ba&oh=00_Af1VSJgBHwqp_PYROlKYqrK3FgBcJUdAb6i-VprOiXbwuw&oe=69DC69B1",
              "width": 640,
              "is_spatial_image": false
            }
          ]
        },
        "original_width": 720,
        "original_height": 1280,
        "is_paid_partnership": true,
        "music_metadata": null,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODc5ZWNlY2VmMmM2NGU5NmE0NDM3NTBlNGU2OGNiY2IzODcwODI4Njg3NTI4NjIxNDQ1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkwNzkyMHwzODcwODI4Njg3NTI4NjIxNDQ1fDMyOTQwMjU0MDYyfDBmYTRiMDNmZGM3MmZkMjllNGQwZmZiZGE4ODIyNDViOTM4NzU0MTJiZGQ2Y2JmOTdmNjg1ZjNhYTk5OWEzM2EifSwic2lnbmF0dXJlIjoiIn0=",
        "ig_media_sharing_disabled": false,
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "creative_config": null,
        "cutout_sticker_info": [],
        "can_hype": false,
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "is_open_to_public_submission": false,
        "media_attributions_data": [],
        "taken_at": 1775658736,
        "product_type": "story",
        "has_liked": false,
        "can_viewer_save": false,
        "is_organic_product_tagging_eligible": true,
        "device_timestamp": 1775658736503736,
        "code": "DW38i7KiPWF",
        "caption_is_edited": false,
        "original_media_has_visual_reply_media": false,
        "is_quicksnap_recap": false,
        "deleted_reason": 0,
        "is_story_image_with_music": false,
        "filter_type": 0,
        "archive_story_deletion_ts": 0,
        "can_send_prompt": false,
        "is_arirang_prize": false,
        "is_first_take": false,
        "is_from_ayt_clips_inspiration": false,
        "is_from_discovery_surface": false,
        "is_rollcall_v2": false,
        "supports_reel_reactions": true,
        "is_photo_mash_story": false,
        "can_reshare": true,
        "can_reply": false,
        "can_mention_back": false,
        "can_play_spotify_audio": false,
        "is_superlative": false,
        "show_one_tap_fb_share_tooltip": true,
        "can_mention_share": false,
        "is_viewer_mentioned": false,
        "wearables_creator_tools_info": [],
        "wearable_shared_media_resolutions": [],
        "reel_mentions": [
          {
            "end_time_ms": 86400.0,
            "height": 0.0,
            "id": "983436374123185",
            "is_fb_sticker": 0,
            "is_hidden": 0,
            "is_pinned": 0,
            "is_sticker": 1,
            "rotation": 0.0,
            "start_time_ms": 0.0,
            "width": 0.0,
            "x": 0.0,
            "y": 0.0,
            "z": 0,
            "user": {
              "strong_id__": "304662892",
              "id": "304662892",
              "pk": 304662892,
              "pk_id": "304662892",
              "username": "prada",
              "full_name": "Prada",
              "is_private": false,
              "is_verified": true,
              "profile_pic_id": "3256058276699330356_304662892",
              "profile_pic_url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.2885-19/409793882_1787108065048476_562083207041098824_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-xxc1-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHfNR6pbgZTjl3CNUP5l8Xbpv0SjKAC9xPFxCmGtRftAWitUMbzWtnr3tOZjWWALLE&_nc_ohc=vY0PvLetHQgQ7kNvwEoq92C&_nc_gid=hYw4H6QIVXAiRbi75-UwMw&edm=ALCvFkgBAAAA&ccb=7-5&ig_cache_key=GFr1bBicd2SFXVkGAEik5eGy68wHbkULAAAB1501500j-ccb7-5&oh=00_Af08RhGijsLRqWdy9qrrIZBmOf_rb38m9SB9gyfZN889MA&oe=69DC58F0&_nc_sid=6d62aa"
            }
          }
        ]
      }
    ],
    "is_nux": false,
    "has_besties_media": false,
    "media_count": 7,
    "media_ids": [
      3870828041672894129,
      3870828324352170239,
      3870828687528621445
    ],
    "has_fan_club_media": false,
    "show_fan_club_stories_teaser": false,
    "is_cacheable": true,
    "disabled_reply_types": [
      "story_remix_reply",
      "story_selfie_reply",
      "story_voice_reply"
    ],
    "is_archived": false,
    "show_expiration_tray_signal": false
  },
  "unviewable_authors_info": null,
  "status": "ok"
}
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
      "strong_id__": "363248769",
      "pk": 363248769,
      "pk_id": "363248769",
      "id": "363248769",
      "username": "astronomypicturesdaily",
      "full_name": "Astronomy Picture Of The Day",
      "is_private": false,
      "is_verified": false,
      "profile_pic_id": "2300632014331573822_363248769",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-19/95891344_546832856254535_7903437920034357248_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4yMjEuYzIifQ&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=111&_nc_oc=Q6cZ2gFX7F098uPrM_-sBc0QmtI_Les68mbwKbUcB6uTEK4ofRcvTYp-KhKZhfEn2gQjKrE&_nc_ohc=us0DZUFJZyYQ7kNvwF93z5B&_nc_gid=sC3rNa14SgjL908clhk7_w&edm=AIzrcHcBAAAA&ccb=7-5&ig_cache_key=GJAvtwVHCCZyV-EBAAAAAADqpq5tbkULAAAB0j-ccb7-5&oh=00_Af2NtNmjkbbVjZecEn6diqP2oqtkz4DP6s_H-wctEqJtbg&oe=69DC3B8C&_nc_sid=e9f0d8",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "Astronomy Picture Of The Day",
      "social_context": "Astronomy Picture Of The Day"
    },
    {
      "strong_id__": "1934468093",
      "pk": 1934468093,
      "pk_id": "1934468093",
      "id": "1934468093",
      "username": "natgeo_africa",
      "full_name": "Nat Geo Channel Africa",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "3694842092895346377_1934468093",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.82787-19/529167135_18487897162068094_3833751336155906899_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDQyLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gFX7F098uPrM_-sBc0QmtI_Les68mbwKbUcB6uTEK4ofRcvTYp-KhKZhfEn2gQjKrE&_nc_ohc=jx0pWbXHRvsQ7kNvwFeUoe3&_nc_gid=sC3rNa14SgjL908clhk7_w&edm=AIzrcHcBAAAA&ccb=7-5&ig_cache_key=GB9zih9_MP3_pK5BAFODwDSHODQ1bmNDAQAB3203200j-ccb7-5&oh=00_Af2iPBSvq-avawQJWNhOWoAAPuWFBHoI3UctJsfrKuOheQ&oe=69DC41A6&_nc_sid=e9f0d8",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "Nat Geo Channel Africa",
      "social_context": "Nat Geo Channel Africa"
    },
    {
      "strong_id__": "528817151",
      "pk": 528817151,
      "pk_id": "528817151",
      "id": "528817151",
      "username": "nasa",
      "full_name": "NASA",
      "is_private": false,
      "is_verified": true,
      "profile_pic_id": "1735715738009579084_528817151",
      "profile_pic_url": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-19/29090066_159271188110124_1152068159029641216_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gFX7F098uPrM_-sBc0QmtI_Les68mbwKbUcB6uTEK4ofRcvTYp-KhKZhfEn2gQjKrE&_nc_ohc=X3d-833XCzIQ7kNvwHXAI4j&_nc_gid=sC3rNa14SgjL908clhk7_w&edm=AIzrcHcBAAAA&ccb=7-5&ig_cache_key=GBLhuwEsG5c225AAAAAAAADj9-wPbkULAAAB3203200j-ccb7-5&oh=00_Af2DOwdGUSCQKA3xoqw63eNrhMVWI3-rzp0FjppIob-_SQ&oe=69DC31E9&_nc_sid=e9f0d8",
      "chaining_info": {
        "sources": "",
        "algorithm": null
      },
      "profile_chaining_secondary_label": "NASA",
      "social_context": "NASA"
    }
  ],
  "is_backup": false,
  "is_recommend_account": false,
  "chaining_upsell_cards": [],
  "follow_ranking_token": "84a75c2bd3e34016be370688d5e25688|48032594903|chaining",
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
                100358,
                150537
              ],
              "height": 1334,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwFHeXRU&_nc_oc=AdpO-5wfS0_tU4M4hVMymxi0cXQz7DsBQ2Am3Zk88r9MtJ9eMa0A8I0ctsduHNWUGr8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af0TfY_gZQI3wnABVr7u2aEbo2NbwA03JnCJaMD8uNCJ9Q&oe=69DC6562",
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
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwFHeXRU&_nc_oc=AdpO-5wfS0_tU4M4hVMymxi0cXQz7DsBQ2Am3Zk88r9MtJ9eMa0A8I0ctsduHNWUGr8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af2bktvn_bHClMo6I_2-sSjLcCaPB17Wegi65vFHKpRvXQ&oe=69DC6562",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 1,
        "original_width": 1080,
        "original_height": 1334,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNThkNDIzYTM5NThlNDlkYmFlMGJkMTgzZmFiZTI0NmMxOTI5MjYxMTA4OTg2MTAyNDUxIiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkxMzgzMHwxOTI5MjYxMTA4OTg2MTAyNDUxfDM4ODM2NTUyNzI4fDI1YmMwNDJkYWE3Nzg0MTQxMDA0MmZlZmVlMjA4ZDI1M2ZiZDA0YzkwYjFkZDA2N2IxMGI4MzM1MDJiYmVkYTAifSwic2lnbmF0dXJlIjoiIn0=",
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
              "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/11426732_990789794299104_1839082617_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=Nk9rpOO4FmUQ7kNvwE-NquS&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GKxbrgDgfLw5HoUDAHksnm0AAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af1tR39KLzQAt2wN7G3iP-hF-QajoFEUjhWQB3j1GKFpzA&oe=69DC3E73&_nc_sid=a8b8e2",
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
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/487340431_1510016599961079_422634517629355178_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=seU08ayHeVsQ7kNvwF0Hrxe&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GI85DB33rQsjWl0FAKrEHcXaf90FbkULAAAB1501500j-ccb7-5&oh=00_Af2ZN7ZavQWPCs3WP-b-jTMyq8HtdpKfNFWV9I-gAhfu1g&oe=69DC556A&_nc_sid=a8b8e2",
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
              "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/468337925_1583355895611127_2678160184603292032_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=1sUi-nQ8MMwQ7kNvwF287cD&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GAVF6hv3-rXFDaAFAICx35Z-vColbkULAAAB1501500j-ccb7-5&oh=00_Af02N8Gm2utmzYGvcdfIV3-ECXVhSZ5G8NqJd-R3ilGaNQ&oe=69DC34E0&_nc_sid=a8b8e2",
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": false
            },
            "x": 0.9319999814000001,
            "y": 0.0912000015
          }
        ],
        "photo_of_you": false,
        "can_see_insights_as_brand": false,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "fb_user_tags": {
          "in": []
        },
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": false,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": true,
          "is_pivot_page_available": false,
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "media_overlay_info": null,
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "media_notes": {
          "items": []
        },
        "product_type": "feed",
        "subscribe_cta_visible": false,
        "creative_config": null,
        "is_cutout_sticker_allowed": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "meta_ai_suggested_prompts": [],
        "gen_ai_chat_with_ai_cta_info": null,
        "can_reply": false,
        "floating_context_items": [],
        "is_eligible_content_for_post_roll_ad": false,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "eligible_insights_entrypoints": "NONE",
        "media_attributions_data": [],
        "is_eligible_for_poe": false,
        "is_eligible_for_organic_eager_refresh": false,
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "coauthor_producers": [],
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "product_suggestions": [],
        "igbio_product": null,
        "is_paid_partnership": false,
        "reshare_count": 11,
        "ig_media_sharing_disabled": false,
        "media_repost_count": 2,
        "like_count": 14016,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "caption": {
          "strong_id__": "18006729967037433",
          "bit_flags": 0,
          "created_at": 1544205875,
          "created_at_utc": 1544205875,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "18006729967037433",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 1929261108986102451,
          "status": "Active",
          "type": 1,
          "user_id": 429173,
          "text": "Vardzia is a cave monastery site located in southern Georgia. It is excavated from the slopes of the Erusheti Mountain on the left side of the Kura River. Oh Georgia, I miss you when I look at these images 😭 #georgia #exploregeorgia #MavicPro\n.\n.\n.\n.\n.\n#mymavic #awesome_earthpix #collectivelycreate #exploretocreate #livefolk #beautifuldestinations #iglifecz #folkcreative #exklusive_shot #AGameOfTones #igerscz #discoverglobe #QueekyGrams #ourplanetdaily #adventureculture #welivetoexplore #stayandwander #dnescestujem #droneofficial #droneoftheday #dronesdaily #dji #fromwhereidrone #earthofficial #natgeo #MavicPro @beautifuldestinations @roamtheplanet @earthofficial @earthpix @folkmagazine @liveoutdoor.s @awesomeglobe @awesome.earth @djiglobal @fromwhereidrone @dronestagr.am @droneoftheday @droneofficial @earthstoke @livefolk @global_hotshotz @vzcomood @artofvisuals @majestic_earth_ @folkvibe @welivetoexplore @lastingvisuals @mountainsphoto @theglobewanderer @tentree @awesome.earth @awesomeglobe @ourplanetdaily",
          "user": {
            "strong_id__": "429173",
            "pk": 429173,
            "pk_id": "429173",
            "id": "429173",
            "is_unpublished": false,
            "fbid_v2": 17841401355190006,
            "username": "hynecheck",
            "full_name": "Hynek Hampl",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3301920468198178307_429173",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/427378186_275046522125863_1224244213859159903_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43ODUuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=Bb5J40vuSOQQ7kNvwGgEnXI&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GApGeRknfj9CJ-oAAF8PZ02gY-0QbkULAAAB1501500j-ccb7-5&oh=00_Af14CvRWrBbxZ_tng7XCzyQf4iSr2gRRtx29EYwwnzJmuA&oe=69DC51BA&_nc_sid=a8b8e2"
          },
          "is_covered": false,
          "private_reply_status": 0
        },
        "comment_count": 579,
        "can_view_more_preview_comments": false,
        "preview_comments": [],
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
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
        "locations": [],
        "shop_routing_user_id": null,
        "featured_products": [],
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "sharing_friction_info": {
          "should_have_sharing_friction": false,
          "bloks_app_url": null,
          "sharing_friction_payload": null
        },
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "user": {
          "pk": "429173",
          "id": "429173",
          "username": "hynecheck",
          "full_name": "Hynek Hampl",
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/427378186_275046522125863_1224244213859159903_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43ODUuYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=107&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=Bb5J40vuSOQQ7kNvwGgEnXI&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GApGeRknfj9CJ-oAAF8PZ02gY-0QbkULAAAB1501500j-ccb7-5&oh=00_Af14CvRWrBbxZ_tng7XCzyQf4iSr2gRRtx29EYwwnzJmuA&oe=69DC51BA&_nc_sid=a8b8e2",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "caption_is_edited": true,
        "code": "BrGHMHIF8Kz",
        "device_timestamp": 1544205867,
        "enable_media_notes_production": true,
        "filter_type": 0,
        "has_views_fetching": true,
        "like_and_view_counts_disabled": false,
        "original_media_has_visual_reply_media": false,
        "report_info": {
          "has_viewer_submitted_report": false
        },
        "is_organic_product_tagging_eligible": true,
        "can_viewer_reshare": true,
        "has_shared_to_fb": 0,
        "media_reposter_bottomsheet_enabled": false,
        "has_liked": false,
        "can_viewer_save": true,
        "is_comments_gif_composer_enabled": true,
        "image_versions": [
          {
            "estimated_scans_sizes": [
              50179,
              100358,
              150537
            ],
            "height": 1334,
            "scans_profile": "e35",
            "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwFHeXRU&_nc_oc=AdpO-5wfS0_tU4M4hVMymxi0cXQz7DsBQ2Am3Zk88r9MtJ9eMa0A8I0ctsduHNWUGr8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af0TfY_gZQI3wnABVr7u2aEbo2NbwA03JnCJaMD8uNCJ9Q&oe=69DC6562",
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
            "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwFHeXRU&_nc_oc=AdpO-5wfS0_tU4M4hVMymxi0cXQz7DsBQ2Am3Zk88r9MtJ9eMa0A8I0ctsduHNWUGr8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af2bktvn_bHClMo6I_2-sSjLcCaPB17Wegi65vFHKpRvXQ&oe=69DC6562",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/640956567_18562047613037433_6822966074348684895_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=102&ig_cache_key=MTkyOTI2MTEwODk4NjEwMjQ1MQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4MTMzNC5zZHIuQzMifQ%3D%3D&_nc_ohc=JqNPf-kaCNsQ7kNvwFHeXRU&_nc_oc=AdpO-5wfS0_tU4M4hVMymxi0cXQz7DsBQ2Am3Zk88r9MtJ9eMa0A8I0ctsduHNWUGr8&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af0TfY_gZQI3wnABVr7u2aEbo2NbwA03JnCJaMD8uNCJ9Q&oe=69DC6562",
        "taken_at_ts": 1544205867,
        "sponsor_tags": [],
        "play_count": 0
      },
      {
        "strong_id__": "1929229904589027835_276524869",
        "id": "1929229904589027835_276524869",
        "fbid": 17989037833125917,
        "deleted_reason": 0,
        "client_cache_key": "MTkyOTIyOTkwNDU4OTAyNzgzNQ==.3",
        "integrity_review_decision": "approved",
        "pk": "1929229904589027835",
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
                16232,
                32464,
                48696
              ],
              "height": 720,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFf5LCB&_nc_oc=Adrux8RnIYUlrnOZKQ5Kki4R_UpYmilibSCwmgegoX8Pm_z9Dw2GjaCVXNEMvz5thIE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af2JFNWfDPFicPsvlyW7QsD2FneAmIgfSN8vvZ6PXlF_eg&oe=69DC4804",
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
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFf5LCB&_nc_oc=Adrux8RnIYUlrnOZKQ5Kki4R_UpYmilibSCwmgegoX8Pm_z9Dw2GjaCVXNEMvz5thIE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af09lbSzS3n_oJzRkf8TLBp63dI89PVNY80hoa9_FXsm3g&oe=69DC4804",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 1,
        "original_width": 1080,
        "original_height": 720,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNThkNDIzYTM5NThlNDlkYmFlMGJkMTgzZmFiZTI0NmMxOTI5MjI5OTA0NTg5MDI3ODM1Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkxMzg3MXwxOTI5MjI5OTA0NTg5MDI3ODM1fDM4ODM2NTUyNzI4fDZkNTBmZGVkYjNiMWFiZWRjYTJhZmI4ZDExOTI0ZGViZGE4MTgzNjkyYmRhODU1ZjAyMTA5OTY2NmM2NzM1ZDcifSwic2lnbmF0dXJlIjoiIn0=",
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
        "taken_at": 1544202148,
        "usertags": [
          {
            "user": {
              "pk": "1029649300",
              "id": "1029649300",
              "username": "natgeoanimals",
              "full_name": "National Geographic Animals",
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/658262907_18585322099017301_1153555058553566840_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=ic5ODsLE2O8Q7kNvwHbMs82&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GHtLPCdVhr_BQAdCAHi28MU2QAIQbmNDAQAB1501500j-ccb7-5&oh=00_Af2dfAP-npm_9o13z2oP7__8PvYi-iFNxFvcmRbTYnnx9Q&oe=69DC588C&_nc_sid=a8b8e2",
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
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/525764789_18523595374024831_4665287119118685063_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby42NjcuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=tshhWSqzMN4Q7kNvwG-qBiF&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GLWIVh9-WDuiHM9BAIdTRsbqbb5AbmNDAQAB1501500j-ccb7-5&oh=00_Af0CKHeYNU_LEbcECFnGDhLEjDMrWfDz-mkhM2AfOqO8GA&oe=69DC41A3&_nc_sid=a8b8e2",
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
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/10175116_700926226628139_537225696_a.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xNTAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=ErU9paF0HF0Q7kNvwG3eoDT&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GIxCmwArfsAafX0CAOBpBSAAAAAAYUULAAAB1501500j-ccb7-5&oh=00_Af1dPK9F3kHX94_U3ra6nIvrys1eX08VwlYu2JEzz3dBVA&oe=69DC3FE3&_nc_sid=a8b8e2",
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": false
            },
            "x": 0.5,
            "y": 0.5
          }
        ],
        "photo_of_you": false,
        "can_see_insights_as_brand": false,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "fb_user_tags": {
          "in": []
        },
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": false,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": true,
          "is_pivot_page_available": false,
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "media_overlay_info": null,
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "media_notes": {
          "items": []
        },
        "product_type": "feed",
        "subscribe_cta_visible": false,
        "creative_config": null,
        "is_cutout_sticker_allowed": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "meta_ai_suggested_prompts": [],
        "gen_ai_chat_with_ai_cta_info": null,
        "can_reply": false,
        "floating_context_items": [],
        "is_eligible_content_for_post_roll_ad": false,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "eligible_insights_entrypoints": "NONE",
        "media_attributions_data": [],
        "is_eligible_for_poe": false,
        "is_eligible_for_organic_eager_refresh": false,
        "commerce_integrity_review_decision": "approved",
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "coauthor_producers": [],
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "product_suggestions": [],
        "igbio_product": null,
        "is_paid_partnership": false,
        "reshare_count": 1,
        "ig_media_sharing_disabled": false,
        "media_repost_count": 1,
        "like_count": 6172,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "caption": {
          "strong_id__": "17989037887125917",
          "bit_flags": 0,
          "created_at": 1544202155,
          "created_at_utc": 1544202155,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "17989037887125917",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 1929229904589027835,
          "status": "Active",
          "type": 1,
          "user_id": 276524869,
          "text": "No helmet needed once your on Cát Bà Island.\n.\nCát Bà Island || Vietnam\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nShot on EOS T3i and SIGMA 85mm F1.4 EX DG HSM\nISO 100 | f/1.4 | 1/2000\n——\n#vietnam #vietnamese #vietnamesefood #vietnamflashback #vietnamesegirl #vietnamtravel #vietnamtrip #vietnamesehair #vietnamwar #vietnamesecuisine #vietnamflashbacks #vietnamesecoffee #vietnamfood #Canon #canonphotography #canonphoto #canon6d #canoneos #canonusa #canon70d #canon5dmarkiii #canon5d #canonaustralia #canonphotos #canon7d #canon60d #canon700d #canon5dmarkiv #canonphotographer #canoncanada",
          "user": {
            "strong_id__": "276524869",
            "pk": 276524869,
            "pk_id": "276524869",
            "id": "276524869",
            "is_unpublished": false,
            "fbid_v2": 17841401346074320,
            "username": "samuellemieux",
            "full_name": "Samuel Lemieux",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "3460593955377529534_276524869",
            "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/460602681_1286701775682716_7443510089900581929_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NTguYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=Enb1_W-dnWUQ7kNvwFaWgPm&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GDk9dBucfEWaP5IEAClkj0b9qExnbkULAAAB1501500j-ccb7-5&oh=00_Af3dwvCEijio1P9nwv-GpOZWdDFqlNtl5BIk4VBXoaFosA&oe=69DC36EC&_nc_sid=a8b8e2"
          },
          "is_covered": false,
          "private_reply_status": 0
        },
        "comment_count": 182,
        "can_view_more_preview_comments": false,
        "preview_comments": [],
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
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
        "locations": [],
        "shop_routing_user_id": null,
        "featured_products": [],
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "sharing_friction_info": {
          "should_have_sharing_friction": false,
          "bloks_app_url": null,
          "sharing_friction_payload": null
        },
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "user": {
          "pk": "276524869",
          "id": "276524869",
          "username": "samuellemieux",
          "full_name": "Samuel Lemieux",
          "profile_pic_url": "https://scontent-dfw5-2.cdninstagram.com/v/t51.2885-19/460602681_1286701775682716_7443510089900581929_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby45NTguYzIifQ&_nc_ht=scontent-dfw5-2.cdninstagram.com&_nc_cat=108&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=Enb1_W-dnWUQ7kNvwFaWgPm&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GDk9dBucfEWaP5IEAClkj0b9qExnbkULAAAB1501500j-ccb7-5&oh=00_Af3dwvCEijio1P9nwv-GpOZWdDFqlNtl5BIk4VBXoaFosA&oe=69DC36EC&_nc_sid=a8b8e2",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "caption_is_edited": true,
        "code": "BrGAGBxFvn7",
        "device_timestamp": 1544202148,
        "enable_media_notes_production": true,
        "filter_type": 0,
        "has_views_fetching": true,
        "like_and_view_counts_disabled": false,
        "original_media_has_visual_reply_media": false,
        "report_info": {
          "has_viewer_submitted_report": false
        },
        "is_organic_product_tagging_eligible": true,
        "can_viewer_reshare": true,
        "has_shared_to_fb": 0,
        "media_reposter_bottomsheet_enabled": false,
        "has_liked": false,
        "can_viewer_save": true,
        "is_comments_gif_composer_enabled": true,
        "image_versions": [
          {
            "estimated_scans_sizes": [
              16232,
              32464,
              48696
            ],
            "height": 720,
            "scans_profile": "e35",
            "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFf5LCB&_nc_oc=Adrux8RnIYUlrnOZKQ5Kki4R_UpYmilibSCwmgegoX8Pm_z9Dw2GjaCVXNEMvz5thIE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af2JFNWfDPFicPsvlyW7QsD2FneAmIgfSN8vvZ6PXlF_eg&oe=69DC4804",
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
            "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFf5LCB&_nc_oc=Adrux8RnIYUlrnOZKQ5Kki4R_UpYmilibSCwmgegoX8Pm_z9Dw2GjaCVXNEMvz5thIE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af09lbSzS3n_oJzRkf8TLBp63dI89PVNY80hoa9_FXsm3g&oe=69DC4804",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/630462428_18409600975125917_7503154876014188463_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ig_cache_key=MTkyOTIyOTkwNDU4OTAyNzgzNQ%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzIwLnNkci5DMyJ9&_nc_ohc=3uGKfyTgKa8Q7kNvwFf5LCB&_nc_oc=Adrux8RnIYUlrnOZKQ5Kki4R_UpYmilibSCwmgegoX8Pm_z9Dw2GjaCVXNEMvz5thIE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af2JFNWfDPFicPsvlyW7QsD2FneAmIgfSN8vvZ6PXlF_eg&oe=69DC4804",
        "taken_at_ts": 1544202148,
        "sponsor_tags": [],
        "play_count": 0
      },
      {
        "strong_id__": "1929198769279088926_1423130965",
        "id": "1929198769279088926_1423130965",
        "fbid": 17992565425118532,
        "deleted_reason": 0,
        "client_cache_key": "MTkyOTE5ODc2OTI3OTA4ODkyNg==.3",
        "integrity_review_decision": "approved",
        "pk": "1929198769279088926",
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
                25149,
                50299,
                75448
              ],
              "height": 716,
              "scans_profile": "e35",
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwFrPumI&_nc_oc=AdpCOMtRajNMIBnOnhK9YRLMAYBqCPvFeSCr6g99sgv55bviF7yN4Q_Bv96lTv3YjrE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af39TYWu5Te37cVSt1EcJBm793l9y4ZlIBBVVLOGJ0iUpw&oe=69DC6737",
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
              "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwFrPumI&_nc_oc=AdpCOMtRajNMIBnOnhK9YRLMAYBqCPvFeSCr6g99sgv55bviF7yN4Q_Bv96lTv3YjrE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af14gcVUQckv0aJsYxGEflCjuz8RwD1RiVI7HG7JKywgAA&oe=69DC6737",
              "width": 750,
              "is_spatial_image": false
            }
          ]
        },
        "media_type": 1,
        "original_width": 1080,
        "original_height": 716,
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiNThkNDIzYTM5NThlNDlkYmFlMGJkMTgzZmFiZTI0NmMxOTI5MTk4NzY5Mjc5MDg4OTI2Iiwic2VydmVyX3Rva2VuIjoiMTc3NTY2MzkxMzg3MXwxOTI5MTk4NzY5Mjc5MDg4OTI2fDM4ODM2NTUyNzI4fDRjNjMzMTVhM2EyNzY5OWZjNGVkZjAyMzIyMDAyMzM0MGYzZWI2YzEyNGYzMjc0ZDc0NzNkMDc5ODg4ZDJlNDcifSwic2lnbmF0dXJlIjoiIn0=",
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
        "taken_at": 1544198436,
        "usertags": [
          {
            "user": {
              "pk": "20388776",
              "id": "20388776",
              "username": "visittheusa",
              "full_name": "Visit The USA",
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/491438798_18500574025036777_282017071777073097_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=iCn6e-hArvwQ7kNvwH4d9g_&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GM7CSh3pM_eOLLpBAMlH3lcI7ekDbvEnAQAB1501500j-ccb7-5&oh=00_Af3aVEWyRTsfkrgdsl6Ws8JpjZ-0xJjKbSfn-KAAsewXSg&oe=69DC5871&_nc_sid=a8b8e2",
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
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-19/539584343_18524625733003826_8708481332788290688_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby43OTYuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=jHwtv1i8lr8Q7kNvwF09Hpr&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GFdnKSAyqmmIDNBBAIBk9-Whvdp4bmNDAQAB1501500j-ccb7-5&oh=00_Af3v_aejRxRrizdl6aarIEAXBS8LhxJyMFm3qUCa9JZeIg&oe=69DC69E7&_nc_sid=a8b8e2",
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
              "profile_pic_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.2885-19/264061680_892373304802999_2303500327805762813_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4zNjAuYzIifQ&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=EUO-NceyQRAQ7kNvwEEmD68&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GPBCvQ_3-tbZmysDAP282-pXrfcfbkULAAAB1501500j-ccb7-5&oh=00_Af2oUYLKQdUbxa18L3UFv4aa8FXbMzJbity1RFtI1mlR0Q&oe=69DC48AB&_nc_sid=a8b8e2",
              "profile_pic_url_hd": null,
              "is_private": false,
              "is_verified": true
            },
            "x": 0.5124999881,
            "y": 0.267295599
          }
        ],
        "photo_of_you": false,
        "can_see_insights_as_brand": false,
        "fundraiser_tag": {
          "has_standalone_fundraiser": false
        },
        "fb_user_tags": {
          "in": []
        },
        "mashup_info": {
          "can_toggle_mashups_allowed": false,
          "formatted_mashups_count": null,
          "has_been_mashed_up": false,
          "has_nonmimicable_additional_audio": false,
          "is_creator_requesting_mashup": false,
          "is_light_weight_check": true,
          "is_light_weight_reuse_allowed_check": true,
          "is_pivot_page_available": false,
          "is_reuse_allowed": false,
          "mashup_type": null,
          "mashups_allowed": false,
          "mashups_allowed_for_carousel": false,
          "non_privacy_filtered_mashups_media_count": 0,
          "privacy_filtered_mashups_media_count": null,
          "original_media": null
        },
        "media_overlay_info": null,
        "is_in_profile_grid": false,
        "profile_grid_control_enabled": false,
        "media_notes": {
          "items": []
        },
        "product_type": "feed",
        "subscribe_cta_visible": false,
        "creative_config": null,
        "is_cutout_sticker_allowed": false,
        "is_tagged_media_shared_to_viewer_profile_grid": false,
        "should_show_author_pog_for_tagged_media_shared_to_profile_grid": false,
        "meta_ai_suggested_prompts": [],
        "gen_ai_chat_with_ai_cta_info": null,
        "can_reply": false,
        "floating_context_items": [],
        "is_eligible_content_for_post_roll_ad": false,
        "related_ads_pivots_media_info": "USER_NOT_IN_TEST_GROUP",
        "eligible_insights_entrypoints": "NONE",
        "media_attributions_data": [],
        "is_eligible_for_poe": true,
        "is_eligible_for_organic_eager_refresh": false,
        "commerce_integrity_review_decision": "approved",
        "is_reuse_allowed": false,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "coauthor_producers": [],
        "coauthor_producer_can_see_organic_insights": false,
        "invited_coauthor_producers": [],
        "product_suggestions": [],
        "igbio_product": null,
        "is_paid_partnership": false,
        "reshare_count": 3,
        "ig_media_sharing_disabled": false,
        "media_repost_count": 1,
        "like_count": 5581,
        "top_likers": [],
        "hidden_likes_string_variant": -1,
        "caption": {
          "strong_id__": "17992565452118532",
          "bit_flags": 0,
          "created_at": 1544198440,
          "created_at_utc": 1544198440,
          "did_report_as_spam": false,
          "is_ranked_comment": false,
          "pk": "17992565452118532",
          "share_enabled": false,
          "content_type": "comment",
          "media_id": 1929198769279088926,
          "status": "Active",
          "type": 1,
          "user_id": 1423130965,
          "has_translation": true,
          "text": "☀️Warme Sonnenstrahlen, herrliche Seeluft und weicher Sandstrand - erlebt den ewigen Sommer in Florida😍 Die rund 700 Kilometer lange Landzunge zwischen dem Atlantik und dem Golf von Mexiko wird auch Sunshine State genannt und wird seinem Namen auf jeden Fall gerecht - rund 300 Sonnentage im Jahr kann man in dem US-Bundeststaat genießen.🏝#mycanusa #sunshinestate #visitflorida #florida #exploremore #visittheusa",
          "user": {
            "strong_id__": "1423130965",
            "pk": 1423130965,
            "pk_id": "1423130965",
            "id": "1423130965",
            "is_unpublished": false,
            "fbid_v2": 17841400808972236,
            "username": "canusatouristik",
            "full_name": "CANUSA TOURISTIK 🇺🇸 & 🇨🇦",
            "is_private": false,
            "is_verified": false,
            "profile_pic_id": "2600837206099067919_1423130965",
            "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.2885-19/205154326_1843163085845566_6652282020977594618_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDAwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=4Co_t95in6EQ7kNvwHpUVEF&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GBZoOgw_tP7YWIwGAPpQFrZAp1FcbkULAAAB1501500j-ccb7-5&oh=00_Af2LRIucxwT-udBF2ilcvnw9xnOJtzYiOzTIRrKUiqxiOA&oe=69DC5283&_nc_sid=a8b8e2"
          },
          "is_covered": false,
          "private_reply_status": 0,
          "text_translation": "☀️Warm sun rays, wonderful sea air and soft sandy beach - experience eternal summer in Florida😍 The 700-kilometer-long landline between the Atlantic and the Gulf of Mexico is also called the Sunshine State and it certainly lives up to its name - around 300 sunny days a year you can enjoy enjoying the U.S. state. 🏝#mycanusa #visitflorida #exploremore #visittheusa"
        },
        "comment_count": 204,
        "can_view_more_preview_comments": false,
        "preview_comments": [],
        "comment_likes_enabled": true,
        "comment_inform_treatment": {
          "action_type": null,
          "should_have_inform_treatment": false,
          "text": "",
          "url": null
        },
        "is_photo_comments_composer_enabled_for_author": false,
        "hide_view_all_comment_entrypoint": true,
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
        "locations": [],
        "shop_routing_user_id": null,
        "featured_products": [],
        "crosspost_metadata": {
          "fb_downstream_use_xpost_metadata": {
            "downstream_use_xpost_deny_reason": "NONE"
          }
        },
        "sharing_friction_info": {
          "should_have_sharing_friction": false,
          "bloks_app_url": null,
          "sharing_friction_payload": null
        },
        "gen_ai_detection_method": {
          "detection_method": "NONE"
        },
        "user": {
          "pk": "1423130965",
          "id": "1423130965",
          "username": "canusatouristik",
          "full_name": "CANUSA TOURISTIK 🇺🇸 & 🇨🇦",
          "profile_pic_url": "https://scontent-dfw5-1.cdninstagram.com/v/t51.2885-19/205154326_1843163085845566_6652282020977594618_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDAwLmMyIn0&_nc_ht=scontent-dfw5-1.cdninstagram.com&_nc_cat=110&_nc_oc=Q6cZ2gHqEotov74fm6ANe2H-LMV_5PpK7f7FkD9q159XBuiu2D52Xw0djqk-s8wjh20NdhY&_nc_ohc=4Co_t95in6EQ7kNvwHpUVEF&_nc_gid=CPGasSafj3wEZeZd2qsx8A&edm=APGXKFABAAAA&ccb=7-5&ig_cache_key=GBZoOgw_tP7YWIwGAPpQFrZAp1FcbkULAAAB1501500j-ccb7-5&oh=00_Af2LRIucxwT-udBF2ilcvnw9xnOJtzYiOzTIRrKUiqxiOA&oe=69DC5283&_nc_sid=a8b8e2",
          "profile_pic_url_hd": null,
          "is_private": false,
          "is_verified": false
        },
        "community_notes_info": {
          "has_viewer_submitted_note": false,
          "note_submission_disabled": false,
          "enable_submission_friction": false,
          "is_eligible_for_request_a_note": true
        },
        "has_high_risk_gen_ai_inform_treatment": false,
        "caption_is_edited": true,
        "code": "BrF5A8wADke",
        "device_timestamp": 1544198436,
        "enable_media_notes_production": true,
        "filter_type": 0,
        "has_views_fetching": true,
        "like_and_view_counts_disabled": false,
        "original_media_has_visual_reply_media": false,
        "report_info": {
          "has_viewer_submitted_report": false
        },
        "is_organic_product_tagging_eligible": true,
        "can_viewer_reshare": true,
        "has_shared_to_fb": 0,
        "media_reposter_bottomsheet_enabled": false,
        "has_liked": false,
        "can_viewer_save": true,
        "is_comments_gif_composer_enabled": true,
        "image_versions": [
          {
            "estimated_scans_sizes": [
              25149,
              50299,
              75448
            ],
            "height": 716,
            "scans_profile": "e35",
            "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwFrPumI&_nc_oc=AdpCOMtRajNMIBnOnhK9YRLMAYBqCPvFeSCr6g99sgv55bviF7yN4Q_Bv96lTv3YjrE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af39TYWu5Te37cVSt1EcJBm793l9y4ZlIBBVVLOGJ0iUpw&oe=69DC6737",
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
            "url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_s750x750_sh0.08_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwFrPumI&_nc_oc=AdpCOMtRajNMIBnOnhK9YRLMAYBqCPvFeSCr6g99sgv55bviF7yN4Q_Bv96lTv3YjrE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af14gcVUQckv0aJsYxGEflCjuz8RwD1RiVI7HG7JKywgAA&oe=69DC6737",
            "width": 750,
            "is_spatial_image": false
          }
        ],
        "thumbnail_url": "https://scontent-dfw6-1.cdninstagram.com/v/t51.82787-15/639492080_18437172370118532_7460465766046979666_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=101&ig_cache_key=MTkyOTE5ODc2OTI3OTA4ODkyNg%3D%3D.3-ccb7-5&ccb=7-5&_nc_sid=58cdad&efg=eyJ2ZW5jb2RlX3RhZyI6InhwaWRzLjEwODB4NzE2LnNkci5DMyJ9&_nc_ohc=RYstf_4MrPsQ7kNvwFrPumI&_nc_oc=AdpCOMtRajNMIBnOnhK9YRLMAYBqCPvFeSCr6g99sgv55bviF7yN4Q_Bv96lTv3YjrE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&se=8&_nc_ht=scontent-dfw6-1.cdninstagram.com&_nc_gid=CPGasSafj3wEZeZd2qsx8A&_nc_ss=7a3ba&oh=00_Af39TYWu5Te37cVSt1EcJBm793l9y4ZlIBBVVLOGJ0iUpw&oe=69DC6737",
        "taken_at_ts": 1544198436,
        "sponsor_tags": [],
        "play_count": 0
      }
    ],
    "auto_load_more_enabled": true,
    "next_max_id": 1926933891264902156,
    "new_photos": [],
    "requires_review": false,
    "total_count": 1123,
    "status": "ok"
  },
  "next_page_id": "1926933891264902156"
}
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
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGbt7kPt-z9_KW3Au-w_4ss74ZbZO55l6ujEmFEpOHH36_YHD6OeEEN4awhFgoYnq0&_nc_ohc=XbeNvhLXv28Q7kNvwF-ryg0&_nc_gid=Kw5H1NvfkMv_nLOfM7FIfA&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1y2z3n_a63533ZvkiaCPK6RpzZJsHlQ3RgWn8zqrsXog&oe=69DC51E9&_nc_sid=6c5dea"
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
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGbt7kPt-z9_KW3Au-w_4ss74ZbZO55l6ujEmFEpOHH36_YHD6OeEEN4awhFgoYnq0&_nc_ohc=XbeNvhLXv28Q7kNvwF-ryg0&_nc_gid=Kw5H1NvfkMv_nLOfM7FIfA&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1y2z3n_a63533ZvkiaCPK6RpzZJsHlQ3RgWn8zqrsXog&oe=69DC51E9&_nc_sid=6c5dea",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGneKg6pSsv4Qg7pwVFd2A1jgL9DsuaQgEdbjbK9MKw9-yW08e_q2Z9bZOCHtI_aem_zI9oSeb5u0ZObh5bAGNHbA&e=AT4Ck9_GTiCmO1JZP2xLCQxaxj4oht1PO5EDPq6r2QFry88mkfKrvTtDR7Py96w_rNHXwllaR4kzpeYeUYDg__7bfKTYy0VUoDpnZ88xPw",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGneKg6pSsv4Qg7pwVFd2A1jgL9DsuaQgEdbjbK9MKw9-yW08e_q2Z9bZOCHtI_aem_zI9oSeb5u0ZObh5bAGNHbA",
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
        "follower_count": 274984769
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "fbid_v2": 17841400573960012,
        "pk_id": "787132",
        "pk": 787132,
        "eligible_for_text_app_activation_badge": false,
        "feed_post_reshare_disabled": false,
        "has_ever_selected_topics": false,
        "has_nme_badge": false,
        "third_party_downloads_enabled": 2,
        "show_fb_link_on_profile": false,
        "show_fb_page_link_on_profile": false,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "is_opal_enabled": false,
        "primary_profile_link_type": 0,
        "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
        "account_type": 2,
        "highlights_tray_type": "DEFAULT",
        "current_catalog_id": null,
        "mini_shop_seller_onboarding_status": null,
        "ads_incentive_expiration_date": null,
        "ads_page_id": null,
        "ads_page_name": null,
        "account_category": "",
        "can_add_fb_group_link_on_profile": false,
        "can_use_affiliate_partnership_messaging_as_creator": false,
        "can_use_affiliate_partnership_messaging_as_brand": false,
        "has_gen_ai_personas_for_profile_banner": false,
        "has_guides": false,
        "highlight_reshare_disabled": false,
        "include_direct_blacklist_status": true,
        "is_direct_roll_call_enabled": true,
        "is_eligible_for_meta_verified_links_in_reels": false,
        "is_eligible_for_post_boost_mv_upsell": false,
        "is_meta_verified_related_accounts_display_enabled": false,
        "is_new_to_instagram": false,
        "is_profile_broadcast_sharing_enabled": true,
        "is_secondary_account_creation": false,
        "profile_type": 0,
        "is_coppa_enforced": false,
        "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
        "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
        "is_bestie": false,
        "latest_reel_media": 1775659002,
        "latest_besties_reel_media": 0,
        "is_ring_creator": false,
        "account_badges": [],
        "has_highlight_reels": true,
        "is_creator_agent_enabled": false,
        "is_private": false,
        "interop_messaging_user_fbid": 113671860027320,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "has_anonymous_profile_picture": false,
        "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGbt7kPt-z9_KW3Au-w_4ss74ZbZO55l6ujEmFEpOHH36_YHD6OeEEN4awhFgoYnq0&_nc_ohc=XbeNvhLXv28Q7kNvwF-ryg0&_nc_gid=Kw5H1NvfkMv_nLOfM7FIfA&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af1y2z3n_a63533ZvkiaCPK6RpzZJsHlQ3RgWn8zqrsXog&oe=69DC51E9&_nc_sid=6c5dea",
        "username": "natgeo",
        "full_name": "National Geographic",
        "fan_club_info": {
          "autosave_to_exclusive_highlight": null,
          "connected_member_count": null,
          "fan_club_id": null,
          "fan_club_name": null,
          "has_created_ssc": null,
          "has_enough_subscribers_for_ssc": null,
          "is_fan_club_gifting_eligible": null,
          "is_fan_club_referral_eligible": null,
          "is_free_trial_eligible": null,
          "largest_public_bc_id": null,
          "subscriber_count": null,
          "should_show_playlists_in_profile_tab": null,
          "fan_consideration_page_revamp_eligiblity": null
        },
        "hd_profile_pic_url_info": {
          "height": 1080,
          "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGI27swUp1bfcf0l1R6npOp-3IjPVRWPknCnMI9yegfgFcyhhCW63qkUBgO3WLj3Jw&_nc_ohc=XbeNvhLXv28Q7kNvwF-ryg0&_nc_gid=Kw5H1NvfkMv_nLOfM7FIfA&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB0j-ccb7-5&oh=00_Af2Q5attgpN3GmFLCSQIevSBkodnPMCxC20o51XFS_S8Lg&oe=69DC51E9&_nc_sid=6c5dea",
          "width": 1080
        },
        "hd_profile_pic_versions": [
          {
            "height": 320,
            "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGI27swUp1bfcf0l1R6npOp-3IjPVRWPknCnMI9yegfgFcyhhCW63qkUBgO3WLj3Jw&_nc_ohc=XbeNvhLXv28Q7kNvwF-ryg0&_nc_gid=Kw5H1NvfkMv_nLOfM7FIfA&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB3203200j-ccb7-5&oh=00_Af1VZNisl3Fy0eV972pIv1ErEh0HRJ-sDWB3GdU4KuVAFg&oe=69DC51E9&_nc_sid=6c5dea",
            "width": 320
          },
          {
            "height": 640,
            "url": "https://scontent-lga3-3.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s640x640_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-lga3-3.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGI27swUp1bfcf0l1R6npOp-3IjPVRWPknCnMI9yegfgFcyhhCW63qkUBgO3WLj3Jw&_nc_ohc=XbeNvhLXv28Q7kNvwF-ryg0&_nc_gid=Kw5H1NvfkMv_nLOfM7FIfA&edm=AGqCYasBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB6406400j-ccb7-5&oh=00_Af3o2VTypouh4XZplkYI8K_fynr8Rr35KX0aAo7MB4iLZg&oe=69DC51E9&_nc_sid=6c5dea",
            "width": 640
          }
        ],
        "is_active_on_text_post_app": true,
        "is_cannes": false,
        "is_facebook_onboarded_charity": false,
        "is_favorite": false,
        "merchant_checkout_style": "none",
        "seller_shoppable_feed_type": "none",
        "show_account_transparency_details": true,
        "show_shoppable_feed": false,
        "transparency_product_enabled": false,
        "text_app_last_visited_time": null,
        "text_post_app_joiner_number": 672534,
        "follower_count": 274984769,
        "following_count": 193,
        "is_eligible_for_slide": false,
        "live_subscription_status": "default",
        "business_contact_method": "UNKNOWN",
        "category_id": "0",
        "city_id": "0",
        "city_name": "",
        "direct_messaging": "UNKNOWN",
        "instagram_location_id": "",
        "page_id": null,
        "public_email": "",
        "public_phone_country_code": "",
        "public_phone_number": "",
        "should_show_category": false,
        "should_show_public_contacts": true,
        "zip": "",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "contact_phone_number": "",
        "has_music_on_profile": false,
        "has_videos": true,
        "has_views_fetching": true,
        "is_call_to_action_enabled": false,
        "is_category_tappable": false,
        "is_eligible_for_creator_product_links": false,
        "is_eligible_for_lead_center": true,
        "is_eligible_for_schools_search_upsell": false,
        "is_eligible_for_smb_support_flow": true,
        "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
        "num_of_admined_pages": null,
        "page_name": "National Geographic",
        "professional_conversion_suggested_account_type": 3,
        "profile_context": "",
        "smb_support_partner": null,
        "ring_creator_metadata": {},
        "text_post_app_joiner_number_label": "672,534",
        "is_onboarding_account": false,
        "recon_features": {
          "enable_recon_cta": true
        },
        "text_post_app_badge_label": "natgeo",
        "is_business": true,
        "is_prime_onboarding_account": false,
        "is_profile_picture_expansion_enabled": true,
        "show_all_highlights_as_selected_in_management_screen": false,
        "show_schools_badge": null,
        "text_post_new_post_count": 5,
        "trial_clips_enabled": false,
        "enable_add_school_in_edit_profile": false,
        "shopping_post_onboard_nux_type": null,
        "fb_page_call_to_action_id": "",
        "address_street": "",
        "is_profile_audio_call_enabled": false,
        "displayed_action_button_partner": null,
        "smb_delivery_partner": null,
        "smb_support_delivery_partner": null,
        "displayed_action_button_type": null,
        "category": "",
        "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn4RfoQOVnG012HhcQoXkgYct7qo3m_CasR3RnZx03aGopX38EQYdVtgQJarM_aem__vEVDIjVTMyZKuIgCyRy_g&e=AT7dIQoYEOwHoId4oSa7UcGig-tBPMa4mudzmZn5VB8bvHa10mgWgL69FYKO1BuVG-YPSnNyyf3pn5qsKgBJf5N3dlCToxAya10T00-7sQ",
        "external_url": "http://visitstore.bio/natgeo",
        "active_standalone_fundraisers": {
          "total_count": 0,
          "fundraisers": []
        },
        "additional_business_addresses": [],
        "allow_manage_memorialization": false,
        "auto_expand_chaining": false,
        "avatar_status": {
          "has_avatar": false
        },
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGneKg6pSsv4Qg7pwVFd2A1jgL9DsuaQgEdbjbK9MKw9-yW08e_q2Z9bZOCHtI_aem_zI9oSeb5u0ZObh5bAGNHbA&e=AT4Ck9_GTiCmO1JZP2xLCQxaxj4oht1PO5EDPq6r2QFry88mkfKrvTtDR7Py96w_rNHXwllaR4kzpeYeUYDg__7bfKTYy0VUoDpnZ88xPw",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGneKg6pSsv4Qg7pwVFd2A1jgL9DsuaQgEdbjbK9MKw9-yW08e_q2Z9bZOCHtI_aem_zI9oSeb5u0ZObh5bAGNHbA",
            "creation_source": "NONE"
          }
        ],
        "broadcast_chat_preference_status": {
          "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
          "is_broadcast_chat_creator": true,
          "notification_setting_type": 2
        },
        "can_use_branded_content_discovery_as_brand": false,
        "can_use_branded_content_discovery_as_creator": false,
        "can_use_paid_partnership_messaging_as_creator": false,
        "chaining_upsell_cards": [],
        "charity_profile_fundraiser_info": {
          "pk": 787132,
          "has_active_fundraiser": false,
          "is_facebook_onboarded_charity": false,
          "consumption_sheet_config": {
            "can_viewer_donate": false,
            "currency": null,
            "donation_disabled_message": null,
            "donation_url": null,
            "has_viewer_donated": null,
            "privacy_disclaimer": null,
            "profile_fundraiser_id": null,
            "you_donated_message": null,
            "donation_amount_config": {
              "default_selected_donation_value": null,
              "donation_amount_selector_values": [],
              "maximum_donation_amount": null,
              "minimum_donation_amount": null,
              "prefill_amount": null,
              "user_currency": null
            }
          }
        },
        "creator_shopping_info": {
          "linked_merchant_accounts": []
        },
        "follow_friction_type": 0,
        "has_active_charity_business_profile_fundraiser": false,
        "has_chaining": true,
        "has_collab_collections": false,
        "has_exclusive_feed_content": false,
        "instagram_pk": "787132",
        "is_profile_search_enabled": false,
        "is_eligible_for_diverse_owned_business_info": false,
        "is_eligible_for_meta_verified_links_in_post": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
        "is_eligible_for_meta_verified_multiple_addresses_creation": false,
        "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
        "is_eligible_for_meta_verified_related_accounts": false,
        "meta_verified_related_accounts_count": 0,
        "is_eligible_to_display_diverse_owned_business_info": false,
        "is_eligible_to_host_profile_reels_ads": false,
        "is_favorite_for_clips": false,
        "is_favorite_for_highlights": false,
        "is_in_canada": false,
        "is_interest_account": true,
        "is_memorialized": false,
        "is_potential_business": false,
        "is_regulated_news_in_viewer_location": false,
        "is_remix_setting_enabled_for_posts": true,
        "is_remix_setting_enabled_for_reels": true,
        "is_regulated_c18": false,
        "profile_overlay_info": {
          "overlay_format": "NONE",
          "bloks_payload": null
        },
        "is_stories_teaser_muted": false,
        "is_supervision_features_enabled": false,
        "is_whatsapp_linked": false,
        "media_count": 31529,
        "mutual_followers_count": 0,
        "nametag": {
          "available_theme_colors": [
            -1,
            7747834,
            13828293
          ],
          "background_image_url": "",
          "emoji": "😀",
          "emoji_color": 0,
          "gradient": 2,
          "is_background_image_blurred": false,
          "mode": 0,
          "selected_theme_color": -1,
          "selfie_sticker": 0,
          "selfie_url": "",
          "theme_color": {
            "available_theme_colors": [
              {
                "display_label": "Default",
                "int_value": -1
              },
              {
                "display_label": "Purple",
                "int_value": 7747834
              },
              {
                "display_label": "Lavender",
                "int_value": 13828293
              }
            ],
            "selected_theme_color": {
              "display_label": "Default",
              "int_value": -1
            }
          }
        },
        "not_meta_verified_friction_info": {
          "label_friction_content": "Not Meta Verified",
          "is_eligible_for_label_friction": false
        },
        "open_external_url_with_in_app_browser": true,
        "pinned_channels_info": {
          "has_public_channels": false,
          "pinned_channels_list": []
        },
        "profile_context_facepile_users": [],
        "profile_context_links_with_user_ids": [],
        "profile_pic_genai_tool_info": [],
        "pronouns": [],
        "relevant_news_regulation_locations": [],
        "remove_message_entrypoint": false,
        "request_contact_enabled": false,
        "show_blue_badge_on_main_profile": true,
        "show_ig_app_switcher_badge": true,
        "disable_profile_shop_cta": false,
        "show_text_post_app_badge": true,
        "show_text_post_app_switcher_badge": true,
        "spam_follower_setting_enabled": true,
        "total_ar_effects": 0,
        "total_clips_count": 1,
        "upcoming_events": [],
        "whatsapp_number": "",
        "recs_from_friends": {
          "enable_recs_from_friends": false,
          "recs_from_friends_entry_point_type": "banner"
        },
        "adjusted_banners_order": [],
        "has_visible_media_notes": true,
        "is_open_to_collab": false,
        "is_daily_limit_blocking": false,
        "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF0hfXLXamLyFGerggX7SMAyKaVEDq3IlFqQSqY02GVqNQ",
        "is_oregon_custom_gender_consented": false,
        "profile_reels_sorting_eligibility": "DISABLED",
        "nonpro_can_maybe_see_profile_hypercard": false,
        "should_show_tagged_tab": true,
        "posts_subscription_status": "default",
        "reels_subscription_status": "default",
        "stories_subscription_status": "default",
        "is_profile_wa_calling_enabled": false,
        "wa_calling_option_for_wa_linked": 0,
        "wa_calling_option_for_legacy_num": 0,
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
        "has_private_collections": true,
        "is_guardian_r_account_cannes_pair": false,
        "can_see_support_inbox": null,
        "has_fan_club_subscriptions": false,
        "show_wa_link_on_profile": false,
        "meta_verified_benefits_info": {
          "active_meta_verified_benefits": [],
          "is_eligible_for_meta_verified_content_protection": false,
          "is_eligible_for_ig_meta_verified_label": false
        },
        "existing_user_age_collection_enabled": true,
        "has_public_tab_threads": true,
        "is_eligible_for_meta_verified_label": true,
        "is_favorite_for_stories": false,
        "is_parenting_account": false,
        "show_post_insights_entry_point": true,
        "short_drama_creator": null,
        "short_drama_series_playlist_id": null,
        "short_drama_series_episode_count": null,
        "short_drama_series_seed_media_id": null,
        "short_drama_series_title": null,
        "short_drama_role": "NONE",
        "short_drama_series_profiles": [],
        "short_drama_producer_account": null,
        "moonshot_joiner_number": null,
        "is_creator_marketplace_badge_visible": false,
        "creator_marketplace_accounts_reached_metric": null,
        "school_affiliated_account_viewer_status": null,
        "qa_freeform_banner": null,
        "qa_freeform_banner_available_prompts": [
          {
            "prompt": "CURRENT_OBSESSION",
            "display_text": "Current obsession"
          },
          {
            "prompt": "DREAM_DESTINATION",
            "display_text": "Dream destination"
          },
          {
            "prompt": "PLAYING",
            "display_text": "Playing"
          }
        ],
        "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
        "can_message_pinned_carrera_interest_owner": true
      },
      "status": "ok"
    }
  ]
}
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
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gES6tqqzCj2JSr3Ia1E4y2K7YgN4Xx0pQiyJ4lxy6PJWXxBQJttOivQ3u7Llxl5ADg&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=goCIu4Ngux6ab7UGmwFfPw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2oumKXcRq4EXrxl2m2309EIrrL7l9FeY8rc3otKiOukg&oe=69DC51E9&_nc_sid=164c1d"
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
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gES6tqqzCj2JSr3Ia1E4y2K7YgN4Xx0pQiyJ4lxy6PJWXxBQJttOivQ3u7Llxl5ADg&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=goCIu4Ngux6ab7UGmwFfPw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2oumKXcRq4EXrxl2m2309EIrrL7l9FeY8rc3otKiOukg&oe=69DC51E9&_nc_sid=164c1d",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGna9ZA-PNyvtS9rka3df1MG_Xj5RyBKnWMbFcaCkxpqp-VMgtbOwA01D4DkD4_aem_bZ-9QLsaW3IK1aAClYhHDw&e=AT5ta79-yW8tVkQ8wpyJZzsIL9RwewprpsNvC6XQIs9JIzMBbxNRET8BP-DUpmXMQ-8odNEtFCJYqoE12ROg9P24pUn_ZVYHlS9EH_aHqQ",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGna9ZA-PNyvtS9rka3df1MG_Xj5RyBKnWMbFcaCkxpqp-VMgtbOwA01D4DkD4_aem_bZ-9QLsaW3IK1aAClYhHDw",
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
        "full_name": "National Geographic",
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "is_private": false,
        "username": "natgeo",
        "following_count": 193,
        "follower_count": 274984769
      },
      "status": "ok"
    },
    {
      "user": {
        "strong_id__": "787132",
        "id": "787132",
        "fbid_v2": 17841400573960012,
        "pk_id": "787132",
        "pk": 787132,
        "eligible_for_text_app_activation_badge": false,
        "feed_post_reshare_disabled": false,
        "has_ever_selected_topics": false,
        "has_nme_badge": false,
        "third_party_downloads_enabled": 2,
        "show_fb_link_on_profile": false,
        "show_fb_page_link_on_profile": false,
        "can_hide_category": true,
        "can_hide_public_contacts": true,
        "is_opal_enabled": false,
        "primary_profile_link_type": 0,
        "is_recon_ad_cta_on_profile_eligible_with_viewer": true,
        "account_type": 2,
        "highlights_tray_type": "DEFAULT",
        "current_catalog_id": null,
        "mini_shop_seller_onboarding_status": null,
        "ads_incentive_expiration_date": null,
        "ads_page_id": null,
        "ads_page_name": null,
        "account_category": "",
        "can_add_fb_group_link_on_profile": false,
        "can_use_affiliate_partnership_messaging_as_creator": false,
        "can_use_affiliate_partnership_messaging_as_brand": false,
        "has_gen_ai_personas_for_profile_banner": false,
        "has_guides": false,
        "highlight_reshare_disabled": false,
        "include_direct_blacklist_status": true,
        "is_direct_roll_call_enabled": true,
        "is_eligible_for_meta_verified_links_in_reels": false,
        "is_eligible_for_post_boost_mv_upsell": false,
        "is_meta_verified_related_accounts_display_enabled": false,
        "is_new_to_instagram": false,
        "is_profile_broadcast_sharing_enabled": true,
        "is_secondary_account_creation": false,
        "profile_type": 0,
        "is_coppa_enforced": false,
        "is_auto_confirm_enabled_for_all_reciprocal_follow_requests": false,
        "views_on_grid_status": "SHOW_VIEWS_ON_GRID",
        "is_bestie": false,
        "latest_reel_media": 1775659002,
        "latest_besties_reel_media": 0,
        "is_ring_creator": false,
        "account_badges": [],
        "has_highlight_reels": true,
        "is_creator_agent_enabled": false,
        "is_private": false,
        "interop_messaging_user_fbid": 113671860027320,
        "is_verified": true,
        "profile_pic_id": "3865702555259028436_787132",
        "has_anonymous_profile_picture": false,
        "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gES6tqqzCj2JSr3Ia1E4y2K7YgN4Xx0pQiyJ4lxy6PJWXxBQJttOivQ3u7Llxl5ADg&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=goCIu4Ngux6ab7UGmwFfPw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB1501500j-ccb7-5&oh=00_Af2oumKXcRq4EXrxl2m2309EIrrL7l9FeY8rc3otKiOukg&oe=69DC51E9&_nc_sid=164c1d",
        "username": "natgeo",
        "full_name": "National Geographic",
        "fan_club_info": {
          "autosave_to_exclusive_highlight": null,
          "connected_member_count": null,
          "fan_club_id": null,
          "fan_club_name": null,
          "has_created_ssc": null,
          "has_enough_subscribers_for_ssc": null,
          "is_fan_club_gifting_eligible": null,
          "is_fan_club_referral_eligible": null,
          "is_free_trial_eligible": null,
          "largest_public_bc_id": null,
          "subscriber_count": null,
          "should_show_playlists_in_profile_tab": null,
          "fan_consideration_page_revamp_eligiblity": null
        },
        "hd_profile_pic_url_info": {
          "height": 1080,
          "url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGA17YsNr19igBwbXq9srXUBvIgjtdkd30j46aIUExoR60rB7xDziHZstcezWGZdXA&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=goCIu4Ngux6ab7UGmwFfPw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB0j-ccb7-5&oh=00_Af2gtn8hh8mj-3UCJN6q3R6eih21BENJMYvXmFf5My8W8A&oe=69DC51E9&_nc_sid=164c1d",
          "width": 1080
        },
        "hd_profile_pic_versions": [
          {
            "height": 320,
            "url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGA17YsNr19igBwbXq9srXUBvIgjtdkd30j46aIUExoR60rB7xDziHZstcezWGZdXA&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=goCIu4Ngux6ab7UGmwFfPw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB3203200j-ccb7-5&oh=00_Af2qBFdBpDTTx1mPUvKPh7jFP5BlXvTt0OVGUL3NEy-nRA&oe=69DC51E9&_nc_sid=164c1d",
            "width": 320
          },
          {
            "height": 640,
            "url": "https://scontent-atl3-1.cdninstagram.com/v/t51.82787-19/658394700_18646025323019133_1238097625523693065_n.jpg?stp=dst-jpg_s640x640_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGA17YsNr19igBwbXq9srXUBvIgjtdkd30j46aIUExoR60rB7xDziHZstcezWGZdXA&_nc_ohc=XbeNvhLXv28Q7kNvwFZ1DtU&_nc_gid=goCIu4Ngux6ab7UGmwFfPw&edm=AO4kU9EBAAAA&ccb=7-5&ig_cache_key=GExOPid9_9kTdj5CAAkmmA47my4RbmNDAQAB6406400j-ccb7-5&oh=00_Af1yzk-dKpCsVfplcvzyz3IL19CPbbxUunXxQ-PjlpUZkA&oe=69DC51E9&_nc_sid=164c1d",
            "width": 640
          }
        ],
        "is_active_on_text_post_app": true,
        "is_cannes": false,
        "is_facebook_onboarded_charity": false,
        "is_favorite": false,
        "show_account_transparency_details": true,
        "transparency_product_enabled": false,
        "text_app_last_visited_time": null,
        "text_post_app_joiner_number": 672534,
        "follower_count": 274984769,
        "following_count": 193,
        "is_eligible_for_slide": false,
        "live_subscription_status": "default",
        "business_contact_method": "UNKNOWN",
        "category_id": "0",
        "city_id": "0",
        "city_name": "",
        "direct_messaging": "UNKNOWN",
        "instagram_location_id": "",
        "page_id": null,
        "public_email": "",
        "public_phone_country_code": "",
        "public_phone_number": "",
        "should_show_category": false,
        "should_show_public_contacts": true,
        "zip": "",
        "biography": "Step into wonder and find your inner explorer with National Geographic 🌎",
        "biography_with_entities": {
          "raw_text": "Step into wonder and find your inner explorer with National Geographic 🌎",
          "entities": []
        },
        "contact_phone_number": "",
        "has_music_on_profile": false,
        "has_videos": true,
        "has_views_fetching": true,
        "is_call_to_action_enabled": false,
        "is_category_tappable": false,
        "is_eligible_for_creator_product_links": false,
        "is_eligible_for_lead_center": true,
        "is_eligible_for_schools_search_upsell": false,
        "is_eligible_for_smb_support_flow": true,
        "lead_details_app_id": "com.bloks.www.ig.smb.lead_gen.subpage",
        "num_of_admined_pages": null,
        "page_name": "National Geographic",
        "professional_conversion_suggested_account_type": 3,
        "profile_context": "",
        "smb_support_partner": null,
        "ring_creator_metadata": {},
        "text_post_app_joiner_number_label": "672,534",
        "is_onboarding_account": false,
        "recon_features": {
          "enable_recon_cta": true
        },
        "text_post_app_badge_label": "natgeo",
        "is_business": true,
        "is_prime_onboarding_account": false,
        "is_profile_picture_expansion_enabled": true,
        "show_all_highlights_as_selected_in_management_screen": false,
        "show_schools_badge": null,
        "text_post_new_post_count": 5,
        "trial_clips_enabled": false,
        "enable_add_school_in_edit_profile": false,
        "shopping_post_onboard_nux_type": null,
        "fb_page_call_to_action_id": "",
        "address_street": "",
        "is_profile_audio_call_enabled": false,
        "displayed_action_button_partner": null,
        "smb_delivery_partner": null,
        "smb_support_delivery_partner": null,
        "displayed_action_button_type": null,
        "category": "",
        "external_lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGn1R0N0CxDnxaGKKBBM9yuEiA_R_qcqEpEk6DTFUuUgAQT1Suby9lFK008Pwg_aem_zWW-ZRQm09PdPJkSnboL1A&e=AT65WnVpggEK-mG9yl6iyelo_MNK38BuUaGiZj9aGsizw5E6iXDuDp1gfIMUv3qyHzp_8m1mN37SFd8P3yg54P201cokEsLymXB5H4u93w",
        "external_url": "http://visitstore.bio/natgeo",
        "active_standalone_fundraisers": {
          "total_count": 0,
          "fundraisers": []
        },
        "additional_business_addresses": [],
        "allow_manage_memorialization": false,
        "auto_expand_chaining": false,
        "avatar_status": {
          "has_avatar": false
        },
        "bio_links": [
          {
            "link_id": 17954981494900183,
            "url": "http://visitstore.bio/natgeo",
            "lynx_url": "https://l.instagram.com/?u=http%3A%2F%2Fvisitstore.bio%2Fnatgeo%3Futm_source%3Dig%26utm_medium%3Dsocial%26utm_content%3Dlink_in_bio%26fbclid%3DPAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGna9ZA-PNyvtS9rka3df1MG_Xj5RyBKnWMbFcaCkxpqp-VMgtbOwA01D4DkD4_aem_bZ-9QLsaW3IK1aAClYhHDw&e=AT5ta79-yW8tVkQ8wpyJZzsIL9RwewprpsNvC6XQIs9JIzMBbxNRET8BP-DUpmXMQ-8odNEtFCJYqoE12ROg9P24pUn_ZVYHlS9EH_aHqQ",
            "link_type": "external",
            "title": "",
            "media_type": "none",
            "image_url": "",
            "icon_url": "",
            "media_accent_color_hex": "",
            "is_pinned": false,
            "is_verified": false,
            "open_external_url_with_in_app_browser": true,
            "click_id": "PAZXh0bgNhZW0CMTEAc3J0YwZhcHBfaWQPNTY3MDY3MzQzMzUyNDI3AAGna9ZA-PNyvtS9rka3df1MG_Xj5RyBKnWMbFcaCkxpqp-VMgtbOwA01D4DkD4_aem_bZ-9QLsaW3IK1aAClYhHDw",
            "creation_source": "NONE"
          }
        ],
        "broadcast_chat_preference_status": {
          "json_response": "{\"status\":\"ok\",\"status_code\":\"200\",\"is_broadcast_chat_creator\":true,\"notification_setting_type\":2}",
          "is_broadcast_chat_creator": true,
          "notification_setting_type": 2
        },
        "can_use_branded_content_discovery_as_brand": false,
        "can_use_branded_content_discovery_as_creator": false,
        "can_use_paid_partnership_messaging_as_creator": false,
        "chaining_upsell_cards": [],
        "charity_profile_fundraiser_info": {
          "pk": 787132,
          "has_active_fundraiser": false,
          "is_facebook_onboarded_charity": false,
          "consumption_sheet_config": {
            "can_viewer_donate": false,
            "currency": null,
            "donation_disabled_message": null,
            "donation_url": null,
            "has_viewer_donated": null,
            "privacy_disclaimer": null,
            "profile_fundraiser_id": null,
            "you_donated_message": null,
            "donation_amount_config": {
              "default_selected_donation_value": null,
              "donation_amount_selector_values": [],
              "maximum_donation_amount": null,
              "minimum_donation_amount": null,
              "prefill_amount": null,
              "user_currency": null
            }
          }
        },
        "follow_friction_type": 0,
        "has_active_charity_business_profile_fundraiser": false,
        "has_chaining": false,
        "has_collab_collections": false,
        "has_exclusive_feed_content": false,
        "instagram_pk": "787132",
        "is_profile_search_enabled": false,
        "is_eligible_for_diverse_owned_business_info": false,
        "is_eligible_for_meta_verified_links_in_post": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet": false,
        "is_eligible_for_meta_verified_enhanced_link_sheet_consumption": false,
        "is_eligible_for_meta_verified_multiple_addresses_creation": false,
        "is_eligible_for_meta_verified_multiple_addresses_consumption": false,
        "is_eligible_for_meta_verified_related_accounts": false,
        "meta_verified_related_accounts_count": 0,
        "is_eligible_to_display_diverse_owned_business_info": false,
        "is_eligible_to_host_profile_reels_ads": false,
        "is_favorite_for_clips": false,
        "is_favorite_for_highlights": false,
        "is_in_canada": false,
        "is_interest_account": true,
        "is_memorialized": false,
        "is_potential_business": false,
        "is_regulated_news_in_viewer_location": false,
        "is_remix_setting_enabled_for_posts": true,
        "is_remix_setting_enabled_for_reels": true,
        "is_regulated_c18": false,
        "profile_overlay_info": {
          "overlay_format": "NONE",
          "bloks_payload": null
        },
        "is_stories_teaser_muted": false,
        "is_supervision_features_enabled": false,
        "is_whatsapp_linked": false,
        "media_count": 31529,
        "mutual_followers_count": 0,
        "nametag": {
          "available_theme_colors": [
            -1,
            7747834,
            13828293
          ],
          "background_image_url": "",
          "emoji": "😀",
          "emoji_color": 0,
          "gradient": 2,
          "is_background_image_blurred": false,
          "mode": 0,
          "selected_theme_color": -1,
          "selfie_sticker": 0,
          "selfie_url": "",
          "theme_color": {
            "available_theme_colors": [
              {
                "display_label": "Default",
                "int_value": -1
              },
              {
                "display_label": "Purple",
                "int_value": 7747834
              },
              {
                "display_label": "Lavender",
                "int_value": 13828293
              }
            ],
            "selected_theme_color": {
              "display_label": "Default",
              "int_value": -1
            }
          }
        },
        "not_meta_verified_friction_info": {
          "label_friction_content": "Not Meta Verified",
          "is_eligible_for_label_friction": false
        },
        "open_external_url_with_in_app_browser": true,
        "pinned_channels_info": {
          "has_public_channels": false,
          "pinned_channels_list": []
        },
        "profile_context_facepile_users": [],
        "profile_context_links_with_user_ids": [],
        "profile_pic_genai_tool_info": [],
        "pronouns": [],
        "relevant_news_regulation_locations": [],
        "remove_message_entrypoint": false,
        "request_contact_enabled": false,
        "show_blue_badge_on_main_profile": true,
        "show_ig_app_switcher_badge": true,
        "disable_profile_shop_cta": true,
        "show_text_post_app_badge": true,
        "show_text_post_app_switcher_badge": true,
        "spam_follower_setting_enabled": true,
        "total_ar_effects": 0,
        "total_clips_count": 1,
        "upcoming_events": [],
        "whatsapp_number": "",
        "recs_from_friends": {
          "enable_recs_from_friends": false,
          "recs_from_friends_entry_point_type": "banner"
        },
        "adjusted_banners_order": [],
        "has_visible_media_notes": true,
        "is_open_to_collab": false,
        "is_daily_limit_blocking": false,
        "threads_profile_glyph_url": "barcelona://user?username=natgeo&xmt=AQF0kzVh9e6hZ90SYrh93jy5vcYHyDgiLrOQDcV-e4_e2qs",
        "is_oregon_custom_gender_consented": false,
        "profile_reels_sorting_eligibility": "CHECK_VIEWER_QE",
        "nonpro_can_maybe_see_profile_hypercard": false,
        "should_show_tagged_tab": true,
        "posts_subscription_status": "default",
        "reels_subscription_status": "default",
        "stories_subscription_status": "default",
        "is_profile_wa_calling_enabled": false,
        "wa_calling_option_for_wa_linked": 0,
        "wa_calling_option_for_legacy_num": 0,
        "birthday_today_visibility_for_viewer": "NOT_VISIBLE",
        "is_eligible_for_meta_verified_ig_self_profile_not_verified_badge": false,
        "has_private_collections": true,
        "is_guardian_r_account_cannes_pair": false,
        "can_see_support_inbox": null,
        "has_fan_club_subscriptions": false,
        "show_wa_link_on_profile": false,
        "meta_verified_benefits_info": {
          "active_meta_verified_benefits": [],
          "is_eligible_for_meta_verified_content_protection": false,
          "is_eligible_for_ig_meta_verified_label": false
        },
        "existing_user_age_collection_enabled": true,
        "has_public_tab_threads": true,
        "is_eligible_for_meta_verified_label": true,
        "is_favorite_for_stories": false,
        "is_parenting_account": false,
        "show_post_insights_entry_point": true,
        "short_drama_creator": null,
        "short_drama_series_playlist_id": null,
        "short_drama_series_episode_count": null,
        "short_drama_series_seed_media_id": null,
        "short_drama_series_title": null,
        "short_drama_role": "NONE",
        "short_drama_series_profiles": [],
        "short_drama_producer_account": null,
        "moonshot_joiner_number": null,
        "is_creator_marketplace_badge_visible": false,
        "creator_marketplace_accounts_reached_metric": null,
        "school_affiliated_account_viewer_status": null,
        "qa_freeform_banner": null,
        "qa_freeform_banner_available_prompts": [
          {
            "prompt": "CURRENT_OBSESSION",
            "display_text": "Current obsession"
          },
          {
            "prompt": "DREAM_DESTINATION",
            "display_text": "Dream destination"
          },
          {
            "prompt": "PLAYING",
            "display_text": "Playing"
          }
        ],
        "qa_freeform_banner_transparency": "The banner is visible to everyone on and off Instagram.",
        "can_message_pinned_carrera_interest_owner": true
      },
      "status": "ok"
    }
  ]
}
```

</details>

---

**Ready to integrate?** First 100 requests free — [Get your API key →](https://hikerapi.com/p/7it8oc2i?utm_source=docs&utm_medium=cta&utm_content=api-v2-user){ target=_blank }
