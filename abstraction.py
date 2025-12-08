from abc import ABC,abstractmethod
class ATM():
    @abstractmethod
    def balance(self):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass
class hdfc_atm(ATM):
    amount=234
    password=3423
    def balance(self):
        verify = int(input("enter the password:"))
        if(self.password == verify):
            print("balance",self.amount)
        else:
            print("password incorrect")
    def deposit(self):
        verify = int(input("enter the password:"))
        if verify==self.password:
            deposit=int(input("enter the deposite amount:"))
            self.amount= self.amount+deposit
            print("total after deposite amount: ",self.amount)
        else:
            print("password incorrect")
    def withdraw(self):
        verify=int(input("enter the password:"))
        if verify==self.password:
            withdraw=int(input("enter the withdraw amt:"))
            self.amount=self.amount-withdraw
            print("amt after withdraw:",self.amount)
        else:
            print("password incorrect")
obj=hdfc_atm()
obj.balance()
obj.deposit()
obj.withdraw()