from app.the_flesh.openai_templates import (
    get_text_request,
    get_image_request,
)


def make_header_for_topic(url):
    return get_text_request(f'Придумай заголовок для статті за посиланням {url}')


def make_seo_optimized_topic_text(url):
    return get_text_request(f'Зроби рерайт статті {url}. Результат має бути SEO-оптимізованим')


def make_tags_for_topic(url):
    return get_text_request(f'Підбери 5 ключових слів для новини {url}, перелічи їх через кому')


def make_image_for_topic(topic_title):
    return get_image_request(topic_title)
