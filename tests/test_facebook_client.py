import os
import sys

# Create a dummy mock for the 'facebook' module if it's not installed
# This is useful if GraphAPIError is directly referenced for type checking or catching
from unittest.mock import Mock

# This import is usually only needed if you specifically catch facebook.GraphAPIError
import facebook
import pytest

from prodigal_automation.auth import FacebookAuth

# Import the actual classes we want to test
from prodigal_automation.client import FacebookClient

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sys.modules["facebook"] = Mock()
sys.modules["facebook.GraphAPIError"] = type(
    "GraphAPIError", (Exception,), {}
)  # Mock the specific exception


@pytest.fixture
def mock_auth():
    """Provides a mock FacebookAuth instance."""
    return FacebookAuth(access_token="TEST_ACCESS_TOKEN", page_id="TEST_PAGE_ID")


@pytest.fixture
def facebook_client(mock_auth, mocker):
    """Provides an initialized FacebookClient with a mocked GraphAPI."""
    # Mock the facebook.GraphAPI class when it's instantiated
    mock_graph_api_class = mocker.patch("prodigal_automation.client.facebook.GraphAPI")
    mock_graph_api_instance = mock_graph_api_class.return_value

    client = FacebookClient(mock_auth)
    client.initialize()  # Initialize to set self.client to the mock_graph_api_instance
    return client, mock_graph_api_instance  # Return both for assertions


def test_initialize_success(mock_auth, mocker):
    """Test successful initialization of FacebookClient."""
    mock_graph_api_class = mocker.patch("prodigal_automation.client.facebook.GraphAPI")
    mock_graph_instance = mock_graph_api_class.return_value

    client = FacebookClient(mock_auth)
    initialized_client = client.initialize()

    # Assert that GraphAPI was called with the correct access token
    mock_graph_api_class.assert_called_once_with(access_token=mock_auth.access_token)
    # Assert that initialize returns the mock GraphAPI instance
    assert initialized_client == mock_graph_instance
    # Assert that the internal self.client is set
    assert client.client == mock_graph_instance
    # Assert that page_id is set on the client
    assert client.page_id == mock_auth.page_id


def test_initialize_no_access_token(mocker):
    """Test initialization failure if no access token is provided."""
    auth_no_token = FacebookAuth(access_token="", page_id="some_id")
    client = FacebookClient(auth_no_token)

    with pytest.raises(ValueError, match="Facebook Access Token not provided."):
        client.initialize()

    # Ensure GraphAPI was never called
    mocker.patch("prodigal_automation.client.facebook.GraphAPI").assert_not_called()


def test_put_object_success(facebook_client):
    """Test put_object for successful post creation."""
    client, mock_graph_instance = facebook_client
    mock_graph_instance.put_object.return_value = {
        "id": "12345_67890",
        "post_id": "67890",
    }

    parent_object = "test_page_id"
    connection_name = "feed"
    message = "Hello from test!"

    result = client.put_object(parent_object, connection_name, message=message)

    # Assert that put_object was called correctly on the mock GraphAPI instance
    mock_graph_instance.put_object.assert_called_once_with(
        parent_object,
        connection_name,
        access_token=client.auth.access_token,
        message=message,
    )
    assert result == {"id": "12345_67890", "post_id": "67890"}


def test_put_object_not_initialized(mock_auth, mocker):
    """Test put_object raises error if client is not initialized."""
    client = FacebookClient(mock_auth)  # Not calling initialize()

    with pytest.raises(RuntimeError):
        client.put_object("page_id", "feed", message="test")

    mocker.patch("prodigal_automation.client.facebook.GraphAPI").assert_not_called()


def test_get_page_insights_success(facebook_client):
    """Test get_page_insights for successful data retrieval."""
    client, mock_graph_instance = facebook_client
    expected_insights = {
        "data": [
            {
                "name": "page_impressions_unique",
                "period": "day",
                "values": [{"value": 100}],
            },
            {"name": "page_engaged_users", "period": "day", "values": [{"value": 50}]},
        ]
    }
    mock_graph_instance.get_connections.return_value = expected_insights

    metrics = ["page_impressions_unique", "page_engaged_users"]
    period = "day"
    since = 1678886400  # Example timestamp
    until = 1678972799  # Example timestamp

    result = client.get_page_insights(client.page_id, metrics, period, since, until)

    mock_graph_instance.get_connections.assert_called_once_with(
        client.page_id,
        "insights",
        metric=",".join(metrics),
        period=period,
        since=since,
        until=until,
        access_token=client.auth.access_token,
    )
    assert result == expected_insights


def test_get_page_insights_error(facebook_client):
    """Test get_page_insights handles API errors."""
    client, mock_graph_instance = facebook_client
    mock_graph_instance.get_connections.side_effect = facebook.GraphAPIError(
        "Insights error"
    )

    metrics = ["page_impressions_unique"]
    result = client.get_page_insights(client.page_id, metrics)

    assert "error" in result
    assert "Insights error" in result["error"]


def test_delete_object_success(facebook_client):
    """Test delete_object for successful deletion."""
    client, mock_graph_instance = facebook_client
    mock_graph_instance.delete_object.return_value = {"success": True}

    object_id = "12345_67890"
    result = client.delete_object(object_id)

    mock_graph_instance.delete_object.assert_called_once_with(object_id)
    assert result == {
        "success": True,
        "message": f"Object {object_id} deleted successfully.",
    }


def test_delete_object_failure(facebook_client):
    """Test delete_object handles API errors."""
    client, mock_graph_instance = facebook_client
    mock_graph_instance.delete_object.side_effect = facebook.GraphAPIError(
        "Delete failed"
    )

    object_id = "12345_67890"
    result = client.delete_object(object_id)

    assert not result["success"]
    assert "error" in result
    assert "Delete failed" in result["error"]
