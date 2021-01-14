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