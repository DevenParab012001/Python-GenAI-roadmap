# Python — Conditionals & Loops
# Practice Solutions

# Q1 — Grade Calculator
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Q2 — Login Check
username = "deven"
password = "python123"

entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

if username == entered_username and password == entered_password:
    print("Login successful")
else:
    print("Invalid username or password")


# Q3 — Skill Search
skills = ["Java", "Python", "SQL", "React", "Docker"]

if "Python" in skills:
    print("Python exists in the skills")
else:
    print("Python does not exist in the skills")

if "FastAPI" in skills:
    print("FastAPI exists in the skills")
else:
    print("FastAPI does not exist in the skills")


# Q4 — Number Classification
numbers = [10, 15, 22, 31, 40, 55]

for number in numbers:
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


# Q5 — Find the First Match
numbers = [12, 7, 25, 18, 30, 9]

for number in numbers:
    if number > 20:
        print(number)
        break


# Q6 — Skip Values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)


# Q7 — Enumerate
skills = ["Python", "FastAPI", "PostgreSQL", "Docker"]

for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")


# Q8 — Nested Data
users = [
    {
        "name": "Deven",
        "skills": ["Python", "Java"]
    },
    {
        "name": "Rahul",
        "skills": ["React", "JavaScript"]
    },
    {
        "name": "Amit",
        "skills": ["Java", "Docker"]
    }
]

for user in users:
    for skill in user["skills"]:
        print(f"{user['name']} knows {skill}")


# Q9 — Mini Challenge
users = [
    {
        "name": "Deven",
        "skills": ["Python", "Java", "SQL"]
    },
    {
        "name": "Rahul",
        "skills": ["Python", "React", "Docker"]
    },
    {
        "name": "Amit",
        "skills": ["Java", "Spring Boot", "Docker"]
    }
]

for user in users:
    print(user["name"])

    for skill in user["skills"]:
        print(f"  {skill}")

    if "Python" in user["skills"]:
        print(f"{user['name']} knows Python")
    else:
        print(f"{user['name']} does not know Python")
