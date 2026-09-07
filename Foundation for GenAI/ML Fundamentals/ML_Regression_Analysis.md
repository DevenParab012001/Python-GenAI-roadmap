# ML Regression Analysis

## Regression
Regression predicts a **numeric target**.

Examples: house price, energy consumption, temperature.

## Multiple Regression
Multiple regression predicts one numeric target using multiple features.

```text
Predicted Price = b₀ + b₁(Size) + b₂(Bedrooms) + b₃(Age)
```

## Feature Interactions
A feature interaction represents a combined effect between features.

Example:
```text
Size × Bedrooms
```

For `Size = 1000` and `Bedrooms = 2`:
`Size × Bedrooms = 2000`

A model can include the interaction:
```text
Predicted Price =
b₀ + b₁(Size) + b₂(Bedrooms) + b₃(Age)
+ b₄(Size × Bedrooms)
```

## Prediction Error
```text
Error = Actual − Predicted
```

## MAE — Mean Absolute Error
Measures average absolute prediction error.

```text
MAE = Σ|Actual − Predicted| / n
```

Steps:
`Error → Absolute value → Average`

Example:
```text
Actual:    [100, 80, 120]
Predicted: [95, 95, 110]

Errors:          [5, -15, 10]
Absolute errors: [5, 15, 10]

MAE = (5 + 15 + 10) / 3
    = 10
```

## RMSE — Root Mean Squared Error
Measures prediction error while giving larger errors more influence because errors are squared.

Steps:
`Error → Square → Mean → Square root`

```text
RMSE = √(Σ(Actual − Predicted)² / n)
```

Example:
```text
Actual:    [100, 80, 120]
Predicted: [90, 90, 115]

Errors:  [+10, -10, +5]
Squared: [100, 100, 25]

MSE = 75
RMSE = √75 ≈ 8.66
```

## R² Score
Describes how well a regression model explains variation in target values.

```text
R² closer to 1 → Explains more variation
R² closer to 0 → Explains less variation

R² = 1 − SSE / SST
```

- **SSE:** sum of squared prediction errors.
- **SST:** total variation from the mean.

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

The model explains about **81.25% of the variation**.

## MAE vs RMSE vs R²
| Metric | Main question |
|---|---|
| MAE | How wrong are predictions on average? |
| RMSE | How large are prediction errors, with larger errors penalized more? |
| R² | How well does the model explain variation in the target? |

## Quick Revision
```text
Regression = Predict a numeric value
Multiple Regression = One numeric target using multiple features
Feature Interaction = Combined effect of features
MAE = Average absolute error
RMSE = Square-root of average squared error
R² = How well the model explains target variation
```
