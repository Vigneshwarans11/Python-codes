# Reverse a String Without Using Built-in Functions

# s="hello"
# rev=""

# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# print(rev)

# for i in s:
#     rev=i+rev
# print(rev)

#Two pointers
# S=list("hello")
# left = 0
# right=len(S)-1

# while left<right:
#     S[left],S[right]=S[right],S[left]
#     left=left+1
#     right=right-1
#     result="".join(S)
# print(result)


#Reverse Each Word in a Sentence
# s=("hello world")
# word=s.split()
# result=""

# for i in word:
#     rev=""
#     for ch in i:
#         rev=ch+rev
#     result=result+rev+" "
# print(result.strip())

#Check Palindrome Using Reverse
# S="MADAM"
# rev=""
# for ch in S:
#     rev=ch+rev
# if S==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")



#  Find the Second Largest Element in an Array 
# arr=  [12, 35, 1, 10, 34, 1] 
# largest=arr[0]
# second=-1

# for num in arr:
#     if num>largest:
#         second=largest
#         largest=num
#     elif num >second and num!=largest:
#         second=num
# print(second)

#min max in a given digit

# n=int(input("Enter the value:"))
# max_value=0
# min_value=978753
# while n>0:
#     digit=n%10
#     max_value=max(max_value,digit)
#     min_value=min(min_value,digit)
#     n=n//10
# print(max_value,min_value)


#Chat Moderation System
# s="hellllo"
# count=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         count=count+1
#         if count==3:
#             print("spam")
#             break
#     else:
#         count=1
# else:
#     print("safe")


#chocolate distribution
# n=7
# arr=list(map(int,input().split()))
# m=3
# arr.sort()
# min_diff=float("inf")
# for i in range(n-m+1):
#     diff=arr[i+m-1]-arr[i]
#     min_diff=min(min_diff,diff)
# print(min_diff)

# library fine Calculation

# n=5
# arr=list(map(int,input().split()))
# k=5
# fine=0 
# for days in arr:
#     if days>k:
#         fine=fine+days-k
# print(fine)

#bus passanger tracking
# n=int(input())
# current=0
# max_pass=0

# for i in  range(n):
#     off,on=map(int,input().split())
#     current=current-off
#     current=current+on
#     max_pass=max(max_pass,current)
# print(max_pass)


#size of array is given ,we create a list of array

# n=int(input("enter the size of array:"))
# arr=[]
# for i in range (n):
#     num=int(input("enter the list nums"))
#     arr.append(num)
# print(arr)

#space seperated array is given 
# arr=list(map(int,input().split()))
# print("array:",arr)

#comma seperated array is given 
# arr=list(map(int,input().split(",")))
# print("array:",arr)

#space seperated value is input    #input: 2 3
# r,s=map(int,input().split())
# print("no of rows:",r)
# print("no of column:",s)

#comma seperated value is input     #input: 2,3
# r,s=map(int,input().split(","))
# print("no of rows:",r)
# print("no of column:",s)

#Replace Elements by its rank in the array

# def replaceWithRank(arr):
#     rank_map={}
#     rank=1
#     for num in sorted (arr):
#         if num not in rank_map:
#             rank_map[num]=rank
#             rank=rank+1
#     return [rank_map[num] for num in arr]
# n=int(input().strip())
# arr=list(map(int,input().split()))
# result=replaceWithRank(arr)
# print(*result)  


#Remove character from first string present in second string
# def removeChars(str1,str2):
#     Remove_sets=set(str2)
#     result=[]
#     for ch in str1:
#         if ch not in Remove_sets:
#             result.append(ch)
#     return "".join(result)
# str1=input("str1:")
# str2=input("str2:")
# print(removeChars(str1, str2))


#leader in array
# def findleaders(arr):
#     n=len(arr)
#     leaders=[]
#     max_from_right=arr[-1]
#     leaders.append(max_from_right)
#     for i in range(n-2,-1,-1):
#         if arr[i]>= max_from_right:
#             max_from_right=arr[i]
#             leaders.append(arr[i])
#     return leaders[::-1]
# n=int(input().strip())
# arr=list(map(int,input().split()))
# result=findleaders(arr)
# print(*result)


#LONGEST SUBSTRING WITHOUT REPEATING CHAR
# def lengthOfString(s):
#     left=0
#     max_len=0
#     ch_set=set()
#     for right in range(len(s)):
#         while s[right] in ch_set:
#             ch_set.remove(s[left])
#             left=left+1
#         ch_set.add(s[right])
#         max_len=max(max_len,right-left+1)
#     return max_len
# s=input().strip()
# print(lengthOfString(s))

#Missing num in array
# n=int(input().strip())
# arr=list(map(int,input().split()))

# expected_sum=n*(n+1)//2
# actual_sum=sum(arr)

# print(expected_sum-actual_sum)
        