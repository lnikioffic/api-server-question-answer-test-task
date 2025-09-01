import contextlib
from collections.abc import AsyncGenerator, AsyncIterator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from src.config import config_db


class DataBase:
    def __init__(self, db_url: str, echo: bool = False):
        self._engine: AsyncEngine = create_async_engine(url=db_url, echo=echo)
        self._sessionmaker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self._engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise OSError("Session if not initialized")
        async with self._sessionmaker() as session:
            try:
                yield session

            except Exception:
                await session.rollback()
                raise


db = DataBase(db_url=config_db.get_db_url())


async def get_session() -> AsyncGenerator[AsyncSession]:
    async with db.session() as session:
        yield session


DbSession = Annotated[AsyncSession, Depends(get_session)]
