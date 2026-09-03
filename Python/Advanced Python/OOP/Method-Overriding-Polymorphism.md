# Method Overriding & Polymorphism

## 1. Method Overriding

**Method overriding** means a child class provides its own implementation of a method that already exists in the parent class.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
```

The child `Dog` overrides the parent's `sound()` method.

---

## 2. `super()` with Overriding

A child can call the parent's implementation using `super()`.

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
```

Output:

```text
Animal sound
Dog barks
```

---

## 3. Polymorphism

**Polymorphism** means the same method call can produce different behavior depending on the object.

```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
```

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

The same `animal.sound()` call behaves differently for different objects.

---

## 4. Polymorphism with Inheritance

```python
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts")

class Bike(Vehicle):
    def start(self):
        print("Bike starts")
```

```python
vehicles = [Vehicle(), Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()
```

Each object uses its own `start()` implementation.

---

## 5. Practical GenAI Example

Different AI models can expose the same method:

```python
class AIModel:
    def generate(self):
        pass

class OpenAIModel(AIModel):
    def generate(self):
        print("OpenAI response")

class GeminiModel(AIModel):
    def generate(self):
        print("Gemini response")
```

Then:

```python
models = [OpenAIModel(), GeminiModel()]

for model in models:
    model.generate()
```

The calling code does not need to know which model it is using.

---

## Quick Revision

```text
Method overriding
    ↓
Child changes parent's method behavior

Polymorphism
    ↓
Same method call
    ↓
Different behavior depending on object

super()
    ↓
Access parent implementation
```

### Key Difference

| Concept | Meaning |
|---|---|
| Inheritance | Child reuses parent code |
| Overriding | Child changes parent's method behavior |
| Polymorphism | Same method call, different behavior |
| `super()` | Access parent functionality |
