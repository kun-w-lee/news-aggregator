# Init
from newsapi import NewsApiClient
from urllib.parse import quote
import urllib.request
import requests
import pandas as pd
import datetime as dt


my_api_key = '4da6b3bee82a4f26aa7fb66537d31e3f'
newsapi = NewsApiClient(api_key=my_api_key)


def get_news():
    query = input('Enter you query:')
    url_query = quote(query)
    pg_size = int(input('Enter the number of news you wish to get:'))
    numb = 10
    data = newsapi.get_everything(
        q=url_query, language='en', page_size=pg_size)

    articles = data['articles']

    # print(articles)

    # for x, y in enumerate(articles):
    #     print(f'{x} {y["title"]}')

    for key, value in articles[0].items():
        print(f"\n{key.ljust(15)} {value}")

    # print(articles[0].items)

    # pub_date = dt.datetime.strptime(
    #     articles[0]['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").date()

    # print(pub_date)
    # print(pub_date.year)
    # print(pub_date.month)
    # print(pub_date.day)


get_news()
