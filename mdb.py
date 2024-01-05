from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
#import os
#import datetime
#import bson

def insert_one(collection, document:dict):
    try:
        result = collection.insert_one(document)
        if result.inserted_id:
            print("Document inserted successfully with ID:", result.inserted_id)
        else:
            print("Error inserting document")
    except Exception as e:
        print(e)