from typing import List
import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = [[] for _ in range(numCourses)] # key - all #s that depend on it
        dependent = [[] for _ in range(numCourses)] # key - it depends on all #'s in its list in key

        for l in prerequisites:
            dependencies[l[1]].append(l[0])
            dependent[l[0]].append(l[1])

        cycle_status = [0 for _ in range(numCourses)]

        schedule = []
        q = queue.Queue()

        for i in range(numCourses):
            if len(dependent[i]) == 0:
                q.put(i)

        prev = -1

        while not q.empty():
            v = q.get()
            # print(v, cycle_status)
            if cycle_status[v] == 1:
                continue
            put_status = True
            for n in dependent[v]:
                if cycle_status[n] != 1:
                    put_status = False
                    q.put(n)
                    
            if put_status:
                cycle_status[v] = 1
                schedule.append(v)
                for n in dependencies[v]:
                    if cycle_status[n] != 1:
                        q.put(n)
                    else:
                        return []
            else:
                if cycle_status[v] == -1 and cycle_status[prev] == -1:
                    # print(v)
                    return []
                cycle_status[v] = -1
                q.put(v)
            prev = v
        # print(cycle_status)
        if len(schedule) != numCourses: # no root exists for an island
            return []
        return schedule

s = Solution()
# print(s.findOrder(9, [[1,0], [4,2],[5,7],[6,2],[4,3]]))
# print(s.findOrder(2, [[1,0], [0,1]])==[])
# print(s.findOrder(10, [[5,1],[3,1],[4,3],[4,1],[6,4],[1,6]])==[])
# print(s.findOrder(10, [[5,1],[3,1],[4,3],[4,1]]))
# print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
# print(s.findOrder(10, [[5,1],[3,1],[4,3],[4,1],[1,6],[6,3]])==[])
# print(s.findOrder(3, [[1,0],[1,2],[0,1]])==[])

# print(s.findOrder(3,[[0,1],[0,2],[1,2]]))
