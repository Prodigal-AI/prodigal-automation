import pytest
from unittest.mock import MagicMock, patch
from prodigal_automation.facebook.facebook import FacebookAutomator
from prodigal_automation.core.errors import SocialMediaError, APIError
from prodigal_automation.core.models import FacebookPostResponse
import facebook

MOCK_FB_CREDENTIALS = {
    "access_token": "mock_facebook_access_token",
    "page_id": "mock_facebook_page_id",
}

@pytest.fixture
def mock_facebook_automator():
    with patch('src.core.auth.DotEnvAuthenticator.get_facebook_credentials') as mock_get_creds:
        mock_creds_obj = MagicMock()
        mock_creds_obj.access_token.get_secret_value.return_value = MOCK_FB_CREDENTIALS["access_token"]
        mock_creds_obj.page_id = MagicMock(get_secret_value=MagicMock(return_value=MOCK_FB_CREDENTIALS["page_id"]))
        mock_get_creds.return_value = mock_creds_obj

        with patch('facebook.GraphAPI') as MockGraphAPI:
            mock_graph_api_instance = MockGraphAPI.return_value # This is the mock facebook.GraphAPI instance
            mock_graph_api_instance.put_object.return_value = {
                "id": f"{MOCK_FB_CREDENTIALS['page_id']}_1234567890",
            }

            # For connect method, we can mock get_object("me") if needed
            mock_graph_api_instance.get_object.return_value = {"id": "test_user_id", "name": "Test User"}


            automator = FacebookAutomator()
            yield automator, mock_graph_api_instance.put_object, mock_graph_api_instance.get_object


def test_facebook_post_success(mock_facebook_automator):
    automator, mock_put_object, _ = mock_facebook_automator
    content = "Hello from Facebook test!"
    response = automator.post(content)

    mock_put_object.assert_called_once_with(
        parent_object=MOCK_FB_CREDENTIALS['page_id'],
        connection_name="feed",
        message=content
    )
    assert isinstance(response, FacebookPostResponse)
    assert response.id == f"{MOCK_FB_CREDENTIALS['page_id']}_1234567890"
    assert response.post_id == "1234567890"
    assert response.message == content

def test_facebook_post_empty_content_raises_error(mock_facebook_automator):
    automator, _, _ = mock_facebook_automator
    with pytest.raises(SocialMediaError, match="Invalid post data"):
        automator.post("")

def test_facebook_post_api_error(mock_facebook_automator):
    automator, mock_put_object, _ = mock_facebook_automator
    mock_put_object.side_effect = facebook.GraphAPIError("Permissions error")

    with pytest.raises(SocialMediaError, match="Error posting to Facebook"):
        automator.post("Test post with error")