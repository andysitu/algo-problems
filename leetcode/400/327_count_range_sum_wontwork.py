from typing import List

import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        print(nums)
        nlen = len(nums)
        leftsum = [0] * nlen
        rightsum = [0] * nlen
        leftsum[0] = nums[0]
        for i in range(1,nlen):
            leftsum[i] = leftsum[i-1] + nums[i]
        
        rightsum[nlen-1] = nums[nlen-1]
        for i in range(nlen-2, -1, -1):
            rightsum[i] = rightsum[i+1] + nums[i]
        total = rightsum[0]
        print(leftsum, rightsum)

        leftsum.sort()
        rightsum.sort()
        
        print(leftsum, rightsum)

        s = 0

        for l in leftsum:
            # upper >= total-left-rightsum or rightsum >= total - l - upper
            li = bisect.bisect_right(rightsum, total-l-upper)
            print("le", l, li)
            
            # lower <= total - left - rightsum
            ri = bisect.bisect_left(rightsum, total-l-lower)
            print("re", l, ri)
            
            s += max(0, ri-li+1)
            # having a 0 means that you can have no values, so account for it
            if lower <= 0 <= upper:
                s -= 1
            print(ri-li, s)
        print(s)
        return s

s = Solution()
print(s.countRangeSum([-2,5,-1], -2, 2))