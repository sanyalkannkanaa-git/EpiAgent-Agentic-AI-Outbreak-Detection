"""
EpiAgent: Autonomous AI System for Disease Outbreak Detection
Agentic workflow simulation — 5-stage pipeline.
"""

import pandas as pd
import numpy as np
import random

SEPARATOR = "=" * 52

# ─────────────────────────────────────────────────────
# STAGE 1: Data Ingestion
# Load CSV and return a clean DataFrame.
# ─────────────────────────────────────────────────────
def ingest_data(filepath):
    print(f"\n{SEPARATOR}")
    print("  STAGE 1 — Data Ingestion")
    print(SEPARATOR)

    df = pd.read_csv(filepath, parse_dates=["date"])
    df = df.dropna().sort_values("date").reset_index(drop=True)
    df["cases"] = df["cases"].astype(int)

    print(f"  Sources  : health_data.csv")
    print(f"  Records  : {len(df)} days")
    print(f"  Range    : {df['date'].min().date()} → {df['date'].max().date()}")
    print(f"  Status   : ✓ Data loaded successfully")
    return df


# ─────────────────────────────────────────────────────
# STAGE 2: NLP Signal Extraction (mock simulation)
# In a real system this would parse news articles,
# hospital reports, and social media text. Here we
# simulate signal keywords the NLP engine might find.
# ─────────────────────────────────────────────────────
def nlp_signal_extraction(df):
    print(f"\n{SEPARATOR}")
    print("  STAGE 2 — NLP Signal Extraction")
    print(SEPARATOR)

    # Simulated signals a real NLP model might extract
    all_signals = [
        "unusual fever clusters reported",
        "hospital admissions rising",
        "emergency room visits increased",
        "community health alerts issued",
        "pharmacies reporting high demand",
    ]
    neutral_signals = [
        "routine seasonal flu activity",
        "no significant health events",
        "normal hospital occupancy levels",
    ]

    # Simulate higher alert signals if recent cases are elevated
    recent_avg = df["cases"].tail(7).mean()
    baseline_avg = df["cases"].head(14).mean()

    if recent_avg > baseline_avg * 1.5:
        detected = random.sample(all_signals, k=3)
        signal_level = "HIGH"
    else:
        detected = random.sample(neutral_signals, k=2)
        signal_level = "LOW"

    print(f"  Signal level : {signal_level}")
    print(f"  Signals found:")
    for s in detected:
        print(f"    • {s}")

    return {"signals": detected, "signal_level": signal_level}


# ─────────────────────────────────────────────────────
# STAGE 3: ML Anomaly Detection
# Z-score method — flags days where case count
# deviates significantly from the historical mean.
# ─────────────────────────────────────────────────────
def ml_anomaly_detection(df, threshold=2.5):
    print(f"\n{SEPARATOR}")
    print("  STAGE 3 — ML Anomaly Detection")
    print(SEPARATOR)

    mean = df["cases"].mean()
    std  = df["cases"].std()

    df["z_score"] = (df["cases"] - mean) / std
    df["anomaly"] = df["z_score"].abs() > threshold

    anomalies = df[df["anomaly"]]

    print(f"  Method    : Z-score (threshold = {threshold})")
    print(f"  Baseline  : mean={mean:.1f}, std={std:.1f}")
    print(f"  Anomalies : {len(anomalies)} day(s) flagged")

    if not anomalies.empty:
        for _, row in anomalies.iterrows():
            print(
                f"    ↑ {row['date'].date()}  {row['cases']} cases  "
                f"(z={row['z_score']:.2f})"
            )

    return df, anomalies


# ─────────────────────────────────────────────────────
# STAGE 4: Outbreak Decision Logic
# Agent combines ML anomaly flags with NLP signals
# to make a final outbreak determination.
# ─────────────────────────────────────────────────────
def outbreak_decision(anomalies, nlp_result):
    print(f"\n{SEPARATOR}")
    print("  STAGE 4 — Outbreak Decision Logic")
    print(SEPARATOR)

    has_anomaly     = len(anomalies) > 0
    high_nlp_signal = nlp_result["signal_level"] == "HIGH"

    print(f"  ML anomaly flagged : {'Yes' if has_anomaly else 'No'}")
    print(f"  NLP signal level   : {nlp_result['signal_level']}")

    # Decision matrix
    if has_anomaly and high_nlp_signal:
        verdict = "OUTBREAK CONFIRMED"
        severity = "HIGH"
    elif has_anomaly or high_nlp_signal:
        verdict = "OUTBREAK SUSPECTED"
        severity = "MODERATE"
    else:
        verdict = "NO OUTBREAK"
        severity = "LOW"

    print(f"\n  ▶ Verdict  : {verdict}")
    print(f"  ▶ Severity : {severity}")

    return {"verdict": verdict, "severity": severity}


# ─────────────────────────────────────────────────────
# STAGE 5: Response Recommendation
# Agent recommends actions based on severity level.
# ─────────────────────────────────────────────────────
def response_recommendation(decision):
    print(f"\n{SEPARATOR}")
    print("  STAGE 5 — Response Recommendation")
    print(SEPARATOR)

    actions = {
        "HIGH": [
            "Activate emergency public health response team",
            "Issue early warning alert to health authorities",
            "Accelerate vaccine production and distribution",
            "Deploy mobile health units to affected regions",
            "Initiate contact tracing and containment measures",
        ],
        "MODERATE": [
            "Increase disease surveillance frequency",
            "Alert regional hospitals to prepare surge capacity",
            "Review vaccine stockpile levels",
            "Issue public health advisory notice",
        ],
        "LOW": [
            "Continue routine monitoring",
            "Log data for trend analysis",
            "No immediate action required",
        ],
    }

    severity  = decision["severity"]
    verdict   = decision["verdict"]
    rec_list  = actions[severity]

    print(f"  Outbreak status : {verdict}")
    print(f"  Recommended actions:\n")
    for i, action in enumerate(rec_list, 1):
        print(f"    {i}. {action}")

    print(f"\n{SEPARATOR}")
    print("  EpiAgent cycle complete.")
    print(SEPARATOR)


# ─────────────────────────────────────────────────────
# MAIN: Run the full EpiAgent agentic pipeline
# ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\n{'*' * 52}")
    print("  EpiAgent — Autonomous Outbreak Detection System")
    print(f"{'*' * 52}")

    df                  = ingest_data("health_data.csv")
    nlp_result          = nlp_signal_extraction(df)
    df, anomalies       = ml_anomaly_detection(df, threshold=2.5)
    decision            = outbreak_decision(anomalies, nlp_result)
    response_recommendation(decision)
