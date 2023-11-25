import tweepy
import json

# Twitter credentials


# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Listener Class


class StreamListener(tweepy.Stream):
    def on_status(self, status):
        print(status.text)
        with open('../../data/raw/tweets.json', 'a') as f:
            json.dump(status._json, f)
            f.write('\n')


# Keywords
keywords = ['#KPop', '#BTS', '#Blackpink']

# Streaming
stream_listener = StreamListener(consumer_key, consumer_secret,
                                 access_token, access_token_secret)
stream_listener.filter(track=keywords)
