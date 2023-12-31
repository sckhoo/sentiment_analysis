from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sent import analyze_sentiment
from mdb import insert_one
from dotenv import load_dotenv
import os
import requests
#import pymongo


load_dotenv()
NEWSAPI = os.environ.get("NEWSAPI")
MDB_USER = os.environ.get("MDB_USER")
MDB_PW = os.environ.get("MDB_PW")
MDB_DB = os.environ.get("MDB_DB")
MDB_DB_INSTANCE = os.environ.get("MDB_DB_INSTANCE")
MDB_DB_COLLECTION = os.environ.get("MDB_DB_COLLECTION")

mdb_uri = "mongodb+srv://"+MDB_USER+":"+MDB_PW+"@"+MDB_DB+".mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mdb_uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # connect to database
    db = client[MDB_DB_INSTANCE]
    # Choose the collection to insert the document into
    collection = db[MDB_DB_COLLECTION]
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
            #print("----")
            #print(f"Published: {article['publishedAt']} -> Author: {article['author']} -> Headline: {article['title']}")
            score, magnitude = analyze_sentiment(article['title'])
            document = {
                "publishedAt": article['publishedAt'],
                "author": article['author'],
                "title": article['title'],
                "score": score,
                "magnitude": magnitude
            }  
            insert_one(collection, document)
else:
    # Handle error
    print("NewsAPI Request failed with status code:", response.status_code)
 