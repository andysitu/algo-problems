class Solution:
    def rob(self, nums: List[int]) -> int:
        nlen = len(nums)

        if nums == None or nlen == 0:
            return 0
        if nlen == 1:
            return nums[0]
        if nlen == 2:
            return max(nums[1], nums[0])
        

        dp = [0] * nlen
        dp[nlen-1], dp[nlen-2] = nums[nlen-1], nums[nlen-2]
        dp[nlen-3] = dp[nlen-1] + nums[nlen-3]
        for i in range(nlen-4, -1, -1):
            dp[i] = max(dp[i+2], dp[i+3]) + nums[i]
        return max(dp[0], dp[1])