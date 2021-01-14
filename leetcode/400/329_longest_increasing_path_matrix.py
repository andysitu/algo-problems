from typing import List

class Solution:
    def travel(self, matrix, i, j, prevn, dp):
        if i == -1 or j == -1 or i == len(matrix) or j == len(matrix[0]):
            return 0
        if matrix[i][j] == '.':
            return 0
        if matrix[i][j] <= prevn:
            return 0

        if dp[i][j] != '.':
            return dp[i][j]
        
        p = matrix[i][j]
        matrix[i][j] = '.'
        best_value = max(
            self.travel(matrix,i+1,j,p, dp),
            self.travel(matrix,i,j+1,p, dp),
            self.travel(matrix,i-1,j,p, dp),
            self.travel(matrix,i,j-1,p, dp),
        )
        matrix[i][j] = p
        dp[i][j] = best_value + 1
        return best_value + 1
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        if cols == 0:
            return 0
        dp = [['.'] * cols for _ in range(rows)]
        m = 0
        for i in range(rows):
            for j in range(cols):
                m = max(m, self.travel(matrix,i,j,-float('inf'), dp))
        
        return m

s = Solution()
print(s.longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
] ), 4)

print(s.longestIncreasingPath([
  [1,1,1],
  [1,1,1],
  [1,1,1]
] ), 1)

print(s.longestIncreasingPath([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]))