from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # print(buildings)
        if (len(buildings)) == 0:
            return []
        points = []
        for i in range(len(buildings)-1, -1, -1):
            b = buildings[i]
            points.append([b[1], b[2], b[2], "r"])
            points.append([b[0], b[2], b[2], "l"])
        # reversed so that you can delete from list successfully by going in rev
        points.sort(key=lambda p: p[0], reverse=True)
        # print(points)

        # compare points with buildings
        start = len(points) - 1
        for i in range(len(buildings)):
            b = buildings[i]
            for j in range(start, -1, -1):
                p = points[j]
                # print(p, b)
                
                if b[0] <= p[0] <= b[1] and b[2] > p[1]:
                    del points[j]
                    start -= 1
                elif b[0] <= p[0] < b[1] and b[2] < p[1] and p[3] == "r":
                    if p[2] == p[1]:
                        p[2] = b[2]
                    else:
                        p[2] = max(p[2], b[2])
                elif (p[3] == "r" and b[0] == p[0] and b[2] == p[1]) or \
                    (p[3] == 'l' and b[1] == p[0] and b[2] == p[1]) or \
                    (b[0] < p[0] < b[1] and b[2] == p[1]):
                    del points[j]
                    start -= 1
                elif b[0] > p[0]:
                    start = j - 1
                elif p[0] > b[1]:
                    break
        # print(points)
        a = []
        prev = None
        for i in range(len(points)-1, -1, -1):
            p = points[i]
            if p[3] == "l":
                n = [p[0], p[1]]
            else:
                if p[1] == p[2]:
                    n = [p[0], 0]
                else:
                    n = [p[0], p[2]]
            if prev != None and prev[1] == n[1]:
                continue
            a.append(n)
            prev = n
        return a

s = Solution()
# print(s.getSkyline([[2,9,10],[2,20,3],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# print(s.getSkyline([[0,1,3]]))
# print(s.getSkyline([[0,2,3],[2,5,3]]))
# print(s.getSkyline([[0,3,3],[1,5,3],[2,4,3],[3,7,3]]))
print(s.getSkyline([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]))

[[0,3,3],[1,5,3],[2,4,3],[3,7,3]]
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8],[30,40,5],[35,40,10],[36,60,2],[50,52,20]]
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
[[1,5,3], [1,5,3], [1,5,3]]
[[0,2,3],[2,5,3]]
[[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]