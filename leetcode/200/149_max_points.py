# Didn't Continue, Seems to be about float calculation more
from typing import List
import sys
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        maxpoints = 0
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if points[i][0] - points[j][0] == 0:
                    m = "inf"
                else:
                    m = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    b = points[i][1] - m * points[i][0]

                # print(m, i, j, b)

                count = 2
                for index in range(len(points)):
                    if index == i or index == j:
                        continue
                    if m == "inf":
                        if points[index][0] == points[i][0]:
                            count += 1
                        continue
                    else:
                        if points[i][0] - points[index][0] == 0:
                            continue
                        testm = (points[i][1] - points[index][1]) / (points[i][0] - points[index][0])
                        testb = points[i][1] - testm * points[index][0]
                        print(m.as_integer_ratio(), testm.as_integer_ratio())
                        print(b.as_integer_ratio(), testb.as_integer_ratio())
                        if m.as_integer_ratio() == testm.as_integer_ratio() \
                            and b.as_integer_ratio() == testb.as_integer_ratio():
                            count += 1
                    print(index, points[index][1] - m * points[index][0] == b)
                maxpoints = max(maxpoints, count)
        return maxpoints

"""
Got up to 40/41
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        maxpoints = 0
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if points[i][0] - points[j][0] == 0:
                    m = "inf"
                else:
                    m = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    b = points[i][1] - m * points[i][0]

                # print(m, i, j, b)

                count = 2
                for index in range(len(points)):
                    if index == i or index == j:
                        continue
                    if m == "inf":
                        if points[index][0] == points[i][0]:
                            count += 1
                        continue
                    elif math.isclose(points[index][1] - m * points[index][0],b):
                        count += 1
                    # print(index, points[index][1] - m * points[index][0] == b)
                maxpoints = max(maxpoints, count)
        return maxpoints

[[0,0]]
[[3,1],[12,3],[3,1],[-6,-1]]
[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
[[0,0],[94911151,94911150],[94911152,94911151]]
"""
[[0,0],[94911151,94911150],[94911152,94911151]]