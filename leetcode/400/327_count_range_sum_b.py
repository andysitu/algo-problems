from typing import List

import bisect

class Solution:
    def count(self, nums,  lower, upper):
        nlen = len(nums)
        if  nlen == 0:
            return

        leftsum = []
        s = 0
        for i in range(nlen):
            s += nums[i]
            leftsum.append(s)
        
        sorted_leftsum = list(leftsum)
        sorted_leftsum.sort()

        print(leftsum, sorted_leftsum)

        removed = 0
        adjusted = 0
        for i in range(nlen):

            if lower - adjusted <= leftsum[i] <= upper - adjusted:
                removed += 1
            adjusted += nums[i]

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.answers = []
        self.count(nums, lower, upper)

s = Solution()
print(s.countRangeSum([-2,5,-1], -2, 2))