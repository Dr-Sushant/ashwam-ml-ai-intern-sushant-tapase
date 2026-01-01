from typing import List, Tuple, Dict


def agreement_rate(matched: int, total: int) -> float:
    return matched / total if total else 0.0


def polarity_flip_rate(matches: List[Tuple[Dict, Dict]]) -> float:
    flips = sum(
        1 for a, b in matches if a.get("polarity") != b.get("polarity")
    )
    return flips / len(matches) if matches else 0.0


def bucket_drift_rate(matches: List[Tuple[Dict, Dict]]) -> float:
    drift = 0
    tracked_fields = ["intensity_bucket", "arousal_bucket", "time_bucket"]

    for a, b in matches:
        for field in tracked_fields:
            if field in a and field in b and a[field] != b[field]:
                drift += 1
                break

    return drift / len(matches) if matches else 0.0
