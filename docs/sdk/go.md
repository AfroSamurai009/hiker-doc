# Go

!!! info "SDK coming soon"
    The official Go SDK is under development. In the meantime, you can use the REST API directly — see examples below.

    Need it sooner? [Contact us](../support/contacts.md) and we'll prioritize it.

## Using the API with Go

```go
package main

import (
    "encoding/json"
    "fmt"
    "io"
    "net/http"
)

func main() {
    req, _ := http.NewRequest("GET",
        "https://api.hikerapi.com/v1/user/by/username?username=ronaldo", nil)
    req.Header.Set("x-access-key", "YOUR_TOKEN")
    req.Header.Set("accept", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    body, _ := io.ReadAll(resp.Body)

    var user map[string]interface{}
    json.Unmarshal(body, &user)
    fmt.Printf("Username: %s, Followers: %v\n",
        user["username"], user["follower_count"])
}
```

## Pagination example

```go
func getFollowers(userID, token string) ([]map[string]interface{}, error) {
    var allFollowers []map[string]interface{}
    endCursor := ""

    for {
        url := fmt.Sprintf(
            "https://api.hikerapi.com/gql/user/followers/chunk?user_id=%s&end_cursor=%s",
            userID, endCursor)

        req, _ := http.NewRequest("GET", url, nil)
        req.Header.Set("x-access-key", token)

        resp, err := http.DefaultClient.Do(req)
        if err != nil {
            return nil, err
        }

        body, _ := io.ReadAll(resp.Body)
        resp.Body.Close()

        var result []interface{}
        json.Unmarshal(body, &result)

        // result[0] = users list, result[1] = end_cursor
        users := result[0].([]interface{})
        for _, u := range users {
            allFollowers = append(allFollowers, u.(map[string]interface{}))
        }

        cursor, ok := result[1].(string)
        if !ok || cursor == "" {
            break
        }
        endCursor = cursor
    }

    return allFollowers, nil
}
```

See [API Reference](../api-reference/v1/index.md) for all endpoints.
