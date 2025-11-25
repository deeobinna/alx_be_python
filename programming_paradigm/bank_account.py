#define a class named BankAccount
#use the __init__ method to initialize an account_balance attribute
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    #Implement deposit(amount), withdraw(amount), and display_balance() methods.
    def deposit(self, amount):
        #deposit should add the specified amount to account_balance.
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")


    def withdraw(self, amount):
        if amount >= self.account_balance:
            print("Insufficient funds.")
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            


    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
