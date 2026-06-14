from fastapi import FastAPI
from routes.greetings import router

app = FastAPI()

app.include_router(router)

