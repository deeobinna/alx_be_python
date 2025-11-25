#define a class named BankAccount
#use the __init__ method to initialize an account_balance attribute
class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    #Implement deposit(amount), withdraw(amount), and display_balance() methods.
    def deposit(self, amount):
        #deposit should add the specified amount to account_balance.
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.account_balance:
            print("Insufficient funds.")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True


    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
