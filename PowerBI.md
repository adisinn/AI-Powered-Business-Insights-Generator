# Power BI Integration Guide (notes)

This file explains simple ways to connect generated insights to Power BI for a conversational or tiles-based demo.

1) Export insights as CSV/JSON
- From the app, save generated insights to a CSV or JSON file with columns: `insight`, `explanation`, `metric`.
- Import the file into Power BI Desktop as a data source.

2) Create a card/visual
- Use a table or card visual to display the latest insights.
- Create measures for tracked metrics (e.g., `Churn Rate`, `Inventory Turnover`) using your dataset.

3) Embedding conversational insights
- Use Power BI's `Q&A` feature for natural-language questions over your dataset.
- For a more integrated experience, host the Streamlit app and embed it in Power BI using a web content tile (requires Power BI Service and allowed embed settings).

4) Automation ideas
- Schedule a script to run nightly to generate insights for the day's data, push CSV to OneDrive, and let Power BI refresh the dataset.

5) Security
- Do not store API keys in public datasets. Use Azure Key Vault or environment variables on your host when automating insight generation.

These notes are starting points — I can add a step-by-step example with exported files if you want a runnable demo.
