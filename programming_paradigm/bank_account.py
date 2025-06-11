class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
      
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount}"
        else:
            return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: ${amount}"
        elif amount > self.account_balance:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: {self.account_balance}"
