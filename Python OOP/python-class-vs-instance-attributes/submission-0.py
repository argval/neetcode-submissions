class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
    
    def __str__(self):
        print(f"{self.name}'s balance: ${self.balance}")

# TODO: Create two accounts
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
alice.__str__()
bob.__str__()
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
