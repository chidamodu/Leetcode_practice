#For reference from career cup: Given "n", generate all valid parenthesis strings of length "2n". 
Example: 
Given n=2 

Output: 
(()) 
()()

def paren(left,right,string):
    if(left == 0 and right == 0):
        print (string)
    if(left>right):
        return
    if (left > 0):
        paren(left-1,right,string+"(")
    if (right > 0):
        paren(left,right-1,string+")")

def parentheses(n):
    paren(n/2,n/2,"")