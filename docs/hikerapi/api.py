from typing import Dict, List, Optional

from .base import BaseSyncClient


class Client(BaseSyncClient):
    def user_a1(self, username: str) -> Dict:
        '''User'''
        params = {"username": username}
        return self._request("get", "/a1/user", params=params)

    def media_a1(self, code: str) -> Dict:
        '''Media. Get media object'''
        params = {"code": code}
        return self._request("get", "/a1/media", params=params)

    def media_by_id_a1(self, id: int) -> Dict:
        '''Media By Id. Get media object'''
        params = {"id": id}
        return self._request("get", "/a1/media/by/id", params=params)

    def media_by_url_a1(self, url: str) -> Dict:
        '''Media By Url. Get media object'''
        params = {"url": url}
        return self._request("get", "/a1/media/by/url", params=params)

    def hashtag_a1(self, name: str) -> Dict:
        '''Hashtag. Get hashtag object'''
        params = {"name": name}
        return self._request("get", "/a1/hashtag", params=params)

    def location_a1(self, id: int) -> Dict:
        '''Location. Get location object'''
        params = {"id": id}
        return self._request("get", "/a1/location", params=params)

    def comments_chunk_gql(self, media_id: str, end_cursor: Optional[str] = None) -> Dict:
        '''Media Comments Chunk. Get comments on a media'''
        params = {"media_id": media_id, "end_cursor": end_cursor}
        return self._request("get", "/gql/comments/chunk", params=params)

    def comments_gql(self, media_id: str, amount: Optional[int] = None, max_requests: Optional[int] = None) -> Dict:
        '''May return fewer comments than there are if instagram limits the issue (use /gql/comments/chunk instead). Get comments on a media'''
        params = {"media_id": media_id, "amount": amount, "max_requests": max_requests}
        return self._request("get", "/gql/comments", params=params)

    def comments_threaded_chunk_gql(self, comment_id: str, end_cursor: Optional[str] = None) -> Dict:
        '''Media Comments Threaded Chunk. Get threaded comments for comment'''
        params = {"comment_id": comment_id, "end_cursor": end_cursor}
        return self._request("get", "/gql/comments/threaded/chunk", params=params)

    def comments_threaded_gql(self, comment_id: str, amount: Optional[int] = None) -> Dict:
        '''Media Comments Threaded. Get threaded comments for comment'''
        params = {"comment_id": comment_id, "amount": amount}
        return self._request("get", "/gql/comments/threaded", params=params)

    def comment_likers_chunk_gql(self, media_id: str, end_cursor: Optional[str] = None) -> Dict:
        '''Comment Likers Chunk. Get likers on a comment'''
        params = {"media_id": media_id, "end_cursor": end_cursor}
        return self._request("get", "/gql/comment/likers/chunk", params=params)

    def comment_likers_gql(self, media_id: str, amount: Optional[int] = None) -> Dict:
        '''Comment Likers. Get likers on a comment'''
        params = {"media_id": media_id, "amount": amount}
        return self._request("get", "/gql/comment/likers", params=params)

    def media_likers_chunk_gql(self, media_id: str, end_cursor: Optional[str] = None) -> Dict:
        '''Media Likers Chunk. Get likers on media (returns 50 users in one request)'''
        params = {"media_id": media_id, "end_cursor": end_cursor}
        return self._request("get", "/gql/media/likers/chunk", params=params)

    def media_likers_gql(self, media_id: str, amount: Optional[int] = None) -> Dict:
        '''Media Likers. Get likers on a media (for every 50 users an request will be made)'''
        params = {"media_id": media_id, "amount": amount}
        return self._request("get", "/gql/media/likers", params=params)

    def user_related_profiles_gql(self, id: str) -> Dict:
        '''Related Profiles. Get related profiles by user id'''
        params = {"id": id}
        return self._request("get", "/gql/user/related/profiles", params=params)

    def user_followers_gql(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''Get a user followers (one request is required for every 46 followers). Get followers users'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/gql/user/followers", params=params)

    def user_followers_chunk_gql(self, user_id: str, amount: Optional[int] = None, end_cursor: Optional[str] = None) -> Dict:
        '''Get a user followers (one request required). Get part (one page) of followers users with cursor'''
        params = {"user_id": user_id, "amount": amount, "end_cursor": end_cursor}
        return self._request("get", "/gql/user/followers/chunk", params=params)

    def user_following_gql(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''Get a user following (one request is required for every 46 following). Get following users'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/gql/user/following", params=params)

    def user_following_chunk_gql(self, user_id: str, amount: Optional[int] = None, end_cursor: Optional[str] = None) -> Dict:
        '''Get a user following (one request required). Get part (one page) of following users with cursor'''
        params = {"user_id": user_id, "amount": amount, "end_cursor": end_cursor}
        return self._request("get", "/gql/user/following/chunk", params=params)

    def user_by_id_v1(self, id: str) -> Dict:
        '''User By Id. Get user object by id'''
        params = {"id": id}
        return self._request("get", "/v1/user/by/id", params=params)

    def user_by_username_v1(self, username: str) -> Dict:
        '''Get user object by username (one request required). Get user object by username'''
        params = {"username": username}
        return self._request("get", "/v1/user/by/username", params=params)

    def user_by_url_v1(self, url: str) -> Dict:
        '''Get user object by URL (one request required). Get user object by URL'''
        params = {"url": url}
        return self._request("get", "/v1/user/by/url", params=params)

    def user_medias_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''Get user medias (one request is required for every 33 media). Get user medias'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/medias", params=params)

    def user_medias_chunk_v1(self, user_id: str, max_amount: Optional[int] = None, end_cursor: Optional[str] = None) -> Dict:
        '''User Medias Chunk. Get part of user medias with cursor'''
        params = {"user_id": user_id, "max_amount": max_amount, "end_cursor": end_cursor}
        return self._request("get", "/v1/user/medias/chunk", params=params)

    def user_medias_pinned_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''Get pinned medias. Get user medias'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/medias/pinned", params=params)

    def user_clips_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''Get user clips (one request is required for every 50 media). Get user clips'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/clips", params=params)

    def user_clips_chunk_v1(self, user_id: str, end_cursor: Optional[str] = None) -> Dict:
        '''User Clips Chunk. Get part of user clips with cursor (default 50 media per request)'''
        params = {"user_id": user_id, "end_cursor": end_cursor}
        return self._request("get", "/v1/user/clips/chunk", params=params)

    def user_videos_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''Get user videos (one request is required for every 50 media). Get user videos'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/videos", params=params)

    def user_videos_chunk_v1(self, user_id: str, max_amount: Optional[int] = None, end_cursor: Optional[str] = None) -> Dict:
        '''User Videos Chunk. Get part of user videos with cursor (default 50 media per request)'''
        params = {"user_id": user_id, "max_amount": max_amount, "end_cursor": end_cursor}
        return self._request("get", "/v1/user/videos/chunk", params=params)

    def user_tag_medias_chunk_v1(self, user_id: str, max_id: Optional[str] = None) -> Dict:
        '''Usertag Medias Chunk. Get usertag medias'''
        params = {"user_id": user_id, "max_id": max_id}
        return self._request("get", "/v1/user/tag/medias/chunk", params=params)

    def user_stories_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''User Stories. Get user stories'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/stories", params=params)

    def user_stories_by_username_v1(self, username: str, amount: Optional[int] = None) -> Dict:
        '''User Stories By Username. Get user stories'''
        params = {"username": username, "amount": amount}
        return self._request("get", "/v1/user/stories/by/username", params=params)

    def user_highlights_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''User Highlights. Get user highlights'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/highlights", params=params)

    def user_highlights_by_username_v1(self, username: str, amount: Optional[int] = None) -> Dict:
        '''User Highlights By Username. Get user highlights by username'''
        params = {"username": username, "amount": amount}
        return self._request("get", "/v1/user/highlights/by/username", params=params)

    def user_search_followers_v1(self, user_id: str, query: str) -> Dict:
        '''Search Followers. Search users by followers'''
        params = {"user_id": user_id, "query": query}
        return self._request("get", "/v1/user/search/followers", params=params)

    def user_search_following_v1(self, user_id: str, query: str) -> Dict:
        '''Search Following. Search users by following users'''
        params = {"user_id": user_id, "query": query}
        return self._request("get", "/v1/user/search/following", params=params)

    def user_following_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''User Following. Get following users'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/following", params=params)

    def user_following_chunk_v1(self, user_id: str, amount: Optional[int] = None, max_id: Optional[str] = None) -> Dict:
        '''Get a user following (one request required). Get part (one page) of following users with cursor'''
        params = {"user_id": user_id, "amount": amount, "max_id": max_id}
        return self._request("get", "/v1/user/following/chunk", params=params)

    def user_followers_v1(self, user_id: str, amount: Optional[int] = None) -> Dict:
        '''Get a user followers (one request is required for every 100-1000 followers). Get followers users'''
        params = {"user_id": user_id, "amount": amount}
        return self._request("get", "/v1/user/followers", params=params)

    def user_followers_chunk_v1(self, user_id: str, amount: Optional[int] = None, max_id: Optional[str] = None) -> Dict:
        '''Get a user followers (one request required). Get part (one page) of followers users with cursor'''
        params = {"user_id": user_id, "amount": amount, "max_id": max_id}
        return self._request("get", "/v1/user/followers/chunk", params=params)

    def user_web_profile_info_v1(self, username: str) -> Dict:
        '''Web Profile Info'''
        params = {"username": username}
        return self._request("get", "/v1/user/web_profile_info", params=params)

    def user_guides_v1(self, user_id: int) -> Dict:
        '''User Guides V1. Get user guides'''
        params = {"user_id": user_id}
        return self._request("get", "/v1/user/guides", params=params)

    def media_by_id_v1(self, id: str) -> Dict:
        '''Media By Id. Get media object'''
        params = {"id": id}
        return self._request("get", "/v1/media/by/id", params=params)

    def media_by_code_v1(self, code: str) -> Dict:
        '''Media By Code. Get media object'''
        params = {"code": code}
        return self._request("get", "/v1/media/by/code", params=params)

    def media_by_url_v1(self, url: str) -> Dict:
        '''Media By Url. Get media object'''
        params = {"url": url}
        return self._request("get", "/v1/media/by/url", params=params)

    def media_insight_v1(self, media_id: str) -> Dict:
        '''Insights Media. Get media insight'''
        params = {"media_id": media_id}
        return self._request("get", "/v1/media/insight", params=params)

    def media_comments_chunk_v1(self, id: str, min_id: Optional[str] = None, max_id: Optional[str] = None) -> Dict:
        '''Get media comments (one request return 20 comments). Get comments on a media'''
        params = {"id": id, "min_id": min_id, "max_id": max_id}
        return self._request("get", "/v1/media/comments/chunk", params=params)

    def media_likers_v1(self, id: str) -> Dict:
        '''Media Likers. Get user's likers'''
        params = {"id": id}
        return self._request("get", "/v1/media/likers", params=params)

    def media_user_v1(self, media_id: str) -> Dict:
        '''Media User. Get author of the media'''
        params = {"media_id": media_id}
        return self._request("get", "/v1/media/user", params=params)

    def media_oembed_v1(self, url: str) -> Dict:
        '''Media Oembed. Return info about media and user from post URL'''
        params = {"url": url}
        return self._request("get", "/v1/media/oembed", params=params)

    def media_download_photo_v1(self, id: str) -> Dict:
        '''Photo Download. Download photo using media pk'''
        params = {"id": id}
        return self._request("get", "/v1/media/download/photo", params=params)

    def media_download_photo_by_url_v1(self, url: str) -> Dict:
        '''Photo Download By Url. Download photo using URL'''
        params = {"url": url}
        return self._request("get", "/v1/media/download/photo/by/url", params=params)

    def media_download_video_v1(self, id: str) -> Dict:
        '''Video Download. Download video using media pk'''
        params = {"id": id}
        return self._request("get", "/v1/media/download/video", params=params)

    def media_download_video_by_url_v1(self, url: str) -> Dict:
        '''Video Download By Url. Download video using URL'''
        params = {"url": url}
        return self._request("get", "/v1/media/download/video/by/url", params=params)

    def media_code_from_pk_v1(self, pk: str) -> Dict:
        '''Media Code From Pk. Get media code from pk'''
        params = {"pk": pk}
        return self._request("get", "/v1/media/code/from/pk", params=params)

    def media_pk_from_code_v1(self, code: str) -> Dict:
        '''Media Pk From Code. Get media pk from code'''
        params = {"code": code}
        return self._request("get", "/v1/media/pk/from/code", params=params)

    def media_pk_from_url_v1(self, url: str) -> Dict:
        '''Media Pk From Url. Get Media pk from URL'''
        params = {"url": url}
        return self._request("get", "/v1/media/pk/from/url", params=params)

    def story_by_id_v1(self, id: int) -> Dict:
        '''Story By Id. Get story object by id'''
        params = {"id": id}
        return self._request("get", "/v1/story/by/id", params=params)

    def story_by_url_v1(self, url: str) -> Dict:
        '''Attention! To work with /s/ links, call /v1/share/by/url first. Get story object by id'''
        params = {"url": url}
        return self._request("get", "/v1/story/by/url", params=params)

    def story_download_v1(self, id: str) -> Dict:
        '''Story Download. Download story media by story id'''
        params = {"id": id}
        return self._request("get", "/v1/story/download", params=params)

    def story_download_by_url_v1(self, url: str) -> Dict:
        '''Download story file by URL to file. Download story file by URL to file (you can take it from "/v1/story/by/id" or "/v1/story/by/url")
        Example: https://scontent-lga3-1.cdninstagram.com/v/t66.30100-16/310890533_1622838408176007_5601749632271872566_n.mp4?efg=...'''
        params = {"url": url}
        return self._request("get", "/v1/story/download/by/url", params=params)

    def story_download_by_story_url_v1(self, url: str) -> Dict:
        '''Download story file by story URL. Download story file by story URL
        Example: https://instagram.com/stories/example/30038568123745341231284'''
        params = {"url": url}
        return self._request("get", "/v1/story/download/by/story/url", params=params)

    def location_by_id_v1(self, id: int) -> Dict:
        '''Location By Id. Get location object by id'''
        params = {"id": id}
        return self._request("get", "/v1/location/by/id", params=params)

    def location_medias_top_v1(self, location_pk: int, amount: Optional[int] = None) -> Dict:
        '''Location Medias Top V1. Get location top medias'''
        params = {"location_pk": location_pk, "amount": amount}
        return self._request("get", "/v1/location/medias/top", params=params)

    def location_medias_recent_v1(self, location_pk: int, amount: Optional[int] = None) -> Dict:
        '''Location Medias Recent V1. Get location recent medias'''
        params = {"location_pk": location_pk, "amount": amount}
        return self._request("get", "/v1/location/medias/recent", params=params)

    def location_medias_top_chunk_v1(self, location_pk: int, max_amount: Optional[int] = None, max_id: Optional[str] = None) -> Dict:
        '''Location Medias Top Chunk. Get location chunk of top medias'''
        params = {"location_pk": location_pk, "max_amount": max_amount, "max_id": max_id}
        return self._request("get", "/v1/location/medias/top/chunk", params=params)

    def location_medias_recent_chunk_v1(self, location_pk: int, max_amount: Optional[int] = None, max_id: Optional[str] = None) -> Dict:
        '''Location Medias Recent Chunk. Get location chunk of recent medias'''
        params = {"location_pk": location_pk, "max_amount": max_amount, "max_id": max_id}
        return self._request("get", "/v1/location/medias/recent/chunk", params=params)

    def location_search_v1(self, lat: float, lng: float) -> Dict:
        '''Location Search. Get locations using lat and long'''
        params = {"lat": lat, "lng": lng}
        return self._request("get", "/v1/location/search", params=params)

    def location_guides_v1(self, location_pk: int) -> Dict:
        '''Location Guides V1. Get location guides'''
        params = {"location_pk": location_pk}
        return self._request("get", "/v1/location/guides", params=params)

    def search_hashtags_v1(self, query: str) -> Dict:
        '''Search Hashtags. Search hashtags'''
        params = {"query": query}
        return self._request("get", "/v1/search/hashtags", params=params)

    def search_users_v1(self, query: str) -> Dict:
        '''Search Users. Search users'''
        params = {"query": query}
        return self._request("get", "/v1/search/users", params=params)

    def search_music_v1(self, query: str) -> Dict:
        '''Search Music. Search music'''
        params = {"query": query}
        return self._request("get", "/v1/search/music", params=params)

    def fbsearch_places_v1(self, query: str, lat: Optional[float] = None, lng: Optional[float] = None) -> Dict:
        '''Fbsearch Places. Search locations'''
        params = {"query": query, "lat": lat, "lng": lng}
        return self._request("get", "/v1/fbsearch/places", params=params)

    def fbsearch_topsearch_v1(self, query: str) -> Dict:
        '''Fbsearch Topsearch. Topsearch'''
        params = {"query": query}
        return self._request("get", "/v1/fbsearch/topsearch", params=params)

    def fbsearch_topsearch_hashtags_v1(self, query: str) -> Dict:
        '''Web Search Topsearch Hashtags. Search hashtags via topsearch'''
        params = {"query": query}
        return self._request("get", "/v1/fbsearch/topsearch/hashtags", params=params)

    def hashtag_by_name_v1(self, name: str) -> Dict:
        '''Hashtag By Name. Get hashtag object by name'''
        params = {"name": name}
        return self._request("get", "/v1/hashtag/by/name", params=params)

    def hashtag_medias_top_v1(self, name: str, amount: Optional[int] = None) -> Dict:
        '''Hashtag Medias Top. Get hashtag medias top'''
        params = {"name": name, "amount": amount}
        return self._request("get", "/v1/hashtag/medias/top", params=params)

    def hashtag_medias_top_chunk_v1(self, name: str, max_amount: Optional[int] = None, max_id: Optional[str] = None) -> Dict:
        '''Hashtag Medias Top Chunk. Get hashtag chunk of top medias'''
        params = {"name": name, "max_amount": max_amount, "max_id": max_id}
        return self._request("get", "/v1/hashtag/medias/top/chunk", params=params)

    def hashtag_medias_recent_v1(self, name: str, amount: Optional[int] = None) -> Dict:
        '''Hashtag Medias Recent. Get hashtag medias top'''
        params = {"name": name, "amount": amount}
        return self._request("get", "/v1/hashtag/medias/recent", params=params)

    def hashtag_medias_recent_chunk_v1(self, name: str, max_amount: Optional[int] = None, max_id: Optional[str] = None) -> Dict:
        '''Hashtag Medias Recent Chunk. Get hashtag chunk of recent medias'''
        params = {"name": name, "max_amount": max_amount, "max_id": max_id}
        return self._request("get", "/v1/hashtag/medias/recent/chunk", params=params)

    def hashtag_medias_clips_v1(self, name: str, amount: Optional[int] = None) -> Dict:
        '''Hashtag Medias Clips. Get hashtag clips (reels)'''
        params = {"name": name, "amount": amount}
        return self._request("get", "/v1/hashtag/medias/clips", params=params)

    def hashtag_medias_clips_chunk_v1(self, name: str, max_amount: Optional[int] = None, max_id: Optional[str] = None) -> Dict:
        '''Hashtag Medias Clips Chunk. Get hashtag chunk of clips (reels)'''
        params = {"name": name, "max_amount": max_amount, "max_id": max_id}
        return self._request("get", "/v1/hashtag/medias/clips/chunk", params=params)

    def highlight_by_id_v1(self, id: int) -> Dict:
        '''Highlight By Id. Get highlight object by id'''
        params = {"id": id}
        return self._request("get", "/v1/highlight/by/id", params=params)

    def highlight_by_url_v1(self, url: str) -> Dict:
        '''Attention! To work with /s/ links, call /v1/share/by/url first. Get highlight object by id'''
        params = {"url": url}
        return self._request("get", "/v1/highlight/by/url", params=params)

    def share_by_code_v1(self, code: str) -> Dict:
        '''Share By Code. Get share object by code (aGlnaGxpZ2h0OjE4MTQ2MjE2Njk4MDIyMTc0 ->
        {"pk": 18146216698022176, "type": "highlight"})'''
        params = {"code": code}
        return self._request("get", "/v1/share/by/code", params=params)

    def share_by_url_v1(self, url: str) -> Dict:
        '''Share By Url. Get share object by url (
        https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MTQ2MjE2Njk4MDIyMTc0 ->
        {"pk": 18146216698022176, "type": "highlight"})'''
        params = {"url": url}
        return self._request("get", "/v1/share/by/url", params=params)

    def user_by_id_v2(self, id: str) -> Dict:
        '''User By Id. Get user object by id'''
        params = {"id": id}
        return self._request("get", "/v2/user/by/id", params=params)

    def user_by_username_v2(self, username: str) -> Dict:
        '''Get user object by username (one request required). Get user object by username'''
        params = {"username": username}
        return self._request("get", "/v2/user/by/username", params=params)

    def user_stories_v2(self, user_id: str) -> Dict:
        '''User Stories. Get user stories'''
        params = {"user_id": user_id}
        return self._request("get", "/v2/user/stories", params=params)

    def user_stories_by_username_v2(self, username: str) -> Dict:
        '''User Stories By Username. Get user stories'''
        params = {"username": username}
        return self._request("get", "/v2/user/stories/by/username", params=params)

    def user_medias_v2(self, user_id: str, page_id: Optional[str] = None) -> Dict:
        '''User Medias. Get user medias. Results paginated.'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._request("get", "/v2/user/medias", params=params)

    def user_medias(self, user_id: str, page_id: Optional[str] = None, count: Optional[int] = None, container: Optional[List[Dict]] = None, max_requests: Optional[int] = None) -> List[Dict]:
        '''User Medias. Get user medias. Results paginated.'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._paging_request("/v2/user/medias", params=params, count=count, container=container, max_requests=max_requests)

    def user_clips_v2(self, user_id: str, page_id: Optional[str] = None) -> Dict:
        '''User Clips. Get user clips.'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._request("get", "/v2/user/clips", params=params)

    def user_clips(self, user_id: str, page_id: Optional[str] = None, count: Optional[int] = None, container: Optional[List[Dict]] = None, max_requests: Optional[int] = None) -> List[Dict]:
        '''User Clips. Get user clips.'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._paging_request("/v2/user/clips", params=params, count=count, container=container, max_requests=max_requests)

    def user_videos_v2(self, user_id: str, page_id: Optional[str] = None) -> Dict:
        '''User Videos. Get part of user videos with cursor (default 50 media per request)'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._request("get", "/v2/user/videos", params=params)

    def user_videos(self, user_id: str, page_id: Optional[str] = None, count: Optional[int] = None, container: Optional[List[Dict]] = None, max_requests: Optional[int] = None) -> List[Dict]:
        '''User Videos. Get part of user videos with cursor (default 50 media per request)'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._paging_request("/v2/user/videos", params=params, count=count, container=container, max_requests=max_requests)

    def user_following_v2(self, user_id: str, page_id: Optional[str] = None) -> Dict:
        '''Get a user following (one request required). Get part (one page) of following users'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._request("get", "/v2/user/following", params=params)

    def user_following(self, user_id: str, page_id: Optional[str] = None, count: Optional[int] = None, container: Optional[List[Dict]] = None, max_requests: Optional[int] = None) -> List[Dict]:
        '''Get a user following (one request required). Get part (one page) of following users'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._paging_request("/v2/user/following", params=params, count=count, container=container, max_requests=max_requests)

    def user_followers_v2(self, user_id: str, page_id: Optional[str] = None) -> Dict:
        '''Get a user followers (one request required). Get part (one page) of followers users with cursor'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._request("get", "/v2/user/followers", params=params)

    def user_followers(self, user_id: str, page_id: Optional[str] = None, count: Optional[int] = None, container: Optional[List[Dict]] = None, max_requests: Optional[int] = None) -> List[Dict]:
        '''Get a user followers (one request required). Get part (one page) of followers users with cursor'''
        params = {"user_id": user_id, "page_id": page_id}
        return self._paging_request("/v2/user/followers", params=params, count=count, container=container, max_requests=max_requests)

    def media_by_id_v2(self, id: str) -> Dict:
        '''Media By Id. Get media object'''
        params = {"id": id}
        return self._request("get", "/v2/media/by/id", params=params)

    def media_by_code_v2(self, code: str) -> Dict:
        '''Media By Code. Get media object'''
        params = {"code": code}
        return self._request("get", "/v2/media/by/code", params=params)

    def media_by_url_v2(self, url: str) -> Dict:
        '''Media By Url. Get media object'''
        params = {"url": url}
        return self._request("get", "/v2/media/by/url", params=params)

    def media_likers_v2(self, id: str) -> Dict:
        '''Media Likers. Get user's likers'''
        params = {"id": id}
        return self._request("get", "/v2/media/likers", params=params)

    def track_by_canonical_id_v2(self, canonical_id: str) -> Dict:
        '''Track By Canonical Id. Get music track object by canonical_id'''
        params = {"canonical_id": canonical_id}
        return self._request("get", "/v2/track/by/canonical/id", params=params)

    def track_by_id_v2(self, track_id: str) -> Dict:
        '''Track By Id. Get music track object by id'''
        params = {"track_id": track_id}
        return self._request("get", "/v2/track/by/id", params=params)

    def media_likers(self, media_id: str, page_id: Optional[str] = None, count: Optional[int] = None, container: Optional[List[Dict]] = None, max_requests: Optional[int] = None) -> List[Dict]:
        '''Get likers on media'''
        params = {"media_id": media_id, "end_cursor": page_id}
        return self._paging_request("/gql/media/likers/chunk", params=params, count=count, container=container, page_key="end_cursor", max_requests=max_requests)
