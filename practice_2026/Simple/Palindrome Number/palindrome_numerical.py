

def isPalindrome(x):
    new_x = x
    result = 0
    print(x)
    if x < 0:
        return print(False)
    
    while new_x > 0:
        result *= 10
        result += (new_x % 10)
        new_x = (new_x // 10)
    
    if result == x:
        return print(True)
    
    return print(False)

isPalindrome(121)
