"""
Brute Force
This would require you sort all the numbers
added so far each time you need a median and then
get the median. Eacn sort would take nln while
the space complexity would be O(n) to store the
array of numbers and then to sort it.
"""

"""
In doing so, you see that you need a datastructure
to store two heaps with one being the numbers larger
than the median and then other numbers smaller

From the larger heap, you need to be able to get the
smallest number and from the smaller, you need to
be able to get the largest. One way to do this is by
pushing the negative of the number into the smaller heap
so that it would be sorted as desired.

Thus, it becomes a matter of managing the logistics

Runtime: O(lnn) for each n ; Space: O(n)
"""

import heapq

small = []
big = []

def addNum(self, num):
    heappush(large, -heappushpop(small, -num))
    if len(big) > len(small):
        heappush(small, -heappop(large))

def findMedian(self) -> float:
    if len(small) == small(big):
        return (large[0] - small[0]) / 2
    else:
        return -small[0]