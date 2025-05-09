


n = int(input())

for i in range(n):
    if i == n -1:
        print("|" * i + "@" + "|" * i)
    else:
        print("|" * i + "@" + " " * (2 * (n - i - 1) - 1) + "@" + "|" * i)
