from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import uuid4

from app.schemas.conta import ContaCreate, ContaOut
from app.models.conta import Conta
from app.db.session import get_db
from app.core.jwt import get_current_user
from app.models.usuario import Usuario

router = APIRouter(prefix="/contas", tags=["Contas"])

@router.post("/", response_model=ContaOut)
def criar_conta(
    conta: ContaCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):
    nova_conta = Conta(
        numero_conta=str(uuid4())[:8],  # Gera número de conta simples
        tipo=conta.tipo,
        saldo=conta.saldo_inical,
        usuario_id=usuario.id
    )
    db.add(nova_conta)
    db.commit()
    db.refresh(nova_conta)
    return nova_conta
