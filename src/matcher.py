import re
from typing import List, Dict


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().strip())


def evidence_overlap(span_a: str, span_b: str) -> float:
    a = normalize(span_a)
    b = normalize(span_b)

    if not a or not b:
        return 0.0

    overlap = sum(1 for ch in a if ch in b)
    return overlap / max(len(a), len(b))


def match_items(run_items: List[Dict], reference_items: List[Dict], threshold: float = 0.6):
    matches = []
    unmatched = []

    for item in run_items:
        best_match = None
        best_score = 0.0

        for ref in reference_items:
            if item["domain"] != ref["domain"]:
                continue

            score = evidence_overlap(item["evidence_span"], ref["evidence_span"])
            if score > best_score:
                best_score = score
                best_match = ref

        if best_score >= threshold:
            matches.append((item, best_match))
        else:
            unmatched.append(item)

    return matches, unmatched
