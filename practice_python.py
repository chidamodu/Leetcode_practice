Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""

from itertools import takewhile
class Solution:
    def longestCommonPrefix(self, strs):
        return ''.join(map(lambda strs: strs[0],takewhile(lambda strs: len(set(strs)) == 1,zip(*strs))))#takewhile:Make an iterator that returns elements from the iterable as long as the predicate is true.

# takewhile is roughly equivalent to:
# def takewhile(predicate, iterable):
#     # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
#     for x in iterable:
#         if predicate(x):
#             yield x
#         else:
#             break

#very interesting use case using os.path for longest common prefix
import os
os.path.commonprefix(["flower","flow","flight"])

#for the same problem an algorithmic way of solution
class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]#to return an empty string in case of strs=[""] in other words to avoid returning null(no output at all) as output
