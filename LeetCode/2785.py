
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        cur_str = list(s)
        n = len(cur_str)
        for k in range(n):
            if cur_str[k] in 'aeiouAEIOU':
                vowels.append(cur_str[k])
                cur_str[k] = '@'

        vowels.sort()
        cur_idx = 0
        for k in range(n):
            if cur_str[k] == '@':
                cur_str[k] = vowels[cur_idx]
                cur_idx += 1
        return ''.join(cur_str)

