"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

"""
Brute Force
2 For loops, at i search if there are values from i+1 to end of the same value
Runtime: O(n^2) ; space: O(1)
"""

"""
Using Set
Check if number is in the saved set, If not, add to the set, and continue checking
Runtime: O(n) ; Space: O(n)
"""

"""
Sorting
Sort the numbers first and then for each number check if the previous number is equal
to it.
Runtime(nln(n)) ; Space: O(1)
"""