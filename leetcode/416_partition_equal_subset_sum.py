from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = 0
        for n in nums:
            goal += n
        if goal % 2 != 0:
            return False
        goal //= 2

        nlen = len(nums)

        dp = [[False] * (goal+1) for _ in range(nlen+1)]

        for i in range(nlen+1):
            dp[i][0] = True

        # i is # of items used, so actual index = i-1
        for i in range(1, nlen+1):
            for j in range(1, goal+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[nlen][goal]


s = Solution()
print(s.canPartition([1,5,11,5]))