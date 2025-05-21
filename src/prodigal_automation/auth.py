# src/prodigal_automation/auth.py

from typing import Optional
from fastapi import HTTPException, Request

class AuthError(HTTPException):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(401, detail)

def require_token(request: Request, token: Optional[str] = None) -> str:
    """
    Extract and validate a Bearer token from the header.
    Raises AuthError if missing/invalid.
    """
    token = token or request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise AuthError("Missing Bearer token")
    _, tk = token.split(" ", 1)
    # TODO: verify tk via JWT or DB lookup
    if tk != "expected_token":
        raise AuthError("Invalid token")
    return tk
