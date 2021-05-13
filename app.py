from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from newsapi import NewsApiClient

app = Flask(__name__)
my_api_key = '4da6b3bee82a4f26aa7fb66537d31e3f'

# starting page


@app.route('/')
def index():
    return render_template('index.html', context=get_news(True, None, None), start=True)


# get the news for the users' input
@app.route('/get_news', methods=['POST', 'GET'])
def news_bar():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        temp = request.args.get('char1')
        temp2 = int(request.args.get('num1'))
        return render_template('base.html', char1=temp, num1=temp2, start=False, context=get_news(False, temp, temp2))


def get_news(start, url_query, num_articles):
    newsapi = NewsApiClient(api_key=my_api_key)
    if (start == True):
        # get headlines
        topheadlines = newsapi.get_top_headlines(
            country='ca', category='business')
        articles = topheadlines['articles']
    else:
        data = newsapi.get_everything(
            q=url_query, language='en', page_size=num_articles)
        articles = data['articles']

    # get info for the articles
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
    return mylist


if __name__ == "__main__":
    app.run(debug=True)
