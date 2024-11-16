"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        # Creacion diccionario letras magazine
        for letter in magazine:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        # Comprobar RansomNote
        for letter in ransomNote:
            if dictionary.get(letter, 0) > 0:
                dictionary[letter] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    # Inicializamos la variables
    ransomNote = "aa"
    magazine = "ab"

    # Llamar a la solución
    handler = Solution()
    response = handler.canConstruct(ransomNote=ransomNote, magazine=magazine)
    print(response)
