from prodigal_automation.core.auth import DotEnvAuthenticator
from prodigal_automation.core.client import TwitterClient
from prodigal_automation.twitter.twitter_manager import TwitterManager
from prodigal_automation.core.models import SocialMediaPost, TwitterPostResponse, Timeline
from prodigal_automation.core.errors import SocialMediaError
from typing import Dict, Any

class TwitterAutomator:
    def __init__(self, env_path: str = '.env'):
        self.authenticator = DotEnvAuthenticator(env_path)
        self.credentials = self.authenticator.get_twitter_credentials()
        self.client = TwitterClient(self.credentials)
        self.manager = TwitterManager(self.client)

    def post(self, content: str) -> TwitterPostResponse:
        """Posts a tweet."""
        try:
            return self.manager.post_tweet({"content": content})
        except SocialMediaError as e:
            print(f"Error during Twitter post: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def get_timeline(self, count: int = 20) -> Timeline:
        """Fetches the user's home timeline."""
        try:
            return self.manager.get_user_timeline(count=count)
        except SocialMediaError as e:
            print(f"Error during Twitter timeline fetch: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise