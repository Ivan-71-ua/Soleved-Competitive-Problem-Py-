from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i_isdig = [ [False] * 9 for i in range(9)]
        j_isdig = [ [False] * 9 for i in range(9)]
        ij_isdig = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit = ord(board[i][j]) - ord('1')
                    if i_isdig[i][digit]:
                        return False
                    i_isdig[i][digit] = True
                    if j_isdig[j][digit]:
                        return False
                    j_isdig[j][digit] = True
                    if ij_isdig[i // 3][j // 3][digit]:
                        return False
                    ij_isdig[i // 3][j // 3][digit] = True
        return True
