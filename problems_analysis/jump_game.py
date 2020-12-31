"""
Brute Force
Probably use recursion in this case or a stack/ queue
to test every single combination/ route.
Runtime: O(n^n) would be my guess
"""

"""
DP
In the brute force approach, you can see that many of the 
routes are travelled repeatedly, especially the ones
close to the end of the route. As a result, you can save
the results if you first travel from left to right with
the results being whether at that i if it were able to
reach the end or not
Runtime: O(n); Space: O(n)
"""

"""
Save a variable instead
In doing the DP approach, you can see that you can just
save a variable that signifies the left most variable
that was seen that can reach the end. Then as you continue
to iterate the array, if you see anything to the right that
is able to reach that variable, you set variable to i
Runtime: O(n); Space: O(1)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left_marker = len(nums)-1
        for i in range(left_marker, -1, -1):
            if nums[i] + i >= left_marker:
                left_marker = i
        return left_marker == 0