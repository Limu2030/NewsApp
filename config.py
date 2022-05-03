from distutils.command.config import config
from distutils.debug import DEBUG
import os



class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={497e7187eacd41839283d6145650e5df}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET KEY')


class ProdConfig(config):
    pass

class DevConfig(config):
    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}    