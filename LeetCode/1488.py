from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rain_pos = {}
        dry_pos = SortedList()
        res = [1] * len(rains)
        for i, rain in enumerate(rains):
            if rain == 0:
                dry_pos.add(i)
            else:
                res[i] = -1
                if rain in rain_pos:
                    prev_pos = dry_pos.bisect(rain_pos[rain])
                    if prev_pos == len(dry_pos):
                        return []
                    res[dry_pos[prev_pos]] = rain
                    dry_pos.discard(dry_pos[prev_pos])
                rain_pos[rain] = i
        return res


