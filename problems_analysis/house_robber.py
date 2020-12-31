"""
Brute Force:
Can use recursive function to calculate every single combination
Due to the recursive nature where 1 function call will lead
to 2 more, with n depth, the runtime I think would be 2^n
"""

"""
DP
In the brute force approach, many of the calculations are redundant
and you can skip them saving the calculated max files in an array.
In each house at i, if you have the max profits from i+2 and i+3 
house then you can pick whichever is larger to rob and so on.
Runtime: O(n) ; Space: O(n)
"""

"""
DP with only 2 previous homes
Instead of looking 3 houses away, you only need to consider whether
you can rob the current house (and thus 2 houses away as well) or the
previous house (thus not robbing the current one)
"""

"""
Iterative with Constant Variables
The DP approach can be simplified where the variables can hold
the previous 2 values and for the current value you can either
rob the house and then add the profits in n+2 houses away or you
can not rob the house which means that you carry the profit from
i+1 house away.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p1 = 0
        p2 = 0
        for n  in nums:
            m = max(p1, p2+ n)
            p2 = p1
            p1 = m
        return m