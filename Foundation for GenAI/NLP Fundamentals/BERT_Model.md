# Transformer — BERT Model

## 1. Transformer Architecture

The Transformer architecture uses **Encoder–Decoder blocks**.

At a high level:

```text
Input
  ↓
Transformer Architecture
  ↓
Encoder / Decoder Blocks
  ↓
Processed Representation / Output
```

The encoder is used to build a representation of the input, while the Transformer architecture also includes decoder blocks.

---

## 2. Multi-Head Self-Attention

Self-attention allows each token to consider information from other tokens in the input.

For example, in a sentence, a token can use information from other relevant tokens to build a better representation.

### Multi-Head Self-Attention

Multi-head self-attention uses multiple attention heads.

The idea is that different heads can capture different relationships or patterns between tokens.

Conceptually:

```text
Input Tokens
     ↓
Self-Attention Heads
     ↓
Multiple Relationships / Patterns
     ↓
Combined Representation
```

### Key Idea

- **Self-attention** → tokens can consider information from other tokens.
- **Multi-head self-attention** → multiple heads can capture different relationships or patterns.

---

## 3. Positional Encoding

Transformers need information about the **position or order of tokens**.

Consider:

```text
Dog bites man
```

and:

```text
Man bites dog
```

The same words appear, but their order is different.

Positional encoding provides the Transformer with information about the position/order of tokens.

Conceptually:

```text
Token Information
       +
Position Information
       ↓
Token Representation
```

### Simple Example

```text
The   → Position 1
dog   → Position 2
runs  → Position 3
```

The position information helps the Transformer distinguish the order of tokens.

---

## 4. BERT Pre-Training Objectives

The PDF specifies two BERT pre-training objectives:

1. **MLM — Masked Language Modeling**
2. **NSP — Next Sentence Prediction**

---

## 5. MLM — Masked Language Modeling

MLM asks BERT to predict a missing or masked word.

Example:

```text
The cat is drinking [MASK].
```

BERT attempts to predict:

```text
milk
```

Conceptually:

```text
Sentence with Mask
        ↓
       BERT
        ↓
Predicted Missing Word
```

### Key Idea

**MLM → predict the masked word.**

---

## 6. NSP — Next Sentence Prediction

NSP asks BERT to determine whether the second sentence is the next sentence related to the first.

Example:

```text
Sentence A:
I went to the restaurant.

Sentence B:
I ordered a pizza.
```

BERT determines whether Sentence B is the next sentence associated with Sentence A.

Conceptually:

```text
Sentence A + Sentence B
          ↓
         BERT
          ↓
Relationship / Next Sentence Prediction
```

### Key Idea

**NSP → determine whether the second sentence follows the first.**

---

## 7. BERT Use Cases in Real NLP Systems

The PDF includes **use cases of BERT in real NLP systems**.

At a general level, BERT can be used for understanding and processing text in NLP systems.

A project in the roadmap demonstrates one such application:

```text
Sentences
    ↓
Pretrained BERT
    ↓
BERT Embeddings
    ↓
Sentence Vectors
    ↓
Simple Classifier
    ↓
Sentiment Classification
```

This is the basis of **Project 9 — Sentiment Analysis Using BERT**.

---

## 8. Important Concepts to Remember

### Transformer Architecture

Uses:

```text
Encoder + Decoder Blocks
```

### Self-Attention

Allows tokens to consider information from other tokens.

### Multi-Head Self-Attention

Uses multiple attention heads to capture different relationships or patterns.

### Positional Encoding

Provides information about token position/order.

### MLM

```text
Masked word → predict the missing word
```

### NSP

```text
Sentence A + Sentence B → determine whether B follows A
```

---

## 9. Summary

- Transformer architecture includes **Encoder–Decoder blocks**.
- Self-attention allows tokens to consider information from other tokens.
- Multi-head self-attention uses multiple heads to capture different relationships or patterns.
- Positional encoding provides information about token position/order.
- BERT uses **MLM** and **NSP** as the pre-training objectives listed in the roadmap.
- MLM predicts a masked word.
- NSP determines whether the second sentence is the next sentence related to the first.
- BERT can be used for understanding and processing text in real NLP systems.
