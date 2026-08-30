# 🧩 Python — List & Dictionary Comprehensions

> **Python + GenAI Roadmap**  
> A concise reference for creating and filtering collections.

---

## 🧭 Core Idea

A comprehension provides a compact way to create a new collection from an existing collection.

```text
Collection → process/filter → New Collection
```

---

# 1️⃣ List Comprehension

Basic pattern:

```python
[expression for item in collection]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
```

---

# 2️⃣ Filtering

Add `if` to keep only matching values.

```python
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]
```

Pattern:

```python
[expression for item in collection if condition]
```

---

# 3️⃣ Transforming Data

```python
skills = ["python", "java", "docker"]

upper_skills = [skill.upper() for skill in skills]
```

The original collection is used to create a transformed collection.

---

# 4️⃣ `if / else` in a Comprehension

Used when every item should produce a value, but the value depends on a condition.

```python
result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]
```

Pattern:

```python
[true_value if condition else false_value for item in collection]
```

### Remember the difference

```python
# Filter
[x for x in numbers if x > 5]

# Choose a value for every item
["Yes" if x > 5 else "No" for x in numbers]
```

---

# 5️⃣ Dictionary Comprehension

Creates a dictionary using a comprehension.

```python
squares = {
    number: number ** 2
    for number in numbers
}
```

Pattern:

```python
{key: value for item in collection}
```

---

# 6️⃣ Dictionary Filtering

```python
users = {
    "Deven": 25,
    "Rahul": 17,
    "Amit": 30
}

adults = {
    name: age
    for name, age in users.items()
    if age >= 18
}
```

`.items()` gives access to both keys and values.

---

# 7️⃣ Nested JSON-like Data

Comprehensions are useful when processing API-style data.

```python
users = [
    {
        "name": "Deven",
        "skills": ["Python", "Java"]
    },
    {
        "name": "Rahul",
        "skills": ["React", "Java"]
    }
]

names = [
    user["name"]
    for user in users
    if "Python" in user["skills"]
]
```

This produces the names of users who know Python.

---

# ⚠️ Readability

Comprehensions are useful when they make code simpler.

Avoid extremely complicated comprehensions.

```text
Readable code > clever code
```

If the logic becomes difficult to understand, use a normal `for` loop.

---

# 🤖 GenAI Connection

Comprehensions are useful when processing:

```text
API responses
JSON data
Documents
Chunks
Retrieved results
Metadata
```

For example:

```text
Retrieved documents
       ↓
Filter relevant results
       ↓
Extract text
       ↓
Create new collection
```

This pattern will appear frequently in our GenAI projects.

---

## 🧠 Quick Reference

```text
[expression for x in data]
→ transform

[x for x in data if condition]
→ filter

[value_if_true if condition else value_if_false for x in data]
→ transform with condition

{key: value for x in data}
→ dictionary comprehension

.items()
→ key + value
```

---

## ✅ Practice Completed

- [x] List comprehensions
- [x] Filtering
- [x] Transforming data
- [x] `if / else` expressions
- [x] Dictionary comprehensions
- [x] Dictionary filtering
- [x] Nested JSON-like data
