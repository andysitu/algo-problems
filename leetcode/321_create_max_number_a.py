from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        len1 = len(nums1)
        len2 = len(nums2)

        count = len1 + len2 - k + 1
        # print("c", count, len1, len2)

        max1,max2=-1,-1
        max1i, max2i = -1, -1
        # print(nums1[:count], nums2[:count])
        for i, n in enumerate(nums1[:count]):
            if n > max1:
                max1 = n
                max1i = i
                if max1 == 9:
                    break
        for i, n in enumerate(nums2[:count]):
            if n > max2:
                max2 = n
                max2i = i
                if max2 == 9:
                    break
        # print(max1, max2, max1i, max2i)

        if max1 > max2:
            return [max1] + self.maxNumber(nums1[max1i+1:], nums2, k-1)
        elif max1 < max2:
            return [max2] + self.maxNumber(nums1, nums2[max2i+1:], k-1)
        else:
            a = [max1] + self.maxNumber(nums1[max1i+1:], nums2, k-1)
            b = [max2] + self.maxNumber(nums1, nums2[max2i+1:], k-1)
            for i in range(k-1):
                if a[i] > b[i]:
                    return a
                elif a[i] < b[i]:
                    return b
            return a

s = Solution()
print(s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), [9, 8, 6, 5, 3])
print(s.maxNumber([6,7], [6,0,4], 5), [6,7,6,0,4])
print(s.maxNumber([3,9], [8,9], 3), [9,8,9])

s1 = [4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2]
s2 = [9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
print(s.maxNumber(s1, s2, 60))