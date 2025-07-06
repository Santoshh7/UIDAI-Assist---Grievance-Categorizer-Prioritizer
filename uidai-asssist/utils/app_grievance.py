# app_grievance.py
import streamlit as st
import pandas as pd
from grievance_utils import load_complaints
from grievance_classify import classify_complaint
from grievance_summarizer import summarize_text
from grievance_urgency import urgency_score

st.set_page_config(page_title="UIDAI Assist — Grievance Categorizer", layout="wide")
st.title("📋 Aadhaar Grievance Categorizer & Prioritizer")

uploaded_file = st.file_uploader(
    "Upload Complaint File (CSV / PDF / JPG / PNG)", 
    type=["csv", "pdf", "jpg", "jpeg", "png"]
)
manual_text = st.text_area("Or enter a complaint manually")

if uploaded_file or manual_text:
    try:
        df = load_complaints(uploaded_file, manual_text)

        if df is not None and not df.empty:
            results = []
            for i, row in df.iterrows():
                complaint = row['complaint']
                category, confidence = classify_complaint(complaint)
                summary = summarize_text(complaint)
                urgency = urgency_score(complaint)
                results.append([i+1, complaint, category, summary, urgency])

            output_df = pd.DataFrame(
                results, columns=["ID", "Complaint", "Category", "Summary", "Urgency"]
            )

            st.dataframe(output_df, use_container_width=True)
            st.download_button("📥 Download Results as CSV", output_df.to_csv(index=False), file_name="complaint_results.csv")
        else:
            st.warning("No text could be extracted.")
    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")
