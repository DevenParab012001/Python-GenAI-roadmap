# Topic Modeling

## 1. Introduction

Topic Modeling is an NLP technique used to discover hidden themes or topics in a collection of documents.

The basic idea is:

```text
Collection of Documents
          ↓
    Topic Modeling
          ↓
     Hidden Topics
```

The topics are discovered from patterns in the words used across the documents.

---

## 2. Why Topic Modeling Is Used

A collection of documents may contain different themes without explicitly telling us what those themes are.

Topic modeling helps discover those underlying themes.

For example, a collection of documents might contain words related to:

```text
football, player, goal, match
```

and another group might contain:

```text
doctor, hospital, patient, treatment
```

Topic modeling can help identify these as different underlying topics.

The human can then interpret and assign meaningful names to the discovered topics.

---

## 3. LDA

LDA stands for:

**Latent Dirichlet Allocation**

LDA is a topic modeling approach in which a document can be represented as a mixture of topics.

Conceptually:

```text
Document
   ↓
Topic Modeling
   ↓
Topic 1 + Topic 2 + Topic 3 ...
```

A document does not necessarily have to belong to only one topic.

For example, a document could contain:

```text
Topic A → 60%
Topic B → 40%
```

The topics are associated with patterns or distributions of words.

The human interprets those word patterns and gives the topics meaningful labels.

---

## 4. LDA Example

Suppose we have several documents about different subjects.

Some documents contain words such as:

```text
goal
player
match
team
```

Another group contains:

```text
hospital
doctor
patient
medicine
```

LDA can discover patterns in these words and produce latent topics.

Conceptually:

```text
Topic 1:
goal, player, match, team

Topic 2:
hospital, doctor, patient, medicine
```

The human can interpret these as topics such as:

```text
Topic 1 → Sports
Topic 2 → Healthcare
```

The labels are interpretations of the discovered topics.

---

## 5. LSA / LST

The PDF lists:

**LSA / LST**

under Topic Modeling.

At a high level, LSA / LST deals with discovering latent semantic patterns and relationships in text.

The important idea is that the method helps identify underlying semantic structure rather than simply looking at individual words in isolation.

---

## 6. LDA vs LSA / LST

At the level specified in the roadmap:

| Method | Main idea |
|---|---|
| LDA | Discovers latent topics using patterns/distributions of words; a document can be a mixture of topics |
| LSA / LST | Identifies latent semantic patterns and relationships in text |

---

## 7. Important Note

The SDE Master Program PDF lists **Topic Modeling**, with **LDA** and **LSA/LST**, but does not provide detailed mathematical procedures, algorithms, implementation steps, or formulas.

Therefore, this note stays at the conceptual level covered by the roadmap and does not introduce additional details as required roadmap material.

---

## 8. Summary

- **Topic Modeling** discovers hidden themes in a collection of documents.
- It uses patterns in words to identify underlying topics.
- **LDA** allows a document to be represented as a mixture of topics.
- LDA topics are associated with distributions or patterns of words.
- Humans interpret the discovered word patterns and assign meaningful topic labels.
- **LSA/LST** is listed as another Topic Modeling approach for identifying latent semantic patterns and relationships.
