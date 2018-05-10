In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

# Intuition
# We scan through the string to identify the start and end of each group. If the size of the group is at least 3, we add it to the answer.
#
# Algorithm
# Maintain pointers i, j with i <= j.
# The i pointer will represent the start of the current group, and we will increment j forward until it reaches the end of the group.
# We know that we have reached the end of the group when j is at the end of the string, or S[j] != S[j+1].
# At this point, we have some group [i, j]; and after, we will update i = j+1, the start of the next group.

class Solution():
    def largeGroupPositions(self, s):
        ans=[]
        i=0
        for j in range(len(s)):
            if j==len(s)-1 or s[j] != s[j+1]:
                if j-i+1 >=3:
                    ans.append([i, j])
                i=j+1
        return ans

Masking Personal Information
We are given a personal information string S, which may represent either an email address or a phone number.
We would like to mask this personal information according to the following rules:
# 1. Email address:
# We define a name to be a string of length ≥ 2 consisting of only lowercase letters a-z or uppercase letters A-Z.
# An email address starts with a name, followed by the symbol '@', followed by a name, followed by the dot '.' and followed by a name.
# All email addresses are guaranteed to be valid and in the format of "name1@name2.name3".
# To mask an email, all names must be converted to lowercase and all letters between the first and last letter of the first name must be replaced by 5 asterisks '*'.
# 2. Phone number:
# A phone number is a string consisting of only the digits 0-9 or the characters from the set {'+', '-', '(', ')', ' '}. You may assume a phone number contains 10 to 13 digits.
# The last 10 digits make up the local number, while the digits before those make up the country code. Note that the country code is optional. We want to expose only the last 4 digits and mask all other digits.
# The local number should be formatted and masked as "***-***-1111", where 1 represents the exposed digits.
# To mask a phone number with country code like "+111 111 111 1111", we write it in the form "+***-***-***-1111".  The '+' sign and the first '-' sign before the local number should only exist if there is a country code.  For example, a 12 digit phone number mask should start with "+**-".
# Note that extraneous characters like "(", ")", " ", as well as extra dashes or plus signs not part of the above formatting scheme should be removed.
# Return the correct "mask" of the information provided.

import re
class Solution():
    def maskPII(self, S):
        if re.findall(r'[\w\.-]+@[\w\.-]+', S):
            S=S.lower().lstrip(" ").rstrip(" ")
            s1, s2=S.split("@")
            s1=s1[0]+'*****'+s1[-1]
            return s1+'@'+s2
        else:
            S=re.sub('[^0-9]+', '', S)
            if len(S)==10:
                S=S.replace(S[:-4], "***-***-")
                return S[:-4]+S[-4:]
            else:
                S2=S[-10:]
                S2=S2.replace(S2[:-4], "***-***-")
                leftover=len(S[:-10])
                S1='+'+'*'*leftover
            return S1+'-'+S2
