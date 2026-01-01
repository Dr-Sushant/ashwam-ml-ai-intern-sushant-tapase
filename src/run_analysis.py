import json
from pathlib import Path
from matcher import match_items
from metrics import agreement_rate, polarity_flip_rate, bucket_drift_rate


DATA_DIR = Path("data/llm_runs")
OUTPUT_PATH = Path("outputs/stability_report.json")


def load_run(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["items"]


def analyze(journal_id: str):
    runs = [
        load_run(DATA_DIR / f"{journal_id}.run1.json"),
        load_run(DATA_DIR / f"{journal_id}.run2.json"),
        load_run(DATA_DIR / f"{journal_id}.run3.json"),
    ]

    ref = runs[0]
    all_matches = []
    total_items = sum(len(r) for r in runs)

    for run in runs[1:]:
        matches, _ = match_items(run, ref)
        all_matches.extend(matches)

    report = {
        "journal_id": journal_id,
        "agreement_rate": agreement_rate(len(all_matches), total_items),
        "polarity_flip_rate": polarity_flip_rate(all_matches),
        "bucket_drift_rate": bucket_drift_rate(all_matches),
        "status": "UNSAFE"
        if polarity_flip_rate(all_matches) > 0
        else "STABLE",
    }

    return report


def main():
    results = []
    for jid in ["B001", "B004"]:
        results.append(analyze(jid))

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
