# 📦 Python — Modules & Packages

> **Python + GenAI Roadmap**  
> Organizing Python code into reusable modules and packages.

---

## 🧭 Core Concepts

| Concept | Meaning |
|---|---|
| Module | A Python `.py` file containing reusable code |
| Package | A collection of related modules |
| `import` | Import a module |
| `from ... import ...` | Import specific objects |
| `as` | Create an alias |
| `__name__` | Identifies how a module is being run |
| `pip` | Installs third-party packages |

---

# 1️⃣ Module

A **module** is a Python file containing reusable code.

```python
# calculator.py

def add(a, b):
    return a + b
```

Use it from another file:

```python
from calculator import add

print(add(10, 20))
```

```text
Module = Python file containing reusable code
```

---

# 2️⃣ `import`

Import an entire module:

```python
import math

print(math.sqrt(25))
```

Pattern:

```text
module.function()
```

---

# 3️⃣ Import Specific Functions

```python
from math import sqrt, ceil, floor

print(sqrt(25))
```

---

# 4️⃣ Alias

```python
import math as m

print(m.sqrt(25))
```

```text
as → creates an alias
```

---

# 5️⃣ Python Standard Library

Python provides many modules without requiring installation.

Examples:

```text
math
random
datetime
os
pathlib
```

---

# 6️⃣ Creating Your Own Module

```text
project/
├── main.py
└── calculator.py
```

**calculator.py**

```python
def add(a, b):
    return a + b
```

**main.py**

```python
from calculator import add

print(add(10, 20))
```

This lets us write code once and reuse it.

---

# 7️⃣ `__name__`

A common pattern is:

```python
def greet(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("Deven")
```

When the file is executed directly:

```text
__name__ == "__main__"
```

When the file is imported, the code inside this block does not automatically execute.

---

# 8️⃣ Package

A package organizes related modules.

```text
utilities/
├── __init__.py
├── calculator.py
└── user.py
```

Import from the package:

```python
from utilities.calculator import add
from utilities.user import create_user
```

```text
Module  → one .py file
Package → collection of related modules
```

---

# 9️⃣ Third-Party Packages

Some libraries do not come with Python.

They can be installed using `pip`:

```powershell
pip install fastapi
```

Examples:

```text
FastAPI
Pydantic
OpenAI SDK
LangChain
```

---

# 🧠 Key Takeaway

```text
.py file         → Module
Multiple modules → Package
import           → Reuse code
as               → Alias
pip              → Install external packages
__name__         → Detect direct execution
```

### Why Modules Matter

```text
Write code once
      ↓
Put it in a module
      ↓
Import it where needed
      ↓
Reuse + easier maintenance
```

---

## 🤖 GenAI Connection

Real GenAI applications will be split into modules such as:

```text
app/
├── main.py
├── config.py
├── services/
│   ├── llm_service.py
│   ├── embedding_service.py
│   └── retrieval_service.py
└── utils/
```

Each module can have a clear responsibility instead of putting the entire application into one file.

---

## ✅ Practice Completed

- [x] Standard library imports
- [x] Specific imports
- [x] Aliases
- [x] Custom modules
- [x] `__name__`
- [x] Packages
- [x] Third-party packages
- [x] Module-based project structure
