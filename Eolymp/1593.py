from collections import deque

tests = int(input())

for case_num in range(1, tests + 1):
    data = list(map(int, input().split()))
    n = data[0]
    a = data[1:]

    a.sort()

    v = deque()

    v.append(a[-1])
    v.appendleft(a[0])

    s = abs(v[1] - v[0])

    a.pop()
    a.pop(0)

    while a:
        mx = [
            abs(v[0] - a[0]),
            abs(v[-1] - a[0]),
            abs(v[0] - a[-1]),
            abs(v[-1] - a[-1])
        ]

        rmax = max(mx)

        if rmax == mx[0]:
            v.appendleft(a[0])
            a.pop(0)
        elif rmax == mx[1]:
            v.append(a[0])
            a.pop(0)
        elif rmax == mx[2]:
            v.appendleft(a[-1])
            a.pop()
        else:
            v.append(a[-1])
            a.pop()

        s += rmax

    print(f"Case {case_num}: {s}")
