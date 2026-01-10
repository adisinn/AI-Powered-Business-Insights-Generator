# Slide 1 - Title

AI-Powered Business Insights Generator

---

# Slide 2 - Problem

Analysts spend hours reading reports; insights are fragmented and hard to operationalize.

---

# Slide 3 - Solution

Automated insight extraction using lightweight NLP + LLMs; conversational dashboard for Q&A.

---

# Slide 4 - Architecture

- Ingest CSV / SQL
- Extract key sentences
- Build prompt → LLM or fallback
- Serve via Streamlit (or embed in Power BI)

---

# Slide 5 - Demo Walkthrough

1. Upload or paste report
2. Adjust `top_n` to control excerpt size
3. Generate insights and export

---

# Slide 6 - Example Insight

- Insight: Scale email channel
- Explanation: Higher conversion observed in email campaigns
- Metric: Email conversion rate, CAC

---

# Slide 7 - Interview talking points

- Explain prompt design and evaluation
- Discuss fallback strategies for offline demos
- Show metrics you'd track and A/B tests you'd run

---

# Slide 8 - Next Steps

- Add model evaluation and human-in-the-loop feedback
- Add scheduled generation and Power BI automation

---

# Slide 9 - How to run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

---

# Slide 10 - Contact

Your Name — Data Analyst candidate
LinkedIn / GitHub / Email
