from typing import List

class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        k = k % nlen
        if k == 0 or nlen==0 or nums == None:
            return

        self.reverse(nums, 0, nlen - 1 - k)
        self.reverse(nums, nlen - k, nlen-1)
        self.reverse(nums, 0, nlen-1)

s = Solution()
print(s.rotate([1,2,3,4,5,6], 2))