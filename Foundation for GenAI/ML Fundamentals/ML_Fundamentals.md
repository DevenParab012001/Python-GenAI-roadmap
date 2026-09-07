# ML Fundamentals

## Machine Learning Basics
Traditional programming: `Rules + Data → Program → Output`

Machine learning: `Data + Expected Answers → ML Algorithm → Model → Prediction`

## Supervised vs Unsupervised Learning
- **Supervised learning:** learns from data with known labels.
- **Unsupervised learning:** works without known target labels and discovers patterns/groups.

## Features and Labels
- **Features:** input information used for prediction.
- **Label / Target:** value the model predicts.

Example:
`House Size, Bedrooms, Age → Features`
`House Price → Label`

## Training, Validation and Test Sets
- **Training:** learn patterns.
- **Validation:** tune/develop the model.
- **Test:** final evaluation on unseen data.

## Generalization
Generalization means performing well on unseen data.

## Overfitting and Underfitting
- **Overfitting:** learns training data too specifically; training performance is high but unseen/test performance is poor.
- **Underfitting:** does not learn the underlying pattern sufficiently; training and test performance are poor.

## Bias–Variance Trade-off
- **High Bias → Underfitting**
- **High Variance → Overfitting**

## End-to-End ML Workflow
`Collect Data → Understand Data → Clean Data → Prepare Features → Split Data → Train Model → Validate/Evaluate → Improve Model → Test Final Model → Use Model for Predictions`

## Quick Revision
```text
Features = Inputs
Label = Target

Supervised = Known labels
Unsupervised = No known labels

Training = Learn
Validation = Tune / Develop
Test = Final unseen evaluation

Generalization = Performs well on unseen data
High Bias = Underfitting
High Variance = Overfitting
```
