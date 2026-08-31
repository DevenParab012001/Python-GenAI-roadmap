# ⚡ Python — Lambda Functions

> **Python + GenAI Roadmap**  
> Anonymous functions for short, simple operations.

---

## 1️⃣ Lambda

A lambda is a small **anonymous function** written in one expression.

```python
def square(number):
    return number ** 2
```

Lambda:

```python
square = lambda number: number ** 2
```

Pattern:

```text
lambda parameters: expression
```

---

## 2️⃣ Multiple Parameters

```python
add = lambda a, b: a + b
```

---

## 3️⃣ `map()` + Lambda

`map()` applies a function to every item.

```python
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, numbers))
```

---

## 4️⃣ `filter()` + Lambda

`filter()` keeps items for which the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

---

## 5️⃣ `sort()` / `sorted()` + Lambda

Lambda can tell Python which value to sort by.

```python
users.sort(
    key=lambda user: user["age"]
)
```

---

## 6️⃣ Practical Data Processing

Lambda is useful with:

```text
Lists
Dictionaries
API responses
JSON data
Data transformations
```

---

## ⚠️ Don't Overuse Lambda

```text
Simple operation → Lambda
Complex logic    → Normal function
```

Readable code is more important than making code shorter.

---

# 🧠 Quick Reference

```text
lambda x: x ** 2
        ↓
small anonymous function

map()
        ↓
transform every item

filter()
        ↓
keep matching items

sort(key=lambda ...)
        ↓
sort using a specific value
```

---

## 🤖 GenAI Connection

Lambda can help process structured data returned by APIs and GenAI systems:

```text
API / LLM response
       ↓
JSON / dictionaries
       ↓
filter / transform / sort
       ↓
Application logic
```

---

## ✅ Practice Completed

- [x] Basic Lambda
- [x] Multiple parameters
- [x] `map()` + Lambda
- [x] `filter()` + Lambda
- [x] `sort()` + Lambda
- [x] Dictionary data processing
