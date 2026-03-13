"""
prediction_agent.py
Simulates outbreak severity scoring and projected spread.
In a real system this would use an epidemiological model (e.g. SIR).
"""

import numpy as np


def run(df, anomalies, nlp_result):
    """Estimate severity and projected case growth from anomaly data."""

    has_anomaly     = len(anomalies) > 0
    high_nlp        = nlp_result["signal_level"] == "HIGH"

    # Severity scoring: start at 0, add weight for each signal
    score = 0
    if has_anomaly:
        # Weight by peak z-score
        peak_z = anomalies["z_score"].max()
        score += min(peak_z * 10, 50)       # cap anomaly contribution at 50

    if high_nlp:
        score += 30                          # NLP adds up to 30 points

    score = round(min(score, 100), 1)       # Clamp to 0–100

    # Simulate projected cases: simple linear extrapolation from recent trend
    recent_avg  = df["cases"].tail(7).mean()
    projected   = round(recent_avg * 1.25, 1)   # 25% growth estimate

    # Map score to severity label
    if score >= 70:
        severity = "HIGH"
    elif score >= 40:
        severity = "MODERATE"
    else:
        severity = "LOW"

    print(f"  [PredictionAgent] Severity score: {score}/100 → {severity} | "
          f"Projected next-day cases: ~{projected}")

    return {"severity": severity, "score": score, "projected_cases": projected}
