# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
 
# Constraints:
# -231 <= x <= 231 - 1

def reverse(x):
    reverse_result = ""

    if x < 1:
        reverse_result += '-'
        if str(x)[1:]:
            print(str(x)[1:])
            x = int(str(x)[1:])
        else:
            return 0
    while x:    
            reverse_result += str(x % 10)
            x = x // 10
    print(int(reverse_result))
    return print(int(reverse_result)) if -2**31 <= int(reverse_result) <= 2**31 - 1 else print(0)

reverse(2340)





