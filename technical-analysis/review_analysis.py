"""Reproduce high-level review metrics from the coded review dataset.

Usage:
    python technical-analysis/review_analysis.py

Outputs are written to outputs/.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reviews_110.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def pct(n, d):
    return round((n / d) * 100, 1) if d else 0.0


def main():
    df = pd.read_csv(DATA)
    total = len(df)

    sentiment = df["Sentiment"].value_counts().rename_axis("Sentiment").reset_index(name="Count")
    sentiment["Percent"] = sentiment["Count"].apply(lambda x: pct(x, total))

    severity_order = ["Critical", "High", "Medium", "Low"]
    severity = df["Severity"].value_counts().reindex(severity_order, fill_value=0).rename_axis("Severity").reset_index(name="Count")
    severity["Percent"] = severity["Count"].apply(lambda x: pct(x, total))

    primary = df["Primary Issue"].value_counts().rename_axis("Primary Issue").reset_index(name="Count")
    primary["Percent"] = primary["Count"].apply(lambda x: pct(x, total))

    year = pd.to_datetime(df["Date"], errors="coerce").dt.year.value_counts().sort_index().rename_axis("Year").reset_index(name="Reviews")

    metrics = pd.DataFrame([
        ["User reviews analyzed", total],
        ["Negative reviews", int((df["Sentiment"] == "Negative").sum())],
        ["Negative %", pct((df["Sentiment"] == "Negative").sum(), total)],
        ["High + Critical", int(df["Severity"].isin(["High", "Critical"]).sum())],
        ["High + Critical %", pct(df["Severity"].isin(["High", "Critical"]).sum(), total)],
        ["Helpful votes", int(df["Helpful Votes"].fillna(0).sum())],
    ], columns=["Metric", "Value"])

    sentiment.to_csv(OUT / "sentiment_summary.csv", index=False)
    severity.to_csv(OUT / "severity_summary.csv", index=False)
    primary.to_csv(OUT / "primary_issue_summary.csv", index=False)
    year.to_csv(OUT / "year_summary.csv", index=False)
    metrics.to_csv(OUT / "metrics.csv", index=False)

    print("MoveInSync FDE review analysis")
    print(metrics.to_string(index=False))
    print("\nTop primary issues:")
    print(primary.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
