from typing import List

class Solution:
    def maxProfit_infinitek(self, prices: List[int]) -> int:
        plen = len(prices)

        if 0 >= plen <= 1:
            return 0

        max_profits = [0] * plen
        # contains tuples - max_profit used, last index used,
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

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or prices == None or len(prices) == 0:
            return 0

        plen = len(prices)

        k = min(k, int(plen/2))

        transactions = []
        start = 0
        end = 0
        for i in range(1, plen):
            if prices[i] > prices[i-1]:
                end = i
            else:
                if end > start:
                    transactions.append([start, end])
                start = i
        if end > start:
            transactions.append([start, end])

        while len(transactions) > k:
            deletei = 0
            delete_loss = float('inf')
            for i in range(len(transactions)):
                t = transactions[i]
                loss = prices[t[1]] - prices[t[0]]
                if loss < delete_loss:
                    deletei = i
                    delete_loss = loss

            mergei = 0
            merge_loss = float('inf')
            for i in range(0, len(transactions) -1):
                t1 = transactions[i]
                t2 = transactions[i+1]
                loss = prices[t1[1]] - prices[t2[0]]
                if loss < merge_loss:
                    mergei = i
                    merge_loss = loss
                    
            if delete_loss <= merge_loss:
                transactions.pop(deletei)
            else:
                transactions[mergei + 1][0] = transactions[mergei][0]
                transactions.pop(mergei)
        return sum(prices[j]-prices[i] for i,j in transactions)