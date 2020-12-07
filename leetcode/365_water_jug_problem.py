class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x + y == z or x == z or y == z:
            return True
        g = self.gcd(x, y)
        return z % g == 0

s = Solution()
print(s.canMeasureWater(3, 5, 4), True)