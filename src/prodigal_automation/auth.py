# src/prodigal_automation/auth.py

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TwitterAuth(BaseModel):
    """Twitter authentication credentials model"""

    bearer_token: Optional[str] = Field(
        None,
        description="Twitter API Bearer Token"
        )

    api_key: Optional[str] = Field(
        None,
        description="Twitter API Key"
        )

    api_key_secret: Optional[str] = Field(
        None,
        description="Twitter API Secret"
        )

    access_token: Optional[str] = Field(
        None,
        description="Twitter Access Token"
        )

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
