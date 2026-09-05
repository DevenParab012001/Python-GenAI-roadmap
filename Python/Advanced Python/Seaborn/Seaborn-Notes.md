# Seaborn — Handwritten Notes

## 1. What is Seaborn?

Seaborn is a Python visualization library built on top of Matplotlib.

It makes statistical and DataFrame-based plots easier to create.

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

## 2. Bar Plot

Used to compare values across categories.

```python
sns.barplot(data=df, x="Category", y="Value")
plt.show()
```

Example:

```python
sns.barplot(data=sales, x="Product", y="Sales")
```

---

## 3. Scatter Plot

Used to show the relationship between two numerical variables.

```python
sns.scatterplot(data=df, x="Hours", y="Marks")
plt.show()
```

Example:

```python
sns.scatterplot(data=students, x="Hours", y="Marks")
```

---

## 4. Histogram

Used to see the distribution of numerical data.

```python
sns.histplot(data=df, x="Marks", bins=5)
plt.show()
```

`bins` controls the number of intervals.

---

## 5. Box Plot

Used to visualize the distribution of numerical data.

```python
sns.boxplot(data=df, x="Marks")
plt.show()
```

---

## 6. Count Plot

Used to count how many observations belong to each category.

```python
sns.countplot(data=df, x="Department")
plt.show()
```

---

## 7. Pandas + Seaborn

Seaborn works very well with Pandas DataFrames.

Example:

```python
average_salary = employees.groupby("Department")["Salary"].mean()

sns.barplot(
    x=average_salary.index,
    y=average_salary.values
)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()
```

---

## 8. Common Seaborn Functions

| Function | Use |
|---|---|
| `sns.barplot()` | Compare categories |
| `sns.scatterplot()` | Relationship between variables |
| `sns.histplot()` | Data distribution |
| `sns.boxplot()` | Distribution/spread |
| `sns.countplot()` | Count categories |

---

## 9. Basic Pattern

Most Seaborn plots follow this pattern:

```python
sns.plot_function(
    data=df,
    x="column1",
    y="column2"
)

plt.title("Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()
```

---

## 10. Installation

If Seaborn is not installed:

```bash
python -m pip install seaborn
```

If using a specific Python installation:

```bash
"C:\Program Files\Python313\python.exe" -m pip install seaborn
```

---

## Quick Revision

- **Bar plot** → compare categories
- **Scatter plot** → relationship between two numerical variables
- **Histogram** → distribution
- **Box plot** → distribution/spread
- **Count plot** → category counts
- **Pandas + Seaborn** → useful for data analysis and EDA
