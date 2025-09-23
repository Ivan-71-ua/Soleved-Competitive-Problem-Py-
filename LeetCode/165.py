
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1 = list(map(int, version1.split('.')))
        num2 = list(map(int, version2.split('.')))
        print(num1, num2)
        inv = 1
        if len(num2) > len(num1):
            inv = -1
            num1, num2 = num2, num1
        for i in range(len(num1)):
            a = num1[i]
            b = num2[i] if i < len(num2) else 0
            if a > b:
                return 1 * inv
            elif a < b:
                return -1 * inv
        return 0