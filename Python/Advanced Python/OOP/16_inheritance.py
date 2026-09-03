# OOP - Inheritance, super() and Method Reuse


# 1. Basic Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()
dog.bark()
dog.eat()


# 2. Constructor Inheritance and super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Car is starting")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


car = Car("Toyota", "Fortuner")

print("Brand:", car.brand)
print("Model:", car.model)
car.start()


# 3. Employee -> Developer
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


developer = Developer("Deven", 100000, "Python")

developer.display()
print("Programming Language:", developer.programming_language)


# 4. Method Inheritance
class AnimalWithSound:
    def sound(self):
        print("Some sound")


class DogWithInheritedSound(AnimalWithSound):
    pass


dog2 = DogWithInheritedSound()
dog2.sound()


# 5. Practical Vehicle Service Example
class ServiceVehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class ServiceCar(ServiceVehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print("Number of Doors:", self.number_of_doors)


class Bike(ServiceVehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_info(self):
        super().display_info()
        print("Engine CC:", self.engine_cc)


service_car = ServiceCar("Toyota", "Fortuner", 5)
bike = Bike("Yamaha", "R15", 155)

print("Car Information:")
service_car.display_info()

print()

print("Bike Information:")
bike.display_info()
