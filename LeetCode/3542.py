from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        stack = []
        for num in nums:
            while stack and num < stack[-1]:
                stack.pop()
            if num == 0:
                continue
            if not stack or stack[-1] < num:
                cnt += 1
                stack.append(num)
        return cnt