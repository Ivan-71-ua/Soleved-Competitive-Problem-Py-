n = int(input())

for i in range(n):
    print(" " * i + "@" + "*" * (2 * n - 3 - 2 * i) + "@" * (i != n - 1))
