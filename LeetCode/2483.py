


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        wr = customers.count('Y')
        n, best, penalty = len(customers), -1, float('inf')
        cur_cl, cur_wr = 0, 0
        for i in range(n):
            if penalty > cur_cl + (wr - cur_wr):
                best = i
                penalty = cur_cl + (wr - cur_wr)

            if customers[i] == 'Y':
                cur_wr += 1
            else:
                cur_cl += 1

        if penalty > cur_cl + (wr - cur_wr):
            best = n

        return best