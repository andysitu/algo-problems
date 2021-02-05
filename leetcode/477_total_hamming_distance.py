class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        onecount = [0] * 30
        nlen = len(nums)
        maxl = 0
        for n in nums:
            bbin = bin(n)
            l = len(bbin)
            maxl = max(l, maxl)
            for i in range(2, l):
                if bbin[i] == '1':
                    onecount[l - i-1] += 1
        total = 0
        for i in range(maxl-2):
            total += (onecount[i] * (nlen-onecount[i]))
        return total