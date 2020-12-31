"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that 
amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

"""
Brute Force
Try every single combination using a breath first search and return
the first result
Runtime O((num coins) ^ (amount / smallest coin denomination))
"""

"""
DP
In the brute force approach, one can see that there are a lot of overlap
in repeated calculations that you make to get a certain denomination
and combinations. By saving these results in DP, you can save a lot of time
at the expense of memory. You'd also save results that result in null
Runtime: O()
"""

"""
Optimization
Sort the values first so that largest goes first to fill up the space
as quickly as possible.

Remove any coins larger than the given value since you can't use it.
"""