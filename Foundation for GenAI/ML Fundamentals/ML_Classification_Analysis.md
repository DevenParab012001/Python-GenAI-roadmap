# ML Classification Analysis

## Classification
Classification predicts a **class/category**.

Example:
```text
Class 0 → No Default
Class 1 → Default
```

## Binary Classification
Binary classification has exactly two possible classes.

Examples:
- Default / No Default
- Approved / Rejected
- Fraud / Normal

## Logistic Regression for Binary Classification
Despite its name, Logistic Regression is used for classification.

```text
Input Features → Logistic Regression → Probability → Class
```

With threshold `0.5`:
```text
Probability ≥ 0.5 → Class 1
Probability < 0.5 → Class 0
```

The threshold can change. For example:
```text
Probability = 0.72
Threshold = 0.50 → Class 1
Threshold = 0.80 → Class 0
```

A higher threshold makes it harder to predict Class 1.

## Class Imbalance
Class imbalance occurs when one class has many more examples than another.

Example:
```text
Normal transactions → 9,500
Fraud transactions  →   500
```

A model can have high overall accuracy while detecting few minority cases.

## Sampling Techniques

### Undersampling
Reduce the majority class.

```text
Before:
Class 0 → 9,000
Class 1 → 1,000

After:
Class 0 → 1,000
Class 1 → 1,000
```

**Main disadvantage:** useful majority-class information may be lost.

### Oversampling
Increase the minority class.

```text
Before:
Class 0 → 9,000
Class 1 → 1,000

After:
Class 0 → 9,000
Class 1 → 9,000
```

**Main disadvantage:** repeated minority examples can contribute to overfitting.

Sampling techniques are applied to training data.

## Precision
Answers: **Of all cases predicted as positive, how many were actually positive?**

```text
Precision = TP / (TP + FP)
```

- **TP:** predicted positive and actually positive.
- **FP:** predicted positive but actually negative.

Memory:
`Precision → "When I say YES, how often am I right?"`

Example:
```text
20 predicted fraud
15 actually fraud
5 actually normal

Precision = 15 / (15 + 5)
          = 0.75
          = 75%
```

## Recall
Answers: **Of all actual positive cases, how many did the model successfully find?**

```text
Recall = TP / (TP + FN)
```

- **FN:** actually positive but predicted negative.

Memory:
`Recall → "Did I find the YES cases?"`

Example:
```text
20 actual fraud
15 correctly identified

Recall = 15 / (15 + 5)
       = 0.75
       = 75%
```

## Precision vs Recall
| Metric | Question |
|---|---|
| Precision | Of predicted positives, how many were actually positive? |
| Recall | Of actual positives, how many did we find? |

Example:
```text
Actual fraud = 100
Predicted fraud = 80
60 are actually fraud
20 are actually normal

TP = 60
FN = 40
FP = 20

Precision = 60 / (60 + 20) = 75%
Recall    = 60 / (60 + 40) = 60%
```

## F1-Score
Combines Precision and Recall into a single metric.

```text
F1 = 2 × (Precision × Recall)
         ─────────────────────
          Precision + Recall
```

Example:
```text
Precision = 0.75
Recall = 0.60

F1 = 2 × (0.75 × 0.60) / (0.75 + 0.60)
   ≈ 0.67
```

F1 balances Precision and Recall; a low value for either can pull the F1-Score down.

## ROC-AUC
ROC-AUC evaluates how well a classification model separates the two classes across different classification thresholds.

`AUC = Area Under the ROC Curve`

General interpretation:
```text
AUC closer to 1 → Better class separation
AUC around 0.5 → Little/no useful separation
```

Example:
```text
Model A → ROC-AUC = 0.91
Model B → ROC-AUC = 0.63
```

Model A has stronger class-separation ability.

## Quick Revision
```text
Classification = Predict a class/category
Binary Classification = Two classes

Logistic Regression → Probability → Threshold → Class
Higher threshold → Fewer Class 1 predictions

Class imbalance = Unequal class distribution
Undersampling → Reduce majority class
Oversampling → Increase minority class

Precision → Reliability of positive predictions
Recall → Actual positives successfully found
F1-Score → Balance between Precision and Recall
ROC-AUC → Class-separation ability across thresholds
```
