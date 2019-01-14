from twython import Twython
import json
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


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


def tweets_to_dict(tweets):
    tweets_dict = {'user': [], 'text': []}
    t_list = []
    for status in tweets['statuses']:
        username = status['user']['name']
        text = status['text']
        dict_ = {'user': username, 'text': text}
        t_list.append(dict_)
        tweets_dict['user'].append(status['user']['name'])
        tweets_dict['text'].append(status['text'])
    return t_list
