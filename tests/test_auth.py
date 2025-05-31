# tests/test_auth.py

import pytest

from prodigal_automation.auth import TwitterAuth


def test_bearer_token_validation():
    # valid token
    auth = TwitterAuth(bearer_token="validbearertoken123")
    assert auth.has_bearer_token()

    # short token should raise validation error
    with pytest.raises(ValueError):
        TwitterAuth(bearer_token="short")


def test_oauth_credentials_check():
    auth = TwitterAuth(
        api_key="key",
        api_key_secret="secret",
        access_token="token",
        access_token_secret="secret_token",
    )
    assert auth.has_oauth_credentials()

    auth = TwitterAuth()
    assert not auth.has_oauth_credentials()
