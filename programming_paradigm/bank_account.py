class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
      
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: {amount}, New Balance: {self.account_balance}"
        else:
            return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: {amount}, New Balance: {self.account_balance}"
        elif amount > self.account_balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."
        
    def display_balance(self):
        return f"Current balance: {self.account_balance}"  
