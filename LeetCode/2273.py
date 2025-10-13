from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for i in range(1, len(words)):
            if sorted(res[-1]) != sorted(words[i]):
                res.append(words[i])
        return res