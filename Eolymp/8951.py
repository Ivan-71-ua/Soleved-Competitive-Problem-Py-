n = int(input())

for i in range(n // 2):
    print(" " * (n // 2 - i) + "*" + " " * (2 * i - 1) * (i > 0) + "*" * (i > 0) + " " * (n // 2 - i))

print("*" +  " " * (n - 2) + "*")

for i in range(n // 2 - 1, -1, -1):
    print(" " * (n // 2 - i) + "*" + " " * (2 * i - 1) * (i > 0) + "*" * (i > 0) + " " * (n // 2 - i))
