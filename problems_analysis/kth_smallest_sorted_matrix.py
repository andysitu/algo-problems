"""
The only solution that I have is the naive solution.
Go through the smallest number and count up until
you reach k. I need a data structure to be able to do that
or else I would have to compare the values every time.

The heap is perfect for this scenario and to retrieve the 
smallest value would be constant time which to store it
would take ln n for n numbers placed.

Runtime: O(klnk) ; Space: O(k)
"""

"""
A solution that I read was to do a binary search with the highest
and lowest numbers. You would have to find the number the is closest
to this middle number and then count the number of values that are
equal or less than this value. The solution will be probably much
faster at the average case, but it seems messy to me. In scenarios 
such as when you have a high proportion of numberse being higher than
the mid point or even better lower than the mid point, then you 
can skew the results such that the runtime of this method will be
greater.
"""