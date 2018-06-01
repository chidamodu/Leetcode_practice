Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
class Solution():
    def singleNumber(self, nums):
        d={}
        c=0
        for i in nums:
            d[i]=d.get(i, 0)+1
        for k, v in d.items():
            if v==1:
                return (k)


Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Examples:
Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false

class Solution(object):
    def isPalindrome(self, s):
        s=re.sub(r'[^\w\s]+','',s).replace(" ", "").lower()
        res=re.sub(r'[^\w\s]+','',s).replace(" ", "").lower()
        if res[::-1]==s:
            return True
        else:
            return False
