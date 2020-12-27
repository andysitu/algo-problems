"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

"""
Brute Force
Use recursion to solve every single combination where each point expands
to 2 new points.

As a result, this would like to Runtime: O(2^n)
"""

"""
Dynamic Programming
In calculating the brute force method you can see that dp would be very helpful
because you reuse many of the calculations repeatedly. Thus by using dp and
saving those points, your calculations would then have 
Runtime: O(n) ; Space : O(n)
"""

"""
Finally, in writing out the points that are to be calculated in using the
DP, you can see that at n, it uses n-1 and n-2 and so forth. As a result,
you can start at 1 and 2 and then build your way up from there with i
calculations (i being the actually required).
Runtime: O(n) ; Space: O(1)
"""