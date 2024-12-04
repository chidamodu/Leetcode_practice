
def addSpaces(s, spaces):
    m, n = len(s), len(spaces)
    t = [" "]*(m+n)
    j = 0
    for ind, val in enumerate(s):
        if j < n and ind == spaces[j]:
            j += 1
        t[j+ind] = s[ind]
    print("".join(t))

addSpaces("LeetcodeHelpsMeLearn", [8,13,15])


Official submission on Leetcode

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n = len(s), len(spaces)
        t = [" "]*(m+n)
        j = 0
        for ind, val in enumerate(s):
            if j < n and ind == spaces[j]:
                j += 1
            t[j+ind] = s[ind]
        return "".join(t)







# for i in range(len(spaces)):
#     if i == 0:
#         s = s[:spaces[i]] + " " + s[spaces[i]:]
#
#     else:
#         s = s[:spaces[i]+i] + " " + s[spaces[i]+i:]
#
# print(s)




