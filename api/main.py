from fastapi import FastAPI
from lib import lc
from pydantic import BaseModel

app = FastAPI()

class Link(BaseModel):
    url: str

@app.post("/langchain")
async def root_post(link: Link):
    page_contents = lc.extract_from_url(link.url)
    return {
        "message": lc.summarize_recipe(page_contents)
    }
