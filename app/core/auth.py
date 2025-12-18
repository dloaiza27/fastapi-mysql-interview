from fastapi import Request, HTTPException, status
import os
import base64


BASIC_USER = "admin"
BASIC_PASS = "1234"
BEARER_TOKEN = "supersecret"


def verify_basic_auth(request: Request):
    """
    Reto: Elimina la vulnerabilidad de seguridad.
    """    
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Basic "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Se requiere Basic Auth"
        )
    
    try:
        encoded_credentials = auth_header.split(" ")[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        if ":" not in decoded_credentials:
            raise ValueError("Invalid format")
            
        username, password = decoded_credentials.split(":", 1)
        
        if username == BASIC_USER and password == BASIC_PASS:
            return True
    except Exception as e:
        pass

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail=f"Invalid Credentials"
    )


def verify_bearer_token(request: Request):

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Bearer Token")
    token = auth_header.split(" ")[1]
    if token != BEARER_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return True
