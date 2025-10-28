from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.cartao import CartaoCreate, CartaoOut
from app.models.cartao import Cartao
from app.models.conta import Conta
from app.db.session import get_db

router = APIRouter(prefix="/cartoes", tags=["Cartões"])

@router.post("/", response_model=CartaoOut)
def criar_cartao(cartao: CartaoCreate, db: Session = Depends(get_db)):
    conta = db.query(Conta).get(cartao.conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if db.query(Cartao).filter(Cartao.numero == cartao.numero).first():
        raise HTTPException(status_code=400, detail="Número de cartão já cadastrado")

    novo_cartao = Cartao(
        numero=cartao.numero,
        validade=cartao.validade,
        cvv=cartao.cvv,
        tipo=cartao.tipo,
        limite=cartao.limite,
        conta_id=cartao.conta_id
    )

    db.add(novo_cartao)
    db.commit()
    db.refresh(novo_cartao)
    return novo_cartao
