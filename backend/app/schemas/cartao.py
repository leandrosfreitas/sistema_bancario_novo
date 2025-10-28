from pydantic import BaseModel
from typing import Literal
from datetime import date
from uuid import UUID

class CartaoCreate(BaseModel):
    numero: str
    validade: date
    cvv: str
    tipo: Literal["credito", "debito"]
    limite: float
    conta_id: UUID

class CartaoOut(BaseModel):
    id: UUID
    numero: str
    validade: date
    tipo: str
    limite: float
    conta_id: UUID

    class Config:
        from_attributes = True
