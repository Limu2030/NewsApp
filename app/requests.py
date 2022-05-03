from urllib import request
# from models import News
import json


# api_key = None
# base_url = None

# def config_request(app):
#     api_key = app.config['NEWS_API_KEY']
#     base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    base_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=497e7187eacd41839283d6145650e5df'

    with request.urlopen(base_url) as url_data:
        get_news_data = url_data.read()
        py_readable_urlData = json.loads(get_news_data) 
        print(py_readable_urlData)


get_news()     

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt') 

        print(f'{title} {description} {urlToImage} {content} {publishedAt}')

    return(news_results)     

