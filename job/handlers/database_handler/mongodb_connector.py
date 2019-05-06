import json
from pymongo import MongoClient
import pymongo
import os

MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_URL = os.getenv('MONGO_URL', 'localhost')

def mongo_connect():
    client = MongoClient(MONGO_URL, MONGO_PORT)
    db = client.twitterdb
    col = db.tweets
    return col