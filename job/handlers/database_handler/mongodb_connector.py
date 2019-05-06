import json
from pymongo import MongoClient
import pymongo
import os

MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')

def mongo_connect():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.twitterdb
    col = db.tweets
    return col