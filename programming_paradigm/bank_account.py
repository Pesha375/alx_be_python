# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes a new bank account with an optional starting balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account, if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds for withdrawal.")
            return False

    def display_balance(self):
        """Displays the current balance of the account."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
