import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# SECTION 1: LOAD DATA
# ============================================================

sales = pd.read_csv("retail_sales.csv")

print("=" * 60)
print("SECTION 1: LOAD DATA")
print("=" * 60)

print(sales)


# ============================================================
# SECTION 2: INSPECT DATA
# ============================================================

print("\n" + "=" * 60)
print("SECTION 2: INSPECT DATA")
print("=" * 60)

print("\nFirst 5 rows:")
print(sales.head())

print("\nLast 5 rows:")
print(sales.tail())

print("\nDataset shape:")
print(sales.shape)

print("\nColumn names:")
print(sales.columns)

print("\nDataset information:")
sales.info()

print("\nStatistical summary:")
print(sales.describe())


# ============================================================
# SECTION 3: CLEAN DATA
# ============================================================

print("\n" + "=" * 60)
print("SECTION 3: CLEAN DATA")
print("=" * 60)

# Check missing values
print("\nMissing values:")
print(sales.isnull().sum())

# Check duplicates
print("\nNumber of duplicate rows:")
print(sales.duplicated().sum())

# Display duplicate rows
print("\nDuplicate rows:")
print(sales[sales.duplicated()])

# Remove duplicates
sales = sales.drop_duplicates()

# Convert Date column to datetime
sales["Date"] = pd.to_datetime(sales["Date"])

# Check data types
print("\nData types after cleaning:")
print(sales.dtypes)

# Save cleaned dataset
sales.to_csv("retail_sales_cleaned.csv", index=False)

print("\nData cleaning completed!")


# ============================================================
# SECTION 4: FILTER & SORT
# ============================================================

print("\n" + "=" * 60)
print("SECTION 4: FILTER & SORT")
print("=" * 60)

# Sales above ₹50,000
high_sales = sales[sales["Sales"] > 50000]

print("\nSales above ₹50,000:")
print(high_sales)

# Laptop sales
laptop_sales = sales[sales["Product"] == "Laptop"]

print("\nLaptop sales:")
print(laptop_sales)

# Electronics sales
electronics_sales = sales[sales["Category"] == "Electronics"]

print("\nElectronics sales:")
print(electronics_sales)

# Electronics sales above ₹50,000
result = sales[
    (sales["Category"] == "Electronics") &
    (sales["Sales"] > 50000)
]

print("\nElectronics sales above ₹50,000:")
print(result)

# Sort by Sales - highest to lowest
sorted_sales = sales.sort_values(
    "Sales",
    ascending=False
)

print("\nSales sorted highest to lowest:")
print(sorted_sales)

# Sort by Quantity - highest to lowest
sorted_quantity = sales.sort_values(
    "Quantity",
    ascending=False
)

print("\nQuantity sorted highest to lowest:")
print(sorted_quantity)

# Top 5 sales
top_sales = sales.sort_values(
    "Sales",
    ascending=False
).head(5)

print("\nTop 5 sales:")
print(top_sales)


# ============================================================
# SECTION 5: GROUPBY ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("SECTION 5: GROUPBY ANALYSIS")
print("=" * 60)

# Total sales by product
total_sales_product = sales.groupby("Product")["Sales"].sum()

print("\nTotal sales by product:")
print(total_sales_product)

# Average sales by product
average_sales = sales.groupby("Product")["Sales"].mean()

print("\nAverage sales by product:")
print(average_sales)

# Total quantity sold by product
total_quantity = sales.groupby("Product")["Quantity"].sum()

print("\nTotal quantity sold by product:")
print(total_quantity)

# Total sales by category
category_sales = sales.groupby("Category")["Sales"].sum()

print("\nTotal sales by category:")
print(category_sales)

# Average price by category
average_price = sales.groupby("Category")["Price"].mean()

print("\nAverage price by category:")
print(average_price)

# Maximum sale by product
max_sales = sales.groupby("Product")["Sales"].max()

print("\nMaximum sale by product:")
print(max_sales)

# Product-wise sales summary
product_summary = sales.groupby("Product")["Sales"].agg([
    "sum",
    "mean",
    "min",
    "max"
])

print("\nProduct-wise sales summary:")
print(product_summary)


# ============================================================
# SECTION 6: PRODUCT & CATEGORY ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("SECTION 6: PRODUCT & CATEGORY ANALYSIS")
print("=" * 60)

# Best-selling product
best_product = total_sales_product.idxmax()
best_product_sales = total_sales_product.max()

print("\nBest-selling product:")
print(best_product)
print("Total sales:", best_product_sales)

# Lowest-selling product
lowest_product = total_sales_product.idxmin()
lowest_product_sales = total_sales_product.min()

print("\nLowest-selling product:")
print(lowest_product)
print("Total sales:", lowest_product_sales)

# Best category
best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("\nBest category:")
print(best_category)
print("Category sales:", best_category_sales)

# Lowest category
lowest_category = category_sales.idxmin()
lowest_category_sales = category_sales.min()

print("\nLowest category:")
print(lowest_category)
print("Category sales:", lowest_category_sales)

# Most units sold by product
most_units_product = total_quantity.idxmax()
most_units = total_quantity.max()

print("\nMost units sold:")
print(most_units_product)
print("Units:", most_units)

# Monthly sales
sales["Month"] = sales["Date"].dt.strftime("%b")

monthly_sales = sales.groupby("Month")["Sales"].sum()

print("\nMonthly sales:")
print(monthly_sales)

# Best month
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

print("\nBest month:")
print(best_month)
print("Sales:", best_month_sales)

# Product sales ranking
product_ranking = total_sales_product.sort_values(
    ascending=False
)

print("\nProduct sales ranking:")
print(product_ranking)


# ============================================================
# SECTION 7: MATPLOTLIB
# ============================================================

print("\n" + "=" * 60)
print("SECTION 7: MATPLOTLIB")
print("=" * 60)

# 1. Total Sales by Product

plt.figure(figsize=(8, 5))

plt.bar(
    total_sales_product.index,
    total_sales_product.values
)

plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# 2. Total Sales by Category

plt.figure(figsize=(7, 5))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Total Sales by Category")

plt.tight_layout()
plt.show()


# 3. Monthly Sales Trend

plt.figure(figsize=(8, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")

plt.tight_layout()
plt.show()


# ============================================================
# SECTION 8: SEABORN
# ============================================================

print("\n" + "=" * 60)
print("SECTION 8: SEABORN")
print("=" * 60)

# 1. Total Sales by Product

plt.figure(figsize=(8, 5))

sns.barplot(
    x=total_sales_product.index,
    y=total_sales_product.values
)

plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# 2. Total Sales by Category

plt.figure(figsize=(7, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Total Sales by Category")

plt.tight_layout()
plt.show()


# 3. Sales Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
    data=sales,
    x="Sales"
)

plt.xlabel("Sales")
plt.ylabel("Number of Transactions")
plt.title("Distribution of Sales")

plt.tight_layout()
plt.show()


# 4. Quantity vs Sales

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=sales,
    x="Quantity",
    y="Sales"
)

plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.title("Quantity vs Sales")

plt.tight_layout()
plt.show()


# 5. Monthly Sales

plt.figure(figsize=(8, 5))

sns.barplot(
    x=monthly_sales.index,
    y=monthly_sales.values
)

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales")

plt.tight_layout()
plt.show()


# ============================================================
# SECTION 9: FINAL BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("SECTION 9: FINAL BUSINESS INSIGHTS")
print("=" * 60)

# Total revenue
total_revenue = sales["Sales"].sum()

# Average transaction value
average_transaction = sales["Sales"].mean()

# Highest transaction
highest_transaction = sales.loc[
    sales["Sales"].idxmax()
]

# Electronics revenue percentage
electronics_percentage = (
    category_sales["Electronics"] /
    total_revenue
) * 100

print("\nTotal Revenue:")
print(f"₹{total_revenue:,.0f}")

print("\nAverage Transaction Value:")
print(f"₹{average_transaction:,.0f}")

print("\nHighest Single Transaction:")
print(f"₹{highest_transaction['Sales']:,.0f}")

print("Product:", highest_transaction["Product"])

print("\nBest-Selling Product:")
print(best_product)

print(f"Revenue: ₹{best_product_sales:,.0f}")

print("\nBest Category:")
print(best_category)

print(f"Revenue: ₹{best_category_sales:,.0f}")

print("\nElectronics Contribution:")
print(f"{electronics_percentage:.2f}% of total revenue")

print("\nProduct with Most Units Sold:")
print(most_units_product)

print(f"Units Sold: {most_units}")

print("\nBest Month:")
print(best_month)

print(f"Revenue: ₹{best_month_sales:,.0f}")


# ============================================================
# FINAL CONCLUSIONS
# ============================================================

print("\n" + "=" * 60)
print("FINAL CONCLUSIONS")
print("=" * 60)

print("""
1. Laptop generated the highest total revenue.

2. Electronics was the strongest category and contributed
   the majority of the company's total revenue.

3. Mouse had the highest number of units sold, but its
   contribution to revenue was relatively low because of
   its low selling price.

4. January was the strongest sales month in this dataset.

5. The business generated strong revenue from high-value
   Electronics products such as Laptops and Phones.

6. Quantity sold does not always determine revenue.
   Product price has a major impact on total revenue.
""")

print("\nRetail Sales EDA completed successfully!")