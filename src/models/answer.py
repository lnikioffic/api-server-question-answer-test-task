from src.models.base import Base
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.question import Question
    from src.models.user import User


class Answer(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', onupdate='CASCADE', ondelete='RESTRICT'), nullable=False
    )
    question_id: Mapped[int] = mapped_column(
        ForeignKey(
            'questions.id',
            onupdate='CASCADE',
            ondelete='CASCADE',
        ),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user: Mapped['User'] = relationship(back_populates='answers_user')
    question: Mapped['Question'] = relationship(back_populates='answers_question')
