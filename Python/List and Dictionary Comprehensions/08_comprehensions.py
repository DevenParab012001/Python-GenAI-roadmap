# Python — List & Dictionary Comprehensions
# Practice Solutions

# ------------------------------------------------------------
# Q1 — Square Numbers
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# ------------------------------------------------------------
# Q2 — Even Numbers
# ------------------------------------------------------------

numbers = [10, 15, 22, 31, 40, 55]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# ------------------------------------------------------------
# Q3 — Transform Strings
# ------------------------------------------------------------

skills = ["python", "java", "docker", "fastapi"]

upper_skills = [skill.upper() for skill in skills]

print(upper_skills)


# ------------------------------------------------------------
# Q4 — Filter Skills
# ------------------------------------------------------------

skills = ["Python", "Java", "Python", "React", "Python"]

python_skills = [skill for skill in skills if skill == "Python"]

print(python_skills)


# ------------------------------------------------------------
# Q5 — if/else Expression
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)


# ------------------------------------------------------------
# Q6 — Dictionary Comprehension
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ------------------------------------------------------------
# Q7 — Filter Dictionary
# ------------------------------------------------------------

users = {
    "Deven": 25,
    "Rahul": 17,
    "Amit": 30,
    "Neha": 16
}

adults = {
    name: age
    for name, age in users.items()
    if age >= 18
}

print(adults)


# ------------------------------------------------------------
# Q8 — Nested Data
# ------------------------------------------------------------

users = [
    {
        "name": "Deven",
        "skills": ["Python", "Java", "SQL"]
    },
    {
        "name": "Rahul",
        "skills": ["React", "JavaScript"]
    },
    {
        "name": "Amit",
        "skills": ["Python", "Docker"]
    }
]

names = [
    user["name"]
    for user in users
    if "Python" in user["skills"]
]

print(names)


# ------------------------------------------------------------
# Q9 — Mini Challenge
# ------------------------------------------------------------

products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Mouse", "price": 1500},
    {"name": "Keyboard", "price": 3000},
    {"name": "Monitor", "price": 15000}
]

result = [
    product["name"]
    for product in products
    if product["price"] > 5000
]

print(result)
