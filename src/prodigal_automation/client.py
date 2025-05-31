# src/prodigal_automation/client.py

from tweepy import Client

from .auth import TwitterAuth


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
