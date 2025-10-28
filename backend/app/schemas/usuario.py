from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None
    documento: str

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None

class UsuarioOut(BaseModel):
    id: UUID
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    documento: str
    is_ativo: bool

    class Config:
        from_attributes = True
