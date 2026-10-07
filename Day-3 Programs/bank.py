class InsufficientFundsError(Exception): 
    pass
class NegativeAmountError(Exception): 
    pass
class BankAccount:
    def __init__(self, id, balance):
        self.id=id
        self.balance=float(balance)
    def deposit(self, n):
        if n<=0: 
            raise NegativeAmountError
        self.balance+=n
    def withdraw(self, n):
        if n<=0: 
            raise NegativeAmountError
        if n>self.balance: 
            raise InsufficientFundsError
        self.balance-=n
    def get_balance(self):
        return self.balance
a=BankAccount("ACC1001",500.0)
a.deposit(200)
a.withdraw(300)
print(a.get_balance())