from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        for i in range(k):
            while d:
                if d[0] < nums[i]:
                    d.popleft()
                else:
                    break
            d.appendleft(nums[i])
        maxlist = [d[-1]]
        
        for i in range(k, len(nums)):
            while d:
                if d[0] < nums[i]:
                    d.popleft()
                else:
                    break
            d.appendleft(nums[i])
            if d[-1] == nums[i-k]:
                d.pop()
            maxlist.append(d[-1])
        
        return maxlist