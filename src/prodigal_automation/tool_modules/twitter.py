# src/prodigal_automation/tools/twitter.py

from prodigal_automation.auth import TokenData, check_token
from prodigal_automation.tools.manager import register_tool
from prodigal_automation.twitter_manager import get_client_for


def twitter_get_user_timeline(
    tenant_id: str,
    username: str,
    max_results: int = 5,
    token: str = None,
) -> list:
    # 1) Enforce RBAC
    claims: TokenData = check_token(token)
    if "twitter.read" not in claims.capabilities:
        raise PermissionError("Missing 'twitter.read' capability")

    # 2) Fetch per-tenant client
    client = get_client_for(tenant_id)

    # 3) Lookup user
    user = client.get_user(username=username)
    if not user.data:
        raise RuntimeError(f"@{username} not found")
    user_id = user.data.id

    # 4) Fetch tweets
    resp = client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=["created_at", "text"],
    )
    return resp.data or []


def twitter_get_tweet(
    tenant_id: str,
    tweet_id: str,
    token: str = None,
) -> dict:
    claims: TokenData = check_token(token)
    if "twitter.read" not in claims.capabilities:
        raise PermissionError("Missing 'twitter.read' capability")
    client = get_client_for(tenant_id)
    resp = client.get_tweet(
        id=tweet_id,
        tweet_fields=["created_at", "text"],
    )
    if not resp.data:
        raise RuntimeError(f"Tweet {tweet_id} not found")
    return resp.data


# register both under unique names
register_tool("twitter.get_timeline", twitter_get_user_timeline)
register_tool("twitter.get_tweet", twitter_get_tweet)
