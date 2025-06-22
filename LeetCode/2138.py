from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = list(s)
        ost = len(arr) % k
        if ost != 0:
            ost = k - ost
        for i in range(ost):
            arr.append(fill)
        res = []
        for i in range(0, len(arr), k):
            res.append(''.join(arr[i:i + k]))
        return res