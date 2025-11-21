from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from core.auth import verify_basic_auth, BEARER_TOKEN

router = APIRouter()

@router.post("/login")
def login(request: Request):
    verify_basic_auth(request)
    return JSONResponse(
        content={"access_token": BEARER_TOKEN, "token_type": "bearer"}
    )
