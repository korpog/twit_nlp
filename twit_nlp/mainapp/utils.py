from twython import Twython  
import json

def get_query(query_term):
    with open('twitter_credentials.json', 'r') as file:
        credentials = json.load(file)
    
    tweets = Twython(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])

    query = {'q': 'learn python',  
        'result_type': 'popular',
        'count': 100,
        'lang': 'en',
        }

    return tweets.search(**query)