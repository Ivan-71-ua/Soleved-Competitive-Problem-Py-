n = int(input())

for i in range(n):
    if not (i & 1):
        r = "* " * (n // 2)
        if (n & 1) == 1:
            r += "*"
    else:
        r = " *" * (n // 2)
        if (n & 1) == 1:
            r += " "
    print(r)