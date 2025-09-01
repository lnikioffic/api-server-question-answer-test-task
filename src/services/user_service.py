from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from src.schemas.user_schemas import UserCreate


async def create_user(session: AsyncSession, user: UserCreate) -> UserCreate:
    new_user = User(**user.model_dump())
    session.add(new_user)
    await session.commit()
    return new_user
