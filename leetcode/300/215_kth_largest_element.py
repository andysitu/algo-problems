from typing import List
import random

class Solution:
    def qs(self, nums, start, end, k):
        if start >= end and start == k:
            return nums[k]
        pivot = random.randint(start, end)
        nums[pivot], nums[end] = nums[end], nums[pivot]
        p = start - 1
        for i in range(start, end):
            if nums[end] >= nums[i]:
                p += 1
                nums[p], nums[i] = nums[i], nums[p]
        p += 1
        nums[end], nums[p] = nums[p], nums[end]

        if k == p:
            return nums[k]
        elif p > k:
            self.qs(nums,start, p-1,k)
            return nums[k]
        else:
            self.qs(nums,p+1,end,k)
            return nums[k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.qs(nums,0, len(nums)-1, len(nums)-k)

p = [11,4,3,2,12,4,3,2,5,6,3,1,22,4,5,0,-4,3,10,8]
s = Solution()
print( s.findKthLargest(p, 4) )
print( s.findKthLargest([4,3,2,1,10,10,10,8,8,5], 4) )