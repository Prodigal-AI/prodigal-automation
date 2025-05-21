from requests_oauthlib import OAuth2Session

class OAuthClient:
    def __init__(self, client_id: str, client_secret: str, authorize_url: str, token_url: str, scope: list[str]):
        self._oauth = OAuth2Session(client_id, scope=scope, redirect_uri="urn:ietf:wg:oauth:2.0:oob")
        self.client_secret = client_secret
        self.token_url = token_url

    def get_authorization_url(self):
        url, state = self._oauth.authorization_url(self._oauth.authorization_url)
        return url, state

    def fetch_token(self, authorization_response: str):
        return self._oauth.fetch_token(
            token_url=self.token_url,
            authorization_response=authorization_response,
            client_secret=self.client_secret,
        )
