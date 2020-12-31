"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

"""
Brute Force
You'd search all of the intervals invidiaully. Insertion would be similar
to the next option as it is difficult trying to maintain all the use cases

Runtime O(n) ; Space O(1)
"""

"""
Pointers
Left and right pointer for the left & right of the interval.
Then, bin search for all the respective values and then insert it
Remove those in the middle of the interval and then the cases needed
are if pointer equals a start value or end value or if it is in between
a start and end value or a end and start value.

For simplicity, insert a new interval but change its left and right 
values depending on what scenarios the two pointers encounter.
Then, test if it should merge with adjacent intervals.

For example, if it is between an interval, set the starting value
to the end value
"""