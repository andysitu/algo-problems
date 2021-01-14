class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrows = len(matrix)
        if nrows == 0:
            return []
        ncols = len(matrix[0])
        if ncols == 0 or ncols == 1:
            return matrix
        level = 0
        while True:


