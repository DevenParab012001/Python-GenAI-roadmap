# 📂 Python — File Handling

> **Python + GenAI Roadmap**  
> Reading, writing, appending, and discovering files.

---

## 🧭 Core Concepts

| Concept | Purpose |
|---|---|
| `open()` | Open a file |
| `"r"` | Read |
| `"w"` | Write / overwrite |
| `"a"` | Append |
| `"x"` | Create |
| `read()` | Read all content |
| `readline()` | Read one line |
| `readlines()` | Read all lines |
| `write()` | Write content |
| `Path` | Work with paths |
| `glob()` | Find matching files |

---

## 1️⃣ Opening Files

Preferred pattern:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

`with` automatically closes the file.

---

## 2️⃣ File Modes

```text
"r" → Read
"w" → Write / overwrite
"a" → Append
"x" → Create new file
```

⚠️ `"w"` overwrites existing content.

---

## 3️⃣ Reading

```python
file.read()       # Entire content
file.readline()   # One line
file.readlines()  # List of lines
```

Line-by-line:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

---

## 4️⃣ Writing

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\n")
```

---

## 5️⃣ Appending

```python
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("New line\n")
```

Existing content is preserved.

---

## 6️⃣ `pathlib`

```python
from pathlib import Path

file_path = Path("data.txt")
```

Useful methods:

```python
file_path.exists()
file_path.is_file()
file_path.read_text(encoding="utf-8")
file_path.write_text("Hello", encoding="utf-8")
```

---

## 7️⃣ Finding Files

```python
from pathlib import Path

documents = Path("documents")

for file_path in documents.glob("*.txt"):
    print(file_path.name)
```

```text
file_path.name → filename
file_path      → Path object
```

---

## 8️⃣ Handling Missing Files

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

---

## 🤖 GenAI Connection

File handling is an early part of document ingestion:

```text
Documents
    ↓
Find files
    ↓
Read content
    ↓
Extract text
    ↓
Split into chunks
    ↓
Embeddings
    ↓
RAG
```

This will become directly useful when we build document-processing and RAG projects.

---

## 🧠 Quick Reference

```text
open()      → open files
"r"         → read
"w"         → overwrite
"a"         → append
read()      → entire content
readlines() → list of lines
write()     → write content
Path        → filesystem paths
glob()      → find matching files
```

---

## ✅ Practice Completed

- [x] Write a file
- [x] Read a file
- [x] Read line by line
- [x] Append content
- [x] Count lines
- [x] Search file content
- [x] Use `pathlib`
- [x] Handle missing files
- [x] Find multiple `.txt` files
