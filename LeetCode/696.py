
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur = '%'
        prev_cnt, cur_cnt = 0, 0
        res = 0
        for ch in s:
            if cur != ch:
                res += min(cur_cnt, prev_cnt)
                cur = ch
                prev_cnt = cur_cnt
                cur_cnt = 0
            cur_cnt += 1
        res += min(cur_cnt, prev_cnt)
        return res
