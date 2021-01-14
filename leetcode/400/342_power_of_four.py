import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        v = int(math.log(n, 4))
        if 4 ** v == n or 4 ** (v+1) == n:
            return True
        return False