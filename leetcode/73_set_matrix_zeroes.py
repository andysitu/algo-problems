from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numrows = len(matrix)
        if numrows == 0:
            return matrix
        numcols = len(matrix[0])
        rows = [0] * numrows
        cols = [0] * numcols

        for row in range(numrows):
            for col in range(numcols):
                if matrix[row][col] == 0:
                    rows[row] = 1
                    cols[col] = 1
                    
        for row in range(numrows):
            if rows[row] == 1:
                for i in range(numcols):
                    matrix[row][i] = 0
        for col in range(numcols):
            if cols[col] == 1:
                for i in range(numrows):
                    matrix[i][col] = 0

s = Solution()
print(s.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))