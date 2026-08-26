# 🐍 Python Collections

> **Python + GenAI Roadmap**  
> Practical reference for Python's built-in collection types.

---

## 📌 Collection Overview

| Collection | Ordered | Mutable | Duplicates | Main Use |
|---|:---:|:---:|:---:|---|
| `list` | ✅ | ✅ | ✅ | General collection |
| `tuple` | ✅ | ❌ | ✅ | Fixed collection |
| `set` | ❌ | ✅ | ❌ | Unique values |
| `dict` | ✅* | ✅ | Keys: ❌ | Key-value data |

> \* Modern Python dictionaries preserve insertion order.

### Quick decision rule

```text
Normal collection  → list
Should not change  → tuple
Need unique values → set
Key → value mapping → dict
```

---

# 1️⃣ Lists

A list is **ordered, mutable, and allows duplicate values**.

```python
skills = ["Java", "Python", "React"]
```

### Indexing

Python uses zero-based indexing.

```python
skills[0]      # First element
skills[-1]     # Last element
```

### Modifying

```python
skills[1] = "FastAPI"
```

### Adding

```python
skills.append("GenAI")           # Add to end
skills.insert(1, "Spring Boot")   # Add at index
skills.extend(["Docker", "SQL"])  # Add multiple
```

### Removing

```python
skills.remove("React")  # Remove first matching value
skills.pop()            # Remove last element
skills.pop(1)           # Remove by index
del skills[0]           # Delete by index
```

---

## ✂️ List Slicing

Syntax:

```python
list[start:stop:step]
```

`start` is included; `stop` is excluded.

```python
skills[:3]     # First 3
skills[-2:]    # Last 2
skills[::2]    # Every second element
skills[::-1]   # Reverse
```

### Useful operations

```python
len(skills)             # Number of elements
"Python" in skills      # Membership check
skills.count("Python")  # Count occurrences
skills.index("Python")  # Find index
```

### Sorting

```python
numbers.sort()
```

`sort()` modifies the existing list.

```python
sorted_numbers = sorted(numbers)
```

`sorted()` returns a sorted result without modifying the original list.

---

# 2️⃣ Tuples

A tuple is **ordered and immutable**.

```python
coordinates = (19.07, 72.87)
```

Access values using indexes:

```python
coordinates[0]
```

A tuple cannot be modified after creation.

### Tuple Unpacking

```python
employee = ("Deven", "Software Engineer", 4)

name, role, experience = employee
```

This assigns:

```text
name       → "Deven"
role       → "Software Engineer"
experience → 4
```

Python also allows variable swapping:

```python
a = 10
b = 20

a, b = b, a
```

---

# 3️⃣ Sets

A set stores **unique values**.

```python
skills = {"Python", "Java", "Python", "React"}
```

Duplicate values are removed.

### Add / Remove

```python
skills.add("Docker")

skills.remove("Java")
skills.discard("Java")
```

`discard()` does not raise an error if the value doesn't exist.

### Set Operations

```python
backend = {"Java", "Python", "SQL"}
ai = {"Python", "RAG", "Docker"}
```

**Union — all unique values**

```python
backend | ai
```

**Intersection — common values**

```python
backend & ai
```

**Difference — backend only**

```python
backend - ai
```

**Difference — AI only**

```python
ai - backend
```

---

# 4️⃣ Dictionaries

A dictionary stores **key-value pairs**.

```python
user = {
    "name": "Deven",
    "age": 25,
    "role": "Software Engineer"
}
```

Think:

```text
key       → value
"name"    → "Deven"
"age"     → 25
"role"    → "Software Engineer"
```

### Accessing values

```python
user["name"]
```

or:

```python
user.get("name")
```

`get()` can provide a default:

```python
user.get("salary", 0)
```

### Add / Update

```python
user["salary"] = 62000
user["age"] = 26
```

The same syntax handles both adding and updating.

### Remove

```python
user.pop("age")
del user["age"]
```

---

## 🔑 Useful Dictionary Methods

```python
user.keys()
user.values()
user.items()
```

Example:

```python
for key, value in user.items():
    print(key, value)
```

---

# 5️⃣ Nested Collections

Collections can contain other collections.

```python
user = {
    "name": "Deven",
    "profile": {
        "age": 25,
        "role": "Software Engineer"
    },
    "skills": ["Python", "Java", "React"]
}
```

Access nested values:

```python
user["profile"]["role"]
user["skills"][0]
```

This pattern is extremely common when working with JSON and APIs.

---

# 🤖 Why Collections Matter for GenAI

LLM and API responses commonly contain nested dictionaries and lists.

```python
response = {
    "answer": "Python is dynamically typed.",
    "sources": [
        {"title": "Python Docs", "page": 10},
        {"title": "Programming Guide", "page": 25}
    ],
    "usage": {
        "input_tokens": 120,
        "output_tokens": 45
    }
}
```

This combines:

```text
Dictionary
├── String
├── List
│   ├── Dictionary
│   └── Dictionary
└── Dictionary
    ├── Integer
    └── Integer
```

These structures will appear frequently in:

- FastAPI APIs
- JSON processing
- LLM responses
- RAG pipelines
- Tool calling
- Agent state
- Configuration

---

## 🧪 Practice Completed

- [x] List manipulation
- [x] List slicing
- [x] Tuple unpacking
- [x] Set operations
- [x] Dictionary manipulation
- [x] Nested collections
- [x] Nested API-like data

---

## 💡 Key Takeaway

```text
list  → ordered, mutable collection
tuple → ordered, immutable collection
set   → unique values
dict  → key-value mapping
```
