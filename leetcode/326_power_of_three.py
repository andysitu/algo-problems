import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        v = int(math.log(n, 3))
        if 3 ** v == n or 3 ** (v+1) == n:
            return True
        return False