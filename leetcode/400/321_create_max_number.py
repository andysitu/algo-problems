from typing import List

class Solution:
    def maxNum1(self, nums, k):
        if k == 0:
            return []
        a = []
        nlen = len(nums)
        i = 0
        for remaining in range(k, 0, -1):
            count = nlen - remaining + 1 - i 
            maxn = nums[i]
            maxi = i
            for c in range(i,i+count):
                if nums[c] > maxn:
                    maxn = nums[c]
                    maxi = c
            a.append(maxn)
            i = maxi+1
        return a

        
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        maxn = []
        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(max(0, k - len2), min(k+1, len1+1)):
            a = []
            l = self.maxNum1(nums1, i)
            r = self.maxNum1(nums2, k-i)
            while l or r:
                if l > r:
                    a.append(l[0])
                    l = l[1:]
                else:
                    a.append(r[0])
                    r = r[1:]
            maxn = max(maxn, a)
        return maxn

s = Solution()
print(s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), [9, 8, 6, 5, 3])
print(s.maxNumber([6,7], [6,0,4], 5), [6,7,6,0,4])
print(s.maxNumber([3,9], [8,9], 3), [9,8,9])