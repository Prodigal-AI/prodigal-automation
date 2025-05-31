import facebook
from prodigal_automation.core.base_client import BaseSocialMediaClient
from prodigal_automation.core.models import FacebookAuthCredentials
from prodigal_automation.core.errors import APIError
from typing import Dict, Any

class FacebookClient(BaseSocialMediaClient):
    def __init__(self, credentials: FacebookAuthCredentials):
        super().__init__(credentials)
        self._api_client: facebook.GraphAPI = None

    def connect(self):
        try:
            self._api_client = facebook.GraphAPI(
                access_token=self.credentials.access_token.get_secret_value(),
                version="18.0" # Specify Graph API version, e.g., "v18.0" or latest
            )
            # Test connection - can fetch user's own profile
            # self._api_client.get_object("me")
            return self._api_client
        except facebook.GraphAPIError as e:
            raise APIError(f"Failed to connect to Facebook Graph API: {e}")

    def post(self, content: str, **kwargs) -> dict:
        try:
            page_id = self.credentials.page_id.get_secret_value() if self.credentials.page_id else "me"
            # Posting to a page or user's own feed
            # For pages, ensure the access token is a Page Access Token with publish_pages permission.
            # For user's feed, ensure user_posts permission.
            response = self._api_client.put_object(
                parent_object=page_id,
                connection_name="feed",
                message=content,
                **kwargs
            )
            # response typically contains {'id': '<page_id>_<post_id>'}
            return response
        except facebook.GraphAPIError as e:
            raise APIError(f"Failed to post to Facebook: {e}")

    # def get_feed(self, page_id: str = "me", limit: int = 25) -> list:
    #     try:
    #         feed = self._api_client.get_connections(page_id, "feed", limit=limit)
    #         return feed['data']
    #     except facebook.GraphAPIError as e:
    #         raise APIError(f"Failed to fetch Facebook feed: {e}")