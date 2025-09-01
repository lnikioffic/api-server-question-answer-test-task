from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.models.question import Question
from sqlalchemy.engine import Result
from sqlalchemy.orm import selectinload
from src.models.answer import Answer
from src.schemas.answer_schemas import AnswerCreate


async def get_answer_by_id(session: AsyncSession, answer_id: int) -> Answer | None:
    query = (
        select(Answer)
        .where(Answer.id == answer_id)
        .options(selectinload(Answer.user))
        .options(selectinload(Answer.question))
    )
    result: Result = await session.execute(query)
    result = result.scalar_one_or_none()
    return result


async def create_answer_by_id_q(session: AsyncSession, answer: AnswerCreate) -> Answer:
    new_answer = Answer(**answer.model_dump())
    session.add(new_answer)
    await session.commit()
    await session.refresh(new_answer)
    result = await get_answer_by_id(session, new_answer.id)
    if result is None:
        raise ValueError("Answer not found after creation")
    return result


async def delete_answer(session: AsyncSession, answer_id: int):
    query = delete(Answer).filter(Answer.id == answer_id)
    await session.execute(query)
