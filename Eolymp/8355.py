


from collections import deque

n = int(input())
sh = deque()

for i in range(n):
    op = list(map(int, input().split()))

    if op[0] == 1:
        sh.appendleft(op[1])
    elif op[0] == 2:
        sh.append(op[1])
    elif op[0] == 3:
        print(sh.popleft())
    elif op[0] == 4:
        print(sh.pop())  
