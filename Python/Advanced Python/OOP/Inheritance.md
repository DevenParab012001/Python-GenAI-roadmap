# OOP — Inheritance

## 1. What is Inheritance?

**Inheritance** allows one class to reuse properties and methods of another class.

```python
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass
```

Here:

```text
Animal → Parent / Base class
Dog    → Child / Derived class
```

`Dog` inherits `eat()` from `Animal`.

---

## 2. Why Use Inheritance?

Inheritance avoids repeating common code.

Instead of putting the same method in multiple classes, put the common behavior in a parent class.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

Both `Dog` and `Cat` can use `eat()`.

---

## 3. Child Class with Its Own Method

A child can use inherited methods and define its own methods.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")
```

```python
dog = Dog()

dog.eat()     # inherited
dog.bark()   # own method
```

---

## 4. Constructor Inheritance

A child class can inherit the parent's constructor.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    pass
```

```python
car = Car("Toyota")
print(car.brand)
```

---

## 5. `super()`

`super()` is used to access the parent class.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
```

Here:

```text
Car.__init__()
      ↓
super().__init__(brand)
      ↓
Vehicle.__init__(brand)
```

This allows the child to reuse the parent's initialization code.

---

## 6. Method Inheritance

If a method is not defined in the child class, Python looks in the parent class.

```python
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    pass
```

```python
dog = Dog()
dog.sound()
```

Python finds `sound()` in `Animal`.

---

## 7. `pass`

`pass` means the class has no additional code in that block.

```python
class Dog(Animal):
    pass
```

It does **not** stop inheritance.

---

## 8. Practical Example

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(self.brand, self.model)


class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors
```

The `Car` gets:

- `brand`
- `model`
- `display_info()`

and adds:

- `number_of_doors`

---

## Quick Revision

```text
Inheritance
    ↓
Child reuses Parent code

Parent / Base class
        ↓
Child / Derived class

class Dog(Animal):
    ↓
Dog inherits from Animal

super()
    ↓
Access parent class functionality
```

## Key Terms

| Term | Meaning |
|---|---|
| Parent class | Class being inherited from |
| Child class | Class that inherits |
| Base class | Another name for parent |
| Derived class | Another name for child |
| `super()` | Access parent functionality |
| `pass` | No additional code in the block |
