from pydantic import BaseModel
from datetime import datetime

class ContaCreate(BaseModel):
    tipo: str
    saldo_inical: float

class ContaOut(BaseModel):
    id: int
    tipo: str
    saldo: float
    data_criacao: datetime
    usuario_id: int

    class Config:
        from_attributes = True
