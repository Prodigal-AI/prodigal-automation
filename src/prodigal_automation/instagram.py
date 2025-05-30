import os
import requests
from prodigal_automation.tools import register_tool
from prodigal_automation.auth import check_token, TokenData
from prodigal_automation.instagram_manager import get_client_for

# Base URL for the Meta Graph API (Instagram is part of it)
INSTAGRAM_GRAPH_API_BASE_URL = "https://graph.facebook.com/v22.0/" # Use the latest API version

def _instagram_api_call(
    tenant_id: str,
    endpoint: str,
    method: str = "GET",
    params: dict = None,
    json_data: dict = None,
) -> dict:
    """Helper to make authenticated Instagram API calls."""
    session = get_client_for(tenant_id)
    url = f"{INSTAGRAM_GRAPH_API_BASE_URL}{endpoint}"
    
    response = session.request(method, url, params=params, json=json_data)
    response.raise_for_status() # Raise an exception for HTTP errors
    return response.json()

def instagram_get_user_media(
    tenant_id: str,
    instagram_business_account_id: str,
    token: str = None,
    limit: int = 5,
) -> dict:
    """
    Fetches media (photos, videos) from an Instagram Business Account.
    The access token must have 'instagram_basic' and 'pages_read_engagement' permissions.
    """
    claims: TokenData = check_token(token)
    if "instagram.read" not in claims.capabilities:
        raise PermissionError("Missing 'instagram.read' capability")

    endpoint = f"{instagram_business_account_id}/media"
    params = {
        "fields": "id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username",
        "limit": limit,
    }
    return _instagram_api_call(tenant_id, endpoint, params=params)

def instagram_post_image(
    tenant_id: str,
    instagram_business_account_id: str,
    image_url: str,
    caption: str = "",
    token: str = None,
) -> dict:
    """
    Publishes an image to an Instagram Business Account.
    Requires 'instagram_content_publish' permission and a long-lived user access token.
    The image_url must be a publicly accessible URL.
    """
    claims: TokenData = check_token(token)
    if "instagram.write" not in claims.capabilities:
        raise PermissionError("Missing 'instagram.write' capability")

    # Step 1: Create a media container
    creation_id_response = _instagram_api_call(
        tenant_id,
        f"{instagram_business_account_id}/media",
        method="POST",
        json_data={
            "image_url": image_url,
            "caption": caption,
        },
    )
    creation_id = creation_id_response.get("id")
    if not creation_id:
        raise RuntimeError("Failed to create Instagram media container.")

    # Step 2: Publish the media container
    publish_response = _instagram_api_call(
        tenant_id,
        f"{instagram_business_account_id}/media_publish",
        method="POST",
        json_data={
            "creation_id": creation_id,
        },
    )
    return publish_response

# Register Instagram tools
register_tool("instagram.get_user_media", instagram_get_user_media)
register_tool("instagram.post_image", instagram_post_image)