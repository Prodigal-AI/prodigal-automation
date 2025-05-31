import tweepy
from prodigal_automation.core.base_client import BaseSocialMediaClient
from prodigal_automation.core.models import TwitterAuthCredentials
from prodigal_automation.core.errors import APIError

class TwitterClient(BaseSocialMediaClient):
    def __init__(self, credentials: TwitterAuthCredentials):
        super().__init__(credentials)
        self._api_client: tweepy.Client = None # Renamed for clarity

    def connect(self):
        try:
            self._api_client = tweepy.Client(
                consumer_key=self.credentials.consumer_key.get_secret_value(),
                consumer_secret=self.credentials.consumer_secret.get_secret_value(),
                access_token=self.credentials.access_token.get_secret_value(),
                access_token_secret=self.credentials.access_token_secret.get_secret_value(),
                wait_on_rate_limit=True
            )
            return self._api_client
        except tweepy.TweepyException as e:
            raise APIError(f"Failed to connect to Twitter API v2: {e}")

    def post(self, content: str, **kwargs) -> dict: # Added kwargs for future flexibility
        try:
            response = self._api_client.create_tweet(text=content, **kwargs)
            if response.data:
                return response.data
            else:
                raise APIError(f"Tweet creation failed: {response.errors}")
        except tweepy.TweepyException as e:
            raise APIError(f"Failed to post to Twitter: {e}")

    def get_timeline(self, count: int = 20) -> list:
        try:
            me_response = self._api_client.get_me()
            if not me_response.data:
                raise APIError("Could not retrieve authenticated user ID for timeline.")
            user_id = me_response.data.id

            response = self._api_client.get_home_timeline(
                user_id=user_id,
                max_results=min(count, 100),
                tweet_fields=["created_at", "author_id"],
                expansions=["author_id"]
            )
            tweets_data = response.data if response.data else []
            return tweets_data
        except tweepy.TweepyException as e:
            raise APIError(f"Failed to fetch Twitter timeline: {e}")