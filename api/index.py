from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api/auth")
async def handle_auth(payload: Optional[str] = None):
    data = json.loads(payload)
    return data

@app.get("/api/hello")
async def handle_chat_data():
    return {"message": "Hello World"}
