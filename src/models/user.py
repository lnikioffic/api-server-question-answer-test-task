from src.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.answer import Answer


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    answers_user: Mapped[list['Answer']] = relationship(back_populates='user')
