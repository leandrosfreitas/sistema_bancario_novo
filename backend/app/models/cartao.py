from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base_class import Base

class Cartao(Base):
    __tablename__ = "cartoes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    numero = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)
    limite = Column(Float, default=0.0)
    fatura_atual = Column(Float, default=0.0)
    conta_id = Column(UUID(as_uuid=True), ForeignKey("contas.id"), nullable=False)
