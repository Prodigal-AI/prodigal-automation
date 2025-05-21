# src/prodigal_automation/oauth.py

from requests_oauthlib import OAuth2Session

class OAuthClient:
    """
    A simple OAuth2 “out-of-band” helper.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        authorize_url: str,
        token_url: str,
        scope: list[str],
    ):
        self._oauth = OAuth2Session(
            client_id,
            scope=scope,
            redirect_uri="urn:ietf:wg:oauth:2.0:oob",
        )
        self.client_secret = client_secret
        self.token_url = token_url

    def get_authorization_url(self) -> tuple[str,str]:
        """
        Step 1: redirect user to this URL, have them paste back the code.
        """
        url, state = self._oauth.authorization_url(authorize_url)
        return url, state

    def fetch_token(self, authorization_response: str) -> dict:
        """
        Step 2: call this with the URL the user was redirected back to.
        """
        return self._oauth.fetch_token(
            token_url=self.token_url,
            authorization_response=authorization_response,
            client_secret=self.client_secret,
        )
