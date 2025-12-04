# class bank():
#     def __init__(self,name,balance):
#         self.name=name
#         self._balance=balance
#         self.__pin =1234
#     def display_customer(self):
#         print(self.name,self._balance)
#     def __show_pin(self):
#         print(self.__pin)
#     def access_pin(self):
#         self.__show_pin()
# obj=bank("vignesh",123,)
# obj.display_customer()
# obj.access_pin()

#protector
# class bank():
#     _b_name="hdfc"
#     _b_ifsc=6444
#     def __init__(self,c_name):
#         self.c_name=c_name
#     def display(self):
#         print(self.c_name)
# obj1=bank("vignesh") 
# obj1.display() 
# print(obj1._b_name,obj1._b_ifsc,obj1.c_name)


#private
# class bank():
#     def __init__(self,b_name,b_type,b_pin):
#         self.b_name=b_name
#         self._b_type=b_type
#         self.__b_pin=b_pin
#     def display(self):
#         print(self.b_name,self._b_type)
#     def display_1(self):
#         print(self.__b_pin)
# obj1=bank("hdfc","saving",6866)
# obj1.display()
# obj1.display_1()   




