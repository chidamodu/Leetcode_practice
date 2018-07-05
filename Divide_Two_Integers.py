# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Note:
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend, divisor):
        c=1
        
        if divisor == 0:
            return "Divisor cannot be equal to 0"
        
        elif divisor == dividend:
            return 1 
        
        elif divisor==1: 
            return -dividend if dividend < 0 else dividend
        
        elif divisor==-1:
            return dividend if dividend < 0 else -dividend
        
        else:
            if divisor<0:
                res=dividend+divisor   
            else:
                res=dividend-divisor   
        
            if res==0:
                return 1

            elif res <= 0:
                return 0
        
            else:
                while res > 0 and res != 1: 
                    if divisor < 0:
                        res+=divisor
                    else:
                        res-=divisor
                    c+=1
        
        return c if divisor>0 else -c