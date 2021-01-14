from typing import List

class Solution:
    def find_best_profit(self, prices, start, end):
        plen = end-start
        if 0 >= plen <= 1:
            return (0, 0, 0)
        max_profit_tup = (0, end, end)
        max_value = prices[end]
        max_value_index = end

        for i in range(end - 1, start - 1, -1):
            if max_value - prices[i] > max_profit_tup[0]:
                max_profit_tup = (max_value - prices[i], i, max_value_index)
            if prices[i] > max_value:
                max_value_index = i
                max_value = prices[i]
        # print(max_profit)
        return max_profit_tup

    # find best price and with remaining price list, finds 2nd best
    def find_2_best(self, prices, start, end):
        best_profits = self.find_best_profit(prices, start, end)
        # print(best_profits)

        if best_profits[0] == 0:
            return (0,0,0), (0,0,0)

        # exclude start and end from best point found
        left_of_best = self.find_best_profit(prices, start, best_profits[1] -1)
        right_of_best = self.find_best_profit(prices, best_profits[2] + 1, end)

        if left_of_best[0] > right_of_best[0]:
            return best_profits, left_of_best
        else:
            return best_profits, right_of_best

    def maxProfit(self, prices: List[int]) -> int:
        prev_profits = -1
        best_profits = 0

        endPoint = len(list)

        while prev_profits < best_profits:
            a, b = self.find_2_best(prices, 0, len(prices) - 1)
            prev_profits = best_profits
            best_profits = a[0] + b[0]
            print(a, b)

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
# print(s.maxProfit([7,1,5,3,6,4]))
# print(s.maxProfit([1,2,3,4,5]))
# print(s.maxProfit([7,6,4,3,1]))
# print(s.maxProfit([2,4,3,2,1,2,3,5,19,24,21,3,4,2,10,4,2,3,4,1,3,2,4,1,4,5,1,2,3,4,2,10,4,2,3,4,12,44,23,42,3]))