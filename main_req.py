from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sent import analyze_sentiment
from dotenv import load_dotenv
import os
import requests
import pymongo


load_dotenv()
NEWSAPI = os.environ.get("NEWSAPI")
MDB = os.environ.get("MDB")

mdb_uri = "mongodb+srv://sckhoo:"+MDB+"@workshop-bakery.uflbdbq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mdb_uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
my_authors = ["The Star Online", "Malaysiakini", "Malay Mail", "New Straits Times", "Free Malaysia Today"]

# Init
url = "https://newsapi.org/v2/top-headlines"  # Replace with the actual API endpoint
params = {"category": "general", "country":"my", "apiKey":NEWSAPI}

response = requests.get(url, params=params)
 
if response.status_code == 200:
    # Successful response
    print("Request success with status code:", response.status_code)
    data = response.json()  # Assuming a JSON response
    print(data['totalResults'])
    for article in data['articles']:
        if article['author'] in my_authors:
            print("----")
            print(f"Published: {article['publishedAt']} -> Author: {article['author']} -> Headline: {article['title']}")
            analyze_sentiment(article['title'])
else:
    # Handle error
    print("Request failed with status code:", response.status_code)
 