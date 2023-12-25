from newsapi import NewsApiClient
from sent import analyze_sentiment
from dotenv import load_dotenv
import os

load_dotenv()
NEWSAPI = os.environ.get("NEWSAPI")

# Init
newsapi = NewsApiClient(api_key=NEWSAPI)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(category='sports',
                                          country='my',
                                          language='en')

if top_headlines['totalResults'] != 0:
    print(top_headlines['totalResults'])
    #for article in top_headlines['articles']:
    #    print(f"Author: {article['author']} -> Headline: {article['title']}")
    #    analyze_sentiment(article['title'])
else:
    print("no news")



