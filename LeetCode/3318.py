from typing import List, Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n, res = len(nums), []
        for i in range(n - k + 1):
            cnt = Counter(nums[i : i + k])
            item = list(zip(map(lambda x: -x, cnt.values()), map(lambda x: -x, cnt.keys())))
            item.sort()
            j, cur_sum = 0, 0
            while j < len(item) and j < x:
                cur_sum += -item[j][0] * -item[j][1]
                j += 1
            res.append(cur_sum)
        return res
