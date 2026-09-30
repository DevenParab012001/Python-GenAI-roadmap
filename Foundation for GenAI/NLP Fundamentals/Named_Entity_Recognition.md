# Named Entity Recognition (NER)

## 1. Introduction

Named Entity Recognition (NER) is an NLP task that identifies named entities in text and assigns them categories.

Examples of entity categories include:

- Person
- Organization
- Location

---

## 2. What NER Does

NER takes text and identifies meaningful named entities.

Conceptually:

```text
Text
 ↓
NER
 ↓
Named Entities + Categories
```

### Example

Sentence:

```text
Rahul works at Microsoft in Mumbai.
```

NER can identify:

```text
Rahul      → Person
Microsoft  → Organization
Mumbai     → Location
```

---

## 3. Named Entities

A named entity is a specific entity mentioned in text.

Common examples include:

| Entity | Category |
|---|---|
| Rahul | Person |
| Microsoft | Organization |
| Mumbai | Location |

NER is not limited to single-word entities.

### Multi-word Entities

A named entity can contain multiple words.

For example:

```text
New York
```

can be identified as:

```text
New York → Location
```

The complete phrase represents the entity.

---

## 4. NER Process

The basic idea can be represented as:

```text
Input Text
    ↓
Identify entity mentions
    ↓
Assign entity categories
    ↓
NER Output
```

For example:

```text
"Apple opened an office in London."

Apple  → Organization
London → Location
```

---

## 5. Why NER Is Useful

NER helps NLP systems identify important named entities in text.

Instead of treating the complete sentence as undifferentiated text, an NLP system can recognize specific entities and their categories.

For example:

```text
"John joined Google in Mumbai."

John   → Person
Google → Organization
Mumbai → Location
```

---

## 6. Important Note

The SDE Master Program PDF lists **NER** as an NLP topic, but it does not specify a detailed list of NER algorithms, libraries, implementation steps, or additional entity categories.

Therefore, this note stays within the concepts covered during the roadmap learning and does not introduce additional techniques as required roadmap content.

---

## 7. Summary

- **NER** stands for Named Entity Recognition.
- It identifies named entities in text.
- It assigns categories to identified entities.
- Common categories covered are **Person, Organization, and Location**.
- NER can identify multi-word entities such as **New York**.
