# 🐍 Variables & Data Types

> **Python for GenAI — Handwritten Notes**
>
> Focus: variables, data types, collections, and mutability

---

## 1. Variables

A variable is a **name that refers to a value/object**.

```python
name = "Deven"
age = 25
salary = 62000
```

Python is **dynamically typed**, so the type does not need to be declared explicitly.

```python
value = 25
value = "Deven"
```

A variable can refer to objects of different types during execution.

---

## 2. Basic Data Types

| Type | Purpose | Example |
|---|---|---|
| `int` | Whole numbers | `age = 25` |
| `float` | Decimal numbers | `price = 99.99` |
| `str` | Text | `name = "Deven"` |
| `bool` | `True` / `False` | `is_admin = False` |
| `None` | Absence of a value | `result = None` |

### String

```python
name = "Deven"

name.upper()
name.lower()
len(name)
```

### Boolean

```python
is_learning = True
is_admin = False
```

### None

```python
result = None
```

---

## 3. Checking Data Type

Use `type()` to check the type of a value.

```python
age = 25

print(type(age))
```

Output:

```text
<class 'int'>
```

---

## 4. f-Strings

An f-string allows variables to be inserted directly into a string.

```python
name = "Deven"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

---

# 5. Python Collections

## List

A list is **ordered and mutable**.

```python
skills = ["Java", "Python", "React"]

skills.append("FastAPI")
```

Access elements using an index:

```python
skills[0]
```

---

## Tuple

A tuple is **ordered and immutable**.

```python
coordinates = (19.07, 72.87)
```

Its elements cannot be changed after creation.

---

## Set

A set stores **unique values**.

```python
skills = {"Java", "Python", "Java"}
```

Duplicate values are removed.

---

## Dictionary

A dictionary stores data as **key-value pairs**.

```python
user = {
    "name": "Deven",
    "age": 25,
    "skills": ["Java", "Python"]
}
```

Access a value:

```python
user["name"]
```

Add a new key:

```python
user["role"] = "Software Engineer"
```

Update an existing value:

```python
user["age"] = 26
```

---

# 6. Mutable vs Immutable

## Mutable

An object can be changed after creation.

```python
skills = ["Java", "Python"]

skills.append("React")
```

Common mutable types:

```text
list
dict
set
```

## Immutable

An object cannot be changed after creation.

Common immutable types:

```text
int
float
str
tuple
bool
```

Strings cannot be modified character-by-character.

Instead, a **new string** is created:

```python
name = "Python"

new_name = name[:2] + "X" + name[3:]
```

`name` remains unchanged.

---

# 7. Quick Reference

| Concept | Key Point |
|---|---|
| Python | Dynamically typed |
| `list` | Ordered + Mutable |
| `tuple` | Ordered + Immutable |
| `set` | Unique values |
| `dict` | Key-value pairs |
| `str` | Immutable |
| `type()` | Checks data type |
| `len()` | Returns length |
| `append()` | Adds an element to a list |

---

## 🤖 Connection to GenAI

Lists and dictionaries are especially important because **API responses, JSON data, model outputs, configuration, and many AI application workflows** are commonly represented using these structures.

---

### Topic Status

- [x] Variables
- [x] Basic data types
- [x] `type()`
- [x] f-strings
- [x] Lists
- [x] Tuples
- [x] Sets
- [x] Dictionaries
- [x] Mutable vs immutable
- [x] Practical exercises
