# grievance_utils.py
import pandas as pd
import pytesseract
import pdfplumber
from PIL import Image
import re
import io

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@w+|\#','', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def extract_text_from_pdf(file):
    all_text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"
    return clean_text(all_text)

def extract_text_from_image(file):
    image = Image.open(file).convert("RGB")
    text = pytesseract.image_to_string(image)
    return clean_text(text)

def load_complaints(file=None, manual_text=None):
    if file:
        filename = file.name.lower()
        if filename.endswith(".csv"):
            df = pd.read_csv(file)
            df['complaint'] = df['complaint'].astype(str).apply(clean_text)
            return df
        elif filename.endswith(".pdf"):
            extracted = extract_text_from_pdf(file)
            return pd.DataFrame({'complaint': [extracted]})
        elif filename.endswith((".jpg", ".jpeg", ".png")):
            extracted = extract_text_from_image(file)
            return pd.DataFrame({'complaint': [extracted]})
        else:
            raise ValueError("Unsupported file format.")
    elif manual_text:
        return pd.DataFrame({'complaint': [clean_text(manual_text)]})
    else:
        return None
