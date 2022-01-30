from flask import render_template,request,redirect,url_for
from . import main
# from app.models import news
from ..request import getNews,get_news

# Views
@main.route('/')
def index():
    content_news = getNews('content')
    tech_news = getNews('tech')
    articles_news = getNews('articles')
    title = 'Home - Faska News Channel'
    return render_template('index.html', title = title,content= content_news,tech=tech_news,articles=articles_news)
   
@main.route('/news/<name>')
def news(name):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = getNews(name)
    # title = f'{news.title}'

    return render_template('news.html',news= news)    