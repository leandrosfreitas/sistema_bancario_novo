from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base_class import Base

class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    valor = Column(Float, nullable=False)
    parcelas = Column(Integer, nullable=False)
    taxa_juros = Column(Float, nullable=False)
    status = Column(String, default="simulado")
    conta_id = Column(UUID(as_uuid=True), ForeignKey("contas.id"), nullable=False)
