# Python — Functions
# Practice Solutions

# Q1 — Simple Function
def greet(name):
    print(f"Hello {name}")

greet("Deven")


# Q2 — Return a Value
def calculate_sum(a, b):
    return a + b

total = calculate_sum(10, 20)
print(total)


# Q3 — User Information
def get_user_info(name, age, role):
    return {
        "name": name,
        "age": age,
        "role": role
    }

user = get_user_info("Deven", 25, "Software Engineer")
print(user)


# Q4 — Default Parameter
def greet(name, message="Hello"):
    print(f"{message} {name}")

greet("Deven")
greet("Deven", "Welcome")


# Q5 — Function + List
skills = ["Python", "Java", "SQL", "React"]

def find_skill(skills, skill):
    if skill in skills:
        return True
    else:
        return False

print(find_skill(skills, "Python"))
print(find_skill(skills, "FastAPI"))


# Q6 — Function + Dictionary
user = {
    "name": "Deven",
    "age": 25,
    "skills": ["Python", "Java", "SQL"]
}

def has_skill(user, skill):
    if skill in user["skills"]:
        return True
    else:
        return False

print(has_skill(user, "Python"))
print(has_skill(user, "React"))


# Q7 — *args
def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(calculate_total(10, 20, 30))
print(calculate_total(5, 10))
print(calculate_total(1, 2, 3, 4, 5))


# Q8 — **kwargs
def create_profile(**details):
    return details

profile = create_profile(
    name="Deven",
    age=25,
    role="Software Engineer",
    learning="Python + GenAI"
)

print(profile)


# Q9 — Practical Mini Challenge
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

def find_users_with_skill(users, skill):
    result = []

    for user in users:
        if skill in user["skills"]:
            result.append(user)

    return result

print(find_users_with_skill(users, "Python"))
print(find_users_with_skill(users, "Docker"))
print(find_users_with_skill(users, "FastAPI"))
