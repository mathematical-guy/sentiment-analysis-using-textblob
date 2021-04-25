from textblob import TextBlob
import tweepy
import pandas as pd
import twitter_credentials
from tweepy import Cursor
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
"""Cleaning Tweets!"""

def clean_links(string):
    ss = ' '
    words = []
    ar = string.split(' ')          #array of words
    for x in ar:                    #reading one word at time
        if (x.find('http') == -1):
            words.append(x)
        else:
            pass

    string = ss.join(words)
    print(string)
    return string

def clean_at_the_rate(word):
    for x in word:
        if (x == '@'):
            return False
    return True


def clean_hashtag(word):
    for x in word:
        if (x == '#'):
            return False
    return True


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
    return s2


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
    #df['Polarity'] = [tweet.polarity for tweet in TextBlob(cleaning_tweet(tweet))]
    df['Polarity'] = [sentimental_analysis(x) for x in df['Clean Tweet']]
    df.to_csv(r'C:\Users\MOHIT TALREJA\Desktop\sentimental Analysis Twitter\tweetsincsv.csv')
    drawing_piechart(list(df['Clean Tweet']))


"""Sentimental Analysis"""
def sentimental_analysis(tweet):
    tww = cleaning_tweet(tweet)
    blob = TextBlob(tww)
    print(blob.polarity)
    return blob.polarity

def percentage(list):
    lisst = []
    positive = 0
    negative = 0
    neutral = 0
    for p in list:
        if(p > 0):
            positive = positive + 1
        elif(p == 0):
            neutral = neutral + 1
        else:
            negative = negative + 1
    positive = (positive/len(list))
    lisst.append(positive)
    negative = (negative / len(list))
    lisst.append(negative)
    neutral = (neutral / len(list))
    lisst.append(neutral)
    return lisst

def drawing_piechart(Cleaned_Tweets):
    polarities = [sentimental_analysis(tweet)*10 for tweet in Cleaned_Tweets]
    #print(polarities)
    sizes = percentage(polarities)
    labels = ['Positive', 'Neutral', 'Negative']
    colors = ['green', 'yellow', 'red']
    plt.pie(sizes, labels = labels, colors = colors, autopct = '%1.1f%%')
    plt.axis('equal')
    plt.show()

scname=input("Enter query for search: ")
tcount=int(input("How many tweets do you want to fetch?: "))
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
tweets = tweepy.Cursor(api.search, q = scname, lang = "en").items(tcount)
#print(type(tweets))
# for tweet in tweets:
#     if tweet.lang == "en":
#         #print(tweet.text)
# print(type(tweets))
print("*************************************************************************************\n")
tweet_to_dataframe(tweets)