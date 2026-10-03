# AI-Powered Business Insights Generator

> Turn reports and business data into concise, actionable insights with an interactive Streamlit dashboard.

[![CI](https://github.com/adisinn/AI-Powered-Business-Insights-Generator/actions/workflows/ci.yml/badge.svg)](https://github.com/adisinn/AI-Powered-Business-Insights-Generator/actions/workflows/ci.yml)

The **AI-Powered Business Insights Generator** is an end-to-end application for extracting meaningful business insights from reports and structured data. It combines lightweight text processing, configurable prompts, and an LLM-powered analysis workflow in a simple interface that is easy to run locally and demonstrate.

It is designed for experimentation, portfolio projects, interviews, and teams that want a starting point for turning raw business information into readable analysis.

## Highlights

- **Multiple input modes** — upload a CSV, query a SQL database, or paste report text directly.
- **LLM-powered analysis** — generate insights using Groq and the Llama 3.3 70B model.
- **Rule-based fallback** — run a local demo without an API key.
- **Configurable extraction** — control how many key sentences are selected with `top_n`.
- **Data-aware prompts** — include a summary of tabular data alongside report text.
- **Streamlit dashboard** — explore the workflow through a clean, interactive UI.
- **Reusable Python modules** — use the ingestion and insight-generation components independently.
- **Optional Power BI workflow** — connect generated insights to Power BI using the included guide.

## How it works

```text
CSV upload / SQL query / pasted report
                 │
                 ▼
          Data ingestion
                 │
                 ▼
   Key sentence and data extraction
                 │
                 ▼
      Prompt construction and LLM
                 │
                 ▼
       Business insight generation
                 │
                 ▼
        Results in the Streamlit app
```

The application extracts the most relevant sentences from a report, optionally combines them with a tabular data summary, and sends the resulting context to the configured insight-generation workflow. If no API key is available, the application uses a rule-based fallback so the project remains demoable offline.

## Screens and workflow

The Streamlit app provides three ways to supply data:

1. **CSV Upload** — upload a report CSV and preview the loaded data.
2. **SQL Query** — connect to a configured database and run a query against it.
3. **Paste Report** — enter report text manually for a quick analysis.

After selecting an input, adjust the number of key sentences and click **Generate Insights**.

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/adisinn/AI-Powered-Business-Insights-Generator.git
cd AI-Powered-Business-Insights-Generator
```

### 2. Create and activate a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example environment file:

```bash
cp .env.example .env
```

On Windows PowerShell, use:

```powershell
Copy-Item .env.example .env
```

Then edit `.env`:

```dotenv
# Optional: enables LLM-powered insights
GROQ_API_KEY=gsk_your_api_key_here

# Optional: enables the SQL Query tab
DATABASE_URL=postgresql://user:password@host:5432/database
```

> **Security:** Never commit `.env` or expose API keys in source code. The application can run without `GROQ_API_KEY` by using the rule-based fallback.

### 5. Launch the dashboard

```bash
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`.

## Run the command-line demo

To run the included demo against the sample report data:

```bash
python scripts/demo.py
```

This loads `sample_data/sample_reports.csv`, selects a report, and prints the generated insights in the terminal.

## Run tests

```bash
pytest
```

Continuous integration is configured in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) and runs the test suite for pushes and pull requests.

## Configuration

| Variable | Required | Purpose |
| --- | --- | --- |
| `GROQ_API_KEY` | No | Enables LLM-powered insight generation through Groq. |
| `DATABASE_URL` | No | Enables the SQL Query input mode. |

### Adjusting `top_n`

`top_n` controls how many key sentences are extracted from the report before the prompt is built:

- Use a lower value for short reports or faster prompts.
- Increase it for longer reports that require more context.
- Experiment with different values to compare concise and comprehensive analyses.

## Project structure

```text
.
├── app.py                       # Streamlit application
├── src/
│   ├── ingest.py                # CSV loading and SQL querying
│   ├── insights.py              # Insight-generation workflow
│   └── prompt_templates.py      # Reusable analysis prompts
├── scripts/
│   └── demo.py                  # Command-line demonstration
├── sample_data/
│   └── sample_reports.csv       # Example input data
├── tests/                       # Automated tests
├── .github/workflows/ci.yml     # GitHub Actions workflow
├── PROMPTS.md                   # Prompt ideas and analysis directions
├── PowerBI.md                   # Optional Power BI integration guide
├── slides.md                    # Project presentation deck
├── requirements.txt             # Python dependencies
└── .env.example                 # Environment variable template
```

## Example use cases

- Summarize quarterly or monthly business reports.
- Identify growth, retention, revenue, or operational trends.
- Turn analyst notes into executive-ready observations.
- Prototype an internal business intelligence assistant.
- Demonstrate an LLM-powered analytics workflow in an interview or portfolio.
- Generate a first-pass narrative to accompany a Power BI dashboard.

## Prompt customization

The project separates prompt configuration from the application logic. To experiment with different analysis styles, review:

- [`PROMPTS.md`](PROMPTS.md) for example prompt directions.
- [`src/prompt_templates.py`](src/prompt_templates.py) for reusable prompt templates.

You can adapt the prompts for themes such as:

- Growth and revenue performance
- Customer retention and churn
- Product or regional comparisons
- Risks, anomalies, and opportunities
- Executive summaries and recommended actions

## Power BI integration

See [`PowerBI.md`](PowerBI.md) for guidance on connecting generated insights to Power BI. The integration is optional; the Streamlit application works independently.

## Limitations

- Generated insights depend on the quality and completeness of the input data.
- LLM output should be reviewed before being used for business decisions.
- SQL queries are executed against the configured database, so use appropriate credentials and access controls.
- The current prototype focuses on a single selected report or result context rather than a full production analytics platform.

## Roadmap ideas

- Add structured insight output with categories, confidence, and supporting evidence.
- Support more file formats, including Excel and PDF reports.
- Add charts and trend visualizations to the Streamlit interface.
- Add authentication and role-based access for shared deployments.
- Add richer database schema discovery and query assistance.
- Add evaluation datasets for measuring insight quality.

## Contributing

Contributions and improvements are welcome. A typical workflow is:

1. Create a feature branch.
2. Make a focused change.
3. Add or update tests where appropriate.
4. Run `pytest` locally.
5. Open a pull request with a clear description of the change.

## License

No license has been specified yet. Until a license is added, all rights are reserved by the repository owner.

## Acknowledgements

Built with:

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Groq](https://groq.com/)
- [pytest](https://pytest.org/)
