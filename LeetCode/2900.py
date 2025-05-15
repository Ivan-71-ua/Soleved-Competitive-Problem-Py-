from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        stack = 0
        for i in range(len(words)):
            if len(res) == 0:
                res.append(words[i])
                stack  = i
            else:
                if groups[i] == groups[stack]:
                    res.append(words[i])
                    stack = i
        return res