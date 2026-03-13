"""
nlp_agent.py
Simulates NLP extraction from health reports and news feeds.
In a real system this would use an LLM or NER pipeline.
"""

import random


# Signals a real NLP model might surface from text sources
ALERT_SIGNALS = [
    "hospital admissions rising sharply",
    "unusual fever clusters reported in region",
    "emergency rooms overwhelmed with patients",
    "pharmacies reporting abnormally high demand",
    "community health alerts issued by authorities",
]

NORMAL_SIGNALS = [
    "routine seasonal flu activity observed",
    "no significant health events reported",
    "normal hospital occupancy levels",
    "standard winter respiratory illness pattern",
]


def run(df):
    """Return mock NLP signals based on recent trend in case data."""

    # Compare last 7 days to the first 14-day baseline
    recent  = df["cases"].tail(7).mean()
    baseline = df["cases"].head(14).mean()

    # Elevated recent average → surface alert signals
    if recent > baseline * 1.5:
        signals = random.sample(ALERT_SIGNALS, k=3)
        level   = "HIGH"
    else:
        signals = random.sample(NORMAL_SIGNALS, k=2)
        level   = "LOW"

    print(f"  [NLPAgent]       Signal level: {level} | "
          f"Signals: {len(signals)} extracted")

    return {"signals": signals, "signal_level": level}
