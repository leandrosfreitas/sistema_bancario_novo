import uuid
from sqlalchemy import String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base

class Investimento(Base):
    __tablename__ = "investimentos"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    tipo: Mapped[str] = mapped_column(String, nullable=False)
    valor_aplicado: Mapped[float] = mapped_column(Float, nullable=False)
    data_aplicacao: Mapped[str] = mapped_column(Date, nullable=False)
    rentabilidade: Mapped[float] = mapped_column(Float, default=0.0)

    conta_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("contas.id"),
        nullable=False
    )
