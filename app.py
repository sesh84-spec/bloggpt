import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY must be set")

class Topic(BaseModel):
    topic: str

def generate_content(topic: str):
    try:
        title = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Придумай короткий заголовок для поста на тему: {topic}"}],
            max_tokens=60,
            temperature=0.7,
        ).choices[0].message.content.strip()

        post_content = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Напиши пост в Telegram на тему: {topic}. Короткие абзацы, подзаголовки. Без хэштегов."}],
            max_tokens=700,
            temperature=0.7,
        ).choices[0].message.content.strip()

        return {"title": title, "meta_description": "", "post_content": post_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Service is running"}

@app.get("/heartbeat")
async def heartbeat():
    return {"status": "OK"}

@app.post("/generate-post")
async def generate_post(topic: Topic):
    return generate_content(topic.topic)
