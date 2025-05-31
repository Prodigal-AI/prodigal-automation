class SocialMediaError(Exception):
    """Base exception for social media automation."""
    pass

class AuthError(SocialMediaError):
    """Raised when authentication fails."""
    pass

class APIError(SocialMediaError):
    """Raised when there's an issue with the social media API."""
    pass

class ValidationError(SocialMediaError):
    """Raised when data validation fails."""
    pass