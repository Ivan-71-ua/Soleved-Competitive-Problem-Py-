from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cnt = 0
        k -= 1
        i = 0
        while k != 0:
            cnt += ((k & 1) & operations[i])
            k >>= 1
            i += 1
        return chr(ord('a') + cnt % 26)