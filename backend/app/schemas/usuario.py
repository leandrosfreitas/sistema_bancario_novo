from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UsuarioCreate(BaseModel):
    nome: str
    cpf: str
    data_nascimento: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None

class UsuarioOut(BaseModel):
    id: UUID
    nome: str
    cpf: str
    email: EmailStr
    telefone: Optional[str]

    class Config:
        from_attributes = True
