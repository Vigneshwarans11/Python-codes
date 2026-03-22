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



#Valid Capital Usage Conditions:
# def checkCapitalletters(word):
#     if word.isupper():
#         return True
#     elif word.islower():
#         return True
#     elif word[0].isupper() and word[1:].islower():
#         return True
#     else:
#         return False
# word=input("enter the word:")
# result=checkCapitalletters(word)
# print(result)     


# all are upper or lower case or 1st letter is upper and nxt or lower or if change one letter is upper pr lower its true eg(Flag-flag  or leetcOde - leetcode)  
# def letterchange(word):
#     upper=0
#     lower=0

#     for ch in word:
#         if ch.isupper():
#             upper=upper+1
#         else:
#             lower=lower+1

#     if upper==len(word) or lower==len(word):
#         return True
#     elif ch[0].isupper() and ch[1:].islower():
#         return False
#     elif upper==1 or lower==1:
#         return True
#     return False

# word=input("enter the word:")
# print(letterchange(word))

# all are upper or lower case or 1st letter is upper and nxt or lower or and also (FlaG - Flag 1st letter is upper nxt we can change in one letter is ok )
# def lettercheck(word):
#     def iscorrect(w):
#         return(
#             w.isupper() or
#             w.islower() or
#             (w[0].isupper() and w[1:].islower())
#             )
#     if iscorrect(word):
#         return True
    
#     for i in range(len(word)):
#         if word[i].isupper():
#             new_word=word[:i] + word[i].lower() + word[i+1:]
#         else:
#             new_word=word[:i] + word[i].upper() + word[i+1:]

#         if iscorrect(new_word):
#             return True
#     return  False

# word=input("enter the word:")
# print(lettercheck(word))



# Given a binary string s, return the number of substrings with all characters 1's

# Example 1:

# Input: s = "0110111"
# Output:9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" ->3 times.
# "111" -> 1 time.

# def countnumbers(s):
#     count=0
#     current=0
#     for ch in s:
#         if ch =="1":
#             current=current+1
#             count=current+count
#         else:
#             current=0
#     return count

# s=input("numbers:")
# print(countnumbers(s))

# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

# Return the number of bulbs that are on after n rounds.

# Input: n = 3
# Output: 1

# def bulbswitch(n):
#     bulb=[False] * n

#     for i in range(1,n+1):
#         for j in range(i-1,n,i):
#             bulb[j]=not bulb[j]

#     count=0
#     for b in bulb:
#         if b:
#             count=count+1
#     return count

# n=int(input("enter the num:"))
# print(bulbswitch(n))

