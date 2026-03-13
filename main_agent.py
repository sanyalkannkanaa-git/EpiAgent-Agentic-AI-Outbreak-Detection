"""
main_agent.py
EpiAgent — Manager / Orchestrator Agent

Coordinates the full outbreak detection pipeline by calling
each specialist agent in sequence and passing results between them.
"""

import data_agent
import nlp_agent
import detection_agent
import prediction_agent
import response_agent

DIVIDER = "─" * 52


def run_pipeline(filepath="health_data.csv"):

    print("\n" + "=" * 52)
    print("  EpiAgent: Autonomous Outbreak Detection System")
    print("  Agentic AI Pipeline — Manager Orchestrator")
    print("=" * 52)

    # ── Stage 1: Data Ingestion ───────────────────────
    print(f"\n{DIVIDER}")
    print("  STAGE 1 — Data Ingestion")
    print(DIVIDER)
    df = data_agent.run(filepath)

    # ── Stage 2: NLP Signal Extraction ───────────────
    print(f"\n{DIVIDER}")
    print("  STAGE 2 — NLP Signal Extraction")
    print(DIVIDER)
    nlp_result = nlp_agent.run(df)
    print("  Signals detected:")
    for s in nlp_result["signals"]:
        print(f"    • {s}")

    # ── Stage 3: ML Anomaly Detection ────────────────
    print(f"\n{DIVIDER}")
    print("  STAGE 3 — ML Anomaly Detection")
    print(DIVIDER)
    df, anomalies = detection_agent.run(df)

    # ── Stage 4: Severity Prediction ─────────────────
    print(f"\n{DIVIDER}")
    print("  STAGE 4 — Outbreak Severity Prediction")
    print(DIVIDER)
    prediction = prediction_agent.run(df, anomalies, nlp_result)

    # ── Stage 5: Response Recommendation ─────────────
    print(f"\n{DIVIDER}")
    print("  STAGE 5 — Response Recommendation")
    print(DIVIDER)
    response_agent.run(prediction)

    # ── Pipeline summary ──────────────────────────────
    print(f"\n{'=' * 52}")
    print(f"  Pipeline complete.  "
          f"Verdict: {prediction['severity']} severity outbreak.")
    print("=" * 52 + "\n")


if __name__ == "__main__":
    run_pipeline("health_data.csv")
