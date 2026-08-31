# Simple Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    print("===== Simple Calculator =====")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

            print("\nChoose operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("\nEnter choice: ")

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)

            else:
                print("Invalid operation.")
                continue

            print("\nResult:", result)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")

        again = input(
            "\nDo you want to perform another calculation? (y/n): "
        )

        if again.lower() != "y":
            print("Calculator closed.")
            break


if __name__ == "__main__":
    calculator()
