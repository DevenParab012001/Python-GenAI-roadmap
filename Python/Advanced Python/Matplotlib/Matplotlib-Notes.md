# 📊 Matplotlib — Handwritten Notes

## 1. What is Matplotlib?

Matplotlib is a Python library used to create data visualizations and charts.

```python
import matplotlib.pyplot as plt
```

---

## 2. Line Plot

Used for showing trends or changes across ordered values.

```python
plt.plot(days, temperature)
```

Example:

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 33, 34]

plt.plot(days, temperature)
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weekly Temperature")
plt.show()
```

---

## 3. Bar Chart

Used for comparing categories.

```python
plt.bar(products, sales)
```

Example:

```python
products = ["Laptop", "Phone", "Tablet"]
sales = [50, 80, 40]

plt.bar(products, sales)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()
```

---

## 4. Scatter Plot

Used to show the relationship between two numerical variables.

```python
plt.scatter(x, y)
```

Example:

```python
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 60, 65, 75, 85]

plt.scatter(hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
```

---

## 5. Histogram

Used to show the distribution/frequency of numerical values.

```python
plt.hist(data)
```

Example:

```python
marks = [45, 50, 55, 60, 62, 65, 68, 70,
         72, 75, 80, 85, 90, 95]

plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()
```

---

## 6. Labels and Title

X-axis:

```python
plt.xlabel("Month")
```

Y-axis:

```python
plt.ylabel("Sales")
```

Title:

```python
plt.title("Monthly Sales")
```

Display:

```python
plt.show()
```

---

## 7. Pandas + Matplotlib

Pandas can provide the data and Matplotlib can visualize it.

```python
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 130, 180, 200]
})

plt.plot(sales["Month"], sales["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
```

Think:

```text
Pandas
  ↓
DataFrame
  ↓
Select columns
  ↓
Matplotlib
  ↓
Chart
```

---

## 🧠 Quick Revision

| Chart | Function | Main Use |
|---|---|---|
| Line | `plt.plot()` | Trends |
| Bar | `plt.bar()` | Category comparison |
| Scatter | `plt.scatter()` | Relationship |
| Histogram | `plt.hist()` | Distribution |

Common commands:

```python
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Chart Title")
plt.show()
```

## Matplotlib Roadmap Status

Completed:

- Line plots
- Bar charts
- Scatter plots
- Histograms
- Chart labels
- Chart titles
- Pandas + Matplotlib visualization
