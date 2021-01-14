from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        place = m + n - 1
        
        for t in range(m + n):
            if i < 0:
                nums1[place] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[place] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[place] = nums1[i]
                i -= 1
            else:
                nums1[place] = nums2[j]
                j -= 1
            place -= 1
        print(nums1)


s = Solution()
s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)