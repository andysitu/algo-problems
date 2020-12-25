"""
The brute force attempt would be to try every single combination
at every single k. It would be logarithmic I believe but I can't
imagine a solution without having saved the values somewhere.
"""

"""
DP with 2 2D Arrays
One array would be for the bought profits with size num of days * k,
with k being the amount of transactions.
Another array would be for the sold profits with size num of days * k.
Each day you have 4 options: buy, continue holding the bought stock,
sell a stock you hold, continue holding nothing

You can combine the first 2 into the array since in either case you have
a stock in hand and you can combine the last 2 into an array since in either
case you won't have a stock in hand and you get the maximum profits from
each day.

Thus, 
Iterate through each day for each k
bought maxprofits = max(bmp[i-1][k], smp[i-1][k-1]-prices[i])
sold maxprofits = max(smp[i-1][k], bmp[i-1][k]+prices[i])

Runtime: O(numDays * k); Space: O(numDays * k)
"""

"""
DP with 1 2D array
This can be further reduced to 1 array because sold maxprofits only depends
on bmp at the current k, so you don't need a 2D array for bmp and you don't
even need an array since you can record the best buy profits at each k
in a separate variable. It would start at the -price[0] because at day 1
you either don't buy (meaning no stock) or you buy so you're forced to buy
in order to have a stock to sell on day 2.

It would either through k for each day
"""

"""
Edge case
An edge case would be k exceeds num of days or num of days /2 depending on what
is considered a transaction (if you can buy and sell on the same day, but then
that wouldn't make sense). If it does, then you can jus buy whenever you see a profit
"""