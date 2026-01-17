class BankAccount:
    # 1. Parameterized constructor
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    # 2. Deposit and Withdraw methods
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} credited to {self.owner}'s account. Total: ₹{self.balance}")

    def withdraw(self, amount):
        # 4. Handle invalid withdrawal with checks
        if amount > self.balance:
            print(f"Error: Insufficient balance for {self.owner}. Available: ₹{self.balance}")
        elif amount <= 0:
            print("Error: Amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"₹{amount} debited. New Balance: ₹{self.balance}")

    # 3. Destructor
    def __del__(self):
        print(f"Record for account {self.account_number} has been cleared from the system.")

# Test

# Account Rahul
account = BankAccount("Rahul Verma", "SB-9921", 10000)

# Transaction
account.deposit(2500)
account.withdraw(3000)

# Withdrawl
account.withdraw(15000)

# Deleting object (Requirement 3)
del account