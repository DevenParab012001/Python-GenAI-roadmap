# ML Fundamentals — Notes

## 1. Machine Learning Basics

Traditional programming:
`Rules + Data → Program → Output`

Machine Learning:
`Data + Expected Answers → ML Algorithm → Model → Prediction`

## 2. Supervised vs Unsupervised Learning

**Supervised Learning:** The model learns from data where the correct answers (labels) are known.

Example:
`House features → House price`

**Unsupervised Learning:** The data has no known target/label. The model looks for patterns or groups.

## 3. Features and Labels

**Features:** Input information used to make a prediction.

Examples:
- Size
- Bedrooms
- Location
- Age

**Label / Target:** The value we want the model to predict.

```text
Features = Inputs
Label    = Target / answer
```

## 4. Training, Validation, and Test Sets

- **Training set:** Used by the model to learn patterns.
- **Validation set:** Used during development to evaluate and tune the model.
- **Test set:** Used for final evaluation on unseen data.

```text
Training   → Learn
Validation → Tune / develop
Test       → Final unseen evaluation
```

## 5. Generalization

Generalization means the model performs well on data it has not seen before.

```text
Training data → Learn useful patterns
Unseen data    → Apply those patterns
```

A good model should not simply memorize training examples.

## 6. Overfitting

Overfitting occurs when a model learns the training data too specifically and performs poorly on unseen data.

```text
Training performance → Very good
Test performance     → Poor
```

**Memory:** Overfitting = learns too much detail from training data.

## 7. Underfitting

Underfitting occurs when a model does not learn the underlying pattern sufficiently.

```text
Training performance → Poor
Test performance     → Poor
```

**Memory:** Underfitting = model learns too little.

## 8. Bias–Variance Trade-off

### High Bias

The model is too simple and fails to capture the underlying pattern.

```text
High Bias → Underfitting
```

### High Variance

The model is too sensitive to the particular training data and does not generalize well.

```text
High Variance → Overfitting
```

Remember:

```text
High Bias     → Underfitting
High Variance → Overfitting
```

## 9. End-to-End ML Workflow

```text
Collect Data
     ↓
Understand Data
     ↓
Clean Data
     ↓
Prepare Features
     ↓
Split Data
     ↓
Train Model
     ↓
Validate / Evaluate
     ↓
Improve Model
     ↓
Test Final Model
     ↓
Use Model for Predictions
```

Core idea:

```text
Data
 ↓
Features + Labels
 ↓
Learning Algorithm
 ↓
Model
 ↓
Predictions
 ↓
Evaluation
```

# Regression Analysis

## 10. Regression

Regression is used when the target we want to predict is a numeric value.

Example:

```text
House features → House price
```

Regression predicts a number.

Classification predicts a class/category, for example:

```text
House sells within 30 days? → Yes / No
```

## 11. Multiple Regression

Multiple regression predicts one numeric target using multiple features.

Example:

```text
Predicted Price =
b₀ + b₁(Size) + b₂(Bedrooms) + b₃(Age)
```

## 12. Feature Interactions

A feature interaction represents a combined relationship between two features.

Example:

```text
Size × Bedrooms
```

For:

```text
Size = 1000
Bedrooms = 2
```

The interaction value is:

```text
1000 × 2 = 2000
```

This is a new interaction feature; it is not simply the area.

A regression model with an interaction can be written as:

```text
Predicted Price =
b₀ + b₁(Size) + b₂(Bedrooms) + b₃(Age)
  + b₄(Size × Bedrooms)
```

# Regression Model Evaluation

## 13. Prediction Error

```text
Error = Actual − Predicted
```

Example:

```text
Actual    = 100
Predicted = 95

Error = 100 − 95 = 5
```

## 14. MAE — Mean Absolute Error

MAE measures the average absolute size of prediction errors.

Formula:

```text
MAE = Σ|Actual − Predicted| / n
```

Steps:

```text
Error
  ↓
Absolute value
  ↓
Average
```

Example:

```text
Actual:    [100, 80, 120]
Predicted: [95, 95, 110]

Errors:          [5, -15, 10]
Absolute errors: [5, 15, 10]

MAE = (5 + 15 + 10) / 3
    = 10
```

**MAE = 10** means predictions are off by about 10 target units on average.

## 15. RMSE — Root Mean Squared Error

RMSE measures prediction error while giving larger errors more influence because the errors are squared.

Steps:

```text
Error
  ↓
Square
  ↓
Mean
  ↓
Square root
```

Formula:

```text
RMSE = √(Σ(Actual − Predicted)² / n)
```

Example:

```text
Actual:    [100, 80, 120]
Predicted: [90, 90, 115]

Errors:  [+10, -10, +5]
Squared: [100, 100, 25]

MSE = (100 + 100 + 25) / 3
    = 75

RMSE = √75
     ≈ 8.66
```

## 16. R² Score

R² describes how well a regression model explains the variation in the target values.

```text
R² closer to 1 → explains more variation
R² closer to 0 → explains less variation
```

Formula:

```text
R² = 1 − SSE / SST
```

Where:
- **SSE** = sum of squared prediction errors
- **SST** = total variation from the mean

Example:

```text
Actual:    [100, 120, 140]
Predicted: [110, 115, 135]

Mean actual = 120
SSE = 150
SST = 800

R² = 1 − 150/800
   = 0.8125
```

So the model explains about **81.25% of the variation** in this example.

## 17. MAE vs RMSE vs R²

| Metric | Main question |
|---|---|
| MAE | How wrong are the predictions on average? |
| RMSE | How large are prediction errors, with larger errors penalized more? |
| R² | How well does the model explain variation in the target? |

Example:

```text
MAE = 10
R²  = 0.94
```

This means:
- predictions are off by about 10 units on average
- the model explains about 94% of the variation in the target

Using multiple metrics gives a more complete picture than using MAE alone.

# Quick Revision

```text
Features = Inputs
Label = Target

Supervised = Known labels
Unsupervised = No known labels

Training = Learn
Validation = Tune / develop
Test = Final unseen evaluation

Generalization = Performs well on unseen data

High Bias = Underfitting
High Variance = Overfitting

Regression = Predict a numeric value
Classification = Predict a class/category

MAE = Average absolute error
RMSE = Square-root of average squared error
R² = How well the model explains target variation
```

## Current Progress

Completed:
- Supervised vs Unsupervised Learning
- Features and Labels
- Training / Validation / Test Sets
- Generalization
- Overfitting / Underfitting
- Bias–Variance Trade-off
- End-to-End ML Workflow
- Regression Analysis
- Multiple Regression
- Feature Interactions
- MAE
- RMSE
- R² Score

Next in the PDF:
- Classification Analysis
- Logistic Regression for binary classification
- Handling class imbalance using sampling techniques
- Precision, Recall, F1-Score, ROC-AUC
