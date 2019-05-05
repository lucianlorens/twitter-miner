import handlers.database_handler.mongodb_connector as mongodb_connector

import handlers.file_handler.file_persistence as file_persistence

import handlers.twitter_handler.twitter_auth as twitter_auth
import handlers.twitter_handler.twitter_listener as twitter_listener

### OAuth Implementation
print('Authenticating: ', end='')
auth = twitter_auth.twitter_authenticate()
print('success!')
print(auth)

### Setting MongoDB Connection and MongoDB values
print('Connecting to Mongo:', end='')
mongo_collection = mongodb_connector.mongo_connect()
print('success!')
print(mongo_collection)

# Set keywords
keywords = ['bieber']

### Initializing Stream
tweet_listener = twitter_listener.TwitterListener()

twitter_stream = Stream(auth, listener = tweet_listener)

print('======= Start stream =======')

twitter_stream.filter(track = keywords, is_async = True)

time.sleep(30)
print('waiting time finished.')
twitter_stream.disconnect()
print('Stream Disconnected.')
print('======= Close stream =======')

### Saving to from MongoDB to .tsv file.
print('Saving to file')
save_from_mongodb_to_tsv(mongo_collection)
print('File saved')