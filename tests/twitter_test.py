import pytest
from unittest.mock import MagicMock, patch
from prodigal_automation.twitter.twitter import TwitterAutomator
from prodigal_automation.core.errors import SocialMediaError
from prodigal_automation.core.models import TwitterPostResponse, Timeline, Tweet
from datetime import datetime

# Mock credentials for testing
MOCK_CREDENTIALS = {
    "consumer_key": "mock_consumer_key",
    "consumer_secret": "mock_consumer_secret",
    "access_token": "mock_access_token",
    "access_token_secret": "mock_access_token_secret",
}

@pytest.fixture
def mock_twitter_automator():
    with patch('src.core.auth.DotEnvAuthenticator.get_twitter_credentials') as mock_get_creds:
        mock_creds_obj = MagicMock()
        mock_creds_obj.consumer_key.get_secret_value.return_value = MOCK_CREDENTIALS["consumer_key"]
        mock_creds_obj.consumer_secret.get_secret_value.return_value = MOCK_CREDENTIALS["consumer_secret"]
        mock_creds_obj.access_token.get_secret_value.return_value = MOCK_CREDENTIALS["access_token"]
        mock_creds_obj.access_token_secret.get_secret_value.return_value = MOCK_CREDENTIALS["access_token_secret"]
        mock_get_creds.return_value = mock_creds_obj

        # Mock tweepy.Client methods
        with patch('tweepy.Client') as MockTweepyClient:
            mock_client_instance = MockTweepyClient.return_value # This is the mock tweepy.Client instance

            with patch('src.core.client.TwitterClient.connect', return_value=mock_client_instance) as mock_connect:
                # Mock create_tweet method on the mock_client_instance
                mock_client_instance.create_tweet.return_value.data = {
                    "id": "12345",
                    "text": "Test tweet",
                }

                # Mock get_me for timeline
                mock_client_instance.get_me.return_value.data = MagicMock(id="test_user_id")

                # Mock get_home_timeline for timeline
                mock_client_instance.get_home_timeline.return_value.data = [
                    {"id": "t1", "text": "Tweet 1", "author_id": "u1", "created_at": "2023-01-01T10:00:00.000Z"},
                    {"id": "t2", "text": "Tweet 2", "author_id": "u2", "created_at": "2023-01-01T11:00:00.000Z"},
                ]
                mock_client_instance.get_home_timeline.return_value.includes = {"users": []} # No users needed for these tests
                mock_client_instance.get_home_timeline.return_value.meta = {"result_count": 2}


                automator = TwitterAutomator()
                yield automator, mock_client_instance.create_tweet, mock_client_instance.get_home_timeline, mock_client_instance.get_me


def test_post_tweet_success(mock_twitter_automator):
    automator, mock_create_tweet, _, _ = mock_twitter_automator
    content = "Hello world!"
    response = automator.post(content)

    mock_create_tweet.assert_called_once_with(text=content)
    assert isinstance(response, TwitterPostResponse)
    assert response.id == "12345"
    assert response.text == "Test tweet"

def test_post_tweet_empty_content_raises_error(mock_twitter_automator):
    automator, _, _, _ = mock_twitter_automator
    with pytest.raises(SocialMediaError, match="Invalid post data"):
        automator.post("")

def test_get_timeline_success(mock_twitter_automator):
    automator, _, mock_get_home_timeline, mock_get_me = mock_twitter_automator

    timeline = automator.get_timeline(count=2)

    mock_get_me.assert_called_once()
    mock_get_home_timeline.assert_called_once_with(
        user_id="test_user_id",
        max_results=2,
        tweet_fields=["created_at", "author_id"],
        expansions=["author_id"]
    )
    assert isinstance(timeline, Timeline)
    assert timeline.count == 2
    assert len(timeline.tweets) == 2
    assert isinstance(timeline.tweets[0], Tweet)
    assert timeline.tweets[0].id == "t1"
    assert timeline.tweets[0].text == "Tweet 1"
    assert timeline.tweets[0].author_id == "u1"
    assert isinstance(timeline.tweets[0].created_at, datetime)

def test_get_timeline_api_error(mock_twitter_automator):
    automator, _, mock_get_home_timeline, mock_get_me = mock_twitter_automator
    from tweepy.errors import TweepyException
    mock_get_home_timeline.side_effect = TweepyException("Rate limit exceeded")

    with pytest.raises(SocialMediaError, match="Error during Twitter timeline fetch"):
        automator.get_timeline(count=5)