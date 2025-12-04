# How to Add / Merge Two Dictionaries in Python

# using update()
# a={"a":10, "b":20}
# b={"c":30}

# a.update(b)
# print(a)

# using **dict1,**dict2
# a={"a":10, "b":20}
# b={"c":30}
# result={**a,**b}
# print(result)

# Using | Operator
# a={"a":10, "b":20}
# b={"c":30}
# result=a|b
# print(result)

# Reverse a String Using Slicing
# a="vignesh"
# rev=a[::-1]
# print(rev)

# Reverse a String Using for loop
# a="vignesh"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev) 

# Using reversed() Function
# a="hello"
# rev="".join(reversed(a))
# print(rev)

# Using While Loop
# s="hello"
# rev=""
# i=len(s)-1

# while i>=0:
#     rev = rev+s[i]
#     i =i-1
# print(rev)

# Factorial Program Using for Loop
# n=int(input("enter the numbers:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial:",fact)

# Factorial Using While Loop
# n=int(input("enter the value:"))
# fact=1
# i=1

# while i<=n:
#     fact =fact*i
#     i =i+1
# print("factorial",fact)


# Factorial Using Recursion
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("enter the value:"))
# print(factorial(n))



# sum of 2 numbers
# def add(a,b):
#     return a+b
# print(add(10,20))

# lambda
# double=lambda x:x*2
# print(double(20))

# add=lambda x,y:x+y
# print(add(10,20))



# Create one list with duplicates and asked how can u remove the duplicates from list?
# list1=[1,2,2,4,5,6,7,4]
# unique=list(set(list1))
# print(unique)

# list1=[1,2,2,4,5,6,7,4]
# unique=list(dict.fromkeys(list1))
# print(unique)

# What is list comprehension and asked to write a program to print even numbers from 1 to 10
# even=[i for i in range(1,11) if i%2==0]
# print(even)

# Write a program to swap the values without using temporary variable? 
# a=int(input("enter the value a="))
# b=int(input("enter the value b="))

# print("befor swapping a=",a,"b=", b)
# a,b=b,a
# print("After Swapping a=",a,"b=", b)

# Write a program to swap the values with using temporary variable? 
a=int(input("enter the value a="))
b=int(input("enter the value b="))

print("befor swapping a=",a,"b=", b)
temp=a
a=b
b=temp
print("After Swapping a=",a,"b=", b)


