from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if 0 >= len(prices) <= 1:
            return 0
        max_profit = 0
        max_value = prices[len(prices) - 1]
        for i in range(len(prices) - 2, -1, -1):
            max_profit = max(max_profit, max_value - prices[i])
            max_value = max(max_value, prices[i])
            # print(max_profit, max_value, prices[i])
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))