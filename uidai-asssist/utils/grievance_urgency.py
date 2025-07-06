# grievance_urgency.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)
sentiment_analyzer = SentimentIntensityAnalyzer()

def urgency_score(text):
    sentiment = sentiment_analyzer.polarity_scores(text)['compound']
    emotion = emotion_classifier(text)[0]['label']
    
    if sentiment < -0.5 or emotion in ['anger', 'fear', 'sadness']:
        return "High"
    elif -0.5 <= sentiment < 0.2:
        return "Medium"
    else:
        return "Low"
