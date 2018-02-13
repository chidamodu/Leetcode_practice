algorithm:to find indices of two numbers from the list of integers such that adding those two numbers will be equivalent
to target
pseudo:
a list of integers is given as input
current previous - index
as soon as u get the target adding two numbers then break otherwise continue

class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = []
        self.target = int

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

if __name__ == "__main__":
    a = Solution()

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
class Solution():
    def threeSum(self, nums):
        from itertools import permutations
        import operator
        from itertools import groupby
        answer=[]
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums=nums
        if len(self.nums) > 3:
            a = [k for k, v in list(groupby(self.nums))]
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

Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer. Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
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
