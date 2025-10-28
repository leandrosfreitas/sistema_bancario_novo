from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.emprestimo import EmprestimoCreate, EmprestimoOut
from app.models.emprestimo import Emprestimo
from app.models.conta import Conta
from app.db.session import get_db

router = APIRouter(prefix="/emprestimos", tags=["Empréstimos"])

@router.post("/", response_model=EmprestimoOut)
def simular_emprestimo(emprestimo: EmprestimoCreate, db: Session = Depends(get_db)):
    conta = db.query(Conta).get(emprestimo.conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    novo_emprestimo = Emprestimo(
        valor=emprestimo.valor,
        taxa_juros=emprestimo.taxa_juros,
        parcelas=emprestimo.parcelas,
        data_inicio=emprestimo.data_inicio,
        conta_id=emprestimo.conta_id,
        status="simulado"
    )

    db.add(novo_emprestimo)
    db.commit()
    db.refresh(novo_emprestimo)
    return novo_emprestimo
