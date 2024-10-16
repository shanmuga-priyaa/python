print("\t\t\t\tWELCOME")
print("------------------------------------------------------------------------------")

class BankAccount:
    def _init_(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient balance")
            return self.balance
    
    def display(self):
        print("---------------------------------------")
        print("Account no : ", self.account_number)
        print("Balance    : ", self.balance)
        print("---------------------------------------")

# Creating an instance of BankAccount
account = BankAccount("1234556678", 1000)

# Display initial balance
account.display()

# Asking (deposit or withdraw)
action = input("\nEnter action (Deposit/Withdraw): ").strip().lower()

if action == "deposit":
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)
    print("Deposit successful.")
    account.display()
    
elif action == "withdraw":
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount <= account.balance:
        account.withdraw(withdraw_amount)
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
    account.display()
    
else:
    print("Invalid action. Please enter 'Deposit' or 'Withdraw'.")
