
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_URL = os.getenv('MONGO_URL', 'localhost')

### Setting MongoDB Connection

import json
from pymongo import MongoClient
import pymongo

client = MongoClient(MONGO_URL, MONGO_PORT)
db = client.twitterdb
col = db.tweets
raw_col = db.raw_data
keywords = ['bieber']