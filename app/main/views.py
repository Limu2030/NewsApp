from flask import render_template

from app.requests import get_news
from . import main

@main.route('/')
def index(): 
    news = get_news()
    return render_template('index.html', news = news)
    



    #call getnews function
    #watchlist
    #assign a variable , resend the varialbe to the template to be rendered