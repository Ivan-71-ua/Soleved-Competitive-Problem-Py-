from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        memory = [0] * 1000000
        max_v = 0
        def backtrack(idx, cur):
            for i in range(idx, len(nums)):
                tmp = cur | nums[i]
                nonlocal max_v
                max_v = max(tmp, max_v)
                memory[tmp] += 1
                backtrack(i + 1, tmp)

        return memory[max_v]

