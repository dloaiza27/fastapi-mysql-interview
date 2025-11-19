from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.core.database import SessionLocal

def giant_function(action, user_id=None, user_create: UserCreate = None, user_update: UserUpdate = None):
    """
    Reto: refactoriza esta función aplicando principios SOLID.
    """
    db = SessionLocal()
    result = None

    if action == "create":
        if not user_create:
            return {"error": "Datos de usuario requeridos"}
        new_user = User(email=user_create.email, name=user_create.name)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        result = UserOut.from_orm(new_user)

    elif action == "get":
        if not user_id:
            return {"error": "ID de usuario requerido"}
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        result = UserOut.from_orm(user)

    elif action == "update":
        if not user_id or not user_update:
            return {"error": "ID y datos de usuario requeridos para actualizar"}
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return {"error": "Usuario no encontrado"}
        if user_update.email:
            user.email = user_update.email
        if user_update.name:
            user.name = user_update.name
        db.commit()
        result = UserOut.from_orm(user)

    elif action == "delete":
        if not user_id:
            return {"error": "ID de usuario requerido para eliminar"}
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return {"error": "Usuario no encontrado"}
        db.delete(user)
        db.commit()
        result = {"message": "Usuario eliminado", "user_id": user.id}

    else:
        result = {"error": "Acción inválida"}

    db.close()
    return result
