import os
from dotenv import load_dotenv
from prodigal_automation.core.models import TwitterAuthCredentials, FacebookAuthCredentials # NEW import
from prodigal_automation.core.errors import AuthError

class BaseAuthenticator:
    def get_credentials(self):
        raise NotImplementedError

class DotEnvAuthenticator(BaseAuthenticator):
    def __init__(self, env_path: str = '.env'):
        load_dotenv(dotenv_path=env_path)

    def get_twitter_credentials(self) -> TwitterAuthCredentials:
        try:
            return TwitterAuthCredentials(
                consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
                consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
                access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
                access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
            )
        except Exception as e:
            raise AuthError(f"Failed to load Twitter credentials from .env: {e}")

    # --- NEW: Get Facebook Credentials ---
    def get_facebook_credentials(self) -> FacebookAuthCredentials:
        try:
            return FacebookAuthCredentials(
                access_token=os.getenv("FACEBOOK_ACCESS_TOKEN"),
                page_id=os.getenv("FACEBOOK_PAGE_ID") # Optional
            )
        except Exception as e:
            raise AuthError(f"Failed to load Facebook credentials from .env: {e}")