from fastapi import Body, FastAPI

from app.doctor_who.text import (
    make_header_for_topic,
    make_seo_optimized_topic_text,
    make_tags_for_topic, make_image_for_topic,
)
from settings import DB_TOPICS_ENGINE

app = FastAPI()


@app.get('/ping/')
def root():
    return {'message': 'pong'}


@app.post('/topic_by_url/')
async def topic_by_url(data=Body()):
    return {
        'message': {
            'header': make_header_for_topic(data['url']),
            'text': make_seo_optimized_topic_text(data['url']),
            'tags': make_tags_for_topic(data['url']),
            'image': make_image_for_topic(make_tags_for_topic(data['url']))
        }
    }
