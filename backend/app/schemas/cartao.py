from pydantic import BaseModel
from typing import Literal
from datetime import date

class CartaoCreate(BaseModel):
    numero: str
    validade: date
    cvv: str
    tipo: Literal["credito", "debito"]
    limite: float
    conta_id: int

class CartaoOut(BaseModel):
    id: int
    numero: str
    validade: date
    tipo: str
    limite: float
    conta_id: int

    class Config:
        from_attributes = True
