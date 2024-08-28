import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: List[int], l2: List[int]) -> List[int]:
        carry = 0
        result = []

        while l1 or l2 or carry:
            val1 = l1.pop(0) if l1 else 0
            val2 = l2.pop(0) if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            result.append(total % 10)
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_case_1(self):
        self.assertEqual(self.s.addTwoNumbers([2, 4, 3], [5, 6, 4]), [7, 0, 8])

    def test_case_2(self):
        self.assertEqual(self.s.addTwoNumbers([0], [0]), [0])

    def test_case_3(self):
        self.assertEqual(
            self.s.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
            [8, 9, 9, 9, 0, 0, 0, 1],
        )


if __name__ == "__main__":
    unittest.main()
