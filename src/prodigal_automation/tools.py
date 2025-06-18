# src/prodigal_automation/tools.py

from typing import Optional

import google.generativeai as genai
from pydantic import BaseModel, Field, field_validator


class ContentRequest(BaseModel):
    """Pydantic model for content generation request"""

    topic: str = Field(
        ..., min_length=2, max_length=200, description="Topic of the content" # Increased max_length
    )
    # Changed default length and upper bound for more general use
    length: int = Field(500, ge=50, le=5000, description="Maximum content length in characters")
    style: Optional[str] = Field(
        "professional", description="Writing style (casual/professional/funny)"
    )

    @field_validator("topic")
    @classmethod
    def validate_topic(cls, v):
        if len(v.strip().split()) < 2:
            raise ValueError("Topic should be at least 2 words")
        return v


class ContentGenerator:
    """Generates content using Gemini AI with Pydantic validation"""

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_content(self, request: ContentRequest) -> str:
        """
        Generate content with validation
        Args:
            request: ContentRequest object with validated parameters
        Returns:
            Generated content
        """
        prompt = (
            f"Write a {request.style} post about {request.topic} "
            f"with max {request.length} characters. "
            "Include relevant hashtags if appropriate. "
            "Make it sound natural for social media."
        )

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise ValueError(f"Content generation failed: {str(e)}")

    def generate_tweet(self, request: ContentRequest) -> str:
        """
        Generate tweet content with validation
        Args:
            request: ContentRequest object with validated parameters
        Returns:
            Generated tweet content
        """
        # Ensure length is within Twitter limits
        request.length = max(50, min(request.length, 280))
        prompt = (
            f"Write a {request.style} tweet about {request.topic} "
            f"with max {request.length} characters. "
            "Include relevant hashtags if appropriate. "
            "Make it sound natural for Twitter."
        )

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise ValueError(f"Tweet content generation failed: {str(e)}")

    def generate_post(self, request: ContentRequest) -> str:
        """
        Generate social media post content with validation
        Args:
            request: ContentRequest object with validated parameters
        Returns:
            Generated post content
        """
        # For Facebook, a higher character limit is acceptable
        request.length = min(request.length, 5000) # Facebook posts can be much longer
        prompt = (
            f"Write a {request.style} social media post about {request.topic} "
            f"with max {request.length} characters. "
            "Include relevant hashtags if appropriate. "
            "Make it sound natural for Facebook/general social media."
        )

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise ValueError(f"Social media post content generation failed: {str(e)}")


    # Alternative simple interface
    def simple_generate(self, topic: str, length: int = 500) -> str:
        """
        Simplified interface without style option
        Args:
            topic: Content topic (min 2 words)
            length: Content length in characters (default 500)
        Returns:
            Generated content
        """
        request = ContentRequest(topic=topic, length=length)
        return self.generate_content(request)

    # Add the method that tests expect for general content generation
    def generate_simple_content(self, topic: str) -> str:
        """
        Method name that matches what tests expect
        Args:
            topic: Topic (min 2 words)
        Returns:
            Generated content
        """
        return self.simple_generate(topic)