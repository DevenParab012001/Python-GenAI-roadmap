# 🧮 Simple Calculator

> **Python + GenAI Roadmap — Core Python Project**

A console-based calculator built using Python fundamentals.

---

## 🎯 Project Goal

The calculator accepts two numbers and allows the user to perform:

- Addition
- Subtraction
- Multiplication
- Division

The program also handles invalid input and division by zero.

---

## ✨ Features

```text
1. Addition
2. Subtraction
3. Multiplication
4. Division
```

The calculator runs repeatedly until the user chooses to exit.

---

## 🧠 Python Concepts Used

- Variables
- Numeric data types
- Functions
- Parameters and return values
- `if / elif / else`
- `while` loop
- `try / except`
- `ValueError`
- `ZeroDivisionError`
- User input
- Formatted output

---

## 📂 Project Structure

```text
Simple Calculator/
├── simple_calculator.py
└── Simple-Calculator.md
```

---

## ▶️ How to Run

From the project directory:

```powershell
python simple_calculator.py
```

---

## 💻 Example

```text
===== Simple Calculator =====

Enter first number: 20
Enter second number: 5

Choose operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter choice: 4

Result: 4.0
```

---

## 🛡️ Error Handling

### Invalid number

```text
Enter first number: abc
Invalid input. Please enter valid numbers.
```

### Division by zero

```text
Cannot divide by zero.
```

### Invalid operation

```text
Invalid operation.
```

---

## 🔄 Program Flow

```text
Start
  ↓
Enter two numbers
  ↓
Choose operation
  ↓
Perform calculation
  ↓
Display result
  ↓
Another calculation?
  ├── Yes → Repeat
  └── No  → Exit
```

---

## ✅ Project Status

- [x] Addition
- [x] Subtraction
- [x] Multiplication
- [x] Division
- [x] Input validation
- [x] Division-by-zero handling
- [x] Repeated calculations
- [x] Function-based implementation
