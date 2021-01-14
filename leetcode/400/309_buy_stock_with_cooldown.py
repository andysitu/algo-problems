from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plen = len(prices)
        if plen == 0 or plen == 1:
            return 0
        if plen == 2:
            return max(prices[1]-prices[0], 0)
        bought = [0] * plen # current profits from holding a stock
        sold = [0] * plen # current profits from not holding a stock

        bought[0] = -prices[0]

        for i in range(1,3):
            bought[i] = max(bought[i-1], -prices[i])
            sold[i] = max(sold[i-1], bought[i-1] + prices[i])
        
        for i in range(3, plen):
            bought[i] = max(bought[i-1], sold[i-2] - prices[i])
            sold[i] = max(sold[i-1], bought[i-1] + prices[i])
        return sold[plen-1]

s = Solution()
print(s.maxProfit([1,2,3,0,2]))