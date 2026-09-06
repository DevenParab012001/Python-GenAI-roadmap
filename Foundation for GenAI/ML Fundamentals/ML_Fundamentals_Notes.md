# ML Fundamentals — Notes

## 1. Machine Learning

Machine Learning learns patterns from data so a model can make predictions or decisions.

### Traditional Programming
Rules + Data → Program → Output

### Machine Learning
Data + Expected Answers → ML Algorithm → Model → Prediction

---

## 2. Supervised Learning

Training data contains:

- Input/features
- Known correct answer/label

The model learns the relationship between features and the label.

**Example:**

Features:
- Hours studied
- Attendance

Label:
- Marks

Used when the target answer is known during training.

---

## 3. Unsupervised Learning

Training data does not contain a known target label.

The algorithm tries to discover patterns or groups in the data.

**Example:**

Customer age + spending data → discover groups of similar customers.

---

## 4. Supervised vs Unsupervised

| Supervised | Unsupervised |
|---|---|
| Known answers/labels | No known labels |
| Features + label | Features only |
| Learn to predict | Discover patterns/groups |

---

## 5. Features and Labels

**Features** = information used to make a prediction.

**Label / Target** = the value we want to predict.

Example:

```text
Age + Salary + Experience → Loan Approval
```

Features:
`Age, Salary, Experience`

Label:
`Loan Approval`

---

## 6. Training, Validation and Test Sets

### Training Set
Used to teach the model and learn patterns.

### Validation Set
Used during model development to compare/tune the model.

### Test Set
Used for the final evaluation on unseen data.

Remember:

```text
Training   → Learn
Validation → Develop / Tune
Test       → Final Evaluation
```

---

## 7. Generalization

**Generalization** means a model performs well on data it has not seen during training.

A good model should not simply memorize the training examples.

```text
Training data → Learn useful patterns
Unseen data    → Apply those patterns
```

---

## 8. Overfitting

Overfitting occurs when a model learns the training data too specifically and performs poorly on unseen data.

Typical pattern:

```text
Training performance → Very good
Test performance     → Poor
```

Memory:

**Overfitting = learns too much detail from training data.**

---

## 9. Underfitting

Underfitting occurs when a model does not learn the underlying pattern sufficiently.

Typical pattern:

```text
Training performance → Poor
Test performance     → Poor
```

Memory:

**Underfitting = model learns too little.**

---

## 10. Bias–Variance Trade-off

### High Bias

Model is too simple and fails to capture the underlying pattern.

```text
High Bias → Underfitting
```

### High Variance

Model is too sensitive to the particular training data and does not generalize well.

```text
High Variance → Overfitting
```

Remember:

```text
High Bias     → Underfitting
High Variance → Overfitting
```

---

## 11. End-to-End ML Workflow

High-level workflow:

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

---

## Quick Revision

```text
Features = Inputs used for prediction
Label    = Target / answer to predict

Supervised   = Known labels
Unsupervised = No known labels

Training   = Learn
Validation = Tune / develop
Test       = Final unseen evaluation

Generalization = Performs well on unseen data

High Bias     = Underfitting
High Variance = Overfitting
```

## Current ML Fundamentals Progress

Completed so far:

- Supervised vs Unsupervised Learning
- Features and Labels
- Training / Validation / Test Sets
- Generalization
- Overfitting / Underfitting
- Bias–Variance Trade-off

**Still to cover from the PDF:** End-to-end ML workflow in more detail, followed by Regression Analysis and Classification Analysis.
