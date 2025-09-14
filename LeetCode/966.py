from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        for qw in queries:
            same, diff_c, diff_v = None, None, None
            for w in wordlist:
                if not same and w == qw:
                    same = w
                    break
                if not diff_c:
                    if len(w) == len(qw) and w.lower() == qw.lower():
                        diff_c = w

                if not diff_v:
                    if len(w) == len(qw):
                        can = True
                        for i in range(len(qw)):
                            if qw[i].lower() in 'aeiou' and w[i].lower() in 'aeiou':
                                continue
                            if qw[i].lower() != w[i].lower():
                                can = False
                                break
                        if can:
                            diff_v = w

            if same:
                res.append(same)
            elif diff_c:
                res.append(diff_c)
            elif diff_v:
                res.append(diff_v)
            else:
                res.append("")
        return res
