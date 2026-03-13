"""
data_agent.py
Responsible for loading and preprocessing the health dataset.
"""

import pandas as pd


def run(filepath="health_data.csv"):
    """Load CSV, clean data, and return a tidy DataFrame."""

    # Load the CSV with date parsing
    df = pd.read_csv(filepath, parse_dates=["date"])

    # Drop any rows with missing values
    df = df.dropna()

    # Sort chronologically and reset index
    df = df.sort_values("date").reset_index(drop=True)

    # Ensure case counts are integers
    df["cases"] = df["cases"].astype(int)

    print(f"  [DataAgent]      Loaded {len(df)} records "
          f"({df['date'].min().date()} → {df['date'].max().date()})")

    return df
