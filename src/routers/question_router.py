from fastapi import APIRouter, Depends, status
from typing import Annotated
from src.database import DbSession
from src.services.question_service import (
    get_questions,
    create_question,
    delete_question,
)
from src.dependencies.question_dep import get_question
from src.schemas.question_schemas import QuestionCreate, QuestionRead
from src.schemas.answer_schemas import AnswerCreate, AnswerRead
from src.services.answer_service import create_answer_by_id_q

router = APIRouter(
    prefix='/questions',
    tags=['questions'],
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[QuestionRead])
async def questions(session: DbSession):
    return await get_questions(session)


@router.get(
    '/{question_id}', status_code=status.HTTP_200_OK, response_model=QuestionRead
)
async def question(
    question: Annotated[QuestionRead, Depends(get_question)],
):
    return question


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(session: DbSession, question: QuestionCreate):
    return await create_question(session, question)


@router.post(
    '/{question_id}/answers',
    status_code=status.HTTP_201_CREATED,
    response_model=AnswerRead,
)
async def create_answer(
    session: DbSession,
    question: Annotated[QuestionRead, Depends(get_question)],
    answer: AnswerCreate,
):
    answer.question_id = question.id
    answer = await create_answer_by_id_q(session, answer)
    return answer


@router.delete('/{question_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    session: DbSession,
    question: Annotated[QuestionRead, Depends(get_question)],
):
    await delete_question(session, question.id)
