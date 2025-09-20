import bisect
from collections import deque, defaultdict
from typing import List


class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque([])
        self.relevant = defaultdict()
        self.counts = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.relevant:
            return False

        if len(self.queue) + 1 > self.limit:
            self.forwardPacket()

        self.relevant[(source, destination, timestamp)] = True
        self.counts[destination].append(timestamp)
        self.queue.append((source, destination, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []

        source, destination, timestamp = self.queue.popleft()
        self.counts[destination].pop(0)
        if not self.counts[destination]:
            del self.relevant[(source, destination, timestamp)]
            del self.counts[destination]

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.counts[destination]
        if not arr:
            return 0
        left = bisect.bisect_left(arr, startTime)
        right = bisect.bisect_right(arr, endTime)

        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)