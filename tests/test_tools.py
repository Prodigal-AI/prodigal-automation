# tests/test_tools.py

import pytest

from prodigal_automation.tools import ContentGenerator, ContentRequest


def test_content_request_validation():
    # Valid topic with 2 words
    req = ContentRequest(topic="AI technology", length=100)
    assert req.topic == "AI technology"

    # Topic with less than 2 words should raise error
    with pytest.raises(ValueError):
        ContentRequest(topic="AI")


def test_generate_tweet(monkeypatch):
    # Mock the generative model's generate_content method
    class DummyResponse:
        text = "This is a generated tweet."

    class DummyModel:
        def generate_content(self, prompt):
            return DummyResponse()

    gen = ContentGenerator(api_key="fake_api_key")
    gen.model = DummyModel()

    request = ContentRequest(topic="test topic", length=100)
    tweet = gen.generate_tweet(request)
    assert isinstance(tweet, str)
    assert tweet == "This is a generated tweet."
