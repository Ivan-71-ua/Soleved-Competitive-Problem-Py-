from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt, n, len_w = 0, len(strs), len(strs[0])
        for i in range(len_w):
            for j in range(1, n):
                if strs[j - 1][i] > strs[j][i]:
                    cnt += 1
                    break
        return cnt