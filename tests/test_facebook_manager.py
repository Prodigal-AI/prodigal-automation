import unittest
from unittest.mock import MagicMock, patch
import os
import sys
import datetime
import time

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from prodigal_automation.facebook_manager import FacebookManager
from prodigal_automation.auth import FacebookAuth
# No need to import FacebookClient or ContentGenerator directly here,
# as we will mock them.

class TestFacebookManager(unittest.TestCase):

    def setUp(self):
        self.mock_access_token = "TEST_ACCESS_TOKEN"
        self.mock_page_id = "TEST_PAGE_ID"
        self.mock_gemini_api_key = "TEST_GEMINI_KEY"

        self.mock_auth = FacebookAuth(
            access_token=self.mock_access_token,
            page_id=self.mock_page_id
        )

        # Mock the FacebookClient and ContentGenerator
        # We need to mock where they are imported in facebook_manager.py
        self.mock_facebook_client_class = MagicMock()
        self.mock_content_generator_class = MagicMock()

        # Mock instances that will be returned when the classes are instantiated
        self.mock_client_instance = self.mock_facebook_client_class.return_value
        self.mock_content_generator_instance = self.mock_content_generator_class.return_value

        # Configure mock_client_instance if it has attributes/methods used by FacebookManager's init
        self.mock_client_instance.auth = self.mock_auth # Ensure auth property is available
        self.mock_client_instance.page_id = self.mock_page_id # Ensure page_id is available
        self.mock_client_instance.initialize.return_value = self.mock_client_instance # For chainable .initialize()

    # We need to patch the classes where they are imported in facebook_manager.py
    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_init_production_mode(self, MockContentGenerator, MockFacebookClient):
        """Test initialization in production mode (with auth object and API key)."""
        MockFacebookClient.return_value = self.mock_client_instance
        MockContentGenerator.return_value = self.mock_content_generator_instance

        manager = FacebookManager(self.mock_auth, self.mock_gemini_api_key)

        MockFacebookClient.assert_called_once_with(self.mock_auth)
        self.mock_client_instance.initialize.assert_called_once()
        MockContentGenerator.assert_called_once_with(self.mock_gemini_api_key)

        self.assertEqual(manager.client, self.mock_client_instance)
        self.assertEqual(manager.content_generator, self.mock_content_generator_instance)
        self.assertEqual(manager.page_id, self.mock_page_id)

    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_init_test_mode(self, MockContentGenerator, MockFacebookClient):
        """Test initialization in test mode (with mock client and generator)."""
        # In test mode, we pass already instantiated mocks
        mock_test_client = MagicMock()
        mock_test_client.auth.page_id = "TEST_PAGE_ID_MOCK" # Simulate auth property on mock client
        mock_test_generator = MagicMock()

        manager = FacebookManager(mock_test_client, mock_test_generator)

        MockFacebookClient.assert_not_called() # Should not create new client
        MockContentGenerator.assert_not_called() # Should not create new generator

        self.assertEqual(manager.client, mock_test_client)
        self.assertEqual(manager.content_generator, mock_test_generator)
        self.assertEqual(manager.page_id, "TEST_PAGE_ID_MOCK")

    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_create_post_success(self, MockContentGenerator, MockFacebookClient):
        """Test successful post creation."""
        MockFacebookClient.return_value = self.mock_client_instance
        MockContentGenerator.return_value = self.mock_content_generator_instance

        # Configure behavior of mocked dependencies
        self.mock_content_generator_instance.generate_simple_content.return_value = "Generated test content."
        self.mock_client_instance.put_object.return_value = {"id": "post_id_123"}

        manager = FacebookManager(self.mock_auth, self.mock_gemini_api_key)
        topic = "AI in healthcare"
        result = manager.create_post(topic)

        self.mock_content_generator_instance.generate_simple_content.assert_called_once_with(topic)
        self.mock_client_instance.put_object.assert_called_once_with(
            parent_object=self.mock_page_id,
            connection_name='feed',
            message="Generated test content."
        )
        self.assertEqual(result, {"success": True, "post_id": "post_id_123", "content": "Generated test content."})

    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_create_post_api_error(self, MockContentGenerator, MockFacebookClient):
        """Test create_post handles Facebook API errors."""
        MockFacebookClient.return_value = self.mock_client_instance
        MockContentGenerator.return_value = self.mock_content_generator_instance

        self.mock_content_generator_instance.generate_simple_content.return_value = "Generated test content."
        # Simulate Facebook API error
        import facebook # Need to import facebook here to get GraphAPIError
        self.mock_client_instance.put_object.side_effect = facebook.GraphAPIError('Mock FB API Error')

        manager = FacebookManager(self.mock_auth, self.mock_gemini_api_key)
        topic = "AI in healthcare"
        result = manager.create_post(topic)

        self.assertFalse(result["success"])
        self.assertIn("Facebook API error: Mock FB API Error", result["error"])

    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_create_post_no_page_id(self, MockContentGenerator, MockFacebookClient):
        """Test create_post handles missing page ID."""
        # Create an auth object with no page_id
        auth_no_page_id = FacebookAuth(access_token=self.mock_access_token, page_id=None)
        MockFacebookClient.return_value.auth = auth_no_page_id # Ensure mock client uses this auth
        MockFacebookClient.return_value.page_id = None # Explicitly set page_id on mock client to None

        MockContentGenerator.return_value = self.mock_content_generator_instance
        self.mock_content_generator_instance.generate_simple_content.return_value = "Test content."

        manager = FacebookManager(auth_no_page_id, self.mock_gemini_api_key)
        topic = "test"
        result = manager.create_post(topic)

        self.assertFalse(result["success"])
        self.assertIn("Facebook Page ID is required to post.", result["error"])
        self.mock_client_instance.put_object.assert_not_called() # Should not attempt to post

    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_create_post_scheduled_success(self, MockContentGenerator, MockFacebookClient):
        """Test successful scheduled post creation."""
        MockFacebookClient.return_value = self.mock_client_instance
        MockContentGenerator.return_value = self.mock_content_generator_instance

        self.mock_content_generator_instance.generate_simple_content.return_value = "Scheduled test content."
        self.mock_client_instance.put_object.return_value = {"id": "scheduled_post_id_456"}

        manager = FacebookManager(self.mock_auth, self.mock_gemini_api_key)
        topic = "Future tech"
        # Schedule for 1 hour from now
        scheduled_time = int(time.time()) + 3600
        result = manager.create_post(topic, scheduled_publish_time=scheduled_time)

        self.mock_client_instance.put_object.assert_called_once_with(
            parent_object=self.mock_page_id,
            connection_name='feed',
            message="Scheduled test content.",
            published=False,
            scheduled_publish_time=scheduled_time
        )
        self.assertEqual(result["post_id"], "scheduled_post_id_456")
        self.assertTrue(result["success"])

    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_post_image_success(self, MockContentGenerator, MockFacebookClient):
        """Test successful image post."""
        MockFacebookClient.return_value = self.mock_client_instance
        MockContentGenerator.return_value = self.mock_content_generator_instance

        self.mock_client_instance.put_object.return_value = {"id": "photo_id_789"}
        manager = FacebookManager(self.mock_auth, self.mock_gemini_api_key)
        
        message = "Test image caption"
        image_url = "http://example.com/test.jpg"
        result = manager.post_image(message, image_url)

        self.mock_client_instance.put_object.assert_called_once_with(
            parent_object=self.mock_page_id,
            connection_name='photos',
            url=image_url,
            message=message,
            published=True,
            access_token=self.mock_access_token
        )
        self.assertTrue(result["success"])
        self.assertEqual(result["post_id"], "photo_id_789")
        self.assertEqual(result["image_url"], image_url)

    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_get_page_metrics_success(self, MockContentGenerator, MockFacebookClient):
        """Test successful retrieval of page insights."""
        MockFacebookClient.return_value = self.mock_client_instance
        MockContentGenerator.return_value = self.mock_content_generator_instance

        expected_insights = {"data": [{"name": "page_impressions", "values": [{"value": 500}]}]}
        self.mock_client_instance.get_page_insights.return_value = expected_insights

        manager = FacebookManager(self.mock_auth, self.mock_gemini_api_key)
        metrics = ['page_impressions']
        period = 'day'
        since = int(datetime.datetime(2025, 1, 1).timestamp())
        until = int(datetime.datetime(2025, 1, 2).timestamp())

        result = manager.get_page_metrics(metrics, period, since, until)

        self.mock_client_instance.get_page_insights.assert_called_once_with(
            self.mock_page_id, metrics, period, since, until
        )
        self.assertEqual(result, expected_insights)


    @patch('prodigal_automation.facebook_manager.FacebookClient')
    @patch('prodigal_automation.facebook_manager.ContentGenerator')
    def test_delete_post_success(self, MockContentGenerator, MockFacebookClient):
        """Test successful post deletion."""
        MockFacebookClient.return_value = self.mock_client_instance
        MockContentGenerator.return_value = self.mock_content_generator_instance

        self.mock_client_instance.delete_object.return_value = {"success": True, "message": "Object deleted."}
        manager = FacebookManager(self.mock_auth, self.mock_gemini_api_key)
        
        post_id = "test_post_to_delete"
        result = manager.delete_post(post_id)

        self.mock_client_instance.delete_object.assert_called_once_with(post_id)
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Object deleted.")


if __name__ == '__main__':
    # You might need to import facebook here if GraphAPIError is directly referenced
    # and not otherwise mocked or available in the test environment.
    try:
        import facebook
    except ImportError:
        # Create a dummy mock for the 'facebook' module if it's not installed
        # This is for scenarios where FacebookManager directly catches facebook.GraphAPIError
        from unittest.mock import Mock
        sys.modules['facebook'] = Mock()
        sys.modules['facebook.GraphAPIError'] = type('GraphAPIError', (Exception,), {})

    unittest.main(argv=['first-arg-is-ignored'], exit=False)