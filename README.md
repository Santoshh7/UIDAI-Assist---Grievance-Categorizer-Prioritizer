# 📋 UIDAI Assist — Grievance Categorizer & Prioritizer

UIDAI Assist — Grievance Categorizer & Prioritizer is an AI-powered Streamlit application designed to automate the handling of Aadhaar-related complaints. By leveraging advanced NLP models, it classifies grievances into predefined categories, summarizes lengthy complaints for quick review, and assigns urgency scores based on sentiment and emotional cues.

The app supports inputs in various formats—including CSV files, scanned documents (PDFs), and images (JPG/PNG)—making it ideal for digitizing and processing complaints from physical or digital sources. UIDAI Assist aims to reduce manual overhead, accelerate response times, and improve citizen satisfaction by helping public service teams prioritize and resolve issues more efficiently.

This Streamlit app helps categorize, summarize, and prioritize Aadhaar-related grievances based on uploaded complaints. It uses state-of-the-art NLP models to assist customer service teams in sorting issues faster.

---
**CAUTION** : **DO NOT USE REAL IDs FOR DEMO**
**USE SAMPLES UPLOADED IN THE samples/... FOR DEMO**

## 🚀 Features

- Upload complaints as **CSV, PDF, or Image (JPG/PNG)**
- Or enter a complaint **manually**
- Automatically:
  - **Categorizes** the complaint
  - **Summarizes** it for quick understanding
  - **Prioritizes** based on urgency using sentiment & emotion analysis
- Download results as **CSV**

---



## 🧠 Tech Stack

- **Streamlit** for UI
- **Transformers (Hugging Face)**:
  - BART for summarization & classification
  - DistilRoBERTa for emotion detection
- **VADER** for sentiment analysis
- **Tesseract OCR** via `pytesseract` for image processing
- **pdfplumber** for PDF text extraction

---
Developed By **SANTOSH THAKUR**
