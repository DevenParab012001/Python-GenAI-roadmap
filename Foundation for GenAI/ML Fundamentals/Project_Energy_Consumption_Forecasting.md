# Project 6 — Energy Consumption Forecasting

## 1. Project Overview

This project applies regression concepts to household energy consumption.

### PDF Roadmap Scope

The SDE Master Program specifies:

- Predict household energy consumption using **linear regression**
- Analyze:
  - Temperature
  - Appliances
  - Daily usage patterns
- Perform **feature engineering**
- Evaluate the model using:
  - RMSE
  - R² score

These are the requirements from the roadmap. Exact dataset, column names, train/test ratio, and implementation details are not specified by the PDF.

---

## 2. Problem Statement

Build a machine learning model that predicts the amount of energy a household consumes.

### Inputs

Examples of inputs include:

- Temperature
- Number of appliances used
- Daily usage

Feature engineering can create additional useful representations of these inputs.

### Output

The target is:

```text
Energy Consumption
```

Because energy consumption is numeric, this is a **regression problem**.

---

## 3. Machine Learning Formulation

```text
Features
    |
    +-- Temperature
    +-- Appliances Used
    +-- Daily Usage
    +-- Engineered Features
    |
    v
Linear Regression
    |
    v
Predicted Energy Consumption
```

### Features

Features are the input values used by the model.

Example:

```text
Temperature = 30
Appliances Used = 5
Daily Usage = 7
```

### Target

The target is the value the model learns to predict:

```text
Energy Consumption
```

Example:

```text
Energy Consumption = 21 kWh
```

---

# 4. Feature Engineering

Feature engineering means creating or transforming features so useful patterns can be represented to the model.

Feature engineering is explicitly required by the roadmap for this project.

## 4.1 Interaction Feature

One implementation choice is:

```text
Usage × Appliances
```

Example:

```text
Appliances Used = 5
Daily Usage = 8

Usage × Appliances
= 5 × 8
= 40
```

This represents the combined relationship between appliance count and usage duration.

> The exact interaction feature above is an **implementation choice**. The PDF requires feature engineering but does not prescribe this exact formula.

## 4.2 Weekend Usage Pattern

Another implementation choice is:

```text
Is_Weekend
```

Encoding:

```text
Weekday → 0
Weekend → 1
```

Example:

```text
Sunday
→ Weekend
→ Is_Weekend = 1
```

This can represent a difference between weekday and weekend usage patterns.

> The PDF requires analysis of daily usage patterns but does not prescribe an `Is_Weekend` column or this exact encoding. It is an **implementation choice**.

---

# 5. Example Dataset

A conceptual dataset could look like this:

| Temperature | Appliances Used | Daily Usage | Is_Weekend | Usage × Appliances | Energy Consumption |
|---:|---:|---:|---:|---:|---:|
| 25 | 3 | 5 | 0 | 15 | 12 |
| 30 | 5 | 7 | 0 | 35 | 20 |
| 22 | 2 | 4 | 1 | 8 | 9 |
| 35 | 6 | 8 | 1 | 48 | 25 |

Features:

```text
Temperature
Appliances Used
Daily Usage
Is_Weekend
Usage × Appliances
```

Target:

```text
Energy Consumption
```

The exact dataset above is only a learning example and is not specified by the PDF.

---

# 6. Linear Regression

The project uses linear regression to predict energy consumption.

Conceptually:

```text
Predicted Energy =
    b₀
  + b₁(Temperature)
  + b₂(Appliances Used)
  + b₃(Daily Usage)
  + b₄(Is_Weekend)
  + b₅(Usage × Appliances)
```

The model learns the coefficients from training data.

The exact feature list and equation above are **implementation choices**. The PDF requires linear regression using temperature, appliances, daily usage patterns, and feature engineering.

---

# 7. Model Evaluation

The roadmap specifically requires:

```text
RMSE
R²
```

## 7.1 RMSE — Root Mean Squared Error

RMSE measures prediction error while giving larger errors more influence because errors are squared.

```text
RMSE = √(Σ(Actual − Predicted)² / n)
```

Steps:

```text
Error
  ↓
Square
  ↓
Mean
  ↓
Square Root
```

### Example

```text
Actual:
[20, 25, 30]

Predicted:
[22, 23, 29]
```

Errors:

```text
[-2, 2, 1]
```

Squared errors:

```text
[4, 4, 1]
```

MSE:

```text
(4 + 4 + 1) / 3
= 3
```

RMSE:

```text
√3
≈ 1.73 kWh
```

### Interpretation

```text
RMSE ≈ 1.73 kWh
```

The model's prediction error has a typical scale of about 1.73 kWh.

It does **not** mean every prediction is guaranteed to be within ±1.73 kWh.

Lower RMSE is generally better when comparing models on the same target and dataset.

---

# 8. R² Score

R² describes how well the regression model explains variation in target values.

```text
R² = 1 − SSE / SST
```

Where:

```text
SSE = Sum of Squared Errors
SST = Total variation from the mean
```

### Example

Actual:

```text
[20, 25, 30]
```

Predicted:

```text
[22, 23, 29]
```

Mean actual:

```text
(20 + 25 + 30) / 3
= 25
```

Deviations:

```text
[-5, 0, 5]
```

Squared deviations:

```text
[25, 0, 25]
```

Therefore:

```text
SST = 25 + 0 + 25
    = 50
```

Previously calculated:

```text
SSE = 9
```

Therefore:

```text
R² = 1 − 9/50
   = 0.82
```

### Interpretation

```text
R² = 0.82
```

The model explains about **82% of the variation** in household energy consumption for this example.

A value closer to 1 generally indicates that the model explains more of the variation.

---

# 9. RMSE vs R²

| Metric | Question it answers |
|---|---|
| RMSE | How large are the prediction errors? |
| R² | How much variation in the target does the model explain? |

Example:

```text
RMSE = 2.5 kWh
R²   = 0.88
```

Interpretation:

```text
RMSE → Prediction error has a scale of about 2.5 kWh

R² → Model explains about 88% of target variation
```

When comparing models:

```text
Lower RMSE → generally better
Higher R² → generally better
```

---

# 10. End-to-End Project Workflow

```text
1. Obtain Dataset
        ↓
2. Load Dataset
        ↓
3. Understand the Data
        ↓
4. Identify Features and Target
        ↓
5. Clean / Prepare Data
        ↓
6. Perform Feature Engineering
        ↓
7. Split Data
        ↓
8. Train Linear Regression Model
        ↓
9. Generate Predictions
        ↓
10. Calculate RMSE
        ↓
11. Calculate R²
        ↓
12. Interpret Results
```

This follows the ML workflow learned in the fundamentals section while keeping the project focused on the PDF requirements.

---

# 11. Suggested Project Structure

The following structure is an **implementation choice**, because the PDF does not prescribe a folder structure.

```text
Project 6 - Energy Consumption Forecasting/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── energy_consumption.csv
│
├── notebooks/
│   └── energy_consumption_analysis.ipynb
│
├── src/
│   ├── data_preparation.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── evaluate_model.py
│
└── results/
    └── model_metrics.txt
```

### Purpose

**README.md**
- Project objective
- Dataset
- Features and target
- Feature engineering
- Model
- Metrics
- Results

**data/**
- Dataset files

**notebooks/**
- Exploratory analysis and learning work

**src/**
- Reusable Python implementation

**results/**
- Final evaluation results

---

# 12. Recommended Implementation Sequence

## Phase 1 — Dataset

- Select a suitable household energy dataset.
- Load it using Pandas.
- Inspect rows, columns, and data types.

## Phase 2 — Data Preparation

- Identify the target.
- Identify input features.
- Perform required preparation.

## Phase 3 — Feature Engineering

Create useful features based on the actual dataset.

Possible implementation choices:

```text
Usage × Appliances
Is_Weekend
```

Only use features that make sense for the selected dataset.

## Phase 4 — Train Linear Regression

Use scikit-learn to train the regression model.

## Phase 5 — Predictions

Generate predictions for evaluation data.

## Phase 6 — Evaluation

Calculate:

```text
RMSE
R²
```

## Phase 7 — Interpretation

Explain what the metrics mean for household energy prediction.

---

# 13. Tools

The roadmap lists:

```text
scikit-learn
Pandas
```

These will be the primary Python libraries for this project.

---

# 14. What We Have Learned

```text
Energy Consumption Forecasting
        ↓
Regression Problem
        ↓
Features
- Temperature
- Appliances Used
- Daily Usage
        ↓
Feature Engineering
- Interaction features
- Usage-pattern features
        ↓
Linear Regression
        ↓
Predicted Energy Consumption
        ↓
Evaluation
- RMSE
- R²
```

---

# 15. Quick Revision

### Problem

Predict household energy consumption.

### Model

```text
Linear Regression
```

### Features

```text
Temperature
Appliances Used
Daily Usage
```

### Target

```text
Energy Consumption
```

### Feature Engineering

```text
Create or transform features
to represent useful patterns.

Example:
Usage × Appliances
```

### RMSE

```text
Measures prediction error.
Lower is generally better.
```

### R²

```text
Measures how well the model explains
variation in the target.
Higher / closer to 1 is generally better.
```

### Required Project Evaluation

```text
RMSE
R²
```

---

# 16. Roadmap Compliance

This project covers the Project 6 scope:

```text
✓ Household energy consumption prediction
✓ Linear regression
✓ Temperature
✓ Appliances
✓ Daily usage patterns
✓ Feature engineering
✓ RMSE evaluation
✓ R² evaluation
```

Any dataset choice, exact feature-engineering formula, file structure, and implementation organization should be treated as implementation choices unless explicitly specified by the roadmap.
