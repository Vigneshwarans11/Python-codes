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
# class A:
#     a=20
#     b=30
#     def __init__(self,c,d):
#         self.c=c
#         self.d=d
# obj1=A(40,50)
# print(obj1.c,obj1.d)
# class B(A):
#     e=40
#     f=20
#     def __init__(self,g,h,i):
#         self.g=g
#         self.h=h
#         self.i=i
# obj2=B(100,200,300)
# print(obj2.a,obj2.g,obj2.h,obj2.i)


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


        

        
