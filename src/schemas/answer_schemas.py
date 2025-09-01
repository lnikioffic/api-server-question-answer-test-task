from pydantic import BaseModel, ConfigDict
from datetime import datetime
from src.schemas.user_schemas import UserRead
from src.schemas.question_schemas import QuestionRead


class AnswerBase(BaseModel):
    text: str
    user_id: int
    question_id: int


class AnswerCreate(AnswerBase):
    question_id: int | None = None


class AnswerRead(AnswerBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

    user: UserRead
    question: QuestionRead
