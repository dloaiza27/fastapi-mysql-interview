from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.services.user_service import giant_function
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.core.auth import verify_basic_auth

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def list_users(auth=Depends(verify_basic_auth)):
    """
    Listar todos los usuarios
    """
    result = giant_function(action="list")
    return result

@router.post("/", response_model=UserOut)
def create_user(user_create: UserCreate, auth=Depends(verify_basic_auth)):
    """
    Crear un usuario
    """
    result = giant_function(action="create", user_create=user_create)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_update: UserUpdate, auth=Depends(verify_basic_auth)):
    """
    Actualizar un usuario
    """
    result = giant_function(action="update", user_id=user_id, user_update=user_update)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.delete("/{user_id}")
def delete_user(user_id: int, auth=Depends(verify_basic_auth)):
    """
    Eliminar un usuario
    """
    result = giant_function(action="delete", user_id=user_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
