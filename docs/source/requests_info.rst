Requests Information
===================================

Each client request to our API may include several internal service calls. The total number of spent request units is returned in the response header:

.. code-block:: text

   x-hiker-info: reqs=<number>

Most requests to the API are counted as a single request. However, some complex operations (such as searching for a user by name or ID, where the system first performs an internal request to convert identifiers, checking privacy settings, and other compound operations) require more resources and may involve multiple internal requests. Details of the number of queries used by different endpoints are summarized in the table below.

Note: The "performs privacy checks" step specifically identifies **PrivateAccount** status, which is handled separately from shadow-banned, deleted or suspended accounts in our API logic.

.. list-table::
   :header-rows: 1
   :widths: 20 5 75

   * - Path
     - Reqs
     - Description
   * - `/v1/user/highlights`
     - 2
     - | Gets highlights by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 1 req).
   * - `/v2/user/highlights`
     - 2
     - | Gets highlights by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 1 req).
   * - `/v1/user/highlights/by/username`
     - 3
     - | Performs ID search by username + gets highlights by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 2 req).
   * - `/v2/user/highlights/by/username`
     - 3
     - | Performs ID search by username + gets highlights by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 2 req).
   * - `/v1/user/stories`
     - 2
     - | Gets stories by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 1 req).
   * - `/v2/user/stories`
     - 2
     - | Gets stories by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 1 req).
   * - `/v1/user/stories/by/username`
     - 3
     - | Performs ID search by username + gets stories by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 2 req).
   * - `/v2/user/stories/by/username`
     - 3
     - | Performs ID search by username + gets stories by ID + performs privacy checks.
       |
       | **Force mode (force: "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 2 req).
   * - `/v1/user/search/followers`
     - 2
     - | Gets followers by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 1 req).
   * - `/v1/user/search/following`
     - 2
     - | Gets following by ID + performs privacy checks.
       |
       | **With parameter ("force": "on")**:
       | Skips privacy checks and reduces reqs (total reqs in this mode is 1 req).
   * - `/a2/user`
     - 2
     - Gets profile data + media.
   * - `/v2/user/explore/businesses/by/id`
     - 2
     - Gets business recommendations by user ID + account details.
