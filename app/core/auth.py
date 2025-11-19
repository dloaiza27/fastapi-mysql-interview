from fastapi import Request, HTTPException, status
import os

BASIC_USER = "admin"
BASIC_PASS = "1234"
BEARER_TOKEN = "supersecret"


def verify_basic_auth(request: Request):
    """
    Reto: Elimina la vulnerabilidad de seguridad.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Basic "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Basic Auth")
    return True

def verify_bearer_token(request: Request):

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Bearer Token")
    token = auth_header.split(" ")[1]
    if token != BEARER_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return True
