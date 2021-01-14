from typing import List

class Solution:
    def travel(self, dependencies, cycle_status, value):
        if cycle_status[value] == 1:
            return True
        if cycle_status[value] == -1:
            return False
        for d in dependencies[value]:
            cycle_status[value] = -1
            r = self.travel(dependencies, cycle_status, d)
            if r == False:
                return False
        cycle_status[value] = 1
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = [[] for _ in range(numCourses)]
        for l in prerequisites:
            dependencies[l[1]].append(l[0])
        cycle_status = [0 for _ in range(numCourses)]

        for i in range(numCourses):
            if len(dependencies[i]) == 0:
                cycle_status[i] = 1
        
        for i in range(numCourses):
            r = self.travel(dependencies, cycle_status, i)
            if r == False:
                return False
        return True
            

s = Solution()
print(s.canFinish(9, [[1,0], [4,2],[5,7],[6,2],[4,3]])==True)
print(s.canFinish(2, [[1,0], [0,1]])==False)
print(s.canFinish(10, [[5,1],[3,1],[4,3]])==True)
print(s.canFinish(10, [[5,1],[3,1],[4,3],[4,1]])==True)
print(s.canFinish(10, [[5,1],[3,1],[4,3],[4,1],[1,6],[6,3]])==False)