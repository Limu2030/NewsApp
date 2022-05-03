from urllib import request
import json



def get_news():
    base_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=497e7187eacd41839283d6145650e5df'

    with request.urlopen(base_url) as url_data:
        get_news_data = url_data.read()
        py_readable_urlData = json.loads(get_news_data) 
        print(py_readable_urlData)


get_news()        
