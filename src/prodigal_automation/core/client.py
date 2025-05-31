import tweepy
from prodigal_automation.core.models import TwitterAuthCredentials
from prodigal_automation.core.errors import APIError

class BaseSocialMediaClient:
    def __init__(self, credentials):
        self.credentials = credentials

    def connect(self):
        raise NotImplementedError

    def post(self, content: str):
        raise NotImplementedError

    def get_timeline(self, **kwargs):
        raise NotImplementedError

class TwitterClient(BaseSocialMediaClient):
    def __init__(self, credentials: TwitterAuthCredentials):
        super().__init__(credentials)
        self._client: tweepy.Client = None

    def connect(self):
        try:
            # tweepy.Client is the API v2 client.
            # It accepts OAuth 1.0a credentials directly for user context actions.
            self._client = tweepy.Client(
                consumer_key=self.credentials.consumer_key.get_secret_value(),
                consumer_secret=self.credentials.consumer_secret.get_secret_value(),
                access_token=self.credentials.access_token.get_secret_value(),
                access_token_secret=self.credentials.access_token_secret.get_secret_value(),
                # bearer_token=self.credentials.bearer_token.get_secret_value() if self.credentials.bearer_token else None,
                wait_on_rate_limit=True
            )
            # You can test connection with a simple call, e.g., get_me()
            # self._client.get_me()
            return self._client
        except tweepy.TweepyException as e:
            raise APIError(f"Failed to connect to Twitter API v2: {e}")

    def post(self, content: str) -> dict:
        try:
            response = self._client.create_tweet(text=content)
            # The 'data' attribute of the response object contains the created tweet details
            if response.data:
                return response.data
            else:
                raise APIError(f"Tweet creation failed: {response.errors}")
        except tweepy.TweepyException as e:
            raise APIError(f"Failed to post to Twitter: {e}")

    def get_timeline(self, count: int = 20) -> list:
        try:
            # For home timeline, we need the authenticating user's ID.
            # We can get this from client.get_me() which is typically done once.
            # For simplicity, we'll assume the user ID is available or fetched once.
            # In a real app, you'd cache this.
            # Tweepy's get_home_timeline fetches the authenticated user's timeline.
            # max_results for get_home_timeline is 1 to 100.
            # To get more, you'd use Tweepy's Paginator or handle pagination tokens.
            # For this example, we'll stick to max_results.

            # First, get the authenticated user's ID
            me_response = self._client.get_me()
            if not me_response.data:
                raise APIError("Could not retrieve authenticated user ID for timeline.")
            user_id = me_response.data.id

            response = self._client.get_home_timeline(
                user_id=user_id,
                max_results=min(count, 100), # max_results for timeline is 100
                tweet_fields=["created_at", "author_id"], # Request specific fields
                expansions=["author_id"] # To get user info alongside tweets
            )

            # Response structure for timeline:
            # response.data: list of tweet objects
            # response.includes: dict of expanded objects (e.g., users)
            # response.meta: pagination tokens, result count

            tweets_data = response.data if response.data else []
            # Optionally, process includes to get user details if needed:
            # users_data = {user['id']: user for user in response.includes.get('users', [])}

            return tweets_data
        except tweepy.TweepyException as e:
            raise APIError(f"Failed to fetch Twitter timeline: {e}")