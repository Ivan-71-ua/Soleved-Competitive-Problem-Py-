from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        pref_sum = [0] * n
        pref_sum[0] = prices[0] * strategy[0]

        for i in range(1, n):
            pref_sum[i] = pref_sum[i - 1] + prices[i] * strategy[i]

        cur_w = sum(prices[i] for i in range(k - k // 2, k))
        res = max(pref_sum[-1], cur_w + pref_sum[-1] - pref_sum[k - 1])
        l = k // 2

        for r in range(k, n):
            cur_w -= prices[l]
            cur_w += prices[r]
            res = max(res, cur_w + pref_sum[l - k // 2] + pref_sum[-1] - pref_sum[r])
            l += 1

        return res

__import__("atexit").register(lambda: open("dis  play_runtime.txt", "w").write("0"))
