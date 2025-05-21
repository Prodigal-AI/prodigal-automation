import os
import tweepy
from prodigal_automation.tools import register_tool

# Pull your v2 bearer token from the environment
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
if not BEARER_TOKEN:
    raise RuntimeError("Please set TWITTER_BEARER_TOKEN in your env to a v2 bearer token")

# Initialize a global Tweepy client
_client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

def get_user_timeline(username: str, max_results: int = 5) -> dict:
    """
    Fetch the most recent tweets from a user timeline.
    Uses Tweepy Client.user_timeline under the hood.
    """
    # Look up the user’s ID first
    user = _client.get_user(username=username)
    if not user.data:
        raise RuntimeError(f"User @{username} not found")
    user_id = user.data.id

    # Now fetch tweets for that user
    resp = _client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=["created_at", "text"]
    )
    return resp.data or []

def get_tweet(tweet_id: str) -> dict:
    """
    Fetch a single tweet by ID.
    """
    resp = _client.get_tweet(
        id=tweet_id,
        tweet_fields=["created_at", "text"]
    )
    if not resp.data:
        raise RuntimeError(f"Tweet {tweet_id} not found")
    return resp.data

# Register these functions as “tools”:
register_tool("twitter_get_user_timeline", get_user_timeline)
register_tool("twitter_get_tweet", get_tweet)
