class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        clen = len(isConnected)
        
        def travel(isConnected, cities, i, n):
            for j in range(clen):
                if isConnected[i][j] == 1 and i != j and cities[j] == 0:
                    cities[j] = n
                    travel(isConnected, cities, j, n)
        
        cities = [0] * clen
        num = 1
        for i in range(clen):
            if cities[i] == 0:
                travel(isConnected, cities, i, num)
                num += 1
        return num - 1