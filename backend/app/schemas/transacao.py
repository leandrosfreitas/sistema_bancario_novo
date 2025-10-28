from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, Literal

class TransacaoCreate(BaseModel):
    conta_id: UUID
    valor: float
    tipo: Literal["deposito", "saque"]  # "deposito" ou "saque"
    descricao: Optional[str] = None

class TransacaoOut(BaseModel):
    id: UUID
    conta_id: UUID
    valor: float
    tipo: str
    descricao: Optional[str]
    status: str
    data: datetime

    class Config:
        from_attributes = True
