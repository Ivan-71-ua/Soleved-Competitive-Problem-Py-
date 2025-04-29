from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxs, cnt, res, n, l = 0, 0, 0, len(nums), 0
        for i in nums:
            if i > maxs:
                maxs = i
                cnt = 1
            elif i == maxs:
                cnt += 1
        if cnt < k:
            return 0
        cnt = 0
        for r in range(n):
            if nums[r] == maxs:
                cnt += 1
            while cnt >= k:
                if nums[l] == maxs:
                    cnt -= 1
                l += 1
            res += l
        return res
