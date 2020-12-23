"""
Brute force approach
Try all combinations O(n^3) Runtime; space O(1)
"""

"""
Sort First, then for i in nums,
get left pointer to be i+1, right pointer to be end of nums
Want to set target - nums[i] - nums[ltpr] - nums[rptr] = 0
if that value is greater than 0, move rptr down by 1
if value is less than 0, move ltptr up
Runtime O(n^2); Space O(1)
"""

"""
HashMap of all the possible 2 values
Then, iterate through nums with i and
check if target-nums[i] exist in the nums map
Complexity: O(n^2); Space(n^2)
"""

"""
HashMap of all values
Iterate through numbers in 2 for loops,
check if targetnums[i][j] exist in nums map
Complexisty: O(n^2); Space (n)
"""
