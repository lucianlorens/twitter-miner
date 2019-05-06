import json
from pymongo import MongoClient
import pymongo
import os

MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_URL = os.getenv('MONGO_URL', 'mongodb://mongo:27017')

def mongo_connect():
    #client = MongoClient(MONGO_HOST, MONGO_PORT)
    client = MongoClient(MONGO_URL)
    db = client.twitterdb
    col = db.tweets
    return col