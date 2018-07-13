# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Note:
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend, divisor):
        
        quotient = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        #res = 0
        p = abs(dividend)
        q = abs(divisor)
        if divisor == 0 or (divisor == 1 and dividend >= INT_MAX) :
            return INT_MAX
        
        elif dividend <= INT_MIN and divisor == -1 :
            return INT_MAX
        
        elif abs(divisor) == 1 :
            return dividend * divisor
        
        else:
            while (p >= q): 
                p -= q
                quotient += 1
     
        if ((dividend < 0) and  (divisor < 0)) or ((dividend > 0) and  (divisor > 0)):
            sign=1
        
        elif (dividend < 0) or  (divisor < 0):
            sign = -1
       
        
        return sign * quotient


