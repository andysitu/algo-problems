from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plen = len(prices)
        if plen == 0 or plen == 1:
            return 0
        leftpricemap = [0] * plen # max profit per i from start to i
        rightpricemap = [0] * plen # max profit per i from i to end

        max_profit = 0
        max_value = prices[plen-1]
        for i in range(len(prices) - 2, -1, -1):
            max_profit = max(max_profit, max_value - prices[i])
            max_value = max(max_value, prices[i])
            rightpricemap[i] = max_profit
            # print(max_profit, max_value, prices[i])
        
        max_profit = 0
        min_value = prices[0]

        for i in range(1, plen):
            max_profit = max(max_profit, prices[i]-min_value)

            min_value = min(min_value, prices[i])
            leftpricemap[i] = max_profit
            # print(max_profit, max_value, prices[i])

        max_profit = max(leftpricemap[plen-1], rightpricemap[0])

        for i in range(0, plen-1):
            max_profit = max(max_profit, leftpricemap[i] + rightpricemap[i+1])
        
        # print(leftpricemap)
        # print(rightpricemap)
        return max_profit

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
# print(s.maxProfit([7,1,5,3,6,4]))
# print(s.maxProfit([1,2,3,4,5]))
# print(s.maxProfit([7,6,4,3,1]))
# print(s.maxProfit([2,4,3,2,1,2,3,5,19,24,21,3,4,2,10,4,2,3,4,1,3,2,4,1,4,5,1,2,3,4,2,10,4,2,3,4,12,44,23,42,3]))