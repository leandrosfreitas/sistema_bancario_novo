from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class TransacaoCreate(BaseModel):
    valor: float
    tipo: Literal["deposito", "saque"]
    descricao: str
    conta_id: int

class TransacaoOut(BaseModel):
    id: int
    valor: float
    tipo: str
    descricao: str
    data: datetime
    conta_id: int

    class Config:
        from_attributes = True
