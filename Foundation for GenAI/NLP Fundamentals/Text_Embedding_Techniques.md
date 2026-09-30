# Text Embedding Techniques

## 1. Introduction

Text embedding techniques convert text into numerical representations that can be used by NLP systems.

The PDF lists:
- Bag of Words (BoW)
- TF-IDF
- Word2Vec
  - CBOW
  - Skip-Gram

## 2. Bag of Words (BoW)

Bag of Words represents text using word counts.

Example:

```text
cat dog dog
```

Vocabulary:

```text
[cat, dog, ball]
```

BoW representation:

```text
[1, 2, 0]
```

This means `cat` appears once, `dog` twice, and `ball` zero times.

**Important:** BoW represents word occurrence/counts but does not preserve original word order.

## 3. TF-IDF

TF-IDF represents the importance of a word using:
- How frequently the word occurs in a document
- How common or rare the word is across documents

TF-IDF stands for **Term Frequency – Inverse Document Frequency**.

### Term Frequency (TF)

A basic form is:

```text
TF = Number of times the word appears / Total number of words
```

### Inverse Document Frequency (IDF)

IDF represents how rare a word is across documents.

A common conceptual formula is:

```text
IDF = log(N / DF)
```

where `N` is the total number of documents and `DF` is the number of documents containing the word.

A word appearing in many documents has lower IDF. A word appearing in fewer documents has higher IDF.

### TF-IDF

```text
TF-IDF = TF × IDF
```

A word that occurs frequently in a document but is relatively rare across the document collection can receive a higher TF-IDF value. A word common across many documents can receive a lower value because its IDF is lower.

## 4. Word2Vec

Word2Vec learns numerical representations of words based on their context.

The two approaches listed in the PDF are:
- CBOW
- Skip-Gram

## 5. CBOW

CBOW (Continuous Bag of Words) uses surrounding context words to predict the target word.

```text
Context Words
      ↓
    CBOW
      ↓
Target Word
```

## 6. Skip-Gram

Skip-Gram uses a target word to predict surrounding context words.

```text
Target Word
     ↓
 Skip-Gram
     ↓
Context Words
```

## 7. CBOW vs Skip-Gram

| Technique | Input | Predicts |
|---|---|---|
| CBOW | Context words | Target word |
| Skip-Gram | Target word | Context words |

Simple memory aid:

```text
CBOW:      Context → Target
Skip-Gram: Target  → Context
```

## 8. Comparison

| Technique | Basic idea |
|---|---|
| BoW | Represents text using word counts |
| TF-IDF | Represents word importance using frequency and document rarity |
| Word2Vec | Learns word representations from context |
| CBOW | Context → target word |
| Skip-Gram | Target word → context words |

## 9. Summary

- **BoW** represents text using word counts.
- BoW does not preserve word order.
- **TF-IDF** considers term frequency and document-level rarity.
- **Word2Vec** learns word representations from context.
- **CBOW** predicts a target word from surrounding context.
- **Skip-Gram** predicts surrounding context from a target word.
