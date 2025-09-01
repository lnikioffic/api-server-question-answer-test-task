from src.database import DbSession
from src.services.question_service import get_question_by_id
from fastapi import HTTPException, Path, status
from typing import Annotated

error_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Question not found',
)


async def get_question(session: DbSession, question_id: Annotated[int, Path]):
    question = await get_question_by_id(session, question_id)
    if not question:
        raise error_found
    return question
