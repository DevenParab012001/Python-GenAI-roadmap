# Object-Oriented Programming (OOP) — Basics

## 1. What is OOP?

**OOP = Object-Oriented Programming**

OOP organizes programs around **classes and objects**.

A **class** is a blueprint.

An **object** is an instance created from a class.

```python
class Vehicle:
    pass

car = Vehicle()
```

- `Vehicle` → Class
- `car` → Object

---

## 2. `__init__()`

`__init__()` initializes an object's data when the object is created.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create an object:

```python
student = Student("Deven", 25)
```

---

## 3. `self`

`self` refers to the **current object**.

```python
self.name = name
```

It stores the value inside that particular object.

Different objects can have different values:

```python
student1 = Student("Deven", 25)
student2 = Student("Rahul", 24)
```

---

## 4. Attributes

Variables belonging to an object are called **attributes**.

```python
self.name
self.age
self.course
```

Access them using the object:

```python
print(student1.name)
print(student1.age)
```

---

## 5. Methods

A function defined inside a class is called a **method**.

```python
class Vehicle:
    def start(self):
        print("Vehicle started")
```

Call the method:

```python
car = Vehicle()
car.start()
```

---

## 6. Class + Object Example

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(self.brand, self.model)


car = Vehicle("Toyota", "Fortuner")
car.display_info()
```

---

## 7. Multiple Objects

One class can create many objects.

```python
vehicle1 = Vehicle("Toyota", "Fortuner")
vehicle2 = Vehicle("Honda", "City")
```

Each object stores its own data.

```text
vehicle1 → Toyota Fortuner
vehicle2 → Honda City
```

---

## 8. Practical OOP Structure

A class usually contains:

```text
Class
 ├── __init__()
 │    └── Object data / attributes
 │
 └── Methods
      └── Object behavior
```

Example:

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

---

## Quick Revision

```text
class       → blueprint
object      → instance of a class
__init__()  → initializes object data
self        → current object
attribute   → data stored in object
method      → function inside a class
```

## Why OOP Matters

OOP keeps related **data and behavior together** and is useful for building larger applications.

The same concepts are heavily used in Java and Spring Boot.
