

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        empty = numBottles
        while empty >= numExchange:
            result += 1
            empty -= numExchange - 1
            # print(result, empty, numExchange, "*\*")
            numExchange += 1

        return result