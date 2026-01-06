from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.repositories.user_repository import UserRepository

from app.core.security import gerar_hash_senha

class UserService:

    @staticmethod
    def register(db: Session, data: UsuarioCreate):
        if UserRepository.get_by_email(db, data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="E-mail já cadastrado"
            )

        user = Usuario(
            nome=data.nome,
            cpf=data.cpf,
            data_nascimento=data.data_nascimento,
            email=data.email,
            telefone=data.telefone,
            senha=gerar_hash_senha(data.senha)  # 🔐 AQUI
        )
        return UserRepository.create(db, user)
