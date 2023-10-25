from fastapi import FastAPI
from lib import summarize_recipe, extract_from_url
from pydantic import BaseModel

app = FastAPI()

class Link(BaseModel):
    url: str

@app.post("/")
async def root_post(link: Link):
    page_contents = extract_from_url(link.url)
    return {
        "message": summarize_recipe(page_contents)
    }
