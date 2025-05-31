from pydantic import BaseModel, Field, SecretStr, validator, model_validator
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

# --- NEW: Facebook Credentials ---
class FacebookAuthCredentials(BaseModel):
    access_token: SecretStr
    page_id: Optional[str] = None # For posting to a specific page

# --- Updated SocialMediaPost for more general use ---
class SocialMediaPost(BaseModel):
    content: str = Field(..., min_length=1) # Removed max_length for general purpose
    media_urls: Optional[List[str]] = None
    platform: str = Field(..., description="Target platform (e.g., 'twitter', 'facebook')")
    # Add platform-specific fields later if needed, e.g., twitter_hashtags, facebook_link

    @validator('content')
    def content_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Content cannot be empty or just whitespace.")
        return v

# --- Twitter Models (No Change from previous update) ---
class TwitterPostResponse(BaseModel):
    id: str
    text: str

class Tweet(BaseModel):
    id: str
    text: str
    created_at: datetime
    author_id: str

class Timeline(BaseModel):
    user_id: Optional[str] = None
    username: Optional[str] = None
    tweets: List[Tweet]
    count: int

    @model_validator(mode='after')
    def count_matches_tweets(self) -> 'Timeline':
        if self.count != len(self.tweets):
            raise ValueError("Count must match the number of tweets.")
        return self

# --- NEW: Facebook Models ---
class FacebookPostResponse(BaseModel):
    id: str # typically in format <page_id>_<post_id>
    post_id: str # The actual post ID
    message: Optional[str] = None # The message that was posted

    @model_validator(mode='after')
    def parse_facebook_id(self) -> 'FacebookPostResponse':
        if '_' in self.id:
            self.post_id = self.id.split('_')[1]
        else:
            self.post_id = self.id # In case it's just post_id
        return self

# You can add Facebook specific timeline/feed models later if needed
# class FacebookFeedItem(BaseModel):
#     id: str
#     message: str
#     created_time: datetime
#     from_user: Optional[FacebookUserData] = None

# class FacebookUserData(BaseModel):
#     id: str
#     name: str