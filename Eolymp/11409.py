n = int(input())

for i in range(2 * n - 1):
    if i < n:
        if i == 0:
            print(" " * i + "*")
        else:
            print("*" + " " * (i -1) + "*")


    else:
        j = 2 * n - 2 - i
        if j == 0 :
            print(" " * j + "*")
        else:
            print("*" + " " * (j-1) + "*")

