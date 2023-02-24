from fastapi import Body, FastAPI

from app.doctor_who.text import (
    make_header_for_topic,
    make_seo_optimized_topic_text,
    make_tags_for_topic, make_image_for_topic,
)
from app.white_guardian.white_guardian import new_topic

app = FastAPI()


@app.get('/ping/')
def ping():
    return {'message': 'pong'}


@app.get('/topic_by_url/')
async def topic_by_url(data=Body()):
    return {
        'message': {
            'header': make_header_for_topic(data['url']),
            'text': make_seo_optimized_topic_text(data['url']),
            'tags': make_tags_for_topic(data['url']),
            'image': make_image_for_topic(make_tags_for_topic(data['url']))
        }
    }


@app.post('/topic_by_url/')
async def topic_by_url(data=Body()):
    new_topic(
        make_header_for_topic(data['url']).replace('\n', ''),
        make_seo_optimized_topic_text(data['url']).replace('\n', '')
    )
    return {
        'message': 'success'
    }
