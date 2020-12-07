from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)   
        l = list(nums)
        l.sort()
        if nlen % 2 == 0:
            mid = (nlen // 2) - 1
        else:
            mid = nlen // 2
        m = mid
        for i in range(0, nlen, 2):
            nums[i] = l[m]
            m -= 1
        m = nlen - 1
        for i in range(1, nlen, 2):
            nums[i] = l[m]
            m -= 1
        print(nums)
        

s = Solution()
print(s.wiggleSort([1, 5, 1, 1, 6, 4]))
print(s.wiggleSort([1, 3, 2, 2, 3, 1]))
print(s.wiggleSort([1,1,1,1,1,1,3,3,3,3,3,3]))
print(s.wiggleSort([4,5,5,6]))
print(s.wiggleSort([4,5]))
print(s.wiggleSort([5,4]))
print(s.wiggleSort([4,2,1,5,7,8,3,4,1,1,2,4,5,7,8]))
print(s.wiggleSort([2,3,3,2,2,2,1,1]))