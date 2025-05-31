from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_idx(num):
            row = (num - 1) // n
            col = (num - 1) % n
            if row % 2 == 0:
                return [n - 1 - row, col]
            return [n - 1 - row, n - 1 - col]
        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0
        while q:
            cur = q.popleft()
            for i in range(1, 7):
                if cur + i > n * n:
                    break
                next_pos = cur + i
                r, c = get_idx(next_pos)
                if board[r][c] != -1:
                    next_pos = board[r][c]
                if next_pos == n * n:
                    return dist[cur] + 1
                if dist[next_pos] == -1:
                    dist[next_pos] = dist[cur] + 1
                    q.append(next_pos)
        return -1
