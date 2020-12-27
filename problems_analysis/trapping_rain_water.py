"""
Brute Force
At i test from i+1 to get the other wall and terrain
that detracts from the overall water. 

Runtime O(n^2) ; Space O(1)
"""

"""
DP
Have an array save the max wall seen from right edge to i
Iterate from the left side and then use the array for the 
calculation by know the right wall ahead of time while also
subtracting the land.

Runtime O(n); Space O(n)
"""

"""
Stack
Instead of using an array, use a stack. Space should usually
be much less unless the walls have a descending max height,
but on average it will take less space than the array,
which will always be sized n.
"""