# 🐼 Pandas — Handwritten Notes

## 1. Pandas

Pandas is a Python library for working with structured/tabular data.

```python
import pandas as pd
```

Basic flow:

```text
CSV / Excel / JSON
        ↓
      Pandas
        ↓
    DataFrame
        ↓
Clean → Filter → Sort → Group → Prepare
```

## 2. Series

A Series is one-dimensional data.

```python
marks = pd.Series([80, 75, 90, 85])
```

Access by position:

```python
marks.iloc[0]
marks.iloc[-1]
```

## 3. DataFrame

A DataFrame is a table containing rows and columns.

```python
students = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": [20, 21, 20],
    "Marks": [85, 72, 91]
})
```

One column:

```python
students["Name"]
```

Multiple columns:

```python
students[["Name", "Marks"]]
```

## 4. Reading Data

CSV:

```python
df = pd.read_csv("students.csv")
```

Excel:

```python
df = pd.read_excel("students.xlsx")
```

JSON:

```python
df = pd.read_json("students.json")
```

For `.xlsx`, install the Excel engine:

```powershell
python -m pip install openpyxl
```

## 5. Writing Data

CSV:

```python
df.to_csv("output.csv", index=False)
```

Excel:

```python
df.to_excel("output.xlsx", index=False)
```

JSON:

```python
df.to_json("output.json", orient="records", indent=4)
```

`index=False` prevents the DataFrame index from being written as an extra column.

## 6. Missing Values

Detect:

```python
df.isnull()
df.isnull().sum()
```

Remove rows:

```python
df = df.dropna()
```

Fill values:

```python
df["Age"] = df["Age"].fillna(20)
```

## 7. Duplicates

Find duplicates:

```python
df.duplicated()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

## 8. Type Casting

Use `astype()`:

```python
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(float)
```

## 9. Filtering

Select rows using a condition:

```python
df[df["Marks"] >= 80]
```

Multiple conditions:

```python
df[
    (df["Marks"] >= 70) &
    (df["Marks"] <= 85)
]
```

OR:

```python
df[
    (df["Marks"] < 70) |
    (df["Marks"] > 90)
]
```

Text condition:

```python
df[df["Department"] == "IT"]
```

## 10. Sorting

Ascending:

```python
df.sort_values("Marks")
```

Descending:

```python
df.sort_values("Marks", ascending=False)
```

## 11. `groupby()`

Group rows by a column:

```python
employees.groupby("Department")["Salary"].mean()
```

This can calculate a department-wise average.

## 12. Aggregation

Common functions:

```python
.sum()
.mean()
.count()
.min()
.max()
```

Examples:

```python
employees.groupby("Department")["Salary"].sum()
employees.groupby("Department")["Salary"].mean()
employees.groupby("Department")["Salary"].max()
employees.groupby("Department")["Salary"].min()
```

Multiple aggregations:

```python
employees.groupby("Department")["Salary"].agg(
    ["sum", "mean", "min", "max"]
)
```

## 13. Feature Preparation for ML / GenAI Pipelines

Pandas can prepare cleaned and useful data for a later ML or GenAI pipeline.

Flow:

```text
Raw Data
   ↓
Clean Data
   ↓
Filter / Select
   ↓
Prepare Features
   ↓
ML / GenAI Pipeline
```

Example:

```python
data["Passed"] = data["Marks"] >= 40
features = data[["Age", "Marks"]]
```

## Quick Revision

| Task | Pandas |
|---|---|
| Series | `pd.Series()` |
| DataFrame | `pd.DataFrame()` |
| Read CSV | `pd.read_csv()` |
| Read Excel | `pd.read_excel()` |
| Read JSON | `pd.read_json()` |
| Write CSV | `df.to_csv()` |
| Write Excel | `df.to_excel()` |
| Write JSON | `df.to_json()` |
| Detect missing | `df.isnull()` |
| Remove missing | `df.dropna()` |
| Fill missing | `df.fillna()` |
| Find duplicates | `df.duplicated()` |
| Remove duplicates | `df.drop_duplicates()` |
| Type casting | `df.astype()` |
| Filtering | `df[condition]` |
| Sorting | `df.sort_values()` |
| Grouping | `df.groupby()` |
| Aggregation | `.sum()`, `.mean()`, `.min()`, `.max()` |
| Multiple aggregation | `.agg()` |

## Roadmap Status

Completed:

- Series and DataFrame
- CSV, Excel, JSON
- Missing values
- Duplicates
- Type casting
- Filtering
- Sorting
- Conditional selections
- `groupby()`
- Aggregation
- Feature preparation for ML/GenAI pipelines
