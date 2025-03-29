Timeout Information
===================================

.. container:: note

    We would like to draw your attention to important aspects of working with our API so that you can effectively use its capabilities and avoid possible problems. By default, the volume of requests is limited to 1 million requests per day,  which is equivalent to about 11 requests per second. This limit is introduced to ensure stable operation of the service for all users.

    If you exceed the limit of 11 requests per second, the server will return error 429 (Too Many Requests) and your request will be rejected. To avoid such situations, it is important to monitor the frequency of requests and regulate the number of requests.

    For optimal performance with the API, we recommend keeping an eye on the frequency of requests. Make sure you send no more than 11 requests per second. You can use semaphores to limit the number of simultaneous requests and add delays  between requests using await asyncio.sleep(1 / 11). This will help to evenly distribute the load and avoid errors.

    If you do get error 429, pause before resending the request. For example, wait 1-2 seconds and try again. This will allow you to continue without a long downtime.

    Here is a code example that helps you to respect the request limit:

.. code-block:: python

    import httpx
    import asyncio

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

    headers = {
        "x-access-key": "<your_token_here>",
        "accept": "application/json",
    }
    all_followers = []
    rate_limit = httpx.get(
        "https://api.hikerapi.com/sys/balance", headers=headers, params={}
    ).json()["rate"]
    semaphore = asyncio.Semaphore(rate_limit)


    async def get_followers(user_id):
        async with httpx.AsyncClient(timeout=20) as client:
            params = {"user_id": user_id, "page_id": "", "force": "on"}
            followers = []

            while True:
                async with semaphore:
                    try:
                        response = await client.get(
                            "https://api.hikerapi.com/v2/user/followers",
                            params=params,
                            headers=headers,
                        )
                        if response.status_code == 429:
                            print("Rate limit exceeded, waiting")
                            await asyncio.sleep(2)
                            continue
                        elif response.status_code == 402:
                            raise Exception("Insufficient balance")

                        res = response.json()
                        users, page_id = res["response"]["users"], res["next_page_id"]
                        followers.extend(users)

                        if not page_id:
                            break

                        params["page_id"] = page_id
                    except Exception as e:
                        print(f"Error in response for user_id={user_id}: {e}")
                        break
            return followers


    async def main():
        tasks = [asyncio.create_task(get_followers(user_id)) for user_id in users_ids]
        results = await asyncio.gather(*tasks)
        all_followers.extend(result for result in results)


    asyncio.run(main())
