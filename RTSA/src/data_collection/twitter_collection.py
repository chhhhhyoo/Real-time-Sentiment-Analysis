import tweepy
import json

# Bearer Token
bearer_token = '***REMOVED***'

# Define the Stream Listener


class CustomStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print("Received a tweet!")
        try:
            # Fetch user details
            user_data = client.get_user(id=tweet.author_id).data

            tweet_data = {
                'tweet': tweet.text,
                'author_id': tweet.author_id,
                'username': user_data.username,
                'followers_count': user_data.public_metrics['followers_count']
            }

            with open('../../data/raw/tweet_data.json', 'a') as f:
                json.dump(tweet_data, f)
                f.write('\n')
        except Exception as e:
            print(f"Error in on_tweet: {e}")


# Initialize Stream
stream_listener = CustomStreamListener(bearer_token=bearer_token)

# Keywords
keywords = ['#KPop', '#LESSERAFIM', '#IVE', '#NEWJEANS',
            '#AESPA', '#NMIXX', '#ITZY', '#fromis_9']

# Add rules for each keyword
for keyword in keywords:
    stream_listener.add_rules(tweepy.StreamRule(keyword))

# Start streaming
stream_listener.filter()
