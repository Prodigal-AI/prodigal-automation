import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import the actual classes we want to test
from prodigal_automation.client import FacebookClient
from prodigal_automation.auth import FacebookAuth

# Import the third-party library we will mock
# We don't import 'facebook' at the top level of client.py anymore due to circular import fix.
# So, when patching, we need to patch where it's *used*, which is inside FacebookClient.initialize().

class TestFacebookClient(unittest.TestCase):

    def setUp(self):
        # Common setup for all tests in this class
        self.mock_access_token = "TEST_ACCESS_TOKEN"
        self.mock_page_id = "TEST_PAGE_ID"
        self.mock_auth = FacebookAuth(
            access_token=self.mock_access_token,
            page_id=self.mock_page_id
        )

    # Use patch.object to mock the 'facebook' module within the 'client' module
    # Specifically, we mock the GraphAPI class that gets instantiated
    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_initialize_success(self, MockGraphAPI):
        """Test successful initialization of FacebookClient."""
        # Create a mock instance for GraphAPI that initialize() will return
        mock_graph_instance = MagicMock()
        MockGraphAPI.return_value = mock_graph_instance

        client = FacebookClient(self.mock_auth)
        initialized_client = client.initialize()

        # Assert that GraphAPI was called with the correct access token
        MockGraphAPI.assert_called_once_with(access_token=self.mock_access_token)
        # Assert that initialize returns the mock GraphAPI instance
        self.assertEqual(initialized_client, mock_graph_instance)
        # Assert that the internal self.client is set
        self.assertEqual(client.client, mock_graph_instance)
        # Assert that page_id is set on the client
        self.assertEqual(client.page_id, self.mock_page_id)

    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_initialize_no_access_token(self, MockGraphAPI):
        """Test initialization failure if no access token is provided."""
        # Create an auth object with no access token
        auth_no_token = FacebookAuth(access_token="", page_id="some_id")
        client = FacebookClient(auth_no_token)

        with self.assertRaisesRegex(ValueError, "Facebook Access Token not provided."):
            client.initialize()

        # Ensure GraphAPI was never called
        MockGraphAPI.assert_not_called()

    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_initialize_graph_api_error(self, MockGraphAPI):
        """Test initialization failure if GraphAPI raises an error."""
        # Simulate GraphAPI raising an error during instantiation
        MockGraphAPI.side_effect = facebook.GraphAPIError('Test API Error')

        client = FacebookClient(self.mock_auth)

        with self.assertRaisesRegex(ConnectionError, "Failed to initialize Facebook client: Test API Error"):
            client.initialize()

        MockGraphAPI.assert_called_once_with(access_token=self.mock_access_token)

    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_put_object_success(self, MockGraphAPI):
        """Test put_object for successful post creation."""
        mock_graph_instance = MockGraphAPI.return_value
        # Configure the return value of get_connections (or put_object for your case)
        mock_graph_instance.put_object.return_value = {"id": "12345_67890", "post_id": "67890"}

        client = FacebookClient(self.mock_auth)
        client.initialize() # Initialize the client to set self.client

        parent_object = "test_page_id"
        connection_name = "feed"
        message = "Hello from test!"

        result = client.put_object(parent_object, connection_name, message=message)

        # Assert that put_object was called correctly on the mock GraphAPI instance
        mock_graph_instance.put_object.assert_called_once_with(
            parent_object, connection_name, access_token=self.mock_access_token, message=message
        )
        self.assertEqual(result, {"id": "12345_67890", "post_id": "67890"})

    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_put_object_not_initialized(self, MockGraphAPI):
        """Test put_object raises error if client is not initialized."""
        client = FacebookClient(self.mock_auth) # Not calling initialize()

        with self.assertRaisesRegex(RuntimeError, "FacebookClient is not initialized. Call .initialize() first."):
            client.put_object("page_id", "feed", message="test")

        MockGraphAPI.assert_not_called() # Ensure GraphAPI was never instantiated

    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_get_page_insights_success(self, MockGraphAPI):
        """Test get_page_insights for successful data retrieval."""
        mock_graph_instance = MockGraphAPI.return_value
        expected_insights = {
            "data": [
                {"name": "page_impressions_unique", "period": "day", "values": [{"value": 100}]},
                {"name": "page_engaged_users", "period": "day", "values": [{"value": 50}]}
            ]
        }
        mock_graph_instance.get_connections.return_value = expected_insights

        client = FacebookClient(self.mock_auth)
        client.initialize()

        metrics = ['page_impressions_unique', 'page_engaged_users']
        period = 'day'
        since = 1678886400 # Example timestamp
        until = 1678972799 # Example timestamp

        result = client.get_page_insights(self.mock_page_id, metrics, period, since, until)

        mock_graph_instance.get_connections.assert_called_once_with(
            self.mock_page_id,
            'insights',
            metric=','.join(metrics),
            period=period,
            since=since,
            until=until,
            access_token=self.mock_access_token
        )
        self.assertEqual(result, expected_insights)

    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_get_page_insights_error(self, MockGraphAPI):
        """Test get_page_insights handles API errors."""
        mock_graph_instance = MockGraphAPI.return_value
        mock_graph_instance.get_connections.side_effect = facebook.GraphAPIError('Insights error')

        client = FacebookClient(self.mock_auth)
        client.initialize()

        metrics = ['page_impressions_unique']
        result = client.get_page_insights(self.mock_page_id, metrics)

        self.assertIn("error", result)
        self.assertIn("Insights error", result["error"])


    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_delete_object_success(self, MockGraphAPI):
        """Test delete_object for successful deletion."""
        mock_graph_instance = MockGraphAPI.return_value
        mock_graph_instance.delete_object.return_value = {"success": True}

        client = FacebookClient(self.mock_auth)
        client.initialize()

        object_id = "12345_67890"
        result = client.delete_object(object_id)

        mock_graph_instance.delete_object.assert_called_once_with(object_id)
        self.assertEqual(result, {"success": True, "message": f"Object {object_id} deleted successfully."})

    @patch('prodigal_automation.client.facebook.GraphAPI')
    def test_delete_object_failure(self, MockGraphAPI):
        """Test delete_object handles API errors."""
        mock_graph_instance = MockGraphAPI.return_value
        mock_graph_instance.delete_object.side_effect = facebook.GraphAPIError('Delete failed')

        client = FacebookClient(self.mock_auth)
        client.initialize()

        object_id = "12345_67890"
        result = client.delete_object(object_id)

        self.assertIn("success", result)
        self.assertFalse(result["success"])
        self.assertIn("error", result)
        self.assertIn("Delete failed", result["error"])


if __name__ == '__main__':
    try:
        import facebook
    except ImportError:
        # Create a dummy mock for the 'facebook' module if it's not installed
        # so unittest.mock can find something to patch.
        # This is important if your `client.py` has `import facebook` inside `initialize()`.
        from unittest.mock import Mock
        sys.modules['facebook'] = Mock()
        sys.modules['facebook.GraphAPIError'] = type('GraphAPIError', (Exception,), {}) # Mock the specific exception

    unittest.main(argv=['first-arg-is-ignored'], exit=False)