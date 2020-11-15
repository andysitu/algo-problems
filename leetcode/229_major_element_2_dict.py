class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nlimit = (len(nums) // 3) + 1
        
        nlist = []
        ntimes = {}
        for n in nums:
            if n not in ntimes:
                ntimes[n] = 0
            if ntimes[n] == -1:
                continue
            ntimes[n] += 1
            if ntimes[n] >= nlimit:
                nlist.append(n)
                ntimes[n] = -1
        return nlist