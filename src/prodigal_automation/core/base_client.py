from prodigal_automation.core.errors import APIError

class BaseSocialMediaClient:
    """
    Abstract base class for all social media clients.
    Defines common methods for connecting and posting.
    Specific platforms will implement their own versions.
    """
    def __init__(self, credentials):
        self.credentials = credentials
        self._api_client = None # The actual SDK client instance

    def connect(self):
        """Establishes connection to the social media API."""
        raise NotImplementedError

    def post(self, content: str, **kwargs):
        """Posts content to the social media platform."""
        raise NotImplementedError
