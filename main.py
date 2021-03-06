import tweepy
import pandas as pd
import twitter_credentials
from tweepy import OAuthHandler

"""Cleaning Tweets!"""

def clean_links(string):
    words = []
    ar = string.split(' ')          #array of words
    for x in ar:                    #reading one word at time
        if not (x.find('http')):
            pass
        else:
            words.append(x)
    string = ' '.join(words)
    print(string)
    return string

#----------------------------------------------------------------------------------------------

def clean_at_the_rate(word):
    for x in word:
        if (x == '@'):
            return False
    return True

#----------------------------------------------------------------------------------------------

def clean_hashtag(word):
    for x in word:
        if (x == '#'):
            return False
    return True

#----------------------------------------------------------------------------------------------

def clean_othersymbols(string):
    words = string.split(' ')
    clean_words = []
    for word in words:
        if(word == '[a-z][A-Z]+'):
            clean_words.append(word)

    cleaned_string = ' '.join(clean_words)
    return cleaned_string

#----------------------------------------------------------------------------------------------

def cleaning_tweet(str):
    s1 = clean_links(str)
    string = s1.split(' ')
    words = []
    for word in string:
        if (clean_hashtag(word) and clean_at_the_rate(word)):
            words.append(word)
    s1 = ' '
    s2 = s1.join(words)
    print(s1)
    s3 = clean_othersymbols(s2)
    return s3

#----------------------------------------------------------------------------------------------

"""Converting Tweets into dataframe"""


def tweet_to_dataframe(tweets):
    tweetss = []
    for tweet in tweets:
        if tweet.lang == "en":
            tweetss.append(tweet)
    df = pd.DataFrame(data=[tweet.text for tweet in tweetss], columns=['Tweets'])
    df['ID'] = [tweet.id for tweet in tweetss]
    df['Retweet'] = [tweet.retweet_count for tweet in tweetss]
    df['Length of Tweet'] = [len(tweet.text) for tweet in tweetss]
    df['Clean Tweet'] = [cleaning_tweet(tweet.text) for tweet in tweetss]
    df.to_csv(r'tweetsincsv.csv')

#----------------------------------------------------------------------------------------------


auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='narendramodi', count=100)

# for tweet in tweets:
#     if tweet.lang == "en":
#         #print(tweet.text)
# print(type(tweets))
print("***************************************\n")
tweet_to_dataframe(tweets)
