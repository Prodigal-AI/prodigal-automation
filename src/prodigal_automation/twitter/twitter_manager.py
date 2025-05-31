from datetime import datetime
from prodigal_automation.twitter.twitter_client import TwitterClient
from prodigal_automation.core.models import SocialMediaPost, TwitterPostResponse, Tweet, Timeline
from prodigal_automation.core.errors import ValidationError, APIError
from typing import List, Dict, Any

class TwitterManager:
    def __init__(self, client: TwitterClient):
        self.client = client
        self.client_v2_api = self.client.connect()

    def post_tweet(self, post_data: Dict[str, Any]) -> TwitterPostResponse:
        try:
            validated_post = SocialMediaPost(**post_data, platform='twitter') # Ensure platform is set
            tweet_data = self.client.post(validated_post.content)
            return TwitterPostResponse(**tweet_data)
        except ValidationError as e:
            raise ValidationError(f"Invalid post data: {e}")
        except APIError as e:
            raise APIError(f"Error posting tweet: {e}")
        except Exception as e:
            raise APIError(f"An unexpected error occurred while posting tweet: {e}")

    def get_user_timeline(self, count: int = 20) -> Timeline:
        try:
            timeline_response_data = self.client.get_timeline(count=count)
            tweets = []
            for t_data in timeline_response_data:
                try:
                    t_data['created_at'] = datetime.fromisoformat(t_data['created_at'].replace('Z', '+00:00'))
                except (TypeError, ValueError):
                    pass
                tweets.append(Tweet(**t_data))
            return Timeline(tweets=tweets, count=len(tweets))
        except APIError as e:
            raise APIError(f"Error fetching timeline: {e}")
        except Exception as e:
            raise APIError(f"An unexpected error occurred while fetching timeline: {e}")