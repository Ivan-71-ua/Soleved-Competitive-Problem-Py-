import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        cnt =[0] * n
        free = list(range(n))
        heapq.heapify(free)
        used = []
        for l, r in meetings:
            while used and used[0][0] <= l:
                _, room = heapq.heappop(used)
                heapq.heappush(free, room)
            if free:
                room = heapq.heappop(free)
                end = r
            else:
                prev, room = heapq.heappop(used)
                end = r - l + prev
            cnt[room] += 1
            heapq.heappush(used, (end, room))
        id = 0
        for i in range(n):
            if cnt[id] < cnt[i]:
                id = i
        return id