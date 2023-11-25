import json
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# Load cleaned tweets
with open('../../data/processed/cleaned_tweets_data.json', 'r') as f:
    cleaned_tweets = json.load(f)

# Sentiment analysis
for item in cleaned_tweets:
    sentiment = sia.polarity_scores(item['tweet'])
    item['sentiment'] = sentiment
# Save sentiments
with open('../../data/processed/sentiments.json', 'w') as f:
    json.dump(cleaned_tweets, f)
