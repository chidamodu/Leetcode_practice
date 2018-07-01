# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

class Solution:
    def searchInsert(self, nums, target):
        if len(nums)==0: return 0
        elif target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
            return len(nums)

#final accepted solution on Leetcode: 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
# The solution set must not contain duplicate triplets.

from itertools import groupby
class Solution():
    def threeSum(self, nums):
        res=[]
        num=sorted(nums)
        
        if len(num)<3:
            return []
        
        elif len(set(num))==1 and 0 not in set(num):
            return []  
        
        elif (len(num)==3 and len(set(num))==1 and 0 in set(num)) or len(num)> 3 and  len(set(num))==1 and 0 in set(num):
            return ([[0,0,0]])
           
        else:
            n=len(num)
            for i in range(0, n-2):
                a=num[i]
                start=i+1
                end=n-1
                while start < end:
                    b=num[start]
                    c=num[end]
                    s= a+b+c
                    if s > 0:
                        end-=1
                    elif s < 0:
                        start+=1
                    else:
                        res.append(([a, b, c]))
                        start+=1       
        return [k for k, v in groupby(sorted(res, key=sorted), key=sorted)]