"""
Given an array of integers and an integer k, find out whether there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the absolute difference 
between i and j is at most k.
"""

"""
Brute Force
For each number, have an inner for loop that searches for k values
Runtime: O(kn) ; Space: O(1)
If k is small, this wouldn't be a bad approach since you don't require any space
"""

"""
Dictionary / HashSet
For each number, save n as the key and the index as the value.
For each number, check if it is in the dictionary, and then if it is, compare
the indices to see if it is within k. If not, then overwite the number

Runtime: O(n) ; Space: O(n)
Takes a lot of space because you technically only need k, so if k is small,
then you're wasting a lot of space
"""

"""
Dictionary with a Queue
I tried to think of datastructures to minimize the space. Linked lists sorted,
etc. You can have a queue of size k and then use queue to tell you what to delete
from the dictionary after searching the dictionary as done previously.
This is with the assumption that deleting from the dictionary wouldn't take
that long of a time and in exchange for that slight runtime you decrease your space.
Runtime: O(n) ; Space: O(k)
"""