# OOP - Method Overriding and Polymorphism

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

animal = Animal()
dog = Dog()
animal.sound()
dog.sound()


class AnimalWithSuper:
    def sound(self):
        print("Animal sound")

class DogWithSuper(AnimalWithSuper):
    def sound(self):
        super().sound()
        print("Dog barks")

dog2 = DogWithSuper()
dog2.sound()


class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts")

class Bike(Vehicle):
    def start(self):
        print("Bike starts")

vehicles = [Vehicle(), Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(10, 4)]

for shape in shapes:
    print("Area:", shape.area())


class AIModel:
    def generate(self):
        print("AI model generating response...")

class OpenAIModel(AIModel):
    def generate(self):
        print("OpenAI model generating response...")

class GeminiModel(AIModel):
    def generate(self):
        print("Gemini model generating response...")

models = [OpenAIModel(), GeminiModel()]

for model in models:
    model.generate()
