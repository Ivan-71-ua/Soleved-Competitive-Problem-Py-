from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        l, r, n = 0, nums[-1] - nums[0], len(nums)
        while l < r:
            mid = (l + r) // 2
            cnt =  0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    cnt += 1
                    i += 1
                i += 1
            if cnt >= p:
                r = mid
            else:
                l = mid + 1
        return l