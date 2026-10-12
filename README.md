# MoveInSync FDE Case Study — Employee Commute Reliability

A customer-focused FDE case study analyzing public/app-store review signals and recommending what MoveInSync should fix first to improve the employee commute experience.

## Executive recommendation

> **Make the core commute journey reliable, observable and recoverable before expanding features.**

The analysis points to three priority areas:

1. **Booking / Scheduling** — reduce failed, ambiguous or inconsistent booking states.
2. **App Reliability / Login** — reduce crashes, bugs, authentication friction and startup failures.
3. **Tracking / ETA** — improve location freshness, ETA accuracy and pickup-time confidence.

After stabilizing these P0 areas, improve recovery, communication/support, UX and convenience features.

## What was analyzed

The supplied review dataset contains **117 review blocks**, including **7 developer responses**. The analysis focuses on the resulting **110 user reviews** after excluding developer replies.

### Key signals from the analyzed sample

| Metric | Result |
|---|---:|
| User reviews analyzed | 110 |
| Negative sentiment | 75 (68.2%) |
| Mixed sentiment | 9 (8.2%) |
| Positive sentiment | 26 (23.6%) |
| High + Critical severity | 61 (55.5%) |
| Explicit helpful votes | 137 |
| Most frequent issue category | Booking / Scheduling |

Issue-frequency counts can overlap because a review may contain both a primary and secondary issue.

## Core commute journey

`LOGIN → SCHEDULE / BOOK → ASSIGNMENT → TRACK → PICKUP → RIDE → CHECK-IN / CHECK-OUT → FEEDBACK`

The recommendation is to make failures in this loop **detectable, explainable and recoverable**.

## Proposed FDE investigation loop

```text
Customer complaint
       ↓
Reproduce the issue
       ↓
Collect telemetry / logs
       ↓
Isolate failure point
       ↓
Form root-cause hypothesis
       ↓
Fix / mitigate
       ↓
Monitor KPI
       ↓
Validate with customer outcome
```

Example: for an inaccurate ETA complaint, investigate GPS freshness, location-event timestamps, ETA calculation/recalculation, coordinates, network/API latency, app version and device context before concluding the root cause.

## Priority roadmap

### P0 — Stabilize the core journey
- App reliability and login
- Booking and scheduling consistency
- Tracking and ETA reliability

### P1 — Improve recovery and communication
- Location/routing quality
- Driver communication
- Support/recovery paths
- Feedback loop

### P2/P3 — Optimize the experience
- UX refinements
- Notifications
- Convenience features

## Proposed KPIs

- Booking Success Rate
- Booking State Mismatch Rate
- ETA Absolute Error / P90
- Stale Location Rate
- Crash-Free Sessions
- Login / OTP Success Rate
- System-Attributed Missed Pickup Rate
- Support Resolution Time
- Successful Commute Rate

These are **proposed measurement metrics**, not internal MoveInSync metrics.

## 90-day execution plan

| Period | Focus |
|---|---|
| Days 0–30 | Baseline telemetry, reproduce top failures, stabilize P0 issues |
| Days 31–60 | Add recovery paths, improve tracking/ETA and support workflows |
| Days 61–90 | Optimize UX, notifications and convenience after core reliability improves |

## Repository structure

```text
moveinsync-fde-case-study/
├── README.md
├── data/
│   └── reviews_110.csv
├── analysis/
│   ├── issue_frequency.csv
│   ├── primary_issue_analysis.csv
│   ├── year_trend.csv
│   ├── master_review_analysis.xlsx
│   └── quantitative_analysis.xlsx
├── report/
│   └── MoveInSync_FDE_Recommendation.pdf
├── docs/
│   ├── Case_Study_Brief.pdf
│   └── methodology.md
└── scripts/
    └── summarize_reviews.py
```

## Methodology and tools

The review data was organized and classified by sentiment, severity, primary issue, secondary issue, user impact and helpful votes. Recurring themes were then grouped around the employee commute journey and prioritized by likely impact on successful commuting.

**Tools actually used:**
- Google Play — public app-store evidence
- Excel / spreadsheets — data organization and quantitative analysis
- ChatGPT — review analysis, synthesis and recommendation structuring
- Claude — independent analysis / synthesis cross-check
- Slidesgo — presentation creation

AI tools supported analysis and synthesis; they were not treated as a substitute for production telemetry or internal engineering evidence.

## Important limitations

- App-store reviews are self-selected and are not representative of every MoveInSync user.
- The review sample should be treated as evidence of customer-reported symptoms, not proof of internal root causes.
- Technical root causes in the recommendation are hypotheses that should be validated with production logs, telemetry and stakeholder interviews.
- Public store ratings and review counts can change over time.

## Source note

The case brief and review dataset supplied for the assignment are included for reproducibility of this submission. Public app-store observations should be rechecked against the live listing if this repository is reviewed later.

## Technical / FDE evidence

This repository intentionally does **not** pretend to reproduce MoveInSync's internal production systems. Instead, it demonstrates a reproducible analysis workflow and a technically testable FDE investigation approach.

### Reproducible analysis

```bash
pip install -r requirements.txt
python technical-analysis/review_analysis.py
python technical-analysis/issue_prioritization.py
```

The scripts use the coded review dataset and generate summary CSVs under `outputs/`.

### Example technical investigation

See [`technical-analysis/eta_investigation.md`](technical-analysis/eta_investigation.md) for an FDE investigation plan for inaccurate ETA/GPS complaints, including the evidence/telemetry that should be requested before claiming a root cause.

## Submission map

- **Recommendation:** `report/MoveInSync_FDE_Recommendation.pdf`
- **Evidence / quantitative analysis:** `analysis/`
- **Coded review dataset:** `data/reviews_110.csv`
- **Technical/FDE reasoning:** `technical-analysis/`
- **Methodology:** `docs/methodology.md`
- **Case brief:** `docs/Case_Study_Brief.pdf`

## Important limitations

- App-store reviews are self-selected and are not representative of every MoveInSync user.
- Issue-frequency views may overlap because a review can have both a primary and secondary issue.
- Public reviews reveal customer symptoms, not internal architecture or confirmed root causes.
- Technical root causes and KPI targets in this case study are hypotheses/proposals that should be validated using production telemetry and stakeholder interviews.
