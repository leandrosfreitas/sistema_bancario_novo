import uuid
from sqlalchemy import String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

class Cartao(Base):
    __tablename__ = "cartoes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    numero: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    tipo: Mapped[str] = mapped_column(String, nullable=False)
    validade: Mapped[str] = mapped_column(Date, nullable=False)
    cvv: Mapped[str] = mapped_column(String, nullable=False)
    limite: Mapped[float] = mapped_column(Float, default=0.0)
    fatura_atual: Mapped[float] = mapped_column(Float, default=0.0)

    conta_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("contas.id"),
        nullable=False
    )
