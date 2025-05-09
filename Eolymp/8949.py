n = int(input())

for i in range(n):
    for j in range(n):
        if j >= n - i - 1 and j <= i or j < n - i and j >= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()