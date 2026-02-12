# Remove Duplicates from Sorted Array II (Medium)

**URL:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears **at most twice**. The relative order of the elements should be kept the same.

Return `k` after placing the final result in the first `k` slots of `nums`. Do not allocate extra space—modify the array in-place with O(1) extra memory.

## Examples

### Example 1
- **Input:** `nums = [1,1,1,2,2,3]`
- **Output:** `5`, nums = `[1,1,2,2,3,_]`

### Example 2
- **Input:** `nums = [0,0,1,1,1,1,2,3,3]`
- **Output:** `7`, nums = `[0,0,1,1,2,3,3,_,_]`

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.
