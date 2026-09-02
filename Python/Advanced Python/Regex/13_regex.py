import re

# 1. re.search() - find a pattern
text = "I am learning Python"
result = re.search(r"Python", text)
if result:
    print("Python found")

# 2. re.findall() - find all numbers
text = "I have 4 years of experience and worked on 12 projects."
result = re.findall(r"\d+", text)
print(result)

# 3. \w+ - find word characters
text = "Python Java FastAPI"
result = re.findall(r"\w+", text)
print(result)

# 4. re.sub() - replace text
text = "Python is difficult"
result = re.sub(r"difficult", "powerful", text)
print(result)

# 5. ^ and $ - start and end of string
text = "Python is awesome"
result_start = re.search(r"^Python", text)
result_end = re.search(r"Python$", text)
if result_start:
    print("Starts with Python")
if result_end:
    print("Ends with Python")

# 6. Extract a number
text = "Deven has 4 years of experience"
result = re.findall(r"\d+", text)
print(result)

# 7. Extract email addresses
text = """
Contact deven@example.com
For support contact support@company.com
"""
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)

# 8. Groups - extract name and age
text = "Name: Deven, Age: 25"
result = re.search(r"Name: (\w+), Age: (\d+)", text)
if result:
    print(result.group(1))
    print(result.group(2))

# 9. Remove special characters
text = "Python!!! is @awesome### for GenAI!!!"
result = re.sub(r"[^\w\s]", "", text)
print(result)

# 10. Extract digits from document scores
# Note: \d+ treats decimal parts separately.
text = """
Document 1 scored 0.95
Document 2 scored 0.87
Document 3 scored 0.72
"""
result = re.findall(r"\d+", text)
print(result)
