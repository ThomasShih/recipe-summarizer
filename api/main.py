from fastapi import FastAPI
from lib import lc, pg
from pydantic import BaseModel

app = FastAPI()

class Link(BaseModel):
    url: str

@app.post("/langchain")
async def langchain(link: Link):
    page_contents = lc.extract_from_url(link.url)
    return {
        "message": lc.summarize_recipe(page_contents)
    }

@app.post("/cohere_summarize")
async def cohere_summarize(link: Link):
    page_contents = lc.extract_from_url(link.url)
    return {
        "message": pg.summarize_recipe(page_contents)
    }
