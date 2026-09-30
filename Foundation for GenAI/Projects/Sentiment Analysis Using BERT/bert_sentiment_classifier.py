# Project 9 — BERT Sentiment Classification
#
# Flow:
# Sentences
#     ↓
# Pretrained BERT
#     ↓
# BERT Embeddings
#     ↓
# Sentence Vectors
#     ↓
# Logistic Regression
#     ↓
# Sentiment Classification


import numpy as np
import pandas as pd
import torch

from transformers import AutoTokenizer, AutoModel

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# 1. PROJECT START
# ============================================================

print("=" * 70)
print("BERT SENTIMENT CLASSIFICATION")
print("=" * 70)


# ============================================================
# 2. LOAD DATASET
# ============================================================

data = pd.read_csv("sentiment_data.csv")

print("\nDataset:")
print(data)

print("\nDataset shape:")
print(data.shape)


# ============================================================
# 3. PREPARE SENTENCES AND LABELS
# ============================================================

sentences = data["sentence"].tolist()

labels = data["sentiment"].map({
    "negative": 0,
    "positive": 1
}).values


# ============================================================
# 4. LABEL DISTRIBUTION
# ============================================================

print("\n" + "=" * 70)
print("LABEL DISTRIBUTION")
print("=" * 70)

print(data["sentiment"].value_counts())


# ============================================================
# 5. LOAD PRETRAINED BERT
# ============================================================

print("\n" + "=" * 70)
print("LOADING PRETRAINED BERT")
print("=" * 70)

model_name = "bert-base-uncased"

print(f"\nModel: {model_name}")

tokenizer = AutoTokenizer.from_pretrained(model_name)

bert_model = AutoModel.from_pretrained(model_name)

bert_model.eval()

print("\nBERT loaded successfully.")


# ============================================================
# 6. GENERATE BERT SENTENCE EMBEDDINGS
# ============================================================

def generate_embeddings(sentences):

    embeddings = []

    for sentence in sentences:

        inputs = tokenizer(
            sentence,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128
        )

        with torch.no_grad():

            outputs = bert_model(**inputs)

        # BERT produces an embedding for every token
        token_embeddings = outputs.last_hidden_state

        # Attention mask tells us which tokens are real
        # and which are padding
        attention_mask = inputs["attention_mask"]

        # Expand mask to match embedding dimensions
        mask = attention_mask.unsqueeze(-1).expand(
            token_embeddings.size()
        ).float()

        # Remove padding token influence
        masked_embeddings = token_embeddings * mask

        # Add token embeddings
        summed_embeddings = masked_embeddings.sum(dim=1)

        # Count actual tokens
        token_count = mask.sum(dim=1)

        # Mean pooling
        sentence_embedding = (
            summed_embeddings / token_count
        )

        # Convert PyTorch tensor → NumPy array
        sentence_embedding = (
            sentence_embedding
            .squeeze(0)
            .numpy()
        )

        embeddings.append(sentence_embedding)

    return np.array(embeddings)


# ============================================================
# 7. GENERATE EMBEDDINGS
# ============================================================

print("\n" + "=" * 70)
print("GENERATING BERT EMBEDDINGS")
print("=" * 70)

X_embeddings = generate_embeddings(sentences)

print("\nBERT embedding generation completed.")


# ============================================================
# 8. DISPLAY SENTENCE VECTORS
# ============================================================

print("\n" + "=" * 70)
print("SENTENCE VECTORS")
print("=" * 70)

print("\nEmbedding shape:")
print(X_embeddings.shape)

print("\nFirst sentence:")
print(sentences[0])

print("\nFirst sentence vector:")
print(X_embeddings[0])

print("\nVector size:")
print(X_embeddings.shape[1])


# ============================================================
# 9. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_embeddings,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

print("\n" + "=" * 70)
print("TRAIN / TEST SPLIT")
print("=" * 70)

print("\nTraining vectors:")
print(X_train.shape)

print("\nTesting vectors:")
print(X_test.shape)


# ============================================================
# 10. TRAIN LOGISTIC REGRESSION
# ============================================================

print("\n" + "=" * 70)
print("TRAINING LOGISTIC REGRESSION")
print("=" * 70)

classifier = LogisticRegression(
    max_iter=1000,
    random_state=42
)

classifier.fit(
    X_train,
    y_train
)

print("\nClassifier training completed.")


# ============================================================
# 11. PREDICTIONS
# ============================================================

y_pred = classifier.predict(X_test)

print("\n" + "=" * 70)
print("PREDICTIONS")
print("=" * 70)

print("\nActual labels:")
print(y_test)

print("\nPredicted labels:")
print(y_pred)


# ============================================================
# 12. MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n" + "=" * 70)
print("MODEL EVALUATION")
print("=" * 70)

print(f"\nAccuracy: {accuracy:.2f}")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Negative",
            "Positive"
        ]
    )
)


print("Confusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# ============================================================
# 13. NEW SENTENCE PREDICTION
# ============================================================

print("\n" + "=" * 70)
print("NEW SENTENCE PREDICTION")
print("=" * 70)


def predict_sentiment(sentence):

    # Convert new sentence into BERT embedding
    sentence_vector = generate_embeddings(
        [sentence]
    )

    # Predict sentiment
    prediction = classifier.predict(
        sentence_vector
    )[0]

    # Get probabilities
    probabilities = classifier.predict_proba(
        sentence_vector
    )[0]

    if prediction == 1:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return sentiment, probabilities


# ============================================================
# 14. TEST NEW SENTENCES
# ============================================================

new_sentences = [

    "I really enjoyed this movie",

    "This product is terrible",

    "The experience was wonderful",

    "I am disappointed with the service"

]


for sentence in new_sentences:

    sentiment, probabilities = predict_sentiment(
        sentence
    )

    print("\nSentence:")
    print(sentence)

    print("\nPredicted sentiment:")
    print(sentiment)

    print(
        f"Negative probability: "
        f"{probabilities[0]:.2%}"
    )

    print(
        f"Positive probability: "
        f"{probabilities[1]:.2%}"
    )


# ============================================================
# 15. PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)

print("\n✓ Loaded sentiment dataset")

print("✓ Loaded pretrained BERT")

print("✓ Tokenized sentences")

print("✓ Generated BERT embeddings")

print("✓ Converted sentences into vectors")

print("✓ Trained Logistic Regression classifier")

print("✓ Classified sentiment")

print("✓ Evaluated classifier")

print("✓ Predicted sentiment for new sentences")

print("\nProject completed successfully!")