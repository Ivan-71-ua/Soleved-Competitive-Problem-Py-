

import heapq

n, k = map(int, input().split())
t = list(map(int, input().split()))

pq = []

for i in range(min(k, n)):
    heapq.heappush(pq, t[i])

for i in range(k, n):
    current_time = heapq.heappop(pq)
    heapq.heappush(pq, current_time + t[i])

print(max(pq))
