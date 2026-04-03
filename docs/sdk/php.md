# PHP SDK

Official PHP client for HikerAPI.

## Installation

```bash
composer require hikerapi/hikerapi-php
```

## Quick start

```php
use HikerAPI\Client;

$client = new Client('YOUR_TOKEN');

$user = $client->v1->userByUsername('ronaldo');
echo $user['follower_count'];

$followers = $client->v2->userFollowers('173560420');
```

## Without SDK

```php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,
    'https://api.hikerapi.com/v1/user/by/username?username=ronaldo');
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'x-access-key: YOUR_TOKEN',
    'accept: application/json',
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = json_decode(curl_exec($ch), true);
curl_close($ch);
```

See [API Reference](../api-reference/v1/index.md) for all endpoints.
