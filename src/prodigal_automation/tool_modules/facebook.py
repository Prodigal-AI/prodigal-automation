# src/prodigal_automation/tool_modules/facebook.py

from typing import Any, Dict, Optional

from prodigal_automation.auth import (  # Ensure FacebookAuth is imported
    FacebookAuth,
    TokenData,
    check_token,
)
from prodigal_automation.client import FacebookClient  # Imports from client
from prodigal_automation.tool_modules.manager import register_tool

_FACEBOOK_CLIENTS: Dict[str, FacebookClient] = {}


def get_client_for_facebook(tenant_id: str) -> Any:
    """
    Retrieves or initializes a FacebookClient for a given tenant.
    In a real system, tenant-specific FacebookAuth would be loaded from a DB.
    """
    if tenant_id not in _FACEBOOK_CLIENTS:
        # Dummy credentials for demonstration. Replace with actual secure loading.
        # For multi-tenant, you'd fetch the specific tenant's FacebookAuth
        # from a database or configuration.
        # Example: Load from environment variables for simplicity in this dummy setup
        from os import getenv

        access_token = getenv(f"FB_ACCESS_TOKEN_{tenant_id.upper()}")
        page_id = getenv(f"FB_PAGE_ID_{tenant_id.upper()}")

        if not access_token or not page_id:
            raise ValueError(
                f"Facebook credentials for tenant '{tenant_id}' not found."
            )

        auth = FacebookAuth(access_token=access_token, page_id=page_id)
        _FACEBOOK_CLIENTS[tenant_id] = FacebookClient(auth).initialize()
    return _FACEBOOK_CLIENTS[tenant_id]


def facebook_post_message(
    tenant_id: str,
    message: str,
    token: Optional[str] = None,
) -> dict:
    claims: TokenData = check_token(token)
    if "facebook.post" not in claims.capabilities:
        raise PermissionError("Missing 'facebook.post' capability")

    client = get_client_for_facebook(tenant_id)
    # The page ID should ideally be part of the tenant's configuration
    # or passed as an argument if a tenant can manage multiple pages.
    # For now, let's assume get_client_for_facebook provides a client
    # configured with the page ID.
    try:
        # Assuming the client initialized with FacebookAuth has the page_id
        # or we retrieve it from the tenant configuration.
        # If the client initialized the GraphAPI with just the access token,
        # you might need to query for pages the user can manage first,
        # then select the correct page and get its access token.
        # For simplicity, we'll assume the client is ready to post to the page.
        # The FacebookManager already handles the page_id.
        if not hasattr(client, "page_id"):  # Check if the client instance has page_id
            # This is a simplification; in reality, you might fetch it or store it.
            raise ValueError("Facebook page ID not configured for this client.")

        # Post the message to the page feed
        response = client.put_object(
            # Access page_id from the client (assuming it's set)
            parent_object=client.page_id,
            connection_name="feed",
            message=message,
        )
        return {"success": True, "post_id": response["id"]}
    except Exception as e:
        raise RuntimeError(f"Failed to post to Facebook: {e}")


def facebook_get_page_feed(
    tenant_id: str,
    limit: int = 5,
    token: Optional[str] = None,
) -> list:
    claims: TokenData = check_token(token)
    if "facebook.read" not in claims.capabilities:
        raise PermissionError("Missing 'facebook.read' capability")

    client = get_client_for_facebook(tenant_id)
    try:
        # Again, assuming client is set up to interact with a specific page.
        if not hasattr(client, "page_id"):
            raise ValueError("Facebook page ID not configured for this client.")

        feed = client.get_connections(
            id=client.page_id,  # Access page_id from the client
            connection_name="feed",
            limit=limit,
        )
        return feed["data"]
    except Exception as e:
        raise RuntimeError(f"Failed to get Facebook page feed: {e}")


# Register both under unique names
register_tool("facebook.post_message", facebook_post_message)
register_tool("facebook.get_page_feed", facebook_get_page_feed)
