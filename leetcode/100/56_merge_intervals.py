from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nlens = len(intervals)
        if nlens==0:
            return []
        values = []
        intervals = sorted(intervals, key = lambda x: x[0])

        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, nlens):
            a = intervals[i]
            if right > a[1]:
                pass
            elif right >= a[0]:
                right = a[1]
            else:
                values.append([left, right])
                left = a[0]
                right = a[1]
        values.append([left, right])
        return values

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
print(s.merge([]))
print(s.merge([[1,2]]))