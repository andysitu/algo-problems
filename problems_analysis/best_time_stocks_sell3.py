"""
Two passes Sweep
First you need to find the max profit of the first transaction
for each price and then save it in an array.
This is solved by using the solution in the first version of the problem
record min price, and then get the max profits by selling at i with maxprice
set that max price in an array

Then, travel backwards. This time you are recording the max price
while you are selling at i and then also adding it with the array
calculated previously since you can sell and buy at the same day

Runtime O(n), Space O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minprice = prices[0]
        maxprofits = 0
        profits = [0] * len(prices)
        for i in range(len(prices)):
            maxprofits = max(maxprofits, prices[i] - minprice)
            profits[i] = maxprofits
            minprice = min(minprice, prices[i])
        
        maxprice = prices[-1]
        maxprofits = 0
        total = 0
        for i in range(len(prices)-1, -1, -1):
            maxprofits = max(maxprofits, maxprice - prices[i])
            maxprice = max(maxprice, prices[i])
            total = max(total, profits[i] + maxprofits)
        return total