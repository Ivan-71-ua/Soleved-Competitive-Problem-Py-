from collections import deque

n, a, b, c, x = map(int, input().split())
value = deque()
mn = deque()
res = 0

for i in range(1, n + 1):
    x = ((a * x * x + b * x + c) // 100) % 1000000

    if x % 5 < 2:
        if value:
            if value[0] == mn[0]:
                mn.popleft()
            value.popleft()
    else:
        value.append(x)
        while mn and x < mn[-1]:
            mn.pop()
        mn.append(x)

    if mn:
        res += mn[0]

print(res)
