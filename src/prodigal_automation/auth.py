from typing import Optional
from fastapi import HTTPException, Request

# Stub: replace with JWT or your own scheme
class AuthError(HTTPException):
    def __init__(self, detail="Unauthorized"):
        super().__init__(401, detail)

def require_token(request: Request, token: Optional[str] = None):
    token = token or request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise AuthError("Missing Bearer token")
    _, tk = token.split(" ", 1)
    # TODO: verify tk via JWT library or DB lookup
    if tk != "expected_token":
        raise AuthError("Invalid token")
    return tk
