import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid(str):
            return bool(re.fullmatch(r"[A-Za-z0-9_]+", str))
        valid_category = {"electronics", "grocery", "pharmacy", "restaurant"}
        group = [[] for _ in range(4)]
        for i in range(len(businessLine)):
            if is_valid(code[i]) and businessLine[i] in valid_category and isActive[i]:
                if businessLine[i] == 'electronics':
                    group[0].append(code[i])
                elif businessLine[i] == 'grocery':
                    group[1].append(code[i])
                elif businessLine[i] == 'pharmacy':
                    group[2].append(code[i])
                else:
                    group[3].append(code[i])

        return sorted(group[0]) + sorted(group[1]) + sorted(group[2]) + sorted(group[3])
