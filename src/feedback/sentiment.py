

from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze emotional
    Between -1 (Very negative) +1 (Very Positive)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity
