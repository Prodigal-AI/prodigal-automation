import pytest
from fastapi import Request
from prodigal_automation.auth import require_token, AuthError

class DummyRequest:
    def __init__(self, headers):
        self.headers = headers

def test_no_token():
    with pytest.raises(AuthError):
        require_token(DummyRequest({}))

def test_bad_token():
    with pytest.raises(AuthError):
        require_token(DummyRequest({"Authorization":"Bearer bad"}))

def test_good_token():
    # update expected_token in auth.py for test
    token = "expected_token"
    req = DummyRequest({"Authorization":f"Bearer {token}"})
    assert require_token(req) == token
