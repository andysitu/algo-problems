"""
Bruce force
Calculate all combinations
Runtime: O(2^n)
"""

"""
DP
Use previous 2 calculations and save the minimal
along with cost at i into dp.
Runtime O(n); Space O(n)
"""

"""
Truncate DP into 2 variables + temporary variable
From the previous calculation, you only need the last two
values and then to get the minimal of them which then
becomes the most recent of the two variables.

Runtime O(n) Space O(1)
"""