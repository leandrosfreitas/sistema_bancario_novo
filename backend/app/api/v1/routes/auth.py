from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, TokenResponse
from app.models.usuario import Usuario
from app.core.security import verificar_senha
from app.core.jwt import create_access_token
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == request.email).first()
    if not usuario or not verificar_senha(request.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token(data={"sub": str(usuario.id)})
    return TokenResponse(access_token=token)
