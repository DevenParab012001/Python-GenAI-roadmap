import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# 1. Bar Plot
# ---------------------------------

sales = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Sales": [60000, 30000, 20000, 55000, 35000]
})

sns.barplot(data=sales, x="Product", y="Sales")
plt.title("Sales by Product")
plt.show()


# ---------------------------------
# 2. Scatter Plot
# ---------------------------------

students = pd.DataFrame({
    "Hours": [2, 3, 4, 5, 6],
    "Marks": [45, 55, 65, 75, 85]
})

sns.scatterplot(data=students, x="Hours", y="Marks")
plt.title("Study Hours vs Marks")
plt.show()


# ---------------------------------
# 3. Histogram
# ---------------------------------

marks = pd.DataFrame({
    "Marks": [45, 55, 60, 62, 65, 70, 72, 75, 80, 85, 90, 95]
})

sns.histplot(data=marks, x="Marks", bins=5)
plt.title("Marks Distribution")
plt.show()


# ---------------------------------
# 4. Box Plot
# ---------------------------------

sns.boxplot(data=marks, x="Marks")
plt.title("Marks Distribution - Box Plot")
plt.show()


# ---------------------------------
# 5. Count Plot
# ---------------------------------

students = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Department": ["CS", "IT", "CS", "IT", "CS", "EXTC"]
})

sns.countplot(data=students, x="Department")
plt.title("Students by Department")
plt.show()


# ---------------------------------
# 6. Pandas + Seaborn
# ---------------------------------

employees = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Salary": [60000, 70000, 45000, 50000, 55000, 65000]
})

average_salary = employees.groupby("Department")["Salary"].mean()

sns.barplot(x=average_salary.index, y=average_salary.values)
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.show()


# ---------------------------------
# 7. Combined EDA Example
# ---------------------------------

sales = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Laptop"],
    "Category": ["Electronics"] * 6,
    "Sales": [60000, 30000, 55000, 20000, 35000, 65000]
})

total_sales = sales.groupby("Product")["Sales"].sum()

sns.barplot(x=total_sales.index, y=total_sales.values)
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.show()
