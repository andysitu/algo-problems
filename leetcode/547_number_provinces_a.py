class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        clen = len(isConnected)
        cities = [0] * clen
        num = 1
        for i in range(clen):
            if cities[i] != 0:
                continue
            new_status = -1
            for j in range(i+1, clen):
                if isConnected[i][j] and cities[j] != 0:
                    new_status = cities[j]
                    break
            if new_status == -1:
                new_status = num
            for j in range(i, clen):
                if isConnected[i][j]:
                    cities[j] = new_status
            if new_status == num:
                num += 1
        return num - 1