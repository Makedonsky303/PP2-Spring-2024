class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def getInfo(self):
        print(self.owner,"has",self.balance)    
    def deposit(self,amount):
        self.balance+=amount 
    def withdraw(self,amount):
        if self.balance-amount < 0:
            print(self.owner,"doesn't have enough funds")
        else:
            self.balance-=amount

beta = Account("beta", 1000) 
beta.withdraw(300)
beta.getInfo()
beta.deposit(100)               
beta.getInfo()

beta.withdraw(1000)