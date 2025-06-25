import os
import sys
from unittest.mock import Mock

import pytest

from prodigal_automation.auth import FacebookAuth
from prodigal_automation.facebook_manager import FacebookManager

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sys.modules["facebook"] = Mock()
sys.modules["facebook.GraphAPIError"] = type("GraphAPIError", (Exception,), {})


@pytest.fixture
def mock_auth_prod():
    """Provides a mock FacebookAuth instance for production-like setup."""
    return FacebookAuth(access_token="TEST_ACCESS_TOKEN", page_id="TEST_PAGE_ID")


@pytest.fixture
def mock_facebook_client_class(mocker):
    """Mocks the FacebookClient class."""
    return mocker.patch("prodigal_automation.facebook_manager.FacebookClient")


@pytest.fixture
def mock_content_generator_class(mocker):
    """Mocks the ContentGenerator class."""
    return mocker.patch("prodigal_automation.facebook_manager.ContentGenerator")


@pytest.fixture
def mock_client_instance(mock_facebook_client_class, mock_auth_prod):
    """Provides a mock FacebookClient instance."""
    instance = mock_facebook_client_class.return_value
    instance.auth = mock_auth_prod
    instance.page_id = mock_auth_prod.page_id
    instance.initialize.return_value = instance  # For chainable .initialize()
    return instance


@pytest.fixture
def mock_content_generator_instance(mock_content_generator_class):
    """Provides a mock ContentGenerator instance."""
    return mock_content_generator_class.return_value


@pytest.fixture
def facebook_manager_prod(
    mock_auth_prod,
    mock_facebook_client_class,
    mock_content_generator_class,
    mock_client_instance,
    mock_content_generator_instance,
):
    """Provides a FacebookManager instance initialized for production mode."""
    return FacebookManager(mock_auth_prod, "TEST_GEMINI_KEY")


@pytest.fixture
def facebook_manager_test(mocker):
    # Provides a FacebookManager instance initialized for test mode (with explicit mocks). # noqa
    mock_test_client = mocker.MagicMock()
    mock_test_client.auth.page_id = (
        "TEST_PAGE_ID_MOCK"  # Simulate auth property on mock client
    )
    mock_test_generator = mocker.MagicMock()
    return FacebookManager(mock_test_client, mock_test_generator)
