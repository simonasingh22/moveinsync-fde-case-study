# Example FDE Investigation: Incorrect ETA / GPS Tracking

## Customer symptom

An employee reports that the vehicle's GPS position or ETA is inaccurate, delayed or keeps changing.

## Do not jump directly to the root cause

The review tells us **what the customer experienced**, not which internal component failed. The first FDE task is to separate the possible failure points.

```text
Driver / vehicle GPS
        ↓
Location event ingestion
        ↓
Location processing / validation
        ↓
ETA calculation / route engine
        ↓
Backend API
        ↓
Mobile app
        ↓
Employee sees ETA
```

## Evidence to request

| Evidence | Why it matters |
|---|---|
| GPS event timestamp | Checks location freshness |
| Device timestamp | Detects device/clock mismatch |
| Latitude / longitude history | Checks movement and location quality |
| ETA calculation timestamp | Measures backend calculation delay |
| ETA returned by API | Separates backend from UI issues |
| Route / pickup coordinates | Checks routing and pickup-point mismatch |
| API latency / error logs | Identifies transport/backend delay |
| Network state | Separates connectivity problems |
| App version + OS + device | Finds version/device-specific patterns |
| Vehicle/driver identifier | Checks whether incidents cluster by source |

## Investigation sequence

1. Reproduce the complaint with a known trip if possible.
2. Compare the timestamp of the latest GPS event with the time shown in the app.
3. Check whether the backend received and processed the location promptly.
4. Compare the backend ETA with the ETA rendered by the mobile app.
5. Check route and pickup coordinates for mismatches.
6. Segment incidents by app version, device, network and vehicle/driver.
7. Form the smallest testable root-cause hypothesis.
8. Apply a fix or mitigation and monitor the relevant KPI.

## Example hypotheses

- **H1:** GPS/location events are stale before ETA calculation.
- **H2:** Location events are received promptly but ETA recalculation is delayed.
- **H3:** Backend ETA is correct but the mobile client displays stale data.
- **H4:** Pickup coordinates or route data do not match the employee's selected location.
- **H5:** A subset of app versions/devices has a client-side tracking problem.

These are **hypotheses only**. The public review data cannot confirm any of them.

## Useful KPIs

- ETA absolute error
- ETA p90 error
- stale-location rate
- location-to-ETA processing latency
- tracking API error rate
- system-attributed missed pickup rate

The goal is not merely to make the screen look more accurate. The goal is to make the employee's commute outcome more reliable.
