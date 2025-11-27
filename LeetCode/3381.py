from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

       ans = float('-inf')
       min_pref = [float('inf')] * k
       min_pref[0] = 0
       pref = 0
       for i, num in enumerate(nums, start = 1):
           pref += num
           l = i % k

           if min_pref[l] != float('-inf'):
               ans = max(ans, pref - min_pref[l])

           if pref < min_pref[l]:
               min_pref[l] = pref
       return ans



