from fastapi import Body, FastAPI

from app.doctor_who.text import make_topic

app = FastAPI()


@app.get("/ping/")
async def ping():
    return {"message": "pong"}


@app.post("/topic_by_url/")
async def topic_by_url(data=Body()):
    return {"message": make_topic(data['url'])}

