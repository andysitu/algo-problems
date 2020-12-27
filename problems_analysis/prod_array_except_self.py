"""
Given an array nums of n integers where n > 1,  return an array 
output such that output[i] is equal to the product of all the 
elements of nums except nums[i].
"""

"""
Brute Force
For each i in num, calculate all other in a product
Runtime: O(n^n) Space: O(n)
"""

"""
2 Arrays
Have 2 arrays, one to save calculation on starting from the left
and one starting from the right. Then, have save all calculations
from starting point up until i-1.
Finally iterate through it and calculate the values by getting
product of left[i] * right[i]
Runtime: O(n) ; Space O(n)
"""

"""
1 Array
You can just calculate one direction and then as you iterate 
through the other direction you have an variable saving this value
It would give your space in half.
"""
