from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        num_people = len(languages)
        bad_pair = set()
        for a, b in friendships:
            mp = {}
            uncommon = True
            for lg in languages[a - 1]:
                mp[lg] = 1
            for lg in languages[b - 1]:
                if lg in mp:
                    uncommon = False
                    break
            if uncommon:
                bad_pair.add(a)
                bad_pair.add(b)

        cnt_lang = [0] * n
        max_lang = 0
        for pr in bad_pair:
            for lg in languages[pr - 1]:
                cnt_lang[lg - 1] += 1
                max_lang = max(max_lang, cnt_lang[lg - 1])

        return len(bad_pair) - max_lang
