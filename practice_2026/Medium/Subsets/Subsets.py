"""
Subsets (Medium)
URL: https://leetcode.com/problems/subsets/
Saved on: February 3, 2025

Problem Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
    Example 1:
        Input: nums = [1,2,3]
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Example 2:
        Input: nums = [0]
        Output: [[],[0]]

Constraints:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10
    - All the numbers of nums are unique.
"""

from itertools import combinations


# Solution 1: Cascading approach
def subsets_cascading(nums):
    result = [[]]
    for num in nums:
        for i in range(len(result)):
            result.append(result[i] + [num])
    return result


# Solution 2: itertools.combinations
def subsets_combinations(nums):
    d = []
    for i in range(len(nums) + 1):
        for combo in combinations(nums, i):
            d.append(list(combo))
    return d


# Solution 3: Backtracking
def subsets_backtracking(nums):
    result = []

    def backtrack(start, subset):
        if start == len(nums):
            result.append(subset[:])
            return
        subset.append(nums[start])
        backtrack(start + 1, subset)
        subset.pop()
        backtrack(start + 1, subset)

    backtrack(0, [])
    return result


# LeetCode expects function named 'subsets' - use any of the above
def subsets(nums):
    return subsets_cascading(nums)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print("Solution 1 (Cascading):", subsets_cascading(nums))
    print("Solution 2 (Combinations):", subsets_combinations(nums))
    print("Solution 3 (Backtracking):", subsets_backtracking(nums))
