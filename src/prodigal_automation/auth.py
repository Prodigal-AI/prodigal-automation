# src/prodigal_automation/auth.py

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TwitterAuth(BaseModel):
    """Twitter authentication credentials model"""

    bearer_token: Optional[str] = Field(None, description="Twitter API Bearer Token")

    api_key: Optional[str] = Field(None, description="Twitter API Key")

    api_key_secret: Optional[str] = Field(None, description="Twitter API Secret")

    access_token: Optional[str] = Field(None, description="Twitter Access Token")

    access_token_secret: Optional[str] = Field(
        None, description="Twitter Access Token Secret"
    )

    # Updated to Pydantic V2 syntax
    @field_validator("bearer_token", mode="before")
    @classmethod
    def validate_bearer_token(cls, v):
        if v and len(v) < 10:
            raise ValueError("Bearer token seems too short")
        return v

    def has_oauth_credentials(self):
        """Check if OAuth 1.0a credentials are present"""
        return all(
            [
                self.api_key,
                self.api_key_secret,
                self.access_token,
                self.access_token_secret,
            ]
        )

    def has_bearer_token(self):
        """Check if Bearer token is present"""
        return bool(self.bearer_token)


# New: Facebook authentication credentials model
class FacebookAuth(BaseModel):
    """Facebook authentication credentials model"""

    access_token: str = Field(..., description="Facebook Page Access Token")
    page_id: Optional[str] = Field(None, description="Facebook Page ID")
    # You might also need app_id and app_secret for certain flows,
    # but for page posting, page access token is usually sufficient.
    # Consider adding them if your integration requires user authentication
    # or other advanced features.
    app_id: Optional[str] = Field(None, description="Facebook App ID")
    app_secret: Optional[str] = Field(None, description="Facebook App Secret")


class TokenData(BaseModel):
    """
    User token claims (example - for demonstration,
    integrate with actual identity system)
    """

    user_id: str = Field(..., description="User ID")
    capabilities: list[str] = Field(..., description="List of capabilities/permissions")


def check_token(token: Optional[str]) -> TokenData:
    """
    Dummy function for token validation. Replace with actual JWT/auth validation.
    For this example, we'll assume a valid token grants all capabilities if present,
    otherwise, it's anonymous.
    """
    if token:
        # In a real application, you'd decode and validate the JWT here
        # For simplicity, we grant all permissions if a token is provided.
        return TokenData(
            user_id="test_user", capabilities=["twitter.read", "facebook.post"]
        )
    raise PermissionError("Authentication token is missing or invalid")
