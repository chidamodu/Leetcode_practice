#Reverse Integer
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
#For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        self.x=x
        if self.x <0:
            return -self.reverse(-x)
        while self.x:
            rev=(10*rev)+self.x%10
            self.x //= 10
        return rev if rev <= 0x7fffffff else 0

#my idea: by using groupby on a list of integers and then apply permutation on them and then the final groupby to get rid of duplicates
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero. The solution set must not contain duplicate triplets.
class Solution():
  def threeSum(self, nums):
      from itertools import permutations
      import operator
      from itertools import groupby
      answer=[]
      self.nums=nums
      if len(self.nums) > 3:
          a = [k for k, v in list(groupby(self.nums))]
                #print(a)
        res=list(permutations(a, 3))
        for ele in res:
            if sum(ele) ==0:
                answer.append(ele)
                return ([k for k, v in groupby(sorted(answer, key=sorted), key=sorted)])
            elif len(self.nums) < 3:
                return []
            else:
                return [self.nums]

if __name__ == "__main__":
    s = Solution()


#algorithm:to find indices of two numbers from the list of integers such that adding those two numbers will be equivalent
#to target
# a list of integers is given as input
# current previous - index
# as soon as u get the target adding two numbers then break
# otherwise continue
def twoSum(nums, target):
    s=0
    for i in range(len(nums)-1):
        current_index=i
        next_index=i+1
        if nums[current_index]+nums[next_index]==target:
            break

        else:
            continue
    return [current_index, next_index]
twoSum([2,3,4,5], 8)

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Solution():
    def twoSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for z in range(i+2, len(nums)):
                    if nums[i] + nums[j] + nums[z]== 0:
                        return [nums[i], nums[j], nums[z]]

if __name__ == "__main__":
    a = Solution()
a.twoSum([5,-9,-11,9,9,-4,14,10,-11,1,-13,11,10,14,-3,-3,-4,6,-15,6,6,-13,7,-11,-15,10,-8,13,-14,-12,12,6,-6,8])
