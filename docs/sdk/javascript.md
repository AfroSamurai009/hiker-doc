# JavaScript SDK

Official Node.js client for HikerAPI.

## Installation

```bash
npm install hikerapi
```

## Quick start

```javascript
import { Client } from "hikerapi";

const client = new Client({ token: "YOUR_TOKEN" });

// Get user profile
const user = await client.v1.userByUsername("ronaldo");
console.log(user.follower_count);

// Get followers
const { users, nextPageId } = await client.v2.userFollowers("173560420");
```

## Pagination

```javascript
let pageId = "";
const allFollowers = [];

while (true) {
  const { response, next_page_id } = await client.v2.userFollowers(
    "173560420",
    { page_id: pageId }
  );
  allFollowers.push(...response.users);
  if (!next_page_id) break;
  pageId = next_page_id;
}
```

## Without SDK

```javascript
const headers = { "x-access-key": "YOUR_TOKEN" };

const response = await fetch(
  "https://api.hikerapi.com/v1/user/by/username?username=ronaldo",
  { headers }
);
const user = await response.json();
```

See [API Reference](../api-reference/v1/index.md) for all endpoints.
