import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        h = []
        for n in count:
            if len(h) == k:
                if count[n] > h[0][0]:
                    heapq.heappop(h)
                    heapq.heappush(h, (count[n], n))
            else:
                heapq.heappush(h, (count[n], n))
                
        return [x[1] for x in h]