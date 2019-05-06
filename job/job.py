import handlers.database_handler.mongodb_connector as mongodb_connector

import handlers.file_handler.file_persistence as file_persistence

import handlers.twitter_handler.twitter_auth as twitter_auth
import handlers.twitter_handler.twitter_listener as twitter_listener

### OAuth Implementation
app.logger.info('Authenticating: ', end='')
auth = twitter_auth.twitter_authenticate()
app.logger.info('success!')
app.logger.info(auth)

### Setting MongoDB Connection and MongoDB values
app.logger.info('Connecting to Mongo:', end='')
mongo_collection = mongodb_connector.mongo_connect()
app.logger.info('success!')
app.logger.info(mongo_collection)

# Set keywords
keywords = ['bieber']

### Initializing Stream
tweet_listener = twitter_listener.TwitterListener()

twitter_stream = Stream(auth, listener = tweet_listener)

app.logger.info('======= Start stream =======')

twitter_stream.filter(track = keywords, is_async = True)

time.sleep(30)
app.logger.info('waiting time finished.')
twitter_stream.disconnect()
app.logger.info('Stream Disconnected.')
app.logger.info('======= Close stream =======')

### Saving to from MongoDB to .tsv file.
app.logger.info('Saving to file')
save_from_mongodb_to_tsv(mongo_collection)
app.logger.info('File saved')