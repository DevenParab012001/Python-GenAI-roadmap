# Python Collections — Practice Solutions

# Question 1 — List Manipulation
skills = ["Java", "Spring Boot", "SQL", "React"]
skills.append("Python")
skills.insert(2, "FastAPI")
skills[4] = "TypeScript"
skills.remove("SQL")

print("Q1:", skills)
print("Number of skills:", len(skills))


# Question 2 — List Slicing
technologies = [
    "Java",
    "Python",
    "React",
    "FastAPI",
    "Docker",
    "PostgreSQL"
]

print("\nQ2 — First 3:", technologies[:3])
print("Q2 — Last 2:", technologies[-2:])
print("Q2 — Every second:", technologies[::2])
print("Q2 — Reversed:", technologies[::-1])


# Question 3 — Tuple Unpacking
employee = ("Deven", "Software Engineer", 4)
name, role, experience = employee

print(f"\nQ3 — Name: {name}")
print(f"Q3 — Role: {role}")
print(f"Q3 — Experience: {experience} years")


# Question 4 — Set Operations
backend = {"Java", "Python", "SQL", "Docker"}
ai = {"Python", "RAG", "Docker", "LLM"}

print("\nQ4 — All technologies:", backend | ai)
print("Q4 — Common technologies:", backend & ai)
print("Q4 — Backend only:", backend - ai)
print("Q4 — AI only:", ai - backend)


# Question 5 — Dictionary
developer = {
    "name": "Deven",
    "age": 25,
    "role": "Associate Software Engineer",
    "skills": ["Java", "SQL", "React"]
}

developer["skills"].append("Python")
developer["skills"].append("GenAI")
developer["role"] = "Python GenAI Engineer"
developer["experience"] = 4

print("\nQ5 — Name:", developer["name"])
print("Q5 — Skills:", developer["skills"])

for key, value in developer.items():
    print(f"{key}: {value}")


# Question 6 — Nested Data
company = {
    "name": "TechCorp",
    "employees": [
        {
            "name": "Deven",
            "role": "Developer",
            "skills": ["Python", "Java"]
        },
        {
            "name": "Rahul",
            "role": "Developer",
            "skills": ["React", "JavaScript"]
        }
    ]
}

print("\nQ6 — Company:", company["name"])
print("Q6 — Deven's role:", company["employees"][0]["role"])
print("Q6 — Deven's first skill:", company["employees"][0]["skills"][0])

company["employees"][0]["skills"].append("FastAPI")

print("Q6 — Updated Deven:", company["employees"][0])


# Question 7 — Practical Mini Challenge
users = [
    {"name": "Deven", "skills": ["Python", "Java", "SQL"]},
    {"name": "Rahul", "skills": ["Python", "React", "Docker"]},
    {"name": "Amit", "skills": ["Java", "Spring Boot", "Docker"]}
]

print("\nQ7 — Number of users:", len(users))
print("Q7 — Rahul's skills:", users[1]["skills"])

users[0]["skills"].append("FastAPI")

unique_skills = set()

for user in users:
    for skill in user["skills"]:
        unique_skills.add(skill)

print("Q7 — Unique skills:", unique_skills)
