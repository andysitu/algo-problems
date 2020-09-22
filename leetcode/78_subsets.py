from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        numslen = len(nums)

        nlists = [[],]

        for i in range(numslen):
            n = nums[i]
            nlen = len(nlists)
            for j in range(nlen-1, -1, -1):
                nlists.append(nlists[j] + [n,])
        return nlists

s = Solution()
print(s.subsets([1,2,3]))
print(s.subsets([]))
print(s.subsets([1]))
print(s.subsets([1,2,3,4,5,6,7,8,9,10]))