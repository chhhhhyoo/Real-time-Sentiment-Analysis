# Real-time-Sentiment-Analysis
Tracking K-Pop Sentiment on Twitter

1. Data Collection
   - fetch real time tweets from twitter [data storage] -> data/raw/
2. Data Preprocessing
   - preprocess the collected tweets
     - [data load] -> data/raw/
     - text cleaning
     - [data storage] -> data/processed/
3. Sentiment Analysis
   - perform sentiment analysis on processed tweets
     - [data load] -> data/processed/
     - sentiment analysis (VADER)
     - [data storage] -> data/processed/
4. Visualization (Matplotlib)
   - [data load] -> data/processed/
   - [save pdf & show] -> data/visualizations/

## Additional Analysis

### Topic Modeling (LDA - 5 topics)
Discover the main topics discussed in K-Pop tweets

### Influencer Identification
Identify key influencers in K-Pop discussions on Twitter
