from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.services.user_service import giant_function
from app.schemas.user import UserOut, UserCreate, UserUpdate
from app.core.auth import verify_basic_auth

router = APIRouter()

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, auth=Depends(verify_basic_auth)):
    """
    Reto: adapta este endpoint considerando buenas prácticas de trazabilidad
    """
    result = giant_function(action="get", user_id=user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return result

@router.post("/", response_model=UserOut)
def create_user(user_create: UserCreate, auth=Depends(verify_basic_auth)):
    result = giant_function(action="create", user_create=user_create)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.put("/", response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate, auth=Depends(verify_basic_auth)):
    result = giant_function(action="update", user_id=user_id, user_update=user_update)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.delete("/")
def delete_user(user_id: int, auth=Depends(verify_basic_auth)):
    result = giant_function(action="delete", user_id=user_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
