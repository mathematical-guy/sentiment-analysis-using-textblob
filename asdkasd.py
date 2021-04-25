import tweepy
import re
import twitter_credentials
import tweepy
class LISTENER(tweepy.StreamListener):
    def on_data(self, raw_data):                   #take in data from streamlistener
        print(raw_data)
        return True
    def on_error(self, status_code):               #prints encountered error
        print(status_code)


name = input("Enter name whose tweets you want to retrieve?")
listenerobject = LISTENER()     #LISTENER OBJECT
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
tweetcount = 10
streamobject = tweepy.Stream(auth, listenerobject)
streamobject.filter(track = name)
tweets = tweepy.api.user_timeline(id = name, count = tweetcount)
for tweet in tweets:
    f = open("Tweets.text", 'a')
    print(tweet)
    f.write(tweet)




