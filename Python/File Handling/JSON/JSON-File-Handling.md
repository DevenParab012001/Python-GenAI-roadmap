# 🗂️ Python — JSON File Handling

> **Python + GenAI Roadmap**  
> Reading, writing, converting, and processing JSON data.

---

## 1️⃣ JSON

JSON = **JavaScript Object Notation**.

It is commonly used to store and exchange structured data.

Example:

```json
{
    "name": "Deven",
    "age": 25,
    "skills": ["Python", "Java"]
}
```

---

## 2️⃣ Python `json` Module

Python provides a built-in `json` module:

```python
import json
```

No installation is required.

---

## 3️⃣ `dumps()` — Python → JSON String

```python
json_string = json.dumps(user)
```

With formatting:

```python
json_string = json.dumps(user, indent=4)
```

---

## 4️⃣ `loads()` — JSON String → Python Object

```python
user = json.loads(json_string)
```

---

## 5️⃣ `dump()` — Python → JSON File

```python
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)
```

---

## 6️⃣ `load()` — JSON File → Python Object

```python
with open("user.json", "r") as file:
    user = json.load(file)
```

---

## 🧠 The Four Functions

```text
dump()   → Python object → JSON file
dumps()  → Python object → JSON string

load()   → JSON file → Python object
loads()  → JSON string → Python object
```

### Easy Memory Trick

```text
"s" = string
```

So:

```text
dump  = file
dumps = string

load  = file
loads = string
```

---

## 7️⃣ Nested JSON

JSON can contain nested objects and arrays.

```python
user = {
    "name": "Deven",
    "profile": {
        "role": "Software Engineer",
        "experience": 4
    },
    "skills": ["Python", "Java"]
}
```

Access nested data:

```python
user["profile"]["role"]
```

---

## 8️⃣ JSON List of Objects

A very common API structure:

```json
[
    {
        "name": "Deven",
        "role": "Developer"
    },
    {
        "name": "Rahul",
        "role": "Tester"
    }
]
```

In Python, this becomes:

```text
list → dictionaries → values
```

---

## 9️⃣ JSON + APIs

APIs commonly exchange JSON data:

```text
API
 ↓
JSON
 ↓
Python dictionary / list
 ↓
Application logic
```

---

## 🤖 JSON + GenAI

JSON is heavily used with GenAI applications.

For example:

```json
{
    "answer": "Python is a programming language.",
    "confidence": 0.95,
    "sources": [
        "document1",
        "document2"
    ]
}
```

Typical flow:

```text
LLM / API
   ↓
JSON response
   ↓
Python object
   ↓
Application logic
```

---

# 🧠 Quick Reference

```text
json.dumps()
→ Python → JSON string

json.loads()
→ JSON string → Python

json.dump()
→ Python → JSON file

json.load()
→ JSON file → Python
```

---

## ⚠️ Important

JSON objects become Python dictionaries.

JSON arrays become Python lists.

JSON values can include:

```text
string
number
boolean
null
object
array
```

---

## ✅ Practice Completed

- [x] `json.dumps()`
- [x] Pretty JSON with `indent=4`
- [x] `json.loads()`
- [x] `json.dump()`
- [x] `json.load()`
- [x] Nested JSON
- [x] Lists of JSON objects
- [x] JSON filtering
- [x] GenAI-style JSON responses
