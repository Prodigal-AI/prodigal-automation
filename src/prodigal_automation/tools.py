# src/prodigal_automation/tools.py

import google.generativeai as genai
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict

class ContentRequest(BaseModel):
    """Pydantic model for tweet generation request"""
    topic: str = Field(..., min_length=2, max_length=100, 
                     description="Topic of the tweet")
    length: int = Field(280, ge=50, le=280,
                      description="Maximum tweet length")
    style: Optional[str] = Field("professional",
                               description="Writing style (casual/professional/funny)")

    @field_validator('topic')  # Updated to Pydantic V2 syntax
    @classmethod
    def validate_topic(cls, v):
        if len(v.strip().split()) < 2:
            raise ValueError("Topic should be at least 2 words")
        return v

class ContentGenerator:
    """Generates content using Gemini AI with Pydantic validation"""
    
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_tweet(self, request: ContentRequest) -> str:
        """
        Generate tweet content with validation
        Args:
            request: ContentRequest object with validated parameters
        Returns:
            Generated tweet content
        """
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
            raise ValueError(f"Content generation failed: {str(e)}")

    # Alternative simple interface
    def simple_generate(self, topic: str, length: int = 500) -> str:
        """
        Simplified interface without style option
        Args:
            topic: Tweet topic (min 2 words)
            length: Tweet length in words (default 200)
        Returns:
            Generated tweet content
        """
        # Estimate character length based on word count (approx 6 chars per word)
        char_length = length * 6
        # Ensure character length is within Twitter limits (50-280)
        char_length = max(50, min(char_length, 280))
        request = ContentRequest(topic=topic, length=char_length)
        return self.generate_tweet(request)

    # Add the method that tests expect
    def generate_simple_content(self, topic: str) -> str:
        """
        Method name that matches what tests expect
        Args:
            topic: Tweet topic (min 2 words)
        Returns:
            Generated tweet content
        """
        return self.simple_generate(topic)