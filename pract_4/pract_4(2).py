class BankAccount:
    def __init__(self, accountNo, balance=0):
        self.accountNo = accountNo
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount, "into account")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawn", amount, "from account")

    def getBalance(self):
        print("Balance:", self.balance)


# Store multiple accounts
accD = []

noofacc = int(input("Enter number of accounts: "))
for i in range(noofacc):
    accNo = int(input(f"Enter account number {i+1}: "))
    InitialBalance = int(input(f"Enter initial balance for account {i+1}: "))
    accD.append(BankAccount(accNo, InitialBalance))  # Append each account to the list

# Fetch account details
accNo = int(input("Enter account number to fetch details: "))

found = None
for account in accD:
    if account.accountNo == accNo:
        found = account
        break

if found:
    found.getBalance()
    while True:
        print("1. Deposit  2. Withdraw  3. Check Balance  4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            amount = int(input("Enter amount to deposit: "))
            found.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            found.withdraw(amount)
        elif choice == 3:
            found.getBalance()
        elif choice == 4:
            print("Thank you for using our service.")
            break
        else:
            print("Invalid choice! Please enter again.")
else:
    print("Account not found.")
