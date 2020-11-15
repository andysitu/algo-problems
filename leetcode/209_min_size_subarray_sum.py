from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0,0
        value = nums[0]
        nmin = len(nums)+1
        while left <= right:
            if value < s:
                if right == len(nums)-1:
                    break
                else:
                    right += 1
                    value += nums[right]
            else:
                if right - left + 1 < nmin:
                    nmin = right-left+1
                value -= nums[left]
                left += 1
        if nmin == len(nums)+1:
            return 0
        return nmin

s = Solution()
print(s.minSubArrayLen(42,
[4, 15, 15, 13, 9, 13, 13, 6, 15, 9, 5, 9, 8, 13, 14, 11, 3, 1, 4, 4, 7, 12, 13, 6, 43, 12, 14, 15, 4, 14]))
