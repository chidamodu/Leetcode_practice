
import unittest
def fourSum(nums, target):
    nums = sorted(nums)
    result = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i + 1 and nums[j] == nums[j-1]: 
                continue
            left = j + 1
            right = len(nums)-1
            while left < right:
                quadrapulet_total = nums[i]+nums[j]+nums[left]+nums[right]
                if quadrapulet_total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif quadrapulet_total < target:
                    left += 1
                else:
                    right -= 1 
    return result

# nums = [1,0,-1,0,-2,2] 
# target = 0
# nums = [2,2,2,2,2]
# target = 8
# fourSum(nums, target)

class TestQuadSum(unittest.TestCase):
    # def test_empty_array(self):
    #     self.assertTrue(fourSum([2,2,2,2,2], 8), [[2,2,2,2]])
    #     self.assertEqual(fourSum([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

    # def test_empty_array1(self):
    #     self.assertEqual(
    #         fourSum([2,2,2,2,2], 8), 
    #         [[2,2,2,2]], 
    #         msg="Failed on the all-twos array!" # This only prints if the test fails
    #     )

    def test_empty_array(self):
        with self.subTest(msg="Testing all twos"):
            # self.assertEqual(fourSum([2,2,2,2,2], 8), [[2,2,2,2]])
            self.assertEqual(fourSum([2,2,2,2,2], 8), [[99]])
            
        with self.subTest(msg="Testing mixed numbers"):
            self.assertCountEqual(fourSum([1,0,-1,0,-2,2], 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

    def test_returns_correct_type(self):
        result = fourSum([2, 2, 2, 2], 8)
        self.assertIsInstance(result, list)

    def test_contains_specific_quadruplet(self):
        result = fourSum([-5, -4, -3, -2, 1, 3, 3, 5, 6, 8, 9], 0)
        # I just want to ensure my code found this specific combination
        self.assertIn([-4, -2, 3, 3], result)

    def test_no_solution_exists(self):
        # Target is 100, but array is too small. Expecting an empty list [].
        self.assertFalse(fourSum([1, 2, 3, 4], 100))
        
        # Array doesn't have 4 numbers
        self.assertFalse(fourSum([1, 2, 3], 0))

    def test_unordered_results(self):
        # Even if your function returns the quadruplets in a different order, this passes!
        expected = [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
        result = fourSum([1,0,-1,0,-2,2], 0)
        self.assertCountEqual(result, expected)

if __name__ == '__main__':
    unittest.main()



    
