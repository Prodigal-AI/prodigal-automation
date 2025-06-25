# src/prodigal_automation/client.py
from typing import Dict, Optional

import facebook
from tweepy import Client

from .auth import FacebookAuth, TwitterAuth


class TwitterClient:
    """Twitter API client wrapper"""

    def __init__(self, auth: TwitterAuth):
        self.auth = auth
        self.client = None

    def initialize(self):
        """
        Initialize the appropriate Twitter client based on available
        credentials.
        """
        if self.auth.has_oauth_credentials():
            self.client = Client(
                consumer_key=self.auth.api_key,
                consumer_secret=self.auth.api_key_secret,
                access_token=self.auth.access_token,
                access_token_secret=self.auth.access_token_secret,
            )
        elif self.auth.has_bearer_token():
            self.client = Client(bearer_token=self.auth.bearer_token)
        else:
            raise ValueError("No valid Twitter credentials provided")

        return self.client


class FacebookClient:
    """Facebook API client wrapper"""

    def __init__(self, auth: FacebookAuth):
        self.auth = auth
        self.client = None

    def initialize(self):
        """
        Initialize the Facebook Graph API client using the access token.
        """

        if not self.auth.access_token:
            raise ValueError("Facebook Access Token not provided.")

        try:
            self.client = facebook.GraphAPI(access_token=self.auth.access_token)
            self.page_id = self.auth.page_id
            return self.client
        except facebook.GraphAPIError as e:
            raise ConnectionError(f"Failed to initialize Facebook client: {e}")

    def _check_initialized(self):
        """Helper to ensure client is initialized before making API calls."""
        if self.client is None:
            raise RuntimeError(
                "FacebookClient is not initialized. Call .initialize() first."
            )

    def put_object(self, parent_object: str, connection_name: str, **kwargs) -> Dict:
        """
        Wrapper for facebook.GraphAPI.put_object().
        Used for creating posts, photos, videos, etc.
        """
        self._check_initialized()  # Ensure client is ready
        try:
            # IMPORTANT: Call put_object on the self.client (GraphAPI instance)
            # Ensure access_token is passed if not already handled by GraphAPI's init
            # The python-facebook-sdk usually uses the token provided at GraphAPI init,
            # but sometimes explicit passing helps or is required by newer API versions.
            if "access_token" not in kwargs:
                kwargs["access_token"] = self.auth.access_token
            return self.client.put_object(parent_object, connection_name, **kwargs)
        except facebook.GraphAPIError as e:
            print(f"Facebook Graph API Error putting object: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"An unexpected error occurred putting object: {e}")
            return {"error": str(e)}

    def get_page_insights(
        self,
        page_id: str,
        metrics: list[str],
        period: str = "day",
        since: Optional[int] = None,
        until: Optional[int] = None,
    ) -> Dict:
        """
        Fetches insights for a Facebook Page.
        Args:
            page_id: The ID of the Facebook Page.
            metrics: A list of insight metrics to fetch (e.g., ['page_impressions_unique', 'page_engaged_users']). # noqa
            period: The aggregation period (e.g., 'day', 'week', 'days_28').
            since: Optional start UNIX timestamp for the data range.
            until: Optional end UNIX timestamp for the data range.
        Returns:
            Dictionary containing the insight data.
        """

        if self.client is None:
            raise RuntimeError(
                "FacebookClient is not initialized. Call .initialize() first."
            )

        params = {
            "metric": ",".join(metrics),
            "period": period,
            "access_token": self.auth.access_token,  # Ensure access token is passed
        }
        if since:
            params["since"] = since
        if until:
            params["until"] = until

        try:
            response = self.client.get_connections(page_id, "insights", **params)
            return response
        except facebook.GraphAPIError as e:
            print(f"Facebook Graph API Error fetching insights: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"An unexpected error occurred fetching insights: {e}")
            return {"error": str(e)}

    def get_post_insights(self, post_id: str, metrics: list[str]) -> Dict:
        """
        Fetches insights for a specific Facebook Post.
        Args:
            post_id: The ID of the Facebook Post.
            metrics: A list of insight metrics to fetch (e.g., ['post_impressions_unique']). # noqa
        Returns:
            Dictionary containing the insight data.
        """

        if self.client is None:
            raise RuntimeError(
                "FacebookClient is not initialized. Call .initialize() first."
            )

        params = {"metric": ",".join(metrics), "access_token": self.auth.access_token}
        try:
            response = self.client.get_connections(post_id, "insights", **params)
            return response
        except facebook.GraphAPIError as e:
            print(f"Facebook Graph API Error fetching post insights: {e}")
            return {"error": str(e)}
        except Exception as e:
            print(f"An unexpected error occurred fetching post insights: {e}")
            return {"error": str(e)}

    def delete_object(self, object_id: str) -> Dict:
        """
        Deletes a Facebook object (e.g., post, photo).
        Args:
            object_id: The ID of the object to delete.
        Returns:
            Dictionary indicating success or error.
        """

        if self.client is None:
            raise RuntimeError(
                "FacebookClient is not initialized. Call .initialize() first."
            )

        try:
            response = self.client.delete_object(object_id)
            if response.get("success"):
                return {
                    "success": True,
                    "message": f"Object {object_id} deleted successfully.",
                }
            else:
                return {
                    "success": False,
                    "error": f"Failed to delete object {object_id}: {response}",
                }
        except facebook.GraphAPIError as e:
            print(f"Facebook Graph API Error deleting object: {e}")
            return {"success": False, "error": str(e)}
        except Exception as e:
            print(f"An unexpected error occurred deleting object: {e}")
            return {"success": False, "error": str(e)}
