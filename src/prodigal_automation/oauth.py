# src/prodigal_automation/oauth.py

from tweepy import OAuth1UserHandler
from .auth import TwitterAuth

class TwitterOAuthHandler:
    """Handles Twitter OAuth 1.0a authentication"""
    
    def __init__(self, auth: TwitterAuth):
        if not auth.has_oauth_credentials():
            raise ValueError("Missing required OAuth credentials")
        
        self.handler = OAuth1UserHandler(
            consumer_key=auth.api_key,
            consumer_secret=auth.api_secret,
            access_token=auth.access_token,
            access_token_secret=auth.access_token_secret
        )
    
    def get_auth_handler(self):
        """Returns the configured OAuth handler"""
        return self.handler