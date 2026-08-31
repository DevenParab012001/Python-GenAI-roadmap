# Python — JSON File Handling
# Practice Solutions

import json

# Q1 — Dictionary -> JSON string
user = {
    "name": "Deven",
    "age": 25,
    "role": "Software Engineer"
}

json_string = json.dumps(user)
print(json_string)


# Q2 — Pretty JSON
json_string = json.dumps(user, indent=4)
print(json_string)


# Q3 — JSON string -> Python dictionary
json_data = '{"name": "Deven", "age": 25, "role": "Developer"}'

user = json.loads(json_data)

print(user["name"])
print(user["role"])


# Q4 — Write JSON file
user = {
    "name": "Deven",
    "age": 25,
    "skills": ["Python", "Java", "SQL"],
    "learning": "Python + GenAI"
}

with open("profile.json", "w") as file:
    json.dump(user, file, indent=4)


# Q5 — Read JSON file
with open("profile.json", "r") as file:
    user = json.load(file)

print("Name:", user["name"])
print("Age:", user["age"])
print("Learning:", user["learning"])


# Q6 — Nested JSON
user = {
    "name": "Deven",
    "profile": {
        "role": "Software Engineer",
        "experience": 4
    },
    "skills": ["Python", "Java", "SQL"]
}

print("Role:", user["profile"]["role"])
print("Experience:", user["profile"]["experience"])
print("First Skill:", user["skills"][0])


# Q7 — Create users.json
users = [
    {
        "name": "Deven",
        "role": "Developer"
    },
    {
        "name": "Rahul",
        "role": "Tester"
    },
    {
        "name": "Amit",
        "role": "Manager"
    }
]

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)


# Q8 — Filter JSON data
with open("users.json", "r") as file:
    users = json.load(file)

for user in users:
    if user["role"] == "Developer":
        print(user["name"], "-", user["role"])


# Q9 — GenAI-style response JSON
response = {
    "answer": "Python is a programming language.",
    "confidence": 0.95,
    "sources": [
        "python-basics.txt",
        "python-guide.txt"
    ]
}

with open("response.json", "w") as file:
    json.dump(response, file, indent=4)

with open("response.json", "r") as file:
    response = json.load(file)

print("Answer:", response["answer"])
print("Confidence:", response["confidence"])
print("Sources:")

for source in response["sources"]:
    print("-", source)


# Q10 — Filter documents by score
documents = [
    {
        "id": 1,
        "text": "Python is a programming language.",
        "score": 0.95
    },
    {
        "id": 2,
        "text": "FastAPI is a Python framework.",
        "score": 0.87
    },
    {
        "id": 3,
        "text": "RAG combines retrieval and generation.",
        "score": 0.72
    }
]

with open("documents.json", "w") as file:
    json.dump(documents, file, indent=4)

with open("documents.json", "r") as file:
    documents = json.load(file)

for document in documents:
    if document["score"] >= 0.90:
        print(document["text"], "-", document["score"])
