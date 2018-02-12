Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
example:
Input: 121
Output: true
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            if str(x)[::-1] == x:
            return True
        else:
            return False

To reverse an integer without converting it to string:
class Solution:
    def isPalindrome(self, x):
        ori=x
        res=0
        if x<0:
            return False
        while x > 0:
            res = (res*10)+ (x % 10)
            x//=10
        if res == ori:
            return True
        return False

Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

# pseudo:
# find the smallest of all strings in the list:
# answ=[]
# if s1[0]==s2[0]==s3[0]:
#     answ.append(s1[0])
#     for i in range(1, len(smallest_string)):
#         if s1[i] == s2[i] == s3[i]:
#             answ.append(s1[i])
#         else:
#             break
# else:
#     return ("there are no common prefix")

class Solution:
    def longestCommonPrefix(self, strs):
        #print(len(strs))
        answ=[]
        res_len=[]
        for i in strs:
            res_len.append(len(i))
#         print(res_len)
        for y in range(0, min(res_len)):
            if min(res_len) > 0:
                if strs[0][y]==strs[1][y] and strs[1][y]==strs[-1][y]:
                    answ.append(strs[0][y])
                else:
                    break
            else:
                return "String cannot be empty!"
        return ''.join(answ)
