class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        p = 1
        while n > 4:
            p *= 3
            n -= 3
        return p * n

s = Solution()
print(s.integerBreak((58)))