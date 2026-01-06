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
# num=123456
# temp=num
# rev=0

# while temp>0:
#     rev=rev*10+temp%10
#     temp=temp//10
####### print(rev)(we use only for rev of num not for palindrome)
# if num==rev:
#     print("palindrom")
# else:
#     print("not a palindrom")

#Check if a str is a palindrome(loop)
# s="madam"
# rev=""
# for i in s:
#     rev=i+rev
# if s==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#Check if a str is a palindrome(slice)
# s="madam"
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#4. Check if two strings are anagrams
# s1="listen"
# s2="silent"
# if sorted(s1)==sorted(s2):
#     print("anagram")
# else:
#     print("not anangram")

#5. First non-repeating character in a string
# s="swiss"
# for ch in s:
#     if s.count(ch)==1:
#         print(ch)
#         break

#Remove duplicate characters (preserve order)
# s="programming"
# uni=""
# for ch in s:
#     if ch not in uni:
#         uni=uni+ch
# print(uni)

#Sum of digits until single digit
# num=9875
# while num>10:
#     s=0
#     while num>0:
#         s=s+num%10
#         num=num//10
#     num=s
# print(s)
