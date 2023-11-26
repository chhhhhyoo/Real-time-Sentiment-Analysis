import tweepy
import json

# Twitter credentials
consumer_key = 'ENTER HERE'
consumer_secret = 'ENTER HERE'
access_token = 'ENTER HERE'
access_token_secret = 'ENTER HERE'

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print(api.rate_limit_status())

# Listener Class


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print("collection successful")
        tweet_data = {
            'tweet': status.text,
            'username': status.user.screen_name,
            'followers_count': status.user.followers_count,
            'retweet_count': status.retweet_count
        }
        try:
            with open('../data/raw/tweet_data.json', 'a') as f:
                json.dump(tweet_data, f)
                f.write('\n')
        except Exception as e:
            print(f"Error in on_status: {e}")


# Create StreamListener instance
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

# Keywords
keywords = ['#KPop', '#LESSERAFIM', '#IVE', '#NEWJEANS',
            '#AESPA', '#NMIXX', '#ITZY', '#fromis_9']

# Start streaming
stream.filter(track=keywords)
