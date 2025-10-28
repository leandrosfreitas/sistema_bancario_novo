from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from app.db.base_class import Base

class Conta(Base):
    __tablename__ = "contas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    numero_conta = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)
    saldo = Column(Float, default=0.0)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False)
