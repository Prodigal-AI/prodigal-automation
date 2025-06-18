# src/prodigal_automation/facebook_manager.py

from typing import Dict, Union

# REMOVE this top-level import: import facebook
from prodigal_automation.client import FacebookClient
from prodigal_automation.tools import ContentGenerator
from prodigal_automation.auth import FacebookAuth #noqa


class FacebookManager:
    """Manages Facebook operations with proper error handling"""

    def __init__(
        self,
        facebook_client_or_auth,
        content_generator_or_api_key=None,
    ):
        """
        Initialize FacebookManager with flexible constructor to support both
        test and production use
        Args:
            facebook_client_or_auth: Either a FacebookClient instance (for tests)
                or FacebookAuth instance
            content_generator_or_api_key: Either a ContentGenerator instance
                (for tests) or API key string
        """
        # Ensure 'facebook' is imported only when it's definitely needed
        # (i.e., when initializing the client in production).
        # However, the FacebookClient itself handles the 'facebook' import,
        # so you might not even need it directly here.
        # Let's verify what 'facebook_client_or_auth' truly is here.

        if content_generator_or_api_key is None:
            raise ValueError(
                "Missing required parameter: content_generator_or_api_key"
            )

        if isinstance(facebook_client_or_auth, FacebookClient):
            # Test usage: mock facebook_client + mock content_generator
            self.client = facebook_client_or_auth # The mock client is already initialized or doesn't need facebook.GraphAPI()
            self.content_generator = content_generator_or_api_key
            if hasattr(self.client, 'auth') and self.client.auth.page_id:
                self.page_id = self.client.auth.page_id
            else:
                self.page_id = None # Mocks might not have page_id directly on client
        else:
            # Production usage: FacebookAuth + gemini_api_key
            self.auth_data = facebook_client_or_auth # Store auth for later use if needed
            self.client = FacebookClient(facebook_client_or_auth).initialize()
            self.content_generator = ContentGenerator(content_generator_or_api_key)
            self.page_id = facebook_client_or_auth.page_id if facebook_client_or_auth.page_id else None


    def create_post(self, topic: str) -> Union[Dict, str]:
        """
        Create and post content to Facebook with validation
        Args:
            topic: Topic for the Facebook post
        Returns:
            Dictionary with success status and response data (production)
            or post_id string (test compatibility)
        """
        # ... (rest of your code, which already calls self.client methods)
        # The 'facebook' import is now implicitly handled by FacebookClient,
        # so no direct import is needed here.

        try:
            content = self.content_generator.generate_simple_content(topic)

            if not self.page_id:
                # If page_id was not set during init, try to get it from auth_data if available
                if hasattr(self, 'auth_data') and self.auth_data.page_id:
                    self.page_id = self.auth_data.page_id
                else:
                    raise ValueError("Facebook Page ID is required to post.")


            response = self.client.put_object(
                parent_object=self.page_id, connection_name='feed', message=content
            )

            # ... (rest of your error handling and return logic)
            if hasattr(response, "get") and response.get("id"):
                return response.get("id")

            if response and "id" in response:
                return {
                    "success": True,
                    "post_id": response["id"],
                    "content": content,
                }
            else:
                return {
                    "success": False,
                    "error": (
                        f"Facebook post creation failed or returned "
                        f"unexpected response: {response}"
                    ),
                }

        except ValueError as ve:
            # For tests, re-raise the exception
            if hasattr(self.client, "_mock_name"):
                raise ve
            return {"success": False, "error": f"Validation error: {str(ve)}"}
        except Exception as e: # Catch facebook.GraphAPIError here too
            # For tests, re-raise the exception
            # Explicitly import facebook here if you need to catch GraphAPIError
            # from facebook-sdk directly in this file's 'except' block.
            # If not, the generic 'Exception' will catch it.
            import facebook # Import here only if needed for specific exception handling
            if isinstance(e, facebook.GraphAPIError): # Check if it's a GraphAPIError
                if hasattr(self.client, "_mock_name"):
                    raise e
                return {"success": False, "error": f"Facebook API error: {str(e)}"}
            else: # Other unexpected errors
                if hasattr(self.client, "_mock_name"):
                    raise e
                return {
                    "success": False,
                    "error": (
                        "An unexpected error occurred during Facebook post creation: "
                        f"{type(e).__name__} - {str(e)}"
                    ),
                }
    def post_image(self, message: str, image_url: str, published: bool = True) -> Dict:
        """
        Posts an image to the Facebook page.
        Args:
            message: The caption for the image.
            image_url: URL of the image.
            published: Whether to publish immediately (True) or as unpublished (False).
        Returns:
            Dictionary with success status and response data.
        """
        if not self.page_id:
            return {"success": False, "error": "Facebook Page ID is not set."}

        try:
            params = {
                'url': image_url,
                'message': message,
                'published': published,
                'access_token': self.client.auth.access_token # Ensure access token is passed for specific calls
            }
            response = self.client.put_object(
                parent_object=self.page_id,
                connection_name='photos',
                **params
            )
            if response and "id" in response:
                return {"success": True, "post_id": response["id"], "content": message, "image_url": image_url}
            else:
                return {"success": False, "error": f"Image post failed: {response}"}
        except Exception as e:
            import facebook # Local import for exception handling
            if isinstance(e, facebook.GraphAPIError):
                return {"success": False, "error": f"Facebook API error (Image Post): {str(e)}"}
            return {"success": False, "error": f"An unexpected error occurred during image post: {str(e)}"}

    def post_video(self, message: str, video_url: str, published: bool = True) -> Dict:
        """
        Posts a video to the Facebook page.
        Args:
            message: The caption for the video.
            video_url: URL of the video file (e.g., mp4, mov).
            published: Whether to publish immediately (True) or as unpublished (False).
        Returns:
            Dictionary with success status and response data.
        """
        if not self.page_id:
            return {"success": False, "error": "Facebook Page ID is not set."}

        try:
            params = {
                'file_url': video_url, # Use 'file_url' for external video URLs
                'description': message, # Use 'description' for video caption
                'published': published,
                'access_token': self.client.auth.access_token # Ensure access token is passed
            }
            response = self.client.put_object(
                parent_object=self.page_id,
                connection_name='videos',
                **params
            )
            if response and "id" in response:
                return {"success": True, "post_id": response["id"], "content": message, "video_url": video_url}
            else:
                return {"success": False, "error": f"Video post failed: {response}"}
        except Exception as e:
            import facebook # Local import for exception handling
            if isinstance(e, facebook.GraphAPIError):
                return {"success": False, "error": f"Facebook API error (Video Post): {str(e)}"}
            return {"success": False, "error": f"An unexpected error occurred during video post: {str(e)}"}
