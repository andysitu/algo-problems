class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        branchMap = [ set() for _ in range(n) ]
        
        for s, e in edges:
            branchMap[e].add(s)
            branchMap[s].add(e)
            
        leaves = []
        for i in range(n):
            if len(branchMap[i]) == 1:
                leaves.append(i)
        numn = n
        while numn > 2:
            numn -= len(leaves)
            next_leaves = []
            while leaves:
                l = leaves.pop()
                
                neighbor = branchMap[l].pop()
                branchMap[neighbor].remove(l)
                if len(branchMap[neighbor]) == 1:
                    next_leaves.append(neighbor)
            leaves = next_leaves

        return leaves