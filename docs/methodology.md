# Methodology Note

I started by reviewing the MoveInSync FDE case brief and the supplied/public app-store review material. The review dataset contained 117 review blocks; 7 were developer responses, so the analysis focused on 110 user reviews.

Each user review was classified using:

- Sentiment: Positive, Mixed or Negative
- Severity: Critical, High, Medium or Low
- Primary issue
- Secondary issue, where applicable
- User impact
- Helpful votes

I then examined issue frequency, primary-issue distribution, sentiment/severity patterns and review-year trends. The recurring complaints were mapped onto the employee commute journey: login → booking/scheduling → assignment → tracking → pickup → ride → check-in/check-out → feedback.

The recommendation prioritizes the failure points most likely to disrupt the core commute journey. The FDE solution is intentionally framed as an investigation and reliability approach rather than assuming access to MoveInSync's internal architecture.

## Tools actually used

- **Google Play:** public app-store listing and recent review signals
- **Excel / spreadsheets:** data cleaning, classification and quantitative analysis
- **ChatGPT:** analysis support, synthesis and recommendation structuring
- **Claude:** independent analysis / synthesis cross-check
- **QuillBot:** final presentation design

## Honesty / limitations

No internal MoveInSync logs, telemetry, codebase or production database were available. Therefore, technical causes such as GPS freshness, booking-state divergence, API latency or ETA recalculation behavior are **root-cause hypotheses**, not confirmed findings. They should be validated through production telemetry and controlled reproduction.
