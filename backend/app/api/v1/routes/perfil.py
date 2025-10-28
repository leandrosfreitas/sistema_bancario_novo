from fastapi import APIRouter, Depends
from app.core.jwt import get_current_user
from app.models.usuario import Usuario

router = APIRouter()

@router.get("/perfil")
def perfil(usuario: Usuario = Depends(get_current_user)):
    return {"id": usuario.id, "nome": usuario.nome, "email": usuario.email}
