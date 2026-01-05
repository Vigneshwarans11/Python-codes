#Print all unique elements in an array
# arr=[1,2,3,4,5,2,3,6]
# new_arr=[]

# for i in arr:
#     if i not in new_arr:
#         new_arr.append(i)
# print(new_arr)

#builtin function
#  arr=[1,2,3,4,5,2,3,6]
# unique=list(set(arr))
# print(unique)

#Find the second largest number with sorting
# a=[3,1,5,8,4,9,2]
# a.sort()
# print(a[-2])

#Find the second largest number without sorting
# a=[3,1,5,8,4,9,2]
# first=second=float('-inf')

# for num in a:
#     if num>first:
#         second=first
#         first=num
#     elif first>num>second:
#         second=num
# print(second)

#Check if a number is a palindrome
# num=121
# temp=num
# rev=0

# while temp>0:
#     rev=rev*10+temp%10
#     temp=temp//10
# if num==rev:
#     print("palindrom")
# else:
#     print("not a palindrom")

