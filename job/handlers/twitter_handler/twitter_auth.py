from tweepy.streaming import StreamListener
from tweepy.auth import OAuthHandler
from tweepy import Stream

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)