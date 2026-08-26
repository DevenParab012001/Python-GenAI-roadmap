# Variables & Data Types — Practice

# Exercise 1 — Personal Profile
# Write your solution below.

name = "Deven"

age = 25

year_of_exp = "3 years 11 months"

salary = 530000

isLearningGenAI = True

print(f"My name is {name}")

print(f"I am {age} years old")

print(f"I have {year_of_exp} of experience")

print(f"My salar is {salary} rs")

print(f"Leaning GenAI ? {isLearningGenAI}")

print(type(name))

print(type(age))

print(type(year_of_exp))

print(type(salary))

print(type(isLearningGenAI))


# Exercise 2 — Skills
# Write your solution below.

skills = ["Java", "Spring Boot", "Python", "React", "Progress 4GL"]

print(skills[0])

skills.append("Javascript")

print(skills)

print(len(skills))


# Exercise 3 — User Profile
# Write your solution below.

user_info = {

    "name": "Deven Parab",

    "experience": "3 years 11 months",

    "role": "Associate SE",

    "skills": ["Java", "Spring Boot", "Python", "GenAI"],

    "isEmployed": True

}

print(user_info["name"])

print(user_info["skills"])

user_info["learning"] = "Python + GenAI"

user_info["role"] = "Software Engineer"

print(user_info)


# Exercise 4 — Mutable vs Immutable
# Write your solution below.

skills = ["Java", "Spring Boot", "Python", "React", "Progress 4GL"]

skills[3] = "Typescript"

print(skills)

name = "Python"

new_name = name[:2] + "X" + name[3:]

print(name)

print(new_name)


# Exercise 5 — Mini Challenge
# Write your solution below.

user = {

    "name": "Deven",

    "age": 25,

    "skills": ["Java", "SQL", "React"]

}

user["skills"].append("Python")

user["skills"].append("GenAI")

user["experience"] = 4

user["age"] = 26

print(user)
