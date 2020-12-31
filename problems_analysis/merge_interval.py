"""
Continuing from insert interval
Using left and right pointer
Have a new array with the final intervals
Set left and right pointer to the current interval i
move right pointer until you find either the right interval
being larger or the first interval or none at all

Sort the intervals.

If the right, continue. If the left, append to the answer
interval with left ptr and right interval. If none,
then append left right interval

Runtime O(nln n) due to sorting, space: O(n) for the answer array
"""