from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plen = len(prices)

        if 0 >= plen <= 1:
            return 0

        max_profits = [0] * plen
        # contains tuples - max_profit used, last index used
        max_profits[plen-1] = (0, plen-1)

        for i in range(plen - 2, -1, -1):
            prev_tup = max_profits[i+1]

            new_profit_by_replace = prev_tup[0] + prices[ prev_tup[1] ] - prices[i]
            adjacent_profit = prices[i+1] - prices[i] + prev_tup[0]

            if new_profit_by_replace > prev_tup[0] or adjacent_profit > prev_tup[0]:
                if adjacent_profit >= new_profit_by_replace:
                    max_profits[i] = (adjacent_profit, i)
                else:
                    max_profits[i] = (new_profit_by_replace, i)
            else:
                max_profits[i] = max_profits[i+1]
        
        # print(max_profits)
        return max_profits[0][0]

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([2,4,3,2,1,2,3,5,19,24,21,3,4,2,10,4,2,3,4,1,3,2,4,1,4,5,1,2,3,4,2,10,4,2,3,4,12,44,23,42,3]))