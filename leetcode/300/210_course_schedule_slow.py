import queue

class Solution:
    def travel(self, dependencies, cycle_status, value):
        if cycle_status[value] >= 1:
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

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = [[] for _ in range(numCourses)] # key - all #s that depend on it
        dependent = [[] for _ in range(numCourses)] # key - it depends on all #'s in its list in key

        for l in prerequisites:
            dependencies[l[1]].append(l[0])
            dependent[l[0]].append(l[1])
        cycle_status = [0 for _ in range(numCourses)]

        for i in range(numCourses):
            if len(dependencies[i]) == 0:
                cycle_status[i] = 2
        
        for i in range(numCourses):
            if self.travel(dependencies, cycle_status, i) == False:
                return []

        schedule = []
        q = queue.Queue()

        for i in range(numCourses):
            if len(dependent[i]) == 0:
                q.put(i)

        # print(dependencies, dependent)

        while not q.empty():
            v = q.get()
            if cycle_status[v] == 3:
                continue
            put_status = True
            for n in dependent[v]:
                if cycle_status[n] != 3:
                    put_status = False
                    q.put(n)
            if put_status:
                cycle_status[v] = 3
                schedule.append(v)
                for n in dependencies[v]:
                    if cycle_status[n] != 3:
                        q.put(n)
            else:
                q.put(v)
        return schedule