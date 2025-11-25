#define a class named BankAccount
#use the __init__ method to initialize an account_balance attribute
class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    #Implement deposit(amount), withdraw(amount), and display_balance() methods.
    def deposit(self, amount):
        #deposit should add the specified amount to account_balance.
        self.account_balance += amount

    def withdraw(self, amount):
        if amount >= self.account_balance:
            print("Insufficient Balance")
        else:
            self.account_balance -= amount


    def display_balance(self):
        print(f"Current Balance:{self.account_balance}")
