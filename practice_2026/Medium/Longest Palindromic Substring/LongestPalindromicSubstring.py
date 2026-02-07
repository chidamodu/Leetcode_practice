"""
Longest Palindromic Substring (Medium)
URL: https://leetcode.com/problems/longest-palindromic-substring/
Saved on: February 4, 2025

Problem Description:
Given a string s, return the longest palindromic substring in s.

Examples:
    Example 1:
        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

    Example 2:
        Input: s = "cbbd"
        Output: "bb"

Constraints:
    - 1 <= s.length <= 1000
    - s consists of only digits and English letters.
"""


def expand_left_right(left, right, s):
    while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
        left -= 1
        right += 1
    return left, right - left + 1


def longestPalindrome(s: str) -> str:
    start = 0
    max_len = 0
    for i in range(len(s)):
        # odd base case
        odd_start, odd_len = expand_left_right(i, i, s)
        if odd_len > max_len:
            max_len = odd_len
            start = odd_start
        # even base case
        if i < len(s) - 1 and s[i] == s[i + 1]:
            even_start, even_len = expand_left_right(i, i + 1, s)
            if even_len > max_len:
                max_len = even_len
                start = even_start
    return s[start : start + max_len]
