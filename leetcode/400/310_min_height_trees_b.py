from typing import List
import queue
import data310

class Solution:
    def travel(self, root, n):
        travelset = set()
        travelset.add(root)
        q = queue.Queue()
        q.put((n, 1, [n]))

        maxheight = 0
        paths = None
        
        while not q.empty():
            ntup = q.get()
            if ntup[1] > maxheight:
                maxheight = ntup[1]
                paths = [ntup[2]]
            for child in self.branchMap[ntup[0]]:
                if child not in travelset:
                    q.put((child, ntup[1]+1, ntup[2] + [child]))
                    travelset.add(child)
        return maxheight, paths

    def getHeight(self, n):
        travelset = set()
        maxheight = 1
        travelset.add(n)
        q = queue.Queue()
        q.put((n, 1))

        while not q.empty():
            ntup = q.get()
            maxheight = max(maxheight, ntup[1])
            for b in self.branchMap[ntup[0]]:
                if b not in travelset:
                    q.put((b, ntup[1]+1))
                    travelset.add(b)
        return maxheight

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

        q = queue.Queue()
        q.put(0)
        while not q.empty():
            v = q.get()
            vheight = self.getHeight(v)
            if len(self.branchMap[v]) == 1:
                child = self.branchMap[v][0]
                maxh, paths = self.travel(v, child)
                if maxh % 2 == 0:
                    q.put(paths[ (len(paths) / 2 - 1 )])
                else:
                    q.put(paths[ (len(paths) // 2)])
            else:
                maxh = 0
                minh = n+1
                maxhs = None
                maxh2 = None
                maxh2s = None
                for child in self.branchMap[v]:
                    h, paths = self.travel(v, child)
                    minh = min(minh, h)
                    if h > maxh:
                        maxh2 = maxh
                        maxh = h
                        maxh2s = maxhs
                        maxhs = [h] 
                    elif h == maxh:
                        maxhs.append(h)                        
                    elif h == maxh2:
                        maxh2s.append(h)
                if len(maxhs) > 1:
                    return v
                elif maxh2 != None and len(maxh2s) == 1 and maxh = maxh2 - 1:
                    return [v] + maxhs
                else:
                    if (maxhs - minh)%2==0:
                        q.put(paths[ (len(paths) / 2 - 1 )])
                
                     
        

s = Solution()
# print(s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
# print(s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))


# print(s.findMinHeightTrees(1111, s1))
print(s.findMinHeightTrees(5000, data310.s2))