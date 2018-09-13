#Buddy Strings
#Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

#Here I have considered only the last two elements, meaning only the last two characters in A are reversed (along with the rest of A up until the last two elements)
#and verified whether they are equivalent to B

class Solution:
    def buddyStrings(self, A, B):
        if A=="" or B=="":
            return False
        elif len(A) != len(B):
            return False
        elif (len(A)>=2 and len(A)<= 20000) and (len(B)>=2 and len(B)<= 20000):
            res=''.join((A[:-2], A[-2:][::-1]))
            if res==B:
                return True
            else:
                return False




