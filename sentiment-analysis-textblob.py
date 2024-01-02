from textblob import TextBlob

# Array of comment strings
comments = ["This product is amazing!", "I am very disappointed with the service.", "What a fantastic experience.", "Worst experience ever.", "Absolutely love this!"]

# Function to perform sentiment analysis
def analyze_sentiments(comments):
    for comment in comments:
        blob = TextBlob(comment)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            print(f'Comment: "{comment}" - Sentiment: Positive')
        elif sentiment < 0:
            print(f'Comment: "{comment}" - Sentiment: Negative')
        else:
            print(f'Comment: "{comment}" - Sentiment: Neutral')

# Analyzing the sentiments
analyze_sentiments(comments)
