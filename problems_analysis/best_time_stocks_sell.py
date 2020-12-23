"""
Brute Force approach:
Iterate through all of them with two for loops to test
out all combinations
Runtime: O(n^2), Space: O(1)
"""
def maxProfit(self, prices):
    maxprofit = 0
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            maxprofit = max( prices[j] - prices[i], maxprofit)
    return maxprofit

"""
What it's really looking for is the lowest price to buy and 
the highest price to sell. This value can be saved instead
to get the profit
Runtime: O(n); space: O(1)
"""
def maxProfit2(self, prices):
    maxprofits = 0
    maxprice = 0
    minprice = prices[0]
    for i in range(len(prices)-1):
        maxprice = max(maxprice, prices[i])
        minprice = min(minprice, prices[i+1])
        maxprofits = max(maxprice - minprice)
    return maxprofits

"""
Don't have to save the maxprice since the calculation is done at 
every step and you either encounter a min or max in price
Also, if you encounter a minprice, you can't calculate
since this requires you to sell later
"""
def maxProfits3(self, prices):
    maxprofits = 0
    minprice = prices[0]
    for p in prices:
        if p < minprice:
            minprice = p
        else:
            maxprofits = max(p - minprice)
    return maxprofits