import json
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# Load cleaned tweets
with open('../../data/processed/cleaned_tweets.json', 'r') as f:
    cleaned_tweets = json.load(f)

# Sentiment analysis
sentiments = [sia.polarity_scores(tweet) for tweet in cleaned_tweets]

# Save sentiments
with open('../../data/processed/sentiments.json', 'w') as f:
    json.dump(sentiments, f)
