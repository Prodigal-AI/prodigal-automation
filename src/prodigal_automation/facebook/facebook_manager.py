from prodigal_automation.facebook.facebook_client import FacebookClient
from prodigal_automation.core.models import SocialMediaPost, FacebookPostResponse
from prodigal_automation.core.errors import ValidationError, APIError
from typing import Dict, Any

class FacebookManager:
    def __init__(self, client: FacebookClient):
        self.client = client
        self.graph_api = self.client.connect()

    def post_to_facebook(self, post_data: Dict[str, Any]) -> FacebookPostResponse:
        try:
            validated_post = SocialMediaPost(**post_data, platform='facebook')
            response_data = self.client.post(validated_post.content) # client.post handles Graph API call
            return FacebookPostResponse(id=response_data['id'], message=validated_post.content)
        except ValidationError as e:
            raise ValidationError(f"Invalid post data: {e}")
        except APIError as e:
            raise APIError(f"Error posting to Facebook: {e}")
        except Exception as e:
            raise APIError(f"An unexpected error occurred while posting to Facebook: {e}")
