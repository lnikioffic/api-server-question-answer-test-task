from src.models.base import Base
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from src.models.answer import Answer


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    answers_question: Mapped[list['Answer']] = relationship(back_populates='question')
