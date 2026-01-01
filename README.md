# Ashwam ML/AI Internship — Exercise B  
## Run-to-Run Variance & Stability Analysis

### What did you build?
I built a deterministic stability analysis framework to measure run-to-run variance in LLM-generated structured outputs without relying on canonical labels. The system evaluates whether multiple outputs generated from the same journal entry are safe and consistent by anchoring comparisons to evidence spans and enforcing stability on safety-critical fields such as polarity.

The framework distinguishes between acceptable lexical or heuristic drift and unsafe semantic instability, prioritizing restraint and auditability in a women’s health journaling context.

---

### Key assumptions you made
- Evidence spans extracted from the journal text are the primary anchor of truth.
- Lexical variation is acceptable; semantic polarity variation is not.
- Bucketed fields (intensity, arousal, time) are heuristic and may drift.
- Missing objects across runs represent recall variance rather than hallucination by default.

---

### System / pipeline breakdown
1. **Evidence-first matching**  
   Semantic objects are aligned across runs using deterministic character-level overlap on evidence spans, gated by domain.

2. **Field-level stability checks**  
   Polarity is treated as safety-critical and must not disagree across matched objects. Bucket drift is measured but tolerated.

3. **Metric computation**  
   Agreement rate, polarity flip rate, and bucket drift rate are computed to quantify stability.

4. **Risk classification**  
   Any polarity flip results in an unsafe classification and abstention from reconciliation.

---

### Determinism & safety controls
- Fully deterministic matching rules (no stochastic similarity methods).
- No majority voting on safety-critical fields.
- Abstention when polarity disagreement is detected.
- Explicit unsafe classification rather than forced reconciliation.

---

### Evaluation or monitoring strategy
- **Agreement rate** to measure consistency of extraction.
- **Polarity flip rate** as a blocking safety metric.
- **Bucket drift rate** to monitor heuristic instability over time.

---

### Edge cases / known limitations
- Partial evidence span overlap may fail matching in rare cases.
- No semantic embedding fallback is implemented.
- Missing objects are treated conservatively as recall variance.
- System prioritizes safety over recall.

---

### What would you improve or extend with more time?
- Deterministic, span-aware semantic similarity as a fallback.
- CI-based stability regression tests.
- Longitudinal monitoring dashboards for production deployments.
- Explicit uncertainty propagation to downstream nudges.
