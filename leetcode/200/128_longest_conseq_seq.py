from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ndict = {}

        maxlen = 0
        for n in nums:
            if n in ndict:
                continue
            start, end = n, n
            if n - 1 in ndict:
                start = ndict[n-1]
            if n + 1 in ndict:
                end = ndict[n+1]
            ndict[n] = n
            ndict[start] = end
            ndict[end] = start
            if end-start + 1 > maxlen:
                maxlen = end-start + 1
            maxlen = max(end-start+1, maxlen)
        return maxlen
            
s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2, 6, 100, 7, 42, 11, 42, 32, 10, 42, 9, 42, 8]))
print(s.longestConsecutive([-6,6,-9,-7,0,3,4,-2,2,-1,9,-9,5,-3,6,1,5,-1,-2,9,-9,-4,-6,-5,6,-1,3]))