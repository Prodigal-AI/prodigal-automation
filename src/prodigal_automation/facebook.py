# src/prodigal_automation/facebook.py

import os

from prodigal_automation.auth import FacebookAuth
from prodigal_automation.facebook_manager import FacebookManager


class FacebookAutomation:
    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not set")

    def get_facebook_credentials(self) -> FacebookAuth:
        print("Enter Facebook credentials (leave blank to skip)")
        return FacebookAuth(
            access_token=input("Facebook Page Access Token: ").strip() or None,
            page_id=input(
                "Facebook Page ID (optional, but needed for posting): "
            ).strip()
            or None,
            app_id=input("Facebook App ID (optional): ").strip() or None,
            app_secret=input("Facebook App Secret (optional): ").strip() or None,
        )

    def run(self):
        try:
            auth = self.get_facebook_credentials()
            manager = FacebookManager(auth, self.gemini_api_key)
            topic = input("Facebook post topic: ").strip()
            result = manager.create_post(topic)
            if result["success"]:
                print(
                    f"Facebook post published (ID: {result['post_id']}): "
                    f"{result['content']}"
                )
            else:
                print(f"Facebook post publishing failed: {result['error']}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
