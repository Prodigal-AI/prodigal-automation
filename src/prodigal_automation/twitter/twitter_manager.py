from datetime import datetime
from prodigal_automation.core.client import TwitterClient
from prodigal_automation.core.models import SocialMediaPost, TwitterPostResponse, Tweet, Timeline
from prodigal_automation.core.errors import ValidationError, APIError
from typing import List, Dict, Any

class TwitterManager:
    def __init__(self, client: TwitterClient):
        self.client = client
        self.client_v2_api = self.client.connect() # Establish connection and get the tweepy.Client instance

    def post_tweet(self, post_data: Dict[str, Any]) -> TwitterPostResponse:
        try:
            validated_post = SocialMediaPost(**post_data)
            tweet_data = self.client.post(validated_post.content) # client.post handles v2 API call

            # The tweet_data from client.post (tweepy.Client.create_tweet) will be simpler:
            # {"id": "...", "text": "..."}
            # We need to ensure our TwitterPostResponse model is compatible.
            # It's better to fetch full tweet details if needed after posting, but for this,
            # we'll map directly. created_at is not in the immediate create_tweet response.
            # If you need created_at and author_id for the post response, you'd need to do a
            # separate tweet lookup. For now, we'll keep it simple.

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
            # timeline_response_data is a list of tweet objects with 'created_at' and 'author_id'
            # as requested in client.get_home_timeline.
            
            # If we wanted to include user details in the Timeline model, we'd need to process
            # response.includes from client.get_home_timeline in TwitterClient.
            # For now, let's assume the Tweet model is sufficient with its fields.
            
            tweets = []
            for t_data in timeline_response_data:
                # Ensure created_at is parsed correctly (Tweepy v2 responses often return ISO 8601 strings)
                try:
                    t_data['created_at'] = datetime.fromisoformat(t_data['created_at'].replace('Z', '+00:00'))
                except (TypeError, ValueError):
                    pass # Handle cases where created_at might be missing or not in expected format

                tweets.append(Tweet(**t_data))

            return Timeline(tweets=tweets, count=len(tweets))
        except APIError as e:
            raise APIError(f"Error fetching timeline: {e}")
        except Exception as e:
            raise APIError(f"An unexpected error occurred while fetching timeline: {e}")