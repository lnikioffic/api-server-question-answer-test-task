from fastapi import APIRouter, status
from src.database import DbSession
from src.services.user_service import create_user
from src.schemas.user_schemas import UserCreate, UserRead

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def create(session: DbSession, user: UserCreate):
    return await create_user(session, user)
