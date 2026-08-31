# Python — zip()
# Practice Solutions

# Q1 — Three Lists
names = ["Deven", "Rahul", "Amit"]
roles = ["Developer", "Tester", "Manager"]
departments = ["IT", "QA", "HR"]

result = zip(names, roles, departments)
print(list(result))


# Q2 — Names and Ages
names = ["Deven", "Rahul", "Amit"]
ages = [25, 30, 28]

result = zip(names, ages)
print(list(result))


# Q3 — Create a Dictionary
skills = ["Python", "Java", "SQL"]
levels = ["Advanced", "Intermediate", "Beginner"]

result = zip(skills, levels)
print(dict(result))


# Q4 — Different Lengths
names = ["Deven", "Rahul", "Amit", "Neha"]
scores = [90, 85]

result = zip(names, scores)
print(list(result))


# Q5 — enumerate() + zip()
products = ["Laptop", "Mouse", "Keyboard"]
prices = [70000, 1500, 3000]

for index, (product, price) in enumerate(zip(products, prices), start=1):
    print(f"{index}. {product} - {price}")


# Q6 — Users and Skills
users = ["Deven", "Rahul", "Amit"]

skills = [
    ["Python", "Java"],
    ["React", "JavaScript"],
    ["Java", "Docker"]
]

result = zip(users, skills)
print(list(result))


# Q7 — GenAI-style Data
documents = [
    "Python is a programming language.",
    "FastAPI is a Python web framework.",
    "RAG combines retrieval with generation."
]

scores = [0.95, 0.87, 0.72]

for document, score in zip(documents, scores):
    print(f"Score: {score} -> {document}")
