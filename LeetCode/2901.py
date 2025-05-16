from typing import List


class Solution:

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def check(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for i in range(len(s1)):
                diff += (s1[i] != s2[i])
            return diff == 1
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        maxs = 1
        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and check(words[i], words[j]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] +1
                    prev[i] = j
            maxs = max(maxs, dp[i])

        res = []
        for i in range(n):
            if dp[i] == maxs:
                while i != -1:
                    res.append(words[i])
                    i = prev[i]
                break
        res.reverse()
        return res