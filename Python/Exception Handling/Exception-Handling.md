# ⚠️ Python — Exception Handling

> **Python + GenAI Roadmap**  
> Handling runtime errors without unexpectedly stopping the program.

---

## 🧭 Core Concepts

| Concept | Purpose |
|---|---|
| `try` | Code that may cause an exception |
| `except` | Handle an exception |
| `else` | Runs when no exception occurs |
| `finally` | Runs whether an exception occurs or not |
| `raise` | Manually create an exception |

---

# 1️⃣ `try` / `except`

Use `try` for code that may fail.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
```

---

# 2️⃣ Multiple Exceptions

Different errors can have different handlers.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Common exceptions

```text
ValueError          → Invalid value
TypeError           → Wrong type
ZeroDivisionError   → Division by zero
IndexError          → Invalid list index
KeyError            → Missing dictionary key
FileNotFoundError   → File does not exist
```

---

# 3️⃣ `else`

`else` runs only when the `try` block succeeds.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
else:
    print("Valid number:", number)
```

---

# 4️⃣ `finally`

`finally` always runs.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
finally:
    print("Program finished")
```

Useful for cleanup or operations that must happen regardless of success or failure.

---

# 5️⃣ `raise`

`raise` manually creates an exception when a validation rule is violated.

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return True
```

---

# 6️⃣ Reading the Exception

Store the exception in a variable:

```python
try:
    number = int("abc")
except ValueError as error:
    print(error)
```

---

# 7️⃣ File Errors

```python
try:
    with open("config.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Configuration file not found")
```

---

# 8️⃣ Exceptions Inside Functions

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

The caller can then decide how to handle the result.

---

## 🧠 Key Takeaway

```text
try      → attempt the operation
except   → handle the error
else     → run if successful
finally  → always run
raise    → create an exception
```

### Important

Avoid using:

```python
except Exception:
    pass
```

as a default approach because it can hide real bugs.

Prefer catching the specific exception you expect.

---

# 🤖 GenAI Connection

Exception handling becomes important when working with:

```text
User Input
    ↓
Python Application
    ↓
LLM / API
    ↓
Network
    ↓
Response
```

Possible failures include:

- Invalid input
- API errors
- Rate limits
- Timeouts
- Missing files
- Invalid data

Robust GenAI applications need to handle these failures instead of simply crashing.

---

## ✅ Practice Completed

- [x] `try` / `except`
- [x] Multiple exceptions
- [x] `finally`
- [x] `raise`
- [x] Exception object
- [x] `FileNotFoundError`
- [x] Exception handling inside functions
