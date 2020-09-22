from typing import List

class Solution:
    def print(self, nums):
        n = len(nums)
        for i in range(n):
            print(nums[i])
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        nums = [ [0] * m for x in range(n) ]

        nums[n-1][m-1] = grid[n-1][m-1]

        for col in range(m-2, -1, -1):
            nums[n-1][col] = nums[n-1][col + 1] + grid[n-1][col]

        for row in range(n-2, -1, -1):
            nums[row][m-1] = nums[row+1][m-1] + grid[row][m-1]

        for col in range(m-2, -1, -1):
            for row in range(n-2, -1, -1):
                a = nums[row+1][col]
                b = nums[row][col+1]
                if a > b:
                    nums[row][col] = b + grid[row][col]
                else:
                    nums[row][col] = a + grid[row][col]
        
        # self.print(nums)
        return nums[0][0]

s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))

[[1,3,4,2,5,7,34,4,65,7,23,100,4,2,5,6,3,4,1,2,43,124,2,3,2,5,6,34,143],[1,3,4,2,5,7,34,4,65,7,23,100,4,2,5,6,3,4,1,2,43,124,2,3,2,5,6,34,143],[1,3,4,2,5,7,34,4,65,7,23,100,4,2,5,6,3,4,1,2,43,124,2,3,2,5,6,34,143],[1,3,4,2,5,7,34,4,65,7,23,100,4,2,5,6,3,4,1,2,43,124,2,3,2,5,6,34,143],[1,3,4,2,5,7,34,4,65,7,23,100,4,2,5,6,3,4,1,2,43,124,2,3,2,5,6,34,143],[1,3,4,2,5,7,34,4,65,7,23,100,4,2,5,6,3,4,1,2,43,124,2,3,2,5,6,34,143],[1,3,4,2,5,7,34,4,65,7,23,100,4,2,5,6,3,4,1,2,43,124,2,3,2,5,6,34,143]]