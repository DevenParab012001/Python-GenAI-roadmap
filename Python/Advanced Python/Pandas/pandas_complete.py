import pandas as pd

# Pandas complete roadmap practice

# 1. Series
numbers = pd.Series([15, 25, 35, 45, 55])
print("Series:")
print(numbers)
print("First:", numbers.iloc[0])
print("Last:", numbers.iloc[-1])

# 2. DataFrame
students = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Karan"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 72, 91, 68, 78],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
})
print("\nDataFrame:")
print(students)
print("\nSelected columns:")
print(students[["Name", "Marks"]])

# 3. CSV
students.to_csv("students.csv", index=False)
print("\nCSV:")
print(pd.read_csv("students.csv"))

# 4. Excel
# Requires: python -m pip install openpyxl
students.to_excel("students.xlsx", index=False)
print("\nExcel:")
print(pd.read_excel("students.xlsx"))

# 5. JSON
students.to_json("students.json", orient="records", indent=4)
print("\nJSON:")
print(pd.read_json("students.json"))

# 6. Missing values
cleaning_df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Sneha"],
    "Age": [20, None, 21, None],
    "Marks": [85, 72, None, 68]
})
print("\nMissing values:")
print(cleaning_df.isnull().sum())

filled_df = cleaning_df.copy()
filled_df["Age"] = filled_df["Age"].fillna(20)
filled_df["Marks"] = filled_df["Marks"].fillna(0)
print("\nFilled missing values:")
print(filled_df)

print("\nDropped missing rows:")
print(cleaning_df.dropna())

# 7. Duplicates
duplicate_df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Amit", "Priya", "Rahul"],
    "Marks": [85, 72, 85, 91, 72]
})
print("\nDuplicates:")
print(duplicate_df.duplicated())
print("\nAfter removing duplicates:")
print(duplicate_df.drop_duplicates())

# 8. Type casting
types_df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": ["20", "21", "22"],
    "Marks": ["85", "72", "91"]
})
types_df["Age"] = types_df["Age"].astype(int)
types_df["Marks"] = types_df["Marks"].astype(float)
print("\nType casting:")
print(types_df)
print(types_df.dtypes)

# 9. Filtering
print("\nMarks >= 80:")
print(students[students["Marks"] >= 80])

print("\nMarks between 70 and 85:")
print(students[(students["Marks"] >= 70) & (students["Marks"] <= 85)])

# 10. Conditional selection
employees = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Karan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
})
print("\nIT employees:")
print(employees[employees["Department"] == "IT"])

# 11. Sorting
print("\nSorted by marks descending:")
print(students.sort_values("Marks", ascending=False))

print("\nSorted by age ascending:")
print(students.sort_values("Age", ascending=True))

# 12. groupby and aggregation
print("\nAverage salary:")
print(employees.groupby("Department")["Salary"].mean())

print("\nTotal salary:")
print(employees.groupby("Department")["Salary"].sum())

print("\nMaximum salary:")
print(employees.groupby("Department")["Salary"].max())

print("\nSalary summary:")
print(employees.groupby("Department")["Salary"].agg(["sum", "mean", "min", "max"]))

# 13. Feature preparation
feature_df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya", "Sneha"],
    "Age": [20, 21, 20, 22],
    "Marks": [85, 72, 91, 68]
})
feature_df["Passed"] = feature_df["Marks"] >= 40
features = feature_df[["Age", "Marks"]]
print("\nPrepared data:")
print(feature_df)
print("\nFeatures:")
print(features)
