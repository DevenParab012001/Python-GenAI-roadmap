class BankAccount:

    def __init__(self, account_holder, balance):
        if not account_holder.strip():
            raise ValueError("Account holder name cannot be empty.")

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than ₹0.")

        self.balance += amount

        print(f"\n✓ ₹{amount:,.2f} deposited successfully.")
        print(f"  Current balance: ₹{self.balance:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than ₹0.")

        if amount > self.balance:
            raise ValueError(
                f"Insufficient balance. Available balance: ₹{self.balance:,.2f}"
            )

        self.balance -= amount

        print(f"\n✓ ₹{amount:,.2f} withdrawn successfully.")
        print(f"  Current balance: ₹{self.balance:,.2f}")

    def check_balance(self):
        print("\n---------- ACCOUNT DETAILS ----------")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance        : ₹{self.balance:,.2f}")
        print("-------------------------------------")


def create_account():

    try:
        print("\n---------- CREATE ACCOUNT ----------")

        name = input("Enter account holder name: ").strip()

        balance = float(input("Enter initial balance: ₹"))

        account = BankAccount(name, balance)

        print("\n✓ Account created successfully!")
        print(f"  Account Holder : {account.account_holder}")
        print(f"  Initial Balance: ₹{account.balance:,.2f}")

        return account

    except ValueError as e:
        print(f"\n✗ Error: {e}")
        return None


def display_menu():

    print("\n=====================================")
    print("          BANKING SYSTEM")
    print("=====================================")

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    print("-------------------------------------")


def main():

    account = None

    while True:

        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        try:

            if choice == "1":

                if account is not None:
                    print("\n✗ An account already exists.")
                    print("  You cannot create another account.")

                else:
                    account = create_account()

            elif choice == "2":

                if account is None:
                    print("\n✗ No account found.")
                    print("  Please create an account first.")

                else:
                    amount = float(input("\nEnter deposit amount: ₹"))
                    account.deposit(amount)

            elif choice == "3":

                if account is None:
                    print("\n✗ No account found.")
                    print("  Please create an account first.")

                else:
                    amount = float(input("\nEnter withdrawal amount: ₹"))
                    account.withdraw(amount)

            elif choice == "4":

                if account is None:
                    print("\n✗ No account found.")
                    print("  Please create an account first.")

                else:
                    account.check_balance()

            elif choice == "5":

                print("\nThank you for using the Banking System!")
                print("Have a great day! 👋")
                break

            else:

                print("\n✗ Invalid choice.")
                print("  Please enter a number between 1 and 5.")

        except ValueError as e:

            print(f"\n✗ Error: {e}")


main()
