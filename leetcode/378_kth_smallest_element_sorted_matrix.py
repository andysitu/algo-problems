import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mlen = len(matrix)
        heap = []
        
        for i in range(mlen):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        count = 0
        while heap:
            count += 1
            tup = heapq.heappop(heap)
            if count == k:
                return tup[0]
            elif tup[2] < mlen - 1:
                    heapq.heappush(heap, (matrix[tup[1]][tup[2]+1], tup[1], tup[2] + 1))