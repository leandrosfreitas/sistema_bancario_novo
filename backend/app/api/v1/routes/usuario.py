from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post(
    "/register",
    response_model=UsuarioOut,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    data: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return UserService.register(db, data)
