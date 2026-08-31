# Python — CSV File Handling
# Practice Solutions

import csv

# Q1
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "role"])
    writer.writerow(["Deven", 25, "Developer"])
    writer.writerow(["Rahul", 30, "Tester"])
    writer.writerow(["Amit", 28, "Manager"])

# Q2
with open("employees.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Q3
with open("employees.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# Q4
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} - {row['role']}")

# Q5
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for employee in reader:
        if employee["role"] == "Developer":
            print(employee)

# Q6
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for employee in reader:
        age = int(employee["age"])
        if age >= 25:
            print(employee)

# Q7
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    with open("developers.csv", "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["name", "age", "role"])
        writer.writeheader()
        for employee in reader:
            if employee["role"] == "Developer":
                writer.writerow(employee)

# Q8
with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "price", "category"])
    writer.writerow(["Laptop", 70000, "Electronics"])
    writer.writerow(["Mouse", 1500, "Electronics"])
    writer.writerow(["Chair", 5000, "Furniture"])
    writer.writerow(["Monitor", 15000, "Electronics"])

with open("products.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for product in reader:
        if product["category"] == "Electronics":
            print(product)

# Q9
with open("documents.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "text", "score"])
    writer.writerow([1, "Python is a programming language.", 0.95])
    writer.writerow([2, "FastAPI is a Python framework.", 0.87])
    writer.writerow([3, "RAG combines retrieval and generation.", 0.72])

with open("documents.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for document in reader:
        print(f"Score: {document['score']} → {document['text']}")
