
# You’re given an array A of size N. Write a function to find the minimum index-based distance between two elements in the array.
from collections import defaultdict
import unittest

def min_index_distance(arr, n1, n2):
    last_seen_n1 = -1
    last_seen_n2 = -1
    min_dist = float('inf')
    for ind, num in enumerate(arr):
        if num == n1:
            if n1 == n2:
                last_seen_n2 = last_seen_n1
            last_seen_n1 = ind

        elif num == n2:
            last_seen_n2 = ind

        if last_seen_n1 != -1 and last_seen_n2 != -1:
            curr_dist = abs(last_seen_n1 - last_seen_n2)
            if curr_dist < min_dist:
                min_dist = curr_dist
    return min_dist if min_dist != float('inf') else None
            # print(last_seen_n2)

# min_index_distance([3, 3, 3], 3, 3)

# min_index_distance([3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3], 3, 6)
# min_index_distance([10, 20, 30, 10, 40, 20, 10, 10], 10, 20)

class TestMinIndDist(unittest.TestCase):
    #Happy Path
    def test_expected_min_dist(self):
        self.assertEqual(min_index_distance([3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3], 3, 6), 4)
        self.assertEqual(min_index_distance([10, 20, 30, 10, 40, 20, 10], 10, 20), 1)

    #Tricky cases
    def test_uplicate_values(self):
        self.assertEqual(min_index_distance([4, 4, 4], 4, 4), 1)

    def test_missing_elements(self):
        # One element is missing
        self.assertEqual(min_index_distance([1, 2, 3, 4], 1, 99), None)
        
        # Both elements are missing
        self.assertEqual(min_index_distance([1, 2, 3, 4], 88, 99), None)

    def test_shrinking_distance(self):
        # Distance starts at 4, then shrinks to 2, and finally to 1 at the end
        self.assertEqual(min_index_distance([1, 0, 0, 0, 2, 0, 1, 0, 2, 1, 2], 1, 2), 1)

    def test_array_too_short(self):
        # Only one element exists
        self.assertEqual(min_index_distance([5], 5, 5), None)
        
        # Empty array
        self.assertEqual(min_index_distance([], 1, 2), None)

    def test_adjacent_at_end(self):
        self.assertEqual(min_index_distance([10, 99, 99, 99, 10, 20], 10, 20), 1)


    #Failure cases - boundary constraints
if __name__ == '__main__':
    unittest.main()

# good try but won't work
# def min_index_distance(arr, n1, n2):
#     arr_index_dict = defaultdict(list)
#     for ind, num in enumerate(arr):
#         arr_index_dict[num].append(ind)
#     if n1 == n2:
#         result = arr_index_dict[n1][0] - arr_index_dict[n2][1]
#     else:
#         result = arr_index_dict[n1][0] - arr_index_dict[n2][0]
#     return abs(result)