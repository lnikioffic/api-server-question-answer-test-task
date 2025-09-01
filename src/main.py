from fastapi import FastAPI
from src.routers import question_router, user_router, answer_router

app = FastAPI()
app.include_router(question_router.router)
app.include_router(user_router.router)
app.include_router(answer_router.router)


@app.get('/')
async def root():
    return {'message': 'Welcome to the Question-Answer API'}
