"""Transparent, illustrative issue-prioritization framework.

This is a proposed FDE prioritization model, NOT an internal MoveInSync scoring system.
It uses the coded review dataset and simple weights to make prioritization reproducible.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reviews_110.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

SEVERITY_WEIGHT = {"Critical": 4, "High": 3, "Medium": 2, "Low": 1}
JOURNEY_IMPACT = {
    "Booking/Scheduling": 4,
    "App Reliability": 4,
    "Tracking/ETA": 4,
    "Login/Authentication": 4,
    "Location/Routing": 4,
    "Timing/ETA": 3,
    "Assignment/Operations": 3,
    "Driver Communication": 3,
    "Communication/Support": 3,
    "UX/Navigation": 2,
    "Usability": 2,
    "Notifications": 2,
    "Performance": 2,
    "Feedback/Rating": 1,
    "Installation": 1,
    "Positive Experience": 1,
}


def main():
    df = pd.read_csv(DATA)
    rows = []

    for issue, group in df.groupby("Primary Issue"):
        frequency = len(group)
        avg_severity = group["Severity"].map(SEVERITY_WEIGHT).mean()
        journey_impact = JOURNEY_IMPACT.get(issue, 2)
        score = frequency * avg_severity * journey_impact
        rows.append([issue, frequency, round(avg_severity, 2), journey_impact, round(score, 2)])

    result = pd.DataFrame(rows, columns=[
        "Issue", "Frequency", "Average Severity Weight", "Journey Impact Weight", "Illustrative Priority Score"
    ]).sort_values("Illustrative Priority Score", ascending=False)

    result["Suggested Priority"] = "P2"
    result.loc[result["Illustrative Priority Score"] >= result["Illustrative Priority Score"].quantile(0.75), "Suggested Priority"] = "P1"
    result.loc[result["Issue"].isin(["Booking/Scheduling", "App Reliability", "Tracking/ETA"]), "Suggested Priority"] = "P0"

    result.to_csv(OUT / "illustrative_issue_prioritization.csv", index=False)
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
