import bank_account

def main():
    account = bank_account.BankAccount(100)  # Initialize with a balance of 100
    print(account.display_balance())  # Display initial balance

    print(account.deposit(50))  # Deposit 50
    print(account.withdraw(30))  # Withdraw 30
    print(account.withdraw(670))  # Attempt to withdraw more than the balance
    print(account.display_balance())  # Display final balance

if __name__ == "__main__":
    main()