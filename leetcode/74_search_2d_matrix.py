from typing import List

class Solution:
    def search(self, matrix, target, search_row):
        left = 0
        if search_row == -1:
            right = len(matrix) - 1
        else:
            right = len(matrix[search_row]) - 1

        while left + 1 < right:
            mid = int((right + left) / 2)
            if search_row == -1:
                m = matrix[mid][0]
            else:
                m = matrix[search_row][mid]

            if m == target:
                return mid, -1
            elif m < target:
                left = mid
            else:
                right = mid

        return left, right

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l, r = self.search(matrix, target, -1)

        if r == -1:
            return True

        if matrix[r][0] <= target:
            row = r
        elif matrix[r][0]:
            row = l
        print(l, r, row)

        l, r = self.search(matrix, target, row)
        print(l, r)
        if matrix[row][l] == target or matrix[row][r] == target:
            return True
        return False
        


s = Solution()
# print(s.searchMatrix([
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ], 15)== False)
# print(s.searchMatrix([
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ], 7))
# print(s.searchMatrix([
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 24, 25, 29],
#   [30, 30, 34, 50],
  
# ], 0))
# print(s.searchMatrix([
#   [1, ],
#   [2, ]
# ], 2))
print(s.searchMatrix([
  [1,   3,  5,  7, 8],
  [10, 11, 16, 20, 21],
  [23, 24, 25, 29, 29],
  [30, 30, 34, 50, 58],
], 0))