"""
the most difficult problem I've encountered so far
dp used doesn't make intuitive sense.
it's observed from how coins are calculated
eg [3,1,5,8] -> coins =  3*1*5 +  3*5*8 + 1*3*8 + 1*8*1 = 167
3*1*5 - no dp, uses nums calculation, 
3*5*8 - length 2 - will use dp from previous & uses nums calc size 2 (thus 3*1*5 +  3*5*8)
, 1*3*8 - size 3 (thus 1 & 8 for calc) & dp from previous calc (thus 3*1*5 +  3*5*8 + 1*3*8)

the i is the last balloon popped because it divides the left and right balloons
thus allowing divide and conquer and dp
"""
from typing import List

class Solution:
    def maxCoins(self, nums):
        nlen = len(nums)
        nums = [1] + nums + [1]

        dp = [[0] * (nlen+2) for _ in range(nlen+2)]

        for length in range(1, nlen+1):
            for start in range(1, nlen - length + 2):
                end = start + length - 1
                
                maxcoins = 0
                for i in range(start, end+1):
                    c = dp[start][i-1] + dp[i+1][end] + nums[start-1] * nums[end+1] * nums[i]
                    maxcoins = max(maxcoins, c)
                dp[start][end] = maxcoins
        return dp[1][nlen]

s = Solution()
print(s.maxCoins([3,1,5,8]))
print(s.maxCoins([3,9,6,5,7,8]))