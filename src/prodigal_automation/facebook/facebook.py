from prodigal_automation.core.auth import DotEnvAuthenticator
from prodigal_automation.facebook.facebook_client import FacebookClient
from prodigal_automation.facebook.facebook_manager import FacebookManager
from prodigal_automation.core.models import SocialMediaPost, FacebookPostResponse
from prodigal_automation.core.errors import SocialMediaError
from typing import Dict, Any

class FacebookAutomator:
    def __init__(self, env_path: str = '.env'):
        self.authenticator = DotEnvAuthenticator(env_path)
        self.credentials = self.authenticator.get_facebook_credentials()
        self.client = FacebookClient(self.credentials)
        self.manager = FacebookManager(self.client)

    def post(self, content: str) -> FacebookPostResponse:
        """Posts to Facebook (user's feed or page's feed)."""
        try:
            return self.manager.post_to_facebook({"content": content})
        except SocialMediaError as e:
            print(f"Error during Facebook post: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise