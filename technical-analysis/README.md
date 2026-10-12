# Technical Analysis

This folder demonstrates how I would approach the case as an FDE rather than simply presenting a review summary.

## 1. Reproducible review analysis

`review_analysis.py` reads the coded review dataset and reproduces high-level metrics such as sentiment, severity, primary issues and year distribution.

Run:

```bash
python technical-analysis/review_analysis.py
```

Outputs are written to `outputs/`.

## 2. Transparent prioritization

`issue_prioritization.py` demonstrates an **illustrative** prioritization framework:

`Priority Score = Frequency × Average Severity Weight × Journey Impact Weight`

This is a proposed framework for the case study. It is **not** an internal MoveInSync formula and should not be presented as one.

Run:

```bash
python technical-analysis/issue_prioritization.py
```

## 3. Example FDE investigation

See [`eta_investigation.md`](./eta_investigation.md) for a technical investigation plan for inaccurate ETA/GPS complaints.

The purpose is to show what telemetry and evidence an FDE would request before assigning a root cause.
