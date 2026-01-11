from collections import deque
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sorted_start = sorted(events, key=lambda x: x[0])
        sorted_end = deque(sorted(events, key=lambda x: x[1]))

        ans = max(v for _, _, v in events)

        max_end = 0
        for s, e, v in sorted_start:
            while sorted_end and sorted_end[0][1] < s:
                max_end = max(max_end, sorted_end[0][2])
                sorted_end.popleft()

            ans = max(ans, max_end + v)

        return ans
