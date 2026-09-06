# Project 5 — Retail Sales Data EDA

## Project Goal

Perform Exploratory Data Analysis (EDA) on a retail sales dataset using:
- Pandas
- Matplotlib
- Seaborn

## 1. Load Data

```python
import pandas as pd

sales = pd.read_csv("retail_sales_cleaned.csv")
sales["Date"] = pd.to_datetime(sales["Date"])
```

## 2. Filter & Sort

### Sales above ₹50,000
```python
high_sales = sales[sales["Sales"] > 50000]
```

### Laptop sales
```python
laptop_sales = sales[sales["Product"] == "Laptop"]
```

### Electronics sales
```python
electronics_sales = sales[sales["Category"] == "Electronics"]
```

### Electronics with sales above ₹50,000
```python
result = sales[
    (sales["Category"] == "Electronics") &
    (sales["Sales"] > 50000)
]
```

### Sort by Sales
```python
sorted_sales = sales.sort_values("Sales", ascending=False)
```

### Sort by Quantity
```python
sorted_quantity = sales.sort_values("Quantity", ascending=False)
```

### Top 5 Sales
```python
top_sales = sales.sort_values("Sales", ascending=False).head(5)
```

## 3. GroupBy Analysis

### Total sales by product
```python
total_sales = sales.groupby("Product")["Sales"].sum()
```

### Average sales by product
```python
average_sales = sales.groupby("Product")["Sales"].mean()
```

### Total quantity sold by product
```python
total_quantity = sales.groupby("Product")["Quantity"].sum()
```

### Total sales by category
```python
category_sales = sales.groupby("Category")["Sales"].sum()
```

### Average price by category
```python
average_price = sales.groupby("Category")["Price"].mean()
```

### Maximum sale by product
```python
max_sales = sales.groupby("Product")["Sales"].max()
```

### Product-wise summary
```python
product_summary = sales.groupby("Product")["Sales"].agg([
    "sum", "mean", "min", "max"
])
```

## 4. Product & Category Analysis

### Best-selling product
```python
best_product = total_sales_product.idxmax()
best_sales = total_sales_product.max()
```

### Lowest-selling product
```python
lowest_product = total_sales_product.idxmin()
lowest_sales = total_sales_product.min()
```

### Best category
```python
best_category = category_sales.idxmax()
best_category_sales = category_sales.max()
```

### Lowest category
```python
lowest_category = category_sales.idxmin()
lowest_category_sales = category_sales.min()
```

### Most units sold by product
```python
quantity_by_product = sales.groupby("Product")["Quantity"].sum()

most_units_product = quantity_by_product.idxmax()
most_units = quantity_by_product.max()
```

### Monthly sales
```python
sales["Month"] = sales["Date"].dt.strftime("%b")
monthly_sales = sales.groupby("Month")["Sales"].sum()
```

### Best month
```python
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()
```

### Product sales ranking
```python
product_ranking = sales.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
)
```

## 5. Matplotlib

### Total Sales by Product
```python
plt.bar(total_sales_product.index, total_sales_product.values)
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Total Sales by Category
```python
plt.bar(category_sales.index, category_sales.values)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Total Sales by Category")
plt.tight_layout()
plt.show()
```

### Monthly Sales Trend
```python
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.show()
```

## 6. Seaborn

### Total Sales by Product
```python
sns.barplot(
    x=total_sales_product.index,
    y=total_sales_product.values
)
```

### Total Sales by Category
```python
sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)
```

### Sales Distribution
```python
sns.histplot(data=sales, x="Sales")
```

### Quantity vs Sales
```python
sns.scatterplot(
    data=sales,
    x="Quantity",
    y="Sales"
)
```

### Monthly Sales
```python
sns.barplot(
    x=monthly_sales.index,
    y=monthly_sales.values
)
```

## 7. Quick EDA Patterns

### Filtering
```python
df[df["Column"] > value]
```

### Multiple conditions
```python
df[(df["Column1"] == value) & (df["Column2"] > value)]
```

### Sorting
```python
df.sort_values("Column", ascending=False)
```

### Top N
```python
df.sort_values("Column", ascending=False).head(5)
```

### GroupBy
```python
df.groupby("Column")["Value"].sum()
```

### Multiple aggregations
```python
df.groupby("Column")["Value"].agg(["sum", "mean", "min", "max"])
```

### Highest / lowest group
```python
grouped.idxmax()
grouped.max()

grouped.idxmin()
grouped.min()
```

## Project Flow

```text
CSV Dataset
    ↓
Load with Pandas
    ↓
Convert Date
    ↓
Filter & Sort
    ↓
GroupBy & Aggregation
    ↓
Product / Category Analysis
    ↓
Matplotlib
    ↓
Seaborn
    ↓
EDA Insights
```

## Completion

**Pandas → Matplotlib → Seaborn → Retail Sales EDA**
