

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator  == 0:
            return "0"

        frac = []
        if (denominator < 0) ^ (numerator < 0):
            frac.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        frac.append(str(numerator // denominator))
        rem = numerator % denominator
        if rem == 0:
            return ''.join(frac)

        frac.append(".")
        position = {}
        while rem != 0:

            if rem  in position:
                pos = position[rem]
                frac.append(pos, "(")
                frac.append(")")
                break

            position[rem] = len(frac)
            rem *= 10
            frac.append(str(rem // denominator))
            rem %= denominator


        return ''.join(frac)