from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def root_post():
    return {"message": "Hello World"}