# 🐍 Python — Virtual Environments & `pip`

> **Python + GenAI Roadmap**  
> Managing Python packages and isolated project environments.

---

## 1️⃣ `pip`

`pip` is Python's **package installer**.

```powershell
pip install requests
```

Useful commands:

```powershell
pip list
pip show requests
```

---

## 2️⃣ Virtual Environment

A virtual environment gives a project its own **isolated Python environment**.

Create one:

```powershell
python -m venv .venv
```

Activate in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Deactivate:

```powershell
deactivate
```

---

## 3️⃣ Install Packages

After activating the environment:

```powershell
pip install requests
```

The package is installed inside that environment.

---

## 4️⃣ `requirements.txt`

Stores the project's dependencies.

Create it:

```powershell
pip freeze > requirements.txt
```

Example:

```text
fastapi==0.116.1
requests==2.32.5
numpy==2.3.2
```

Install dependencies from it:

```powershell
pip install -r requirements.txt
```

---

## 5️⃣ `.venv` vs `requirements.txt`

```text
.venv/
    → Actual local Python environment
    → ❌ Don't commit

requirements.txt
    → Dependency list
    → ✅ Commit
```

Another developer can recreate the environment:

```text
requirements.txt
       ↓
python -m venv .venv
       ↓
pip install -r requirements.txt
       ↓
Recreated environment
```

---

## 6️⃣ Check Python

```powershell
python --version
```

On Windows:

```powershell
where python
```

After activating `.venv`, Python should point to the project's virtual environment.

---

## 7️⃣ Upgrade pip

```powershell
python -m pip install --upgrade pip
```

Using `python -m pip` ensures you're using the `pip` associated with that Python interpreter.

---

## 8️⃣ `.gitignore`

Use `.gitignore` to prevent generated/local files from being committed.

Common Python entries:

```text
.venv/
__pycache__/
*.pyc
```

---

# 🧠 Key Takeaway

```text
pip
 ↓
Install Python packages

venv
 ↓
Isolate project environment

requirements.txt
 ↓
Record dependencies

.gitignore
 ↓
Ignore local/generated files
```

### Project Workflow

```text
Create project
      ↓
Create .venv
      ↓
Activate
      ↓
Install packages
      ↓
Develop
      ↓
requirements.txt
      ↓
.gitignore
      ↓
Git
```

**Virtual Environments & `pip` → complete.**
