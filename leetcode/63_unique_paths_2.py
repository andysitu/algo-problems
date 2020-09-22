from typing import List

class Solution:
    def print(self, nums):
        n = len(nums)
        for i in range(n):
            print(nums[i])
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        nums = [ [0] * m for x in range(n) ]

        found_obstacle = False

        for col in range(m-1, -1, -1):
            if found_obstacle:
                nums[n-1][col] = 0
            elif obstacleGrid[n-1][col] == 1:
                nums[n-1][col] = 0
                found_obstacle = True
            else:
                nums[n-1][col] = 1
        
        found_obstacle = False

        for row in range(n-1, -1, -1):
            if found_obstacle:
                nums[row][m-1] = 0
            elif obstacleGrid[row][m-1] == 1:
                nums[row][m-1] = 0
                found_obstacle = True
            else:
                nums[row][m-1] = 1

        for col in range(m-2, -1, -1):
            for row in range(n-2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    nums[row][col] = 0
                else:
                    nums[row][col] = nums[row+1][col]  + nums[row][col+1]
        
        # self.print(nums)
        return nums[0][0]

s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0,0,0,0],
  [0,1,0,0,0,0],
  [0,1,0,0,0,0],
  [0,0,0,0,0,0]
]))

# [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]