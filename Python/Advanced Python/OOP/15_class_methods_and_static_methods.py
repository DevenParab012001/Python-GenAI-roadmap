# OOP - Class Variables, Class Methods and Static Methods

class Employee:
    company = "QAD"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Deven", 15000)
e2 = Employee("Rahul", 124455)

print(f"Name: {e1.name}, Company: {e1.company}")
print(f"Name: {e2.name}, Company: {e2.company}")


class EmployeeWithClassMethod:
    company = "QAD"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, name):
        cls.company = name


employee1 = EmployeeWithClassMethod("Deven", 15000)
employee2 = EmployeeWithClassMethod("Rahul", 124455)

EmployeeWithClassMethod.change_company("Microsoft")

print(employee1.name, employee1.company)
print(employee2.name, employee2.company)


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(10, 20))
print(Calculator.subtract(20, 10))
print(Calculator.multiply(10, 2))


class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1


s1 = Student("Deven")
s2 = Student("Rahul")
s3 = Student("Amit")

print("Total students:", Student.student_count)


class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_account(self):
        print("Bank:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


account = BankAccount("Deven", 10000)

account.display_account()

print("Valid amount:", BankAccount.is_valid_amount(500))
print("Valid amount:", BankAccount.is_valid_amount(-100))
