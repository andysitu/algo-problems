from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangles = [[1]]
        if numRows == 1:
            return triangles
        
        for i in range(1, numRows):
            t = []
            t.append(1)
            
            prev_list = triangles[i-1]
            for j in range( len(prev_list) - 1 ):
                t.append(prev_list[j] + prev_list[j+1])
            t.append(1)

            triangles.append(t)
        return triangles