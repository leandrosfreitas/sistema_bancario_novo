from pydantic import BaseModel
from datetime import datetime
from typing import Literal
from uuid import UUID

class ContaCreate(BaseModel):
    tipo: Literal["corrente", "poupanca", "salario"]
    saldo_inical: float = 0.0

class ContaOut(BaseModel):
    id: UUID
    numero_conta: str
    tipo: str
    saldo: float
    data_criacao: datetime
    usuario_id: UUID

    class Config:
        from_attributes = True
