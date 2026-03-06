class Account:
    def __init__(self,balance,accntNo):
        self.balance= balance
        self.accntNo=accntNo

    def debit(self,amount):
        self.balance-=amount
        print("Rs." ,amount,"debited")
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs." ,amount,"credited")

account1 = Account(20000,1)
print("Account balance : ",account1.balance)
print("Account number : ",account1.accntNo)
account1.debit(200)
account1.credit(1000)
