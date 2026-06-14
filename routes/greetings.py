from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/")
async def greetings():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://go_app:8080/answer")

    return response.json()

@router.get("/answer")
async def greetings():
    return {"msg": "Hello from Python!!!"}

