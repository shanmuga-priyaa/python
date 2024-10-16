class ATM():
    def __init__(self):
        self.account_no=123456789
        self.balance=1000
        print("\t"*3,"welcome")
        print("--------"*10)
        print(self.account_no)
        print(self.balance)
    def deposit(self,amount):
        self.balance=self.balance = amount
        print(self.account_no)
        print(self.balance)
    def withdraw(self,amount):
        if amount > self.balance:
            print("insuffiicient balance")
        else:
            self.balance = self.balance - amount
            print(self.account_no)
            print(self.balance)
person1=ATM()
choice=input("deposit/withdraw=").lower()
if choice=="deposit":
    amount=int(input("amount:"))
    person1.deposit(amount)
elif choice=="withdraw":
    amount=int(input("amount:"))
    person1.withdraw(amount)
else:
    print("invalid input")
































