from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nlist = [[],]

        tempnlist = []

        nlen = len(nums)
        ncount = 0

        for i in range(nlen):
            n = nums[i]

            if i < nlen - 1 and nums[i+1] == n and (i == 0 or nums[i-1] != n):
                tempnlist.clear()
                ncount = 0
                for i in range(len(nlist)-1, -1, -1):
                    a = nlist[i] + [n,]
                    tempnlist.append(a)
                    nlist.append(a)
            elif i > 0 and nums[i-1] == n:
                ncount += 1
                for a in tempnlist:
                    nlist.append(a + [n] * ncount)
            else:
                for i in range(len(nlist)-1, -1, -1):
                    nlist.append(nlist[i] + [n,])
        return nlist

s = Solution()
print(s.subsetsWithDup([1,1]))