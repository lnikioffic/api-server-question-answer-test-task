from src.database import DbSession
from src.services.answer_service import get_answer_by_id
from fastapi import HTTPException, Path, status
from typing import Annotated

error_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Answer not found',
)


async def get_answer(session: DbSession, answer_id: Annotated[int, Path]):
    answer = await get_answer_by_id(session, answer_id)
    if not answer:
        raise error_found
    return answer
