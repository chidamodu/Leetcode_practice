
# You’re given an array of size N. Write a code to search for the second largest element in the array. 
# O(N log N)
# def second_largest(arr):
#     if len(arr) <= 1:
#         return print(0)
#     else:
#         arr = sorted(arr)
#     return print(arr[-2])

import unittest
# without sorting
def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > largest and num > second:
            second = largest
            largest = num
        elif num < largest and num > second:
            second = num
        # elif num < largest and num < second:
        #     continue
    # return print(second)
    return second if second != float('-inf') else None


second_largest([5, 5, 5])
# ([23, 1, 9, 90, 54, 5, 7, 87])
# ([23, 1, 9, 90, 54, 5, 7, 87])

class TestSecondLargest(unittest.TestCase):
    #Happy Path
    def test_standard_array(self):
        self.assertEqual(second_largest([1, 2, 3, 4, 5]), 4)
        self.assertEqual(second_largest([10, 5, 8, 20]), 10)

    #Edge cases
    def test_with_duplicates(self):
        self.assertEqual(second_largest([10, 10, 5]), 5)
        self.assertEqual(second_largest([5, 10, 10]), 5)

    def test_all_negative_numbers(self):
        self.assertEqual(second_largest([-10, -50, -2, -9]), -9)

    def test_all_identical_numbers(self):
        self.assertIsNone(second_largest([7, 7, 7]), None)

    #FAILURE CASES
    def test_array_too_short(self):
        self.assertIsNone(second_largest([5]))
        self.assertIsNone(second_largest([]))

if __name__ == '__main__':
    unittest.main()






