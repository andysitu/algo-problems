import math
class Solution:
    def print_matrix(self, matrix):
        m = len(matrix)
        for i in range(m):
            print(matrix[i])

    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixlen = len(matrix)
        m = math.ceil(matrixlen/2)
        n = matrixlen - 1
        for y in range(m):
            for x in range(m):
                # odd number of rows/cols
                if matrixlen % 2 != 0:
                    if y == m-1 and x != m-1:
                        continue
                tempa = matrix[y][n-x]
                matrix[y][n-x] = matrix[x][y]

                tempb = matrix[n-x][n-y]
                matrix[n-x][n-y] = tempa

                tempc = matrix[n-y][x]
                matrix[n-y][x] = tempb

                matrix[x][y] = tempc
                # print(x, y)
                # print(y,n-x)
                # print(n-x, n-y)
                # print(n-y , x)
        self.print_matrix(matrix)

s = Solution()
print(s.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))

print(s.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

print(s.rotate([
  [ 5, 1, 44, 9, 11],
  [ 2, 4, 33, 8, 10],
  [ 51, 13, 43, 92, 81],
  [13, 3, 22, 6, 7],
  [15,14, 99, 12,16]
]))