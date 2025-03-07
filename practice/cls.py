class BankAccount:
    interest_rate = 3.5  # Class variable (shared by all accounts)

    def __init__(self, balance):
        self.balance = balance  # Instance variable (unique for each account)

    def apply_interest(self):
        """Applies the interest rate to the balance."""
        self.balance += self.balance * (self.interest_rate / 100)

    @classmethod
    def change_interest_rate(cls, new_rate):
        """Updates the interest rate for all accounts."""
        cls.interest_rate = new_rate

# Create two accounts
acc1 = BankAccount(1000)
acc2 = BankAccount(2000)

# Apply interest with the default rate (3.5%)
acc1.apply_interest()
acc2.apply_interest()

print(f"Account 1 Balance: {acc1.balance}")  # 1035.0
print(f"Account 2 Balance: {acc2.balance}")  # 2070.0

# Change the interest rate using the class method
BankAccount.change_interest_rate(5.0)

# Apply interest again with the new rate (5.0%)
acc1.apply_interest()
acc2.apply_interest()

print(f"Account 1 Balance after new rate: {acc1.balance}")  # 1086.75
print(f"Account 2 Balance after new rate: {acc2.balance}")  # 2173.5
