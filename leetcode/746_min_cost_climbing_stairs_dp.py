class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        clen = len(cost)
        dp = [0] * clen
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(clen-3, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        return min(dp[0], dp[1])