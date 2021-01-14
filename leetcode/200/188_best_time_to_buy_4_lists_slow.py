from typing import List

class Solution:
    def get_max(self, best_profits, num_times, start, end, data):
        if start >= end:
            return 0
        num_times = min(num_times, int( (end-start+1)/2) )
        if num_times == 0:
            return 0
        if num_times == 1:
            return best_profits[start][end]
        
        s = str(num_times) + "_" + str(start) + "_" + str(end)
        if s in data:
            return data[s]
        max_price = best_profits[start][start+1]
        for i in range(start+1, end+1):
        # for i in range(end, start, -1):
            max_price = max(max_price, best_profits[start][i] + self.get_max(best_profits,num_times-1, i+1, end, data))
        data[s] = max_price
        # print(num_times, start, end)
        return max_price

    def maxProfit(self, k: int, prices: List[int]) -> int:
        best_profits = []
        data = {}
        for __ in range(len(prices)-1): # can't buy and sell on the same day (last day)
            best_profits.append([0] * len(prices))
        
        for i in range(len(prices)-1):
            best_buy = prices[i]
            for j in range(i+1, len(prices)):
                best_buy = min(best_buy, prices[j-1])
                best_profits[i][j] = max(best_profits[i][j-1], prices[j] - best_buy, 0)
        # print(best_profits)
        return 1
        return self.get_max(best_profits, k, 0, len(prices)-1, data)
        
s = Solution()
print(s.maxProfit(1, [10,9,8,7,6,5,4,3,2,1,0]))
# print(s.maxProfit(4, [3,2,6,5,0,3,4,3,10,4,2,3,1,4,3,2,1,3,4,3]))