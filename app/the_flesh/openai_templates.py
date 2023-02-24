import os

import openai

openai.organization = os.getenv('OPENAI_ORGANIZATION')
openai.api_key = os.getenv('OPENAI_API_KEY')


def get_text_request(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=3800,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1
    )
    return response['choices'][0]['text']


def get_image_request(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size='1024x1024'
    )
    return response['data'][0]['url']
