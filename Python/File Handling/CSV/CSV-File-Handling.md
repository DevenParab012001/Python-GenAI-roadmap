# 📊 Python — CSV File Handling

> **Python + GenAI Roadmap**  
> Reading, writing, filtering, and processing CSV data.

---

## 1️⃣ CSV

CSV = **Comma-Separated Values**.

```text
name,age,role
Deven,25,Developer
Rahul,30,Tester
Amit,28,Manager
```

CSV represents tabular data.

---

## 2️⃣ `csv` Module

Python provides a built-in CSV module:

```python
import csv
```

No installation is required.

---

## 3️⃣ `csv.reader()`

Reads rows as lists:

```python
with open("employees.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

CSV values are read as **strings**.

---

## 4️⃣ Skip the Header

```python
next(reader)
```

`next(reader)` moves past the first row.

---

## 5️⃣ `csv.DictReader()`

Reads each row as a dictionary:

```python
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

Example:

```python
{
    "name": "Deven",
    "age": "25",
    "role": "Developer"
}
```

---

## 6️⃣ Type Conversion

CSV values are strings.

```python
age = int(row["age"])
```

Then numerical comparisons can be performed:

```python
if age >= 25:
    print(row["name"])
```

---

## 7️⃣ `csv.writer()`

Used to write list-based rows:

```python
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "role"])
    writer.writerow(["Deven", 25, "Developer"])
```

```text
writerow()  → one row
writerows() → multiple rows
```

---

## 8️⃣ `csv.DictWriter()`

Useful when data is already stored as dictionaries:

```python
fieldnames = ["name", "age", "role"]

writer = csv.DictWriter(
    file,
    fieldnames=fieldnames
)

writer.writeheader()
writer.writerows(employees)
```

---

## 9️⃣ Common Workflow

```text
CSV
 ↓
Read
 ↓
Python data
 ↓
Filter / transform / process
 ↓
Write output
```

---

## 🤖 GenAI Connection

CSV can be a source of structured data for GenAI applications:

```text
CSV
 ↓
Python
 ↓
Clean / process
 ↓
Documents / chunks
 ↓
Embeddings / retrieval
 ↓
LLM
```

CSV files can contain documents, metadata, IDs, scores, and other structured information.

---

# 🧠 Quick Reference

```text
csv.reader()
    → rows as lists

csv.DictReader()
    → rows as dictionaries

csv.writer()
    → write list-based rows

csv.DictWriter()
    → write dictionary-based rows

next(reader)
    → skip first row

newline=""
    → use when opening CSV for writing
```

---

## ⚠️ Important

```python
row["age"]
```

is a string when read from CSV.

For numerical operations:

```python
int(row["age"])
```

---

## ✅ Practice Completed

- [x] Create CSV
- [x] Read CSV
- [x] Skip header
- [x] `DictReader`
- [x] Filter rows
- [x] Type conversion
- [x] `DictWriter`
- [x] Create filtered CSV
- [x] Process structured document data
