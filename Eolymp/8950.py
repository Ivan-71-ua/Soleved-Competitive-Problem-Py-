n = int(input())


for i in range(n // 2):
    print("*" * (i + 1) + " " * (n - 2 * (i + 1)) + "*" * (i + 1))


print("*" * n)


for i in range(n // 2 - 1, -1, -1):
    print("*" * (i + 1) + " " * (n - 2 * (i + 1)) + "*" * (i + 1))
