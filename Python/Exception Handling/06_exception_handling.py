# Python — Exception Handling
# Practice Solutions

# 1. try and except
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")


# 2. Multiple exceptions
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# 3. finally
try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Invalid number")
finally:
    print("Program finished")


# 4. raise
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True

try:
    age = int(input("Enter your age: "))
    print(validate_age(age))
except ValueError as error:
    print(error)


# 5. FileNotFoundError
try:
    with open("config.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Configuration file not found")


# 6. Function + exception handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

result = safe_divide(10, 0)

if result is None:
    print("Division failed")
else:
    print(result)
