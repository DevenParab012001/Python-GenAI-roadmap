# Project 9 — BERT Sentiment Classification

## 1. Project Objective

The project follows the PDF requirement:

> Use pretrained BERT embeddings to convert sentences into vectors and classify sentiment using a simple classifier.

The implementation uses **Logistic Regression** as the simple classifier.

---

## 2. Project Flow

```text
Sentences
    ↓
Pretrained BERT
    ↓
BERT Embeddings
    ↓
Sentence Vectors
    ↓
Logistic Regression
    ↓
Sentiment Classification
```

---

## 3. Dataset

The project uses a CSV dataset named:

```text
sentiment_data.csv
```

Columns:

```text
sentence
sentiment
```

The dataset contains:

- 20 sentences
- 10 positive sentences
- 10 negative sentences

Labels are converted to numerical values:

```text
negative → 0
positive → 1
```

---

## 4. Pretrained BERT

The implementation uses:

```text
bert-base-uncased
```

Two pretrained BERT components are loaded:

```python
AutoTokenizer
AutoModel
```

The tokenizer converts sentences into tokenized inputs that can be passed to BERT.

The BERT model produces token-level embeddings.

---

## 5. Generating Sentence Embeddings

BERT produces an embedding for every token.

The implementation uses **mean pooling** to convert the token embeddings into one vector representing the complete sentence.

The attention mask is used so that padding tokens do not influence the pooled representation.

Conceptually:

```text
Sentence
   ↓
Tokenization
   ↓
BERT
   ↓
Token Embeddings
   ↓
Attention Mask
   ↓
Mean Pooling
   ↓
Sentence Vector
```

---

## 6. Sentence Vector Size

For this project, each sentence is converted into a:

```text
768-dimensional vector
```

The complete embedding matrix has the shape:

```text
(20, 768)
```

Meaning:

- 20 sentences
- 768 values per sentence vector

---

## 7. Train / Test Split

The project uses an 80/20 train/test split.

Result:

```text
Training vectors: (16, 768)
Testing vectors:  (4, 768)
```

Therefore:

- 16 examples are used for training.
- 4 examples are used for testing.

The split uses stratification so that the sentiment classes are represented in the split.

---

## 8. Logistic Regression Classifier

After generating the BERT sentence vectors, the vectors are passed to a Logistic Regression classifier.

```text
BERT Sentence Vectors
        ↓
Logistic Regression
        ↓
Sentiment Prediction
```

The classifier is trained using the training vectors and their corresponding sentiment labels.

---

## 9. Model Evaluation

The project evaluates the classifier using:

- Accuracy
- Classification Report
- Confusion Matrix

### Accuracy

The accuracy obtained on the 4-example test set was:

```text
1.00
```

or:

```text
100%
```

All four test predictions matched their actual labels.

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Negative | 1.00 | 1.00 | 1.00 | 2 |
| Positive | 1.00 | 1.00 | 1.00 | 2 |

### Confusion Matrix

```text
[[2 0]
 [0 2]]
```

This means:

```text
2 Negative → correctly predicted Negative
2 Positive → correctly predicted Positive
```

---

## 10. New Sentence Prediction

The project also accepts new sentences.

For each new sentence:

```text
New Sentence
    ↓
BERT Embedding
    ↓
Sentence Vector
    ↓
Logistic Regression
    ↓
Predicted Sentiment
```

The classifier also provides the predicted probabilities for the two sentiment classes.

---

## 11. New Sentence Results

### Sentence 1

```text
I really enjoyed this movie
```

Prediction:

```text
Positive
```

Probabilities:

```text
Negative: 7.57%
Positive: 92.43%
```

### Sentence 2

```text
This product is terrible
```

Prediction:

```text
Negative
```

Probabilities:

```text
Negative: 85.60%
Positive: 14.40%
```

### Sentence 3

```text
The experience was wonderful
```

Prediction:

```text
Positive
```

Probabilities:

```text
Negative: 4.81%
Positive: 95.19%
```

### Sentence 4

```text
I am disappointed with the service
```

Prediction:

```text
Negative
```

Probabilities:

```text
Negative: 91.94%
Positive: 8.06%
```

---

## 12. Complete Implementation Flow

```text
Load sentiment_data.csv
        ↓
Separate sentences and labels
        ↓
Convert labels
negative → 0
positive → 1
        ↓
Load pretrained BERT
        ↓
Tokenize sentences
        ↓
Generate BERT token embeddings
        ↓
Apply attention mask
        ↓
Mean pooling
        ↓
Generate 768-dimensional sentence vectors
        ↓
Train/Test Split
        ↓
Train Logistic Regression
        ↓
Predict test sentiments
        ↓
Evaluate model
        ↓
Predict sentiment for new sentences
```

---

## 13. Project Files

The project consists of:

```text
Sentiment Analysis Using BERT/
├── bert_sentiment_classifier.py
├── sentiment_data.csv
└── README.md
```

The Python file contains the complete implementation.

The CSV file contains the sentiment dataset.

This Markdown file documents the project and its results.

---

## 14. Project Requirement Check

The PDF requires:

```text
Pretrained BERT embeddings
        ↓
Convert sentences into vectors
        ↓
Simple classifier
        ↓
Sentiment classification
```

The implementation satisfies these requirements:

- ✓ Pretrained BERT used
- ✓ BERT embeddings generated
- ✓ Sentences converted into vectors
- ✓ Simple classifier used
- ✓ Sentiment classified

---

## 15. Important Result Note

The project achieved 100% accuracy on its test set of only 4 examples.

Therefore, this result represents the performance on this particular small test set. It should not be interpreted as evidence that the system will achieve 100% accuracy on a larger or real-world sentiment dataset.

---

## 16. Project Summary

This project demonstrates how pretrained BERT can be used as an embedding model for sentiment classification.

The overall approach is:

```text
Sentence
   ↓
Pretrained BERT
   ↓
BERT Embedding
   ↓
768-Dimensional Sentence Vector
   ↓
Logistic Regression
   ↓
Positive / Negative
```

Project execution completed successfully.
