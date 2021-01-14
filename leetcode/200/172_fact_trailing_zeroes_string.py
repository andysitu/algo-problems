import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        nstr = str(math.factorial(n))
        count = 0
        for i in range(len(nstr)-1, 0, -1):
            if nstr[i] == '0':
                count += 1
            else:
                return count
        return count