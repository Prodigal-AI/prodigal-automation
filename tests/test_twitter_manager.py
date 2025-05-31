from unittest.mock import MagicMock

import pytest

from src.prodigal_automation.twitter_manager import TwitterManager


class TestTwitterManager:
    def test_create_tweet_success(self):
        # Mock the Twitter API client and its create_tweet method
        mock_twitter_client = MagicMock()
        mock_tweet_response = MagicMock()
        mock_tweet_response.id = 1234567890  # Example tweet ID
        mock_tweet_response.text = "Mock tweet content"
        mock_twitter_client.create_tweet.return_value = mock_tweet_response

        # Mock the ContentGenerator and its method
        mock_content_generator = MagicMock()
        # Mock the correct method name that TwitterManager actually calls
        mock_content_generator.generate_simple_content.return_value = (
            "Mock tweet content"
        )

        # Instantiate TwitterManager with the mocked dependencies
        twitter_manager = TwitterManager(
            mock_twitter_client,
            mock_content_generator,
        )

        # Define test input
        test_topic = "Test Topic"

        # Call the method under test with **one** argument
        tweet_id = twitter_manager.create_tweet(test_topic)

        # Assertions
        # Check if the correct method was called with the correct argument
        mock_content_generator.generate_simple_content.assert_called_once_with(
            test_topic
        )

        # Check if create_tweet was called with the generated content
        mock_twitter_client.create_tweet.assert_called_once_with(
            text="Mock tweet content"
        )

        # Check if the returned tweet_id is correct
        assert tweet_id == mock_tweet_response.id

    def test_create_tweet_api_error(self):
        # Mock the Twitter API client to raise an exception
        mock_twitter_client = MagicMock()
        mock_twitter_client.create_tweet.side_effect = Exception(
            "Twitter API Error"
        )

        # Mock the ContentGenerator
        mock_content_generator = MagicMock()
        mock_content_generator.generate_simple_content.return_value = (
            "Mock tweet content"
        )

        # Instantiate TwitterManager with the mocked dependencies
        twitter_manager = TwitterManager(
            mock_twitter_client,
            mock_content_generator,
        )

        # Test that the exception is properly handled or raised
        with pytest.raises(Exception, match="Twitter API Error"):
            twitter_manager.create_tweet("Test Topic")
