# another possibility would be to use a heap
# for the addition of numbers, making it ln(n), but it wouldn't
# require sorting to get intervals. Depends on which takes priority
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nmap = set()
        # larger number is the bottom
        self.top = {}
        self.bottom = {}
        
    def addNum(self, val: int) -> None:
        if val not in self.nmap:
            self.nmap.add(val)
            if val-1 in self.nmap and val+1 in self.nmap:
                top = self.bottom[val-1]
                bottom = self.top[val+1]
                
                self.top[top] = bottom
                self.bottom[bottom] = top
                
                del self.bottom[val-1]
                del self.top[val+1]
            elif val-1 in self.nmap:
                top = self.bottom[val-1]
                self.top[top] = val
                self.bottom[val] = top
                
                del self.bottom[val-1]
            elif val+1 in self.nmap:
                bottom = self.top[val+1]
                self.top[val] = bottom
                self.bottom[bottom] = val
                
                del self.top[val+1]
            else:
                self.top[val] = val
                self.bottom[val] = val

    def getIntervals(self) -> List[List[int]]:
        a = []
        for start in self.top:
            a.append([start, self.top[start]])
        a.sort()
        return a


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()