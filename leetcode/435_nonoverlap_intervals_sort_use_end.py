class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        sorted_intervals = sorted(intervals, key=lambda i: i[1])
        last = -float('inf')
        count = 0
        for i in sorted_intervals:
            if i[0] >= last:
                last = i[1]
            else:
                count += 1
        return count