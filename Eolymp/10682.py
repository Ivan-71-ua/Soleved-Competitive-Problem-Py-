
n, m = map(int, input().split())
costs = list(map(int, input().split()))

max_sum = 0
cur_sum = 0
left = 0

for right in range(n):
    cur_sum += costs[right]

    while cur_sum > m:
        cur_sum -= costs[left]
        left += 1

    max_sum = max(max_sum, cur_sum)

print(max_sum)
