# src/prodigal_automation/tools/linkedin.py

import os
from linkedin_v2 import linkedin
from prodigal_automation.auth import check_token, TokenData
from prodigal_automation.tools.manager import register_tool

# your app credentials—usually per‐tenant too
_LINKEDIN_KEY    = os.getenv("LINKEDIN_CLIENT_ID")
_LINKEDIN_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
_LINKEDIN_REDIRECT = os.getenv("LINKEDIN_REDIRECT_URI")

def linkedin_get_profile(
    tenant_id: str,
    member_urn: str,
    token: str = None,
) -> dict:
    # enforce RBAC
    claims: TokenData = check_token(token)
    if "linkedin.read" not in claims.capabilities:
        raise PermissionError("Missing 'linkedin.read' capability")

    # here you’d look up per-tenant OAuth2 tokens from your orchestrator DB
    # for simplicity, we assume a global user‐context token in an env var:
    user_token = os.getenv(f"{tenant_id}_LINKEDIN_TOKEN")
    if not user_token:
        raise RuntimeError(f"No LinkedIn token for tenant {tenant_id}")

    app = linkedin.LinkedInApplication(token=user_token)
    profile = app.get_profile(member_urn)
    return profile

def linkedin_share_post(
    tenant_id: str,
    author_urn: str,
    text: str,
    token: str = None,
) -> dict:
    claims: TokenData = check_token(token)
    if "linkedin.write" not in claims.capabilities:
        raise PermissionError("Missing 'linkedin.write' capability")

    user_token = os.getenv(f"{tenant_id}_LINKEDIN_TOKEN")
    app = linkedin.LinkedInApplication(token=user_token)
    share = app.submit_share(author=author_urn, comment=text)
    return share

register_tool("linkedin.get_profile",    linkedin_get_profile)
register_tool("linkedin.share_post",     linkedin_share_post)
