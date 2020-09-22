class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if n <= 1:
            return n
        m = len(obstacleGrid[0])
        if m == 1:
            return m

        nums = []
        for row in range(n):
            nums.append([0] * m)

        for col in range(m):
            nums[n-1][col] = 1

        for row in range(n):
            nums[row][m-1] = 1

        for col in range(m-2, -1, -1):
            for row in range(n-2, -1, -1):
                nums[row][col] = nums[row+1][col]  + nums[row][col+1]
        
        # print(nums)
        return nums[0][0]

s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])==2)