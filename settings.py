import os
from enum import Enum

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ORGANIZATION = os.getenv('OPENAI_ORGANIZATION')


class DATABASES:
    class DB_TOPICS(Enum):
        USERNAME = os.getenv('DB_TOPICS_USERNAME')
        PASSWORD = os.getenv('DB_TOPICS_PASSWORD')
        HOST = os.getenv('DB_TOPICS_HOST')
        PORT = os.getenv('DB_TOPICS_PORT')
        DATABASE = os.getenv('DB_TOPICS_DATABASE', 3306)
