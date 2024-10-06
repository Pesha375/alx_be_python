# bank_account.py
# bank_account.py
# bank_account.py
# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

# main.py
from bank_account import BankAccount
import sys

def main():
    if len(sys.argv)!= 2:
        print("Usage: python main.py <account_balance>")
        sys.exit(1)

    account_balance = float(sys.argv[1])
    account = BankAccount(account_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if not account.withdraw(amount):
                print("Insufficient funds")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()