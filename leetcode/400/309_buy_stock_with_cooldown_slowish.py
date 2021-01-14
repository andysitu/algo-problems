from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plen = len(prices)
        if plen == 0 or plen == 1:
            return 0
        maxprofits = [0] * plen # buy time start
        # maxprofit, last index used to buy
        maxprofits[plen-1] = (0, plen-1)

        for i in range(plen-2, -1, -1):
            # replace the buy day from prev maxprofits
            replace_buy = maxprofits[i+1][0] + prices[maxprofits[i+1][1]] - prices[i]
            
            buy_profit = 0
            # buy a new stock instead
            end = maxprofits[i+3][1]-1 if i < plen - 3 else plen
            sell_day = -1
            profit = 0

            for j in range(i+1, end):
                if prices[j] - prices[i] > profit:
                    sell_day = j
                    profit = prices[j] - prices[i]
                
            buy_profit = profit + (maxprofits[i+3][0] if sell_day != -1 and i < plen-3 else 0)
            
            if replace_buy > maxprofits[i+1][0] or buy_profit > maxprofits[i+1][0]:
                if buy_profit >= replace_buy:
                    maxprofits[i] = (buy_profit, i)
                else:
                    maxprofits[i] = (replace_buy, i)
            else: # not do anything this day
                maxprofits[i] = maxprofits[i+1]
        return max(maxprofits[0][0], maxprofits[1][0])
        

s = Solution()
print(s.maxProfit([1,4,2]))