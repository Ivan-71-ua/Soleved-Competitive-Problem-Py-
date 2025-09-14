
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def make_w(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        set_words = set(wordlist)
        cap_words = {}
        vol_words = {}
        for w in wordlist:
            word_low = w.lower()
            cap_words.setdefault(word_low, w)
            vol_words.setdefault(make_w(word_low), w)

        def solve(query):
            if query in set_words:
                return query
            q_low = query.lower()
            if q_low in cap_words:
                return cap_words[q_low]
            q_make = make_w(q_low)
            if q_make in vol_words:
                return vol_words[q_make]
            return ""

        return list(map(solve, queries))
