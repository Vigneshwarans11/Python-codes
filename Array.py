#1 Second Largest Element in an Array 

#using sort method
# arr=[10,5,20,39]
# arr.sort()
# print(arr[-2])

#without sorting
# arr = [12, 35, 1, 10, 34, 1]

# largest=second=-1
# for num in arr:
#     if num > largest:
#         second=largest
#         largest=num
#     elif num>second and num!=largest:
#         second=num
# print(second)

# arr = [12,35, 1, 10, 34, 1]
# arr=list(set(arr))
# arr.sort()

# if len(arr)<2:
#     print(arr[-1])
# else:
#     print(arr[-2])


#2 Find the Missing Number (1 to N) 
# You are given an array of N-1 distinct integers taken from 1 to N. Find the one missing number using the sum formula or XOR. 
# Sample Input: arr = [1, 2, 4, 5, 6], N = 6 
# Expected Output: 3

# arr=[1,2,4,5,6]
# N=6
# expect_sum=N*(N+1)//2
# actual_sum = sum(arr)

# missing =expect_sum - actual_sum
# print(missing)

# arr=[1,2,4,5,6]
# n=6
# for i in range(1,n+1):
#     if i not in arr:
#        print(i)

# Move All Zeros to the End  
# Given an integer array, move all 0s to the end while maintaining the relative order of non-zero elements. Do it in-place.
# Sample Input: arr = [0, 1, 0, 3, 12] 
# Expected Output: [1, 3, 12, 0, 0] 

# arr = [0, 1, 0, 3, 12]
# pos=0
# for i in range(len(arr)):
#     if arr[i]!=0:
#         arr[pos]=arr[i]
#         pos=pos+1
# for i in range(pos,len(arr)):
#     arr[i]=0
# print(arr)