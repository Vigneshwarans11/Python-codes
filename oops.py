class person:
    def __init__(self,name):
        self.name=name
class employee(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary

    
    def show(self):
        print(self.name)
        print(self.salary)
e1=employee("vignesh",98765)
e1.show()


class dog:
    def sound(self):
        print("barks")
class cat:
    def sound(self):
        print("meow")

d=dog()
c=cat()

d.sound()
c.sound()


class bank:
    def __init__(self):
        self.__balance=1000
    def show_balance(self):
        print("balance",self.__balance)
b =bank()
b.show_balance()
