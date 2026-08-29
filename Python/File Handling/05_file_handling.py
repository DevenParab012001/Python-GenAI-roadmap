# Python — File Handling
# Practice Solutions

from pathlib import Path

# Q1
with open("profile.txt", "w", encoding="utf-8") as file:
    file.write("Name: Deven\n")
    file.write("Role: Software Engineer\n")
    file.write("Learning: Python + GenAI\n")

# Q2
with open("profile.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

# Q3
with open("profile.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")

# Q4
with open("profile.txt", "a", encoding="utf-8") as file:
    file.write("Experience: 4 years\n")

with open("profile.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print(contents)

# Q5
with open("skills.txt", "w", encoding="utf-8") as file:
    file.write("Python\nJava\nSQL\nReact\nDocker\nFastAPI\n")

with open("skills.txt", "r", encoding="utf-8") as file:
    skills = file.readlines()
print("Number of skills:", len(skills))

# Q6
skill = input("Enter a skill: ").strip()

with open("skills.txt", "r", encoding="utf-8") as file:
    skills = file.readlines()

found = False
for line in skills:
    if line.strip() == skill:
        found = True
        break

if found:
    print(f"{skill} found")
else:
    print(f"{skill} not found")

# Q7
file_path = Path("skills.txt")
print("File exists:", file_path.exists())
print(file_path.read_text(encoding="utf-8"))

# Q8
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

# Q9
documents_path = Path("documents")
txt_files = documents_path.glob("*.txt")

for file_path in txt_files:
    print("Filename:", file_path.name)
    print("Contents:")
    print(file_path.read_text(encoding="utf-8"))
    print("-" * 40)
