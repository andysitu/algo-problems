class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        nlen = len(nums)
        if nlen == 0:
            return 0
        
        nmax = 1
        for i in range(nlen-2, -1, -1):
            tmax = 1
            for j in range(i+1, nlen):
                if nums[i] >= nums[j]:
                    continue
                tmax = max(tmax, dp[j]+1)
            dp[i] = tmax
            nmax = max(nmax, tmax)
        return nmax