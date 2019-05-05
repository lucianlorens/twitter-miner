import handlers.
import handlers.
import handlers.


# OAuth keys

# MongoDB values
### Setting MongoDB Connection

### OAuth Implementation


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
