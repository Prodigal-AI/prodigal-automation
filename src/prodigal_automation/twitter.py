# src/prodigal_automation/twitter.py

import os

from .auth import TwitterAuth
from .twitter_manager import TwitterManager


class TwitterAutomation:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not set")

    def get_twitter_credentials(self) -> TwitterAuth:
        print("Enter Twitter credentials (leave blank to skip)")
        return TwitterAuth(
            bearer_token=input("Bearer Token: ").strip() or None,
            api_key=input("API Key: ").strip() or None,
            api_key_secret=input("API Secret: ").strip() or None,
            access_token=input("Access Token: ").strip() or None,
            access_token_secret=(input(
                "Access Token Secret: "
                ).strip() or None),
        )

    def run(self):
        try:
            auth = self.get_twitter_credentials()
            manager = TwitterManager(auth, self.gemini_api_key)
            topic = input("Tweet topic: ").strip()
            result = manager.create_tweet(topic)
            if result["success"]:
                print(
                    f"Tweet posted (ID: {result['tweet_id']}): "
                    f"{result['content']}"
                )
            else:
                print(f"Tweet posting failed: {result['error']}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
