from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
async def handle_chat_data():
    return {"message": "Hello World"}
