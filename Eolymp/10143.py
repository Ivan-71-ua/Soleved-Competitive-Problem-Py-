
from collections import deque

while True:
    n = int(input())
    if n == 0:
        break
    deck = deque(range(1, n + 1))

    disc = []

    while len(deck) > 1:
        disc.append(deck.popleft())
        deck.append(deck.popleft())

    print(f"Discarded cards: {', '.join(map(str, disc)) if disc else ''}")
    print(f"Remaining card: {deck[0]}")
