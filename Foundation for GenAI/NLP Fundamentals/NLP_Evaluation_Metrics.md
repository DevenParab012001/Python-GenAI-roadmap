# NLP Evaluation Metrics

## 1. Introduction

NLP Evaluation Metrics are used to measure the quality or performance of an NLP system.

The basic idea is:

```text
NLP Model / System
        ↓
      Output
        ↓
Evaluation Metric
        ↓
Performance Measurement
```

---

## 2. Purpose of Evaluation Metrics

An NLP system produces an output.

Evaluation metrics provide a way to assess how well the system performed.

Conceptually:

```text
Model Output
     ↓
Evaluation
     ↓
Quality / Performance Measurement
```

This allows us to evaluate the performance of an NLP system rather than relying only on the generated output.

---

## 3. Evaluation in an NLP Pipeline

A simple NLP workflow can be represented as:

```text
Input Text
    ↓
NLP Model / System
    ↓
Output
    ↓
Evaluation Metrics
    ↓
Measure Performance
```

The evaluation stage comes after the system produces its output.

---

## 4. Simple Example

Suppose an NLP system produces an output for a task.

We can compare or evaluate that output using an appropriate evaluation metric.

```text
Expected / Reference Output
          +
       Model Output
          ↓
      Evaluation
          ↓
    Performance Measure
```

The specific metric depends on the NLP task and the type of output being evaluated.

---

## 5. Important Note

The SDE Master Program PDF lists **NLP Evaluation Metrics** as a topic, but it does not specify individual metrics, formulas, or detailed evaluation procedures.

Therefore, this note intentionally stays at the general concept of evaluating NLP system performance and does not introduce additional metrics as required roadmap topics.

---

## 6. Summary

- NLP Evaluation Metrics are used to measure the performance or quality of NLP systems.
- An NLP system produces an output that can then be evaluated.
- Evaluation provides a way to measure system performance.
- The appropriate metric depends on the NLP task and its output.
