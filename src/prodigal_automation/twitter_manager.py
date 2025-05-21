# src/prodigal_automation/twitter_manager.py

import threading
import tweepy
from typing import Dict

_TENANT_LOCK = threading.Lock()
_TENANT_CLIENTS: Dict[str, tweepy.Client] = {}

def register_twitter_credentials(
    tenant_id: str,
    *,
    bearer_token: str = None,
    api_key: str = None,
    api_secret: str = None,
    access_token: str = None,
    access_secret: str = None,
):
    """
    Call at login/orchestrator startup to store each tenant’s Twitter credentials.
    """
    with _TENANT_LOCK:
        if bearer_token:
            client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
        else:
            # OAuth1 user-context flow
            auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
            client = tweepy.Client(
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=access_token,
                access_token_secret=access_secret,
                wait_on_rate_limit=True,
            )
        _TENANT_CLIENTS[tenant_id] = client

def get_client_for(tenant_id: str) -> tweepy.Client:
    client = _TENANT_CLIENTS.get(tenant_id)
    if client is None:
        raise RuntimeError(f"No Twitter client registered for tenant '{tenant_id}'")
    return client
