import streamlit as st
from dotenv import load_dotenv
import os
from src.insights import generate_insights
from src.ingest import load_csv, query_sql

load_dotenv()

st.set_page_config(page_title="AI Business Insights", layout="wide")
st.title("AI-Powered Business Insights Generator")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.warning("⚠️ GROQ_API_KEY not set — using rule-based fallback insights. Set it in `.env` to use Groq's LLM.")
elif api_key.startswith("gsk_"):
    st.success("✅ Groq API key detected. Using Llama-3.3-70b model for insights.")
else:
    st.warning("⚠️ API key format not recognized. Using rule-based fallback.")

# Create tabs for different input modes
tab1, tab2, tab3 = st.tabs(["CSV Upload", "SQL Query", "Paste Report"])

df = None
report_text = ""

with tab1:
    st.header("📊 Upload CSV Report")
    uploaded = st.file_uploader("Upload report CSV", type=["csv"], key="csv_upload")
    if uploaded is not None:
        df = load_csv(uploaded)
        st.write("Data loaded successfully:")
        st.dataframe(df.head(10))

with tab2:
    st.header("🗄️ Query Database")
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        st.warning("⚠️ DATABASE_URL not set in `.env`. Set it to enable SQL queries.")
    else:
        sql_query = st.text_area(
            "Enter SQL query:",
            value="SELECT * FROM reports LIMIT 5;",
            height=150,
            help="Write a SQL query to fetch data from your database"
        )
        if st.button("Execute Query"):
            try:
                df = query_sql(sql_query, connection_string=database_url)
                st.write(f"Query returned {len(df)} rows:")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Query failed: {e}")

with tab3:
    st.header("📝 Paste Report Text")
    report_text = st.text_area("Paste your report text here:", height=300)

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Settings")
    top_n = st.slider("Number of key sentences to extract", 1, 10, 5)
    
    # Prepare input
    input_ready = False
    input_text = ""
    
    if uploaded is not None and df is not None:
        st.info("✓ CSV data loaded")
        input_ready = True
        # Convert first report column to text
        for col in df.columns:
            if 'report' in col.lower() or 'text' in col.lower():
                input_text = df[col].iloc[0]
                break
        if not input_text and len(df.columns) > 0:
            input_text = df.iloc[0, 0]
    elif database_url and df is not None:
        st.info("✓ SQL query results loaded")
        input_ready = True
        # Convert first text column to text
        for col in df.columns:
            if 'report' in col.lower() or 'text' in col.lower():
                input_text = df[col].iloc[0]
                break
        if not input_text and len(df.columns) > 0:
            input_text = df.iloc[0, 0]
    elif report_text.strip():
        st.info("✓ Report text pasted")
        input_ready = True
        input_text = report_text
    
    generate = st.button("🚀 Generate Insights", use_container_width=True)

# Generate insights
if generate:
    if not input_ready:
        st.error("❌ Please upload a CSV, run a SQL query, or paste a report.")
    else:
        data_summary = None
        if df is not None:
            data_summary = df.describe(include='all').to_string()
        
        with st.spinner("✨ Generating insights..."):
            out = generate_insights(input_text, data_summary=data_summary, top_n=top_n)

        st.divider()
        st.subheader("📈 Generated Insights")

        if out.startswith("["):
            st.error("❌ Model is not working: " + out)
        else:
            st.success("✅ Model response:")
            st.write(out)
