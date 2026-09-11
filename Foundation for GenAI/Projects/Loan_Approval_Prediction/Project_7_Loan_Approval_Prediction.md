# Project 7 — Loan Approval Prediction

## PDF Scope

Project 7 requires a **classification model** to predict **loan approvals** from **applicant data**. The PDF gives Logistic Regression and Random Forest as example models and lists scikit-learn and Pandas as tools.

## 1. Problem

Predict whether a loan application is approved or rejected.

This is **binary classification** because there are two target classes:

- `1` → Approved
- `0` → Rejected

## 2. Dataset Inspection

The project loads `loan_approval.csv` with Pandas and inspects:

- First rows
- Shape
- Column names
- Data types
- Statistical summary
- Missing values
- Duplicate rows
- Loan approval distribution

## 3. Feature Engineering

The implementation creates:

```python
loans["Loan_to_Income"] = loans["Loan_Amount"] / loans["Income"]
```

Example:

```text
Income = 70,000
Loan Amount = 400,000
Loan_to_Income ≈ 5.71
```

**Implementation choice:** The PDF requires feature engineering but does not prescribe this exact feature.

## 4. Features and Target

Features:

```text
Income
Credit_Score
Loan_Amount
Employment_Years
Age
Existing_Loan
Loan_to_Income
```

Target:

```text
Loan_Approved
```

Conceptually:

```text
Applicant data → Classification model → Approved / Rejected
```

## 5. Train/Test Split

The dataset is split into:

- 80% training
- 20% testing

`random_state=42` makes the split reproducible.

`stratify=y` keeps the target distribution approximately consistent across the two sets.

## 6. Feature Scaling

`StandardScaler` is used for Logistic Regression.

The scaler is fitted only on training data:

```python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

The same fitted scaler is then used for a new applicant.

## 7. Logistic Regression

```python
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
```

Logistic Regression produces class predictions and probabilities.

The project uses:

```python
model.predict(...)
model.predict_proba(...)
```

## 8. Classification Metrics

The project evaluates Logistic Regression using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The PDF specifically requires Precision, Recall, F1-Score, and ROC-AUC.

### Precision

```text
Precision = TP / (TP + FP)
```

Meaning:

> When the model predicts the positive class, how often is it correct?

### Recall

```text
Recall = TP / (TP + FN)
```

Meaning:

> Of the actual positive cases, how many did the model find?

### F1 Score

```text
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

F1 balances precision and recall.

### ROC-AUC

ROC-AUC evaluates how well the model separates the two classes across different classification thresholds.

General intuition:

```text
Closer to 1 → better separation
Around 0.5 → little useful separation
```

## 9. Confusion Matrix

The project also displays:

```python
confusion_matrix(y_test, y_pred)
```

A binary confusion matrix contains:

```text
                 Predicted
                 0       1

Actual  0       TN      FP
        1       FN      TP
```

## 10. Threshold Experiment

The implementation tests a threshold of `0.60`:

```python
y_pred_threshold = (y_prob >= 0.60).astype(int)
```

This demonstrates that changing the probability threshold can change classification results.

**Implementation choice:** The PDF does not explicitly require a threshold experiment.

## 11. Random Forest

A second model is trained:

```python
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

It is trained using the original, unscaled features.

The same main metrics are calculated for comparison.

## 12. Model Comparison

The project compares:

```text
Metric       Logistic Regression    Random Forest
--------------------------------------------------
Accuracy
Precision
Recall
F1 Score
ROC-AUC
```

The final model should be judged using the evaluation results and the metric that matters for the application.

## 13. New Applicant

The implementation tests:

```text
Income            = 70,000
Credit Score      = 760
Loan Amount       = 400,000
Employment Years  = 7
Age               = 35
Existing Loan     = 0
```

The engineered Loan-to-Income value is:

```text
400,000 / 70,000 ≈ 5.71
```

Both models return:

- Predicted class
- Approval probability

## 14. Random Forest Feature Importance

The implementation displays:

```python
rf_model.feature_importances_
```

and sorts the features by importance.

**Implementation choice:** The PDF does not explicitly require feature importance; it is included as a practical inspection of the Random Forest.

## 15. Complete Workflow

```text
Load Dataset
    ↓
Inspect Dataset
    ↓
Check Data Quality
    ↓
Feature Engineering
    ↓
Select Features + Target
    ↓
Train/Test Split
    ↓
Feature Scaling
    ↓
Train Logistic Regression
    ↓
Predict + Evaluate
    ↓
ROC-AUC + Threshold Experiment
    ↓
Train Random Forest
    ↓
Evaluate + Compare
    ↓
Predict New Applicant
    ↓
Inspect Feature Importance
```

## 16. Suggested Project Structure

```text
Project 7 - Loan Approval Prediction/
│
├── README.md
├── requirements.txt
├── loan_approval.csv
└── Project_7_Loan_Approval_Prediction.py
```

**Implementation choice:** The PDF does not prescribe a folder structure.

## 17. Key Takeaways

1. Loan approval prediction is a classification problem.
2. Applicant information forms the features.
3. `Loan_Approved` is the target.
4. Logistic Regression can produce class probabilities.
5. Random Forest can also perform classification and provide probabilities.
6. Precision measures the correctness of positive predictions.
7. Recall measures how many actual positive cases were found.
8. F1 balances precision and recall.
9. ROC-AUC evaluates class separation across thresholds.
10. A classification threshold can affect predictions.
11. Model comparison should use the same test data and consistent metrics.
12. Feature engineering can create useful information from existing applicant data.
