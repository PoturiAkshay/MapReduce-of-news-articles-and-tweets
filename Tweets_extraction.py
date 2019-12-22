#importing all the required libraries
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import Credentials
import json
import re

from pymongo import MongoClient

#establishing Mongo DB connection
connection = MongoClient()
db=connection.super

#class in which streaming tweets are handled(cleaned and stored in database)
class StreamingTweets(StreamListener):
    def __init__(self):
        self.counter = 0
    def on_data(self,tweet):
        self.counter=self.counter+1
        JTweet=json.loads(tweet)

        JTweet["text"] = re.sub(r"http\S+", '', JTweet["text"], flags=re.MULTILINE)

        remove_emoji = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
        JTweet["text"] = remove_emoji.sub(r'', JTweet["text"])

        #print(JTweet["text"])
        db.tweets.insert_one(JTweet)
        if(self.counter==1000):
            return False
        return True
    def on_error(self,error_status):
        print(error_status)

listener=StreamingTweets()
authorization=OAuthHandler(Credentials.CONSUMER_KEY,Credentials.CONSUMER_KEY_SECRET)
authorization.set_access_token(Credentials.ACCESS_TOKEN,Credentials.ACCESS_TOKEN_SECRET)

Data_Flow = Stream(authorization,listener)
Data_Flow.filter(track=['Canada','Canada import','Canada export','Canada vehicle sales','Canada Education'])

import tweepy as tw
api = tw.API(authorization)

#extracting the tweets using the search api
Extracted_tweets = tw.Cursor(api.search,q=('Canada OR Canada+import OR Canada+export OR Canada+vehicle+sales OR Canada+Education'),lang="en").items(1000)

#cleaning the tweet's text and inserting in Mongo DB
for tweet in Extracted_tweets:
    tweet=tweet._json
    tweet["text"] = re.sub(r"http\S+", '', tweet["text"], flags=re.MULTILINE)
    remove_emoji = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    tweet["text"]= remove_emoji.sub(r'', tweet["text"])
    #print(tweet["text"])
    db.tweets.insert_one(tweet)
