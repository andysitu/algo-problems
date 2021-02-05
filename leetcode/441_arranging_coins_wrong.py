"""
Doesn't work because the area of a triangle
accounts for the small edges. In other words,
it's not discrete in the values/ height such that
this problem  would require.
"""
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(n*2))