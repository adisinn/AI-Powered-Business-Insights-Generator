import streamlit as st
from dotenv import load_dotenv
import os
from src.insights import generate_insights
from src.ingest import load_csv

load_dotenv()

st.set_page_config(page_title="AI Business Insights", layout="wide")
st.title("AI-Powered Business Insights Generator")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.warning("OPENAI_API_KEY not set — LLM calls will not work. Set it in .env or env vars.")

with st.sidebar:
    st.header("Inputs")
    uploaded = st.file_uploader("Upload report CSV (optional)", type=["csv"])
    report_text = st.text_area("Or paste a textual report here (plain text)", height=300)
    top_n = st.slider("Excerpt sentences to use", 1, 10, 5)
    run = st.button("Generate Insights")

if uploaded is not None:
    df = load_csv(uploaded)
    st.write("Loaded data sample:")
    st.dataframe(df.head())
else:
    df = None

if run:
    if not report_text and df is None:
        st.error("Please upload a CSV or paste a report to generate insights.")
    else:
        data_summary = None
        if df is not None:
            # small automatic summary
            data_summary = df.describe(include='all').to_string()
        text = report_text if report_text else '\n'.join(df.sample(n=1).iloc[0].astype(str).tolist())
        with st.spinner("Generating insights..."):
            out = generate_insights(text, data_summary=data_summary, top_n=top_n)
        st.subheader("Generated Insights")
        st.write(out)
