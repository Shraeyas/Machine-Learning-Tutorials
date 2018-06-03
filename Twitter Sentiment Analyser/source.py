import tweepy
from textblob import TextBlob

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweets in public_tweets:
    print(tweets.text)
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment)
