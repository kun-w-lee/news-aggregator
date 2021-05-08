from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from newsapi import NewsApiClient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

my_api_key = '4da6b3bee82a4f26aa7fb66537d31e3f'


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key=my_api_key)
    topheadlines = newsapi.get_top_headlines(country='ca', category='business')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    source = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        source.append(myarticles['source'])

    mylist = zip(news, desc, img, source)

    return render_template('index.html', context=mylist)


def get_news():
    newsapi = NewsApiClient(api_key=my_api_key)
    topheadlines = newsapi.get_top_headlines(country='ca', category='business')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)


if __name__ == "__main__":
    app.run(debug=True)
