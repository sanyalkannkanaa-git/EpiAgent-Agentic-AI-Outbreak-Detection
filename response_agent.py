"""
response_agent.py
Generates tiered public health response recommendations
based on severity level from the prediction agent.
"""


ACTIONS = {
    "HIGH": [
        "Issue early warning alert to national health authorities",
        "Activate emergency public health response team",
        "Accelerate vaccine production and distribution",
        "Deploy mobile health units to affected regions",
        "Initiate contact tracing and containment measures",
        "Coordinate with international health organisations (WHO)",
    ],
    "MODERATE": [
        "Increase disease surveillance frequency",
        "Alert regional hospitals to prepare surge capacity",
        "Issue public health advisory notice",
        "Review and restock vaccine supply levels",
    ],
    "LOW": [
        "Continue routine monitoring",
        "Log data for baseline trend analysis",
        "No immediate action required",
    ],
}


def run(prediction):
    """Print recommended response actions for the predicted severity."""

    severity = prediction["severity"]
    score    = prediction["score"]
    proj     = prediction["projected_cases"]

    print(f"  [ResponseAgent]  Severity: {severity} (score {score}/100) | "
          f"Projected cases: ~{proj}")
    print()
    print("  Recommended actions:")
    for i, action in enumerate(ACTIONS[severity], 1):
        print(f"    {i}. {action}")

    return {"severity": severity, "actions": ACTIONS[severity]}
