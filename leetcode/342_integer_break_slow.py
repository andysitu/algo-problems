class Solution:
    def calc(self, current, n, prod, dp):
        if current == 0:
            end = n
        else:
            end = n-current+1
        for i in range(1, end):
            # print(current, i, prod, dp)
            # print(current+i, i*prod)
            if prod*i > dp[current+i]:
                # print("m")
                dp[current+i] = prod*i
                self.calc(current+i, n, prod * i, dp)
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        self.calc(0, n, 1, dp)
        return dp[n]

s = Solution()
print(s.integerBreak((3)))