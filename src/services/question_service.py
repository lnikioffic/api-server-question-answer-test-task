from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from src.models.question import Question
from sqlalchemy.engine import Result
from src.schemas.question_schemas import QuestionCreate


async def get_questions(session: AsyncSession) -> list[Question]:
    query = select(Question)
    result: Result = await session.execute(query)
    return result.scalars().all()


async def get_question_by_id(
    session: AsyncSession, question_id: int
) -> Question | None:
    query = await session.get(Question, question_id)
    return query


async def create_question(session: AsyncSession, question: QuestionCreate) -> Question:
    new_question = Question(**question.model_dump())
    session.add(new_question)
    await session.commit()
    return new_question


async def delete_question(session: AsyncSession, question_id: int):
    query = delete(Question).filter(Question.id == question_id)
    result: Result = await session.execute(query)
    try:
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise e
    return result.rowcount
