class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 2
        b = 1
        c = 0
        temp = 0
        for i in range(n-2):
            temp = a
            a = temp + b
            b = temp
        return a

s = Solution()
print(s.climbStairs(8))
print(s.climbStairs(3))