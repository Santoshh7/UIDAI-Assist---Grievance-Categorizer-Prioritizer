# grievance_classify.py
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

CATEGORIES = [
    "Authentication failure",
    "Card not delivered",
    "Biometric mismatch",
    "Wrong data in Aadhaar"
]

def classify_complaint(text):
    result = classifier(text, CATEGORIES)
    return result['labels'][0], result['scores'][0]
