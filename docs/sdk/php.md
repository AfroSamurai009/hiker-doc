# PHP

!!! info "SDK coming soon"
    The official PHP SDK is under development. In the meantime, you can use the REST API directly — see examples below.

    Need it sooner? [Contact us](../support/contacts.md) and we'll prioritize it.

## Using the API with PHP

```php
<?php

$token = "YOUR_TOKEN";

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => "https://api.hikerapi.com/v1/user/by/username?username=ronaldo",
    CURLOPT_HTTPHEADER => [
        "x-access-key: $token",
        "accept: application/json",
    ],
    CURLOPT_RETURNTRANSFER => true,
]);

$response = json_decode(curl_exec($ch), true);
curl_close($ch);

echo "Username: " . $response["username"] . "\n";
echo "Followers: " . $response["follower_count"] . "\n";
```

## Pagination example

```php
<?php

function getFollowers(string $userId, string $token): array {
    $allFollowers = [];
    $endCursor = "";

    while (true) {
        $url = "https://api.hikerapi.com/gql/user/followers/chunk?"
            . http_build_query(["user_id" => $userId, "end_cursor" => $endCursor]);

        $ch = curl_init();
        curl_setopt_array($ch, [
            CURLOPT_URL => $url,
            CURLOPT_HTTPHEADER => [
                "x-access-key: $token",
                "accept: application/json",
            ],
            CURLOPT_RETURNTRANSFER => true,
        ]);

        $result = json_decode(curl_exec($ch), true);
        curl_close($ch);

        // result[0] = users list, result[1] = end_cursor
        $allFollowers = array_merge($allFollowers, $result[0]);

        if (empty($result[1])) {
            break;
        }
        $endCursor = $result[1];
    }

    return $allFollowers;
}

$followers = getFollowers("173560420", "YOUR_TOKEN");
echo "Got " . count($followers) . " followers\n";
```

## Using Guzzle

```php
<?php

use GuzzleHttp\Client;

$client = new Client([
    "base_uri" => "https://api.hikerapi.com",
    "headers" => [
        "x-access-key" => "YOUR_TOKEN",
        "accept" => "application/json",
    ],
]);

$response = $client->get("/v1/user/by/username", [
    "query" => ["username" => "ronaldo"],
]);

$user = json_decode($response->getBody(), true);
echo $user["follower_count"];
```

See [API Reference](../api-reference/v1/index.md) for all endpoints.
