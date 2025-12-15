from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cur_cnt, ans, n = 1, 0 , len(prices)
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                cur_cnt += 1
            else:
                ans += cur_cnt * (cur_cnt + 1) // 2
                cur_cnt = 1
        ans += cur_cnt * (cur_cnt + 1) // 2
        return ans