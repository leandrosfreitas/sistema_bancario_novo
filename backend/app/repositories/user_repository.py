from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.usuario import Usuario

class UserRepository:

    @staticmethod
    def get_by_email(db: Session, email: str):
        stmt = select(Usuario).where(Usuario.email == email)
        return db.scalar(stmt)

    @staticmethod
    def create(db: Session, user: Usuario):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
