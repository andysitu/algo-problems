
from typing import List

import queue

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        result = {}
        q = queue.Queue()
        q.put(0)
        while not q.empty():
            value = q.get()

            if value not in result:
                result[value] = 1
            color = result[value]

            if color == 1:
                new_color = 0
            else:
                new_color = 1
            
            nodes = graph[value]
            for y in nodes:
                if y not in result:
                    result[y] = new_color
                    q.put(y)
                else:
                    if result[y] != new_color:
                        return False
            if q.empty(): # Make sure all values have bene tested
                for i in range(len(graph)):
                    if i not in result:
                        q.put(i)
                        break
        return True
                    
s = Solution()
print(s.isBipartite([[1,3], [0,2], [1,3], [0,2]]))
print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
print(s.isBipartite([[2,3], [2,5], [0,1,3], [0,2,4], [3,6], [1,7], [4, 7], [5,6]]))
print(s.isBipartite([[2,3], [2,5], [0,1], [0,4], [3,6], [1,7], [4, 7], [5,6]]))
print(s.isBipartite([[2,3], [2,3,5], [0,1], [0,1,4], [3,6], [1,7], [4, 7], [5,6]]))
print(s.isBipartite([[2,3], [2,3,5], [0,1], [0,1,4], [3,6], [1,6,7], [4, 5, 7], [5,6]]))
print(s.isBipartite([[2,3], [2,3,5,6], [0,1], [0,1,4], [3,6], [1,7], [1,4, 7], [5,6]]))
print(s.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))