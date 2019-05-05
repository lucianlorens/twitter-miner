import handlers.database_handler.mongodb_connector as mongodb_connector

import handlers.file_handler.file_persistence as file_persistence

import handlers.twitter_handler.twitter_auth as twitter_auth
import handlers.twitter_handler.twitter_listener as twitter_listener

### OAuth Implementation
auth = twitter_auth.twitter_authenticate()

### Setting MongoDB Connection and MongoDB values
mongo_collection = mongodb_connector.mongo_connect()

# Set keywords
keywords = ['bieber']

### Initializing Stream
tweet_listener = twitter_listener.TwitterListener()

twitter_stream = Stream(auth, listener = tweet_listener)

print('Start stream')

twitter_stream.filter(track = keywords, is_async = True)

time.sleep(30)

twitter_stream.disconnect()

print('Close stream')

### Saving to from MongoDB to .tsv file.
save_from_mongodb_to_tsv(mongo_collection)