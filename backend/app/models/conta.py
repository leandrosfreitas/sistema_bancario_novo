import uuid
from datetime import datetime
from sqlalchemy import String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

class Conta(Base):
    __tablename__ = "contas"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    numero_conta: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    tipo: Mapped[str] = mapped_column(String, nullable=False)
    saldo: Mapped[float] = mapped_column(Float, default=0.0)
    data_criacao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    usuario_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("usuarios.id"),
        nullable=False
    )
