from collections import deque


def get_min(q_min):
    return q_min[0] if q_min else 0


def solve(n, k, arr):
    q = deque()
    q_min = deque()
    result = []

    for i in range(k):
        x = arr[i]
        q.append(x)
        while q_min and x < q_min[-1]:
            q_min.pop()
        q_min.append(x)

    result.append(get_min(q_min))

    for i in range(k, n):
        x = arr[i]
        if q[0] == q_min[0]:
            q_min.popleft()
        q.popleft()

        q.append(x)
        while q_min and x < q_min[-1]:
            q_min.pop()
        q_min.append(x)

        result.append(get_min(q_min))

    return result


n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = solve(n, k, arr)
print(*res)
