

def pair_sum_sorted(arr, target):
    d = {}
    for i, v in enumerate(arr):
        if target-v in d:
            return print([i, d[target-v]])
        d[v] = i
    return print([])

#taking advantage of the sorted array attribute
def pair_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        sum_val = arr[left] + arr[right]
        if sum_val == target:
            return [left, right]
        elif sum_val < target:
            left += 1
        else:
            right -= 1
    return print([])

pair_sum_sorted([-5, -2, 3, 4, 6], target = 7)