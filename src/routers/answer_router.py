from fastapi import APIRouter, Depends, status
from typing import Annotated
from src.schemas.answer_schemas import AnswerRead
from src.database import DbSession
from src.dependencies.answer_dep import get_answer
from src.services.answer_service import delete_answer

router = APIRouter(
    prefix='/answers',
    tags=['answers'],
)


@router.get('/{answer_id}', status_code=status.HTTP_200_OK, response_model=AnswerRead)
async def answer(
    answer: Annotated[AnswerRead, Depends(get_answer)],
):
    return answer


@router.delete('/{answer_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_answer_endpoint(
    session: DbSession,
    answer: Annotated[AnswerRead, Depends(get_answer)],
):
    await delete_answer(session, answer.id)
