from typing import List
# import queue

class Solution:
    def travel(self, dependencies, travel_status, value,schedule):
        if travel_status[value] == 1:
            return True
        if travel_status[value] == -1:
            return False
        for d in dependencies[value]:
            travel_status[value] = -1
            r = self.travel(dependencies, travel_status, d,schedule)
            if r == False:
                return False
        
        travel_status[value] = 1
        schedule.insert(0,value)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = [[] for _ in range(numCourses)]
        for l in prerequisites:
            dependencies[l[1]].append(l[0])
        travel_status = [0 for _ in range(numCourses)]

        # for i in range(numCourses):
        #     if len(dependencies[i]) == 0:
        #         travel_status[i] = 1

        schedule = []
        for i in range(numCourses):
            if self.travel(dependencies, travel_status, i, schedule) == False:
                return []
        return schedule

s = Solution()
# print(s.findOrder(9, [[1,0], [4,2],[5,7],[6,2],[4,3]]))
print(s.findOrder(2, [[1,0], [0,1]])==[])
print(s.findOrder(10, [[5,1],[3,1],[4,3],[4,1],[6,4],[1,6]])==[])
# print(s.findOrder(10, [[5,1],[3,1],[4,3],[4,1]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
# print(s.findOrder(10, [[5,1],[3,1],[4,3],[4,1],[1,6],[6,3]])==[])
print(s.findOrder(3, [[1,0],[1,2],[0,1]])==[])

# print(s.findOrder(3,[[0,1],[0,2],[1,2]]))
