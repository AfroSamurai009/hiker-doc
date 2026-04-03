# Go SDK

Official Go client for HikerAPI.

## Installation

```bash
go get github.com/hikerapi/hikerapi-go
```

## Quick start

```go
package main

import (
    "fmt"
    "github.com/hikerapi/hikerapi-go"
)

func main() {
    client := hikerapi.NewClient("YOUR_TOKEN")

    user, err := client.V1.UserByUsername("ronaldo")
    if err != nil {
        panic(err)
    }
    fmt.Println(user.FollowerCount)
}
```

## Without SDK

```go
req, _ := http.NewRequest("GET",
    "https://api.hikerapi.com/v1/user/by/username?username=ronaldo", nil)
req.Header.Set("x-access-key", "YOUR_TOKEN")

resp, _ := http.DefaultClient.Do(req)
```

See [API Reference](../api-reference/rest-v1.md) for all endpoints.
