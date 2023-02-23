import os

import openai

openai.organization = os.getenv('OPENAI_ORGANIZATION')
openai.api_key = os.getenv('OPENAI_API_KEY')


def make_topic(url):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Зроби рерайт статті {url}',
        temperature=0.7,
        max_tokens=3800,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1
    )
    return response['choices'][0]['text']
