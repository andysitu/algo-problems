from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            matched = False
            if i > 0 and nums[i] == nums[i-1]:
                matched = True
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                matched = True
            if not matched:
                return nums[i]

s = Solution()
print(s.singleNumber([2,2,1]))