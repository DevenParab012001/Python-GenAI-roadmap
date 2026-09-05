import matplotlib.pyplot as plt

# Matplotlib practice

# 1. Line plot
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 33, 34]
plt.plot(days, temperature)
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weekly Temperature")
plt.show()

# 2. Bar chart
products = ["Laptop", "Phone", "Tablet", "Watch"]
sales = [25, 40, 20, 30]
plt.bar(products, sales)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()

# 3. Scatter plot
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 60, 65, 75, 85]
plt.scatter(hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# 4. Histogram
marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75, 80, 85, 90, 95]
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()

# 5. Pandas + Matplotlib
import pandas as pd

sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 130, 180, 200]
})
plt.plot(sales["Month"], sales["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
