
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt, ost = 0, 0
        while ost + numBottles >= numExchange:
            cnt += numBottles
            ost += numBottles
            numBottles = ost // numExchange
            ost %= numExchange
        cnt += numBottles
        return cnt