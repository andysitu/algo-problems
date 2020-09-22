from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hlen = len(heights)
        if hlen == 0:
            return 0

        leftindex = [-1] * hlen
        rightindex = [-1] * hlen

        leftindex[0] = -1
        rightindex[hlen-1] = hlen

        for i in range(1, hlen):
            if heights[i] <= heights[i-1]:
                a = leftindex[i-1]
                while a >= 0 and heights[a] >= heights[i]:
                    a -= 1
                leftindex[i] = a
            else:
                leftindex[i] = i-1
        
        for i in range(hlen -2, -1, -1):
            if heights[i] <= heights[i+1]:
                a = rightindex[i+1]
                while a <= hlen - 1 and heights[a] >= heights[i]:
                    a += 1
                rightindex[i] = a
            else:
                rightindex[i] = i+1

        maxarea = 0
        for i in range(hlen):
            # print(i, rightindex[i], leftindex[i])
            maxarea = max(maxarea, heights[i] * (rightindex[i] - leftindex[i] - 1))

        return maxarea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0])==0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        max_area = 0

        if rows < cols:
            prev_rows = [0] * rows
            
            for c in range(cols):
                for r in range(rows):
                    cell = matrix[r][c]
                    if cell == "0":
                        prev_rows[r] = 0
                    else:
                        prev_rows[r] += 1
                max_area = max(max_area, self.largestRectangleArea(prev_rows))
        else:
            prev_cols = [0] * cols
            for r in range(rows):
                for c in range(cols):
                    cell = matrix[r][c]
                    if cell == "0":
                        prev_cols[c] = 0
                    else:
                        prev_cols[c] += 1
                max_area = max(max_area, self.largestRectangleArea(prev_cols))

        return max_area
                

        
s = Solution()
print(s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])==6)
print(s.maximalRectangle([])==0)
print(s.maximalRectangle([["0"]])==0)
print(s.maximalRectangle([["1"]])==1)
print(s.maximalRectangle([["1", "1"]])==2)
print(s.maximalRectangle([["0", "0"]])==0)