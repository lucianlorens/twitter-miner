import handlers.database_handler.mongodb_connector as mongodb_connector
import handlers.file_handler.file_persistence as file_persistence
import handlers.twitter_handler.twitter_auth as twitter_auth
import handlers.twitter_handler.twitter_listener as twitter_listener

# OAuth keys

# MongoDB values
### Setting MongoDB Connection

### OAuth Implementation

keywords = ['bieber']

### Initializing Stream
twitter_listener = TwitterListener()
twitter_stream = Stream(auth, listener = twitter_listener)

print('Start stream')
#mystream.filter(track=keywords)
twitter_stream.filter(track = keywords, is_async = True)
#mystream.filter(track = keywords, async = True)

time.sleep(30)

twitter_stream.disconnect()

print('Close stream')

### Saving to from MongoDB to .tsv file.
