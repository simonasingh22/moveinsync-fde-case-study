"""Small reproducible summary for the MoveInSync FDE review dataset.

Run from the repository root:
    python scripts/summarize_reviews.py
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reviews_110.csv"

df = pd.read_csv(DATA)

print("MoveInSync FDE Review Summary")
print("=" * 32)
print(f"User reviews: {len(df)}")
print(f"Helpful votes: {df['Helpful Votes'].fillna(0).sum():.0f}")
print("\nSentiment")
print(df["Sentiment"].value_counts().to_string())
print("\nSeverity")
print(df["Severity"].value_counts().to_string())
print("\nPrimary issues")
print(df["Primary Issue"].value_counts().head(15).to_string())
print("\nYear")
years = pd.to_datetime(df["Date"], errors="coerce").dt.year
print(years.value_counts().sort_index().to_string())
