class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = cost[-1]
        b = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            c = min(a, b) + cost[i]
            a = b
            b = c
        return min(a, b)