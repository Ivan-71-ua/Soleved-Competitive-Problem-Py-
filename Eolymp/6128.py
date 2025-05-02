

from collections import deque

d = deque()

while True:
    cmd = input().strip().split()

    if cmd[0] == "push_back":
        d.append(int(cmd[1]))
        print("ok")

    elif cmd[0] == "push_front":
        d.appendleft(int(cmd[1]))
        print("ok")

    elif cmd[0] == "pop_back":
        print(d.pop())

    elif cmd[0] == "pop_front":
        print(d.popleft())

    elif cmd[0] == "front":
        print(d[0])

    elif cmd[0] == "back":
        print(d[-1])

    elif cmd[0] == "size":
        print(len(d))

    elif cmd[0] == "clear":
        d.clear()
        print("ok")

    elif cmd[0] == "exit":
        print("bye")
        break
