# 🏦 Banking System Simulation

> **Python Roadmap — Project 2**

A simple console-based banking system built with Python classes, objects, methods, conditionals, loops, input handling, and exception handling.

---

## 🎯 Project Requirements

The project covers the four operations specified in the roadmap:

1. Create an account
2. Deposit money
3. Withdraw money
4. Check balance

### Extra functionality added

The implementation also includes:

- Input validation
- Error handling with `try/except`
- A simple interactive menu
- Prevention of creating a second account
- Prevention of deposits/withdrawals with non-positive amounts
- Prevention of withdrawing more than the available balance
- Currency formatting

These are **project implementation extras**, not additional roadmap topics.

---

## 🧱 Main Class

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
```

### Instance variables

| Variable | Purpose |
|---|---|
| `account_holder` | Stores the account holder's name |
| `balance` | Stores the current account balance |

---

## 💰 Deposit

```python
def deposit(self, amount):
    self.balance += amount
```

The deposit method increases the account balance by the supplied amount.

Example:

```text
Initial balance: ₹10,000
Deposit:         ₹2,000
New balance:     ₹12,000
```

---

## 💸 Withdraw

```python
def withdraw(self, amount):
    self.balance -= amount
```

The withdrawal method decreases the account balance.

The project implementation also checks whether enough money is available before withdrawing.

Example:

```text
Initial balance: ₹12,000
Withdrawal:      ₹3,000
New balance:      ₹9,000
```

---

## 🔎 Check Balance

```python
def check_balance(self):
    print(self.balance)
```

Displays the account holder and current balance.

---

## ⚠️ Exception Handling

The program uses `try/except` to handle invalid user input and validation errors.

```python
try:
    balance = float(input("Enter initial balance: ₹"))
except ValueError as e:
    print(f"Error: {e}")
```

The `BankAccount` class also raises `ValueError` for invalid operations.

---

## 🔄 Program Flow

```text
Start
  ↓
Display Menu
  ↓
Create Account
  ↓
Deposit / Withdraw / Check Balance
  ↓
Repeat Menu
  ↓
Exit
```

---

## 🧠 Key Python Concepts Used

- Classes
- Objects
- `__init__`
- Instance variables
- Methods
- `if / elif / else`
- `while` loop
- Functions
- `input()`
- `float()`
- `try / except`
- `raise ValueError`
- f-strings
- String `.strip()`

---

## 🧪 Example Run

```text
=====================================
          BANKING SYSTEM
=====================================
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit

Enter your choice (1-5): 1

---------- CREATE ACCOUNT ----------
Enter account holder name: Deven
Enter initial balance: ₹10000

✓ Account created successfully!

Enter your choice (1-5): 2
Enter deposit amount: ₹2000

✓ ₹2,000.00 deposited successfully.

Enter your choice (1-5): 3
Enter withdrawal amount: ₹3000

✓ ₹3,000.00 withdrawn successfully.

Enter your choice (1-5): 4

---------- ACCOUNT DETAILS ----------
Account Holder : Deven
Balance        : ₹9,000.00
-------------------------------------
```

---

## ✅ Project Completion Checklist

- [x] Create account
- [x] Deposit
- [x] Withdraw
- [x] Check balance
- [x] Interactive console program
- [x] Basic validation
- [x] Exception handling

---

## 📌 Remember

The core idea is simple:

```text
Object → stores account state
Methods → modify or display that state
```

For example:

```python
account = BankAccount("Deven", 10000)

account.deposit(2000)
account.withdraw(3000)
account.check_balance()
```

Final balance:

```text
₹9,000
```
