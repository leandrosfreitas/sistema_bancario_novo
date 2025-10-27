from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.conta import ContaCreate, ContaOut
from app.models.conta import Conta
from app.db.session import get_db

router = APIRouter(prefix="/contas", tags=["Contas"])

@router.post("/", response_model=ContaOut)
def criar_conta(conta: ContaCreate, db: Session = Depends(get_db)):
    nova_conta = Conta(
        tipo=conta.tipo,
        saldo=conta.saldo_inical,
        usuario_id=1
    )
    db.add(nova_conta)
    db.commit()
    db.refresh(nova_conta)
    return nova_conta
