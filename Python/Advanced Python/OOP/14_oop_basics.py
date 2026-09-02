# OOP Basics - Classes, Objects, Attributes and Methods

# 1. Student
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Deven", 25, "Python")

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Course: {student1.course}")


# 2. Employee
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")


emp1 = Employee("Deven", 100000000, "IT")
emp1.display_info()


# 3. Calculator
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


add_1 = Calculator(1, 3)
sub_1 = Calculator(3, 1)
mul_1 = Calculator(5, 2)
div_1 = Calculator(10, 2)

print(add_1.add())
print(sub_1.subtract())
print(mul_1.multiply())
print(div_1.divide())


# 4. Bank Account
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print("Current balance:", self.balance)


account = BankAccount("Deven", 10000)

account.display_balance()

account.deposit(2000)
print("After deposit:", account.balance)

account.withdraw(3000)
print("After withdrawal:", account.balance)

account.display_balance()


# 5. Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(self.brand, self.model, "started.")

    def stop(self):
        print(self.brand, self.model, "stopped.")

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


vehicle1 = Vehicle("Toyota", "Fortuner", 2024)
vehicle2 = Vehicle("Honda", "City", 2023)

vehicle1.display_info()
vehicle1.start()
vehicle1.stop()

print()

vehicle2.display_info()
vehicle2.start()
vehicle2.stop()
