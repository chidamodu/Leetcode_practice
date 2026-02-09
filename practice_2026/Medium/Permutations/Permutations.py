"""
Permutations (Medium)
URL: https://leetcode.com/problems/permutations/

Problem Description:
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Examples:
    Example 1:
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Example 2:
        Input: nums = [0,1]
        Output: [[0,1],[1,0]]

    Example 3:
        Input: nums = [1]
        Output: [[1]]

Constraints:
    - 1 <= nums.length <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique.
"""

from itertools import permutations


# Solution 1: itertools.permutations
def permute_itertools(nums):
    return [list(perm) for perm in permutations(nums)]


# Solution 2: Backtracking
def permute(nums):
    result = []
    backtrack([], set(), nums, result)
    return result


def backtrack(candidate, used_nums, nums, result):
    if len(candidate) == len(nums):
        result.append(candidate[:])
        return
    for num in nums:
        if num not in used_nums:
            candidate.append(num)
            used_nums.add(num)
            backtrack(candidate, used_nums, nums, result)
            candidate.pop()
            used_nums.remove(num)
