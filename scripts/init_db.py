"""Initialize SQLite database with sample business data."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import sqlite3
import pandas as pd

# Create database
conn = sqlite3.connect("analytics.db")
cursor = conn.cursor()

# Create reports table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY,
        date TEXT,
        report_text TEXT,
        category TEXT
    )
""")

# Sample data
sample_data = [
    (
        "2024-01-15",
        "Sales grew 8% this quarter driven by an increase in online channels. Customer churn decreased slightly. Inventory turnover slowed due to supply delays. Marketing ROI improved for email campaigns, but CPC rose for social ads.",
        "Monthly"
    ),
    (
        "2024-01-20",
        "Customer satisfaction dipped in April following product delays. Refund requests increased slightly. Repeat purchase rate stable. New product launch shows promising initial uptake.",
        "Weekly"
    ),
    (
        "2024-02-01",
        "Q1 revenue exceeded targets by 12%. Customer acquisition cost decreased 15% through organic growth. Team productivity improved with new tools. Need to address inventory management issues.",
        "Quarterly"
    ),
]

# Insert sample data
cursor.executemany(
    "INSERT INTO reports (date, report_text, category) VALUES (?, ?, ?)",
    sample_data
)

# Create metrics table (optional)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY,
        date TEXT,
        metric_name TEXT,
        value REAL
    )
""")

metrics_data = [
    ("2024-01-15", "churn_rate", 3.2),
    ("2024-01-15", "revenue", 125000),
    ("2024-01-15", "cac", 45.50),
    ("2024-01-20", "nps", 72),
    ("2024-02-01", "revenue", 140000),
    ("2024-02-01", "cac", 38.75),
]

cursor.executemany(
    "INSERT INTO metrics (date, metric_name, value) VALUES (?, ?, ?)",
    metrics_data
)

conn.commit()
conn.close()

print("✅ SQLite database 'analytics.db' initialized with sample data!")
print("\nSample tables created:")
print("  - reports (id, date, report_text, category)")
print("  - metrics (id, date, metric_name, value)")
print("\nYou can now use SQL queries in the Streamlit app!")
