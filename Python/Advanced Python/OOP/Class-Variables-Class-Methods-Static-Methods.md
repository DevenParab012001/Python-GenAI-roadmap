# Class Variables, Class Methods & Static Methods

## Class Variable

A class variable belongs to the class and is shared by objects.

```python
class Employee:
    company = "QAD"

    def __init__(self, name):
        self.name = name
```

- `company` → class variable
- `self.name` → instance variable

## Class Method

A class method works with class-level data.

Use `@classmethod` and `cls`.

```python
class Employee:
    company = "QAD"

    @classmethod
    def change_company(cls, name):
        cls.company = name
```

Call it:

```python
Employee.change_company("Microsoft")
```

## Static Method

A static method does not need `self` or `cls`.

Use `@staticmethod`.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

Call it without creating an object:

```python
Calculator.add(10, 20)
```

## Student Counter

A class variable can track shared information:

```python
class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1
```

## Quick Revision

```text
Instance method  → self → object
Class method     → cls  → class
Static method    → none → utility logic
```

## Key Difference

| Type | First parameter | Main purpose |
|---|---|---|
| Instance method | `self` | Object data/behavior |
| Class method | `cls` | Class-level data/behavior |
| Static method | None | Independent utility logic |

## Important Syntax

```python
class Example:

    class_variable = "shared"

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass
```
