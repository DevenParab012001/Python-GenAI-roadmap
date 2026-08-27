# 🔀 Python — Conditionals & Loops

> **Python + GenAI Roadmap**  
> Short, practical reference for controlling program flow.

---

## 🧭 Core Concepts

| Concept | Purpose |
|---|---|
| `if / elif / else` | Make decisions |
| `for` | Iterate over data |
| `while` | Repeat while a condition is true |
| `break` | Exit a loop |
| `continue` | Skip the current iteration |
| `range()` | Generate number sequences |
| `enumerate()` | Get index + value |
| `in / not in` | Check membership |
| `and / or / not` | Combine or reverse conditions |

---

# 1. Conditional Statements

Used to execute different code depending on a condition.

```python
if condition:
    # code

elif condition:
    # code

else:
    # code
```

Example:

```python
marks = 78

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
else:
    grade = "C"
```

Python uses **indentation** to define code blocks.

---

## Comparison Operators

```text
==   Equal
!=   Not equal
>    Greater than
<    Less than
>=   Greater than or equal
<=   Less than or equal
```

Remember:

```text
=   → assignment
==  → comparison
```

---

# 2. Logical Operators

```text
and  → Both conditions must be True
or   → At least one condition must be True
not  → Reverses the result
```

Example:

```python
if age >= 18 and has_license:
    print("Can drive")
```

---

# 3. Membership Operators

Check whether a value exists in a collection.

```python
skills = ["Python", "Java", "SQL"]

if "Python" in skills:
    print("Python found")

if "React" not in skills:
    print("React not found")
```

---

# 4. `for` Loop

Used to iterate over a collection or sequence.

```python
skills = ["Python", "Java", "SQL"]

for skill in skills:
    print(skill)
```

Each iteration processes one element.

---

# 5. `range()`

Generates a sequence of numbers.

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 6)     # 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

The stop value is **excluded**.

Example:

```python
for i in range(5):
    print(i)
```

---

# 6. `while` Loop

Repeats while its condition is `True`.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

⚠️ Make sure the condition can eventually become `False` to avoid an infinite loop.

---

# 7. `break`

Immediately exits the loop.

```python
for number in numbers:
    if number > 20:
        break
```

Use it when you want to stop processing early.

---

# 8. `continue`

Skips the current iteration and moves to the next one.

```python
for number in numbers:
    if number % 2 == 0:
        continue

    print(number)
```

Here, even numbers are skipped.

---

# 9. `enumerate()`

Use it when you need both the **index and value**.

```python
skills = ["Python", "FastAPI", "Docker"]

for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")
```

Output:

```text
1. Python
2. FastAPI
3. Docker
```

---

# 10. Dictionary Iteration

### Keys

```python
for key in user:
    print(key)
```

### Values

```python
for value in user.values():
    print(value)
```

### Keys + Values

```python
for key, value in user.items():
    print(key, value)
```

`.items()` is especially useful for JSON-like data.

---

# 11. Nested Loops

A loop can contain another loop.

```python
users = [
    ["Deven", "Python"],
    ["Rahul", "Java"]
]

for user in users:
    for value in user:
        print(value)
```

The inner loop runs for each iteration of the outer loop.

---

# 12. Truthiness

Python treats several values as **falsey** in conditions:

```text
False
None
0
""
[]
{}
set()
```

Example:

```python
skills = []

if skills:
    print("Skills available")
else:
    print("No skills")
```

This is useful for simple existence checks.

---

# 🤖 GenAI Connection

Control flow is used constantly when processing:

```text
Documents
   ↓
Chunks
   ↓
Retrieved Results
   ↓
Tool Calls
   ↓
Agent Workflows
   ↓
LLM Responses
```

Examples:

- `for` → process documents/chunks
- `if` → validate or filter data
- `break` → stop searching after a suitable result
- `continue` → skip invalid data
- `enumerate()` → track position while processing results

---

## 🧠 Key Takeaway

```text
if / elif / else → decision
for              → iteration
while            → repetition
break            → stop
continue         → skip
range()          → numbers
enumerate()      → index + value
in / not in      → membership
```

---

## ✅ Topic Completed

- [x] Conditionals
- [x] Comparison operators
- [x] Logical operators
- [x] Membership operators
- [x] `for` loops
- [x] `range()`
- [x] `while`
- [x] `break`
- [x] `continue`
- [x] `enumerate()`
- [x] Dictionary iteration
- [x] Nested loops
- [x] Truthiness
