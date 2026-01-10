"""Simple demo showing how to call the insight generator locally."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
import os
from src.ingest import load_csv
from src.insights import generate_insights

load_dotenv()

if __name__ == "__main__":
    sample = "sample_data/sample_reports.csv"
    df = load_csv(sample)
    print("Sample rows:")
    print(df.head().to_string())
    # assume column 'report_text'
    col = 'report_text' if 'report_text' in df.columns else df.columns[1]
    text = df.iloc[0][col]
    print('\n=== Generating Insights ===')
    out = generate_insights(text, top_n=5)
    print(out)
