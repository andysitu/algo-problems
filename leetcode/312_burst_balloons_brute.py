from typing import List

class Solution:
    def solve(self, nums):
        if len(nums) == 2:
            return 0
        s = " ".join(str(x) for x in nums)
        if s in self.ndict:
            return self.ndict[s]

        m = 0
        for i in range(1, len(nums)-1):
            m=max(m, nums[i] * nums[i-1] * nums[i+1] + self.solve(nums[:i] + nums[i+1:]))
        self.ndict[s] = m
        return m
        

    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums.insert(0, 1)
        self.ndict = {}
        self.solved = set()
        return self.solve(nums)

s = Solution()
print(s.maxCoins([3,1,5,8]))