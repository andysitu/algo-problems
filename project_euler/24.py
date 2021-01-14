from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        self.dfs(nums, [], output)
        return output
        
    def dfs(self, nums, path, output):
        if not nums:
            output.append(path)
            
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], output)

s = Solution()
print(s.permute([0,1,2,3,4,5,6,7,8,9])[999999])