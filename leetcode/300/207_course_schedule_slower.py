class Solution:
    def travel(self, dependencies, travel_list, cycle_status, value):
        if value not in dependencies or value in cycle_status:
            return True
        if value in travel_list:
            return False
        for d in dependencies[value]:
            r = self.travel(dependencies, travel_list + [value], cycle_status, d)
            if r == False:
                return False
        cycle_status.add(value)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = {}
        for l in prerequisites:
            if l[1] not in dependencies:
                dependencies[l[1]] = []
            dependencies[l[1]].append(l[0])
        cycle_status = set()
        
        for d in dependencies:
            r = self.travel(dependencies, [], cycle_status, d)
            if r == False:
                return False
        return True