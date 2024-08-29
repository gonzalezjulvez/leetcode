import unittest

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         letters = list(s)
#         word = ""
#         max_len = 0

#         for letter in letters:
#             if letter in word:
#                 current_len = len(word)
#                 if current_len > max_len:
#                     max_len = current_len
#                 word = ""
#             word += letter
#         return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        diccionario = {}
        max_len = 0
        inicio = 0

        for fin, letra in enumerate(s):
            if letra in diccionario and diccionario[letra] >= inicio:
                inicio = diccionario[letra] + 1

            diccionario[letra] = fin
            max_len = max(max_len, fin - inicio + 1)

        return max_len


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_case_1(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_case_2(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("bbbbb"), 1)

    def test_case_3(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
# s = Solution()
# s.lengthOfLongestSubstring("abcabcbb")
