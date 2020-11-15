# can also cache precomputed areas and then use that.
# more memory, but make coputations O(1)

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        if self.rows == 0:
            return
        self.cols = len(matrix[0])
        if self.cols == 0:
            return
        
        self.map_values = []
        for r in range(self.rows):
            d = {}
            d["left"] = []
            s=0
            for n in matrix[r]:
                s += n
                d["left"].append(s)
                
            s=0
            d["right"] = [0] * self.cols
            for c in range(self.cols-1, -1, -1):
                s += matrix[r][c]
                d["right"][c] = s
            d["total"] = d["left"][self.cols-1]
            self.map_values.append(d)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.rows == 0 or self.cols == 0:
            return 0
        total = 0
        for r in range(row1, row2+1):
            total += self.map_values[r]["total"]
            if col1 > 0:
                total -= self.map_values[r]["left"][col1-1]
            if col2 < self.cols-1:
                total -= self.map_values[r]["right"][col2+1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)