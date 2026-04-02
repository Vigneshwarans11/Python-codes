# Reverse a String Without Using Built-in Functions
# s="hello"
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev=rev+s[i]
# print(rev)
# for i in s:
#     rev=i+rev
# print(rev)
 
# Two pointers:
# S=list("hello")
# left = 0
# right=len(S)-1

# while left<right:
#     S[left],S[right]=S[right],S[left]
#     left=left+1
#     right=right-1
#     result="".join(S)
# print(result)


# Reverse Each Word in a Sentence
# s=("hello world")
# word=s.split()
# result=""

# for i in word:
#     rev=""
#     for ch in i:
#         rev=ch+rev
#     result=result+rev+" "
# print(result.strip())

# Check Palindrome Using Reverse
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

# min max in a given digit
# n=int(input("Enter the value:"))
# max_value=0
# min_value=9
# while n>0:
#     digit=n%10
#     max_value=max(max_value,digit)
#     min_value=min(min_value,digit)
#     n=n//10
# print(max_value,min_value)


# Chat Moderation System
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


# chocolate distribution
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

# bus passanger tracking
# n=int(input())
# current=0
# max_pass=0

# for i in range(n):
#     off,on=map(int,input().split())
#     current=current-off
#     current=current+on
#     max_pass=max(max_pass,current)
# print(max_pass)


# size of array is given ,we create a list of array

# n=int(input("enter the size of array:"))
# arr=[]
# for i in range (n):
#     num=int(input("enter the list nums"))
#     arr.append(num)
# print(arr)

# space seperated array is given 
# arr=list(map(int,input().split()))
# print("array:",arr)

# comma seperated array is given 
# arr=list(map(int,input().split(",")))
# print("array:",arr)

# space seperated value is input    #input: 2 3
# r,s=map(int,input().split())
# print("no of rows:",r)
# print("no of column:",s)

# comma seperated value is input     #input: 2,3
# r,s=map(int,input().split(","))
# print("no of rows:",r)
# print("no of column:",s)

# Replace Elements by its rank in the array

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


# Remove character from first string present in second string
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


# leader in array
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


# LONGEST SUBSTRING WITHOUT REPEATING CHAR
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

# Missing num in array
# n=int(input().strip())
# arr=list(map(int,input().split()))

# expected_sum=n*(n+1)//2
# actual_sum=sum(arr)

# print(expected_sum-actual_sum)



# Valid Capital Usage Conditions:
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

# Question 1: Multi-Tier Discount Logic Problem: Calculate the final price based on the total bill amount.
# 0 - 1000: 5% discount
# 1001 - 5000: 10% discount
# | 5000: 15% discount
# Logic:
#  we need to return
# "Error" when money is negative.

# def finalprice(amount):
#     if amount<0:
#         return "error"
#     elif amount<1000:
#         discount=0.05
#     elif amount<5000:
#         discount=0.10
#     else:
#         discount=0.15
#     final = amount-(amount*discount)
#     return final

# amount=float(input("enter the amount:"))
# print(finalprice(amount))



# def gymprice(month):
#     if month<=0:
#         return "invalid input"
#     elif month == 1:
#         return 2000
#     elif month>=2 and month<=3:
#         return 5000
#     elif month>=4 and month <=6:
#         return 9000
#     elif month>6:
#         return 15000
# month=int(input("enter the month:"))
# print(gymprice(month))


# parking fine
# def parkingcharges(hours):
#     if hours<=0 or 1<=hours>=24:
#         return "error"
#     elif hours<=2:
#         return hours*100
#     elif hours>=3 and hours<=5:
#         return 200+(hours-2)*50
#     elif hours>5:
#         return 200+150+(hours-5)*20
#     return "error"

# hours=int(input("enter the hours:"))
# print(parkingcharges(hours))

#              or 
# def parkingcharge(s):
#     if s<1 or s>24:
#         return "error"
    
#     total=0
    
#     for i in range(1,s+1):
#         if i<=2:
#             total=total+100
#         elif i>=3 or i<=5:
#             total=total+50
#         else:
#             total=total+20
#     return total

# s=int(input("hours:"))
# print(parkingcharge(s))

# def electricbill(unit):
#     if unit<0:
#         return "error"
#     total=0
        
#     for i in range(1,unit+1):
#         if i>=0 and i<=100:
#             total=total+5
#         elif i>=101 and i<=200:
#             total =total+7
#         else:
#             total=total+10
#     return total
    
# unit=int(input("entert the units:"))
# print(electricbill(unit))

# # max pasanger in ballon with a weight
# n=5
# arr=[45,65,50,55,75]
# m=200
# count=0
# total=0
# for num in arr:
#     if num<m:
#         total=total+num
#         if total<m:
#             count=count+1
# print(count)

# n=5
# arr=[45,65,50,55,75]
# m=200
# count=0
# total=0
# for num in arr:
#     if total+num<=m:
#         total=total+num
#         count=count+1
#     else:
#         break
# print(count)

# def passanger_ballon(n,arr,m):
#     count=0
#     total=0
#     arr.sort()
    
#     for num in arr:
#         if total+num<=m:
#             total=total+num
#             count=count+1
#     return count
# n=int(input("enter the no of passanger:"))
# arr=list(map(int,input("enter the weight").split()))
# m=int(input("max weight:"))
# print(passanger_ballon(n,arr,m)) 

# def checktransaction(transactions):
#     seen=[]

#     for i in range(len(transactions)):
#         sender=transactions[i][0]
#         reciver=transactions[i][1]
#         time=transactions[i][2]
        
#         if (sender,reciver) in seen:
#             return "transaction failed"
#         seen.append(sender,reciver)

#         if i>0:
#             prev_time=transactions[i-1][2]
#             if time-prev_time>60:
#                 return "fraud detection"
#         return "all transaction true"

# n=int(input("enter the num of transaction:"))
# transactions=[]
# for _ in range(n):
#     sender,reciver,time=input().split()
#     transactions.append(sender,reciver,time)
# print(transactions)
# for s,r,t in transactions:
#     print(s,r,t)

# gym membership

# def gym(month):
#     if month<=0:
#         return "invalid input"
#     if month==1:
#         cost=2000
#     elif month>=2 and month<=3:
#         cost=5000
#     elif month>=4 and month<6:
#         cost=9000
#     else:
#         cost=15000
#     return cost
# month=int(input("enter the month:"))
# print(gym(month))

# def selection_sort(arr):
#     n=len(arr)
#     for i in range (n):
#          min_indx=i
#          for j in range(i+1,n):
#               if (arr[j][0]<arr[min_indx][0] or 
#                   (arr[j][0]==arr[min_indx][0] and arr[j][1]<arr[min_indx][1])):
#                    min_indx=j
#          arr[i],arr[min_indx]=arr[min_indx],arr[i]
#     return arr

# n=int(input("enter the arr:"))
# arr=[]
# for i in range (n):
#      a,b=map(int,input().split())
#      arr.append((a,b))
# print(selection_sort(arr))
# for a,b in arr:
#     print(a,b)


# #Login Monitoring System
# def checklogin(record):
#     seen = []

#     for i in range(len(record)):
#         user = record[i][0]
#         time = record[i][1]
#         # Duplicate login
#         if user in seen:
#             return "Duplicate Login"
#         seen.append(user)
#         # Suspicious login (within 30 sec)
#         if i > 0:
#             prev_time = record[i-1][1]
#             if time - prev_time < 30:
#                 return "Suspicious Login"
#     return "All Logins Valid"
# n = int(input("Enter number of records: "))
# record = []
# for i in range(n):
#     user, time = map(int, input().split())
#     record.append((user, time))
# print(checklogin(record))
# for u,i in record:
#     print(u,i)


# Student_mark analysis
# def students_marks(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i        
#         for j in range(i+1,n):
#             if (arr[j][0] < arr[min_index][0] or (arr[j][0]==arr[min_index][0] and arr[j][1]<arr[min_index][1])):
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
    
# n=int(input("enter the value:"))
# arr=[]
# for i in range(n):
#     mark,age=map(int,input("Enter marks and age:").split())
#     arr.append((mark,age))
# print(students_marks(arr))
# for m, a in arr:
#     print(m, a)

# Given N=4 Arr[20,25,30,35] These are prices of ticket in movie theatre We have to find all odd prices And then output Sum of odd prices, count of odd prices and average of odd prices Example output 60 2 30.00
# n=4
# arr=[20,25,30,35]
# count=0
# sum_num=0
# avg=0
# for num in arr:
#     if num%2!=0:
#         count=count+1
#         sum_num=sum_num+num
#         avg=sum_num//count
# print(sum_num,count,format(avg,".2f"))


# def find_pair(arr,target):
#     left=0
#     right=len(arr)-1

#     while left<right:
#         current_num=arr[left]+arr[right]
#         if current_num==target:
#             return (arr[left],arr[right])
#         elif current_num < target:
#             left =left +1
#         else:
#             right=right-1
#     return False

# arr=list(map(int,input().split()))
# target=int(input("enter the target:"))
# result=find_pair(arr,target)
# if result:
#     print("pair exist",result)    
# else:
#     print("not exist")
        
# def find_count(arr,target):
#     left=0
#     right=len(arr)-1
#     count=0

#     while left<right:
#        current_num=arr[left]+arr[right]
#        if current_num == target:
#            count=count+1
#            right=right-1
#            left=left+1
#         elif current_num<target:
#             left=left+1
#         else:
#             right=right-1
#     return count

# arr=list(map(int,input().split()))
# target=int(input("enter the target:"))
# print(find_count(arr,target))

# def find_pair(arr, target):
#     left = 0
#     right = len(arr) - 1
#     count = 0
#     arr1 = []
#     while left < right:
#         current_num = arr[left] + arr[right]
#         if current_num == target:
#             arr1.append((arr[left], arr[right]))  # ✅ store first
#             count += 1
#             left += 1
#             right -= 1
#         elif current_num < target:
#             left += 1
#         else:
#             right -= 1
#     return count, arr1
# arr = list(map(int, input().split()))
# target = int(input("enter the target: "))

# result = find_pair(arr, target)
# print("Result:", result)



# def internet_plan(n):
#     price=0

#     if n==0:
#         return "no usage"
#     elif n<0:
#         return "negative"
#     if n<=10:
#         price=price+n*20
#     elif n<=50:
#         price=(price+10*20)+(n-10)*15
#     elif n<=100:
#         price =(price+10*20)+(price+40*15)+(n-50)*10
#     else:
#         price=(price+10*20)+(price+40*15)+(price+50*10)+(n-100)*5

#     final= price+price*18/100
#     return f"{final:.2f}"
# n=60
# print(internet_plan(n))

# def hospital_bill(days):
#     bill=0
#     for d in range(1,days+1):
#         if days<0:
#             return "invalid days"
#         if days==1:
#             bill = 1500+500
#         elif days<=5:
#             bill = days*(1200+400)
#         elif days<=10:
#             bill = days*(100+300)
#         else:
#             bill=days*(800+200)
#     with_insurance=bill*0.7
#     return bill,with_insurance

# days=3
# print(hospital_bill(days))
    
# def scholarship_amt(n, mark, m):
#     if m > n:
#         return "insufficient students"
    
#     if any(x < 0 or x > 100 for x in mark):
#         return "invalid marks"
    
#     mark.sort()
#     min_diff = float("inf")
#     output = ""

#     for i in range(n - m + 1):
#         total=mark[i:i+m]
#         avg = sum(mark[i:i+m]) / m
#         diff=mark[i+m-1]-mark[i]

#         if avg >= 90:
#             output = "50000"
#         elif avg >= 75:
#             output = "35000"
#         elif avg >= 60:
#             output = "20000"
#         else:
#             output = "10000"

#         min_diff = min(min_diff, diff)
#     return min_diff,output
# n = int(input("enter the students: "))
# mark = list(map(int, input("enter the marks: ").split()))
# m = int(input("enter the taken students: "))
# out1,out2=(scholarship_amt(n, mark, m))
# print(out1)
# print(out2)

# def scholarship_amt(n,mark,m):
#     if m>n:
#         return "insuffecient students"
#     if mark<0 or mark>100:
#         return "invalid marks"
    
#     mark.sort()
#     min_diff = float("inf")
#     for num in range(n-m+1):
#         if num>0:
#             total=mark[i]+mark[i+1]+mark[i+2]
#             avg=total/3
#                 if avg==sum(mark[i+m-1]-mark[i])/3:
#                     return "equal marks group selected"
#                 elif avg>=90:
#                     diff=mark[i+m-1]-mark[i]
#                     min_diff=min(min_diff,diff)
#                     output="50000"
#                     break
#                  elif avg>=75:
#                     diff=mark[i+m-1]-mark[i]
#                     min_diff=min(min_diff,diff)
#                     output="35000"
#                     break
#                  elif avg>=60:
#                     diff=mark[i+m-1]-mark[i]
#                     min_diff=min(min_diff,diff)
#                     output="20000"
#                     break
#                  elif avg<60:
#                     diff=mark[i+m-1]-mark[i]
#                     min_diff=min(min_diff,diff)
#                     output="10000"
#     return min_diff
#     return output
# n=int(input("enter the students:"))
# mark=list(map(int,input("enter the marks")))
# m=int(input("enter the taken students"))
            
# def frequency_num(arr):
#     number={}
#     arr1=sorted(arr)
    
#     for num in arr1:
#         if num not in number:
#             number[num]=1
#         elif num in number:
#             number[num]+=1
#     result=[]
#     for num in arr:
#         result.append(number[num])
#     return result
# n=int(input("enter the numbers:"))
# arr=list(map(int,input().split()))
# print(frequency_num(arr))
        
# def count_num(s):
#     count_0=0
#     count_1=0
#     current_0=0
#     current_1=0
    
#     for ch in s:
#         if ch == "0":
#             current_0=current_0+1
#             count_0=count_0+current_0
#         else:
#             current_0=0
            
#         if ch=="1":
#             current_1=current_1+1
#             count_1=count_1+current_1
#         else:
#             current_1=0
#         length=count_0+count_1
#     return length
# s=input("enter the string:") #00111
# print(count_num(s))      # 9  