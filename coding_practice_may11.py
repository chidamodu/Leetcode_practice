class Solution:
    def isValid(self, s):
        brackets_map = {"[":"]","{":"}","(":")"}
        stack=[]
        if len(s)==0:
            return True
        for b in range(len(s)):
            if s[b] in brackets_map:
                stack.append(s[b])
            elif not stack:
                return False
            elif brackets_map[stack.pop()]!=s[b]:
                return False
        return not stack
