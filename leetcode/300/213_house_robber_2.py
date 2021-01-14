from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        nlen = len(nums)
        if nlen == 0:
            return 0
        if nlen == 1:
            return nums[0]
        if nlen == 2:
            return max(nums[0], nums[1])

        # include last house
        price_inc = [0] * nlen
        price_inc[nlen-1] = nums[nlen-1]
        price_inc[nlen-2] = nums[nlen-2]
        price_inc[nlen-3] = nums[nlen-3] + nums[nlen-1]
        for i in range(nlen-4, 0, -1):
            price_inc[i] = nums[i] + max(price_inc[i+2], price_inc[i+3])

        # not include last house
        price_ninc = [0] * nlen
        price_ninc[nlen-1] = 0
        price_ninc[nlen-2] = nums[nlen-2]
        price_ninc[nlen-3] = nums[nlen-3]
        for i in range(nlen-4, -1, -1):
            price_ninc[i] = nums[i] + max(price_ninc[i+2], price_ninc[i+3])

        print(price_inc)
        print(price_ninc)
        
        return max(price_inc[1], price_inc[2], price_ninc[0], price_ninc[1])

s = Solution()
# print(s.rob([1,2,3,1])==4)
print(417, s.rob([6, 14, 2, 11, 15, 2, 13, 7, 7, 6, 3, 4, 15, 9, 11, 7, 8, 7, 4, 10, 7, 4, 3, 1, 1, 14, 12, 13, 9, 3, 1, 13, 6, 13, 8, 1, 5, 5, 1, 3, 10, 13, 1, 4, 3, 9, 0, 5, 5, 2, 8, 12, 12, 14, 12, 1, 5, 10, 8, 10, 8, 0, 3, 12, 8, 7, 10, 7, 10, 0, 9, 15, 10, 2, 4, 8, 5, 0, 12, 13, 2, 14, 0, 3, 2, 0, 4, 5, 14, 9, 8, 0, 11, 4, 13, 12, 14, 15, 13, 4]))
print(446, s.rob([6, 12, 12, 2, 2, 1, 12, 12, 8, 12, 10, 0, 8, 7, 4, 0, 11, 13, 10, 13, 4, 7, 15, 6, 0, 9, 15, 15, 6, 8, 10, 13, 7, 2, 6, 14, 5, 14, 7, 4, 13, 3, 13, 7, 9, 5, 8, 13, 3, 10, 12, 13, 10, 10, 3, 14, 5, 5, 5, 7, 11, 0, 14, 10, 15, 9, 9, 6, 14, 9, 11, 10, 3, 9, 2, 0, 11, 5, 1, 9, 8, 0, 13, 12, 13, 9, 3, 0, 7, 9, 11, 7, 0, 0, 10, 11, 3, 6, 11]))
print(462, s.rob([9, 0, 6, 12, 6, 9, 6, 10, 3, 5, 14, 15, 2, 15, 15, 14, 9, 15, 9, 14, 14, 6, 6, 11, 13, 9, 10, 2, 12, 10, 8, 7, 10, 5, 7, 10, 1, 2, 12, 6, 14, 10, 8, 15, 12, 13, 7, 14, 11, 6, 9, 2, 5, 3, 8, 10, 1, 7, 8, 12, 2, 7, 8, 0, 5, 5, 1, 3, 4, 15, 12, 12, 1, 12, 14, 4, 10, 2, 3, 15, 8, 15, 10, 1, 10, 6, 1, 13, 10, 8, 10, 15, 7, 11, 4, 2, 10, 2]))
print(14, s.rob([4, 2, 10, 2]))
print(14, s.rob([4, 2, 10, 2, 4]))
print(24, s.rob([4, 2, 10, 2, 14]))
print(24, s.rob([10, 4, 2, 10, 2, 14]))
print(34, s.rob([10, 2, 10, 2, 14, 8]))