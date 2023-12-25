from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import datetime
import bson

document = {
    "publishedAt": "2023-12-21T01:22:12Z",
    "author": "Malaysiakini",
    "title": "Stop taking holier-than-thou approach to make us look corrupt, Rafizi told - Malaysiakini",
    "score": 0.3,
    "magnitude": 0.6
}

load_dotenv()
MDB_USER = os.environ.get("MDB_USER")
MDB_PW = os.environ.get("MDB_PW")

uri = "mongodb+srv://"+MDB_USER+":"+MDB_PW+"@workshop-bakery.uflbdbq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # Access the database:
    db = client["Newsapi_Sentiment"]

    # Choose the collection to insert the document into
    collection = db["headlines"]
    
    result = collection.insert_one(document)
    if result.inserted_id:
        print("Document inserted successfully with ID:", result.inserted_id)
    else:
        print("Error inserting document")
except Exception as e:
    print(e)
    
    
# Example 1: Find a document by a specific field value
#result = collection.find_one({"name": "John Doe"})