from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        listlen = len(triangle)
        if listlen == 1:
            return triangle[0][0]

        paths = triangle[listlen - 1]

        for i in range(listlen-2, -1, -1):
            # print(i, paths)
            for j in range( i + 1):
                paths[j] = triangle[i][j] + min(paths[j], paths[j+1])
            # print(i, paths)
        return paths[0]


s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))