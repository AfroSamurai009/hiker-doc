Timeout Information
===================================

.. container:: note

    We would like to draw your attention to important aspects of working with our API so that you can effectively use its capabilities and avoid possible problems. By default, the volume of requests is limited to 1 million requests per day,  which is equivalent to about 11 requests per second. This limit is introduced to ensure stable operation of the service for all users.

    If you exceed the limit of 11 requests per second, the server will return error 429 (Too Many Requests) and your request will be rejected. To avoid such situations, it is important to monitor the frequency of requests and regulate the number of requests.

    For optimal performance with the API, we recommend keeping an eye on the frequency of requests. Make sure you send no more than 11 requests per second. You can use semaphores to limit the number of simultaneous requests and add delays  between requests using await asyncio.sleep(1 / 11). This will help to evenly distribute the load and avoid errors.

    If you do get error 429, pause before resending the request. For example, wait 1-2 seconds and try again. This will allow you to continue without a long downtime.

    Here is a code example that helps you to respect the request limit:

.. code-block:: python

    import asyncio
    import aiohttp

    users_ids = [
        "1553030189",
        "12345",
        "4238157586",
        "57606704380",
        "44207170437",
        "58568300401",
        "47857986514",
        "419762293",
        "11461087642",
        "5310983422",
        "25044994947",
        "25044994947",
        "6882128701",
        "37452706560",
        "420842043",
        "1220781192",
        "6388630183",
        "1320664128",
        "6438020799",
        "52027596085",
    ]

    rate_limit = 11
    url = "https://api.hikerapi.com/v2/user/followers"
    headers = {
        "x-access-key": "<your_token_here>",
        "accept": "application/json",
    }

    all_followers = []


    async def get_followers(user_id):
        semaphore = asyncio.Semaphore(rate_limit)
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                params = {"user_id": user_id, "page_id": ""}
                followers = []

                while True:
                    try:
                        async with session.get(
                            url=url, params=params, headers=headers
                        ) as response:
                            res = await response.json()
                            if "response" not in res:
                                print(
                                    "Error in response for user_id=%s: %s" % (user_id, res)
                                )
                                break
                            users, page_id = res["response"]["users"], res["next_page_id"]
                            followers.extend(users)

                            if not page_id:
                                break

                            params["page_id"] = page_id
                            await asyncio.sleep(1 / rate_limit)
                    except Exception as e:
                        print("Error in response for user_id=%s: %s" % (user_id, e))
                        break
        return followers


    async def main():
        tasks = [asyncio.create_task(get_followers(user_id)) for user_id in users_ids]
        results = await asyncio.gather(*tasks)
        all_followers.extend(result for result in results)


    asyncio.run(main())
