import json
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')


def remove_urls(text):
    # Regex to remove URLs and email addresses
    cleaned_text = re.sub(r'http\S+|www\S+|\S+@\S+|\s@\S+|[^\w\s]|#', '', text)
    return cleaned_text


def lowercase_and_tokenize(text):
    # Lowercase and tokenize text
    text = text.lower()
    tokens = word_tokenize(text)
    return tokens


def remove_stopwords(tokens):
    # Remove English stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in tokens if w not in stop_words]
    return filtered_words


def clean_text(text):
    text = remove_urls(text)
    tokens = lowercase_and_tokenize(text)
    filtered_words = remove_stopwords(tokens)
    return " ".join(filtered_words)


# Load and clean tweets
cleaned_tweet_data = []
with open('../../data/raw/tweet_data.json', 'r') as file:
    for line in file:
        tweet_data = json.loads(line)
        cleaned_text = clean_text(tweet_data['tweet'])
        tweet_data['tweet'] = cleaned_text
        cleaned_tweet_data.append(tweet_data)

# Save cleaned tweets
with open('../../data/processed/cleaned_tweets_data.json', 'w') as file:
    json.dump(cleaned_tweet_data, file)
