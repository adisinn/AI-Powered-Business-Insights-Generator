# AI-Powered Business Insights Generator

An end-to-end student project that ingests reports and data, uses LLMs to extract insights, and serves a conversational dashboard prototype.

What you'll find:
- `src/` — core modules: ingestion, NLP prompt helpers, insight generation
- `app.py` — Streamlit prototype for conversational insights
- `scripts/demo.py` — simple end-to-end demo script
- `sample_data/sample_reports.csv` — example report data

Quick start (Windows PowerShell):

1. Create a virtual env and install requirements

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Copy `.env.example` → `.env` and set `OPENAI_API_KEY` (or set env var)

3. Run the Streamlit app

```powershell
streamlit run app.py
```

Notes:
- This repo uses an LLM (OpenAI compatible) for automated insight generation. Replace with your preferred LLM.
- See `PowerBI.md` for guidance on connecting generated insights to Power BI (optional).

Tests & CI
- Run tests locally with `pytest` after installing requirements.
- A GitHub Actions workflow is included at `.github/workflows/ci.yml` to run tests on push and PRs.

Interview / Demo tips
- Use `top_n` to tune how many excerpt sentences are fed to prompts.
- Use prompts in `PROMPTS.md` or `src/prompt_templates.py` to demonstrate different lines of analysis (growth vs retention).
- Use the `slides.md` file as a quick 10-slide deck for interviews.

Additional notes
- `top_n` controls how many key sentences are extracted from reports and used to generate prompts; increase for longer reports.
- If you don't set `OPENAI_API_KEY` the app uses a rule-based fallback so you can demo without API access.
