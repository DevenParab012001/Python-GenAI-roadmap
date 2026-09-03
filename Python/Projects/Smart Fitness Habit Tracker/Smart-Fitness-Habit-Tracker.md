# 🏋️ Smart Fitness Habit Tracker

> **Python Roadmap — Project 4**

A console-based fitness habit tracker that records daily exercises, calories burned, and generates a habit summary.

The SDE Master Program roadmap specifies tracking daily exercises and calories burned, then generating habit summaries using basic loops and functions.

## 🎯 Roadmap Requirement

The project focuses on:

- Daily exercise tracking
- Calories burned
- Habit summaries
- Basic loops
- Functions
- Conditional logic

## 🧱 Data Structure

Each activity is stored as a dictionary:

```python
activity = {
    "exercise": exercise,
    "calories": calories
}
```

Multiple activities are stored in a list:

```python
activities = []
```

This allows each day's exercise and calorie value to stay together.

## 🔄 Looping Through Days

The program uses a `for` loop:

```python
for day in range(1, days + 1):
```

This collects activity information repeatedly for the requested number of days.

## 🧮 Total Calories

The total is calculated using a function:

```python
def calculate_total(activities):
    total = 0

    for activity in activities:
        total += activity["calories"]

    return total
```

The function receives the activity list and returns the total calories burned.

## 📊 Average Calories

The program also calculates the average calories per tracked day:

```python
return total / len(activities)
```

This is an extra summary feature added to the project.

## 🏆 Most Active Day

The program compares the calorie values and keeps the activity with the highest value:

```python
if activity["calories"] > most_active["calories"]:
    most_active = activity
```

This is an extra summary feature.

## 🛡️ Input Validation

The implementation validates:

- Number of tracking days must be greater than 0.
- Calories cannot be negative.
- Exercise name cannot be empty.
- Invalid numeric input is handled with `try/except`.

These are implementation extras that improve the console experience.

## 🧠 Concepts Used

- Lists
- Dictionaries
- Functions
- Parameters
- `return`
- `for` loops
- `while` loops
- `if` statements
- `input()`
- `int()`
- `.strip()`
- `try / except`
- `enumerate()`
- List indexing

## 🔄 Program Flow

```text
Start
  ↓
Ask number of days
  ↓
Collect exercise + calories
  ↓
Store each activity
  ↓
Display daily activities
  ↓
Calculate summary
  ↓
Display total / average / most active day
  ↓
Exit
```

## 🧪 Example

```text
🏋️ SMART FITNESS HABIT TRACKER

Let's track your exercise for multiple days.

How many days do you want to track? 3

---------- Day 1 ----------
Exercise: Running
Calories burned: 300

---------- Day 2 ----------
Exercise: Cycling
Calories burned: 250

---------- Day 3 ----------
Exercise: Walking
Calories burned: 200

========== DAILY ACTIVITIES ==========
Day 1: Running - 300 calories
Day 2: Cycling - 250 calories
Day 3: Walking - 200 calories

========== HABIT SUMMARY ==========
Total days       : 3
Total calories   : 750
Average calories : 250.00

---------- Most Active Day ----------
Exercise : Running
Calories : 300
```

## ✅ Completion Checklist

- [x] Track daily exercises
- [x] Track calories burned
- [x] Generate habit summary
- [x] Use loops
- [x] Use functions
- [x] Use conditional logic
- [x] Input validation — extra
- [x] Average calories — extra
- [x] Most active day — extra

## 📌 Core Idea

```text
Daily Activity
      ↓
Store Data
      ↓
Process With Functions
      ↓
Generate Summary
```
