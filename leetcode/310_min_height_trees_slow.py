from typing import List
import queue
import data310

class Solution:
    def travel(self, root, n):
        travelset = set()
        travelset.add(root)
        q = queue.Queue()
        q.put((n, 1, [root, n]))

        maxheight = 0
        paths = None
        
        while not q.empty():
            ntup = q.get()
            travelset.add(ntup[0])
            if ntup[1] > maxheight:
                maxheight = ntup[1]
                paths = ntup[2]
            for child in self.branchMap[ntup[0]]:
                if child not in travelset:
                    q.put((child, ntup[1]+1, ntup[2] + [child]))
                    
        return maxheight, paths

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0,1]
        self.branchMap = {}

        for i in range(n):
            self.branchMap[i] = set()
        
        for e in edges:
            self.branchMap[e[0]].add(e[1])
            self.branchMap[e[1]].add(e[0])

        for b in self.branchMap:
            if len(self.branchMap[b]):
                root = b
        
        maxh=0
        maxhs = []
        for child in self.branchMap[root]:
            traveltup = self.travel(root, child)
            if traveltup[0] > maxh:
                maxh = traveltup[0]
                maxhs = [traveltup[1]]
            elif traveltup[0] == maxh:
                maxhs.append(traveltup[1])
        if len(maxhs) >= 2:
            return [root]

        # print(maxhs)
        
        pointa = maxhs[0][ len(maxhs[0]) - 1 ]
        # print(pointa)

        root=pointa
        maxh=0
        maxhs = []
        for child in self.branchMap[root]:
            traveltup = self.travel(root, child)
            if traveltup[0] > maxh:
                maxh = traveltup[0]
                maxhs = [traveltup[1]]
            elif traveltup[0] == maxh:
                maxhs.append(traveltup[1])
        if len(maxhs) >= 2:
            return [root]
        longest_path = maxhs[0]
        # print(longest_path)
        if len(longest_path) % 2 == 0:
            return [longest_path[ len(longest_path) //2 ], longest_path[ (len(longest_path) //2)-1 ]]
        else:
            return [longest_path[ len(longest_path) //2 ]]
        
        # if len(longest_path)

s = Solution()
print(s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))


print(s.findMinHeightTrees(1111, data310.s1))
print(s.findMinHeightTrees(5000, data310.s2))