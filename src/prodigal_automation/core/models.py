from pydantic import BaseModel, Field, SecretStr, field_validator, model_validator # <-- Changed from root_validator
from typing import Optional, List, Dict, Any
from datetime import datetime

class Credential(BaseModel):
    key: SecretStr
    secret: SecretStr

class TwitterAuthCredentials(BaseModel):
    consumer_key: SecretStr
    consumer_secret: SecretStr
    access_token: SecretStr
    access_token_secret: SecretStr

class SocialMediaPost(BaseModel):
    content: str = Field(..., min_length=1, max_length=280)
    media_urls: Optional[List[str]] = None

    @field_validator('content')
    def content_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Content cannot be empty or just whitespace.")
        return v

class TwitterPostResponse(BaseModel):
    id: str
    text: str
    # v2 API response for created tweets is simpler initially
    # If you need more fields here, you'd perform a lookup after creation.

class Tweet(BaseModel):
    id: str
    text: str
    created_at: datetime
    author_id: str
    # Add more fields from Twitter API v2 Tweet object as needed

class Timeline(BaseModel):
    user_id: Optional[str] = None
    username: Optional[str] = None
    tweets: List[Tweet]
    count: int

    # Corrected for Pydantic v2
    @model_validator(mode='after') # 'after' mode runs after validation of all fields
    def count_matches_tweets(self) -> 'Timeline': # The self argument refers to the model instance
        if self.count != len(self.tweets):
            raise ValueError("Count must match the number of tweets.")
        return self # Return the validated instance