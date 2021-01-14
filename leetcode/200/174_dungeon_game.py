from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ylen, xlen = len(dungeon), len(dungeon[0])
        minhp_cost = [[-float("inf")] * (xlen+1) for i in range(ylen+1)]
        minhp_cost[ylen-1][xlen] = -1
        minhp_cost[ylen][xlen-1] = -1
        
        for i in range(ylen-1, -1, -1):
            for j in range(xlen-1,-1,-1):
                minhp_cost[i][j] = min(-1, max(minhp_cost[i+1][j], minhp_cost[i][j+1]) + dungeon[i][j])
        return -minhp_cost[0][0]
        
s = Solution()

print(s.calculateMinimumHP([[3,0,-3],[-3,-2,-2],[3,1,-3]])==1)
print(s.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])==3)

print(s.calculateMinimumHP([[100]])==1)
print(s.calculateMinimumHP([[-1, -1]])==3)
print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])==7)
print(s.calculateMinimumHP([[-2,-3,5,4],[-5,-1,1,4],[5,6,-5,-2]])==6)
print(s.calculateMinimumHP([[-2,-9,5,4],[-10,-1,-4,4],[5,6,-5,-2],[5,4,-9,-2]])==12)