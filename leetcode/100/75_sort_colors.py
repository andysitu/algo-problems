from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ones = 0
        twos = 0
        for n in nums:
            if n == 0:
                zeroes += 1
            elif n == 1:
                ones += 1
            else:
                twos += 1
        for i in range(zeroes):
            nums[i] = 0
        for i in range(zeroes, ones+ zeroes):
            nums[i] = 1
        for i in range(ones+zeroes, len(nums)):
            nums[i] = 2
        print(nums)

s = Solution()
print(s.sortColors([1,0,0,0,1,1,2,0,2,1,1,0]))
print(s.sortColors([2,1,0]))
print(s.sortColors([]))
print(s.sortColors([1]))