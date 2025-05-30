import threading
import requests
from typing import Dict

_TENANT_LOCK = threading.Lock()
_TENANT_CLIENTS: Dict[str, requests.Session] = {} # Or a custom Instagram client

def register_instagram_credentials(
    tenant_id: str,
    *,
    access_token: str,
):
    """
    Call at login/orchestrator startup to store each tenant's Instagram credentials.
    The access_token should be a long-lived user access token obtained via OAuth.
    """
    with _TENANT_LOCK:
        # For simplicity, we're just storing the access token.
        session = requests.Session()
        session.headers.update({"Authorization": f"Bearer {access_token}"})
        _TENANT_CLIENTS[tenant_id] = session

def get_client_for(tenant_id: str) -> requests.Session:
    """
    Retrieves the requests.Session client configured for the given tenant.
    """
    client = _TENANT_CLIENTS.get(tenant_id)
    if client is None:
        raise RuntimeError(f"No Instagram client registered for tenant '{tenant_id}'")
    return client