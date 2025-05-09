


n = int(input())

for i in range(n):
    if not (i & 1):
        print('*' * n)
    else:
        if i % 4 == 1:
            print(' ' * (n - 1) + '*')
        else:
            print('*' + ' ' * (n - 1))
