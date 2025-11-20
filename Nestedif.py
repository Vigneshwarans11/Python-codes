#login insta username & password
# a="vignesh123"
# b="12345"
# username=input("Enter the Username:")
# if(username==a):
#     password=input("Enter the Password:")
#     if(password==b):
#         print("login")
#     else:
#         print("password incorrect")
# else:
#     print("invalid user")

#Wap to print the middle value of a list only if it is string
# a=eval(input("enter the list:"))
# if(len(a)%2==1):
#     if(type(a[len(a)//2]==str)):
#         print(a[len(a)//2])
#     else:
#         print("its not a string")
# else:
#     print("it has a no middle value")

#wap to check whether the character is vowel or consonant
# a=input("enter the char:")
# if('A'<=a<='Z' or 'a'<=a<='z'):
#     if a in['a','e','i','o','u','A','E','I','O','U']:
#         print("Vowels")
#     else:
#         print("consonenet")
# else:
#     print("not a alphapet")

# wap to print the value as it is only if the length of the value is even
# value=eval(input("enter the value"))
# if len(value)>0:
#     if(len(value)%2==0):
#         print("lenght of the value is even")
#     else:
#         print("not a even")
# else:
#     print("empty")
             
#wap to print the reversed string only if it is starting with a vowel and if it consist of middle character
# char=input("enter the string:")
# if char[0] in "AEIOUaeiou":
#     if(len(char)%2==1):
#         print(char[::-1])
#     else:
#         print("doesnot have a middle value")
# else:
#     print("not start with vowela")


#wap to print middle character of the given string only if it is upper
# char=input("enter the char:")
# if(len(char)%2==1):
#     if(65<=ord(char[len(char)//2])<=90):
#         print(char[len(char)//2])
#     else:
#         print("not a upper char")
# else:
#     print("doesnot have middle value")


#wap to print middle character of the given char only if it is digit
# a=input("enter the char")
# if(len(a)%2==1):
#     if('0'<=(a[len(a)//2])<='9'):
#         print(a[len(a)//2])
#     else:
#         print("not digit")
# else:
#     print("doesnot hve middle value")


#wap to print the last value of a list only if it is palindrome string starting with vowel
# a=eval(input("enter the list"))
# if(type(a[-1])==str):
#     if(a[-1]==a[-1][::-1]):
#         if(a[-1][0] in "AEIOUaeiou"):
#             print(a[-1])
#         else:
#             print("not a vowel")
#     else:
#         print("not a palinndrome")
# else:
#     print("not a string")