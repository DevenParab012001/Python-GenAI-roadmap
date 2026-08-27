# 🐍 Python — Functions

> **Python + GenAI Roadmap**  
> Short, practical reference for reusable Python logic.

---

## 🧭 Core Concepts

```text
Function = reusable block of code
```

A function generally follows:

```text
Input → Processing → Output
```

---

# 1️⃣ Defining a Function

```python
def greet(name):
    print(f"Hello {name}")

greet("Deven")
```

```text
def      → defines a function
name     → parameter
"Deven"  → argument
```

---

# 2️⃣ Parameters & Arguments

```python
def add(a, b):
    return a + b
```

```text
a, b        → parameters
add(10, 20) → arguments
```

---

# 3️⃣ `return`

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

```text
print() → displays a value
return  → sends a value back
```

---

# 4️⃣ Default Parameters

```python
def greet(name, message="Hello"):
    print(f"{message} {name}")

greet("Deven")
greet("Deven", "Welcome")
```

If the argument isn't provided, the default value is used.

---

# 5️⃣ Keyword Arguments

Arguments can be passed using parameter names.

```python
def introduce(name, age, role):
    print(name, age, role)

introduce(
    name="Deven",
    age=25,
    role="Developer"
)
```

---

# 6️⃣ `*args`

Accepts multiple positional arguments.

```python
def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Inside the function, `numbers` behaves like a **tuple**.

```text
*args → multiple positional arguments → tuple
```

---

# 7️⃣ `**kwargs`

Accepts multiple keyword arguments.

```python
def create_profile(**details):
    return details
```

Inside the function, `details` behaves like a **dictionary**.

```text
**kwargs → multiple keyword arguments → dictionary
```

---

# 8️⃣ Scope

Variables created inside a function are generally **local** to that function.

```python
def greet():
    message = "Hello"
    print(message)
```

Prefer passing values into functions and returning results instead of relying heavily on global mutable state.

---

# 9️⃣ Docstrings

A docstring documents what a function does.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

---

# 🔟 Type Hints

Type hints indicate expected types.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints do **not** automatically enforce types at runtime.

---

# 🤖 GenAI Connection

Functions let us split a larger GenAI application into reusable steps:

```text
load_documents()
      ↓
split_documents()
      ↓
create_embeddings()
      ↓
retrieve_documents()
      ↓
generate_response()
```

Each function can have a clear input, responsibility, and output.

---

## 🧠 Key Takeaway

```text
def        → define function
return     → return a result
parameter  → variable in function definition
argument   → value passed to function
*args      → positional arguments → tuple
**kwargs   → keyword arguments → dictionary
```

---

## ✅ Practice Completed

- [x] Function definition
- [x] Parameters and arguments
- [x] `return`
- [x] Default parameters
- [x] Keyword arguments
- [x] `*args`
- [x] `**kwargs`
- [x] Scope
- [x] Docstrings
- [x] Type hints
- [x] Functions with collections
