from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for i in operations:
            if i[0] == '+' or i[-1] == '+':
                res += 1
            else:
                res -= 1
        return res
