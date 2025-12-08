#Payment Systems (UPI / Card / NetBanking)

class payment():
    def pay(self):
        pass
class UPI(payment):
    def pay(self):
        print("UPI payment Success")

class Card(payment):
    def pay(self):
        print("Card payment success")

class NetBanking(payment):
    def pay(self):
        print("NetBanking Sucess")



#Vehicle Billing System

class vehicle:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        return self.price*0.05

class car(vehicle):
    def __init__(self,brand,price):
        super().__init__(brand,price)
    def display(self):
        return self.price*0.10
    
class bike(vehicle):
    def __init__(self,brand,price):
        super().__init__(brand,price)
    def display(self):
        return self.price*0.03
    

vehicle=[car("BMW",5000),bike("TVS",2500)]
for v in vehicle:
    print(v.brand,v.display())