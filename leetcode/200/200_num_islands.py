from typing import List

class Solution:
    def destroy(self, grid, y,x):
        stack = []
        stack.append((y,x))
        i,j = None, None
        
        while stack:
            i,j = stack.pop()
            # if grid[i][j] == '1':
            #     print(i,j)
            grid[i][j] = '.'
            if i != 0 and grid[i-1][j] == '1':
                stack.append((i-1, j))
            if i != len(grid)-1 and grid[i+1][j] == '1':
                stack.append((i+1, j))
            if j != 0 and grid[i][j-1] == '1':
                stack.append((i, j-1))
            if j != len(grid[0])-1 and grid[i][j+1] == '1':
                stack.append((i, j+1))
                        
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0])==0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.destroy(grid, i, j)
        # print(grid)
        return count

s = Solution()
# print(s.numIslands([
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]))

print(s.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]]))