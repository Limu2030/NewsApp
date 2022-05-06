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
        finlist = process_results(py_readable_urlData)




def process_results(url_list):
    url_results = []
    for url_item in url_list['articles']:
        title = url_item.get('title')
        description = url_item.get('description')
        urlToImage = url_item.get('urlToImage')
        content = url_item.get('content')
        publishedAt = url_item.get('publishedAt') 

        print(f'{title} {description} {urlToImage} {content} {publishedAt}')

    return(url_results)     

get_news() 