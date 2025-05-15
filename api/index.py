from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Request(BaseModel):
    payload: str

@app.post("/api/auth")
async def handle_auth(request: Request):
    data = json.loads(request["payload"])
    return data

@app.get("/api/hello")
async def handle_chat_data():
    return {"message": "Hello World"}
