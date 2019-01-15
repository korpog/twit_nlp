from twython import Twython
import json
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_sentiment(tweet_text):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(tweet_text)
    return sentiment

def get_query_results(query_term):
    with open('twitter_credentials.json', 'r') as file:
        credentials = json.load(file)

    tweets = Twython(credentials['CONSUMER_KEY'],
                     credentials['CONSUMER_SECRET'])

    query = {'q': query_term,
             'result_type': 'popular',
             'count': 10,
             'lang': 'en',
             }

    return tweets.search(**query)


def get_tweets_data(tweets):
    tweets_list = []
    for status in tweets['statuses']:
        username = status['user']['name']
        text = status['text']
        sentiment = get_sentiment(text)
        dict_ = {'user': username, 'text': text, 'sentiment': sentiment['compound']}
        tweets_list.append(dict_)
    return tweets_list
