#single level inheritance
# class A:
#     a=10
#     b=20
# object1=A()
# print(A.a,A.b)

# class B(A):
#     c=30
#     d=40
# object2=B()
# print(B.c,B.d,B.a,B.b)

#using init function
class A:
    a=20
    b=30
    def __init__(self,c,d):
        self.c=c
        self.d=d
obj1=A(40,50)
print(obj1.c,obj1.d)
class B(A):
    e=40
    f=20
    def __init__(self,g,h,i):
        self.g=g
        self.h=h
        self.i=i
obj2=B(100,200,300)
print(obj2.a,obj2.g,obj2.h,obj2.i)


#method changing
# class A:
#     a=10
#     b=20
#     def __init__(self,c,d):
#         self.c=c
#         self.d=d
#     def display(self):
#         print(self.c,self.d)
# obj1=A(40,30)
# print(obj1.c,obj1.d)
# class B(A):
#     e=100
#     f=200
#     def __init__(self,c,d,e,f):
#         super().__init__(c,d)
#         self.e=e
#         self.f=f
#     def display_1(self):
#         super().display()
#         print(self.e,self.f)
# obj2=B(10,20,30,40)
# obj2.display_1()

# class bank:
#     b_name="HDFC"
#     b_ifsc=3643
#     def __init__(self,c_name,c_phno):
#         self.c_name=c_name
#         self.c_phno=c_phno
#     def display(self):
#         print(self.c_name,self.c_phno)
# class bank1(bank):
#     def __init__(self,c_name,c_phno,c_age,c_bal):
#         super().__init__(c_name,c_phno) 
#         self.c_age=c_age
#         self.c_bal=c_bal
#     def display_1(self):
#         super().display()
#         print(self.c_age,self.c_bal)
# obj1=bank1("vignesh",987654321,18,86866797)
# obj1.display_1()



#using whatsapp
# class app:
#     a_name="whatsapp"
#     a_no=567536
#     def __init__(self,w_user):
#         self.w_user=w_user
#     def display(self):
#         print(self.w_user)
# class whatsapp1(app):
#     def __init__(self,w_user,w_story):
#         super().__init__(w_user)
#         self.w_story=w_story
#     def display_1(self):
#         super().display()
#         print(self.w_story)
# obj1=whatsapp1("vignesh","bjjbj")
# obj1.display_1()

#inheritence
# class animals():
#     def sound(self):
#         print("makes sound")
# class dog(animals):
#     def sound(self):
#         print("dog barks")
# d=dog()
# d.sound()

#single level inheritence
# class parent():
#     def display(self):
#         print("parent class")
# class child(parent):
#     def show(self):
#         print("child class")
# obj=child()
# obj.display()
# obj.show()

# #single level inheritence using __init__
# class bank():
#     def __init__(self,b_name,b_ifsc):
#         self.b_name=b_name
#         self.b_ifsc=b_ifsc
#     def display_bank(self):
#         print(self.b_name,self.b_ifsc)
# class account(bank):
#     def __init__(self,b_name,b_ifsc,c_name,c_age):
#         super().__init__(b_name,b_ifsc)
#         self.c_name=c_name
#         self.c_age=c_age
#     def display_acc(self):
#         print(self.c_name,self.c_age)
# acc=account("SBI",3433,"vignesh",23)
# acc.display_bank()
# acc.display_acc()

# multi_level inheritence
# class bank():
#     def __init__(self,b_name,b_ifsc):
#         self.b_name=b_name
#         self.b_ifsc=b_ifsc
#     def display_bank(self):
#         print(self.b_name,self.b_ifsc)
# class account(bank):
#     def __init__(self,b_name,b_ifsc,a_num,a_type):
#         super().__init__(b_name,b_ifsc)
#         self.a_num=a_num
#         self.a_type=a_type
#     def display_acc(self):
#         super().display_bank()
#         print(self.a_num,self.a_type)

# class customer(account):
#     def __init__(self,b_name,b_ifsc,a_num,a_type,c_name,c_age):
#         super().__init__(b_name,b_ifsc,a_num,a_type)
#         self.c_name=c_name
#         self.c_age=c_age
#     def display_customer(self):
#         super().display_acc()
#         print(self.c_name,self.c_age)
# obj=customer("hadf",6464,5545,"savings","vicky",21)
# # obj.display_bank()
# # obj.display_acc()
# obj.display_customer()


# Multiple Inheritance
# class bank():
#     def __init__(self,b_name):
#         self.b_name=b_name
#     def display_bank(self):
#         print(self.b_name)
# class customer():
#     def __init__(self,c_name):
#         self.c_name=c_name
#     def display_customer(self):
#         print(self.c_name)

# class account(bank,customer):
#     def __init__(self,b_name,c_name,a_type):
#         bank.__init__(self,b_name)
#         customer.__init__(self,c_name)
#         self.a_type=a_type
#     def display_acc(self):
#         self.display_bank()
#         self.display_customer()
#         print(self.a_type)

# obj=account("hgjbdj","bdjsbd","djbs")
# obj.display_acc()


# Hierarchical Inheritance
# class bank():
#     def __init__(self,b_name):
#         self.b_name=b_name
#     def display_bank(self):
#         print(self.b_name)
# class account(bank):
#     def __init__(self,b_name,acc_name):
#         super().__init__(b_name)
#         self.acc_name= acc_name
#     def display_acc(self):
#         print(self.acc_name)

# class customer(bank):
#     def __init__(self,b_name,c_name):
#         super().__init__(b_name)
#         self.c_name=c_name
#     def display_customer(self):
#         print(self.c_name)

# obj1=account("hdfc","saving")
# obj2=customer("hdfc","vignesh")

# obj1.display_bank()
# obj1.display_acc()

# obj2.display_bank()
# obj2.display_customer()



# Hybrid Inheritance
# Combination of more than one inheritance type
# Parent class
# class Bank:
#     def bank_info(self):
#         print("Bank: HDFC")

# # Level 1 child
# class Customer(Bank):
#     def cust_info(self):
#         print("Customer: Vignesh")

# # Another Level 1 child
# class LoanDetails:
#     def loan_info(self):
#         print("Loan amount: 50000")

# # Hybrid child class (inherits from Customer + LoanDetails)
# class Account(Customer, LoanDetails):
#     def acc_info(self):
#         print("Account Type: Savings")

# # Object
# obj = Account()
# obj.bank_info()
# obj.cust_info()
# obj.loan_info()
# obj.acc_info()


class one:
    def __init__ (self,A,B):
        self.A=A
        self.B=B
    def display(self):
        print(self.A,self.B)
class two(one):
    def __init__ (self,A,B,C,D):
        super().__init__(A,B)
        self.C=C
        self.D=D
    def show(self):
        super().display()
        print(self.C,self.D)
obj1=two(10,20,30,40)
obj1.show()






        
