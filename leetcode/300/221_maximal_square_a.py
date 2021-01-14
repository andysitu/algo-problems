# Count each row in the matrix of subsequent 1's
# Then in the counted row, look at each value and added to a count_set which is
# counting the # of continued values in each row of the counted rows.
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        counter = [0] * (len(matrix[0])+1)

        max_size = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    counter[j] += 1
                else:
                    counter[j] = 0

            count_sets = {}
            delkeys = []
            
            for j in range(len(matrix[0])+1): # the last one will be 0 to recaculate results
                v = 1
                for s in count_sets:
                    if count_sets[s] > max_size and count_sets[s] < s and s > max_size:
                        max_size = max(max_size, count_sets[s])

                    if s <= count_sets[s] and s > max_size:
                        max_size = max(s, max_size)
                        delkeys.append(s)
                    elif s <= max_size:
                        delkeys.append(s)
                    elif s <= counter[j]:
                        count_sets[s] += 1
                    else: # counter[j] is smaller than s
                        if counter[j] <= max_size:
                            delkeys.append(s)
                        else:
                            if counter[j] in count_sets:
                                count_sets[counter[j]] = max(count_sets[s] + 1, count_sets[counter[j]])
                            else:
                                v = max(count_sets[s]+1, v)
                                delkeys.append(s)
                if counter[j] > max_size and (counter[j] not in count_sets):
                    count_sets[counter[j]] = v
                
                while delkeys:
                    del count_sets[delkeys.pop()]
        return max_size ** 2
            

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]),4)
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","0","1"],["1","1","1","1","1"],["1","0","0","1","0"]]),1)
print(s.maximalSquare([["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]),0)
print(s.maximalSquare([["1","1","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]]),1)
print(s.maximalSquare([["1","0","1","1","1"],["1","1","0","0","1"],["0","1","1","1","1"],["1","0","1","0","1"]]),1)
print(s.maximalSquare([["1","0","1","1","1"],["1","1","0","0","1"],["0","1","1","1","1"],["1","0","1","1","1"]]),4)
print(s.maximalSquare([["1","0","1","1","1"],["1","1","1","1","1"],["0","1","1","1","1"],["1","0","1","1","1"]]),9)
print(s.maximalSquare([["1","0","1","1","1"],["1","1","1","1","1"],["0","1","1","1","0"],["1","0","1","1","1"]]),4)
print(s.maximalSquare([["1","1","1","1","1"],["1","1","1","1","1"],["0","1","1","0","0"],["1","0","1","1","1"]]),4)
print(s.maximalSquare([["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","0","0"],["1","0","1","1","1"]]),9)
print(s.maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]),4)