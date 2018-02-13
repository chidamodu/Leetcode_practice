Given two strings, write a method to decide if one is a permutation of the other
Assume same number of elements in both strings
from collections import Counter
def permut_find(x, y):
    if len(x)==len(y):
        if Counter(x)==Counter(y):
            return True
        else:
            return False
    else:
        return False

To check whether two strings are permutations of each other:
import collections
def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())
example:
same_permutation('est-eem', 'teesme-')

Sorting without using sorted function
def sorting_list(k):
    new_list=[]
    while k:
        mini=k[0]
        for ele in k:
            #print(ele)
            if ele < mini:
                mini=ele
        #print(mini)
        new_list.append(mini)
        k.remove(mini)
    return new_list

Binary Search Algorithm
def binarySearch (arr, l, r, x):
    # Check base case
    if r >= l:
        mid = int(l + (r - l)/2)
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        # Element is not present in the array
        return -1
