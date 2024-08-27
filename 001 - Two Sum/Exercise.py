import unittest
from typing import List


# 1. Primer intento
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int] | None:
        len_nums: int = len(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                num_i = nums[i]
                num_j = nums[j]
                if num_i + num_j == target:
                    return [i, j]
        return None


## Complejidad de O(n^2)


# 2. Segundo Intento
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table_hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in table_hash:
                return [table_hash[complement], i]
            table_hash[num] = i
        return [-1, -1]


## Complejidad de O(n)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution1()

    def test_case_1(self):
        self.assertEqual(self.s.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_case_2(self):
        self.assertEqual(self.s.twoSum([3, 2, 4], 6), [1, 2])

    def test_case_3(self):
        self.assertEqual(self.s.twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
