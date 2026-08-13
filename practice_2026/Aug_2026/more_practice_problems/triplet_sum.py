
import unittest
#target=0
# def triplet_sum(arr):
#     arr = sorted(arr)
#     result =[]
#     for i in range(len(arr)):
#         if i > 0 and arr[i] == arr[i-1]:
#             continue
#         left = i + 1
#         right = len(arr) - 1
#         while left < right:
#             tot_val = arr[i] + arr[left] + arr[right]
#             if tot_val == 0:
#                 result.append([arr[i], arr[left], arr[right]])
#                 left += 1
#                 right -= 1
#                 while left < right and arr[left] == arr[left-1]:
#                     left += 1
#                 while left < right and arr[right] == arr[right+1]:
#                     right -= 1
#             elif tot_val < 0:
#                 left += 1
#             else:
#                 right -= 1
#     return print(result)


def triplet_sum(arr, target):
    arr = sorted(arr)
    result =[]
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i + 1
        right = len(arr) - 1
        while left < right:
            tot_val = arr[i] + arr[left] + arr[right]
            if tot_val == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif tot_val < 0:
                left += 1
            else:
                right -= 1
    return result

# triplet_sum([0, 1, -2, 2, -1, 0, 0], 0)
# triplet_sum([9, 1, -2, 4, -3, 8, 0], 0)

class TestTripletSum(unittest.TestCase):
    def test_empty_triplet(self):
        result = triplet_sum([9, 1, -2, 4, -3, 8, 0], 0)
        self.assertFalse(result)

    def test_assert_empty_triplet(self):
        result = triplet_sum([9, 1, -2, 4, -3, 8, 0], 0)
        self.assertEqual(result, [])

    def test_empty_array(self):
        result = triplet_sum([-1, 1], 0)
        self.assertEqual(result, [])

    def test_no_triplet(self):
        result = triplet_sum([1, 0, 1], 0)
        self.assertEqual(result, [])

    def test_duplicate_triplets(self):
        result = triplet_sum([0, 0, 1, -1, 1, -1], 0)
        self.assertCountEqual(result, [[-1, 0, 1]])

    def test_all_zeros_array(self):
        result = triplet_sum([0, 0, 0], 0)
        self.assertEqual(result, [[0, 0, 0]])

if __name__ == '__main__':
    unittest.main()
