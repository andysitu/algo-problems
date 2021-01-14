from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.large, -heappushpop(self.small, -num))
        if len(self.small) != len(self.large):
            heappush(self.small, -heappop(self.large))
            

    def findMedian(self) -> float:
        if len(self.small) != len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()n