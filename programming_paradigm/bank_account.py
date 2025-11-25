#define a class named BankAccount
#use the __init__ method to initialize an account_balance attribute
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

       

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
