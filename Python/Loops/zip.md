# 🔗 Python — `zip()`

> **Python + GenAI Roadmap**  
> Pairing corresponding values from multiple iterables.

---

## 1️⃣ What is `zip()`?

`zip()` combines elements from multiple iterables **position by position**.

```python
names = ["Deven", "Rahul", "Amit"]
ages = [25, 30, 28]

result = zip(names, ages)

print(list(result))
```

Result:

```text
[("Deven", 25), ("Rahul", 30), ("Amit", 28)]
```

---

## 2️⃣ `zip()` Returns an Iterator

```python
result = zip(names, ages)
```

To convert it to a list:

```python
list(result)
```

Or iterate directly:

```python
for name, age in zip(names, ages):
    print(name, age)
```

---

## 3️⃣ Multiple Iterables

`zip()` can combine three or more collections.

```python
for name, age, role in zip(names, ages, roles):
    print(name, age, role)
```

---

## 4️⃣ Different Lengths

`zip()` stops when the **shortest iterable** ends.

```python
names = ["Deven", "Rahul", "Amit"]
ages = [25, 30]

print(list(zip(names, ages)))
```

Only two pairs are produced.

---

## 5️⃣ `zip()` + `dict()`

Useful for creating dictionaries:

```python
skills = ["Python", "Java", "SQL"]
levels = ["Advanced", "Intermediate", "Beginner"]

result = dict(zip(skills, levels))
```

---

## 6️⃣ `zip()` + `enumerate()`

You can combine iteration tools:

```python
for index, (name, role) in enumerate(
    zip(names, roles),
    start=1
):
    print(index, name, role)
```

`zip()` pairs the values, while `enumerate()` adds an index.

---

# 🧠 Quick Reference

```text
zip(list1, list2)
        ↓
pairs corresponding items

list(zip(...))
        ↓
convert pairs to a list

dict(zip(keys, values))
        ↓
create a dictionary

enumerate(zip(...))
        ↓
index + paired values
```

---

## 🤖 GenAI Connection

`zip()` can be useful when processing related data such as:

```text
Documents
Scores
Metadata
```

For example:

```text
Document 1 → Score 1
Document 2 → Score 2
Document 3 → Score 3
```

This kind of paired data appears when processing API and retrieval results.

---

## ⚠️ Important

By default:

```text
Different lengths
       ↓
zip()
       ↓
Stops at the shortest iterable
```

---

## ✅ Practice Completed

- [x] Pair two lists
- [x] Pair three lists
- [x] Convert `zip()` to a list
- [x] Create a dictionary with `zip()`
- [x] Handle different lengths
- [x] Combine `zip()` with `enumerate()`
- [x] Process document + score data
