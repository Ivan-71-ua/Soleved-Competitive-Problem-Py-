

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = ['a', 'e', 'i', 'o', 'u']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        is_vowel, is_consonant = False, False
        for char in word:
            if char in ['@', '#', '$']:
                return False
            elif char in digits:
                is_digits = True
            elif char.lower() in vowels:
                is_vowel = True
            else:
                is_consonant = True
        return is_vowel and is_consonant