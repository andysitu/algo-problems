from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        nmap = {}
        nmax = 0
        nptr = None
        nlen = len(nums)
        for i in range(nlen):
            n = nums[i]
            if n not in nmap:
                for j in range(i+1, nlen):
                    if nums[j] % n == 0 and nums[j] not in nmap:
                        nmap[nums[j]] = [n, nums[j]]
            else:
                for j in range(i+1, nlen):
                    # print(n, nums[j], nmap[n])
                    if nums[j] % n == 0:
                        if nums[j] in nmap:
                            if len(nmap[n]) + 1 > len(nmap[nums[j]]):
                                nmap[nums[j]] = nmap[n] +  [nums[j]]
                        else:
                            nmap[nums[j]] = nmap[n] +  [nums[j]]
        for n in nmap:
            if len(nmap[n]) > nmax:
                nmax = len(nmap[n])
                nptr = nmap[n]
        if nptr == None:
            return [nums[0]]
        return nptr

s = Solution()
print(s.largestDivisibleSubset([1,2,4,8]),4)
print(s.largestDivisibleSubset([1,2,3]),2)
print(s.largestDivisibleSubset([2,3]),1)
print(s.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]),6)
print(s.largestDivisibleSubset([1,2,4,8,9,72]),5)