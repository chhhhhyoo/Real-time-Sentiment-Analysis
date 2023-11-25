import json
import matplotlib.pyplot as plt

# Load sentiment data
with open('../../data/processed/sentiments.json', 'r') as f:
    sentiments = json.load(f)

# Extract sentiment scores
negatives = [s['neg'] for s in sentiments]
positives = [s['pos'] for s in sentiments]
neutrals = [s['neu'] for s in sentiments]

# Plotting
plt.plot(negatives, label='Negative', color='red')
plt.plot(positives, label='Positive', color='green')
plt.plot(neutrals, label='Neutral', color='brown')
plt.legend()
plt.title("Sentiment Analysis of K-Pop Tweets")
plt.xlabel("Tweets")
plt.ylabel("Sentiment Score")
plt.savefig('../../data/visualizations/sentiment_trends.pdf')
plt.show()
