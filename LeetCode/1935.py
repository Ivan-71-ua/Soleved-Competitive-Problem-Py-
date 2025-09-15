
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        result = 0
        for word in words:
            can = True
            for alph in brokenLetters:
                if alph in word:
                    can = False
                    break
            result += can
        return result