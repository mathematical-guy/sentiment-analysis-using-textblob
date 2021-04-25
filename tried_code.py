import tweepy
import re
import twitter_credentials
from tweepy import OAuthHandler
def cleaning_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+://\S+)", " ", tweet).split())

#name = input("Enter Name: ")
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
tweets = []
for tweet in tweepy.Cursor(api.user_timeline, id = 'Vatsal_Gamit').items(3):
    print(tweet.text)
    print("\n----------------------------------------------------------\n")
    x = cleaning_tweet(tweet.text)
    tweets.append(x)
    print(x)
#
# print(tweets)
# print("***************************************\n")
# print(x)
