"""
detection_agent.py
Detects anomalous spikes in daily case counts using z-score analysis.
Days with |z| > threshold are flagged as potential outbreak signals.
"""

import numpy as np


THRESHOLD = 2.5   # Standard deviations above mean to trigger a flag


def run(df):
    """Compute z-scores and return flagged anomaly rows."""

    mean = df["cases"].mean()
    std  = df["cases"].std()

    # Z-score: how many std deviations each day is from the mean
    df["z_score"] = (df["cases"] - mean) / std
    df["anomaly"] = df["z_score"].abs() > THRESHOLD

    anomalies = df[df["anomaly"]][["date", "cases", "z_score"]]

    print(f"  [DetectionAgent] Baseline mean={mean:.1f}, std={std:.1f} | "
          f"Anomalies found: {len(anomalies)}")

    for _, row in anomalies.iterrows():
        print(f"                   ↑ {row['date'].date()}  "
              f"{row['cases']} cases  (z={row['z_score']:.2f})")

    return df, anomalies
