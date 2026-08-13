
# You’re given an array of integers. Write a code to determine if there are three integers in the array whose sum equals a given value.

# [1,2,3,4,2,1], 6
#[1,1,2,2,3,4] 
# 1,2,3
# 1,4,1
# 1,1,2,2,3,4
# 1,1,4
# 1,1,3
# 1,1,2
# 1,2,4
# 1,2,3
# 1,2,2
# 2,2,4
# 2,2,3
# 2,3,4

def three_sum_variation(arr, target):
    arr = sorted(arr)
    triplets = set()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                triplets.add((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return print(triplets)


three_sum_variation([1,2,3,4,2,1], 6)
# ([0,1,1], 0)
# ([-1,0,1,2,-1,-4], 0)
# ([1,2,3,4,2,1], 6)
# ([0,0,0], 0)






