

symbol, h = input().split()
h = int(h)

total_symbols = 0


for i in range(1, h + 1):
    stars = 2 * i - 1 + h - i
    total_symbols += stars


print(total_symbols)


for i in range(1, h + 1):
    spaces = h - i
    stars = 2 * i - 1
    print(' ' * spaces + symbol * stars)
