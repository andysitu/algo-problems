from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return []
        triangles = [[1]]
        
        for i in range(1, rowIndex+1):
            t = []
            t.append(1)
            
            prev_list = triangles[i-1]
            for j in range( len(prev_list) - 1 ):
                t.append(prev_list[j] + prev_list[j+1])
            t.append(1)

            triangles.append(t)
        return triangles[rowIndex]