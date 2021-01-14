import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.large, num)
            heapq.heappush(self.small, -heapq.heappop(self.large))
            # heapq.heappush(self.small, -heapq.heappop(self.large))
            

    def findMedian(self) -> float:
        if len(self.small) != len(self.large):
            return heapq.nsmallest(1, self.large)[0]
        else:
            return (-heapq.nsmallest(1, self.small)[0] + heapq.nsmallest(1, self.large)[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()